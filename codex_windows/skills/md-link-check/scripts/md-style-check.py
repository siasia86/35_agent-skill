#!/usr/bin/env python3
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script
"""
md-style-check.py — Markdown 스타일 검사 도구
STYLE.md 규칙 기반: 표 정렬, 다이어그램 폭/한글/박스 문자, H1 개수,
이모지 공백, bold 괄호, 반말체, 과장 표현, 푸터, _reference 규칙

사용법:
  python3 md-style-check.py <path> [path ...]
  python3 md-style-check.py <path> -E <dir> -X <file> --no-diagram-kr
  python3 md-style-check.py <path> --strict
  python3 md-style-check.py <path> --config <file>
  python3 md-style-check.py -V

대상 경로의 상위 디렉터리에서 .md-style-check.toml을 자동 탐색합니다.
설정 파일의 skip_checks에 검사 키를 추가하면 해당 저장소에만 적용됩니다.

옵션:
  -E, --exclude-dir DIR     제외할 디렉토리명 (여러 번 사용 가능)
  -X, --exclude-file FILE   제외할 파일명 (여러 번 사용 가능)
  --no-<check>              특정 검사 항목 제외 (--help 참고)
  -s, --strict              과장 표현 whitelist 없이 전체 검사
  -V, --version             버전 출력
"""

VERSION = "26.10.10"

import argparse
import os
import re
import sys
import tomllib
import unicodedata
from functools import lru_cache
from md_common import configure_utf8_output, display_path, fence_info, iter_inline_links, mask_inline_code, strip_blockquote_prefix, strip_fenced_code

# ── 컬러 ──────────────────────────────────────────────────────────────────────

RED    = '\033[0;31m'
GREEN  = '\033[0;32m'
YELLOW = '\033[1;33m'
PURPLE = '\033[0;35m'
CYAN   = '\033[0;36m'
NC     = '\033[0m'

# ── 유틸 ──────────────────────────────────────────────────────────────────────

_FENCE_RE = re.compile(r'^\s*(`{3,})([^`]*)$')
_BLOCKQUOTE_PREFIX_RE = re.compile(r'^\s*(?:>\s?)+')


def _strip_blockquote_prefix(line):
    """Normalize the quote container without changing code body indentation."""
    return strip_blockquote_prefix(line)

def _fence_info(line):
    """Return (fence character, length, info) for backticks and tildes."""
    return fence_info(line)

def dw(s):
    """display width: 한글/전각=2, 나머지=1. 인라인 코드 백틱 포함."""
    w = 0
    for c in s:
        if unicodedata.east_asian_width(c) in ('W', 'F'):
            w += 2
        else:
            w += 1
    return w

def split_table_row(line):
    """표 행을 열로 분할. 백틱 내부의 | 는 무시."""
    stripped = line.strip().strip("|")
    cells = []
    current = ""
    in_backtick = False
    for c in stripped:
        if c == "`":
            in_backtick = not in_backtick
            current += c
        elif c == "|" and not in_backtick:
            cells.append(current)
            current = ""
        else:
            current += c
    cells.append(current)
    return cells

@lru_cache(maxsize=1)
def strip_code_blocks(content):
    """Blank fenced code while preserving original diagnostic line numbers."""
    return strip_fenced_code(content)[0]


@lru_cache(maxsize=1)
def get_code_blocks(content):
    """(lang, body) 튜플 리스트를 반환하며 fence 길이를 기준으로 닫습니다."""
    blocks = []
    lines = content.split('\n')
    fence_length = None
    fence_char = None
    lang = ''
    body_lines = []
    for line in lines:
        info = _fence_info(line)
        if fence_length is None and info:
            fence_char, fence_length = info[0], info[1]
            lang = info[2]
            body_lines = []
        elif (fence_length is not None and info
              and info[0] == fence_char and info[1] >= fence_length and not info[2]):
            blocks.append((lang, '\n'.join(body_lines)))
            fence_length = None
            fence_char = None
        elif fence_length is not None:
            body_lines.append(_strip_blockquote_prefix(line))
    return blocks

def strip_frontmatter(content):
    """frontmatter 제거 후 반환."""
    return re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

# ── 검사 함수 ─────────────────────────────────────────────────────────────────

def check_h1(content, strict=False):
    """H1이 정확히 1개인지 확인."""
    body = strip_frontmatter(content)
    body = strip_code_blocks(body)
    h1s = re.findall(r'^# .+', body, re.MULTILINE)
    if len(h1s) != 1:
        return [f"H1 {len(h1s)}개 (1개여야 함): {h1s}"]
    return []

# 출력 결과/UI 경로 패턴 (태그 없이 허용)
_OUTPUT_PATTERN_SOURCES = (
    r'^(?:\d|\.\.\.|\[|SUCCESS|FAILED|ok:|changed:|fatal:|PLAY|TASK|\$|>|#|\*\*|Status|URL:|http)',
    r'|→|\| SUCCESS|\| FAILED|\| CHANGED',
    r'|^[A-Z][a-z]+ →',           # UI 경로 (Grafana →, Jenkins →)
    r'|Securing |Enter password|New password',  # 인터랙티브 출력
    r'|^VPN Client>',  # SoftEther vpncmd 세션
    r'|^Match |^Password|^Permit|^Allow|^Deny',  # sshd_config 등 설정
    r'|^(frontend|backend|global|listen|defaults)\b',  # haproxy 설정
    r'|^prefork:|^worker:|^event:',  # Apache MPM
    r'|^[가-힣].+:',  # 한글 항목 헤더 (사용 조건:, 장점:, 단점: 등)
    r'|^- ',  # 불릿 리스트
    r'|^[A-Z][A-Z_a-z ]+:',  # 대문자 시작 영문 키 (CAP_NET_ADMIN:, PID Namespace: 등)
    r'|^[a-z_]+:',  # 소문자 키 (cpu:, memory: 등)
    r'|^[가-힣/]',  # 한글 또는 슬래시(/) 시작 텍스트 블록
    r'|^[✓✗]',  # 체크마크 기호
)
_OUTPUT_PATTERNS = re.compile(''.join(_OUTPUT_PATTERN_SOURCES))

