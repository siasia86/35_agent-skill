#!/usr/bin/env python3
"""Cooperating-agent project lock. Standard library; never breaks stale locks."""
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


@contextlib.contextmanager
def guard(root):
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
        current = path.lstat()
        if (current.st_dev, current.st_ino) == (owned.st_dev, owned.st_ino):
            path.unlink()


def read_owned(path, token):
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise ValueError('lock is not a regular file')
    fd = os.open(path, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
    with os.fdopen(fd, 'r', encoding='utf-8') as stream:
        actual = os.fstat(stream.fileno())
        if (before.st_dev, before.st_ino) != (actual.st_dev, actual.st_ino):
            raise ValueError('lock replaced while opening')
        data = json.load(stream)
    if data.get('session') != token or data.get('user') != getpass.getuser() or data.get('host') != socket.gethostname():
        raise ValueError('lock belongs to a different session/user/host')
    if hasattr(os, 'getuid') and actual.st_uid != os.getuid():
        raise ValueError('lock has a different filesystem owner')
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['acquire', 'check', 'release'])
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--token', required=True, help='current session token; keep it private to this task')
    parser.add_argument('--task', default='')
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    if not root.is_dir() or not args.token or len(args.token) < 16:
        parser.error('root must be a directory and token must contain at least 16 characters')
    path = root / '.kiro-lock'
    try:
        # This gate serializes helpers following this protocol. An abandoned gate
        # blocks the operation; it is never silently removed. Uncooperative writers
        # require repository isolation, not a promise of filesystem-wide locking.
        with guard(root):
            if args.operation == 'acquire':
                payload = {'user': getpass.getuser(), 'host': socket.gethostname(),
                           'started': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'session': args.token, 'task': args.task}
                fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                    json.dump(payload, stream, ensure_ascii=False)
                    stream.write('\n')
                    stream.flush()
                    os.fsync(stream.fileno())
            else:
                owned = read_owned(path, args.token)
                if args.operation == 'release':
                    current = path.lstat()
                    if (current.st_dev, current.st_ino) != (owned.st_dev, owned.st_ino):
                        raise ValueError('lock replaced before release')
                    path.unlink()
        print(args.operation + ': OK')
        return 0
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        # Do not echo the lock body/token or silently treat missing locks as owned.
        print(f'{args.operation}: BLOCKED ({type(exc).__name__})', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
