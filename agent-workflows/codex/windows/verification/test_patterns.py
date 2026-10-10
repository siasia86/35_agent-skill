#!/usr/bin/env python3
"""Exercise actual Windows compatibility code patterns in temporary fixtures."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
_spec = importlib.util.spec_from_file_location('verify_current', Path(__file__).with_name('verify_current.py'))
_verifier = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_verifier)
active_skill_body = _verifier.active_skill_body
current_entries = _verifier.current_entries
read_current_inventory = _verifier.read_current_inventory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--pattern-document', type=Path,
                        help='Current relocated Windows pattern document; legacy default reads SKILL blocks')
    args = parser.parse_args()
    snippets = []
    if args.pattern_document:
        text = args.pattern_document.read_text(encoding='utf-8')
        for snippet in re.findall(r'^```python\s*\n(.*?)^```\s*$', text, re.M | re.S):
            ast.parse(snippet)
            snippets.append((args.pattern_document.name, snippet))
    inventory = read_current_inventory(Path(__file__).with_name('current_inventory.json'))
    for path in current_entries(args.skills.resolve(), inventory):
        text = path.read_text(encoding='utf-8')
        assert '\x00' not in text, path.name
        body = active_skill_body(text, inventory[path.parent.name])
        for snippet in re.findall(r'^```python\s*\n(.*?)^```\s*$', body, re.M | re.S):
            ast.parse(snippet)
            snippets.append((path.parent.name, snippet))
    cases = []
    def check(name, condition):
        cases.append({'name': name, 'passed': bool(condition)})
        assert condition, name
    check('windows_python_snippets_parse', bool(snippets))
    locks = [body for name, body in snippets if 'def exclusive_file_lock(' in body]
    assert len(locks) == 1
    if sys.platform != 'win32':
        parser.error('Windows native byte locking fixture requires win32')
    with tempfile.TemporaryDirectory(prefix='windows-pattern-') as temporary:
        directory = Path(temporary)
        module_path = directory / 'pattern.py'
        module_path.write_text(locks[0], encoding='utf-8')
        spec = importlib.util.spec_from_file_location('pattern', module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        lock = directory / '협조자 잠금.bin'
        child_code = 'import sys; from pattern import exclusive_file_lock\nwith exclusive_file_lock(sys.argv[1]): print("ACQUIRED")\n'
        def child():
            return subprocess.run([sys.executable, '-X', 'utf8', '-B', '-c', child_code, str(lock)],
                                  cwd=directory, capture_output=True, encoding='utf-8', timeout=10)
        with module.exclusive_file_lock(lock):
            check('byte_lock_initial_file_has_one_byte', lock.stat().st_size == 1)
            result = child()
            check('byte_lock_blocks_competing_process', result.returncode != 0 and 'ACQUIRED' not in result.stdout)
        check('byte_lock_path_retained_after_release', lock.is_file())
        check('byte_lock_reacquired_after_release', child().returncode == 0)
        before = hashlib.sha256(lock.read_bytes()).hexdigest()
        try:
            with module.exclusive_file_lock(lock):
                raise RuntimeError('fixture failure')
        except RuntimeError:
            pass
        check('byte_lock_exception_releases', child().returncode == 0)
        check('byte_lock_persistent_bytes_preserved', hashlib.sha256(lock.read_bytes()).hexdigest() == before)
    result = {'status': 'PASS', 'python_snippets': len(snippets), 'cases': cases}
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