def check_code_lang(content, strict=False):
    """언어 태그 없는 코드블록 검사.
    허용 목록: 트리/다이어그램, URL, 명령어 출력, UI 경로, 로그, 순수 텍스트 흐름."""
    issues = []
    for lang, body in get_code_blocks(content):
        lang = lang.strip()
        if lang:
            continue
        # 트리/다이어그램 문자 포함 — 허용
        if any(c in body for c in ['├──', '└──', '│', '┌', '┐', '└', '┘', '─']):
            continue
        lines = [l for l in body.strip().splitlines() if l.strip()]
        if not lines:
            continue
        first_line = lines[0].strip()
        if first_line.startswith('http'):
            continue
        if first_line.startswith('#') or _OUTPUT_PATTERNS.search(first_line):
            continue
        match_count = sum(1 for l in lines if _OUTPUT_PATTERNS.search(l.strip()))
        if match_count >= len(lines) * 0.3:
            continue
        issues.append(f"언어 태그 없는 코드블록: '{first_line[:50]}'")
    return issues

def check_tables(content, strict=False):
    """표 정렬 검사: 셀 raw 길이 = col_max_dw + 2, 구분선 길이 = col_max_dw + 2."""
    issues = []
    clean = strip_code_blocks(content)
    clean = strip_frontmatter(clean)

    for m in re.finditer(r'((?:\|[^\n]+\|\n)+)', clean):
        block = m.group(1).strip().splitlines()
        if len(block) < 2:
            continue

        rows_raw = [split_table_row(l) for l in block]
        rows_str = [[c.strip() for c in r] for r in rows_raw]

        sep_idx = next(
            (i for i, r in enumerate(rows_str)
             if r and all(re.match(r'^-+$', c) for c in r if c)),
            None
        )
        if sep_idx is None:
            continue

        data_rows = [r for i, r in enumerate(rows_str) if i != sep_idx]
        if not data_rows:
            continue
        ncols = max(len(r) for r in data_rows)
        if ncols == 0:
            continue
        col_widths = [
            max((dw(r[i]) if i < len(r) else 0) for r in data_rows)
            for i in range(ncols)
        ]

        for idx, (raw_row, str_row) in enumerate(zip(rows_raw, rows_str)):
            is_sep = str_row and all(re.match(r'^-+$', c) for c in str_row if c)
            if is_sep:
                for i, c in enumerate(str_row):
                    if i < ncols:
                        expected = col_widths[i] + 2
                        actual = len(c)
                        if actual != expected:
                            issues.append(
                                f"표 구분선 열{i+1}: 길이={actual}, 기대={expected} | '{block[idx][:60]}'"
                            )
            else:
                for i, raw_c in enumerate(raw_row):
                    if i < ncols:
                        cell_content = raw_c.strip()
                        expected_raw = 2 + len(cell_content) + col_widths[i] - dw(cell_content)
                        actual_raw = len(raw_c)
                        if actual_raw != expected_raw:
                            issues.append(
                                f"표 셀 열{i+1}: raw_len={actual_raw}, 기대={expected_raw} | '{cell_content}'"
                            )
    return issues

def check_diagram(content, strict=False):
    """중첩 박스를 포함한 닫힌 다이어그램의 행 display width를 검사합니다."""
    issues = []
    for _lang, body in get_code_blocks(content):
        lines = body.splitlines()
        if not any('┌' in line for line in lines):
            continue
        box_depth = 0
        box_lines = []
        for line in lines:
            starts_box = line.lstrip().startswith('┌')
            opening_count = line.count('┌') if box_depth or starts_box else 0
            closing_count = line.count('└') if box_depth else 0
            if box_depth == 0 and opening_count == 0:
                continue
            if opening_count:
                box_depth += opening_count
            if box_depth:
                box_lines.append(line)
            if closing_count:
                box_depth -= closing_count
            if box_depth == 0 and box_lines:
                check_lines = [bl for bl in box_lines
                               if bl.strip().startswith(('┌', '│', '└'))
                               and '┼' not in bl
                               and bl.strip().endswith(('┐', '│', '┘', '┤', '─'))]
                if check_lines:
                    widths = [dw(bl) for bl in check_lines]
                    max_w = max(widths)
                    for bl, current_width in zip(check_lines, widths):
                        if current_width != max_w:
                            issues.append(
                                f"다이어그램 행 폭 불일치: dw={current_width} "
                                f"(최대={max_w}) | '{bl[:50]}'"
                            )
                box_lines = []
    return issues


def check_diagram_box_chars(content, strict=False):
    """다이어그램 박스 문자 조합 정합성 검사.

    행의 양 끝(시작 문자 ~ 끝 문자)만 검사합니다.
    중간에 ┬┴┼ 등 분기 문자가 있는 것은 정상입니다.

    규칙: 행에서 ┌├└ 로 시작하는 세그먼트가 최종적으로 어떤 문자로 끝나는지 확인.
    - ┌ 로 시작 → 같은 세그먼트 마지막이 ┐ 또는 중간에 ┬┴┼ 경유 후 ┐ 로 끝나야 함
    - └ 로 시작 → ┘ 로 끝나야 함
    - ├ 로 시작 → ┤ 로 끝나야 함

    단, ┬/┴/┼ 는 경유 문자로 허용 (분기/합류 다이어그램).
    """
    issues = []
    for _lang, body in get_code_blocks(content):
        for i, line in enumerate(body.splitlines(), 1):
            stripped = line.rstrip()
            if not stripped:
                continue
            # 독립 세그먼트 추출: 공백으로 분리된 박스 단위
            parts = stripped.split()
            for part in parts:
                if not part:
                    continue
                # ├───┐ 같은 순수 잘못된 조합 (중간에 다른 박스문자 없이 직접 연결)
                m = re.match(r'^([┌├└])([─]+)([┐┘┤┼┬┴])$', part)
                if m:
                    start_ch = m.group(1)
                    end_ch = m.group(3)
                    valid = False
                    if start_ch == '┌' and end_ch in ('┐', '┬'):
                        valid = True
                    elif start_ch == '└' and end_ch in ('┘', '┴'):
                        valid = True
                    elif start_ch == '├' and end_ch in ('┤', '┼', '┬', '┴', '┐'):
                        valid = True
                    if not valid:
                        issues.append(
                            f"박스 문자 오류: '{start_ch}...{end_ch}' ('{start_ch}'는 '{end_ch}'로 끝날 수 없음) | '{stripped[:50]}'"
                        )
        # 박스 상/하단 라인에 ─와 ┐/┘ 사이 공백 혼입 검출
        for i, line in enumerate(body.splitlines(), 1):
            stripped = line.rstrip()
            if re.search(r'─\s+┐', stripped):
                issues.append(
                    f"박스 상단 공백 혼입: ─ 와 ┐ 사이에 공백 | '{stripped[:60]}'"
                )
            if re.search(r'─\s+┘', stripped):
                issues.append(
                    f"박스 하단 공백 혼입: ─ 와 ┘ 사이에 공백 | '{stripped[:60]}'"
                )
    return issues

