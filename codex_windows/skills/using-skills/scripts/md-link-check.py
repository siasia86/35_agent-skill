#!/usr/bin/env python3
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script
"""
md-link-check.py — Markdown 내부 링크 존재 여부 검증
====================================================

사용법:
    python md-link-check.py <file_or_dir> [file_or_dir ...]
    python md-link-check.py ./
    python md-link-check.py README.md
    python md-link-check.py -v ./

검증 대상:
    - [text](relative/path.md) 형태의 상대경로 링크
    - [text](./path) 형태 포함

검증 제외:
    - http:// https:// 외부 링크
    - #anchor 앵커 링크
    - 코드블록 내부 링크
    - 인라인 코드 내부 링크

종료 코드:
    0 = 모든 링크 정상
    1 = 깨진 링크 발견 또는 읽기 실패
    2 = 닫히지 않은 코드 펜스로 검사 미완료
"""

VERSION = "26.10.03"

import argparse
import os
import re
import sys
from md_common import configure_utf8_output, display_path, strip_fenced_code, iter_inline_links

# ── patterns ──────────────────────────────────────────────────────────────────

LINK_PATTERN = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
INLINE_CODE_PATTERN = re.compile(r'`+.+?`+')


def _blank_inline(m):
    """인라인 코드를 동일 길이 공백으로 치환."""
    return ' ' * len(m.group(0))

# ── functions ─────────────────────────────────────────────────────────────────

def parse_args():
    """커맨드라인 인자 파싱."""
    parser = argparse.ArgumentParser(
        description='Markdown 내부 링크 존재 여부 검증',
        epilog='Examples:\n'
               '  python md-link-check.py README.md\n'
               '  python md-link-check.py ./\n'
               '  python md-link-check.py -v README.md    파일별 링크 수 출력\n',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('paths', nargs='+', help='.md 파일 또는 디렉토리')
    parser.add_argument('-v', '--verbose', action='store_true', help='파일별 링크 수 출력')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {VERSION}')
    return parser.parse_args()


def collect_md_files(paths):
    """경로 목록에서 .md 파일 수집. 존재하지 않는 경로는 경고 출력."""
    files = []
    for p in paths:
        if not os.path.exists(p):
            print(f"🟡 경로 없음: {p}", file=sys.stderr)
            continue
        if os.path.isfile(p) and p.endswith('.md'):
            files.append(p)
        elif os.path.isdir(p):
            for root, dirs, filenames in os.walk(p, followlinks=False):
                dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '__pycache__', '.venv')]
                for f in filenames:
                    if f.endswith('.md'):
                        files.append(os.path.join(root, f))
    return sorted(set(files))


class UnclosedCodeBlockError(ValueError):
    """A fence prevented completion of a file's link check."""


def strip_code_blocks_preserve_lines(content, filepath=None):
    """Remove fenced/inline code while preserving source line numbers."""
    clean, open_line = strip_fenced_code(content)
    if open_line is not None:
        label = display_path(filepath) if filepath else '<content>'
        message = f'unclosed code block: {label} (last open: L{open_line})'
        print(f'🟡 {message}', file=sys.stderr)
        raise UnclosedCodeBlockError(message)
    return '\n'.join(INLINE_CODE_PATTERN.sub(_blank_inline, line)
                     for line in clean.split('\n'))

def extract_link_path(raw_link):
    """Extract a destination with angle/parenthesis/title and URL decoding."""
    return next(iter_inline_links('[link](' + raw_link + ')'), ('', ''))[1]

def check_file(filepath):
    """파일 내 상대 링크 검증. (broken_list, total_count) 튜플 반환."""
    try:
        with open(filepath, encoding='utf-8') as f:
            raw_content = f.read()
    except (UnicodeDecodeError, OSError) as e:
        return ([(-1, f"[읽기 실패: {e}]", filepath)], 0)

    clean = strip_code_blocks_preserve_lines(raw_content, filepath=filepath)
    base_dir = os.path.dirname(os.path.abspath(filepath))
    broken = []
    link_count = 0

    for i, line in enumerate(clean.splitlines(), 1):
        for link, link_path in iter_inline_links(line):

            # 외부 링크, 앵커 제외
            if link_path.startswith(('http://', 'https://', '#', 'mailto:')):
                continue

            if not link_path:
                continue

            link_count += 1

            # 상대경로 해석
            target = os.path.normpath(os.path.join(base_dir, link_path))
            if not os.path.exists(target):
                broken.append((i, link, target))

    return (broken, link_count)


# ── entry point ───────────────────────────────────────────────────────────────

def main():
    """메인 실행."""
    configure_utf8_output()
    args = parse_args()
    missing_inputs = [p for p in args.paths if not os.path.exists(p)]
    files = collect_md_files(args.paths)

    if not files:
        print("대상 .md 파일 없음")
        sys.exit(1 if missing_inputs else 0)

    total_broken = 0
    incomplete_files = 0
    total_links = 0
    broken_files = []

    for filepath in files:
        try:
            broken, link_count = check_file(filepath)
        except UnclosedCodeBlockError:
            incomplete_files += 1
            continue
        total_links += link_count
        if broken:
            total_broken += len(broken)
            broken_files.append((filepath, broken))
        if args.verbose and link_count > 0 and not broken:
            rel = display_path(filepath)
            print(f"  ✅ {rel} ({link_count} links)")

    # 출력
    if broken_files:
        for filepath, broken_list in broken_files:
            rel = display_path(filepath)
            print(f"\n❌ {rel}")
            for lineno, link, target in broken_list:
                print(f"   L{lineno}: {link}")
    elif not incomplete_files and not missing_inputs:
        print("✅ 모든 링크 정상")
    if incomplete_files:
        print(f"🟡 검사 미완료: 닫히지 않은 코드 펜스 {incomplete_files}개 파일")

    print(f"\n{'─' * 60}")
    print(f"검사 파일: {len(files)}개 | 링크: {total_links}개 | 깨진 링크: {total_broken}건")

    sys.exit(2 if incomplete_files else (1 if total_broken > 0 or missing_inputs else 0))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
