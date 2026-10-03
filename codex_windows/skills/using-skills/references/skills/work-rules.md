---
name: work-rules
description: Defines operating rules for all agents. Use when executing any task — confirms before action, requires rollback plans for dangerous operations, enforces naming conventions and credential placeholders.
---

# Work Rules

<!-- CODEX-COMPAT-BEGIN -->
## Windows 호환 및 적용 규칙

이 절이 Windows에서 사용할 실행·경로·검증 기준입니다. 블록 밖의 원문·예시·코드·템플릿·체크리스트는 모두 보존했으며 충돌하지 않는 목적·개인 규약은 계속 적용합니다. POSIX/Bash 실행 방법은 비교 자료이며 Windows PowerShell에서 그대로 실행하지 않습니다. 필요한 원격 Linux 작업은 실제 대상·쉘·도구·권한을 확인한 별도 실행입니다. 아래에서 위험하거나 잘못된 과거 예시를 대체한 경우 원래 예시를 실행하지 않습니다.

### 적용 범위와 실제 환경

- 플랫폼·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침 > 개인 skill 기본값** 순서로 적용합니다. 작업별 필요한 skill·참조만 읽고 이미 읽은 본문·순환 참조를 반복하지 않습니다. 원문 보존을 전체 skill의 일괄 실행 조건으로 바꾸지 않습니다.
- 실제 작업 경로에서 `git -C <대상 디렉터리> rev-parse --show-toplevel`, `git -C <확인한 Git 루트> status --short`로 루트·기존 변경을 먼저 확인합니다. worktree의 `.git` 파일도 인정합니다. 적용 AGENTS/override·하위 지침과 실제 `.governance`의 범위만 따르며 다른 저장소 설정을 자동 적용하지 않습니다.
- Windows 네이티브 PowerShell과 실제 Python 3.11 이상을 사용합니다. PowerShell 5.1/7, `python.exe`/`py`의 실제 경로·버전을 확인하고 WindowsApps alias를 설치된 runtime으로 간주하지 않습니다. Python은 `-X utf8 -B`로 호출하고 작성하는 코드의 파일 읽기·쓰기도 `encoding='utf-8'`을 명시합니다. PowerShell 인코딩은 버전별로 확인하며 BOM/UTF-16/개행을 의도 없이 변경하지 않습니다.
- PowerShell의 파일 작업은 `-LiteralPath`, `Join-Path`, 확인한 절대 경로를 사용합니다. Linux의 `/root`, `/opt`, `$HOME`, `chmod`, `sudo`, `systemctl`, `fcntl`을 Windows 계정·경로·ACL·서비스로 이름만 치환하지 않습니다. WSL/Git Bash가 필요하면 명시한 Linux/Bash 역할로 구분하며 설치·활성화·권한 변경은 자동 수행하지 않습니다.
- 네이티브 CLI의 종료 상태는 해당 도구 계약으로 판정합니다. PowerShell cmdlet 오류와 `$LASTEXITCODE`를 혼동하지 않고 오류 로그만으로 성공 처리하지 않습니다. Terraform detailed exit code처럼 정상 차이를 뜻하는 상태는 일반 실패와 구분합니다.
- 이미 승인된 작업은 자율 진행합니다. 신규 파괴 작업·실제 운영 적용·키/ACL 변경·범위 밖 게시 등 추가 권한이 필요한 동작은 그 직전에 현재 승인 범위를 확인합니다. 경로 존재·과거 승인·원문 예시는 새 권한이 아닙니다. 기존 승인에 같은 확인을 반복 요구하지 않습니다.
- 구현·검사 완료, 모델 행동, 설치·새 세션 발견, 원격 적용, Git 게시를 각각 구분합니다. 이 파일의 작성은 개인 홈 설치나 실환경 검증 완료가 아닙니다. 한국어로 목적·관찰·다음 조치와 통과/부분 검사/실패/미실행을 간결하게 보고합니다.
- 사용자와 저장소가 지정한 게시 순서를 따릅니다. 다른 저장소를 yunli로 강제 전환하거나 검토 요청을 commit/push로 확대하지 않습니다. 개인 홈·config·키·release·서비스 적용은 별도 요청 범위입니다.

### 작업 시작과 완료 보고

사용자가 한 채팅 안에서 여러 요청을 `;`로 구분하면 각각의 요청으로 이해하고 빠뜨리지 않도록 수행·검증·미실행 상태를 구분합니다. 요청 사이에 의존 관계가 있으면 그 순서에 맞춰 진행하고 독립된 작업은 함께 진행할 수 있습니다. 코드·명령어·인용문·경로 등 내용 안의 `;`는 원래 의미를 유지하며 기계적으로 요청을 나누지 않습니다. 구분이 실제 작업 범위에 영향을 주고 문맥으로 해결되지 않을 때만 필요한 내용을 확인합니다.

실제 실행·파일 변경 작업을 시작하기 전에 **대상 경로·무엇을 수행하는지·예상 결과**를 간결하게 알립니다. 큰 작업은 주요 단계·변경 범위·검증 방법도 안내하고, 진행 중에는 의미 있는 관찰·방향 변경·남은 조건을 공유합니다. 단순 질의·짧은 답변에는 불필요한 작업 계획이나 고정 양식을 붙이지 않습니다. 시작 안내를 이미 승인된 작업에 대한 반복 승인 질문으로 바꾸지 않습니다.

완료 보고는 핵심 결과부터 설명하고 다음 항목을 실제 근거에 따라 담습니다.

- **결과물과 경로:** 실제 결과물이 있으면 설명·표·폴더 구조 위에 기준 경로를 먼저 표시하고 파일은 클릭 가능한 경로로 연결합니다. 같은 기준 경로를 반복하지 않습니다. 로컬 사용자 보고에는 실제 경로를 쓰되 원격에 게시할 문서는 저장소 상대 경로·공개 가능한 별칭을 사용하며 개인 경로·계정·자격증명·운영 자료를 복사하지 않습니다.
- **수행과 검증:** 무엇을 변경·생성·실행했는지, 어떤 검사를 실행하고 어떤 결과를 관찰했는지 설명합니다. **완료 / 통과·부분 검사·실패 / 미실행·남은 작업**을 구분하고 파일 작성·실행 성공·사용자 확인·Git 게시·설치·배포를 각각의 실제 상태로 보고합니다.
- **큰 결과의 표현:** 비교·상태는 표, 순서는 번호 목록, 파일 구성은 트리를 사용합니다. 내용에 맞는 형식만 선택하고 깊은 `1. → 1) → a.` 중첩은 관계를 설명하는 데 필요할 때 사용합니다. 짧은 결과에 표·다이어그램·정해진 항목 수를 강제하지 않습니다.
- **잘된 점과 문제점:** 확인된 성과와 문제·제약·미확인 사항을 간단히 적고 필요한 다음 조치를 연결합니다. 성과·문제를 억지로 만들지 않으며 문제를 찾지 못했으면 검증 범위 안의 관찰로 설명합니다. 미검증을 ‘문제 없음’으로 바꾸지 않습니다.