def check_diagram_korean(content, strict=False):
    """박스 다이어그램 내부 한글 사용 여부를 검사합니다."""
    issues = []
    all_lines = content.split('\n')
    in_block = False
    fence_length = None
    fence_char = None
    block_start = 0
    block_body = []
    for i, line in enumerate(all_lines, 1):
        info = _fence_info(line)
        if not in_block and info:
            in_block = True
            fence_char, fence_length = info[0], info[1]
            block_start = i + 1
            block_body = []
        elif (in_block and info and info[0] == fence_char and info[1] >= fence_length and not info[2]):
            block_text = '\n'.join(block_body)
            if '┌' in block_text and '┘' in block_text:
                for j, block_line in enumerate(block_body):
                    korean = re.findall(r'[가-힣]+', block_line)
                    if korean:
                        lineno = block_start + j
                        issues.append(
                            f"L{lineno}: 다이어그램 내부 한글 사용: "
                            f"{korean[:3]} (영문 권장)"
                        )
            in_block = False
            fence_length = None
            fence_char = None
        elif in_block:
            block_body.append(_strip_blockquote_prefix(line))
    return issues

# 기본 상태 8개와 사용자가 허용한 기존 보조 기호 5개.
_ALLOWED_EMOJIS = ['✅', '❌', '🟡', '🟢', '🔴', '★', '☆', '💡', '✓', '✗', '🟠', '🔵', '🟣']
_EMOJI_SPACE_TARGETS = ['✅', '❌', '🟡', '🟢', '🔴', '🟠', '🔵', '🟣']
_EMOJI_PATTERN = re.compile(
    r'(' + '|'.join(re.escape(e) for e in _EMOJI_SPACE_TARGETS) + r')[\ufe0e\ufe0f]?([^\s|`\ufe0e\ufe0f])'
)
# Derived from Unicode Emoji 15.1 Emoji property (Unicode, Inc., 2023).
# https://www.unicode.org/Public/15.1.0/ucd/emoji/emoji-data.txt
# Terms: https://www.unicode.org/terms_of_use.html
_EMOJI_CHAR_CLASS = r"""\u0023\u002a\u0030-\u0039\u00a9\u00ae\u203c\u2049\u2122\u2139\u2194-\u2199\u21a9-\u21aa\u231a-\u231b\u2328\u23cf\u23e9-\u23f3\u23f8-\u23fa\u24c2\u25aa-\u25ab\u25b6\u25c0\u25fb-\u25fe\u2600-\u2604\u260e\u2611\u2614-\u2615\u2618\u261d\u2620\u2622-\u2623\u2626\u262a\u262e-\u262f\u2638-\u263a\u2640\u2642\u2648-\u2653\u265f-\u2660\u2663\u2665-\u2666\u2668\u267b\u267e-\u267f\u2692-\u2697\u2699\u269b-\u269c\u26a0-\u26a1\u26a7\u26aa-\u26ab\u26b0-\u26b1\u26bd-\u26be\u26c4-\u26c5\u26c8\u26ce-\u26cf\u26d1\u26d3-\u26d4\u26e9-\u26ea\u26f0-\u26f5\u26f7-\u26fa\u26fd\u2702\u2705\u2708-\u270d\u270f\u2712\u2714\u2716\u271d\u2721\u2728\u2733-\u2734\u2744\u2747\u274c\u274e\u2753-\u2755\u2757\u2763-\u2764\u2795-\u2797\u27a1\u27b0\u27bf\u2934-\u2935\u2b05-\u2b07\u2b1b-\u2b1c\u2b50\u2b55\u3030\u303d\u3297\u3299\U0001f004\U0001f0cf\U0001f170-\U0001f171\U0001f17e-\U0001f17f\U0001f18e\U0001f191-\U0001f19a\U0001f1e6-\U0001f1ff\U0001f201-\U0001f202\U0001f21a\U0001f22f\U0001f232-\U0001f23a\U0001f250-\U0001f251\U0001f300-\U0001f321\U0001f324-\U0001f393\U0001f396-\U0001f397\U0001f399-\U0001f39b\U0001f39e-\U0001f3f0\U0001f3f3-\U0001f3f5\U0001f3f7-\U0001f4fd\U0001f4ff-\U0001f53d\U0001f549-\U0001f54e\U0001f550-\U0001f567\U0001f56f-\U0001f570\U0001f573-\U0001f57a\U0001f587\U0001f58a-\U0001f58d\U0001f590\U0001f595-\U0001f596\U0001f5a4-\U0001f5a5\U0001f5a8\U0001f5b1-\U0001f5b2\U0001f5bc\U0001f5c2-\U0001f5c4\U0001f5d1-\U0001f5d3\U0001f5dc-\U0001f5de\U0001f5e1\U0001f5e3\U0001f5e8\U0001f5ef\U0001f5f3\U0001f5fa-\U0001f64f\U0001f680-\U0001f6c5\U0001f6cb-\U0001f6d2\U0001f6d5-\U0001f6d7\U0001f6dc-\U0001f6e5\U0001f6e9\U0001f6eb-\U0001f6ec\U0001f6f0\U0001f6f3-\U0001f6fc\U0001f7e0-\U0001f7eb\U0001f7f0\U0001f90c-\U0001f93a\U0001f93c-\U0001f945\U0001f947-\U0001f9ff\U0001fa70-\U0001fa7c\U0001fa80-\U0001fa88\U0001fa90-\U0001fabd\U0001fabf-\U0001fac5\U0001face-\U0001fadb\U0001fae0-\U0001fae8\U0001faf0-\U0001faf8"""
_EMOJI_COMPONENT = '[' + _EMOJI_CHAR_CLASS + '★☆✓✗]' + r'[\ufe0e\ufe0f]?[\U0001f3fb-\U0001f3ff]?'
_ALL_EMOJI_PATTERN = re.compile(
    _EMOJI_COMPONENT + r'(?:\u200d' + _EMOJI_COMPONENT + r')*\u20e3?'
)
# ASCII markers, copyright, arrows and math/text symbols are not decorative
# emoji unless an explicit emoji selector or keycap is attached.
_TEXT_STYLE_SYMBOLS = set('#*0123456789©®™ℹ↔↕↖↗↘↙↩↪♀♂')


