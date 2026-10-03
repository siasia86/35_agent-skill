---
name: code-review
description: Provides a structured code review checklist. Use when reviewing code, scripts, or IaC files. Covers correctness, security, error handling, performance, and infrastructure as code.
---

# Code Review

<!-- CODEX-COMPAT-BEGIN -->
## Windows Codex 실행 및 적용 규칙

이 절과 이 절에서 연결한 실행 도구가 Windows의 현재 실행 본문입니다. 아래 Linux/Kiro 원문의 코드·명령·경로는 전체 보존한 비교 자료이며 그대로 자동 실행하지 않습니다. 원문의 목적·예시·체크리스트는 유지하되 플랫폼 차이와 교정 사항은 이 절의 실행 계약을 적용합니다. Linux 본문은 `codex_linux/`에 보존되어 있으며 이번 이식은 경량화·통합 작업이 아닙니다.

- 시스템·개발자·관리 정책과 실제 권한 안에서 **사용자 명시 지시 > 적용 저장소 AGENTS > 개인 스킬 기본값**을 적용합니다. 이미 부여된 범위와 승인을 유지하고 다른 저장소·개인 홈·시스템·운영 환경의 수정 권한을 경로 존재로 추정하지 않습니다.
- 실제 Git 루트·branch·기존 변경을 먼저 확인합니다. 필요한 본문·동봉 참조만 읽고 다른 스킬·전체 작업 기록을 자동 로드하지 않습니다. 원문의 `skill://`는 아래 로컬 참조로 해석하며 URI 도구를 호출하지 않습니다.
- 이 폴더를 통째로 복사하는 개인 스킬입니다. 필수 참조는 아래 상대 링크를 사용합니다. 중앙 catalog·설치기·다른 저장소 또는 형제 스킬 설치를 필수로 요구하지 않습니다. 원문 `references/kiro-original.md`는 비교 자료입니다.
- 네이티브 Windows 작업 셸은 PowerShell입니다. 파일 작업은 `-LiteralPath` 등 실제 대상 인자로 처리하며 셸 문자열·`eval`로 외부 입력을 재해석하지 않습니다. Python 3.11 이상을 `python -X utf8`로 실행하고 Python 하위 실행은 `[sys.executable, '-X', 'utf8', ...]` 인자 배열을 사용합니다. 실제 Python 위치·버전은 현재 환경에서 확인합니다.
- Bash 업무는 Git Bash 또는 승인된 WSL에서 유지합니다. PowerShell에서 Bash/POSIX 예제를 직접 실행하지 않습니다. 원문의 `/root`, `/var/log`, `/backup`, Kiro hook은 과거 환경 자료이며 Windows 개인 홈·시스템 경로로 자동 치환하지 않습니다.
- 검증은 **통과 / 부분 검사 / 실패 / 미실행**을 실행 목적·관찰·다음 조치와 함께 기록합니다. 경로 치환이나 과거 완료 기록을 현재 동작 통과로 사용하지 않습니다. 비공개 경로·계정·토큰·운영 자료를 공개 결과에 복사하지 않습니다.

### 현재 Windows 리뷰 절차

요청한 변경·파일의 실제 코드와 현재 저장소 기준으로 아래 원문 checklist 전체를 적용합니다. 읽기 전용 리뷰는 수정·commit·push·설치를 포함하지 않습니다. 발견 사항은 실제 재현 또는 제어 흐름의 근거와 파일·행·발생 조건·영향·수정 방향을 붙이고, 이미 수정된 역사 결함을 현재 결함으로 다시 보고하지 않습니다. Windows 미지원이 명시된 Linux 전용 자료는 Windows 결함으로 오인하지 않습니다.

- 네이티브 PowerShell의 cmdlet 오류와 외부 프로그램 `$LASTEXITCODE`를 각각 확인합니다. `$ErrorActionPreference = 'Stop'`만으로 모든 native exit 실패가 전파된다고 가정하지 않습니다. 외부 명령은 인자 배열·`-LiteralPath`를 사용하고 `cmd /c` 또는 Bash로 파일 삭제를 우회하지 않습니다.
- Python은 3.11+의 `python -X utf8`와 `sys.executable` 하위 실행을 확인합니다. POSIX-only import·fcntl·fchown/fchmod·symlink/reparse·junction·ACL/ADS·파일 공유/replace·경로 인코딩·CRLF 차이를 실제 지원 계약에 맞춰 검토합니다. Windows의 지원 범위를 무조건 POSIX와 동등하다고 표시하지 않습니다.
- 원문 shell checklist의 `set -euo pipefail`, trap, shellcheck는 실제 Bash 자료에만 적용합니다. 복합 함수/if 조건 안에서 명시적 오류 반환을 확인하며 `set -e` 유무만으로 성공 판정하지 않습니다. PowerShell 코드에는 해당 언어의 오류·cleanup·입력/상태 계약을 검토합니다.
- 잠금·부분 쓰기·리소스 정리는 현재 요청에 필요한 안전 TEMP fixture로 검증하고 실패/미실행 범위를 구분합니다. test가 없는 범위의 정책·권한·운영 실행을 임의로 추가하지 않습니다. 의미 있는 결함과 기능 위험에 집중하며 검토 기록은 코드 전체나 비공개 증거를 복사하지 않습니다.
- 원문의 결과 표·심각도·Priority·Red Flags는 유지합니다. 적용 저장소가 P1/P2/P3 등 다른 표기를 지정하면 그 형식을 따르며 관찰하지 않은 검사를 통과로 쓰지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md).
<!-- CODEX-COMPAT-END -->


