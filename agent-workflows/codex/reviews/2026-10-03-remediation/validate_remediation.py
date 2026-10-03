#!/usr/bin/env python3
"""Capture document, source-preservation and limited secret checks for this change."""
import argparse
import ast
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote

sys.dont_write_bytecode = True


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument('--baseline', type=Path, help='Initial tracked-file hash manifest, when available')
    parser.add_argument('--baseline-ref', default='f66b5b86212927b1913a798be46397ef45e1cafa',
                        help='Committed clean baseline when the temporary manifest is unavailable')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    report = {'commands': [], 'runtime': {'python': sys.version.split()[0]}, 'scope': {}}

    def run(argv):
        result = subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=30)
        report['commands'].append({'argv': argv, 'exit': result.returncode,
                                   'stdout': result.stdout, 'stderr': result.stderr})
        return result

    if args.baseline:
        baseline = json.loads(args.baseline.read_text())
    else:
        listed = run(['git', 'ls-tree', '-r', '--name-only', '-z', args.baseline_ref])
        if listed.returncode:
            raise RuntimeError('Cannot read baseline tree')
        hashes = {}
        for name in listed.stdout.split('\0'):
            if name:
                data = subprocess.check_output(['git', 'show', f'{args.baseline_ref}:{name}'], cwd=root)
                hashes[name] = hashlib.sha256(data).hexdigest()
        baseline = {'head': args.baseline_ref, 'hashes': hashes}
    changed = []
    missing = []
    for name, old_hash in baseline['hashes'].items():
        path = root / name
        if not path.is_file():
            missing.append(name)
        elif hashlib.sha256(path.read_bytes()).hexdigest() != old_hash:
            changed.append(name)
    new = run(['git', 'ls-files', '--others', '--exclude-standard', '-z']).stdout.split('\0')
    new = sorted(name for name in new if name)
    names = sorted(set(changed + new))
    report['scope'] = {
        'baseline_head': baseline['head'], 'baseline_files': len(baseline['hashes']),
        'changed_existing': changed, 'new_files': new, 'missing': missing,
        'unchanged_existing': len(baseline['hashes']) - len(changed) - len(missing),
        'protected_changes': [name for name in changed + missing
                              if name.startswith(('kiro/', 'gpt/', '105_backup/',
                                                  'agent-workflows/codex/pc01_codex-app-home/'))],
    }
    tools = root / 'codex/skills/md-link-check/scripts'
    style = load_module('remediation_style', tools / 'md-style-check.py')
    heading = load_module('remediation_heading', tools / 'md-heading-check.py')
    links = load_module('remediation_links', tools / 'md-link-check.py')
    documents = [name for name in names if name.endswith('.md')]
    report['documents'] = documents
    report['style'] = []
    with tempfile.TemporaryDirectory(prefix='skill-style-baseline-') as temp:
        for name in documents:
            path = root / name
            current_issues = style.check_file(str(path))
            if name.startswith('codex/skills/'):
                if path.name == 'SKILL.md':
                    source = root / 'kiro/skills' / path.parent.name / 'SKILL.md'
                elif path.parent.name in ('skills', 'originals'):
                    source = root / 'kiro/skills' / path.stem / 'SKILL.md'
                else:
                    raise ValueError('Unclassified skill document: ' + name)
                # Compare warnings after removing only line-number offsets.
                source_file = Path(temp) / 'source.md'
                source_file.write_bytes(source.read_bytes())
                previous = style.check_file(str(source_file))
                normalized = lambda issues: Counter((kind, re.sub(r'L\d+', 'L?', text))
                                                     for kind, text in issues)
                added = list((normalized(current_issues) - normalized(previous)).elements())
                report['style'].append({'file': name, 'raw_issues': current_issues,
                                        'source_issues': previous, 'added_issues': added})
            else:
                report['style'].append({'file': name, 'raw_issues': current_issues,
                                        'source_issues': [], 'added_issues': current_issues})

    heading_result = run(['python3', '-I', str(tools / 'md-heading-check.py'),
                          *[str(root / name) for name in documents]])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # The record links to its generated report; create it before the file-existence check.
    args.output.write_text('{"status": "running"}\n')
    link_result = run(['python3', '-I', str(tools / 'md-link-check.py'),
                       *[str(root / name) for name in documents]])
    anchors = []
    anchor_errors = []
    for name in documents:
        path = root / name
        clean = links.strip_code_blocks_preserve_lines(path.read_text(), str(path))
        for lineno, line in enumerate(clean.splitlines(), 1):
            for match in links.LINK_PATTERN.finditer(line):
                raw = match.group(2)
                if '#' not in raw or raw.startswith(('http://', 'https://', 'mailto:')):
                    continue
                target_part, _, fragment = raw.partition('#')
                target = path.parent / links.extract_link_path(target_part) if target_part else path
                fragment = unquote(re.split(r'\s+[\'"]', fragment)[0])
                if not fragment:
                    continue
                if target.suffix != '.md' or not target.is_file():
                    anchor_errors.append({'file': name, 'line': lineno, 'link': raw,
                                          'reason': 'missing Markdown target'})
                    continue
                target_clean = heading.strip_code_blocks(target.read_text())
                slug_counts = Counter()
                slugs = set()
                for _, title, _ in heading.extract_headings(target_clean):
                    base = heading.make_anchor(title)
                    suffix = slug_counts[base]
                    slugs.add(base if suffix == 0 else f'{base}-{suffix}')
                    slug_counts[base] += 1
                anchors.append({'file': name, 'line': lineno, 'link': raw})
                if fragment not in slugs:
                    anchor_errors.append({'file': name, 'line': lineno, 'link': raw,
                                          'reason': 'missing heading anchor'})
    report['anchors'] = {'checked': len(anchors), 'errors': anchor_errors}

    syntax = []
    for name in names:
        if name.endswith('.py'):
            ast.parse((root / name).read_text(), filename=name, feature_version=(3, 11))
            syntax.append(name)
    report['syntax'] = {'python_files': syntax, 'grammar': '3.11', 'errors': []}
    validator = '/root/.codex/skills/.system/skill-creator/scripts/quick_validate.py'
    validation = [run(['python3', validator, str(folder)])
                  for folder in sorted((root / 'codex/skills').iterdir()) if folder.is_dir()]
    report['frontmatter'] = {'skills': len(validation), 'failed': sum(r.returncode != 0 for r in validation)}
    diff = run(['git', 'diff', '--check'])
    cached = run(['git', 'diff', '--cached', '--stat'])
    head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
    report['scope']['head_unchanged'] = head == baseline['head']
    report['scope']['staged_diff_empty'] = not cached.stdout.strip()
    # These patterns are deliberately narrower than Gitleaks. Never expose matched values.
    patterns = {
        'aws_access_key': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
        'github_token': r'\bgh[pousr]_[A-Za-z0-9]{30,}\b',
        'openai_token': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{35,}\b',
        'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    }
    secret_findings = []
    report['non_utf8_files'] = []
    for name in names:
        data = (root / name).read_bytes()
        try:
            content = data.decode('utf-8')
        except UnicodeDecodeError:
            report['non_utf8_files'].append(name)
            # Still inspect ASCII credential markers without assuming a text encoding.
            content = data.decode('utf-8', errors='surrogateescape')
        for category, pattern in patterns.items():
            if re.search(pattern, content):
                secret_findings.append({'file': name, 'category': category})
    report['secret_scan'] = {'status': 'partial: regex only; Gitleaks unavailable',
                             'files': len(names), 'findings': secret_findings}
    regression = json.loads((root / 'agent-workflows/codex/reviews/2026-10-03-remediation/tests.json').read_text())
    mismatches = [name for name, digest in regression['inputs'].items()
                  if hashlib.sha256((root / name).read_bytes()).hexdigest() != digest]
    report['regression_inputs'] = {'hashes': len(regression['inputs']), 'mismatches': mismatches,
                                   'recorded_tests_passed': regression['passed']}
    report['json_files'] = [name for name in names if name.endswith('.json')]
    for name in report['json_files']:
        json.loads((root / name).read_text())
    report['style_added_issues'] = sum(len(row['added_issues']) for row in report['style'])
    report['style_raw_issues'] = sum(len(row['raw_issues']) for row in report['style'])
    report['passed_required_checks'] = not any((
        missing, report['scope']['protected_changes'], report['style_added_issues'],
        heading_result.returncode, link_result.returncode, anchor_errors,
        report['frontmatter']['failed'], diff.returncode, secret_findings,
        not report['scope']['head_unchanged'], not report['scope']['staged_diff_empty'],
        mismatches, not regression['passed']))
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ('style_added_issues', 'style_raw_issues',
                                                  'anchors', 'frontmatter', 'passed_required_checks')},
                     ensure_ascii=False))
    return 0 if report['passed_required_checks'] else 1


if __name__ == '__main__':
    sys.exit(main())