def _mask_indented_emoji_code(content):
    """Mask indented code without treating list prose as root-level code.

    Code needs a block boundary, four spaces beyond its list container,
    and cannot interrupt an existing paragraph. Keep diagnostic line numbers.
    """
    result = []
    containers = []
    paragraph_open = False
    code_indent = None
    for line in content.splitlines(keepends=True):
        expanded = line.expandtabs(4)
        indent = len(expanded) - len(expanded.lstrip(' '))
        text = expanded.strip()
        if not text:
            paragraph_open = False
            result.append(line)
            continue
        if code_indent is not None:
            if indent >= code_indent:
                result.append(''.join(c if c in '\r\n' else ' ' for c in line))
                continue
            code_indent = None
            paragraph_open = False
        while containers and indent < containers[-1]:
            containers.pop()
        required_indent = (containers[-1] if containers else 0) + 4
        if not paragraph_open and indent >= required_indent:
            code_indent = required_indent
            result.append(''.join(c if c in '\r\n' else ' ' for c in line))
            continue
        marker = re.match(r'^( *)(?:[-+*]|\d{1,9}[.)])([ ]+)(.*)$', expanded.rstrip('\r\n'))
        if marker and indent < required_indent:
            # More than four padding spaces means one padding space followed
            # by code indentation, rather than an over-wide list container.
            padding = len(marker.group(2))
            content_indent = marker.start(3) - (padding - 1 if padding > 4 else 0)
            containers.append(content_indent)
            paragraph_open = bool(marker.group(3).strip()) and padding <= 4
            if padding > 4:
                code_indent = content_indent + 4
                result.append(''.join(c if c in '\r\n' else ' ' for c in line))
                continue
        elif re.match(r'^(?:#{1,6}\s|>|(?:-{3,}|\*{3,}|_{3,})\s*$)', text):
            paragraph_open = False
        else:
            paragraph_open = True
        result.append(line)
    return ''.join(result)


def _emoji_prose(content):
    clean = mask_inline_code(_mask_indented_emoji_code(strip_code_blocks(content)))
    for line_number, line in enumerate(clean.splitlines(), 1):
        if line.lstrip().startswith('>'):
            continue
        # Preserve exact inline link destinations/paths, not the visible label.
        for raw, _ in iter_inline_links(line):
            destination = '](' + raw + ')'
            line = line.replace(destination, '](' + ' ' * len(raw) + ')')
        yield line_number, line.strip()


def check_emoji_space(content, strict=False):
    """Require the existing spacing rule for eight status markers only."""
    issues = []
    for line_number, line in _emoji_prose(content):
        for emoji, next_char in _EMOJI_PATTERN.findall(line):
            issues.append(f"L{line_number}: '{emoji}' 뒤 공백 없음 → '{emoji}{next_char}'")
    return issues


def check_emoji_disallowed(content, strict=False):
    """Check authored prose; preserve code, quoted originals and link paths."""
    issues = []
    allowed = set(_ALLOWED_EMOJIS)
    for line_number, line in _emoji_prose(content):
        for match in _ALL_EMOJI_PATTERN.finditer(line):
            symbol = match.group()
            normalized = symbol[:-1] if symbol.endswith(('\ufe0e', '\ufe0f')) else symbol
            if normalized in allowed or symbol in _TEXT_STYLE_SYMBOLS:
                continue
            if symbol.endswith('\ufe0e') and normalized in _TEXT_STYLE_SYMBOLS:
                continue
            issues.append(f"L{line_number}: 비허용 이모지 '{symbol}' — 허용: {' '.join(_ALLOWED_EMOJIS)}")
    return issues


def check_bold_parentheses(content, strict=False):
    """Bold(**) 안에 괄호가 포함된 경우 검출.

    일부 마크다운 렌더러(GitHub 포함)는 **text(...)** 형태에서
    ')' 뒤의 '**'를 bold 닫힘으로 인식하지 못합니다.
    원인: 파서가 ')' 를 bold 범위의 종료 지점으로 혼동하는 엣지 케이스.
    해결: 괄호를 bold 밖으로 이동 — **text**(...)
    """
    if not strict:
        return []
    issues = []
    clean = strip_code_blocks(content)
    for i, line in enumerate(clean.splitlines(), 1):
        # **...(...)** 패턴 검출 (** 안에 ( ) 포함)
        for m in re.finditer(r'[*][*][^*]*[(]([^)]{10,})[)][^*]*[*][*]', line):
            matched = m.group(0)
            paren_content = m.group(1)
            if ' ' not in paren_content:
                continue
            # 표 셀 내 **A** 단독 사용은 제외 (괄호 없는 경우는 이미 필터됨)
            issues.append(
                f"L{i}: bold 안에 괄호 포함 (렌더링 깨짐 가능) → '{matched}'"
            )
    return issues

def check_footer(content, strict=False):
    """README 푸터 존재 여부 (작성일, 마지막 업데이트, 저작권)."""
    issues = []
    if '**작성일**' not in content:
        issues.append("푸터 누락: **작성일** 없음")
    if '**마지막 업데이트**' not in content:
        issues.append("푸터 누락: **마지막 업데이트** 없음")
    if '© ' not in content:
        issues.append("푸터 누락: 저작권(©) 없음")
    return issues

# 반말체 종결어미 패턴
_BANMAL_PATTERN = re.compile(
    r'[가-힣]이다[.\s]|[가-힣]한다[.\s]|[가-힣]된다[.\s]|[가-힣]있다[.\s]'
    r'|[가-힣]없다[.\s]|[가-힣]않는다[.\s]|[가-힣]아니다[.\s]'
)

def check_banmal(content, strict=False):
    """반말체 종결어미 검사 (STYLE.md § 10). 코드블록/인용구/헤더/표 제외."""
    issues = []
    clean = strip_code_blocks(content)
    for i, line in enumerate(clean.splitlines(), 1):
        stripped = line.strip()
        if (not stripped
                or stripped.startswith(('#', '|', '*', '!', '>', '©', '-'))):
            continue
        if re.search(r'[가-힣]', stripped) and _BANMAL_PATTERN.search(stripped):
            issues.append(f"L{i}: {stripped[:80]}")
    return issues


