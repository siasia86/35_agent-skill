"""Native Markdown CLI regression fixtures; no repository writes or installs.

python -X utf8 -B test_markdown.py --skills <codex_windows/skills> --output results.json
Optional --raw-output is for private TEMP diagnostics only; public JSON has no paths/stdout.
"""
import argparse
from contextlib import contextmanager
import json
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import uuid


@contextmanager
def fixture_directory():
    """Use inherited TEMP access; Python 3.14's mode-700 ACL is unsuitable
    for the app's split host/sandbox identity. Only non-sensitive fixtures live here.
    """
    base = Path(tempfile.gettempdir()).resolve()
    target = base / ('codex-md-native-fixtures-' + uuid.uuid4().hex)
    target.mkdir()
    try:
        yield target
    finally:
        resolved = target.resolve()
        if resolved.parent != base or not resolved.name.startswith('codex-md-native-fixtures-'):
            raise RuntimeError('Fixture cleanup escaped the intended TEMP directory')
        shutil.rmtree(resolved)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    targets = parser.add_mutually_exclusive_group(required=True)
    targets.add_argument('--skills', type=Path)
    targets.add_argument('--repo', type=Path)
    targets.add_argument('--scripts', type=Path, help='Canonical draft scripts for development')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--raw-output', type=Path, help='Private TEMP diagnostics, never publish')
    parser.add_argument('--cross-drive-cwd', type=Path, help='Existing read-only directory on another Windows drive')
    parser.add_argument('--cross-drive-file', type=Path, help='Existing read-only Markdown file on another Windows drive')
    args = parser.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    scripts = args.scripts or ((args.repo / 'codex_windows' / 'skills') if args.repo else args.skills) / 'md-link-check' / 'scripts'
    scripts = scripts.resolve()
    for name in ('md-link-check.py', 'md-heading-check.py', 'md-style-check.py', 'md_common.py'):
        if not (scripts / name).is_file():
            parser.error('Required standalone Markdown helper is missing: ' + name)
    results = []
    raw = []
    with fixture_directory() as temp:
        root = Path(temp)

        def write(name, content, crlf=False):
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content.replace('\n', '\r\n').encode('utf-8') if crlf else content.encode('utf-8'))
            return target

        def run(case, tool, expected, *arguments, cwd=None, expected_stdout=None, expected_metrics=None, expected_lines=None):
            command = [sys.executable, '-X', 'utf8', '-B', str(scripts / tool), *map(str, arguments)]
            process = subprocess.run(command, cwd=cwd or root, encoding='utf-8', capture_output=True, timeout=30)
            passed = process.returncode == expected and 'Traceback (most recent call last)' not in process.stderr
            if expected_stdout is not None:
                passed = passed and expected_stdout in process.stdout
            results.append({'case': case, 'tool': tool, 'expected_status': expected,
                            'actual_status': process.returncode, 'passed': passed})
            if expected_metrics is not None:
                metrics = {}
                for key, pattern in {
                    'files': r'검사 파일:\s*(\d+)개',
                    'links': r'\| 링크:\s*(\d+)개',
                    'broken_links': r'깨진 링크:\s*(\d+)건',
                    'headings': r'헤딩:\s*(\d+)개',
                    'issues': r'이슈:\s*(\d+)건',
                }.items():
                    match = re.search(pattern, process.stdout)
                    if match:
                        metrics[key] = int(match.group(1))
                results[-1].update({'expected_metrics': expected_metrics, 'actual_metrics': metrics})
                results[-1]['passed'] = results[-1]['passed'] and all(metrics.get(key) == value for key, value in expected_metrics.items())
            if expected_lines is not None:
                actual_lines = [int(value) for value in re.findall(r'L(\d+):', process.stdout)]
                results[-1].update({'expected_lines': expected_lines, 'actual_lines': actual_lines})
                results[-1]['passed'] = results[-1]['passed'] and actual_lines == expected_lines
            if case.endswith('-version'):
                actual_version = process.stdout.strip().rsplit(' ', 1)[-1]
                results[-1].update({'expected_version': expected_stdout,
                                    'actual_version': actual_version})
                results[-1]['passed'] = results[-1]['passed'] and actual_version == expected_stdout
            if args.raw_output:
                raw.append({'case': case, 'command': command, 'stdout': process.stdout, 'stderr': process.stderr})

        # Valid destinations exercise native spaces, Korean, URL encoding, CRLF,
        # optional titles, escaped punctuation, and nested balanced parentheses.
        write('My Report.md', '# Report\n')
        write('report(1).md', '# Report\n')
        write('deep(one(two)).md', '# Deep\n')
        write("author's.md", '# Author\n')
        write('한글 문서.md', '# 한국어\n')
        write('hash#report.md', '# Hash\n')
        good = write('유효 문서.md', '''# Document
[Angle](<My Report.md>)
[Angle title](<My Report.md> "Report title")
[Balanced](report(1).md)
[Nested](deep(one(two)).md)
[Escaped](report\\(1\\).md)
[Apostrophe](author's.md)
[Encoded](%ED%95%9C%EA%B8%80%20%EB%AC%B8%EC%84%9C.md)
[Encoded hash](hash%23report.md#section)
[Title](report(1).md 'Title')
[External](https://example.invalid/a(b))
[Anchor](#document)
`[Inline](absent-inline.md)`
''', crlf=True)
        missing = root / '명시한 미존재.md'
        broken = write('broken.md', '# Document\n[Missing](absent-file.md)\n')
        mixed_code = write('fences.md', '''# Document
> ```text
> [Missing](absent-quoted-code.md)
> # Hidden
> ```
~~~text
[Missing](absent-tilde-code.md)
# Hidden
~~~
````markdown
```text
[Missing](absent-inner-code.md)
```
~~~
# Hidden
````
''')
        code_then_broken = write('code-then-broken.md', mixed_code.read_text(encoding='utf-8') + '[Missing](after-fence.md)\n')
        unclosed = write('unclosed.md', '# Document\n~~~text\n[Hidden](hidden.md)\n')
        bad_utf8 = root / 'bad-encoding.md'
        bad_utf8.write_bytes(b'# Document\n\xff\xfe\n')
        run('link-valid-native-crlf-destinations', 'md-link-check.py', 0, '-v', good)
        # No selected Markdown is incomplete (2), not a scanned broken link (1).
        run('link-explicit-missing', 'md-link-check.py', 2, missing)
        run('link-valid-plus-missing', 'md-link-check.py', 1, good, missing)
        run('link-broken', 'md-link-check.py', 1, broken)
        broken_angle = write('broken-angle.md', '# Document\n[Missing](<missing report.md> "Title")\n')
        broken_nested = write('broken-nested.md', '# Document\n[Missing](missing(one(two)).md)\n')
        broken_encoded = write('broken-encoded.md', '# Document\n[Missing](%ED%95%9C%EA%B8%80%20missing.md)\n')
        run('link-angle-missing-detected', 'md-link-check.py', 1, broken_angle)
        run('link-balanced-parenthesis-missing-detected', 'md-link-check.py', 1, broken_nested)
        run('link-url-decoded-missing-detected', 'md-link-check.py', 1, broken_encoded)
        run('link-quote-tilde-long-fences', 'md-link-check.py', 0, mixed_code)
        run('link-after-fence-still-checked', 'md-link-check.py', 1, code_then_broken)
        run('link-unclosed-is-incomplete', 'md-link-check.py', 2, unclosed)
        run('link-invalid-utf8', 'md-link-check.py', 1, bad_utf8)
        run('link-version', 'md-link-check.py', 0, '--version', expected_stdout='26.10.03')
        run('link-help', 'md-link-check.py', 0, '--help')

        anchor_flags = ['--no-number', '--no-level', '--no-duplicate', '--no-toc']
        dup = write('duplicate.md', '# Root\n[Second](#overview-1)\n## Overview\n## Overview\n')
        collisions = write('collision.md', '# Root\n[Third](#overview-2)\n## Overview\n## Overview-1\n## Overview\n')
        dup_policy = write('duplicate-policy.md', '# Root\n[First](#overview)\n## Overview\n## Overview\n')
        wrong_anchor = write('wrong-anchor.md', '# Root\n[Missing](#absent)\n')
        numbering = write('numbering.md', '# Root\n## 1. First\n## 3. Third\n')
        levels = write('levels.md', '# Root\n#### Jump\n')
        toc_valid = write('toc-valid.md', '# Root\n## 목차\n[First](#1-first)\n## 1. First\n')
        toc_missing = write('toc-missing.md', '# Root\n## 목차\n## 1. First\n')
        run('heading-valid-native-crlf', 'md-heading-check.py', 0, *anchor_flags, good)
        run('heading-duplicate-suffix-anchor-only', 'md-heading-check.py', 0, *anchor_flags, dup)
        run('heading-suffix-collision-anchor-only', 'md-heading-check.py', 0, *anchor_flags, collisions)
        wrong_suffix = write('wrong-suffix.md', '# Root\n[Absent](#overview-9)\n## Overview\n## Overview\n')
        run('heading-nonexistent-duplicate-suffix', 'md-heading-check.py', 1, *anchor_flags, wrong_suffix)
        run('heading-duplicate-policy-preserved', 'md-heading-check.py', 1, '--no-number', '--no-level', '--no-toc', dup_policy)
        run('heading-explicit-missing', 'md-heading-check.py', 1, missing)
        run('heading-valid-plus-missing', 'md-heading-check.py', 1, *anchor_flags, good, missing)
        run('heading-all-checks-skipped-missing', 'md-heading-check.py', 1, *anchor_flags, '--no-anchor', missing)
        run('heading-invalid-anchor', 'md-heading-check.py', 1, *anchor_flags, wrong_anchor)
        run('heading-numbering-preserved', 'md-heading-check.py', 1, '--no-anchor', '--no-duplicate', '--no-toc', numbering)
        run('heading-level-policy-preserved', 'md-heading-check.py', 1, '--no-number', '--no-anchor', '--no-duplicate', '--no-toc', levels)
        run('heading-toc-valid', 'md-heading-check.py', 0, toc_valid)
        run('heading-toc-missing', 'md-heading-check.py', 1, toc_missing)
        run('heading-quote-tilde-long-fences', 'md-heading-check.py', 0, *anchor_flags, mixed_code)
        run('heading-invalid-utf8', 'md-heading-check.py', 1, bad_utf8)
        run('heading-version', 'md-heading-check.py', 0, '--version', expected_stdout='26.10.03')
        run('heading-help', 'md-heading-check.py', 0, '--help')
        heading_config = write('heading-config/.md-heading-check.toml', 'skip_checks = ["number", "level", "duplicate", "toc"]\n')
        configured = write('heading-config/document.md', '# Root\n## Unnumbered\n')
        run('heading-auto-toml-config', 'md-heading-check.py', 0, configured)
        run('heading-explicit-toml-config', 'md-heading-check.py', 0, '-c', heading_config, configured)
        config_invalid = write('invalid.toml', 'unknown = true\n')
        run('heading-invalid-config', 'md-heading-check.py', 1, '-c', config_invalid, configured)
        write('heading-exclude/ignored/bad.md', wrong_anchor.read_text(encoding='utf-8'))
        write('heading-exclude/document.md', '# Root\n')
        run('heading-directory-exclusion', 'md-heading-check.py', 0, '-E', 'ignored', root / 'heading-exclude')
        write('heading-file-skip/.md-heading-check.toml', '[[file_skip]]\npath = "document.md"\nchecks = ["anchor"]\nreason = "fixture"\n')
        configured_bad = write('heading-file-skip/document.md', '# Root\n[Absent](#absent)\n')
        run('heading-file-skip-preserved', 'md-heading-check.py', 0, '-v', configured_bad)

        clean_style = write('style-한글.md', '# 한국어 문서\n\n한국어 문서입니다.\n', crlf=True)
        style_fences = write('style-fences.md', '''# Document
> ~~~text
> # Hidden
> [Missing](absent.md)
> ~~~
~~~~text
```
# Hidden
~~~
~~~~
''')
        style_h1 = write('style-two-h1.md', '# Root\n# Second\n')
        run('style-native-utf8-crlf', 'md-style-check.py', 0, '--no-footer', clean_style)
        run('style-quote-tilde-mixed-fences', 'md-style-check.py', 0, '--no-footer', style_fences)
        run('style-h1-policy-preserved', 'md-style-check.py', 1, '--no-footer', style_h1)
        run('style-h1-cli-skip-preserved', 'md-style-check.py', 0, '--no-footer', '--no-h1', style_h1)
        run('style-explicit-missing', 'md-style-check.py', 1, '--no-footer', missing)
        run('style-valid-plus-missing', 'md-style-check.py', 1, '--no-footer', clean_style, missing)
        run('style-invalid-utf8', 'md-style-check.py', 1, '--no-footer', bad_utf8)
        run('style-version', 'md-style-check.py', 0, '--version', expected_stdout='26.10.05')
        run('style-help', 'md-style-check.py', 0, '--help')
        run('style-list-skips', 'md-style-check.py', 0, '--list-skips')
        write('style-config/.md-style-check.toml', 'skip_checks = ["footer"]\n')
        style_configured = write('style-config/document.md', '# Root\n')
        run('style-auto-toml-config', 'md-style-check.py', 0, style_configured)
        run('style-explicit-toml-config', 'md-style-check.py', 0, '--config', root / 'style-config/.md-style-check.toml', style_configured)
        run('style-invalid-config', 'md-style-check.py', 1, '--config', config_invalid, style_configured)
        reference = write('_reference/자료.md', '---\nsources: []\nlast_checked: 2026-10-03\n---\n# Reference\n')
        reference_missing = write('_reference/자료 오류.md', '# Reference\n')
        run('style-native-reference-path', 'md-style-check.py', 0, reference)
        run('style-reference-required-metadata', 'md-style-check.py', 1, reference_missing)
        write('style-exclude/document.md', '# Root\n')
        write('style-exclude/ignored/document.md', '# Root\n# Error\n')
        run('style-directory-exclusion', 'md-style-check.py', 0, '--no-footer', '-E', 'ignored', root / 'style-exclude')
        run('style-strict-preserved', 'md-style-check.py', 0, '--strict', '--no-footer', clean_style)

        # W04: escaped opening brackets depend on the parity of the backslash run.
        for count, expected in ((1, 0), (2, 1), (3, 0), (4, 1)):
            escaped_link = write(f'w04-backslashes-{count}.md', '# Root\n' + '\\' * count + '[Broken](absent.md)\n')
            metrics = {'files': 1, 'links': expected, 'broken_links': expected}
            run(f'w04-backslash-parity-{count}', 'md-link-check.py', expected, escaped_link, expected_metrics=metrics)

        # W05: only equal-length runs close inline code; real links still count.
        inline_double = write('w05-inline-double.md', '# Root\n``prefix ` [literal](absent.md) suffix``\n')
        run('w05-code-span-inner-shorter-run', 'md-link-check.py', 0, inline_double,
            expected_metrics={'files': 1, 'links': 0, 'broken_links': 0})
        inline_then_real = write('w05-inline-then-real.md', inline_double.read_text(encoding='utf-8') + '[Broken](outside.md)\n')
        run('w05-real-link-after-code-span', 'md-link-check.py', 1, inline_then_real,
            expected_metrics={'files': 1, 'links': 1, 'broken_links': 1}, expected_lines=[3])
        unmatched_inline = write('w05-unmatched-inline.md', '# Root\n``literal [Broken](absent.md)\n')
        run('w05-unmatched-run-keeps-real-link', 'md-link-check.py', 1, unmatched_inline,
            expected_metrics={'files': 1, 'links': 1, 'broken_links': 1})
        anchor_literal = write('w05-anchor-literal.md', '# Root\n`[literal](#absent)`\n')
        run('w05-inline-anchor-literal', 'md-heading-check.py', 0, *anchor_flags, anchor_literal,
            expected_metrics={'files': 1, 'headings': 1, 'issues': 0})
        literal_then_real = write('w05-anchor-then-real.md', anchor_literal.read_text(encoding='utf-8') + '[Broken](#outside)\n')
        run('w05-real-anchor-after-code-span', 'md-heading-check.py', 1, *anchor_flags, literal_then_real,
            expected_metrics={'files': 1, 'headings': 1, 'issues': 1}, expected_lines=[3])
        code_heading = write('w05-code-heading.md', '# Root\n[API](#api_name)\n## `api_name`\n')
        run('w05-heading-code-text-preserved', 'md-heading-check.py', 0, *anchor_flags, code_heading,
            expected_metrics={'files': 1, 'headings': 2, 'issues': 0})
        duplicate_literal = write('w05-duplicate-literal.md', '# Root\n`[literal](#overview)`\n## Overview\n## Overview\n')
        run('w05-literal-does-not-activate-duplicate-policy', 'md-heading-check.py', 0,
            '--no-number', '--no-level', '--no-toc', duplicate_literal,
            expected_metrics={'files': 1, 'headings': 3, 'issues': 0})

        # W06: Linux-style relative separators remain valid on native Windows.
        write('w06-exclude/document.md', '# Root\n')
        write('w06-exclude/nested/ignored/bad.md', '# Root\n[Bad](#absent)\n')
        for label, exclusion in (('forward', 'nested/ignored'), ('native', str(Path('nested') / 'ignored'))):
            run(f'w06-relative-exclusion-{label}', 'md-heading-check.py', 0, *anchor_flags,
                '-E', exclusion, root / 'w06-exclude', expected_metrics={'files': 1, 'headings': 1, 'issues': 0})
        write('w06-config/.md-heading-check.toml', 'exclude_dirs = ["nested/ignored"]\n')
        write('w06-config/document.md', '# Root\n')
        write('w06-config/nested/ignored/bad.md', '# Root\n[Bad](#absent)\n')
        run('w06-relative-exclusion-toml', 'md-heading-check.py', 0, *anchor_flags, root / 'w06-config',
            expected_metrics={'files': 1, 'headings': 1, 'issues': 0})

        # W07: encoded fragments apply consistently to anchors, TOC, and policy.
        encoded_anchor = write('w07-encoded-anchor.md', '# Root\n[Target](#%ED%95%9C%EA%B8%80)\n## 한글\n')
        run('w07-encoded-korean-anchor', 'md-heading-check.py', 0, *anchor_flags, encoded_anchor,
            expected_metrics={'files': 1, 'headings': 2, 'issues': 0})
        encoded_missing = write('w07-encoded-missing.md', '# Root\n[Missing](#%ED%95%9C%EA%B8%80)\n')
        run('w07-encoded-missing-anchor-fails', 'md-heading-check.py', 1, *anchor_flags, encoded_missing,
            expected_metrics={'files': 1, 'headings': 1, 'issues': 1}, expected_lines=[2])
        encoded_toc = write('w07-encoded-toc.md', '# Root\n## 목차\n[Target](#1-%ED%95%9C%EA%B8%80)\n## 1. 한글\n')
        run('w07-encoded-toc-completeness', 'md-heading-check.py', 0, encoded_toc,
            expected_metrics={'files': 1, 'headings': 3, 'issues': 0})
        encoded_duplicate = write('w07-encoded-duplicate.md', '# Root\n[First](#%ED%95%9C%EA%B8%80)\n## 한글\n## 한글\n')
        run('w07-encoded-duplicate-policy-preserved', 'md-heading-check.py', 1,
            '--no-number', '--no-level', '--no-toc', encoded_duplicate,
            expected_metrics={'files': 1, 'headings': 3, 'issues': 1}, expected_lines=[4])
        encoded_suffix = write('w07-encoded-suffix.md', '# Root\n[Second](#%ED%95%9C%EA%B8%80-1)\n## 한글\n## 한글\n')
        run('w07-encoded-duplicate-suffix', 'md-heading-check.py', 0, *anchor_flags, encoded_suffix,
            expected_metrics={'files': 1, 'headings': 3, 'issues': 0})

        # W08: remove closing ATX syntax without removing literal escaped marks.
        closing_atx = write('w08-closing-atx.md', '# Root\n[Target](#overview)\n## Overview ##\n')
        run('w08-closing-atx-anchor', 'md-heading-check.py', 0, *anchor_flags, closing_atx,
            expected_metrics={'files': 1, 'headings': 2, 'issues': 0})
        closing_tab = write('w08-closing-tab.md', '# Root\n[Target](#overview)\n## Overview\t###\t\n')
        run('w08-closing-atx-tab-whitespace', 'md-heading-check.py', 0, *anchor_flags, closing_tab,
            expected_metrics={'files': 1, 'headings': 2, 'issues': 0})
        escaped_atx = write('w08-escaped-closing.md', '# Root\n[Target](#overview-)\n## Overview \\##\n')
        run('w08-escaped-hashes-remain-heading-text', 'md-heading-check.py', 0, *anchor_flags, escaped_atx,
            expected_metrics={'files': 1, 'headings': 2, 'issues': 0})

        # W09: classify excluded URI schemes without modifying local paths.
        for label, uri in (('https', 'HTTPS://example.invalid/a'), ('http', 'HtTp://example.invalid/a'), ('mail', 'MAILTO:person@example.invalid')):
            external = write(f'w09-external-{label}.md', '# Root\n[External](' + uri + ')\n')
            run(f'w09-scheme-case-{label}', 'md-link-check.py', 0, external,
                expected_metrics={'files': 1, 'links': 0, 'broken_links': 0})

        # W10: every line-numbered diagnostic points into the original source.
        style_line_control = write('w10-line-control.md', '# Document\n\n✅NoSpace\n')
        style_line_fenced = write('w10-line-fenced.md', '# Document\n```text\nsample\n```\n\n✅NoSpace\n')
        style_line_quoted = write('w10-line-quoted.md', '# Document\n> ~~~text\n> sample\n> ~~~\n\n✅NoSpace\n')
        for label, target, line in (('control', style_line_control, 3), ('fenced', style_line_fenced, 6), ('quoted-tilde', style_line_quoted, 6)):
            run(f'w10-original-line-{label}', 'md-style-check.py', 1, '--no-footer', target,
                expected_metrics={'files': 1, 'issues': 1}, expected_lines=[line])


        # The fixture remains on TEMP's drive. Change only subprocess cwd to an
        # existing directory on the other drive; never write that directory.
        cross_cwd = args.cross_drive_cwd
        if cross_cwd is None and sys.platform == 'win32' and scripts.drive != root.drive:
            cross_cwd = scripts.parent
        if cross_cwd is not None:
            cross_cwd = cross_cwd.resolve()
            if not cross_cwd.is_dir() or cross_cwd.drive == root.drive:
                parser.error('--cross-drive-cwd must be an existing directory on a different drive')
            run('cross-drive-cwd-link-valid-display', 'md-link-check.py', 0, '-v', good,
                cwd=cross_cwd, expected_stdout=good.name)
            run('cross-drive-cwd-link-broken-display', 'md-link-check.py', 1, broken,
                cwd=cross_cwd, expected_stdout=broken.name)
            run('cross-drive-cwd-link-unclosed-display', 'md-link-check.py', 2, unclosed, cwd=cross_cwd)
            run('cross-drive-cwd-heading-valid-display', 'md-heading-check.py', 0, '-v', *anchor_flags, good,
                cwd=cross_cwd, expected_stdout=good.name)
            run('cross-drive-cwd-heading-failure-display', 'md-heading-check.py', 1, *anchor_flags, wrong_anchor,
                cwd=cross_cwd, expected_stdout=wrong_anchor.name)
            run('cross-drive-cwd-style-valid-display', 'md-style-check.py', 0, '--no-footer', clean_style,
                cwd=cross_cwd, expected_stdout=clean_style.name)
            run('cross-drive-cwd-style-failure-display', 'md-style-check.py', 1, '--no-footer', style_h1,
                cwd=cross_cwd, expected_stdout=style_h1.name)

        # A user-supplied or current Windows usage README is read-only. These cases exercise
        # TEMP cwd -> existing other-drive file as well as absolute display.
        cross_file = args.cross_drive_file
        skills_root = ((args.repo / 'codex_windows/skills') if args.repo else args.skills)
        if cross_file is None and skills_root:
            candidate = skills_root.resolve().parent / 'README.md'
            if candidate.is_file() and candidate.drive != root.drive:
                cross_file = candidate
        if cross_file is not None:
            cross_file = cross_file.resolve()
            if not cross_file.is_file() or cross_file.drive == root.drive:
                parser.error('--cross-drive-file must be an existing file on a different drive')
            run('cross-drive-target-link-display', 'md-link-check.py', 0, '-v', cross_file,
                expected_stdout=cross_file.name)
            run('cross-drive-target-heading-display', 'md-heading-check.py', 0, '-v', cross_file,
                expected_stdout=cross_file.name)
            style_skips = ['--no-' + name for name in ('diagram-kr', 'diagram-width', 'table', 'emoji',
                           'emoji-disallow', 'banmal', 'exaggeration', 'footer', 'h1', 'box-chars',
                           'bold-paren', 'period', 'reference')]
            run('cross-drive-target-style-display', 'md-style-check.py', 0, *style_skips, cross_file,
                expected_stdout=cross_file.name)
            other_scripts = (skills_root / 'md-link-check/scripts') if skills_root else (cross_file.parent.parent / 'codex_windows/skills/md-link-check/scripts')
            if other_scripts.is_dir() and other_scripts.drive != root.drive:
                # An actual other-drive script directory contains no Markdown.
                # A normal no-input result must survive __file__ -> target drive mismatch.
                run('cross-drive-target-directory-no-input', 'md-style-check.py', 1, *style_skips, other_scripts,
                    expected_stdout='검사할 .md 파일이 없습니다.')

    summary = {'runtime': 'native-windows' if sys.platform == 'win32' else sys.platform,
               'cases': len(results),
               'baseline_cases': sum(not r['case'].startswith(tuple('w' + str(n).zfill(2) + '-' for n in range(4, 11))) for r in results),
               'new_cases': sum(r['case'].startswith(tuple('w' + str(n).zfill(2) + '-' for n in range(4, 11))) for r in results),
               'passed': sum(r['passed'] for r in results),
               'failed': sum(not r['passed'] for r in results), 'results': results}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.raw_output:
        args.raw_output.parent.mkdir(parents=True, exist_ok=True)
        args.raw_output.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in summary.items() if k != 'results'}, ensure_ascii=False))
    for result in results:
        if not result['passed']:
            print(result['case'], 'expected', result['expected_status'], 'actual', result['actual_status'])
    return int(summary['failed'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
