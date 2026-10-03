---
name: security-tools
description: Documents security masking tools (ip_mask.py, json_mask.py, aws-security-check.sh, git-security-check.sh). Use when masking sensitive data, running security checks, or modifying masking scripts.
---

# Security Masking Tools

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 이 스킬은 마스킹 도구의 설계·수정·검증과 보안 점검 지침입니다. 원문 개인 스크립트 5개와 config는 이 저장소에 없으므로 설치되어 있다고 가정하거나 그 결과를 조작하지 않습니다. Python 표준 라이브러리·읽기 전용 검색·Git 조회로 아래 9개/5개 항목을 각각 점검하고 비밀 값은 출력하지 않습니다. 특정 원문 도구와 동일한 실행/정규식/map 호환성이 검증됐다는 주장은 하지 않습니다.
- 마스킹 실행 요청이면 작업 범위 안에서 아래 명세에 맞는 도구를 구현하거나 사용자가 제공한 실제 도구를 확인하고, 격리 fixture에서 문법·round-trip·재실행 멱등·원자적 저장·권한·serial/기존 map 호환 검사를 수행한 뒤 승인된 대상만 처리합니다. 원문의 옵션·색상·18규칙/자원 명칭·9/5 검사 항목은 삭제하지 않습니다. 원문 17종 표기와 실제 나열 수의 차이 또는 미제공 map 형식/정규식은 추정으로 채우지 않고 확인 필요로 보고합니다.
- 복원은 map·serial·원본/마스킹 해시 의미를 먼저 확인합니다. 형식이 불명확하거나 해시가 다르면 중단하고 사용자 데이터를 덮어쓰지 않습니다. --force도 현재 사용자의 명시 요청 없이 적용하지 않습니다. map은 민감한 원본을 포함하므로 공개 출력·Git staging·동기화에서 제외하고 복원 후 보존합니다. 대량 마스킹은 대상·복구 방법을 먼저 제시합니다.
- 외부 conf가 없으면 그 파일을 다른 저장소에서 찾거나 생성하지 않습니다. 제외값은 현재 사용자/저장소가 제공한 fixture·예외만 사용하고 실제 비밀을 예외에 넣지 않습니다. Docker 수동 점검은 그대로 수행합니다. 동봉 Markdown 검사 외 실제 scanner를 실행하지 않은 항목은 수동 검사/미실행으로 구분합니다.

문서 스타일은 동봉 [STYLE.md](references/STYLE.md)를 사용합니다. `sia-md-*` 대신 동봉 스크립트를 Python 3.11 이상으로 실행합니다. 기본 OS/언어 runtime 외 pip·다른 저장소 설치는 필요하지 않습니다. 대상 저장소의 선택적 TOML 설정은 실제 존재할 때만 적용합니다.

- `python3 <SKILL_DIR>/scripts/md-style-check.py <target>`
- `python3 <SKILL_DIR>/scripts/md-heading-check.py <target>`
- `python3 <SKILL_DIR>/scripts/md-link-check.py <target>`

`<SKILL_DIR>`는 현재 복사된 스킬 폴더입니다. 원문의 fix_table_align/trim_diagram 외부 자동 수정기를 필수로 호출하지 않고, 보고된 표/다이어그램을 현재 파일에서 직접 수정한 뒤 다시 검사합니다. 외부 스크립트의 모든 옵션이 구현됐다고 주장하지 않습니다.

저장소 지침이 푸터·날짜·배지를 금지하면 style 검사에 `--no-footer`를 사용하고 그 적용 근거와 제외 범위를 기록합니다. 다른 검사는 계속 실행합니다. 정책상 금지된 푸터를 검사 통과 목적으로 추가하거나 그 결과를 미해결 오류로 취급하지 않습니다. 실제 내용 결함을 숨기기 위한 임의 skip은 하지 않습니다.

- 동봉 STYLE §12의 `readme-template` 참조는 [전체 readme-template 지침](references/skills/readme-template.md)으로 해석합니다. 대상 문서에 적용할 개인 푸터 기본값·원문 예외와 사용자/저장소의 상위 지침을 함께 확인하며, 형제 스킬 설치를 요구하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
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
