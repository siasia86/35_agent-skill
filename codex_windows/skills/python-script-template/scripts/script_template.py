#!/usr/bin/env python3
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script
"""script_template.py - 입력 계약과 오류 전파를 갖춘 Windows Python 템플릿.

사용법 (Python 3.11+):
    python -X utf8 script_template.py --help
    python -X utf8 script_template.py -d -v <file>
    python -X utf8 script_template.py -f <file1> <file2>
    python -X utf8 script_template.py -D <directory>

업무 변환은 transform_content()에 구현합니다. 기본 일반 실행은 미구현 오류이며
기본 dry-run은 입력을 검증하고 계획만 기록합니다. restore는 미구현/미광고입니다.
"""

VERSION = '26.10.03'

import argparse
from datetime import datetime
import logging
import os
from pathlib import Path
import re
import stat
import sys
import tempfile

# ── logger ────────────────────────────────────────────────────────────────────
def _setup_logger(name='script_template', log_dir=None):
    """Log to stderr, optionally to a caller-selected UTF-8 monthly file."""
    fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        console = logging.StreamHandler()
        console.setFormatter(fmt)
        logger.addHandler(console)
    if log_dir is not None:
        try:
            directory = Path(log_dir)
            directory.mkdir(parents=True, exist_ok=True)
            log_path = directory / f'{name}_{datetime.now():%Y%m}.log'
            if not any(isinstance(h, logging.FileHandler) and Path(h.baseFilename) == log_path.absolute() for h in logger.handlers):
                file_handler = logging.FileHandler(log_path, encoding='utf-8')
                file_handler.setFormatter(fmt)
                logger.addHandler(file_handler)
        except OSError:
            logger.warning('log file creation failed, console only')
    return logger


log = _setup_logger()

# ── colors ────────────────────────────────────────────────────────────────────
_RED = '\033[0;31m'
_YELLOW = '\033[0;33m'
_GREEN = '\033[0;32m'
_PURPLE = '\033[0;35m'
_GRAY = '\033[0;90m'
_RESET = '\033[0m'


def _c(text, color=_RED):
    """Colorize terminal output while keeping redirected output plain."""
    if sys.stdout.isatty() or sys.stderr.isatty():
        return f'{color}{text}{_RESET}'
    return str(text)

# ── constants ─────────────────────────────────────────────────────────────────
# Put project-specific compiled regexes here, rather than inside processing loops.
# re.compile is deliberately not called until an actual project pattern exists.

# ── utilities ─────────────────────────────────────────────────────────────────
def _reject_reparse(info):
    """Reject symlinks and reparse attributes observable by Python."""
    if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400):
        raise ValueError('symlink/reparse paths are not supported')


def _checked_path(filepath, kind=None):
    """Validate existing path components and the requested file/directory kind."""
    path = Path(os.path.abspath(os.fspath(filepath)))
    for parent in reversed(path.parents):
        info = parent.lstat()
        _reject_reparse(info)
        if not stat.S_ISDIR(info.st_mode):
            raise ValueError('parent is not a directory')
    info = path.lstat()
    _reject_reparse(info)
    if kind == 'file' and not stat.S_ISREG(info.st_mode):
        raise ValueError('target is not a regular file')
    if kind == 'dir' and not stat.S_ISDIR(info.st_mode):
        raise ValueError('target is not a directory')
    if kind is None and not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode)):
        raise ValueError('target must be a regular file or directory')
    return path, info


def _atomic_write(filepath, data):
    """Replace a regular file through a flushed same-directory temporary file.

    Windows ACL/owner/ADS and filesystem-wide hostile path replacement are
    outside this stdlib contract; use target-specific metadata/locking policy.
    """
    path = Path(os.path.abspath(os.fspath(filepath)))
    _checked_path(path.parent, 'dir')
    try:
        _, original = _checked_path(path, 'file')
    except FileNotFoundError:
        original = None
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.tmp_')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            stream.write(data)
            stream.flush()
            if original is not None:
                os.chmod(temporary, stat.S_IMODE(original.st_mode))
            os.fsync(stream.fileno())
        if original is None:
            if path.exists() or path.is_symlink():
                raise ValueError('target appeared before replacement')
        else:
            _, current = _checked_path(path, 'file')
            if (current.st_dev, current.st_ino) != (original.st_dev, original.st_ino):
                raise ValueError('target replaced before commit')
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        except PermissionError:
            # Windows read-only temporaries need their own write bit restored.
            os.chmod(temporary, stat.S_IWRITE)
            os.unlink(temporary)


# ── core functions ────────────────────────────────────────────────────────────
def transform_content(content, filepath):
    """Implement the requested idempotent business transform before writes."""
    raise NotImplementedError('implement transform_content() for the requested task before normal execution')