# 합니다체 마침표 누락 패턴
_PERIOD_MISSING_PATTERN = re.compile(
    r'[가-힣](니다|합니다|됩니다|있습니다|없습니다|않습니다|아닙니다|입니다)$'
)

def check_period_missing(content, strict=False):
    """합니다체 종결어미 뒤 마침표 누락 검사 (STYLE.md § 10). 코드블록/인용구/헤더/표/불릿 제외."""
    issues = []
    all_lines = content.split('\n')
    in_block = False
    fence_length = None
    fence_char = None
    for i, line in enumerate(all_lines, 1):
        info = _fence_info(line)
        if not in_block and info:
            in_block = True
            fence_char, fence_length = info[0], info[1]
            continue
        elif (in_block and info and info[0] == fence_char and info[1] >= fence_length and not info[2]):
            in_block = False
            fence_length = None
            fence_char = None
            continue
        if in_block:
            continue
        stripped = line.strip()
        if (not stripped
                or stripped.startswith(('#', '|', '*', '!', '>', '©', '-', '['))):
            continue
        if _PERIOD_MISSING_PATTERN.search(stripped):
            issues.append(f"L{i}: 마침표 누락 → '{stripped[-40:]}'")
    return issues

# 과장 표현 패턴
_EXAGGERATION_PATTERN  = re.compile(r'완전한|완벽한|최고의|최강의|완전 |완벽 |최고 |최강 ')
_EXAGGERATION_WHITELIST = re.compile(
    r'완전 이진|완전 그래프|완전 격리|완전 지원|완전 일관성|완전 오버라이딩'
    r'|최고 추론|최고 성능.*→'
    r'|완전한 하드웨어|완전한 제어|완전한 자유 소프트웨어|완전한 빌드|완전한 데이터'
    r'|최고 \|'
)

def check_exaggeration(content, strict=False):
    """Inspect prose; preserve fenced code, same-line literals and quotations.

    An unmatched inline delimiter cannot mask later lines. An unclosed fence
    makes this check incomplete instead of silently accepting hidden prose.
    Strict mode still disables the technical-term whitelist for prose.
    """
    issues = []
    clean, unclosed = strip_fenced_code(content)
    if unclosed is not None:
        issues.append(f"L{unclosed}: 닫히지 않은 코드 펜스 — 문체 검사 미완료")
    for i, line in enumerate(clean.splitlines(), 1):
        if line.lstrip().startswith('>'):
            continue
        stripped = mask_inline_code(line).strip()
        if re.search(r'[가-힣]', stripped) and _EXAGGERATION_PATTERN.search(stripped):
            if strict or not _EXAGGERATION_WHITELIST.search(stripped):
                issues.append(f"L{i}: {stripped[:80]}")
    return issues

def check_reference(content, path, strict=False):
    """_reference/ 파일 전용 검사."""
    issues = []
    path = os.path.normpath(path).replace('\\', '/')
    if '/_reference/' not in '/' + path:
        return issues
    fm = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm:
        issues.append("_reference: frontmatter 없음")
        return issues
    fm_text = fm.group(1)
    if 'sources:' not in fm_text:
        issues.append("_reference: frontmatter에 sources 없음")
    if 'last_checked:' not in fm_text:
        issues.append("_reference: frontmatter에 last_checked 없음")
    return issues

# ── 검사 목록 ─────────────────────────────────────────────────────────────────

CHECKS = [
    # (key,             display_name,        function)
    ("h1",              "H1 개수",           check_h1),
    ("table",           "표 정렬",           check_tables),
    ("diagram-width",   "다이어그램 행 폭",  check_diagram),
    ("diagram-kr",      "다이어그램 한글",   check_diagram_korean),
    ("box-chars",       "박스 문자 정합",    check_diagram_box_chars),
    ("emoji",           "이모지 뒤 공백",    check_emoji_space),
    ("emoji-disallow",  "비허용 이모지",     check_emoji_disallowed),
    ("bold-paren",      "bold 괄호",         check_bold_parentheses),
    ("banmal",          "반말체 종결어미",   check_banmal),
    ("period",          "마침표 누락",       check_period_missing),
    ("exaggeration",    "과장 표현",         check_exaggeration),
    ("footer",          "푸터",              check_footer),
    ("reference",       "_reference 규칙",   check_reference),
]

# _reference 파일은 푸터 불필요
REFERENCE_SKIP = {"footer"}
# .kiro 내부 문서는 푸터 불필요
# INDEX.md는 _reference 규칙 적용 제외
INDEX_SKIP = {"reference"}
# 99_archive 파일은 푸터 불필요
ARCHIVE_SKIP = {"footer"}

# 파일별 특정 검사 항목 제외입니다.
#
# 각 항목은 (검사명 집합, 사유, 재검토 시점) 3요소를 갖습니다. 사유 없는 제외는
# 시간이 지나면 근거를 확인할 수 없게 되고, 근거가 사라진 뒤에도 남아 검사 공백이
# 됩니다. 실제로 2026-06-23 에 도입된 파일 단위 제외 목록은 사유 기록이 없어
# 근거를 추적할 수 없었고, 그 안에 실제 결함 26건이 2개월간 가려져 있었습니다.
#
# 재검토 시점은 날짜 또는 조건으로 적습니다. `상시` 는 문서 성격상 항구적인 예외를
# 뜻합니다 (예: 외부 프로젝트 원문 보존).
FILE_SKIP = {}


def _should_skip_for_file(filepath, check_name):
    """파일 경로 기반 특정 검사 항목 제외 여부."""
    for pattern, entry in FILE_SKIP.items():
        skip_checks = entry[0] if isinstance(entry, tuple) else entry
        if pattern in filepath and check_name in skip_checks:
            return True
    return False


def list_file_skip():
    """FILE_SKIP 항목을 (경로, 검사, 사유, 재검토) 목록으로 반환."""
    rows = []
    for pattern, entry in sorted(FILE_SKIP.items()):
        if isinstance(entry, tuple):
            checks, reason, review = entry
        else:
            checks, reason, review = entry, "미확인 — 점검 필요", "미정"
        rows.append((pattern, ", ".join(sorted(checks)), reason, review))
    return rows