이 절은 폴더 안에서 완결되는 사용 지침입니다. 보고하기 위해 중앙 저장소·다른 skill·별도 설치기 조회를 필수로 요구하지 않습니다. 요청한 읽기 전용 검토를 수정·게시·설치로 확대하지 않습니다.

### 단독 사용과 참조

폴더 전체가 사용 단위입니다. 이 폴더 안의 필수 참조·도구만 사용하며 중앙 catalog·installer·30/31 저장소나 다른 skill의 별도 설치를 요구하지 않습니다. `skill://`는 아래 동봉 대응으로 해석하고 Kiro URI/hook/memory API를 호출하지 않습니다. 개인 경로·계정·config 원문·자격증명·세션·raw 비공개 증거를 공개 자료에 복사하지 않습니다.

### Windows 목적별 대응 — 원문 26절 전체

원문의 26절·예시·템플릿·체크리스트를 줄이지 않습니다. 아래 대응은 각 목적을 Windows에서 수행하기 위한 활성 기준이며 원문의 Bash/POSIX/Kiro 실행 방법은 비교 자료입니다.

1. **§1 승인·§1-1 장시간 실행:** 목적·범위를 간결하게 알리고 승인된 작업은 진행합니다. 도구의 비동기 세션/후속 상태 조회를 사용하며 짧은 timeout을 모든 명령에 강제하지 않습니다. timeout은 실패 확정이 아니므로 실제 소유 프로세스·부분 실행·로그를 먼저 확인합니다. 동일 접근 2회 실패 후 근본적으로 다른 접근을 검토하되 승인 밖 재시도·프로세스 종료를 자동 수행하지 않습니다.
2. **§2 위험 작업·§3 삭제:** 현재 승인 범위를 동작 직전에 확인합니다. 대상·영향·복구 범위를 확인하고 Windows 삭제/이동은 절대 경로가 의도한 범위 안에 있는지 확인한 뒤 `Remove-Item`/`Move-Item -LiteralPath`로 수행합니다. 다른 shell이나 문자열 명령으로 권한/범위를 우회하지 않습니다. 이미 승인된 같은 동작은 재확인하지 않습니다.
3. **§4 Markdown:** 한글·트리·표 display width·용어 설명·문체 기준을 유지하고 현재 사용자/저장소 예외를 함께 적용합니다. STYLE은 이 폴더의 동봉 자료로 읽습니다. 원문의 Kiro URI·개인 경로를 실제 Windows 의존 경로로 사용하지 않습니다.
4. **§5 명명·§6 기호·§9 보고:** 기존 개인 명명·허용 기호·간결 한국어 기본값은 유지하되 사용자/저장소의 명확한 고유 규칙이 우선입니다. 실행·정적 확인·미검증을 분리합니다.
5. **§7 권한:** Windows 관리자 토큰·UAC·파일 ACL·서비스 권한과 원격 Linux의 sudo/become는 별도입니다. 실제 권한·대상을 확인하고 필요한 추가 권한은 정상 승인 경로에서 다룹니다. `/root` 경로, 작업 파일 접근 거부, SSH 소유자 확인 실패가 ACL 변경·관리자 실행·sandbox 우회 권한이 아닙니다.
6. **§8 코드 범위·§14 정리:** 요청 범위와 기존 편집을 보존하고 이번 변경 때문에 생긴 불필요 요소만 정리합니다. 테스트는 사용자 범위·저장소 필수 검사·변경 위험에 맞게 수행하며 개인 기본값으로 필수 검증을 생략하지 않습니다. 다른 skill 전체를 일괄 적용하거나 인접 코드를 최적화하지 않습니다.
7. **§10 placeholder:** 원문의 표준 예시 값·비밀정보 금지 목적을 유지합니다. 실제 키·계정·IP·운영 자료를 placeholder에 채우지 않습니다. gitleaks allowlist를 필요 없이 자동 작성/확장하지 않고 실제 설정 범위와 오탐만 확인합니다.
8. **§11 Markdown 검사:** 현재 변경한 문서에 동봉 Windows Python style/heading/link 도구를 사용합니다. `python -X utf8 -B`와 명시 대상·실제 종료 상태를 확인합니다. 외부 fix_table_align/trim_diagram 도구를 필수 설치하지 않고 보고된 문제를 범위 안에서 수정·재검사합니다. 파일 입력 누락·읽기 실패·미닫힘을 성공으로 처리하지 않습니다.
9. **§12 사후 검증:** 문법/변경 영향/건강/모니터링의 목적을 실제 기술에 맞춰 적용합니다. 코드/문서 검토 요청에 Terraform/AWS/서비스 실행을 강제하지 않습니다. plan/apply/운영 검사가 없거나 미실행이면 그 이유와 남은 조건을 보고합니다.
10. **§13 계획·§26 batch:** 작업에 필요한 계획·checkpoint·pre/post 보고를 현재 사용자·저장소 양식에 맞춰 작성합니다. 본문에 있는 과거 TODO §4·3항목 batch·모델 역할이 모든 새 작업의 강제 체계는 아닙니다. 채택한 batch에는 준비→작성→검사→사실 확인→상태 갱신과 미완료 재개 목적을 유지합니다.
11. **§15–16 reference·§24 GitHub 색인:** 공식 출처 확인·출처/확인일/미확인 구분·전파 범위 대조를 유지합니다. 현재 저장소가 채택한 `_reference`/INDEX/GitHub 목록만 필요한 범위에서 갱신하고 다른 저장소의 디렉터리를 생성/수정하지 않습니다. `lynx`, Bash curl pipeline은 Windows 필수 도구가 아니며 제공된 웹 도구/실제 curl.exe/PowerShell HTTP 도구로 공개 공식 자료를 확인합니다. 네트워크 실패·자료 부재는 미확인이고 추정으로 공식 사실을 만들지 않습니다.
12. **§17 Python:** 구조·SAFETY·날짜 VERSION·argparse·docstring·최소 예외·필수 option/help와 검증 목적을 유지합니다. Windows에서는 실제 python.exe를 명시하고 JSON/TOML/config/status의 encoding·경로·최종 종료 상태를 명확하게 처리합니다. 파일 owner/mode·ACL·atomic replace는 같은 기능으로 간주하지 않습니다.
13. **§18 SSH 인코딩:** local PowerShell → SSH client → 원격 기본 shell → 실제 powershell.exe/pwsh/Linux shell의 계층을 확인합니다. 원문의 `cmd /c chcp` 중첩 quote를 Windows 공통 필수 패턴으로 실행하지 않습니다. 원격 Windows PowerShell의 복잡한 스크립트에는 실제 지원하는 `-EncodedCommand`(UTF-16LE Base64)를 검토하고, 입력 데이터와 스크립트를 분리해 injection을 막습니다. 원격 실행 정책·host key·코드페이지·stdout/stderr·종료 상태를 실제 fixture로 확인하며 인코딩 옵션이 승인/권한을 우회하지는 않습니다.
14. **§19 치환 확인:** 치환 전 대상과 예상 건수를 확인하고 이후 관련 행·잔여 문자열·참조·영향 범위를 `rg` 또는 `Select-String -LiteralPath`로 대조합니다. 일괄 값 변경은 승인한 파일 목록에서 처리하며 로그/비밀정보를 공개 출력하지 않습니다. 0건 치환을 성공으로 처리하지 않고 의도된 0건과 실패를 구분합니다. sed 예시를 PowerShell에서 실행하지 않습니다.
15. **§20 VM:** 실제 VM 목록·대상·상태·삭제/중지/재생성 차이와 현재 승인 범위를 확인합니다. Hyper-V cmdlet·관리자 권한·vagrant provider는 실제 존재할 때만 사용합니다. 이미 대상까지 승인된 작업에 같은 삭제 승인을 반복 요구하지 않으며 범위 밖 VM은 변경하지 않습니다.
16. **§21 SSH 프로세스:** 시작 시 모든 SSH/PID를 일괄 kill하는 원문 예시는 실행하지 않습니다. 현재 작업이 시작한 process/session의 PID·소유·대상과 부분 실행을 확인해 정상 종료를 우선합니다. 필요한 `Stop-Process`는 그 작업의 확인된 PID·승인 범위에서만 사용합니다. 다른 사용자/작업·전체 ssh.exe·원격 서비스를 종료하지 않습니다.
17. **§22 잠금:** Kiro disabled 파일·hook을 생성/삭제하지 않습니다. 현행 저장소 정책을 확인하고 동봉 Windows kiro-lock helper의 root·task token으로 acquire/check/release합니다. token은 현재 작업에서 생성해 유지하고 타인의 token을 채택하지 않습니다. R08 부분 생성 실패 정리는 실제 helper의 소유·inode 확인 범위로 검증해야 하며 손상/오래된 lock을 시간 경과만으로 삭제하지 않습니다. 참여자 공유와 일반 파일 byte lock은 별도 프로토콜입니다.
18. **§23 PLAN 기록:** 비자명한 오류·원인·보완·재현·검증을 현재 저장소가 정한 실제 문서의 기존 항목과 연결합니다. 루트/하위 PLAN 선택과 번호는 현재 지침을 따르고 없으면 자동 governance 초기화를 하지 않습니다. 반복 항목을 중복 생성하지 않으며 Kiro hook 활성화가 기록의 선행 조건은 아닙니다.
19. **§25 memory:** Kiro memory API·개인 파일을 자동 만들지 않습니다. 사용자가 명시한 현재 기록/메모 경로에서만 보존·최대 분량·archive·동기화 목적을 적용합니다. 개인 메모·세션·실제 계정·비밀정보는 공개 Git에 복사하지 않고 요약 확인도 비공개 내용을 드러내지 않습니다.