def process_file(filepath, dry_run=False, verbose=False):
    """Validate/read one UTF-8 file; plan or perform the project's transform."""
    path, _ = _checked_path(filepath, 'file')
    with path.open('r', encoding='utf-8', newline='') as stream:
        content = stream.read()
    if dry_run:
        log.info(f'[dry-run] would invoke project transform: {_c(path, _YELLOW)}')
        if verbose:
            log.info('template has no installed business transform; no content change is promised')
        return
    new_content = transform_content(content, path)
    if not isinstance(new_content, str):
        raise TypeError('transform_content must return text')
    if new_content == content:
        log.info(f'unchanged: {_c(path, _GRAY)}')
        return
    _atomic_write(path, new_content)
    log.info(f'modified: {_c(path, _GREEN)}')


def process_dir(dirpath, dry_run=False, verbose=False):
    """Process immediate regular files, reporting any batch member failures."""
    directory, _ = _checked_path(dirpath, 'dir')
    failures = 0
    for child in sorted(directory.iterdir(), key=lambda p: p.name):
        try:
            info = child.lstat()
            _reject_reparse(info)
            if stat.S_ISDIR(info.st_mode):
                continue  # Recursion is a project-specific feature, not implied.
            process_file(child, dry_run=dry_run, verbose=verbose)
        except (OSError, ValueError, TypeError, NotImplementedError) as exc:
            failures += 1
            log.error(f'failed: {child} ({type(exc).__name__})')
    if failures:
        raise RuntimeError(f'{failures} directory members failed')


# ── entry point ───────────────────────────────────────────────────────────────
def parse_args(argv=None):
    """Parse implemented arguments and return the same parser for no-arg help."""
    parser = argparse.ArgumentParser(
        description='Windows/POSIX Python 업무 변환 템플릿',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            '\nExamples:\n'
            '  %(prog)s -d config.txt             입력 검증과 처리 계획\n'
            '  %(prog)s -d -v config.txt          dry-run 상세 출력\n'
            '  %(prog)s -f config1.txt config2.txt  파일 batch\n'
            '  %(prog)s -D ./configs/             즉시 하위 파일 처리\n'
            '\nNotes:\n'
            '  - 일반 실행 전 transform_content()에 실제 멱등 변환 구현\n'
            '  - 누락/처리 실패가 하나라도 있으면 종료 1; dry-run도 누락 실패\n'
            '  - 기본 stderr 로그; --log-dir를 지정한 경우만 월별 파일 로그\n'
            '  - ACL/owner/ADS 보존, hostile writer 차단, restore는 미구현\n'
        ))
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {VERSION}')
    parser.add_argument('target', nargs='?', help='파일 또는 디렉터리 경로')
    parser.add_argument('-f', '--file', nargs='+', metavar='FILE', help='대상 파일 batch')
    parser.add_argument('-D', '--dir', nargs='+', metavar='DIR', help='대상 디렉터리 batch')
    parser.add_argument('-d', '--dry-run', action='store_true', help='입력 검증과 처리 계획만 출력')
    parser.add_argument('-v', '--verbose', action='store_true', help='상세 출력')
    parser.add_argument('-q', '--quiet', action='store_true', help='에러만 출력')
    parser.add_argument('--log-dir', type=Path, help='요청이 허용한 작업 로그 디렉터리')
    args = parser.parse_args(argv)
    if sum(bool(value) for value in (args.target, args.file, args.dir)) > 1:
        parser.error('choose only target, --file, or --dir')
    return args, parser


def main(argv=None):
    """Dispatch inputs and return nonzero for any missing/failed input."""
    args, parser = parse_args(argv)
    if not (args.target or args.file or args.dir):
        parser.print_help()
        return 0
    _setup_logger(log_dir=args.log_dir)
    log.setLevel(logging.ERROR if args.quiet else logging.DEBUG if args.verbose else logging.INFO)
    targets = [(path, 'file') for path in args.file] if args.file else [(path, 'dir') for path in args.dir] if args.dir else [(args.target, None)]
    failures = 0
    for filepath, kind in targets:
        try:
            path, info = _checked_path(filepath, kind)
            if stat.S_ISDIR(info.st_mode):
                process_dir(path, dry_run=args.dry_run, verbose=args.verbose)
            else:
                process_file(path, dry_run=args.dry_run, verbose=args.verbose)
        except (OSError, ValueError, TypeError, RuntimeError, NotImplementedError) as exc:
            failures += 1
            log.error(f'failed: {filepath} ({type(exc).__name__}: {exc})')
    return 1 if failures else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
