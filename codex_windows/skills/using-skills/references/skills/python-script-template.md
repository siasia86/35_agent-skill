---
name: python-script-template
description: "Python 스크립트 작성 시 표준 구조, 로깅, argparse, 에러 처리 패턴을 적용합니다. 새 스크립트 생성 또는 기존 스크립트 개선 시 사용합니다. 이 skill을 참조할 때 응답 첫 줄에 \"🟡 참조: skill://python-script-template\" 를 출력합니다."
---

# Python Script Template

<!-- CODEX-COMPAT-BEGIN -->
## Windows Codex 실행 및 적용 규칙

이 절과 이 절에서 연결한 실행 도구가 Windows의 현재 실행 본문입니다. 아래 Linux/Kiro 원문의 코드·명령·경로는 전체 보존한 비교 자료이며 그대로 자동 실행하지 않습니다. 원문의 목적·예시·체크리스트는 유지하되 플랫폼 차이와 교정 사항은 이 절의 실행 계약을 적용합니다. Linux 본문은 `codex_linux/`에 보존되어 있으며 이번 이식은 경량화·통합 작업이 아닙니다.

- 시스템·개발자·관리 정책과 실제 권한 안에서 **사용자 명시 지시 > 적용 저장소 AGENTS > 개인 스킬 기본값**을 적용합니다. 이미 부여된 범위와 승인을 유지하고 다른 저장소·개인 홈·시스템·운영 환경의 수정 권한을 경로 존재로 추정하지 않습니다.
- 실제 Git 루트·branch·기존 변경을 먼저 확인합니다. 필요한 본문·동봉 참조만 읽고 다른 스킬·전체 작업 기록을 자동 로드하지 않습니다. 원문의 `skill://`는 아래 로컬 참조로 해석하며 URI 도구를 호출하지 않습니다.
- 이 폴더를 통째로 복사하는 개인 스킬입니다. 필수 참조는 아래 상대 링크를 사용합니다. 중앙 catalog·설치기·다른 저장소 또는 형제 스킬 설치를 필수로 요구하지 않습니다. 원문 `../originals/python-script-template.md`는 비교 자료입니다.
- 네이티브 Windows 작업 셸은 PowerShell입니다. 파일 작업은 `-LiteralPath` 등 실제 대상 인자로 처리하며 셸 문자열·`eval`로 외부 입력을 재해석하지 않습니다. Python 3.11 이상을 `python -X utf8`로 실행하고 Python 하위 실행은 `[sys.executable, '-X', 'utf8', ...]` 인자 배열을 사용합니다. 실제 Python 위치·버전은 현재 환경에서 확인합니다.
- Bash 업무는 Git Bash 또는 승인된 WSL에서 유지합니다. PowerShell에서 Bash/POSIX 예제를 직접 실행하지 않습니다. 원문의 `/root`, `/var/log`, `/backup`, Kiro hook은 과거 환경 자료이며 Windows 개인 홈·시스템 경로로 자동 치환하지 않습니다.
- 검증은 **통과 / 부분 검사 / 실패 / 미실행**을 실행 목적·관찰·다음 조치와 함께 기록합니다. 경로 치환이나 과거 완료 기록을 현재 동작 통과로 사용하지 않습니다. 비공개 경로·계정·토큰·운영 자료를 공개 결과에 복사하지 않습니다.

### 현재 Windows Python 템플릿

실행·생성 기준은 [전체 Python 템플릿](../../scripts/script_template.py)입니다. 원문의 파일 순서, SAFETY 주석, 날짜 VERSION, 한 줄 import, 함수 docstring, logger·color·constants·utilities·core·entry 순서, argparse, KeyboardInterrupt(130), Examples/Notes, 복잡도 표와 간단한 무로거 예외를 유지합니다. 과거 `parse_args/main/_atomic_write` 코드는 비교 자료이며 새 실행에는 동봉 파일의 교정된 함수만 사용합니다.

```powershell
python -X utf8 '<SKILL_DIR>/scripts/script_template.py' --help
python -X utf8 '<SKILL_DIR>/scripts/script_template.py' -d -v '<현재 대상 파일>'
python -X utf8 '<SKILL_DIR>/scripts/script_template.py' -f '<파일 1>' '<파일 2>'
python -X utf8 '<SKILL_DIR>/scripts/script_template.py' -D '<현재 대상 디렉터리>'
```

