#!/usr/bin/env python3
"""Regression checks for preserved templates and corrected local skill examples."""
import argparse
import contextlib
import fcntl
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = {'scope': 'Linux temporary fixtures; no runtime installation', 'commands': []}


def compat_block(path, language, needle):
    """Select executable corrected code from the compatibility section only."""
    text = path.read_text().split('<!-- CODEX-COMPAT-BEGIN -->', 1)[1]
    text = text.split('<!-- CODEX-COMPAT-END -->', 1)[0]
    blocks = re.findall(r'^```' + language + r'\s*\n(.*?)^```\s*$', text, re.M | re.S)
    matches = [block for block in blocks if needle in block]
    if len(matches) != 1:
        raise ValueError((str(path), needle, len(matches)))
    return matches[0]


def execute(command, cwd):
    """Capture actual CLI exit status and both streams for review."""
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=20)
    EVIDENCE['commands'].append({
        'test': EVIDENCE.get('current_test'), 'argv': command, 'cwd': str(cwd),
        'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
    })
    return result


class RemediationTests(unittest.TestCase):
    def setUp(self):
        """Copy affected skills into a workspace independent of the source repo."""
        self.temp = tempfile.TemporaryDirectory(prefix='skill-remediation-test-')
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.copies = self.work / 'skills'
        names = ('python-script-template', 'bash-script-template', 'work-rules',
                 'md-link-check', 'git-commit-rule', 'readme-template',
                 'security-tools', 'using-skills', 'zircon-readme-policy')
        for name in names:
            shutil.copytree(ROOT / 'codex_linux/skills' / name, self.copies / name)

    def python_cli(self):
        """Build a CLI from the actual corrected parse_args and main example."""
        path = self.copies / 'python-script-template/SKILL.md'
        code = compat_block(path, 'python', 'args, parser = parse_args()')
        cli = self.work / 'cli.py'
        cli.write_text(
            "import argparse, logging, os, sys\nVERSION = 'fixture-version'\n"
            "log = logging.getLogger('fixture')\n"
            "def process_file(path, **options):\n    print('file', path, options)\n"
            "def process_dir(path, **options):\n    print('dir', path, options)\n" + code)
        return str(cli)

    def atomic_write(self):
        """Load the actual POSIX replacement helper from the skill."""
        code = compat_block(self.copies / 'python-script-template/SKILL.md',
                            'python', 'def _atomic_write(')
        namespace = {'os': os}
        exec(compile(code, 'corrected-atomic-write', 'exec'), namespace)
        return namespace['_atomic_write']

    def existing_file(self):
        """Create a controlled executable file with known content and mode."""
        target = self.work / 'original.txt'
        target.write_text('original\n')
        target.chmod(0o755)
        return target

    def assert_original(self, target):
        """A failed replacement must preserve content, mode and leave no temp file."""
        self.assertEqual(target.read_text(), 'original\n')
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o755)
        self.assertEqual(list(self.work.glob('.tmp_*')), [])

    def bash_function(self):
        """Extract the corrected argv-based logging function."""
        block = compat_block(self.copies / 'bash-script-template/SKILL.md',
                             'bash', 'run_msg_info()')
        return re.search(r'^run_msg_info\(\) \{\n.*?^\}', block, re.M | re.S).group()

    def lock_namespace(self):
        """Load the persistent-path flock context manager."""
        code = compat_block(self.copies / 'work-rules/SKILL.md',
                            'python', 'def exclusive_file_lock(')
        namespace = {}
        exec(compile(code, 'corrected-flock', 'exec'), namespace)
        return namespace, code

    def test_python_no_args_help_version_and_invalid_option(self):
        """CLI entry paths terminate predictably without parser scope errors."""
        cli = self.python_cli()
        for args, status, message in (([], 0, 'Examples:'), (['--help'], 0, 'Notes:'),
                                      (['--version'], 0, 'fixture-version'),
                                      (['--unknown-option'], 2, 'unrecognized arguments')):
            with self.subTest(args=args):
                result = execute(['python3', '-I', cli, *args], self.work)
                self.assertEqual(result.returncode, status)
                self.assertIn(message, result.stdout + result.stderr)
                self.assertNotIn('NameError', result.stderr)

    def test_python_target_file_directory_and_flags(self):
        """Parser/main changes retain dispatch, multiple files and CLI flags."""
        cli = self.python_cli()
        target = self.existing_file()
        for args, kind in (([str(target), '-d', '-v'], 'file'),
                           (['-f', str(target), str(target), '-q'], 'file'),
                           (['-D', str(self.work), '-d'], 'dir')):
            result = execute(['python3', '-I', cli, *args], self.work)
            self.assertEqual(result.returncode, 0)
            self.assertIn(kind, result.stdout)
            if '-d' in args:
                self.assertIn("'dry_run': True", result.stdout)

    def test_atomic_preserves_modes_owner_and_content(self):
        """Actual replacement keeps existing uid/gid and permission bits."""
        write = self.atomic_write()
        target = self.existing_file()
        for mode in (0o755, 0o644, 0o640, 0o4755):
            target.chmod(mode)
            before = target.stat()
            write(target, 'updated 한글\n')
            after = target.stat()
            self.assertEqual(target.read_text(), 'updated 한글\n')
            self.assertEqual(stat.S_IMODE(after.st_mode), mode)
            self.assertEqual((after.st_uid, after.st_gid), (before.st_uid, before.st_gid))
        self.assertEqual(list(self.work.glob('.tmp_*')), [])

    def test_atomic_new_file_uses_private_mode(self):
        """New files have a deliberate, observable 0600 policy."""
        target = self.work / 'new.txt'
        self.atomic_write()(target, 'new\n')
        self.assertEqual(target.read_text(), 'new\n')
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o600)

    def test_atomic_failures_preserve_original_and_cleanup(self):
        """Write, mode, sync and replace failures cannot publish a partial file."""
        write = self.atomic_write()
        target = self.existing_file()
        for operation in ('fchmod', 'fsync', 'replace'):
            with self.subTest(operation=operation), patch.object(os, operation, side_effect=OSError(operation)):
                with self.assertRaises(OSError):
                    write(target, 'replacement\n')
            self.assert_original(target)
        with self.assertRaises(TypeError):
            write(target, None)
        self.assert_original(target)

    def test_atomic_owner_permission_failure_aborts_before_replace(self):
        """Inject a denied metadata operation without changing OS ownership."""
        write = self.atomic_write()
        target = self.existing_file()
        owner = target.stat()
        different = SimpleNamespace(st_uid=owner.st_uid + 1, st_gid=owner.st_gid)
        with patch.object(os, 'fstat', return_value=different), \
                patch.object(os, 'fchown', side_effect=PermissionError('fixture denial')) as chown:
            with self.assertRaises(PermissionError):
                write(target, 'replacement\n')
            self.assertEqual(chown.call_args.args[1:], (owner.st_uid, owner.st_gid))
        self.assert_original(target)

    def test_atomic_rejects_symlinks_and_directories(self):
        """Replacement cannot silently change a symlink into a regular file."""
        write = self.atomic_write()
        target = self.existing_file()
        link = self.work / 'link.txt'
        link.symlink_to(target)
        for path in (link, self.work):
            with self.assertRaises(ValueError):
                write(path, 'replacement\n')
        self.assertTrue(link.is_symlink())
        self.assert_original(target)

    def test_bash_failure_return_logging_and_stop_in_both_modes(self):
        """Exit 7 is logged and propagated before any dependent step runs."""
        function = self.bash_function()
        for errexit in ('', 'set -e\n'):
            for guarded in (False, True):
                if not guarded and not errexit:
                    suffix = '\nrun_msg_info 1 bash -c \'exit 7\'\nstatus=$?\nexit "$status"\n'
                else:
                    guard = ' || exit "$?"' if guarded else ''
                    suffix = '\nrun_msg_info 1 bash -c \'exit 7\'' + guard + '\nprintf "NEXT\\n"\n'
                result = execute(['bash', '--noprofile', '--norc', '-c', errexit + function + suffix], self.work)
                self.assertEqual(result.returncode, 7)
                self.assertIn('failed with status 7', result.stderr)
                self.assertNotIn('NEXT', result.stdout)

    def test_bash_success_preserves_literal_arguments_and_stdout(self):
        """Shell metacharacters stay data and logs do not contaminate stdout."""
        function = self.bash_function()
        literal = 'spaces ; $(touch SHOULD_NOT_EXIST) *'
        suffix = "\nrun_msg_info 1 printf '%s\\n' '" + literal + "' || exit \"$?\"\n"
        result = execute(['bash', '--noprofile', '--norc', '-c', function + suffix], self.work)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, literal + '\n')
        self.assertIn('success', result.stderr)
        self.assertFalse((self.work / 'SHOULD_NOT_EXIST').exists())

    def test_bash_invalid_call_reports_failure(self):
        """Missing command is an error rather than a successful empty call."""
        result = execute(['bash', '--noprofile', '--norc', '-c',
                          self.bash_function() + '\nrun_msg_info 1'], self.work)
        self.assertEqual(result.returncode, 2)
        self.assertIn('command required', result.stderr)

    def test_flock_waiter_and_new_process_share_one_inode(self):
        """Recreate the old race schedule; a later process remains excluded."""
        namespace, code = self.lock_namespace()
        lock = namespace['exclusive_file_lock']
        target = self.work / 'persistent.lock'
        with lock(target) as holder:
            inode = os.fstat(holder.fileno()).st_ino
            waiter = target.open('a+')
            self.addCleanup(waiter.close)
            with self.assertRaises(BlockingIOError):
                fcntl.flock(waiter, fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.assertEqual(target.stat().st_ino, inode)
        fcntl.flock(waiter, fcntl.LOCK_EX | fcntl.LOCK_NB)
        child = self.work / 'lock_child.py'
        child.write_text('import os, sys\n' + code +
                         '\ntry:\n    with exclusive_file_lock(sys.argv[1]) as fp:\n'
                         '        print(os.fstat(fp.fileno()).st_ino)\n'
                         'except BlockingIOError:\n    sys.exit(7)\n')
        denied = execute(['python3', '-I', str(child), str(target)], self.work)
        self.assertEqual(denied.returncode, 7)
        fcntl.flock(waiter, fcntl.LOCK_UN)
        allowed = execute(['python3', '-I', str(child), str(target)], self.work)
        self.assertEqual(allowed.returncode, 0)
        self.assertEqual(int(allowed.stdout), inode)
        self.assertEqual(target.stat().st_ino, inode)

    def test_flock_exception_releases_and_permission_errors_propagate(self):
        """Work exceptions unlock; unrelated I/O errors are not treated as contention."""
        namespace, _ = self.lock_namespace()
        lock = namespace['exclusive_file_lock']
        target = self.work / 'persistent.lock'
        with self.assertRaises(RuntimeError):
            with lock(target):
                raise RuntimeError('fixture work failed')
        with lock(target):
            pass
        self.assertTrue(target.exists())
        with patch('builtins.open', side_effect=PermissionError('fixture denial')):
            with self.assertRaises(PermissionError):
                with lock(target):
                    pass

    def test_link_fence_matrix_in_all_seven_isolated_copies(self):
        """Fences hide example links and preserve detection/line numbers afterwards."""
        cases = {
            'normal': '# Fixture\n\n[Broken](missing.md)\n',
            'original_nested': '# Fixture\n\n````markdown\n```python\nsample\n````\n\n[Broken](missing.md)\n',
            'nested_complete': '````markdown\n```python\n[Example](ignore.md)\n```\n````\n[Broken](missing.md)\n',
            'longer_close': '```python\n[Example](ignore.md)\n`````\n[Broken](missing.md)\n',
            'tilde': '~~~~markdown\n~~~python\n[Example](ignore.md)\n~~~\n~~~~\n[Broken](missing.md)\n',
            'different_marker': '```text\n~~~\n[Example](ignore.md)\n```\n[Broken](missing.md)\n',
            'tagged_close': '```text\n```python\n[Example](ignore.md)\n```\n[Broken](missing.md)\n',
            'indent_three': '   ```text\n[Example](ignore.md)\n   ```\n[Broken](missing.md)\n',
            'indent_four_cannot_close': '```text\n    ```\n[Example](ignore.md)\n```\n[Broken](missing.md)\n',
            'invalid_backtick_info': '```py`bad\n[Broken](missing.md)\n',
            'closing_spaces': '```text\n[Example](ignore.md)\n```   \t\n[Broken](missing.md)\n',
        }
        checkers = sorted(self.copies.glob('*/scripts/md-link-check.py'))
        self.assertEqual(len(checkers), 7)
        hashes = {hashlib.sha256(path.read_bytes()).hexdigest() for path in checkers}
        self.assertEqual(len(hashes), 1)
        for name, content in cases.items():
            fixture = self.work / (name + '.md')
            fixture.write_text(content)
            line = content.splitlines().index('[Broken](missing.md)') + 1
            for checker in checkers:
                with self.subTest(case=name, checker=checker.parent.parent.name):
                    result = execute(['python3', '-I', str(checker), str(fixture)], self.work)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn(f'L{line}: missing.md', result.stdout)
                    self.assertIn('링크: 1개', result.stdout)
                    self.assertNotIn('ignore.md', result.stdout)
                    self.assertEqual(result.stderr, '')

    def test_link_unclosed_fences_fail_in_all_copies(self):
        """An incomplete check can never print an unconditional success result."""
        for marker in ('```python', '~~~text'):
            fixture = self.work / 'unclosed.md'
            fixture.write_text('# Fixture\n' + marker + '\n[Example](ignore.md)\n')
            for checker in sorted(self.copies.glob('*/scripts/md-link-check.py')):
                result = execute(['python3', '-I', str(checker), str(fixture)], self.work)
                self.assertEqual(result.returncode, 2)
                self.assertIn('unclosed code block', result.stderr)
                self.assertIn('last open: L2', result.stderr)
                self.assertNotIn('모든 링크 정상', result.stdout)

    def test_link_mixed_files_and_existing_exclusions(self):
        """Incomplete files do not stop other files; prior exclusions still apply."""
        unclosed = self.work / 'unclosed.md'
        unclosed.write_text('```text\nexample\n')
        broken = self.work / 'broken.md'
        broken.write_text('[Broken](missing.md)\n')
        good = self.work / 'good.md'
        good.write_text('[Exists](broken.md)\n[External](https://example.com)\n'
                        '[Anchor](#example)\n`[Example](ignore.md)`\n')
        for checker in sorted(self.copies.glob('*/scripts/md-link-check.py')):
            result = execute(['python3', '-I', str(checker), str(good)], self.work)
            self.assertEqual(result.returncode, 0)
            self.assertIn('링크: 1개', result.stdout)
            result = execute(['python3', '-I', str(checker), str(unclosed), str(broken)], self.work)
            self.assertEqual(result.returncode, 2)
            self.assertIn('missing.md', result.stdout)
            self.assertIn('검사 미완료', result.stdout)

    def test_bundled_examples_match_corrected_entrypoints(self):
        """Bundled workflows contain the same executable corrections as entrypoints."""
        for name, language, needle in (
                ('python-script-template', 'python', 'args, parser = parse_args()'),
                ('python-script-template', 'python', 'def _atomic_write('),
                ('bash-script-template', 'bash', 'run_msg_info()'),
                ('work-rules', 'python', 'def exclusive_file_lock(')):
            source = compat_block(self.copies / name / 'SKILL.md', language, needle)
            references = sorted(self.copies.glob(f'*/references/skills/{name}.md'))
            self.assertTrue(references)
            for ref in references:
                self.assertEqual(compat_block(ref, language, needle), source)


class EvidenceResult(unittest.TextTestResult):
    def startTest(self, test):
        EVIDENCE['current_test'] = test.id()
        super().startTest(test)


def main():
    """Run behavioral regressions and save commands, statuses and input hashes."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(RemediationTests)
    result = unittest.TextTestRunner(verbosity=2, resultclass=EvidenceResult).run(suite)
    EVIDENCE.pop('current_test', None)
    EVIDENCE['tests_run'] = result.testsRun
    EVIDENCE['failures'] = [{'test': test.id(), 'traceback': trace} for test, trace in result.failures]
    EVIDENCE['errors'] = [{'test': test.id(), 'traceback': trace} for test, trace in result.errors]
    EVIDENCE['passed'] = result.wasSuccessful()
    EVIDENCE['inputs'] = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted((ROOT / 'codex_linux/skills').rglob('*'))
        if path.is_file() and (path.name == 'SKILL.md' or path.name == 'md-link-check.py'
                               or path.parent.name == 'skills')}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(EVIDENCE, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'tests': result.testsRun, 'passed': result.wasSuccessful(),
                      'cli_runs': len(EVIDENCE['commands']), 'output': str(args.output)}))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
