---
name: code-review
description: Provides a structured code review checklist. Use when reviewing code, scripts, or IaC files. Covers correctness, security, error handling, performance, and infrastructure as code.
---

# Code Review

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 사용자가 지정한 변경·파일과 실제 적용 저장소 기준으로 원문 리뷰 항목을 적용합니다. 읽기 전용 리뷰 요청에서는 코드 수정·commit/push를 자동 수행하지 않습니다. 실제 관찰한 문제에 파일/위치·영향·근거를 붙이고 실행하지 않은 test/보안 검사를 통과로 기록하지 않습니다.

원문 비교 자료: [Kiro 원문](../originals/code-review.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
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