- 무인수 help와 `--help/--version`은 0, 잘못된 옵션은 2입니다. 누락·잘못된 종류·처리 실패를 기록하고 batch 전체에서 하나라도 실패하면 1을 반환합니다. 유효 입력이 먼저 처리된 혼합 batch도 성공으로 보고하지 않습니다. 기본 dry-run에서도 누락 입력은 실패합니다. 임의 skip은 추가하지 않습니다.
- 원문 업무 처리 로직과 `new_content/process_dir`는 placeholder입니다. 동봉 파일은 업무 변경을 날조하지 않습니다. dry-run은 실제 입력을 검증하고 처리 예정 경로만 기록하며, 일반 실행은 `transform_content()`를 구현하기 전 미구현 오류로 종료합니다. 프로젝트의 실제 변환·복원 기능과 멱등성을 구현한 후 일반 실행을 사용합니다. `-r`은 구현되지 않아 현재 help에서 광고하지 않습니다.
- 기본 로깅은 stderr 콘솔입니다. `--log-dir`를 명시한 경우에만 그 작업 경로의 UTF-8 월별 로그를 만들며 파일 로깅 실패 시 원문대로 콘솔 경고와 콘솔 로깅을 유지합니다. `/var/log`를 만들지 않습니다. stdout 데이터와 로그를 구분합니다.
- `_atomic_write()`는 같은 디렉터리의 임시 파일을 flush/fsync 후 `os.replace()`하고 실패한 임시 파일을 정리합니다. 일반 파일만 허용하고 확인 가능한 symlink/reparse 및 부모 reparse를 거부합니다. Windows의 읽기 전용 mode는 가능한 범위에서 보존하지만 ACL·owner·ADS·확장 속성·hard-link 관계·전원 장애 영속성 보존을 보장하지 않습니다. 필요한 메타데이터 계약은 대상 프로젝트에서 구현·검증하며 동시 writer는 별도 잠금으로 조정합니다. 비협조 writer가 검사 사이에 경로를 교체하는 공격을 막는 보안 경계로 사용하지 않습니다.

원문 비교 자료: [Kiro 원문](../originals/python-script-template.md). 비교용 코드를 현재 실행 본문으로 선택하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 참고 스크립트

실제 운영 스크립트에서 사용된 패턴입니다.

| 파일                        | 용도                 | 핵심 패턴                            |
|-----------------------------|----------------------|--------------------------------------|
| `/root/sj_del/ip_mask.py`   | 공인 IP 마스킹/원복  | argparse, logger, _c(), atomic_write |
| `/root/sj_del/json_mask.py` | JSON 민감정보 마스킹 | 동일 패턴 + JSON 처리                |

---

## 파일 구조 (strict order)

```python
#!/usr/bin/env python3
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script
"""
script_name.py - 한 줄 설명

상세 설명 (여러 줄 가능)

사용법:
    python3 script_name.py <file>           기본 동작
    python3 script_name.py -r <file>        원복 모드
    python3 script_name.py -d <file>        dry-run
    python3 script_name.py -D <dir>         디렉토리 처리
"""

VERSION = "YY.MM.DD"

import argparse
import logging
import os
import re
import sys
from datetime import datetime

# ── logger ────────────────────────────────────────────────────────────────────
# ── colors ────────────────────────────────────────────────────────────────────
# ── constants ─────────────────────────────────────────────────────────────────
# ── utilities ─────────────────────────────────────────────────────────────────
# ── core functions ────────────────────────────────────────────────────────────
# ── entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
```

---

## 필수 요소

### shebang + SAFETY

```python
#!/usr/bin/env python3
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script
```

### VERSION

```python
VERSION = "26.06.09"  # YY.MM.DD 날짜 기반
```

### import 규칙

- **한 줄에 하나** (`import re, sys` 금지)
- **stdlib 먼저**, 알파벳순
- 서드파티는 빈 줄로 구분
- `from datetime import datetime` 허용 (한 줄)

```python
import argparse
import logging
import os
import re
import sys
from datetime import datetime
```

---

## 로거 (`_setup_logger`)

콘솔 + `/var/log/sjyun/` 파일 동시 출력. 파일 생성 실패 시 콘솔만.