# CLI skip 옵션과 내부 검사 키의 매핑
_SKIP_FLAG_ATTRIBUTES = {
    'h1': 'no_h1',
    'table': 'no_table',
    'diagram-width': 'no_diagram_width',
    'diagram-kr': 'no_diagram_kr',
    'box-chars': 'no_box_chars',
    'emoji': 'no_emoji',
    'emoji-disallow': 'no_emoji_disallow',
    'bold-paren': 'no_bold_paren',
    'banmal': 'no_banmal',
    'exaggeration': 'no_exaggeration',
    'footer': 'no_footer',
    'period': 'no_period',
    'reference': 'no_reference',
}

# ── 파일 처리 ─────────────────────────────────────────────────────────────────

def _should_skip_for_config(filepath, check_name, file_skip, path_skip):
    """설정 파일의 file_skip·path_skip 예외 적용 여부를 반환합니다."""
    normalized = os.path.normpath(os.path.abspath(filepath))
    for entry in file_skip:
        if normalized == entry['path'] and check_name in entry['checks']:
            return True
    for entry in path_skip:
        base = entry['path']
        if (normalized == base or normalized.startswith(base + os.sep))                 and check_name in entry['checks']:
            return True
    return False


def check_file(path, strict=False, skip_checks=None, file_skip=None, path_skip=None):
    """단일 파일 검사. [(항목명, 이슈메시지), ...] 반환."""
    try:
        with open(path, encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [("파일 읽기", f"실패: {e}")]

    native_path = os.path.normpath(path).replace('\\', '/')
    is_reference = '/_reference/' in native_path or native_path.startswith('_reference/') or native_path.startswith('./_reference/')
    is_index = os.path.basename(path) == 'INDEX.md'
    is_archive = "/99_archive/" in native_path or native_path.startswith("99_archive/") or native_path.startswith("./99_archive/")
    all_issues = []

    for key, name, fn in CHECKS:
        if is_reference and key in REFERENCE_SKIP:
            continue
        if is_index and key in INDEX_SKIP:
            continue
        if is_archive and key in ARCHIVE_SKIP:
            continue
        if _should_skip_for_file(path, key):
            continue
        if _should_skip_for_config(path, key, file_skip or [], path_skip or []):
            continue
        if skip_checks and key in skip_checks:
            continue
        try:
            if name == "_reference 규칙":
                issues = check_reference(content, path, strict)
            else:
                issues = fn(content, strict)
            all_issues.extend([(name, iss) for iss in issues])
        except Exception as e:
            all_issues.append((name, f"검사 오류: {e}"))

    return all_issues

# 검사 제외 디렉토리
EXCLUDE_DIRS = {'.git', '__pycache__', 'node_modules', '.venv'}

# 검사 제외 파일
# 기본값은 비어 있습니다. 파일 전체를 빼면 표 정렬·문체 검사가 함께 빠지므로,
# 특정 항목만 제외해야 하는 경우 FILE_SKIP 을 사용합니다.
EXCLUDE_FILES = set()


CONFIG_LIST_KEYS = ('exclude_dirs', 'exclude_files', 'skip_checks')
CONFIG_ENTRY_KEYS = ('file_skip', 'path_skip')


def _read_config(config_path):
    """TOML 설정 파일을 읽고 목록·예외 항목과 검사명을 검증합니다."""
    with open(config_path, 'rb') as config_file:
        config = tomllib.load(config_file)

    version = config.get('version', 1)
    if isinstance(version, bool) or not isinstance(version, int):
        raise ValueError("config key 'version' must be an integer")
    allowed_keys = {'version', *CONFIG_LIST_KEYS, *CONFIG_ENTRY_KEYS}
    unknown_keys = set(config) - allowed_keys
    if unknown_keys:
        invalid = ', '.join(sorted(unknown_keys))
        available = ', '.join(sorted(allowed_keys))
        raise ValueError(
            f"unknown config keys: {invalid}; available keys: {available}"
        )

    result = {}
    for key in CONFIG_LIST_KEYS:
        if key not in config:
            continue
        values = config[key]
        if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
            raise ValueError(f"config key '{key}' must be a string list")
        result[key] = values

    valid_checks = set(_SKIP_FLAG_ATTRIBUTES)
    unknown_checks = set(result.get('skip_checks', [])) - valid_checks
    for key in CONFIG_ENTRY_KEYS:
        entries = config.get(key, [])
        if not isinstance(entries, list) or not all(isinstance(entry, dict) for entry in entries):
            raise ValueError(f"config key '{key}' must be a table list")
        result[key] = []
        for entry in entries:
            unknown_entry_keys = set(entry) - {'path', 'checks', 'reason', 'review'}
            if unknown_entry_keys:
                invalid = ', '.join(sorted(unknown_entry_keys))
                raise ValueError(f"{key} entry has unknown keys: {invalid}")
            path = entry.get('path')
            checks = entry.get('checks')
            reason = entry.get('reason')
            review = entry.get('review')
            if not isinstance(path, str) or not path:
                raise ValueError(f"{key} entry path must be a non-empty string")
            if not isinstance(checks, list) or not all(isinstance(check, str) for check in checks):
                raise ValueError(f"{key} entry checks must be a string list")
            if not isinstance(reason, str) or not reason:
                raise ValueError(f"{key} entry reason must be a non-empty string")
            if not isinstance(review, str) or not review:
                raise ValueError(f"{key} entry review must be a non-empty string")
            result[key].append({
                'path': path,
                'checks': checks,
                'reason': reason,
                'review': review,
            })
            unknown_checks.update(set(checks) - valid_checks)

    if unknown_checks:
        available = ', '.join(sorted(_SKIP_FLAG_ATTRIBUTES))
        invalid = ', '.join(sorted(unknown_checks))
        raise ValueError(
            f"config skip checks contains unknown checks: {invalid}; "
            f"available checks: {available}"
        )
    return result


def _merge_config(base, override):
    """기본 설정과 저장소 설정을 중복 없이 병합합니다."""
    merged = {key: list(base.get(key, [])) for key in CONFIG_LIST_KEYS}
    merged.update({key: list(base.get(key, [])) for key in CONFIG_ENTRY_KEYS})
    for key in CONFIG_LIST_KEYS + CONFIG_ENTRY_KEYS:
        for value in override.get(key, []):
            if value not in merged[key]:
                merged[key].append(value)
    return merged


def _resolve_config_entries(config, config_path):
    """설정 파일 기준 상대 경로를 절대 경로로 변환합니다."""
    resolved = {key: list(values) for key, values in config.items()}
    base_dir = os.path.dirname(os.path.abspath(config_path))
    for key in CONFIG_ENTRY_KEYS:
        resolved[key] = []
        for entry in config.get(key, []):
            item = dict(entry)
            item['path'] = os.path.normpath(os.path.join(base_dir, item['path']))
            resolved[key].append(item)
    return resolved


def _global_config_path():
    """검사기 저장소의 공통 설정 경로를 반환합니다."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '.md-style-check.toml')


def find_config_path(target):
    """대상 파일 또는 디렉터리에서 상위로 저장소 설정을 탐색합니다."""
    current = os.path.abspath(target)
    if not os.path.isdir(current):
        current = os.path.dirname(current)

    while True:
        candidate = os.path.join(current, '.md-style-check.toml')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def load_config(config_path=None, target=None):
    """공통 설정과 대상 저장소의 TOML 설정을 병합합니다."""
    config = {
        'exclude_dirs': sorted(EXCLUDE_DIRS),
        'exclude_files': sorted(EXCLUDE_FILES),
        'skip_checks': [],
        'file_skip': [],
        'path_skip': [],
    }
    global_path = _global_config_path()
    if os.path.isfile(global_path):
        config = _merge_config(
            config,
            _resolve_config_entries(_read_config(global_path), global_path),
        )

    selected_path = config_path or (find_config_path(target) if target else None)
    if selected_path:
        selected_path = os.path.abspath(selected_path)
        if not os.path.isfile(selected_path):
            raise FileNotFoundError(f"config not found: {selected_path}")
        if os.path.normpath(selected_path) != os.path.normpath(global_path):
            config = _merge_config(
                config,
                _resolve_config_entries(_read_config(selected_path), selected_path),
            )
    elif config_path:
        raise FileNotFoundError(f"config not found: {config_path}")
    return config


def _is_excluded_dir(path, dirname, target_abs, skip_dirs):
    """디렉토리명 또는 저장소 기준 상대 경로의 제외 여부 반환."""
    if dirname in skip_dirs:
        return True
    candidates = set()
    for base in (target_abs, os.path.dirname(os.path.abspath(__file__))):
        try:
            candidates.add(os.path.normpath(os.path.relpath(path, base)))
        except ValueError:
            # Relative exclusions cannot match across native Windows drives.
            continue
    for excluded in skip_dirs:
        normalized = os.path.normpath(excluded)
        if '/' not in normalized and os.sep not in normalized:
            continue
        if normalized in candidates:
            return True
    return False


def collect_files(target, extra_exclude_dirs=None, exclude_files=None,
                  base_exclude_dirs=None, base_exclude_files=None):
    """파일 또는 디렉토리에서 .md 파일 목록 반환."""
    if os.path.isfile(target):
        if exclude_files and os.path.basename(target) in exclude_files:
            return []
        return [target]
    skip_dirs = set(base_exclude_dirs or EXCLUDE_DIRS) | set(extra_exclude_dirs or [])
    skip_files = set(base_exclude_files or EXCLUDE_FILES) | set(exclude_files or [])
    result = []
    target_abs = os.path.abspath(target)
    if _is_excluded_dir(target_abs, os.path.basename(target_abs), target_abs, skip_dirs):
        return []
    for root, dirs, files in os.walk(target):
        dirs[:] = [
            d for d in dirs
            if not _is_excluded_dir(os.path.join(root, d), d, target_abs, skip_dirs)
        ]
        dirs.sort()
        for f in sorted(files):
            if not f.endswith('.md') or f in skip_files:
                continue
            # 루트 디렉토리의 README.md만 제외
            if f == 'README.md' and os.path.abspath(root) == target_abs:
                continue
            result.append(os.path.join(root, f))
    return result

# ── 진입점 ────────────────────────────────────────────────────────────────────

def parse_args():
    """커맨드라인 인자 파싱."""
    parser = argparse.ArgumentParser(
        description='Markdown 스타일 검사 도구 (STYLE.md 규칙 기반)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "\nExamples:\n"
            "  %(prog)s ./01_install/                  디렉토리 전체 검사\n"
            "  %(prog)s ./01_install/nginx_install.md  단일 파일 검사\n"
            "  %(prog)s ./_reference/ --strict         과장 표현 whitelist 없이 전체 검사\n"
            "  %(prog)s ./ -E 99_ETC -E 90_DELETE       디렉토리 제외\n"
            "  %(prog)s ./ -X vim_airline.md            파일 제외\n"
            "  %(prog)s ./ --no-diagram-kr              다이어그램 한글 검사 제외\n"
            "\nChecks:\n"
            "  H1 개수          문서당 H1 정확히 1개\n"
            "  표 정렬          한글 display width 기준 셀 패딩\n"
            "  다이어그램 행 폭  박스 다이어그램 내부 행 폭 일치\n"
            "  다이어그램 한글  박스 다이어그램 내부 영문 권장\n"
            "  이모지 뒤 공백   ✅❌🟡🟢🔴🟠🔵🟣 뒤 공백 1칸 필수\n"
            "  반말체 종결어미  ~이다/한다/된다 등 금지\n"
            "  과장 표현        완전/완벽/최고/최강 등 금지 (--strict: whitelist 무시)\n"
            "  푸터             작성일/마지막 업데이트/저작권 필수\n"
            "  _reference 규칙  sources/last_checked frontmatter 필수\n"
        )
    )
    parser.add_argument('targets', nargs='*', metavar='path',
                        help='검사할 파일 또는 디렉토리 (여러 개 가능)')
    parser.add_argument('-E', '--exclude-dir', action='append', default=[],
                        dest='exclude_dirs', metavar='DIR',
                        help='제외할 디렉토리명 (여러 번 사용 가능)')
    parser.add_argument('--config', metavar='FILE',
                        help='TOML 설정 파일 (미지정 시 대상 경로에서 .md-style-check.toml 자동 탐색)')
    parser.add_argument('-X', '--exclude-file', action='append', default=[],
                        dest='exclude_files', metavar='FILE',
                        help='제외할 파일명 (여러 번 사용 가능)')
    # 검사 항목 제외 플래그
    skip_group = parser.add_argument_group('skip options', '특정 검사 항목 제외')
    skip_group.add_argument('--no-diagram-kr', action='store_true', help='다이어그램 한글 검사 제외')
    skip_group.add_argument('--no-diagram-width', action='store_true', help='다이어그램 행 폭 검사 제외')
    skip_group.add_argument('--no-table', action='store_true', help='표 정렬 검사 제외')
    skip_group.add_argument('--no-emoji', action='store_true', help='이모지 뒤 공백 검사 제외')
    skip_group.add_argument('--no-emoji-disallow', action='store_true', help='비허용 이모지 검사 제외')
    skip_group.add_argument('--no-banmal', action='store_true', help='반말체 종결어미 검사 제외')
    skip_group.add_argument('--no-exaggeration', action='store_true', help='과장 표현 검사 제외')
    skip_group.add_argument('--no-footer', action='store_true', help='푸터 검사 제외')
    skip_group.add_argument('--no-h1', action='store_true', help='H1 개수 검사 제외')
    skip_group.add_argument('--no-box-chars', action='store_true', help='박스 문자 정합 검사 제외')
    skip_group.add_argument('--no-bold-paren', action='store_true', help='bold 괄호 검사 제외')
    skip_group.add_argument('--no-period', action='store_true', help='마침표 누락 검사 제외')
    skip_group.add_argument('--no-reference', action='store_true', help='_reference 규칙 검사 제외')

    parser.add_argument('-s', '--strict', action='store_true',
                        help='과장 표현 whitelist 없이 전체 검사')
    parser.add_argument('--list-skips', action='store_true',
                        help='파일별 검사 제외 항목과 사유 출력 후 종료')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {VERSION}')
    return parser.parse_args()


def _print_file_skips():
    """FILE_SKIP 목록을 표로 출력. 사유 미확인 항목이 있으면 종료 코드 1."""
    rows = [("경로", "제외 검사", "사유", "재검토")] + list_file_skip()

    def dw(s):
        return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)

    widths = [max(dw(r[i]) for r in rows) for i in range(4)]
    for idx, row in enumerate(rows):
        line = "| " + " | ".join(
            cell + " " * (widths[i] - dw(cell)) for i, cell in enumerate(row)
        ) + " |"
        print(line)
        if idx == 0:
            print("|" + "|".join("-" * (w + 2) for w in widths) + "|")

    pending = [r for r in rows[1:] if r[2].startswith("미확인")]
    print(f"\n총 {len(rows) - 1}건 | 사유 미확인 {len(pending)}건")
    if pending:
        print("사유가 기록되지 않은 제외 항목이 있습니다. 근거를 확인하거나 제외를 해제하세요.")
    return 1 if pending else 0


def main():
    configure_utf8_output()
    args = parse_args()
    if args.list_skips:
        sys.exit(_print_file_skips())
    if not args.targets:
        print("검사 대상 경로를 지정하세요. 사용법은 -h 를 참고합니다.", file=sys.stderr)
        sys.exit(2)
    missing_inputs = [p for p in args.targets if not os.path.exists(p)]
    for path in missing_inputs:
        print(f'🟡 경로 없음: {path}', file=sys.stderr)
    try:
        target_configs = []
        for target in args.targets:
            config = load_config(args.config, target=target)
            target_configs.append((target, config, find_config_path(target) if not args.config else args.config))
    except (OSError, tomllib.TOMLDecodeError, ValueError) as error:
        print(f"설정 로드 실패: {error}", file=sys.stderr)
        sys.exit(1)

    configured_exclude_dirs = set()
    configured_exclude_files = set()
    config_sources = set()
    files = []
    file_config_skips = {}
    config_file_skips = []
    config_path_skips = []
    for target, config, config_source in target_configs:
        configured_exclude_dirs.update(config['exclude_dirs'])
        configured_exclude_files.update(config['exclude_files'])
        config_file_skips.extend(config.get('file_skip', []))
        config_path_skips.extend(config.get('path_skip', []))
        if config_source:
            config_sources.add(os.path.abspath(config_source))
        target_files = collect_files(
            target,
            args.exclude_dirs,
            args.exclude_files,
            config['exclude_dirs'],
            config['exclude_files'],
        )
        for fpath in target_files:
            files.append(fpath)
            file_config_skips.setdefault(fpath, set()).update(config['skip_checks'])

    if not files:
        print("검사할 .md 파일이 없습니다.")
        sys.exit(1)

    # 제외 현황 출력
    all_exclude_dirs = sorted(configured_exclude_dirs | set(args.exclude_dirs))
    all_exclude_files = sorted(configured_exclude_files | set(args.exclude_files)) + ['README.md (루트)']
    cli_skip_checks = [key for key, attribute in _SKIP_FLAG_ATTRIBUTES.items()
                       if getattr(args, attribute)]
    configured_skip_checks = sorted({
        check for checks in file_config_skips.values() for check in checks
    } | {
        check
        for entry in config_file_skips + config_path_skips
        for check in entry['checks']
    })
    all_skip_checks = sorted(set(cli_skip_checks) | set(configured_skip_checks))

    if config_sources:
        print(f"{YELLOW}[설정] {', '.join(sorted(config_sources))}{NC}")
    if all_exclude_dirs or all_exclude_files or all_skip_checks:
        print(f"{YELLOW}[제외] 디렉토리: {', '.join(all_exclude_dirs)}{NC}")
        print(f"{YELLOW}[제외] 파일: {', '.join(all_exclude_files)}{NC}")
        if all_skip_checks:
            print(f"{YELLOW}[제외] 검사: {', '.join(all_skip_checks)}{NC}")
        print()

    total_issues = 0
    for fpath in files:
        skip_checks = sorted(set(cli_skip_checks) | file_config_skips.get(fpath, set()))
        issues = check_file(
            fpath,
            strict=args.strict,
            skip_checks=skip_checks,
            file_skip=config_file_skips,
            path_skip=config_path_skips,
        )
        rel = display_path(fpath)
        if issues:
            print(f"\n{RED}❌ {rel}{NC}")
            for name, iss in issues:
                print(f"   {YELLOW}[{name}]{NC} {iss}")
            total_issues += len(issues)
        else:
            print(f"{GREEN}✅ {rel}{NC}")

    print(f"\n{'─'*60}")
    if total_issues:
        print(f"{RED}검사 파일: {len(files)}개 | 이슈: {total_issues}건{NC}")
    else:
        print(f"{GREEN}검사 파일: {len(files)}개 | 이슈: {total_issues}건{NC}")
    sys.exit(1 if total_issues or missing_inputs else 0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
