#!/usr/bin/env python3
"""Validate Windows helpers in fresh TEMP; no repository/home/operating writes.

Python 3.11+. --skills PATH or --repo PATH selects the native package.
Historical Bash fixtures require both --bash and --legacy-bash-script explicitly.
Public results contain only name/code/expected. Optional --raw is local evidence.
"""
import argparse
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import time
from unittest import mock
import uuid

sys.dont_write_bytecode = True


def load_script(path, name):
    """Load one helper without creating bytecode beside its source."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def call_main(module, args):
    """Capture helper main output while leaving business side effects isolated."""
    stdout, stderr = io.StringIO(), io.StringIO()
    with contextlib.ExitStack() as stack:
        stack.enter_context(contextlib.redirect_stdout(stdout))
        stack.enter_context(contextlib.redirect_stderr(stderr))
        if hasattr(module, 'log'):
            for handler in module.log.handlers:
                stack.enter_context(mock.patch.object(handler, 'stream', stderr))
        code = module.main(args)
    return {'code': code, 'stdout': stdout.getvalue(), 'stderr': stderr.getvalue()}


def main(argv=None):
    """Run meaningful helper failure/invariant cases and emit compact results."""
    parser = argparse.ArgumentParser(description=__doc__)
    locations = parser.add_mutually_exclusive_group(required=True)
    locations.add_argument('--skills', type=Path, help='Windows skill collection directory')
    locations.add_argument('--repo', type=Path, help='repository with codex_windows/skills')
    parser.add_argument('--bash', type=Path, help='existing Git Bash bash.exe; omitted means SKIP')
    parser.add_argument('--legacy-bash-script', type=Path,
                        help='optional preserved historical Bash helper, outside the native package')
    parser.add_argument('--output', type=Path, help='optional public JSON result')
    parser.add_argument('--raw', type=Path, help='optional PRIVATE local raw result, never publish')
    args = parser.parse_args(argv)
    skills = (args.skills if args.skills else args.repo / 'codex_windows' / 'skills').resolve()
    template = skills / 'python-script-template' / 'scripts' / 'script_template.py'
    lock_script = skills / 'kiro-lock' / 'scripts' / 'lock.py'
    bash_script = args.legacy_bash_script
    if (args.bash is None) != (bash_script is None):
        parser.error('historical Bash fixtures require both --bash and --legacy-bash-script')
    if args.bash is not None and (not args.bash.is_file() or not bash_script.is_file()):
        parser.error('explicit historical Bash inputs must exist')
    for script in (template, lock_script):
        if not script.is_file():
            parser.error('required helper file is absent; assemble all draft files first')
    if sys.version_info < (3, 11):
        parser.error('Python 3.11 or newer is required')
    public, raw = [], {'runtime': {'python': sys.version.split()[0], 'os': os.name}, 'cases': {}}

    def record(name, code, expected, details=None):
        """Store public statuses separately from private fixture observations."""
        public.append({'name': name, 'code': code, 'expected': expected})
        if details is not None:
            raw['cases'][name] = details

    def run_python(script, extra):
        """Use this interpreter, explicit UTF-8 and no source bytecode writes."""
        result = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(script), *map(str, extra)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8', timeout=20, check=False)
        return {'code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}

    def cli_case(name, extra, expected):
        """Record one template CLI contract case."""
        result = run_python(template, extra)
        record(name, result['code'], expected, result)
        return result

    with tempfile.TemporaryDirectory(prefix='codex-windows-runtime-') as temporary:
        fixture = Path(temporary) / '유니코드 작업 폴더'
        fixture.mkdir()
        valid = fixture / '입력 파일.txt'
        valid.write_text('시작: 한글 데이터\n', encoding='utf-8')
        missing = fixture / '없는 파일.txt'
        directory = fixture / '대상 디렉터리'
        directory.mkdir()
        (directory / '하위 파일.txt').write_text('유니코드\n', encoding='utf-8')
        cli_case('python_no_args_help', [], 0)
        help_result = cli_case('python_help', ['--help'], 0)
        record('python_help_no_unimplemented_restore', int('-r config' in help_result['stdout']), 0)
        cli_case('python_version', ['--version'], 0)
        cli_case('python_unknown_restore_option', ['-r', valid], 2)
        cli_case('python_missing_target', [missing], 1)
        cli_case('python_missing_dry_run', ['-d', missing], 1)
        result = cli_case('python_mixed_file_batch', ['-d', '-f', valid, missing], 1)
        record('python_mixed_batch_valid_dispatch', int('would invoke project transform' not in result['stderr']), 0)
        cli_case('python_mixed_dir_batch', ['-d', '-D', directory, fixture / '없는 폴더'], 1)
        cli_case('python_file_option_rejects_directory', ['-f', directory], 1)
        cli_case('python_dir_option_rejects_file', ['-D', valid], 1)
        cli_case('python_conflicting_input_modes', [valid, '-f', valid], 2)
        cli_case('python_unicode_dry_run', ['-d', '-v', valid], 0)
        record('python_dry_run_preserves_bytes', int(valid.read_text(encoding='utf-8') != '시작: 한글 데이터\n'), 0)
        result = cli_case('python_unimplemented_transform_fails', [valid], 1)
        record('python_placeholder_contract_explicit', int('implement transform_content' not in result['stderr']), 0)

        python_module = load_script(template, 'windows_template_test')
        with mock.patch.object(python_module, 'transform_content', side_effect=lambda text, path: text.replace('시작', '완료')):
            result = call_main(python_module, ['-f', str(valid), str(missing)])
            record('python_real_transform_partial_failure_status', result['code'], 1, result)
            record('python_valid_member_written_despite_batch_failure', int(not valid.read_text(encoding='utf-8').startswith('완료')), 0)
            before = valid.read_bytes()
            result = call_main(python_module, [str(valid)])
            record('python_transform_idempotent_status', result['code'], 0, result)
            record('python_transform_idempotent_bytes', int(valid.read_bytes() != before), 0)
        before = valid.read_bytes()
        with mock.patch.object(python_module.os, 'replace', side_effect=OSError('fixture replacement failure')):
            try:
                python_module._atomic_write(valid, '변경 시도')
            except OSError:
                code = 0
            else:
                code = 1
        record('python_atomic_replace_failure_propagates', code, 0)
        record('python_atomic_replace_failure_preserves_original', int(valid.read_bytes() != before), 0)
        record('python_atomic_replace_failure_cleans_temp', int(bool(list(fixture.glob('.tmp_*')))), 0)

        # W02: real logger setup must not add its output to business inputs.
        shared_log_dir = fixture / 'business and file logs'
        shared_log_dir.mkdir()
        business = shared_log_dir / '00_business.txt'
        lookalike = shared_log_dir / 'script_template_example.log'
        business.write_text('before business\n', encoding='utf-8')
        lookalike.write_text('before user-owned data\n', encoding='utf-8')
        result = run_python(template, ['-d', '-D', shared_log_dir, '--log-dir', shared_log_dir])
        record('python_shared_log_dir_dry_run_status', result['code'], 0, result)
        monthly = python_module._log_file_path(python_module.log.name, shared_log_dir)
        selected = [line for line in result['stderr'].splitlines() if 'would invoke project transform:' in line]
        record('python_shared_log_dir_excludes_active_log', int(any(monthly.name in line for line in selected)), 0)
        record('python_shared_log_dir_keeps_user_loglike_file', int(not any(lookalike.name in line for line in selected)), 0)
        processed = []

        def business_transform(text, path):
            """A real TEMP text transform, leaving the shipping placeholder alone."""
            processed.append(Path(path).name)
            return text.replace('before', 'after')

        try:
            with mock.patch.object(python_module, 'transform_content', side_effect=business_transform):
                result = call_main(python_module, ['-D', str(shared_log_dir), '--log-dir', str(shared_log_dir)])
            record('python_shared_log_dir_normal_status', result['code'], 0, result)
            record('python_shared_log_dir_only_business_dispatch', int(set(processed) != {business.name, lookalike.name}), 0)
            record('python_shared_log_dir_business_written', int(not business.read_text(encoding='utf-8').startswith('after')), 0)
        finally:
            for handler in list(python_module.log.handlers):
                if hasattr(handler, 'baseFilename'):
                    python_module.log.removeHandler(handler)
                    handler.close()  # Own fixture handler only, for Windows cleanup.
        monthly_before = monthly.read_bytes()
        business_before = business.read_bytes()
        result = call_main(python_module, ['-d', '-f', str(business), str(monthly), '--log-dir', str(shared_log_dir)])
        record('python_explicit_log_batch_conflict_status', result['code'], 1, result)
        record('python_explicit_log_conflict_before_log_open', int(monthly.read_bytes() != monthly_before), 0)
        record('python_explicit_log_conflict_before_business_dispatch', int(business.read_bytes() != business_before), 0)
        result = call_main(python_module, ['-d', str(monthly), '--log-dir', str(shared_log_dir)])
        record('python_log_target_conflict_status', result['code'], 1, result)
        alias = shared_log_dir / 'log identity alias.txt'
        try:
            os.link(monthly, alias)
        except OSError:
            record('python_log_identity_alias_capability', 'SKIP', 'SKIP')
        else:
            result = call_main(python_module, ['-d', str(alias), '--log-dir', str(shared_log_dir)])
            record('python_log_identity_alias_conflict_status', result['code'], 1, result)
            record('python_log_identity_alias_preserves_bytes', int(alias.read_bytes() != monthly_before), 0)
            alias.unlink()

        lock_module = load_script(lock_script, 'windows_lock_test')
        token = uuid.uuid4().hex
        base_args = ['--root', str(fixture), '--token', token]
        result = call_main(lock_module, ['acquire', *base_args, '--task', '유니코드 작업'])
        record('lock_unicode_acquire', result['code'], 0, result)
        lock_path = fixture / '.kiro-lock'
        original = lock_path.read_bytes()
        payload = json.loads(original)
        record('lock_unicode_payload', int(payload.get('task') != '유니코드 작업'), 0)
        result = call_main(lock_module, ['acquire', *base_args])
        record('lock_existing_not_overwritten', int(result['code'] != 1 or lock_path.read_bytes() != original), 0, result)
        foreign = ['--root', str(fixture), '--token', uuid.uuid4().hex]
        result = call_main(lock_module, ['release', *foreign])
        record('lock_foreign_release_preserves', int(result['code'] != 1 or lock_path.read_bytes() != original), 0, result)
        result = call_main(lock_module, ['check', *base_args])
        record('lock_owner_check', result['code'], 0, result)
        result = call_main(lock_module, ['release', *base_args])
        record('lock_owner_release', result['code'], 0, result)
        record('lock_release_removes_only_owned_lock', int(lock_path.exists()), 0)

        def partial_dump(payload, stream, **kwargs):
            """Simulate partial JSON output followed by a caught write failure."""
            stream.write('{"session":')
            raise OSError('fixture partial payload failure')

        with mock.patch.object(lock_module.json, 'dump', side_effect=partial_dump):
            result = call_main(lock_module, ['acquire', *base_args])
        record('lock_partial_write_failure_status', result['code'], 1, result)
        record('lock_partial_write_own_cleanup', int(lock_path.exists()), 0)
        record('lock_partial_write_gate_cleanup', int((fixture / '.kiro-lock.guard').exists()), 0)
        with mock.patch.object(lock_module.os, 'fsync', side_effect=OSError('fixture fsync failure')):
            result = call_main(lock_module, ['acquire', *base_args])
        record('lock_fsync_failure_status', result['code'], 1, result)
        record('lock_fsync_failure_own_cleanup', int(lock_path.exists()), 0)
        result = call_main(lock_module, ['acquire', *base_args])
        record('lock_reacquire_after_own_failed_write', result['code'], 0, result)
        call_main(lock_module, ['release', *base_args])
        lock_path.write_bytes(b'{malformed historical lock')
        original = lock_path.read_bytes()
        result = call_main(lock_module, ['release', *base_args])
        record('lock_malformed_preserved', int(result['code'] != 1 or lock_path.read_bytes() != original), 0, result)
        lock_path.unlink()  # fixture-created bytes only, no repository/old lock.
        gate = fixture / '.kiro-lock.guard'
        gate.write_bytes(b'fixture abandoned guard')
        result = call_main(lock_module, ['acquire', *base_args])
        record('lock_existing_guard_preserved', int(result['code'] != 1 or gate.read_bytes() != b'fixture abandoned guard'), 0, result)
        gate.unlink()
        owned_source = fixture / 'owned inode fixture'
        replacement = fixture / 'replacement inode fixture'
        owned_source.write_text('owned', encoding='utf-8')
        replacement.write_text('replacement', encoding='utf-8')
        lock_module.unlink_owned(replacement, owned_source.stat())
        record('lock_cleanup_preserves_other_inode', int(not replacement.exists() or replacement.read_text(encoding='utf-8') != 'replacement'), 0)

        race_root = fixture / '동시 획득'
        race_root.mkdir()
        candidates = [uuid.uuid4().hex for _ in range(8)]
        processes = []
        try:
            for candidate in candidates:
                processes.append(subprocess.Popen([sys.executable, '-X', 'utf8', '-B', str(lock_script),
                                                   'acquire', '--root', str(race_root), '--token', candidate],
                                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'))
            race_results = []
            for process in processes:
                stdout, stderr = process.communicate(timeout=20)
                race_results.append({'code': process.returncode, 'stdout': stdout, 'stderr': stderr})
            winners = [index for index, result in enumerate(race_results) if result['code'] == 0]
            record('lock_concurrent_single_winner', int(len(winners) != 1), 0, {'attempts': race_results})
            if len(winners) == 1:
                result = run_python(lock_script, ['release', '--root', race_root, '--token', candidates[winners[0]]])
                record('lock_concurrent_winner_release', result['code'], 0, result)
            else:
                record('lock_concurrent_winner_release', 1, 0)
        finally:
            for process in processes:
                if process.poll() is None:
                    process.kill()
                process.wait()

        symlink = fixture / 'symlink fixture'
        try:
            symlink.symlink_to(valid)
        except (OSError, NotImplementedError):
            record('reparse_symlink_fixture_capability', 'SKIP', 'SKIP')
        else:
            result = run_python(template, ['-d', symlink])
            record('python_symlink_refused', result['code'], 1, result)
            lock_path.symlink_to(valid)
            result = call_main(lock_module, ['check', *base_args])
            record('lock_symlink_refused', result['code'], 1, result)
            record('lock_symlink_target_preserved', int(valid.read_bytes() != before), 0)
            lock_path.unlink()
            symlink.unlink()

        if args.bash is None:
            record('bash_runtime_selected', 'SKIP', 'SKIP')
        else:
            bash_env = os.environ.copy()
            for variable in ('BASH_ENV', 'ENV'):
                bash_env.pop(variable, None)
            bash_env.update(LOG_FILE01='', backup_status_log_dir='', BK_DIR='')
            shell_path = bash_script.as_posix()
            file_path = valid.as_posix()
            syntax = subprocess.run([str(args.bash), '-n', shell_path], capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_syntax', syntax.returncode, 0, {'stdout': syntax.stdout, 'stderr': syntax.stderr})
            for name, values in [('bash_no_args_help', []), ('bash_help', ['--help']), ('bash_version', ['--version'])]:
                result = subprocess.run([str(args.bash), shell_path, *values],
                                        capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
                record(name, result.returncode, 0, {'stdout': result.stdout, 'stderr': result.stderr})
            failure_harness = 'source "$1"\ncp() { return 7; }\nif main --backup "$2"; then printf "AFTER_BACKUP\\n"; exit 0; else exit "$?"; fi\n'
            for name, flags in [('bash_backup_failure', []), ('bash_backup_failure_errexit', ['-e'])]:
                result = subprocess.run([str(args.bash), *flags, '-c', failure_harness, 'fixture', shell_path, file_path],
                                        capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
                record(name, result.returncode, 7, {'stdout': result.stdout, 'stderr': result.stderr})
                record(name + '_stops_followup', int('AFTER_BACKUP' in result.stdout or 'backup: ' in result.stderr), 0)
            dry_run = subprocess.run([str(args.bash), shell_path, '--dry-run', '--backup', file_path],
                                     capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_unicode_dry_run', dry_run.returncode, 0, {'stdout': dry_run.stdout, 'stderr': dry_run.stderr})
            record('bash_dry_run_creates_no_backup', int(bool(list(fixture.glob(valid.name + '_ORG_*')))), 0)
            owner_target = fixture / 'unsupported owner must not create'
            owner_harness = 'source "$1"\nuname() { printf "MINGW64_NT\\n"; }\nmain --ensure-dir "$2" --owner fixture-user\n'
            owner_result = subprocess.run([str(args.bash), '-c', owner_harness, 'fixture', shell_path, owner_target.as_posix()],
                                          capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_unsupported_owner_status', owner_result.returncode, 2, {'stdout': owner_result.stdout, 'stderr': owner_result.stderr})
            record('bash_unsupported_owner_no_directory_creation', int(owner_target.exists()), 0)

            # Invalid values must fail before initialization/helper dispatch.
            # Every mutation-capable helper is a TEMP-marker stub: no service,
            # package, ownership or operational filesystem command can run.
            invalid_harness = ('source "$1"\nshift\nMUTATION_MARKER=$1\nshift\n'
                               'init_logging() { printf "init" > "$MUTATION_MARKER"; }\n'
                               'backup_conf() { printf "backup" > "$MUTATION_MARKER"; }\n'
                               'ensure_dir() { printf "directory" > "$MUTATION_MARKER"; }\n'
                               'service_start() { printf "service" > "$MUTATION_MARKER"; }\n'
                               'if main "$@"; then printf "followup" > "$MUTATION_MARKER"; exit 0; else exit "$?"; fi\n')
            invalid_values = [
                ('backup_missing', ['--backup']),
                ('backup_empty', ['--backup', '']),
                ('backup_option_value', ['--backup', '--service']),
                ('service_option_value', ['--service', '--help']),
                ('service_empty', ['--service', '']),
                ('directory_option_value', ['--ensure-dir', '--owner']),
                ('directory_empty', ['--ensure-dir', '']),
                ('owner_missing', ['--owner']),
                ('owner_empty', ['--owner', '']),
                ('owner_option_value', ['--owner', '--help']),
                ('action_with_owner_option_value', ['--ensure-dir', 'fixture-dir', '--owner', '--backup']),
                ('backup_leading_dash_literal_requires_path', ['--backup', '-literal']),
            ]
            for name, values in invalid_values:
                marker = fixture / ('invalid-' + name + '.marker')
                result = subprocess.run([str(args.bash), '-c', invalid_harness, 'fixture', shell_path, marker.as_posix(), *values],
                                        capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
                record('bash_invalid_' + name, result.returncode, 2, {'stdout': result.stdout, 'stderr': result.stderr})
                record('bash_invalid_' + name + '_no_mutation_or_followup', int(marker.exists()), 0)
            literal = fixture / '--name'
            literal.write_text('literal filename', encoding='utf-8')
            result = subprocess.run([str(args.bash), shell_path, '--dry-run', '--backup', './--name'], cwd=fixture,
                                    capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_leading_dash_filename_explicit_path', result.returncode, 0, {'stdout': result.stdout, 'stderr': result.stderr})

            # W03: snapshot a private copy, then publish without clobbering.
            backup_source = fixture / 'snapshot source.txt'
            backup_source.write_text('snapshot original\n', encoding='utf-8')
            snapshot_harness = 'source "$1"\nDATE="fixture-snapshot"\nbackup_conf "$2"\n'
            snapshot = Path(str(backup_source) + '_ORG_fixture-snapshot')
            result = subprocess.run([str(args.bash), '-c', snapshot_harness, 'fixture', shell_path, backup_source.as_posix()],
                                    capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_backup_snapshot_status', result.returncode, 0, {'stdout': result.stdout, 'stderr': result.stderr})
            record('bash_backup_success_log_delivered', int('backup: ' not in result.stderr), 0)
            record('bash_backup_snapshot_stage_cleanup', int(bool(list(fixture.glob(backup_source.name + '_ORG_fixture-snapshot.stage.*')))), 0)
            backup_source.write_text('live source changed\n', encoding='utf-8')
            record('bash_backup_snapshot_independent_of_live_source', int(not snapshot.exists() or snapshot.read_text(encoding='utf-8') != 'snapshot original\n'), 0)
            snapshot_before = snapshot.read_bytes() if snapshot.exists() else b''
            result = subprocess.run([str(args.bash), '-c', snapshot_harness, 'fixture', shell_path, backup_source.as_posix()],
                                    capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_existing_snapshot_collision_status', result.returncode, 1, {'stdout': result.stdout, 'stderr': result.stderr})
            record('bash_existing_snapshot_collision_preserves_bytes', int(not snapshot.exists() or snapshot.read_bytes() != snapshot_before), 0)

            publish_failure = 'source "$1"\nDATE="fixture-publish-fail"\nln() { return 11; }\nif backup_conf "$2"; then printf "AFTER_BACKUP\\n"; exit 0; else exit "$?"; fi\n'
            result = subprocess.run([str(args.bash), '-c', publish_failure, 'fixture', shell_path, backup_source.as_posix()],
                                    capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
            record('bash_publish_failure_status', result.returncode, 11, {'stdout': result.stdout, 'stderr': result.stderr})
            record('bash_publish_failure_stops_followup', int('AFTER_BACKUP' in result.stdout or 'backup: ' in result.stderr), 0)
            record('bash_publish_failure_no_overwrite_fallback', int(Path(str(backup_source) + '_ORG_fixture-publish-fail').exists()), 0)
            record('bash_publish_failure_stage_cleanup', int(bool(list(fixture.glob(backup_source.name + '_ORG_fixture-publish-fail.stage.*')))), 0)
            record('bash_copy_failure_stage_cleanup', int(bool(list(fixture.glob(valid.name + '_ORG_*.stage.*')))), 0)

            # Pause one actual publication, complete another snapshot, then
            # verify the loser cannot replace the winner's completed bytes.
            race_source = fixture / 'race snapshot source.txt'
            race_source.write_text('older snapshot\n', encoding='utf-8')
            ready, proceed = fixture / 'publish-ready', fixture / 'publish-proceed'
            race_snapshot = Path(str(race_source) + '_ORG_fixture-race')
            paused_publish = ('source "$1"\nDATE="fixture-race"\nREADY=$3\nPROCEED=$4\n'
                              'ln() { : > "$READY"; local attempt; for ((attempt=0; attempt<300; attempt++)); do '
                              'if [ -f "$PROCEED" ]; then command ln "$@"; return "$?"; fi; sleep 0.02; done; return 99; }\n'
                              'backup_conf "$2"\n')
            winner_publish = 'source "$1"\nDATE="fixture-race"\nbackup_conf "$2"\n'
            loser = subprocess.Popen([str(args.bash), '-c', paused_publish, 'fixture', shell_path, race_source.as_posix(), ready.as_posix(), proceed.as_posix()],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', env=bash_env)
            try:
                deadline = time.monotonic() + 6
                while not ready.exists() and loser.poll() is None and time.monotonic() < deadline:
                    time.sleep(0.02)
                record('bash_race_publication_barrier_ready', int(not ready.exists()), 0)
                race_source.write_text('winner snapshot\n', encoding='utf-8')
                winner = subprocess.run([str(args.bash), '-c', winner_publish, 'fixture', shell_path, race_source.as_posix()],
                                        capture_output=True, encoding='utf-8', timeout=20, env=bash_env)
                winner_bytes = race_snapshot.read_bytes() if race_snapshot.exists() else b''
                proceed.write_text('continue', encoding='utf-8')
                stdout, stderr = loser.communicate(timeout=20)
                record('bash_race_winner_status', winner.returncode, 0, {'stdout': winner.stdout, 'stderr': winner.stderr})
                record('bash_race_loser_status', loser.returncode, 1, {'stdout': stdout, 'stderr': stderr})
                record('bash_race_completed_snapshot_preserved', int(not race_snapshot.exists() or race_snapshot.read_bytes() != winner_bytes or winner_bytes != race_source.read_bytes()), 0)
                record('bash_race_loser_stage_cleanup', int(bool(list(fixture.glob(race_source.name + '_ORG_fixture-race.stage.*')))), 0)
            finally:
                if loser.poll() is None:
                    loser.kill()
                loser.wait()

    text = json.dumps(public, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    if args.raw:
        raw['public'] = public
        args.raw.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(text, end='')
    return int(any(item['code'] != item['expected'] for item in public))


if __name__ == '__main__':
    sys.exit(main())