```python
def _setup_logger(name='script_name'):
    """콘솔 + /var/log/sjyun/ 파일 동시 출력 로거."""
    fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    lgr = logging.getLogger(name)
    lgr.setLevel(logging.INFO)
    if not lgr.handlers:
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        lgr.addHandler(ch)
        try:
            log_dir = '/var/log/sjyun'
            os.makedirs(log_dir, exist_ok=True)
            log_path = os.path.join(log_dir, f"{name}_{datetime.now().strftime('%Y%m')}.log")
            fh = logging.FileHandler(log_path, encoding='utf-8')
            fh.setFormatter(fmt)
            lgr.addHandler(fh)
        except OSError:
            lgr.warning("log file creation failed, console only")
    return lgr


log = _setup_logger()
```

---

## 색상 출력 (`_c`)

터미널이 아니면 색상 코드를 출력하지 않습니다.

```python
# ── colors ────────────────────────────────────────────────────────────────────
_RED = '\033[0;31m'
_YELLOW = '\033[0;33m'
_GREEN = '\033[0;32m'
_PURPLE = '\033[0;35m'
_GRAY = '\033[0;90m'
_RESET = '\033[0m'


def _c(text, color=_RED):
    """Colorize text (no-op if not a tty)."""
    if sys.stdout.isatty() or sys.stderr.isatty():
        return f'{color}{text}{_RESET}'
    return text
```

---

## argparse

- `-h/--help`: 자동 제공
- `-V/--version`: 필수
- `-d/--dry-run`: 권장
- `-v/--verbose`: 권장
- `-q/--quiet`: 선택
- `epilog`: Examples + Notes 포함
- `formatter_class=argparse.RawDescriptionHelpFormatter`

```python
def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='스크립트 한 줄 설명',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "\nExamples:\n"
            "  %(prog)s config.txt              기본 동작\n"
            "  %(prog)s -r config.txt           원복 모드\n"
            "  %(prog)s -d -v config.txt        dry-run 상세 출력\n"
            "  %(prog)s -D ./configs/           디렉토리 처리\n"
            "\nNotes:\n"
            "  - 멱등성 보장: 이미 처리된 파일에 다시 실행해도 결과 동일\n"
        )
    )
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {VERSION}')
    parser.add_argument('target', nargs='?', help='파일 또는 디렉토리 경로')
    parser.add_argument('-f', '--file', nargs='+', metavar='FILE', help='대상 파일')
    parser.add_argument('-d', '--dry-run', action='store_true', help='변경 없이 출력만')
    parser.add_argument('-v', '--verbose', action='store_true', help='상세 출력')
    parser.add_argument('-q', '--quiet', action='store_true', help='에러만 출력')
    parser.add_argument('-D', '--dir', nargs='+', metavar='DIR', help='디렉토리 일괄 처리')
    return parser.parse_args()
```

---

## Atomic Write (안전한 파일 쓰기)

원본 파일을 덮어쓸 때 중간에 실패해도 원본이 유지됩니다.

```python
def _atomic_write(filepath, data):
    """Write data to file atomically (temp + rename)."""
    import tempfile
    dir_name = os.path.dirname(filepath) or '.'
    fd, tmp_path = tempfile.mkstemp(dir=dir_name, prefix='.tmp_')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(data)
        os.replace(tmp_path, filepath)
    except Exception:
        os.unlink(tmp_path)
        raise
```

---

## dry-run 처리 패턴

```python
def process_file(filepath, dry_run=False, verbose=False):
    """Process single file."""
    # ... 처리 로직 ...
    if dry_run:
        log.info(f"[dry-run] would modify: {_c(filepath, _YELLOW)}")
        if verbose:
            # 변경 내용 상세 출력
            pass
        return
    # 실제 변경
    _atomic_write(filepath, new_content)
    log.info(f"modified: {_c(filepath, _GREEN)}")
```

---

## main 구조

```python
def main():
    """Main entry point."""
    args = parse_args()
    if args.quiet:
        log.setLevel(logging.ERROR)

    if args.file:
        for f in args.file:
            if os.path.isfile(f):
                process_file(f, dry_run=args.dry_run, verbose=args.verbose)
            else:
                log.error(f"not found: {f}")
    elif args.dir:
        for d in args.dir:
            if os.path.isdir(d):
                process_dir(d, dry_run=args.dry_run, verbose=args.verbose)
            else:
                log.error(f"not found: {d}")
    elif args.target:
        if os.path.isdir(args.target):
            process_dir(args.target, dry_run=args.dry_run, verbose=args.verbose)
        elif os.path.isfile(args.target):
            process_file(args.target, dry_run=args.dry_run, verbose=args.verbose)
        else:
            log.error(f"not found: {args.target}")
    else:
        parser.print_help()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
```

