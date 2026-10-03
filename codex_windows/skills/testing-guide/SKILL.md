---
name: testing-guide
description: Guides test writing with AAA pattern, BVA, EP, and edge case analysis. Use when writing unit tests, integration tests, or infrastructure validation tests.
---

# Testing Guide

<!-- CODEX-COMPAT-BEGIN -->
## Codex Windows 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트를 전체 보존하며, 플랫폼·경로·권한 충돌과 Windows 직접 실행은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 테스트 요청과 현재 변경의 검증 필요에 맞춰 AAA·BVA·EP·5축·오류·멱등성을 적용합니다. 기존 저장소 test runner를 우선하며 pytest 같은 도구가 없으면 설치됐다고 가정하지 않습니다. Python 표준 unittest 등 실제 사용할 수 있는 수단을 선택하거나 미실행 이유를 기록합니다.
- 외부 edge case 문서는 같은 폴더에 동봉합니다. Terraform/Ansible/Docker/AWS 명령은 사용자의 대상 도구가 실제 존재하고 허용된 범위에 한해 실행하며, 문서 예시만 읽고 통과했다고 하지 않습니다.

### Windows 네이티브 실행

이 Windows 활성본에서는 이 COMPAT 절의 실행 절차를 우선합니다. 아래 보존 본문의 POSIX 셸·`python3`·`/root/...`·Kiro 명령은 원문 비교 자료입니다. 원문의 목적·전체 체크리스트는 유지하고 Windows에서 실행할 때는 여기의 실제 도구·대상 확인 절차로 옮깁니다. 원문 예시를 PowerShell에 그대로 붙여 넣거나 이미 설치·검증된 결과로 취급하지 않습니다.

- 실제 Git 루트·현재 변경·해당 저장소 지침을 확인하고 현재 작업에 필요한 자료만 읽습니다. 다른 저장소 profile이나 30/31 관리 자료를 필수 의존성으로 삼지 않습니다. 이미 적용된 저장소 지침은 그 적용 범위 안에서 유지합니다.
- PowerShell에서 실제 Python 3.11 이상을 확인합니다. `Get-Command python`과 `python -X utf8 -B --version`을 사용하며 `python3` 별칭·WSL·pip 설치를 가정하지 않습니다. 존재하지 않으면 설치/환경 확인이 필요한 미실행으로 보고합니다.
- 파일 작업은 실제 Windows 절대 경로와 `-LiteralPath`를 사용합니다. 공백·한글 경로는 인수로 따로 전달하고, UTF-8 입출력을 명시합니다. 경로 값에 셸 코드를 결합하지 않습니다. 예시의 `$SkillDir`·`$Target`은 실제 확인한 폴더/파일로 지정하며 `$HOME`·`$CODEX_HOME`을 재할당하지 않습니다.
- 실행 스크립트가 동봉된 스킬은 이 폴더 안의 사본을 사용합니다. 세 Markdown 검사기가 동봉된 경우 `scripts/md_common.py`도 같은 폴더에 있어야 합니다. 스크립트가 없는 스킬에 실행 도구가 구현됐다고 가정하지 않습니다. 폴더 전체 복사 외 별도 중앙 설치·전역 alias가 필요하지 않습니다.
- PowerShell 문법 검사·Python AST 검사는 실제 프로그램 실행 결과와 구분합니다. 현재 대상·실행 도구·제외 설정·종료 코드를 기록하고 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다.

### 실제 도구와 실행 계층

Terraform·Docker·AWS는 현재 설치된 Windows CLI와 현재 승인된 로컬/원격 대상을 먼저 확인합니다. 실행 파일이 있다고 daemon·workspace·인증·원격 접근이 준비됐다고 가정하지 않습니다. Terraform `validate`/`plan`의 관찰 범위와 실제 `apply`의 변경 승인은 별개입니다. Docker 조회도 승인된 daemon/context와 컨테이너를 명시합니다.

Ansible은 승인된 WSL/Linux 제어 노드나 원격 제어 노드의 실행 계층을 구분합니다. Windows PowerShell에 POSIX/Ansible 실행 환경이 있다고 가정하지 않습니다. WSL 설치·Linux 패키지 설치·원격 로그인·운영 변경은 이 스킬의 문서 예시만으로 수행하지 않습니다.

대상 인수가 빠진 보존 원문의 시험 명령은 다음처럼 실제 승인된 playbook/컨테이너를 명시하여 대체합니다. Ansible 두 명령은 확인된 Linux 제어 노드에서 실행하며 `--check --diff`도 지원 모듈과 정보 노출 범위를 확인합니다. `site.yml`은 실제 현재 playbook으로 바꿉니다.

```text
ansible-playbook --syntax-check site.yml
ansible-playbook --check --diff site.yml
```

```powershell
$Container = 'approved-container'  # 실제 대상 ID 또는 이름
docker inspect --format '{{.State.Health.Status}}' $Container
```

마지막 명령은 대상에 HEALTHCHECK가 설정됐을 때만 건강 상태를 보여 줍니다. HEALTHCHECK가 없거나 daemon/대상이 없으면 건강 통과로 보고하지 않습니다. 원문의 `pytest`·외부 scanner 등도 실제 설치와 현재 명령 인수를 확인하고, 미설치 상태에서는 표준 `unittest` 등 가능한 검사 범위 또는 미실행 사유를 기록합니다.