### Windows Python config·status·종료 상태

원문의 `load_config` 자동 발견은 현재 SCRIPT_DIR 아래 실제 설정 1개가 확인된 경우만 적용합니다. 경로를 주면 실제 지정 파일을 사용하고 TOML은 binary·JSON은 UTF-8로 읽으며 필수 키·타입·범위를 검증합니다. 다른 홈·config를 검색/복사하거나 모호한 첫 파일을 선택하지 않습니다.

```python
# 현재 코드의 SCRIPT_DIR·필수 키/범위 계약을 사용합니다.
import json
import tomllib
from pathlib import Path


def load_config(config_path=None):
    """Load one explicitly selected or unambiguous TOML/JSON config."""
    if config_path is None:
        candidates = sorted(Path(SCRIPT_DIR).glob('*config.toml'))
        candidates += sorted(Path(SCRIPT_DIR).glob('*config.json'))
        if len(candidates) != 1:
            raise FileNotFoundError('exactly 1 config file required')
        config_path = candidates[0]
    selected = Path(config_path)
    if selected.suffix.lower() == '.toml':
        with selected.open('rb') as stream:
            return tomllib.load(stream)
    if selected.suffix.lower() != '.json':
        raise ValueError('expected TOML or JSON config')
    with selected.open('r', encoding='utf-8') as stream:
        return json.load(stream)
```

이 config 함수는 기존 프로그램의 전달된 자료를 읽는 패턴입니다. 설정 병합·설치·실제 서비스 변경을 수행하지 않습니다. 신규 코드는 module import 순서 등 원문의 개인 양식을 함께 적용합니다.

원문의 `write_status(error_codes)` 목적은 모니터링 프로토콜의 상태 기록입니다. 실제 LOG_DIR/STATUS_FILE·오류 코드 의미를 확인하고 UTF-8로 기록합니다. 0 성공/비정상 실패 집계를 프로젝트 계약에 맞추고 실패를 status나 프로세스의 0으로 덮지 않습니다. `main()`의 최종 결과는 `sys.exit(main())`로 프로세스에 전달하며 R07 누락/혼합 입력과 R14 등록된 도움말 option을 함께 검사합니다.

### Windows file lock의 실행 기준

원문의 `fcntl.flock`·정상 해제 시 경로 삭제 예시는 Windows에서 실행하지 않습니다. 아래는 Windows의 프로세스 중복 실행 방지를 위한 **별도 byte-lock 패턴**입니다. 공유 경로를 유지하고 각 참여자가 같은 byte 위치를 잠급니다. OSError를 모두 “already running”으로 바꾸거나 종료 0으로 처리하지 않습니다.