---

## 단축 옵션 규칙

일관성을 위해 아래 단축키를 표준으로 사용합니다.

| 단축 | 전체 옵션           | 용도                          |
|------|---------------------|-------------------------------|
| `-V` | `--version`         | 버전 출력 (필수)              |
| `-d` | `--dry-run`         | 변경 없이 출력만 (권장)       |
| `-v` | `--verbose`         | 상세 출력 (권장)              |
| `-q` | `--quiet`           | 에러만 출력 (선택)            |
| `-l` | `--list`            | 대상 목록 출력 후 종료 (선택) |
| `-o` | `--os` / `--output` | 대상/출력 지정 (상황별)       |
| `-f` | `--file`            | 파일 지정 (선택)              |
| `-D` | `--dir`             | 디렉토리 지정 (선택)          |
| `-r` | `--restore`         | 원복 모드 (선택)              |
| `-P` | (대문자)            | skip 계열 옵션 (선택)         |

🟡 대문자 단축키(`-P`, `-D`)는 소문자와 혼동 방지가 필요한 경우에만 사용합니다.

## 도움말 출력 규칙

`-h/--help` 출력은 아래 구조를 따릅니다.

```
usage: script_name.py [-h] [--dry-run] [--verbose] [--quiet] [--list] [-V]

한 줄 설명 (description)

options:
  -h, --help      show this help message and exit
  --dry-run, -d   실행 없이 단계만 출력
  --verbose, -v   상세 출력
  --quiet, -q     에러만 출력
  --list, -l      대상 목록 출력 후 종료
  -V, --version   show program's version number and exit

Examples:
  script_name.py -d                 dry-run 전체
  script_name.py -o target_name     특정 대상만 실행

Notes:
  - 멱등성 보장: 이미 처리된 대상에 다시 실행해도 결과 동일
  - 로그: /var/log/sjyun/ansible/
```

### 작성 규칙

- `description`: 스크립트 기능을 한 줄로 설명합니다
- `options`: argparse가 자동 생성합니다. 한글 help 텍스트 권장합니다
- `Examples`: 실제 사용 명령어 2~4개를 포함합니다
- `Notes`: 멱등성, 로그 위치, 주의사항 등을 기재합니다
- `formatter_class=argparse.RawDescriptionHelpFormatter` 필수 (epilog 줄바꿈 유지)

---

## 적용 규칙

| 항목                 | 규칙                                               |
|----------------------|----------------------------------------------------|
| Module-level compile | `re.compile()` 함수 내 금지, 모듈 레벨 상수로 선언 |
| 함수 내 import       | 금지 (`import re as _re` 반복 패턴 금지)           |
| docstring            | 모든 함수에 1줄 요약 필수                          |
| parse_args()         | main()에서 분리, 별도 함수                         |
| 에러 처리            | `log.error()` 후 계속 진행 또는 `sys.exit(1)` 명시 |
| 멱등성               | 동일 입력에 동일 출력 보장 (재실행 안전)           |
| 섹션 구분            | `# ── section ──...` (80자 라인)                   |

## 복잡도 기준

| 복잡도 | 기준                  | 로거            | 구조                                  |
|--------|-----------------------|-----------------|---------------------------------------|
| 간단   | 100줄 이하, 단일 기능 | `print()`       | `main()` 하나                         |
| 보통   | 100~200줄, 파일 처리  | `_setup_logger` | `parse_args()` + `main()` + 핵심 함수 |
| 복잡   | 200줄 이상, 여러 모드 | 전체 패턴       | 모듈 분리 고려                        |

## 간단한 스크립트 예시 (로거 없음)

```python
#!/usr/bin/env python3
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script
"""
simple_task.py - 간단한 단일 작업 스크립트

Usage:
    python3 simple_task.py <target>
    python3 simple_task.py --dry-run <target>
"""

VERSION = "26.06.09"

import argparse
import os
import sys


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="간단한 작업")
    parser.add_argument("target", help="대상 경로")
    parser.add_argument("-d", "--dry-run", action="store_true")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {VERSION}")
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()
    if not os.path.exists(args.target):
        print(f"ERROR: {args.target} not found")
        sys.exit(1)
    if args.dry_run:
        print(f"[dry-run] would process: {args.target}")
        return
    # 작업 수행
    print(f"done: {args.target}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
```
