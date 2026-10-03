---
name: security-tools
description: Documents security masking tools (ip_mask.py, json_mask.py, aws-security-check.sh, git-security-check.sh). Use when masking sensitive data, running security checks, or modifying masking scripts.
---

# Security Masking Tools

<!-- CODEX-COMPAT-BEGIN -->
## Codex Windows 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트를 전체 보존하며, 플랫폼·경로·권한 충돌과 Windows 직접 실행은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 이 스킬은 마스킹 도구의 설계·수정·검증과 보안 점검 지침입니다. 원문 개인 스크립트 5개와 config는 이 저장소에 없으므로 설치되어 있다고 가정하거나 그 결과를 조작하지 않습니다. Python 표준 라이브러리·읽기 전용 검색·Git 조회로 아래 9개/5개 항목을 각각 점검하고 비밀 값은 출력하지 않습니다. 특정 원문 도구와 동일한 실행/정규식/map 호환성이 검증됐다는 주장은 하지 않습니다.
- 마스킹 실행 요청이면 작업 범위 안에서 아래 명세에 맞는 도구를 구현하거나 사용자가 제공한 실제 도구를 확인하고, 격리 fixture에서 문법·round-trip·재실행 멱등·원자적 저장·권한·serial/기존 map 호환 검사를 수행한 뒤 승인된 대상만 처리합니다. 원문의 옵션·색상·18규칙/자원 명칭·9/5 검사 항목은 삭제하지 않습니다. 원문 17종 표기와 실제 나열 수의 차이 또는 미제공 map 형식/정규식은 추정으로 채우지 않고 확인 필요로 보고합니다.
- 복원은 map·serial·원본/마스킹 해시 의미를 먼저 확인합니다. 형식이 불명확하거나 해시가 다르면 중단하고 사용자 데이터를 덮어쓰지 않습니다. --force도 현재 사용자의 명시 요청 없이 적용하지 않습니다. map은 민감한 원본을 포함하므로 공개 출력·Git staging·동기화에서 제외하고 복원 후 보존합니다. 대량 마스킹은 대상·복구 방법을 먼저 제시합니다.
- 외부 conf가 없으면 그 파일을 다른 저장소에서 찾거나 생성하지 않습니다. 제외값은 현재 사용자/저장소가 제공한 fixture·예외만 사용하고 실제 비밀을 예외에 넣지 않습니다. Docker 수동 점검은 그대로 수행합니다. 동봉 Markdown 검사 외 실제 scanner를 실행하지 않은 항목은 수동 검사/미실행으로 구분합니다.

### Windows 네이티브 실행

이 Windows 활성본에서는 이 COMPAT 절의 실행 절차를 우선합니다. 아래 보존 본문의 POSIX 셸·`python3`·`/root/...`·Kiro 명령은 원문 비교 자료입니다. 원문의 목적·전체 체크리스트는 유지하고 Windows에서 실행할 때는 여기의 실제 도구·대상 확인 절차로 옮깁니다. 원문 예시를 PowerShell에 그대로 붙여 넣거나 이미 설치·검증된 결과로 취급하지 않습니다.

- 실제 Git 루트·현재 변경·해당 저장소 지침을 확인하고 현재 작업에 필요한 자료만 읽습니다. 다른 저장소 profile이나 30/31 관리 자료를 필수 의존성으로 삼지 않습니다. 이미 적용된 저장소 지침은 그 적용 범위 안에서 유지합니다.
- PowerShell에서 실제 Python 3.11 이상을 확인합니다. `Get-Command python`과 `python -X utf8 -B --version`을 사용하며 `python3` 별칭·WSL·pip 설치를 가정하지 않습니다. 존재하지 않으면 설치/환경 확인이 필요한 미실행으로 보고합니다.
- 파일 작업은 실제 Windows 절대 경로와 `-LiteralPath`를 사용합니다. 공백·한글 경로는 인수로 따로 전달하고, UTF-8 입출력을 명시합니다. 경로 값에 셸 코드를 결합하지 않습니다. 예시의 `$SkillDir`·`$Target`은 실제 확인한 폴더/파일로 지정하며 `$HOME`·`$CODEX_HOME`을 재할당하지 않습니다.
- 실행 스크립트가 동봉된 스킬은 이 폴더 안의 사본을 사용합니다. 세 Markdown 검사기가 동봉된 경우 `../../scripts/md_common.py`도 같은 폴더에 있어야 합니다. 스크립트가 없는 스킬에 실행 도구가 구현됐다고 가정하지 않습니다. 폴더 전체 복사 외 별도 중앙 설치·전역 alias가 필요하지 않습니다.
- PowerShell 문법 검사·Python AST 검사는 실제 프로그램 실행 결과와 구분합니다. 현재 대상·실행 도구·제외 설정·종료 코드를 기록하고 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다.