```python
import msvcrt
import os
from contextlib import contextmanager


@contextmanager
def exclusive_file_lock(lock_file):
    """Hold one Windows byte lock on a persistent local path."""
    flags = os.O_RDWR | os.O_CREAT | getattr(os, 'O_BINARY', 0)
    fd = os.open(lock_file, flags, 0o600)
    with os.fdopen(fd, 'r+b') as lock_fp:
        if os.fstat(lock_fp.fileno()).st_size == 0:
            lock_fp.write(b'\x00')
            lock_fp.flush()
        lock_fp.seek(0)
        msvcrt.locking(lock_fp.fileno(), msvcrt.LK_NBLCK, 1)
        try:
            yield lock_fp
        finally:
            lock_fp.seek(0)
            msvcrt.locking(lock_fp.fileno(), msvcrt.LK_UNLCK, 1)
    # Keep the path so every cooperating process locks the same file.
```

실제 호출부는 `with exclusive_file_lock(LOCK_FILE):` 안에서 작업하고 I/O·권한·이미 잠긴 경우의 실제 실패를 로그/비정상 상태로 전달합니다. path 존재만으로 잠금 여부를 판단하지 않습니다. 이 패턴은 참여자·동일 경로·로컬 Windows byte locking 범위이며 symlink/reparse point·교체 writer·네트워크 FS·ACL·비협력 프로세스의 보장이나 동봉 kiro-lock helper와의 호환을 주장하지 않습니다. 실제 대상 적용 전 별도 정상·경쟁·예외 검증이 필요합니다.

### Windows SSH·ACL와 문서 도구

Windows OpenSSH user key·server host key·authorized_keys·관리자용 authorized_keys는 서로 다른 소유/ACL 대상입니다. 실제 계정·client/server·공식 설정·현재 ACL을 필요한 범위에서 확인하고 원문의 chmod 600·경로 예시를 기계적으로 적용하지 않습니다. 키 본문·다른 계정의 키를 출력하지 않으며 정상 인증 실패를 ACL 완화·host key 확인 생략으로 우회하지 않습니다.

PowerShell 5.1의 `>`/Out-File·인코딩과 PowerShell 7의 기본값은 다릅니다. Python UTF-8 문서·state bytes·SSH stdout을 각각 확인합니다. 5.1에서 Set-Content -Encoding UTF8의 BOM 여부가 영향을 주는 경우 .NET의 명시적인 UTF8Encoding과 현재 파일 형식을 사용하며 전체 설정을 일괄 다시 저장하지 않습니다.

문서 도구 호출은 실제 runtime과 이 폴더 경로를 사용합니다. 원문의 `python3`/sia-md-* 이름이 Windows alias라는 이유로 설치/동작을 추정하지 않습니다. 사용자/저장소가 footer·날짜·배지를 금지하면 style의 footer 검사만 근거와 함께 제외하고 다른 검사를 유지합니다. 보존 원문 경고·새 경고·읽기 실패·부분 검사를 구분합니다.

