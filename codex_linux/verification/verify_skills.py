#!/usr/bin/env python3
"""Development checks; not required when copying or using a skill folder."""
import ast
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / 'codex_linux/skills'
COMPAT = re.compile(r'\n\n<!-- CODEX-COMPAT-BEGIN -->.*?<!-- CODEX-COMPAT-END -->\n', re.S)


def remove_compat(text):
    text = COMPAT.sub('', text)
    # The only source-line correction quotes invalid YAML descriptions.
    if 'name: bash-script-template\n' in text or 'name: python-script-template\n' in text:
        match = re.search(r'^description: (.+)$', text, re.M)
        value = json.loads(match.group(1))
        text = text[:match.start()] + 'description: ' + value + text[match.end():]
    return text.encode()


def run(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def main():
    originals = sorted((ROOT / 'kiro/skills').glob('*/SKILL.md'))
    assert len(originals) == 19
    assert sorted(p.parent.name for p in originals) == sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    counts = {'skills': 0, 'bundled_workflows': 0, 'local_links': 0, 'scripts': 0, 'isolated_tool_runs': 0}
    for source in originals:
        folder = SKILLS / source.parent.name
        raw = source.read_bytes()
        assert (folder / 'references/kiro-original.md').read_bytes() == raw, source
        migrated = (folder / 'SKILL.md').read_text()
        assert len(COMPAT.findall(migrated)) == 1
        assert remove_compat(migrated) == raw, source
        for ref in sorted((folder / 'references/skills').glob('*.md')):
            original = ROOT / 'kiro/skills' / ref.stem / 'SKILL.md'
            assert remove_compat(ref.read_text()) == original.read_bytes(), ref
            assert (folder / 'references/originals' / ref.name).read_bytes() == original.read_bytes(), ref
            counts['bundled_workflows'] += 1
        # A copy cannot conceal dependency on a symlink or sibling installation.
        assert not any(p.is_symlink() for p in folder.rglob('*')), folder
        for entry in [folder / 'SKILL.md', *sorted((folder / 'references/skills').glob('*.md'))]:
            block = COMPAT.search(entry.read_text()).group()
            for target in re.findall(r'\]\(([^)]+)\)', block):
                path = (entry.parent / target.split('#')[0]).resolve()
                assert path.is_relative_to(folder.resolve()) and path.is_file(), (entry, target)
                counts['local_links'] += 1
        for script in (folder / 'scripts').glob('*.py'):
            ast.parse(script.read_text(), filename=str(script))
            counts['scripts'] += 1
        with tempfile.TemporaryDirectory(prefix='standalone-skill-') as tmp:
            isolated = Path(tmp)
            copy = isolated / 'skill'
            shutil.copytree(folder, copy)
            good = isolated / 'good.md'
            good.write_text('# Fixture\n\n## 1. Overview\n\nText.\n')
            bad = isolated / 'bad.md'
            bad.write_text('# Fixture\n\n[Missing](absent.md)\n[Bad](#absent)\n\n## 1. Overview\n\nText.\n')
            if (copy / 'scripts/md-link-check.py').exists():
                for tool in ('md-link-check.py', 'md-heading-check.py'):
                    cmd = str(copy / 'scripts' / tool)
                    assert run('python3', '-I', cmd, str(good), cwd=isolated).returncode == 0
                    assert run('python3', '-I', cmd, str(bad), cwd=isolated).returncode != 0
                    counts['isolated_tool_runs'] += 2
                assert run('python3', '-I', str(copy / 'scripts/md-style-check.py'), '--help', cwd=isolated).returncode == 0
                counts['isolated_tool_runs'] += 1
        counts['skills'] += 1

    # Exercise actual exclusivity, ownership, corrupted/stale locks and symlinks.
    tool = str(SKILLS / 'kiro-lock/scripts/lock.py')
    with tempfile.TemporaryDirectory(prefix='skill-lock-test-') as tmp:
        project = Path(tmp)
        tokens = [f'fixture-session-{n:02d}' for n in range(12)]
        def lock(op, token):
            return run('python3', '-I', tool, op, '--root', tmp, '--token', token)
        with ThreadPoolExecutor(max_workers=12) as pool:
            results = list(pool.map(lambda t: lock('acquire', t), tokens))
        winners = [token for token, result in zip(tokens, results) if result.returncode == 0]
        assert len(winners) == 1, [r.stdout + r.stderr for r in results]
        owner = winners[0]
        other = next(t for t in tokens if t != owner)
        before = (project / '.kiro-lock').read_bytes()
        assert lock('release', other).returncode != 0
        assert (project / '.kiro-lock').read_bytes() == before
        assert lock('check', owner).returncode == 0
        assert lock('release', owner).returncode == 0
        assert not (project / '.kiro-lock').exists()
        (project / '.kiro-lock').write_text('corrupted lock')
        assert lock('release', owner).returncode != 0
        assert (project / '.kiro-lock').read_text() == 'corrupted lock'
        (project / '.kiro-lock').unlink()
        target = project / 'another-task.txt'
        target.write_text('do not remove')
        (project / '.kiro-lock').symlink_to(target)
        assert lock('release', owner).returncode != 0
        assert target.read_text() == 'do not remove'
        (project / '.kiro-lock').unlink()
        (project / '.kiro-lock.guard').write_text('abandoned operation')
        assert lock('acquire', owner).returncode != 0
        assert (project / '.kiro-lock.guard').read_text() == 'abandoned operation'
    counts['lock_invariants'] = 8
    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