문서 스타일은 동봉 [STYLE.md](../STYLE.md)를 사용합니다. `sia-md-*` 대신 동봉 스크립트를 Python 3.11 이상으로 실행합니다. 기본 OS/언어 runtime 외 pip·다른 저장소 설치는 필요하지 않습니다. 대상 저장소의 선택적 TOML 설정은 실제 존재할 때만 적용합니다.

```powershell
$SkillDir = 'C:\work\skills\security-tools'  # 실제 복사된 해당 스킬 폴더
$Target = 'C:\work\repo\README.md'  # 현재 요청의 실제 대상
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-style-check.py') $Target
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-heading-check.py') $Target
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-link-check.py') $Target
```

각 호출 직후 `$LASTEXITCODE`를 확인합니다. 앞 명령이 실패한 결과를 마지막 호출의 성공으로 덮어 해석하지 않습니다. 명시한 미존재 입력은 종료 코드 `1`이며 유효 파일과 혼합돼도 실패입니다. 빈 디렉토리·설정상 제외된 파일은 실제 검사 수와 제외 이유를 함께 보고합니다.

파일 검사기는 inline Markdown 링크의 각괄호 목적지·공백·균형 괄호·URL 인코딩 경로를 처리합니다. reference-style 링크·네트워크 URL·다른 파일 내부 앵커는 별도 범위이며 모두 통과했다고 확장하지 않습니다. 같은 파일 헤딩 앵커는 실제 등장 순서의 중복 suffix를 확인하고, 중복 헤딩 정책 검사와 앵커 존재 검사를 구분합니다. 인용구·backtick·tilde 펜스의 예시는 코드로 제외합니다. 닫히지 않은 펜스가 있으면 링크 검사 종료 코드 `2`를 미완료로 보고합니다.


`<SKILL_DIR>`는 현재 복사된 스킬 폴더입니다. 원문의 fix_table_align/trim_diagram 외부 자동 수정기를 필수로 호출하지 않고, 보고된 표/다이어그램을 현재 파일에서 직접 수정한 뒤 다시 검사합니다. 외부 스크립트의 모든 옵션이 구현됐다고 주장하지 않습니다.

저장소 지침이 푸터·날짜·배지를 금지하면 style 검사에 `--no-footer`를 사용하고 그 적용 근거와 제외 범위를 기록합니다. 다른 검사는 계속 실행합니다. 정책상 금지된 푸터를 검사 통과 목적으로 추가하거나 그 결과를 미해결 오류로 취급하지 않습니다. 실제 내용 결함을 숨기기 위한 임의 skip은 하지 않습니다.

- 동봉 STYLE §12의 `readme-template` 참조는 [전체 readme-template 지침](../skills/readme-template.md)으로 해석합니다. 대상 문서에 적용할 개인 푸터 기본값·원문 예외와 사용자/저장소의 상위 지침을 함께 확인하며, 형제 스킬 설치를 요구하지 않습니다.

### Windows 보안 도구 경계

원문의 `.sh` scanner·개인 마스킹 스크립트·외부 config는 이 Windows 폴더에 실행 구현으로 제공되지 않습니다. 이를 `.ps1`과 동등하다고 간주하거나 실제 비밀 값으로 시험하지 않습니다. 요청된 도구 구현/이관은 비식별 TEMP fixture로 검증한 뒤 현재 승인 범위에서 진행하며, 읽기 전용 수동 점검과 실제 scanner 실행 결과를 구분합니다.

마스킹 map·serial·원문을 포함한 복구 자료는 현재 사용자에게 허용된 비공개 경로에 보존합니다. POSIX mode/chown을 Windows ACL로 동일시하지 않습니다. 실제 파일 ACL과 대상 권한을 확인하고, 이 문서만으로 사용자/시스템 ACL·개인 홈·동기화 정책을 변경하지 않습니다. 복원 전 map/serial/해시 검증과 --force의 명시 요청 조건은 그대로 유지합니다.

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