Apply when: "리뷰", "review", "검토", "코드 리뷰"

## Checklist

### 1. Correctness
- Logic matches requirements
- Boundary handling (off-by-one, min/max, empty input)
- Missing exception/error handling
- Type mismatch, None/null reference
- Return value correctness (all paths return expected type)

### 2. Security
- Hardcoded secrets/keys/passwords
- SQL/Command injection (use parameterized queries)
- Missing input validation (user input untrusted)
- Missing authorization/authentication check
- Sensitive data in logs or error messages
- Path traversal (user-controlled file paths)

### 3. Error Handling
- Bare except (`except:` → `except Exception:`)
- Silent error swallowing (pass in except)
- Useful error messages (include context for debugging)
- Resource cleanup (finally, context manager, try-with)
- Graceful degradation on external service failure

### 4. Performance
- Unnecessary loops (N+1 query, nested loops on large data)
- Memory: loading entire file/dataset into memory
- Unclosed connections/file handles/cursors
- Cacheable repeated computation
- Blocking I/O in async context

### 5. Concurrency (if applicable)
- Race condition (shared mutable state)
- Deadlock potential (lock ordering)
- Thread safety of shared resources
- Atomic operations where needed

### 6. Readability / Maintainability
- Clear naming (functions, variables, classes)
- Function length (>50 lines → consider splitting)
- DRY violation (duplicated code → extract)
- Magic numbers/strings → named constants
- Comments: missing where complex, unnecessary where obvious
- Consistent code style with project

### 7. Test Adequacy (if tests exist)
- Happy path covered
- Error/exception cases covered
- Boundary values (BVA): min-1, min, max, max+1
- Equivalence partitions: all groups represented
- Branch coverage: both if/else paths tested
- Mock usage appropriate (external deps only)

### 8. Compatibility
- Python version compatibility (f-string 3.6+, match 3.10+, etc.)
- OS-specific code (path separators, commands)
- Dependency version constraints

### 9. Infrastructure as Code (Terraform / Ansible)
- Hardcoded values → variables or locals
- Missing `description` on variables/outputs
- Resource naming convention (`[env]-[category]-[service]-[detail]`)
- Missing tags (Name, Environment, Owner, ManagedBy)
- Overly permissive IAM (`*` actions or resources)
- Security Group `0.0.0.0/0` inbound without justification
- Missing encryption (S3, EBS, RDS `storage_encrypted`)
- No lifecycle/prevent_destroy on stateful resources
- Ansible: missing `become`, handler not notified, no `changed_when`
- State drift risk: manual console changes not reflected in code

### 10. Shell / Bash Scripts
- Missing `set -euo pipefail` (fail-fast + undefined var detection)
- Unquoted variables (`$VAR` → `"$VAR"`, prevents word splitting)
- Missing input validation (argument count, file existence)
- Hardcoded paths → variables or config file
- No cleanup trap (`trap cleanup EXIT`)
- Using `echo` for errors → `>&2` (stderr)
- Parsing command output instead of using proper tools (awk/jq)
- Missing `shellcheck` compliance
- Race condition in temp file creation → `mktemp`
- Excessive use of `sudo` without justification

## Output Format

```
## 코드 리뷰 결과

| # | 심각도 | 위치 | 문제 | 제안 |
|---|--------|------|------|------|
| 1 | 🔴     | L42  | ...  | ...  |
| 2 | 🟡     | L78  | ...  | ...  |

심각도: 🔴 bug/security | 🟡 improvement | ☆ suggestion

총평: (1~2문장 요약)
```

## Priority
- 🔴 items: must fix before merge
- 🟡 items: should fix (technical debt if skipped)
- ☆ items: optional improvement

## Red Flags

- 리뷰 없이 merge/apply 진행
- 🔴 항목을 무시하고 진행
- "나중에 고치겠습니다"로 보안 이슈 보류
- 리뷰 범위를 임의로 축소 (요청된 파일 일부만 검토)
- 변경 의도를 이해하지 않고 형식만 검토
