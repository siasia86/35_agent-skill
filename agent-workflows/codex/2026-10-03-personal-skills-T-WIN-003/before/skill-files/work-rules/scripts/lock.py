#!/usr/bin/env python3
"""Cooperating-agent lock for native Windows/POSIX; never breaks old locks.

Use Python 3.11+ with -X utf8. O_EXCL is not a filesystem-wide security
boundary against noncooperating writers. Windows mode is not an ACL promise.
"""
import argparse
import contextlib
import datetime
import getpass
import json
import os
from pathlib import Path
import socket
import stat
import sys


def identity(info):
    """Return the filesystem identity used for conservative own-file cleanup."""
    return info.st_dev, info.st_ino


def reject_reparse(info):
    """Reject a symlink or a reparse point visible to Python lstat/fstat."""
    if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400):
        raise ValueError('symlink/reparse paths are not supported')


def safe_root(root):
    """Check existing root components without silently resolving a junction."""
    candidate = Path(os.path.abspath(os.fspath(root)))
    for part in [*reversed(candidate.parents), candidate]:
        info = part.lstat()
        reject_reparse(info)
        if not stat.S_ISDIR(info.st_mode):
            raise ValueError('root must be a directory')
    return candidate


def unlink_owned(path, owned):
    """Remove only the still-present, regular inode created by this call."""
    try:
        current = path.lstat()
    except FileNotFoundError:
        return
    reject_reparse(current)
    if stat.S_ISREG(current.st_mode) and identity(current) == identity(owned):
        path.unlink()


@contextlib.contextmanager
def guard(root):
    """Serialize cooperating operations and clean up only this new gate."""
    path = root / '.kiro-lock.guard'
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    owned = os.fstat(fd)
    try:
        os.write(fd, b'cooperating lock operation\n')
        os.close(fd)
        fd = None
        yield
    finally:
        if fd is not None:
            os.close(fd)
        unlink_owned(path, owned)


def read_owned(path, token):
    """Read a regular matching lock, checking open and path identities."""
    before = path.lstat()
    reject_reparse(before)
    if not stat.S_ISREG(before.st_mode):
        raise ValueError('lock is not a regular file')
    fd = os.open(path, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
    with os.fdopen(fd, 'r', encoding='utf-8') as stream:
        actual = os.fstat(stream.fileno())
        reject_reparse(actual)
        if identity(before) != identity(actual):
            raise ValueError('lock replaced while opening')
        data = json.load(stream)
    current = path.lstat()
    reject_reparse(current)
    if identity(current) != identity(actual):
        raise ValueError('lock replaced while reading')
    if data.get('session') != token or data.get('user') != getpass.getuser() or data.get('host') != socket.gethostname():
        raise ValueError('lock belongs to a different session/user/host')
    if hasattr(os, 'getuid') and actual.st_uid != os.getuid():
        raise ValueError('lock has a different filesystem owner')
    return actual


def acquire(path, payload):
    """Create exclusively; remove only our own inode if committing fails."""
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    owned = os.fstat(fd)
    try:
        stream = os.fdopen(fd, 'w', encoding='utf-8', newline='\n')
        fd = None
        with stream:
            json.dump(payload, stream, ensure_ascii=False)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        if fd is not None:
            os.close(fd)
        # Never remove a pre-existing lock or a replacement inode. Guard is
        # still held by the caller while cleaning up this failed acquisition.
        unlink_owned(path, owned)
        raise


def main(argv=None):
    """Acquire/check/release one current-session lock, returning its status."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['acquire', 'check', 'release'])
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--token', required=True, help='private current session token, at least 16 characters')
    parser.add_argument('--task', default='')
    args = parser.parse_args(argv)
    if len(args.token) < 16:
        parser.error('token must contain at least 16 characters')
    try:
        root = safe_root(args.root)
        path = root / '.kiro-lock'
        # Existing, abandoned, foreign or malformed locks/gates block. The
        # tool never treats elapsed time or same user/host as release authority.
        with guard(root):
            if args.operation == 'acquire':
                payload = {'user': getpass.getuser(), 'host': socket.gethostname(),
                           'started': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'session': args.token, 'task': args.task}
                acquire(path, payload)
            else:
                owned = read_owned(path, args.token)
                if args.operation == 'release':
                    current = path.lstat()
                    reject_reparse(current)
                    if identity(current) != identity(owned):
                        raise ValueError('lock replaced before release')
                    path.unlink()
        print(args.operation + ': OK')
        return 0
    except KeyboardInterrupt:
        print(args.operation + ': BLOCKED (KeyboardInterrupt)', file=sys.stderr)
        return 130
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        # Do not print payloads, private tokens or paths.
        print(f'{args.operation}: BLOCKED ({type(exc).__name__})', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