원문 비교 자료: [Kiro 원문](../originals/security-tools.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 1. Script list

| File                                 | Purpose                                                 | Target                     |
|--------------------------------------|---------------------------------------------------------|----------------------------|
| `/root/sj_del/ip_mask.py`            | Public IP masking and restoration using RFC 5737 ranges | All text files             |
| `/root/sj_del/json_mask.py`          | AWS resource masking with 18 regex rules                | `.json` files              |
| `/root/sj_del/aws_security_check.sh` | AWS sensitive-data detection with 9 checks              | Directory scan             |
| `/root/sj_del/git_security_check.sh` | Pre-commit security check with 5 checks                 | Git working-tree directory |
| `/usr/local/bin/sia-md-style-check`  | Markdown style validation                               | `.md` files                |
| `/root/sj_del/security_check.conf`   | Shared configuration for Bash scripts                   | Configuration file         |

## 2. Common option scheme (`ip_mask.py` / `json_mask.py`)

| Option             | Description                                              |
|--------------------|----------------------------------------------------------|
| `-f` / `--file`    | Process a single file                                    |
| `-D` / `--dir`     | Process a directory recursively                          |
| `-r` / `--restore` | Restore the original content                             |
| `-d` / `--dry-run` | Preview changes without modifying files                  |
| `-v` / `--verbose` | Show changed lines in detail                             |
| `--all`            | Include unchanged files in output (`ip_mask.py`)         |
| `--force`          | Ignore serial mismatches                                 |
| `-V` / `--version` | Print the version                                        |
| `-i` / `--include` | Include only matching extensions                         |
| `-e` / `--exclude` | Exclude matching extensions                              |
| `-q` / `--quiet`   | Minimize log output                                      |
| `-m` / `--map`     | Specify a map file path directly                         |
| `--debug`          | Show pattern debugging information (`json_mask.py` only) |

## 3. Design principles

- Do not delete map files after restoration; they are required for reversibility.
- Verify the source file hash against the map `_meta.serial` value.
- Write atomically by using a temporary file followed by a rename.
- Preserve the original file permissions.
- Guarantee idempotency: re-running a mask operation produces no additional changes.
- Create a `.bak.N` backup before overwriting a map file.
- Keep the `SAFETY` line in `ip_mask.py` available for emergency execution blocking.

## 4. Color rules

| Color  | Usage                                   |
|--------|-----------------------------------------|
| Red    | Masked filename and masked count        |
| Purple | Restored filename and backup path       |
| Yellow | Skipped item, warning, or pre-change IP |
| Green  | Post-change IP or restored count        |
| Gray   | Line numbers such as `L1`               |

## 5. `ip_mask.py` details

- Automatically detects public IP addresses and excludes private, example, and special-purpose addresses.
- Allocates RFC 5737 ranges sequentially: `192.0.2.0/24` → `198.51.100.0/24` → `203.0.113.0/24` (maximum 762 addresses).
- Skips version-like values when an IP is adjacent to `-` or `_`.
- Stores the map at `<source_file>.map.ip.json`.
- Applies `SKIP_EXTS`, `SKIP_FILES`, and `SKIP_TARGETS` exclusions.
- Excludes `.git`, `.ssh`, and `.kiro` directories.
- Always excludes files whose names contain `.map.ip.json`.

## 6. `json_mask.py` details

- Provides 18 regex rules covering 17 resource types: `ACCOUNT-ID`, `BUCKET`, `VPCE-ID`, `VPC-ID`, `SUBNET-ID`, `SG-ID`, `ENI-ID`, `INSTANCE-ID`, `ELB-NAME`, `RDS-EP`, `CF-DIST-ID`, `NAT-GW-ID`, `RTB-ID`, `IGW-ID`, `IP`, and `DOMAIN`.
- Uses placeholders such as `<TYPE-N>`, for example `<IP-1>` and `<ACCOUNT-ID-1>`.
- Stores the map at `<source_file>.map.json`.
- Stores serial, source, and version metadata in the `_meta` block.

## 7. Verification procedure

After modifying masking scripts, run the following checks:

1. Verify Python syntax with `py_compile`.
2. Run the script against an isolated temporary directory.
3. Verify a mask → restore round trip.
4. Check compatibility with existing map files.
5. Restore the `SAFETY` line to its original state after testing.

The `SAFETY` line is normally commented and therefore allows execution. To block execution temporarily, uncomment the line below; restore the comment before normal use.

```python
#import sys; sys.exit(0)  # SAFETY: uncomment this line to disable the script
```

```bash
sudo python3 -c "import py_compile; py_compile.compile('/root/sj_del/ip_mask.py', doraise=True); print('OK')"
sudo python3 -c "import py_compile; py_compile.compile('/root/sj_del/json_mask.py', doraise=True); print('OK')"
```

## 8. `aws_security_check.sh` details

- Performs 9 checks: access keys, secret keys, account IDs, ARNs, VPCE IDs, public IPs, AWS resource IDs, S3 buckets, and tracked `.map.json` files.
- Dynamically loads `EXCLUDE_IPS` and `EXCLUDE_BUCKETS` from `/root/sj_del/security_check.conf`.
- Excludes version-like values when an IP is followed or preceded by `-`.
- Excludes `0x` hexadecimal addresses.
- Excludes `ami-` resource IDs from generic resource-ID detection.
- Uses fallback defaults when `/root/sj_del/security_check.conf` is unavailable.

## 9. `git_security_check.sh` details

- Performs 5 checks: sensitive IPs, passwords and keys, AWS account IDs, large files, and sensitive filenames.
- Scans files under `SCAN_DIR` (default: `.`); run it from the repository root when Git status output is required.
- Uses Git tracking information only for the tracked `.map.json` check.
- Dynamically loads `EXCLUDE_PASSWORDS`, `EXCLUDE_KEYWORDS`, and `EXCLUDE_ACCOUNTS` from `/root/sj_del/security_check.conf`.
- Excludes `0x` hexadecimal values, `ULL` C literals, and date-like values to reduce account-ID false positives.
- Applies `EXCLUDE_DIRS` and `EXCLUDE_FILES` while searching.
- Uses `printf`-style ANSI color output for portability.

## 10. Bash script common rules

- Use the output format `[N/M] check_name` followed by `✓`, `✗`, or `⚠`.
- Run `bash -n` after modifying either Bash script.
- Load shared settings from `/root/sj_del/security_check.conf`.
- Exclude the `.kiro` directory from scans.

## 11. Related configuration files

- `/root/sj_del/security_check.conf` — `EXCLUDE_IPS`, `EXCLUDE_PASSWORDS`, `EXCLUDE_KEYWORDS`, `EXCLUDE_ACCOUNTS`, `EXCLUDE_BUCKETS`, `EXCLUDE_DIRS`, and `EXCLUDE_FILES`.
- `/root/sj_del/ip_mask.toml` — Legacy configuration; currently unused.

## 12. AWS account ID and resource placeholders

Do not use real numeric AWS account IDs in documentation or examples. Security scanners treat 12-digit numbers as potential account IDs, so use the following placeholders:

- Account IDs: `<ACCOUNT-ID-1>`, `<ACCOUNT-ID-2>`
- IAM ARN: `arn:aws:iam::<ACCOUNT-ID-1>:root`, `arn:aws:iam::<ACCOUNT-ID-2>:role/backup-writer`
- KMS key ARN: `arn:aws:kms:ap-northeast-2:<ACCOUNT-ID-2>:key/<KEY-ID>`
- S3 bucket: `my-bucket`

Executable command examples must include the following replacement note:

```text
Replace <ACCOUNT-ID-1>, <ACCOUNT-ID-2>, <KEY-ID>, and my-bucket with actual values before execution.
```

- `123456789012` is retained only for compatibility with existing tests and `security_check.conf`; do not add it to new documentation or code.
- Do not add real account IDs to `EXCLUDE_ACCOUNTS` to hide scanner findings. Use that list only for reproducible test fixtures.
- Prefer the `<ACCOUNT-ID-N>` placeholders supported by `json_mask.py`; keep original account IDs separately with their map files.

## 13. Dockerfile / container security check

Manual inspection items not covered by the listed scripts:

- Pin image tags in `FROM`; do not use `:latest`.
- Do not run as `USER root`; specify a non-root user.
- Avoid unnecessary packages; use `--no-install-recommends` where applicable.
- Do not bake secrets into image layers; use a multi-stage build or `--secret`.
- Minimize the `COPY` scope and provide a `.dockerignore` file.
- Define a `HEALTHCHECK` instruction.
