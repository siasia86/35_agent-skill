"""Test actual prose validation and preserved literals in each active consumer."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile


CASES = [
    ('seven_statuses', '✅ 완료\n❌ 실패\n🟡 대기\n🟢 진행\n🔴 중단\n🟠 조율\n🔵 참고', False),
    ('rating_and_existing_symbols', '★★☆☆☆ 💡 설명 ✓ 확인 ✗ 표시', False),
    ('bare_bmp_warning', '\u26a0 주의', True),
    ('bmp_emoji_selector', '\u26a0\ufe0f 주의', True),
    ('bmp_text_selector_not_bypass', '\u26a0\ufe0e 주의', True),
    ('allowed_glyph_extended_selector', '✅\ufe0f 완료', False),
    ('allowed_glyph_text_selector', '✅\ufe0e 완료', False),
    ('allowed_auxiliary_selector', '💡\ufe0f 설명', False),
    ('supplementary_picture', '\U0001f680 시작', True),
    ('regional_flag', '\U0001f1f0\U0001f1f7 표시', True),
    ('skin_modifier', '\U0001f44d\U0001f3fd 표시', True),
    ('joined_sequence', '\U0001f469\u200d\U0001f4bb 작업', True),
    ('keycap', '1\ufe0f\u20e3 항목', True),
    ('ordinary_math_and_text', 'x ∈ A, ∑ x ≠ 0, √4 = 2, © 2026, A ↔ B, # 1 * 2', False),
    ('explicit_arrow_emoji', '↔\ufe0f 설명', True),
    ('explicit_text_copyright', '©\ufe0e 2026', False),
    ('inline_code', '`\u26a0\ufe0f` 원문', False),
    ('multi_backtick_code', '``literal ` \U0001f680`` 원문', False),
    ('unclosed_inline_code', '`\U0001f680 설명', True),
    ('fenced_code', '```text\n\U0001f680\n```\n설명', False),
    ('tilde_fenced_code', '~~~text\n\u26a0\ufe0f\n~~~', False),
    ('nested_shorter_fence', '````text\n```\n\U0001f680\n```\n````', False),
    ('blockquote_original', '> \U0001f680 원문', False),
    ('nested_blockquote', '  > > \u26a0\ufe0f 원문', False),
    ('code_then_authored_prose', '`원문` \U0001f680 설명', True),
    ('quoted_then_authored_prose', '> \U0001f680 원문\n\u26a0\ufe0f 설명', True),
    ('literal_path', '`C:/\U0001f680/file.md` 경로', False),
    ('link_path', '[원문](<folder/\U0001f680.md>)', False),
    ('nested_link_path', '[원문](folder/(\U0001f680).md)', False),
    ('link_label_is_authored', '[\U0001f680 설명](folder/file.md)', True),
    ('root_indented_code', '    \U0001f680 원문\n    \u26a0\ufe0f 원문', False),
    ('indented_code_then_prose', '    \U0001f680 원문\n\n\u26a0\ufe0f 설명', True),
    ('tab_indented_code', '\t\U0001f680 원문', False),
    ('indent_cannot_interrupt_paragraph', '일반 설명\n    \U0001f680 설명', True),
    ('list_indented_prose', '- 항목\n\n    \U0001f680 설명', True),
    ('list_indented_code', '- 항목\n\n      \U0001f680 원문', False),
    ('ordered_list_prose', '1. 항목\n\n    \U0001f680 설명', True),
    ('ordered_list_code', '1. 항목\n\n       \U0001f680 원문', False),
    ('nested_list_prose', '- 항목\n  - 하위\n\n      \U0001f680 설명', True),
    ('nested_list_code', '- 항목\n  - 하위\n\n        \U0001f680 원문', False),
    ('list_first_line_code_padding', '-     \U0001f680 원문', False),
    ('ordered_first_line_code_padding', '1.     \U0001f680 원문', False),
    ('list_short_padding_is_prose', '-  \U0001f680 설명', True),
    ('quoted_indented_original', '>     \U0001f680 원문\n\n\u26a0\ufe0f 설명', True),
]
SPACE_CASES = [
    ('new_status_space_required', '🟠조율', True),
    ('new_info_space_required', '🔵참고', True),
    ('rating_unchanged', '★★☆☆☆', False),
    ('auxiliary_spacing_unchanged', '💡설명 ✓표시 ✗표시', False),
    ('inline_spacing_preserved', '`🟡원문`', False),
    ('quote_spacing_preserved', '> 🟡원문', False),
    ('allowed_selector_spacing', '✅\ufe0f 완료', False),
    ('allowed_selector_without_spacing', '✅\ufe0f완료', True),
    ('indented_spacing_preserved', '    🟡원문', False),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--skills', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []
    paths = sorted(args.skills.resolve().glob('*/scripts/md-style-check.py'))
    if not paths:
        raise RuntimeError('No actual checker consumers')
    for path in paths:
        sys.path.insert(0, str(path.parent))
        spec = importlib.util.spec_from_file_location('emoji_' + path.parent.parent.name.replace('-', '_'), path)
        checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checker)
        for name, content, expected_failure in CASES:
            observed = bool(checker.check_emoji_disallowed(content))
            checks.append({'consumer': path.parent.parent.name, 'case': name,
                           'expected_failure': expected_failure, 'passed': observed == expected_failure})
        for name, content, expected_failure in SPACE_CASES:
            observed = bool(checker.check_emoji_space(content))
            checks.append({'consumer': path.parent.parent.name, 'case': name,
                           'expected_failure': expected_failure, 'passed': observed == expected_failure})
        with tempfile.TemporaryDirectory(prefix='emoji-policy-') as temporary:
            root = Path(temporary)
            for name, symbol, expected_exit in [('cli_allowed', '🟠 조율', 0), ('cli_reject', '\u26a0\ufe0f 주의', 1)]:
                fixture = root / (name + '.md')
                fixture.write_text('# 검증\n\n' + symbol + '\n', encoding='utf-8')
                result = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(path), '--no-footer', str(fixture)],
                                        capture_output=True, text=True, encoding='utf-8', cwd=temporary)
                checks.append({'consumer': path.parent.parent.name, 'case': name,
                               'expected_exit': expected_exit, 'actual_exit': result.returncode,
                               'passed': result.returncode == expected_exit})
        sys.path.pop(0)
    failures = [case for case in checks if not case['passed']]
    result = {'status': 'FAIL' if failures else 'PASS', 'consumers': len(paths),
              'cases': len(checks), 'checks': checks,
              'checker_sha256': sorted({hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})}
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=True), encoding='utf-8')
    print(json.dumps({'status': result['status'], 'consumers': len(paths),
                      'cases': len(checks), 'failures': failures}, ensure_ascii=True))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