로컬 워크플로 대응(필요한 항목만 읽음):

- `skill://debugging-and-recovery` → [debugging-and-recovery](references/skills/debugging-and-recovery.md).

5축 상세: [edge case testing](references/resources/edge_case_testing.md). 원래 file URI 대신 이 자료를 읽습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


Apply when: "테스트 작성", "테스트 추가", "test", "write test"

## Structure (AAA Pattern)

```python
def test_<target>_<condition>_<expected>():
    # Arrange
    ...
    # Act
    ...
    # Assert
    ...
```

## FIRST Principles
- Fast: no external I/O
- Isolated: no dependency between tests
- Repeatable: same result every run
- Self-validating: assert determines pass/fail
- Timely: written with production code

## Boundary Value Analysis (BVA)

For any range [min, max], always test:
- min-1, min, min+1, max-1, max, max+1

## Equivalence Partitioning (EP)

- Identify valid/invalid partitions
- Pick 1 representative from each partition
- Include: None, empty string, empty list

## Coverage Target
- Branch coverage priority (both if/else)
- Exception paths (try/except, raise conditions)
- Normal path + error path

## pytest Rules
- `@pytest.mark.parametrize` for multiple inputs
- `@pytest.fixture` for shared setup
- `pytest.raises()` for exception verification
- File: `test_<module>.py`
- Function: `test_<target>_<condition>_<expected>()`

## Mock Rules
- External API, DB, filesystem → Mock
- Pure logic functions → no Mock
- Use `unittest.mock.patch`

## Test Type Selection

| Request            | Test Type                       |
|--------------------|---------------------------------|
| Function/class     | Unit test (BVA + EP)            |
| Module integration | Integration test                |
| Bug fix            | Regression test (reproduce bug) |
| API endpoint       | Integration + status code       |

## Checklist (every test)
- [ ] Happy path
- [ ] Error case (invalid input, exception)
- [ ] Boundary values (min, max, min-1, max+1)
- [ ] Empty input (None, "", [])
- [ ] Edge cases (see 5-axis below)
- [ ] Idempotency (if applicable)

## Edge Case Analysis (5-axis)

Derive edge cases from 5 axes. Pick at least 1 from each applicable axis.

| Axis        | Question                               | Examples                                 |
|-------------|----------------------------------------|------------------------------------------|
| Input       | Empty, max length, special chars?      | null, 0, MAX_INT, unicode, newline       |
| Environment | Disk full, OOM, network down?          | DNS fail, read-only mount, low bandwidth |
| State       | Initial, mid-failure, post-restart?    | uninitialized, partial write, cold start |
| Time        | Concurrency, timeout, order reversal?  | simultaneous write, expired token        |
| Resource    | Exhaustion, contention, limit reached? | FD exhausted, pool full, PID limit       |

Reference: `file:///root/32_system-engineering-resources/01_fundamentals/cs/testing/04_test_design/edge_case_testing.md`

### Terminology

| Term            | Meaning                              |
|-----------------|--------------------------------------|
| Edge case       | Boundary of valid range              |
| Corner case     | Multiple boundaries intersecting     |
| Degenerate case | Extremely simple/empty input         |
| Race condition  | Timing-dependent concurrent conflict |

## Infrastructure Testing

| 대상             | 검증 명령어                              |
|------------------|------------------------------------------|
| Terraform syntax | `terraform validate`                     |
| Terraform format | `terraform fmt -check`                   |
| Terraform plan   | `terraform plan` (No unexpected changes) |
| Ansible syntax   | `ansible-playbook --syntax-check`        |
| Ansible dry-run  | `ansible-playbook --check --diff`        |
| Shell scripts    | `shellcheck <script>.sh`                 |
| Shell syntax     | `bash -n <script>.sh`                    |

### IaC Test Principles
- `terraform plan` before every apply
- `ansible --check` before every run
- Idempotency: re-run produces no changes
- Validate after apply: health check, resource state query
- Test failure → switch to `skill://debugging-and-recovery`

### Container / Docker Testing

| 대상             | 검증 명령어                                          | 
|------------------|------------------------------------------------------|
| Dockerfile lint  | `hadolint Dockerfile`                                |
| Image build      | `docker build --no-cache -t test .`                  |
| Container health | `docker inspect --format='{{.State.Health.Status}}'` |
| Compose syntax   | `docker compose config`                              |
| Port binding     | `ss -tlnp` 으로 포트 확인                            |

### Post-Change Verification Pattern

변경 후 반드시 실행하는 검증 순서:

```bash
# 1. 문법/구문 검증
terraform validate && terraform fmt -check
ansible-playbook --syntax-check site.yml
bash -n script.sh && shellcheck script.sh

# 2. Dry-run
terraform plan
ansible-playbook --check --diff site.yml

# 3. 적용 후 상태 확인
terraform plan  # "No changes" 확인
curl -f http://endpoint/health
aws ec2 describe-instance-status --instance-ids <id>
```

## Red Flags

- 테스트 없이 "동작 확인했습니다" 주장
- happy path만 테스트하고 에러 케이스 누락
- edge case 도출 없이 "정상 동작" 판단
- terraform plan 미확인 상태에서 apply
- 테스트 실패를 무시하고 진행
- "나중에 테스트 추가하겠습니다"로 건너뜀
