#!/usr/bin/env python3
"""Verify full Windows migration and standalone folders; no installation or network."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

COMPAT = re.compile(r'<!-- CODEX-COMPAT-BEGIN -->.*?<!-- CODEX-COMPAT-END -->', re.S)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return path.read_text(encoding='utf-8')


def cli(script, *arguments, cwd):
    return subprocess.run([sys.executable, '-X', 'utf8', '-B', str(script), *map(str, arguments)],
                          cwd=cwd, text=True, encoding='utf-8', capture_output=True,
                          timeout=30)


def verify(repo):
    root = repo / 'codex_windows'
    manifest = json.loads(read(root / 'verification/source_manifest.json'))
    counts = {'skills': 0, 'source_files_preserved': 0, 'bundled_workflows': 0,
              'compat_local_links': 0, 'python_scripts': 0, 'isolated_tool_runs': 0,
              'settings_sources': 0}
    names = manifest['skills']
    assert len(names) == 19 and len(set(names)) == 19
    assert sorted(p.parent.name for p in (root / 'skills').glob('*/SKILL.md')) == names
    assert sorted(p.parent.name for p in (repo / 'codex_linux/skills').glob('*/SKILL.md')) == names
    for entry in manifest['files']:
        assert sha(repo / entry['source']) == entry['sha256'], entry['source']
        assert sha(repo / entry['preserved']) == entry['sha256'], entry['preserved']
        assert (repo / entry['active']).is_file(), entry['active']
        counts['source_files_preserved'] += 1
    for entry in manifest['settings']:
        assert sha(repo / entry['source']) == entry['sha256'], entry['source']
        assert sha(repo / entry['preserved']) == entry['sha256'], entry['preserved']
        assert (repo / entry['active']).is_file()
        counts['settings_sources'] += 1
    for name in names:
        folder = root / 'skills' / name
        assert not any(p.is_symlink() for p in folder.rglob('*'))
        text = read(folder / 'SKILL.md')
        assert COMPAT.sub('', text) == COMPAT.sub('', read(repo / 'codex_linux/skills' / name / 'SKILL.md')), name
        assert (folder / 'references/kiro-original.md').read_bytes() == (repo / 'kiro/skills' / name / 'SKILL.md').read_bytes()
        documents = [folder / 'SKILL.md', *sorted((folder / 'references/skills').glob('*.md'))]
        for document in documents:
            content = read(document)
            blocks = COMPAT.findall(content)
            assert len(blocks) == 1 and 'Windows' in blocks[0], document
            metadata = content.split('---', 2)[1]
            assert re.search(r'^name: ' + re.escape(document.stem if document.name != 'SKILL.md' else name) + r'$', metadata, re.M)
            assert re.search(r'^description: .+', metadata, re.M)
            # Compatibility prose uses simple destinations; fenced examples are
            # excluded because placeholders are not dependencies.
            prose = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', blocks[0], flags=re.M | re.S)
            for target in re.findall(r'\]\(([^)\n]+)\)', prose):
                if re.match(r'^[a-zA-Z][a-zA-Z\d+.-]*:', target) or target.startswith('#'):
                    continue
                local = (document.parent / target.split('#', 1)[0]).resolve()
                assert local.is_relative_to(folder.resolve()) and local.is_file(), (document, target)
                counts['compat_local_links'] += 1
            if document != folder / 'SKILL.md':
                source = repo / 'codex_linux/skills' / name / 'references/skills' / document.name
                assert COMPAT.sub('', content) == COMPAT.sub('', read(source)), document
                counts['bundled_workflows'] += 1
        for script in sorted((folder / 'scripts').glob('*.py')):
            ast.parse(read(script), filename=script.name)
            counts['python_scripts'] += 1
        # Copy only this folder, change cwd, and invoke real helpers. Neither
        # sibling installations nor the source repository can satisfy imports.
        with tempfile.TemporaryDirectory(prefix='windows-skill-') as temporary:
            temporary = Path(temporary)
            copy = temporary / 'standalone'
            shutil.copytree(folder, copy)
            good = temporary / '한글 문서.md'
            good.write_text('# 제목\n\n## 1. 개요\n\n[개요](#1-개요)\n', encoding='utf-8')
            bad = temporary / 'missing.md'
            bad.write_text('# Title\n\n[missing](absent.md)\n[anchor](#absent)\n', encoding='utf-8')
            for tool in ('md-link-check.py', 'md-heading-check.py'):
                script = copy / 'scripts' / tool
                if script.exists():
                    for target, status in ((good, 0), (bad, 1)):
                        result = cli(script, target, cwd=temporary)
                        assert result.returncode == status and 'Traceback' not in result.stderr, (name, tool, status, result.returncode)
                        counts['isolated_tool_runs'] += 1
            for tool in ('md-style-check.py', 'lock.py', 'script_template.py'):
                script = copy / 'scripts' / tool
                if script.exists():
                    result = cli(script, '--help', cwd=temporary)
                    assert result.returncode == 0 and 'Traceback' not in result.stderr, (name, tool)
                    counts['isolated_tool_runs'] += 1
        counts['skills'] += 1
    for tool in ('md-link-check.py', 'md-heading-check.py', 'md-style-check.py', 'md_common.py', 'lock.py', 'script_template.py', 'script_template.sh'):
        copies = sorted((root / 'skills').glob('*/scripts/' + tool))
        if copies:
            assert len({sha(p) for p in copies}) == 1, tool
    assert read(root / 'personal/AGENTS.md').startswith(read(repo / 'codex_linux/personal/AGENTS.md'))
    config = tomllib.loads(read(root / 'personal/config.example.toml'))
    shared = tomllib.loads(read(repo / '.codex/config.toml'))
    assert all(config[key] == value for key, value in shared.items())
    assert config['windows']['sandbox'] == 'elevated'
    assert sha(root / 'personal/config.shared.example.toml') == sha(repo / '.codex/config.toml')
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        parser.error('Python 3.11 or newer is required')
    print(json.dumps({'status': 'PASS', 'counts': verify(args.repo.resolve())}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
