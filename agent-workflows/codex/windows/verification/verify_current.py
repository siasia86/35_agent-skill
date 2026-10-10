#!/usr/bin/env python3
"""Check the current distribution and preserved sources after T-WIN-004.

The original migration manifest and verifier remain historical evidence.
No installation, personal configuration access, or network is performed.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib


NATIVE_RECORD = 'agent-workflows/codex/2026-10-10-windows-native-T-WIN-004'
NATIVE_MAP = NATIVE_RECORD + '/preservation-map.json'


def read_current_inventory(path):
    """Reviewed distribution contract; deliberately separate from migration history."""
    value = json.loads(path.read_text(encoding='utf-8'))
    skills = value.get('skills')
    if value.get('schema_version') != 1 or not isinstance(skills, dict) or not skills:
        raise ValueError('Invalid current inventory')
    for name, kind in skills.items():
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            raise ValueError('Invalid current inventory name')
        if kind not in ('compat', 'native'):
            raise ValueError('Invalid current inventory format')
    return skills


def current_entries(root, inventory):
    if not root.is_dir() or root.resolve() != root.absolute():
        raise ValueError('Missing or redirected skill root')
    actual = {p.name for p in root.iterdir() if p.is_dir() or p.is_symlink()}
    expected = set(inventory)
    if actual != expected:
        missing, extra = sorted(expected - actual), sorted(actual - expected)
        raise ValueError(f'Current skill inventory differs: missing={missing}, extra={extra}')
    entries = []
    for name in sorted(inventory):
        folder = root / name
        if folder.resolve() != folder.absolute():
            raise ValueError(f'Redirected skill folder: {name}')
        for path in folder.rglob('*'):
            if path.is_symlink() or path.resolve() != path.absolute():
                raise ValueError(f'Redirected skill dependency: {name}')
        entry = folder / 'SKILL.md'
        if not entry.is_file():
            raise ValueError(f'Missing skill entry: {name}')
        entries.append(entry)
    return entries


def string_scalar(value):
    """Required strings in the current single-line YAML schema, not a YAML parser."""
    value = value.strip()
    if value.startswith('"'):
        match = re.fullmatch(r'("(?:[^"\\]|\\.)*")(?:[ \t]+#.*)?', value)
        scalar = match[1][1:-1] if match else ''
        return scalar if scalar.strip() else None
    if value.startswith("'"):
        match = re.fullmatch(r"('(?:[^']|'')*')(?:[ \t]+#.*)?", value)
        scalar = match[1][1:-1].replace("''", "'") if match else ''
        return scalar if scalar.strip() else None
    value = re.split(r'(?:^|[ \t]+)#', value, maxsplit=1)[0].strip()
    if not value or value[0] in '[{!&*|>%' or value.endswith(':') or ': ' in value:
        return None
    if value.lower() in ('true', 'false', 'yes', 'no', 'null', '~') or re.fullmatch(r'[-+]?\d+(\.\d+)?', value):
        return None
    return value


def check_metadata(content, name):
    match = re.match(r'\A---\n(.*?)\n---(?:\n|\Z)', content, re.S)
    if not match:
        raise ValueError(f'Invalid skill frontmatter: {name}')
    required = {}
    for line in match.group(1).splitlines():
        field = re.fullmatch(r'(name|description):[ \t]*(.*)', line)
        if not field:
            raise ValueError(f'Unsupported current frontmatter field: {name}')
        key, value = field.groups()
        if key in required:
            raise ValueError(f'Duplicate skill metadata: {name}/{key}')
        required[key] = string_scalar(value)
    if required.get('name') != name:
        raise ValueError(f'Invalid skill metadata: {name}')
    if not required.get('description'):
        raise ValueError(f'Missing skill description: {name}')


def active_skill_body(content, kind):
    begin, end = '<!-- CODEX-COMPAT-BEGIN -->', '<!-- CODEX-COMPAT-END -->'
    if kind == 'native':
        if begin in content or end in content:
            raise ValueError('Native skill contains compatibility markers')
        return content
    if kind != 'compat' or content.count(begin) != 1 or content.count(end) != 1:
        raise ValueError('Missing or duplicate current compatibility block')
    first, last = content.index(begin), content.index(end)
    if first >= last:
        raise ValueError('Reversed current compatibility block')
    return content[first + len(begin):last]


def check_native_interface(folder):
    path = folder / 'agents/openai.yaml'
    if not path.is_file():
        raise ValueError(f'Missing native interface: {folder.name}')
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0] != 'interface:':
        raise ValueError(f'Invalid native interface: {folder.name}')
    fields, policy = {}, {}
    section = 'interface'
    for line in lines[1:]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line == 'policy:':
            if section == 'policy':
                raise ValueError(f'Duplicate native policy: {folder.name}')
            section = 'policy'
            continue
        if section == 'policy':
            match = re.fullmatch(r'  allow_implicit_invocation:[ \t]*(true|false)', line)
            if not match or policy:
                raise ValueError(f'Invalid native policy: {folder.name}')
            policy['allow_implicit_invocation'] = match[1] == 'true'
            continue
        match = re.fullmatch(r'  (display_name|short_description|default_prompt):[ \t]*(.*)', line)
        if not match or match[1] in fields:
            raise ValueError(f'Invalid native interface field: {folder.name}')
        fields[match[1]] = string_scalar(match[2])
    if set(fields) != {'display_name', 'short_description', 'default_prompt'} or not all(fields.values()):
        raise ValueError(f'Incomplete native interface: {folder.name}')
    if section == 'policy' and not policy:
        raise ValueError(f'Incomplete native policy: {folder.name}')
    if '$' + folder.name not in fields['default_prompt']:
        raise ValueError(f'Native prompt omits skill name: {folder.name}')


def check_windows_distribution(root):
    """Reject retired payloads and execution examples, not platform boundary prose."""
    legacy_names = {'linux-original.md', 'kiro-original.md', 'legacy-work-rules.md'}
    legacy_parts = {'linux-skills', 'linux-tools', 'originals', 'bash-script-template'}
    executable_patterns = re.compile(
        r'(?m)^\s*```(?:bash|sh|shell)\s*$|/root/|/mnt/[a-z]/|'
        r'\b(?:systemctl|journalctl|apt-get)\b|bash-script-template|'
        r'linux-original\.md|kiro-original\.md|legacy-work-rules\.md')
    for path in root.rglob('*'):
        if path.suffix == '.sh' or path.name in legacy_names or legacy_parts.intersection(path.relative_to(root).parts):
            raise ValueError(f'Retired Windows payload: {path.relative_to(root)}')
        if path.is_file() and path.suffix == '.md' and executable_patterns.search(path.read_text(encoding='utf-8')):
            raise ValueError(f'Non-native Windows instructions: {path.relative_to(root)}')


def markdown_helper(root):
    # Reuse the distribution's stdlib parser; no plugin or external package imports.
    path = root / 'md-link-check/scripts/md_common.py'
    spec = importlib.util.spec_from_file_location('current_md_common', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_links(document, content, folder, helper):
    prose, unclosed = helper.strip_fenced_code(content)
    if unclosed is not None:
        raise ValueError(f'Unclosed current Markdown fence: {folder.name}/{document.name}')
    count = 0
    for line in helper.mask_inline_code(prose).splitlines():
        for raw, destination in helper.iter_inline_links(line):
            # The helper already removes the raw fragment before decoding the path.
            # Splitting again would destroy encoded filename characters such as %23.
            if re.match(r'^\s*<?(?:[A-Za-z][A-Za-z0-9+.-]*:|//)', raw) or not destination:
                continue
            path = (document.parent / destination).resolve()
            if not path.is_relative_to(folder) or not path.is_file():
                raise ValueError(f'Broken standalone dependency: {folder.name}/{document.name}')
            count += 1
    return count


def verify(repo):
    def read_json(path):
        return json.loads(path.read_text(encoding='utf-8'))

    def inside(relative):
        target = (repo / relative).resolve()
        if not target.is_relative_to(repo) or not target.is_file():
            raise ValueError(f'Missing or unsafe source: {relative}')
        return target

    def digest(relative):
        return hashlib.sha256(inside(relative).read_bytes()).hexdigest()

    verification = repo / 'agent-workflows/codex/windows/verification'
    history = read_json(verification / 'source_manifest.json')
    routing = read_json(repo / 'agent-workflows/codex/2026-10-04-personal-routing-T-WIN-004/preservation-map.json')
    relocated = {item['before']: item for item in routing['relocated_preserved_files']}
    if len(relocated) != 7 or len(history['files']) != 182 or len(history['settings']) != 2:
        raise ValueError('Unexpected preservation inventory')
    native_map = read_json(repo / NATIVE_MAP)
    archived = {}
    for item in native_map['files']:
        original = 'codex_windows/' + item['source']
        if original in archived:
            raise ValueError('Duplicate native preservation source')
        target = NATIVE_RECORD + '/' + item['preserved']
        expected_prefix = NATIVE_RECORD + '/archive/codex_windows/'
        if not target.startswith(expected_prefix) or not re.fullmatch(r'[0-9a-f]{64}', item['sha256']):
            raise ValueError('Invalid native preservation record')
        path = inside(target)
        if not path.is_relative_to((repo / expected_prefix).resolve()):
            raise ValueError('Native preservation escapes archive')
        if digest(target) != item['sha256'] or path.stat().st_size != item['bytes']:
            raise ValueError(f'Native preserved file changed: {original}')
        for counterpart in item['linux_or_kiro_counterparts']:
            if digest(counterpart['path']) != counterpart['sha256']:
                raise ValueError(f'Native preservation counterpart changed: {original}')
            if not item['windows_only'] and counterpart['sha256'] != item['sha256']:
                raise ValueError(f'Native preservation counterpart differs: {original}')
        archived[original] = {'preserved': target, 'sha256': item['sha256']}
    if native_map['file_count'] != len(archived) or not archived:
        raise ValueError('Unexpected native preservation inventory')
    counts = {'skills': 0, 'compat_skills': 0, 'native_skills': 0,
              'historical_skills': len(history['skills']),
              'source_and_preserved_hashes': 0, 'local_links': 0,
              'native_interfaces': 0, 'python_syntax': 0, 'isolated_helper_runs': 0,
              'archived_files': len(archived), 'linux_tool_copies': 0}
    tool_sources, tool_targets = set(), set()
    for item in native_map['linux_script_copies']:
        if item['source'] in tool_sources or item['preserved'] in tool_targets:
            raise ValueError('Duplicate Linux tool preservation')
        tool_sources.add(item['source'])
        tool_targets.add(item['preserved'])
        saved = archived.get(item['source'])
        if not saved or saved['sha256'] != item['sha256']:
            raise ValueError('Linux tool preservation lacks archived source')
        target = inside(item['preserved'])
        if not item['preserved'].startswith('codex_linux/references/windows-migration/'):
            raise ValueError('Invalid Linux tool preservation target')
        if not target.is_relative_to((repo / 'codex_linux/references/windows-migration').resolve()):
            raise ValueError('Linux tool preservation escapes target')
        if target.stat().st_size != item['bytes'] or digest(item['preserved']) != item['sha256']:
            raise ValueError('Linux tool preservation changed')
        counts['linux_tool_copies'] += 1
    if len(tool_sources) != 2:
        raise ValueError('Unexpected Linux tool preservation inventory')
    for item in history['files'] + history['settings']:
        saved = relocated.get(item['preserved'])
        if saved and saved['sha256'] != item['sha256']:
            raise ValueError('Relocation hash differs from historical source')
        preserved = saved['preserved'] if saved else item['preserved']
        current_archive = archived.get(preserved)
        if current_archive:
            if current_archive['sha256'] != item['sha256']:
                raise ValueError('Native relocation hash differs from historical source')
            preserved = current_archive['preserved']
        for path in (item['source'], preserved):
            if digest(path) != item['sha256']:
                raise ValueError(f'Preserved source changed: {path}')
            counts['source_and_preserved_hashes'] += 1
        # `active` describes the migration at the time, not today's installed path.
        # Current dependencies are independently checked across all native folders.
    root = repo / 'codex_windows/skills'
    inventory = read_current_inventory(verification / 'current_inventory.json')
    if len(history['skills']) != 19 or len(set(history['skills'])) != 19:
        raise ValueError('Unexpected historical skill inventory')
    retired = set(native_map.get('retired_skills', []))
    if retired != {'bash-script-template'} or set(history['skills']) - retired - set(inventory):
        raise ValueError('Historical skill retirement differs')
    if len(inventory) != 21 or any(kind != 'native' for kind in inventory.values()) or retired.intersection(inventory):
        raise ValueError('Windows native inventory differs')
    folders = current_entries(root, inventory)
    check_windows_distribution(root)
    helper = markdown_helper(root)
    for entry in folders:
        folder = entry.parent
        content = entry.read_text(encoding='utf-8')
        check_metadata(content, folder.name)
        kind = inventory[folder.name]
        body = active_skill_body(content, kind)
        counts[kind + '_skills'] += 1
        if kind == 'native':
            check_native_interface(folder)
            counts['native_interfaces'] += 1
        # Current compatibility block and its own operational references only.
        # Legacy documents contain historical, intentionally unresolved examples.
        documents = ([entry, *sorted((folder / 'references/windows').glob('*.md'))]
                     if kind == 'compat' else sorted(folder.rglob('*.md')))
        for document in documents:
            text = body if document == entry else document.read_text(encoding='utf-8')
            counts['local_links'] += check_links(document, text, folder, helper)
        for script in (folder / 'scripts').glob('*.py'):
            ast.parse(script.read_text(encoding='utf-8'), filename=script.name)
            counts['python_syntax'] += 1
        with tempfile.TemporaryDirectory(prefix='current-skill-') as temporary:
            destination = Path(temporary) / 'standalone'
            shutil.copytree(folder, destination)
            for script in (destination / 'scripts').glob('*.py'):
                if script.name == 'md_common.py':
                    continue
                result = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(script), '--help'],
                                        cwd=temporary, capture_output=True, timeout=30)
                if result.returncode:
                    raise ValueError(f'Isolated helper failed: {folder.name}/{script.name}')
                counts['isolated_helper_runs'] += 1
        counts['skills'] += 1
    for name in ('md-link-check.py', 'md-heading-check.py', 'md-style-check.py', 'md_common.py', 'lock.py', 'script_template.py'):
        hashes = {hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob('*/scripts/' + name)}
        if len(hashes) != 1:
            raise ValueError(f'Helper copies differ or are missing: {name}')
    config = tomllib.loads((repo / 'codex_windows/personal/config.example.toml').read_text(encoding='utf-8'))
    shared = tomllib.loads((repo / '.codex/config.toml').read_text(encoding='utf-8'))
    if not all(config.get(key) == value for key, value in shared.items()) or config['windows']['sandbox'] != 'elevated':
        raise ValueError('Example configuration contract differs')
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[4])
    args = parser.parse_args()
    print(json.dumps({'status': 'PASS', 'counts': verify(args.repo.resolve())}))


if __name__ == '__main__':
    main()