공식 플랫폼 근거: [PowerShell 인코딩](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-5.1), [EncodedCommand](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.2), [Windows OpenSSH 키/ACL](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement), [Ansible controller 플랫폼](https://docs.ansible.com/projects/ansible/latest/os_guide/intro_windows.html).

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://incremental-change` → [incremental-change](../skills/incremental-change.md).
- `skill://kiro-lock` → [kiro-lock](../skills/kiro-lock.md).
- `skill://planning-and-breakdown` → [planning-and-breakdown](../skills/planning-and-breakdown.md).
- `skill://spec-driven-infra` → [spec-driven-infra](../skills/spec-driven-infra.md).
- `skill://readme-template` → [전체 readme-template 지침](../skills/readme-template.md).

문서 개인 양식은 [STYLE.md](../STYLE.md)를 현재 사용자/저장소 예외와 함께 적용합니다.

### 동봉 도구 호출

다음 PowerShell 호출의 `$pythonExe`는 확인한 실제 Python, `$skillDir`는 현재 복사된 폴더, `$target`은 명시한 검사 대상입니다. 코드 작성과 실제 실행/설치 검증을 구분합니다.

```powershell
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/lock.py') --help
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-heading-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-link-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-style-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
```

잠금 help 확인은 실제 acquire/check/release나 전체 실패/경쟁 검증이 아닙니다. 원문의 Kiro 실행 상태와 새 Windows 설치 상태를 혼동하지 않습니다.

원문 비교 자료: [Kiro 원문](../originals/work-rules.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 1. Confirm before action
Print task summary before execution. format: "수행할 작업: - [item]"
This applies to **destructive or irreversible** operations only (§ 2, § 3).
For routine tasks (file edits, status checks, builds), proceed without confirmation.

## 1-1. Long-running command timeout handling

For commands that may block (vagrant up, packer build, apt install, docker pull, etc.):

1. **Never use polling loops inside a single tool call** (e.g., `for i in ...; do sleep 30; check; done`) — blocks the session and appears frozen.
2. **Always use `timeout N <command>`** with a short limit (e.g., `timeout 15` for SSH checks).
3. **For background tasks** (Task Scheduler, nohup, etc.):
   - Launch with a single non-blocking command, then immediately move on to the next independent task.
   - Check status in subsequent separate tool calls — never in a polling loop within one call.
4. **If a command times out or hangs**: kill it, diagnose from logs, fix and retry autonomously.
5. **Retry limit**: after 2 failed attempts with the same approach, switch to a fundamentally different method.
6. **Never pause mid-task** for confirmation. The user will Ctrl+C if something is wrong.


## 2. Dangerous operations
terraform apply, infra changes, service restart, deploy → ask "진행할까요?" before execution

For complex infra changes, use `skill://spec-driven-infra` → `skill://planning-and-breakdown` → `skill://incremental-change` workflow.

## 3. Delete operations
List targets → show impact → confirm before proceeding

## 4. Markdown rules
- tree: use `├──`, `└──`, `│` style
- table: align columns considering Korean character width (vi vertical alignment)
  - Korean char = 2 width, ASCII = 1 width
  - pad each cell so all rows have equal column display width
  - separator line `|---|` length = max column width + 2 (one space each side)
- Detailed rules: see `file://~/.kiro/markdown/STYLE.md`
- output language: Korean

### Inline term explanation rule

When an unfamiliar acronym or term first appears in body text, add a 2~3 line blockquote (`>`) explanation immediately below.

Criteria: terms that even a 10-year SE may not know immediately
- Add explanation: HMAC, AEAD, GRE, ISAKMP, HKDF, SPI, MOBIKE, PFS, DPI, MPPE, LCP, NCP, IPCP, Curve25519, Noise IK, BLAKE2 ...
- Skip (well-known): TCP, UDP, IP, TLS, VPN, SSH, DNS, HTTP

Rules:
- No `💡` emoji — the blockquote itself signals an explanation
- `🟡` reserved for warnings/cautions only — do not use for term explanations
- Omit explanation on second and subsequent occurrences in the same document
- **Place blockquotes after the entire table, never inside it** — a blockquote mid-table splits the table into two separate tables in Markdown rendering

```markdown
- DPI environments make SoftEther advantageous.

> DPI(Deep Packet Inspection): firewall technique that inspects packet payloads,
> not just headers, to identify and block specific protocols or applications.
> More precise than port-based filtering; can detect VPN traffic via TLS fingerprint.
```

## 5. Naming convention
format: `[env]-[category]-[service]-[detail]`
env: dev / qa / stg / prd
ex: prd-app-web-frontend, dev-db-rds-postgresql

## 6. Symbols
Allowed: ✅ ❌ 🟡 🟢 🔴 ★★☆☆☆
No other emojis allowed (no decorative emojis)

## 7. sudo
Use sudo when file operations require elevated permissions (e.g., files under /root/, /opt/, /etc/, or any path owned by root).

## 8. Code changes
- Minimal change principle (modify only requested scope)
- Write test code only when explicitly requested
- Never hardcode secret keys

## 9. Response style
- Concise and direct answers
- Skip unnecessary praise/agreement
- Politely correct wrong information

## 10. Example credentials (placeholder only)
Use the following standard placeholders for example passwords/keys in code and docs:
- username:  `Secureuser123`
- password:  `SecurePassword123`
- key/secret: `SecureKey123`
- token:     `SecureToken123`
- db name:   `SecureDbName123`
- domain:    `example.com` / `db.example.com`
- email:     `user@example.com`
- IP:        `192.0.2.1` (RFC 5737 documentation range)
- S3 bucket: `my-bucket`

Add the following to `.gitleaks.toml` to suppress false positives from placeholder values:

```toml
[allowlist]
description = "global allowlist"
regexes = [
    # placeholder values
    '''Secureuser123''',
    '''SecurePassword123''',
    '''SecureKey123''',
    '''SecureToken123''',
    '''SecureDbName123''',
    # RFC 5737 documentation IP ranges
    '''192\.0\.2\.\d+''',
    '''198\.51\.100\.\d+''',
    '''203\.0\.113\.\d+''',
]
```

## 11. Markdown checks (after writing/editing .md)
After creating or modifying any .md file under /root/32_system-engineering-resources or /opt/00_chobo_ansible, run all three:

```bash
BASE=/root/32_system-engineering-resources
sia-md-style-check <path>     # table alignment, tone, footer
sia-md-heading-check <path>   # anchor, H2 numbering, level, duplicate, toc
sia-md-link-check <path>      # internal file links
```

- Run on the specific file or directory modified (not the entire repo unless requested)
- Fix all reported issues before presenting the result
- Use `--strict` / `-s` flag on md-style-check to check without whitelist (for full review)
- sia-md-link-check excludes `#anchor` links by design; sia-md-heading-check covers them

### md quality tools

| Tool                     | Path                                   | Usage                                  |
|--------------------------|----------------------------------------|----------------------------------------|
| sia-md-style-check       | /root/32_system-engineering-resources/ | Style check (mandatory)                |
| sia-md-heading-check     | /root/32_system-engineering-resources/ | Anchor / numbering / level (mandatory) |
| sia-md-link-check        | /root/32_system-engineering-resources/ | Internal file links (mandatory)        |
| fix_table_align.py       | /root/sj_del/                          | Auto-fix table alignment               |
| trim_diagram_trailing.py | /root/sj_del/                          | Remove trailing spaces in diagrams     |

- `fix_table_align.py`: run when md-style-check reports table alignment issues
- `trim_diagram_trailing.py`: run after diagram padding to remove unnecessary trailing spaces
- Both tools support `-d` (dry-run), `-v` (verbose), `-D` (directory recursive)

### _reference citation rule

When creating or modifying a `.md` file that references `_reference/` content, add an HTML comment immediately after the H1 title:

```markdown
# Document Title
<!-- reference: _reference/filename.md -->
```

- Multiple references: `<!-- reference: _reference/a.md, _reference/b.md -->`
- Only add when `_reference/` was actually consulted during writing
- Do NOT add if the document is purely original content (no _reference used)
- This is separate from `_reference/INDEX.md` updates — both are required independently
- Enables `grep -r "reference:" --include="*.md"` for traceability

## 12. Post-change verification
After any infrastructure or code change, verify in order:
1. Syntax/lint pass (terraform validate, shellcheck, ansible --syntax-check)
2. Dry-run clean (terraform plan, ansible --check)
3. Service health (curl health endpoint, aws describe-*)
4. Monitoring normal (no new alarms)

Skip verification only if explicitly told by user.

## 13. Multi-step task plan format
For tasks with 3+ steps, state the plan before starting:
```
1. [step] → verify: [check]
2. [step] → verify: [check]
3. [step] → verify: [check]
```

## 14. Code cleanup scope
When editing code:
- Remove only imports/variables/functions that YOUR changes made unused
- Do not remove pre-existing dead code — mention it instead
- Do not refactor adjacent code that isn't broken

## 15. reference directory rules

`/root/32_system-engineering-resources/_reference/` is **official-homepage-based reference notes only** directory.

### Storage targets
- Recommended settings, deprecated/removed items, breaking changes, version status collected from official docs
- Only store content directly verified from official homepage (docs.*, official blog, GitHub release notes)
- No personal opinions, guesses, or blog content allowed
- ❌ Writing from memory/inference and presenting as official-doc-based is **prohibited** (detail: § 16)

### Filename convention
`{tech}_official_notes.md` (e.g., `docker_official_notes.md`, `ansible_official_notes.md`)

### Mandatory procedure before writing .md

When **creating new** or **significantly modifying** a tech-related `.md` file:

1. Check `_reference/INDEX.md` — verify if reference file exists for that technology
2. If exists → read the file directly (check `last_checked` date, re-verify if older than 6 months)
3. If not exists → scan official homepage using methods below, then **create reference first** (before writing `.md`)
   - Regular pages: `lynx -dump <URL>`
   - JS-rendered pages: `curl` + GitHub API / PyPI API / raw.githubusercontent.com direct call
   - Latest version check: `curl -s "https://api.github.com/repos/<owner>/<repo>/releases/latest"`
4. After creation → add entry to `_reference/INDEX.md` table in this format:
   ```
|  | {tech} | `_reference/{tech}_official_notes.md` | {latest_version} | {today_date} |
   ```
5. Write `.md` referencing the `_reference` file

🟡 **Strict order**: create `_reference` → update INDEX → write `.md`. Reverse order prohibited.

🟡 **Hard stop**: If you find yourself writing a tech `.md` file and realize no `_reference` exists for that technology:
1. **STOP** writing the `.md` immediately (even mid-sentence)
2. Create the `_reference` file first (scan official source)
3. Update `_reference/INDEX.md`
4. Resume `.md` writing

This applies regardless of whether the task was explicitly requested or part of a batch.
Skipping `_reference` because "it's faster" or "I'll do it after" is **never acceptable**.

### reference file structure

```markdown
---
name: {tech}-official-notes
last_checked: YYYY-MM-DD
sources:
  - https://official-URL
---

## 1. Version status
## 2. Recommended settings
## 3. deprecated / removed
## 4. breaking changes
## 5. Security recommendations
```

🟡 Register only `INDEX.md` in agent resources. Read individual files on demand (context window savings)

## 16. reference post-write cross-verification obligation

When **creating new or adding content** to `_reference/` files, the following procedure is mandatory.

### Verification procedure

1. **Version info**: Re-verify actual latest version via GitHub API or PyPI API
   ```bash
   curl -s "https://api.github.com/repos/<owner>/<repo>/releases/latest" | python3 -c "import sys,json; print(json.load(sys.stdin)['tag_name'])"
   curl -s "https://pypi.org/pypi/<package>/json" | python3 -c "import sys,json; print(json.load(sys.stdin)['info']['version'])"
   ```
2. **Feature/concept descriptions**: Open official doc URL directly to confirm content actually exists
3. **Suspicious items**: Do not write content unverifiable from official docs, or mark with comment `# unverified — needs verification`

### Prohibited

- Writing content from memory/inference and presenting it as official-doc-based ❌
- Mixing in blog, Stack Overflow, unofficial tutorial content ❌
- Using feature names/parameter names not found in official docs ❌

### When errors are found

When discovering errors in `_reference` files:
1. Immediately verify correct content from official docs
2. Fix the file
3. Update `last_checked` date
4. Update INDEX.md version info
5. Check if the error propagated to other `.md` files referencing that `_reference`

## 17. Python script writing rules

Style reference: `/root/sj_del/ip_mask.py`, `json_mask.py`, `s3_file_upload.py`.
- `ip_mask.py`, `json_mask.py`: basic CLI script pattern
- `s3_file_upload.py`: long-running service script pattern (config load, file lock, status file)

### File structure (strict order)

```
shebang
SAFETY comment
module docstring (including usage)
VERSION constant
import (stdlib one per line, alphabetical)
constants/patterns (# ── section ──... separator)
function definitions
if __name__ == '__main__': try/except
```

### Mandatory items

- **shebang**: `#!/usr/bin/env python3`
- **SAFETY comment**: `#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable script`
- **VERSION**: `VERSION = "YY.MM.DD"` (date-based)
- **import**: one per line, stdlib first, alphabetical — `import re, sys` on one line prohibited
- **Module-level pattern compile**: `re.compile()` inside functions prohibited — declare as module-level constants
- **No duplicate imports in functions**: `import re as _re` repeated in functions prohibited
- **argparse mandatory**: direct `sys.argv` parsing prohibited
  - `-h/--help`: argparse auto-provides
  - `-V/--version`: `action='version'`, `version=f'%(prog)s {VERSION}'`
  - `-s/--strict` etc. flags: provide both shorthand + full name
  - `epilog`: include Examples + key option descriptions
- **Separate `parse_args()`**: no inline in `main()`, extract to separate function
- **`if __name__` try/except**:
  ```python
  if __name__ == '__main__':
      try:
          main()
      except KeyboardInterrupt:
          sys.exit(130)
  ```

### Section separator comments

```python
# ── colors ────────────────────────────────────────────────────────────────────
# ── constants ─────────────────────────────────────────────────────────────────
# ── utilities ─────────────────────────────────────────────────────────────────
# ── check functions ───────────────────────────────────────────────────────────
# ── entry point ───────────────────────────────────────────────────────────────
```

### Function docstring

One-line summary mandatory. Longer description from second line onward.

```python
def process_file(filepath, dry_run=False):
    """Replace IPs in file (skip if no matching pattern)."""
```

### Config file load pattern (TOML/JSON)

For scripts with external configuration:

```python
def load_config(config_path=None):
    """Load config from TOML/JSON. Auto-discover if path not given."""
    if config_path is None:
        toml_files = glob.glob(os.path.join(SCRIPT_DIR, '*config.toml'))
        json_files = glob.glob(os.path.join(SCRIPT_DIR, '*config.json'))
        config_files = toml_files or json_files
        if len(config_files) != 1:
            raise FileNotFoundError("exactly 1 config file required")
        config_path = config_files[0]
    if config_path.endswith('.toml'):
        import tomllib
        with open(config_path, 'rb') as f:
            return tomllib.load(f)
    with open(config_path, 'r') as f:
        return json.load(f)
```

- Validate required keys immediately after load
- Validate value ranges (min/max) before use

### File lock pattern (duplicate execution prevention)

```python
import fcntl  # Linux
lock_fp = open(LOCK_FILE, 'w')
try:
    fcntl.flock(lock_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
except OSError:
    print("already running")
    sys.exit(0)
# ... do work ...
# finally: fcntl.flock(lock_fp, fcntl.LOCK_UN); lock_fp.close(); os.remove(LOCK_FILE)
```

### Status file pattern (monitoring integration)

```python
STATUS_FILE = os.path.join(LOG_DIR, "backup.status")
def write_status(error_codes):
    """Write error code for external monitoring (Zabbix, etc.)."""
    with open(STATUS_FILE, 'w') as f:
        f.write(str(min(error_codes)) if error_codes else '0')
```

## 18. Windows PowerShell via SSH

To prevent Korean/UTF-8 output corruption when executing Windows PowerShell commands via SSH, always use the following pattern.

```bash
# Correct pattern — set chcp 65001 via cmd then execute powershell
ssh user@host "cmd /c \"chcp 65001 > nul && powershell -Command \"\"<command>\"\"\""

# Wrong pattern — chcp does not work inside PowerShell
ssh user@host "powershell -Command \"chcp 65001 >nul; <command>\""
```

- `chcp 65001`: Changes Windows code page to UTF-8
- `cmd /c` wrapping mandatory: PowerShell standalone treats `>nul` redirection as file output

## 19. Post-replacement immediate verification

After modifying file content with `sed`, `python replace`, `str_replace`, etc., always perform the following.

### Mandatory procedure

1. **Confirm replacement applied**: Print target lines with `grep` or `sed -n` to verify intended changes
2. **Check for remnants**: Run `grep -rn "old_value"` to ensure previous value doesn't remain in same file or project-wide
3. **Check impact scope**: If changed value (IP, path, hostname, etc.) exists in other files, scan project-wide (`grep -rn`)

### Additional rules for global value changes

When changing values used across **multiple files** (IP addresses, file paths, hostnames, etc.):

```bash
# Before change: identify all affected files
grep -rn "old_value" /project_root/ | grep -v ".log|.git"

# After change: confirm 0 remnants
grep -rn "old_value" /project_root/ | grep -v ".log|.git"
```

- **Identify all target files first**, then batch-change
- Partial change with "rest later" pattern prohibited — complete all at once or mark TODO

### Prohibited

- Proceeding to next task without verifying replacement result ❌
- Ignoring `replace()` matching failure (0 replacements) silently ❌
- Changing only some files when same value exists in multiple files, missing the rest ❌

### Python replace safe pattern

```python
# ❌ Dangerous — proceeds silently on match failure
content = content.replace(old, new)

# ✅ Safe — detects match failure immediately
if old not in content:
    print(f"WARNING: '{old[:50]}...' not found in {path}")
else:
    content = content.replace(old, new)
    print(f"✓ replaced in {path}")
```

### sed safe pattern

```bash
# ❌ Dangerous — exit 0 even with 0 matches
sed -i 's/old/new/g' file.txt

# ✅ Safe — verify change applied
sed -i 's/old/new/g' file.txt
grep -q "new" file.txt && echo "✓ applied" || echo "⚠️ not found"
```

## 20. VM deletion confirmation mandatory

VM deletion (Remove-VM, vagrant destroy, Stop-VM -Force, etc.) must **always list targets first and get user confirmation before proceeding**.

```
1. Display current VM list
2. Ask "These VMs will be deleted. Proceed?"
3. Execute deletion only after user approval
```

- Same rule applies to single VM deletion
- Recreation (delete → recreate) also requires confirmation before deletion

## 21. Zombie SSH process cleanup at session start

SSH/scp processes left over from previous sessions interrupted with Ctrl+C can exhaust the remote host's SSH MaxSessions, blocking new connections.

Run at session start or when SSH is unresponsive.

```bash
# Generic pattern — replace <target> with actual SSH target hostname or IP
ps -ef | grep -E "ssh.*<target>|timeout.*ssh" | grep -v grep

# Cleanup
sudo kill -9 $(ps -ef | grep -E "ssh.*<target>|timeout.*ssh" | grep -v grep | awk '{print $2}') 2>/dev/null
```

For the Windows Hyper-V host environment, substitute the account name from the
session context. Do not hardcode the account or host address in this rule.

```bash
HV_USER=<hyperv-account>
sudo kill -9 $(ps -ef | grep -E "ssh.*${HV_USER}|timeout.*ssh" | grep -v grep | awk '{print $2}') 2>/dev/null
```

## 22. Kiro Lock (concurrent work prevention)

> 🟡 Currently **disabled** (`~/.kiro/hooks/kiro-lock.disabled` exists). Skip this rule until re-enabled.

When enabled: before any file modification, follow `skill://kiro-lock` §1–3:

1. Check `.kiro-lock` in the project root (`.git` directory parent)
2. If absent → create lock file
3. After work → `rm -f .kiro-lock`

```bash
# Enable
rm ~/.kiro/hooks/kiro-lock.disabled

# Disable
touch ~/.kiro/hooks/kiro-lock.disabled
```

## 23. Immediate PLAN.md issue logging

When working in a project, log unexpected errors, escape issues, script bugs, or significant fixes in `.governance/PLAN.md` **immediately after resolving them**. Existing projects with a root `PLAN.md` may use that legacy path during migration.

### When to log

Log to `.governance/PLAN.md` when any of the following occur during work outside the plan document:

- Script execution fails (non-trivial error)
- Escape/quoting issue discovered (`$`, `\n`, `\\`, shell vs Python string)
- Code modification causes IndentationError or silent fail
- VM/infrastructure behavior differs from expectation **and root cause required >5 minutes to identify**
- Workaround applied **that is non-obvious or environment-specific**

🟡 **Exception**: Editing PLAN.md itself does not trigger this rule (no loop).
🟡 **Exception**: In a legacy project, if neither `.governance/PLAN.md` nor root `PLAN.md` exists, skip this rule. New repositories must create the default `.governance/PLAN.md` during initialization.
🟡 **Dedup**: Before adding a new issue, check if the same symptom already exists in PLAN.md. If so, append to the existing entry rather than creating a duplicate.
🟡 **Scope**: Only log issues that required non-trivial investigation or had non-obvious root causes. Skip simple retries, typos, or one-liner fixes with no learning value.
🟡 **Collaboration**: When working collaboratively, re-enable kiro-lock (§ 22) before logging to PLAN.md to prevent concurrent modification conflicts.

### What to log

Use the issue template in `.governance/PLAN.md` `## 이슈 기록`; use root `PLAN.md` only for legacy projects. Use the next sequential number after the last existing issue (check existing `#### 이슈 N:` entries to determine N):

```markdown
#### 이슈 N: 제목

- 증상: (what happened)
- 원인: (why it happened)
- 해결:
  ```bash/python/powershell
  (fix code)
  ```
- 재현 방법: (optional — how to reproduce)
  ```bash
  (reproduction command)
  ```
```

### Timing rule

- ✅ Log **immediately after fix** — same tool call or the very next one
- ❌ "I'll log it later" → always forgotten

### How to find PLAN.md

Look for `.governance/PLAN.md` first. Use root `PLAN.md` only as a legacy fallback:

```bash
ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
find "${ROOT}/.governance/PLAN.md" "${ROOT}/PLAN.md" -maxdepth 0 -type f 2>/dev/null
```

## 24. GitHub reference auto-append

When referencing a GitHub repository during work, automatically append the URL to `_reference/github_references.md`.

### Conditions

- Verify repository existence via GitHub API before adding:
  ```bash
  curl -s -o /dev/null -w "%{http_code}" https://api.github.com/repos/<owner>/<repo>
  # 200 = exists, 404 = not found
  ```
- Do not add if the same URL already exists in the file:
  ```bash
  grep -q "github.com/<owner>/<repo>" /root/32_system-engineering-resources/_reference/github_references.md
  # exit 0 = duplicate, skip
  ```
- Do not add temporary references (example-only, comparison-purpose).

### Classification rules

- URL or description contains `agent`, `ai`, `llm`, `prompt` → `## 1. AI/Agent`
- URL or description contains `packer`, `terraform`, `ansible`, `vagrant` → `## 2. Packer/IaC`
- Otherwise → `## 3. 도구`

### Entry format

```markdown
- [repo-name]: [github.com/owner/repo](https://github.com/owner/repo) — ★★☆☆☆
```

### Target file

```
/root/32_system-engineering-resources/_reference/github_references.md
```

## 25. Memory file management

`~/.kiro/.local/memory.md` stores persistent knowledge across sessions.

### Rules

- **Max 100 lines** — keep only active/relevant items
- Update when: architecture decisions finalized, environment changed, important issue resolved
- Delete when: item is no longer relevant or superseded
- Move old items to `~/.kiro/.local/memory_archive.md` if historical value exists
- Keep `~/.kiro/.local/memory.md` and `memory_private.md` out of Git and rsync mirrors
- Do not store passwords, tokens, private keys, or other credentials in either memory file

### Structure (fixed sections)

```
## 환경          ← server/tool versions, IPs
## 프로젝트 경로  ← active project paths
## 작업 규칙 요약 ← top rules (not duplicating work-rules)
## 최근 결정 사항 ← last 10 decisions (FIFO, oldest removed first)
```

### After modifying `.local/memory.md`

Always print confirmation after any update:

```
[.local/memory.md 업데이트] 추가/수정/삭제: <변경 내용 요약>
```

### Line count check

```bash
wc -l ~/.kiro/.local/memory.md  # must be <= 100
```

If over 100 lines: remove oldest entries from "최근 결정 사항" or archive them.

## 26. TODO batch pre/post output obligation

When executing TODO items in batches, the following outputs are **mandatory**.

### Batch size

- Default: **3 items** (write + verify cycle fits within context window)
- Final batch even if only 1~2 items: Pre/Post output still mandatory (no skip)
- Batch numbering: sequential from 1, persists across sessions (check `.governance/TODO.md` for last completed batch; use root `TODO.md` for legacy projects)

### Pre-execution Brief

Output as single block before starting:

```
=== Batch N: items A~B ===

Step 1. _reference preparation
  ├── A: [source file] → [action: existing / new / N/A (reason)]
  ├── B: [source file] → [action]
  └── C: [source file] → [action]

Step 2. Write documents (N)
Step 3. Table alignment (align script)
Step 4. md-style-check + md-heading-check + md-link-check (0 issues required)
Step 5. fact-check (rounds per fact-check table below)
  ├── Round 1: _reference cross-check (skip if N/A)
  ├── Round 2: official source direct verification (lynx -dump)
  └── Round 3: star rating + unverified numbers + exaggeration
Step 6. Update `.governance/TODO.md`
```

- Format: fixed tree style above (inside code block)
- "N/A" in _reference mapping must include reason in parentheses (e.g., `N/A (book-based, no official doc)`)
- If "new" items exist in Step 1, Step 2 is blocked until Step 1 completes (dependency gate)
- Round 1 shows "(skip if N/A)" — actual skip determined per fact-check round table

### Post-execution Summary

Output as single block after completion:

```
=== Batch N complete ===

| Document | md-style-check | fact-check |
|----------|----------------|------------|
| A.md     | ✅ 0 issues    | ✅ 3 rounds |
| B.md     | ✅ 0 issues (fix 1: diagram width) | ✅ 2 rounds (fix 1: number corrected) |

TODO update: items A~B ⬜ → ✅
README/CHANGELOG: [deferred to final batch / updated]
```

- If fixes occurred: note briefly in parentheses within the cell
- If no fixes: just `✅ 0 issues` / `✅ N rounds`
- README.md / CHANGELOG.md update: defer to final batch (avoid repeated edits), note "deferred" or "updated"

### Resume after interruption

On context compaction or session switch:

1. Read `.governance/TODO.md` — check each item status (✅ /⬜); use root `TODO.md` for legacy projects
2. Resume from next ⬜ item with Pre-execution Brief
3. If batch partially complete: skip already ✅ items, continue remaining only
4. Completion criteria: md-style-check 0 issues + all fact-check rounds passed + `.governance/TODO.md` marked ✅

### fact-check failure handling

1. Error found → fix the .md document immediately
2. Re-verify from the failed Round onward (prior Rounds not re-run)
3. Same error repeats 2x → root cause analysis:
   - If .md misquoted _reference → fix .md (most cases)
   - If _reference itself is suspected wrong → re-verify against official source (lynx -dump / API) before any _reference edit
   - _reference modification requires: official source confirmation + `last_checked` date update + INDEX.md version sync
   - Never modify _reference based on inference alone

### Scope

| Agent        | Condition                    | Output                                           |
|--------------|------------------------------|--------------------------------------------------|
| default chat | TODO §4 batch (1+ documents) | Pre + Post both                                  |
| doc-reviewer | 3+ file batch review         | target list (Pre) + per-file result table (Post) |
| all agents   | single doc outside TODO §4   | may skip                                         |

doc-reviewer threshold is 3+ because single-file review is its normal operation and does not need ceremony.

### fact-check round requirements

| Target                           | Required rounds | Content                                                   |
|----------------------------------|-----------------|-----------------------------------------------------------|
| _reference file                  | 2               | URL access + content verification against source          |
| .md (TODO §4, _reference exists) | 3               | _reference cross + official source + rating/numbers       |
| .md (TODO §4, _reference N/A)    | 2               | official source direct + rating/numbers (Round 1 skipped) |
| .md (other)                      | 1               | md-style-check pass is sufficient                         |
