#!/usr/bin/env python3
"""Check the current distribution and preserved sources after T-WIN-004.

The original migration manifest and verifier remain historical evidence.
No installation, personal configuration access, or network is performed.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from urllib.parse import unquote, urlsplit


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
    counts = {'skills': 0, 'source_and_preserved_hashes': 0, 'local_links': 0,
              'python_syntax': 0, 'isolated_helper_runs': 0}
    for item in history['files'] + history['settings']:
        saved = relocated.get(item['preserved'])
        if saved and saved['sha256'] != item['sha256']:
            raise ValueError('Relocation hash differs from historical source')
        preserved = saved['preserved'] if saved else item['preserved']
        for path in (item['source'], preserved):
            if digest(path) != item['sha256']:
                raise ValueError(f'Preserved source changed: {path}')
            counts['source_and_preserved_hashes'] += 1
        active = item['active']
        if active == 'codex_windows/personal/AGENTS.md':
            active = 'codex_windows/AGENTS.md'
        inside(active)
    root = repo / 'codex_windows/skills'
    folders = sorted(root.glob('*/SKILL.md'))
    if len(folders) != 19 or [p.parent.name for p in folders] != history['skills']:
        raise ValueError('Current skill inventory differs')
    for entry in folders:
        folder = entry.parent
        if any(p.is_symlink() for p in folder.rglob('*')):
            raise ValueError('Skill contains a symbolic link')
        content = entry.read_text(encoding='utf-8')
        if not content.startswith('---\n') or not re.search(r'^name: ' + re.escape(folder.name) + '$', content, re.M):
            raise ValueError('Invalid skill metadata')
        if not re.search(r'^description: .+', content, re.M):
            raise ValueError('Missing skill description')
        # Current compatibility block and its own operational references only.
        # Legacy documents contain historical, intentionally unresolved examples.
        documents = [entry, *sorted((folder / 'references/windows').glob('*.md'))]
        for document in documents:
            text = document.read_text(encoding='utf-8')
            if document == entry:
                match = re.search(r'<!-- CODEX-COMPAT-BEGIN -->(.*?)<!-- CODEX-COMPAT-END -->', text, re.S)
                if not match:
                    raise ValueError('Missing current compatibility block')
                text = match.group(1)
            text = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text, flags=re.M | re.S)
            for target in re.findall(r'\]\(([^)\n]+)\)', text):
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                path = (document.parent / unquote(parts.path)).resolve()
                if not path.is_relative_to(folder) or not path.is_file():
                    raise ValueError(f'Broken standalone dependency: {folder.name}/{document.name}')
                counts['local_links'] += 1
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
    for name in ('md-link-check.py', 'md-heading-check.py', 'md-style-check.py', 'md_common.py', 'lock.py', 'script_template.py', 'script_template.sh'):
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
