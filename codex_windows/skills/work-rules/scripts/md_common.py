"""Shared standard-library helpers for the standalone Markdown checkers.

This is a small fence/inline-destination scanner, not a full Markdown renderer.
"""
import re
import os
import sys
from urllib.parse import unquote

_QUOTE_PREFIX = re.compile(r'^ {0,3}>[ \t]?')
_FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')
_LINK_START = re.compile(r'(?<!\\)\[(?:[^\[\]\\]|\\.|\[[^\[\]]*\])*\]\(')


def display_path(path, start=None):
    """Display a relative path when possible, otherwise its native absolute path."""
    try:
        return os.path.relpath(path, start)
    except ValueError:
        return os.path.abspath(path)


def configure_utf8_output():
    """Make native Windows output independent of the active console code page."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='replace')


def strip_blockquote_prefix(line):
    while True:
        match = _QUOTE_PREFIX.match(line)
        if not match:
            return line
        line = line[match.end():]


def fence_info(line):
    match = _FENCE.match(strip_blockquote_prefix(line.rstrip('\r\n')))
    if not match:
        return None
    marker, info = match.groups()
    info = info.strip(' \t')
    if marker[0] == '`' and '`' in info:
        return None
    return marker[0], len(marker), info


def closes_fence(info, opening):
    return bool(info and opening and info[0] == opening[0]
                and info[1] >= opening[1] and not info[2])


def strip_fenced_code(content):
    """Return (line-preserving prose, unclosed-opening-line or None)."""
    lines = []
    opening = None
    open_line = None
    for lineno, line in enumerate(content.split('\n'), 1):
        info = fence_info(line)
        if opening is None and info:
            opening, open_line = info, lineno
            lines.append('')
        elif closes_fence(info, opening):
            opening, open_line = None, None
            lines.append('')
        else:
            lines.append('' if opening else line)
    return '\n'.join(lines), open_line


def _unescape_destination(path):
    # CommonMark backslash escapes apply to ASCII punctuation only.
    path = re.sub(r'\\([!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~])', r'\1', path)
    return unquote(path.split('#', 1)[0])


def iter_inline_links(line):
    """Yield (raw destination/title, decoded path) for valid inline links.

    Supports angle destinations (including spaces), balanced parentheses,
    punctuation escapes, and optional quoted or parenthesized titles.
    Reference-style links and multiline links remain outside this CLI's scope.
    """
    for match in _LINK_START.finditer(line):
        start = i = match.end()
        while i < len(line) and line[i] in ' \t':
            i += 1
        path_start = i
        if i < len(line) and line[i] == '<':
            i += 1
            path_start = i
            while i < len(line):
                if line[i] == '\\' and i + 1 < len(line):
                    i += 2
                elif line[i] == '>':
                    break
                else:
                    i += 1
            if i >= len(line):
                continue
            path = line[path_start:i]
            i += 1
        else:
            depth = 0
            while i < len(line):
                char = line[i]
                if char == '\\' and i + 1 < len(line):
                    i += 2
                    continue
                if char == '(':
                    depth += 1
                elif char == ')':
                    if depth == 0:
                        break
                    depth -= 1
                elif char in ' \t':
                    break
                i += 1
            if depth:
                continue
            path = line[path_start:i]
        path_end = i
        while i < len(line) and line[i] in ' \t':
            i += 1
        # A title must be separated from its destination by whitespace.
        if i > path_end and i < len(line) and line[i] in '\"\'(':
            quote = line[i]
            end_quote = ')' if quote == '(' else quote
            i += 1
            while i < len(line):
                if line[i] == '\\' and i + 1 < len(line):
                    i += 2
                elif line[i] == end_quote:
                    break
                else:
                    i += 1
            if i >= len(line):
                continue
            i += 1
            while i < len(line) and line[i] in ' \t':
                i += 1
        if i < len(line) and line[i] == ')':
            yield line[start:i], _unescape_destination(path)


def unique_heading_anchors(headings, make_anchor):
    """Generate occurrence-sensitive slugs, including suffix collisions."""
    used = set()
    counts = {}
    result = []
    for _, text, _ in headings:
        base = make_anchor(text)
        anchor = base
        while anchor in used:
            counts[base] = counts.get(base, 0) + 1
            anchor = f'{base}-{counts[base]}'
        used.add(anchor)
        result.append(anchor)
    return result
