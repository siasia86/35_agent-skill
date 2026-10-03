---
name: doubt-driven-infra
description: Subjects non-trivial infrastructure decisions to adversarial review before they stand. Use when making production changes, security-sensitive modifications, irreversible operations, or working in unfamiliar infrastructure code.
---

# Doubt-Driven Infra

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

### 단독 사용과 참조

폴더 전체가 사용 단위입니다. 이 폴더 안의 필수 참조·도구만 사용하며 중앙 catalog·installer·30/31 저장소나 다른 skill의 별도 설치를 요구하지 않습니다. `skill://`는 아래 동봉 대응으로 해석하고 Kiro URI/hook/memory API를 호출하지 않습니다. 개인 경로·계정·config 원문·자격증명·세션·raw 비공개 증거를 공개 자료에 복사하지 않습니다.

### Windows에서의 독립 검토

원문의 CLAIM → EXTRACT → DOUBT → RECONCILE → STOP과 비자명한 변경의 적용 조건을 유지합니다. Windows에서도 제공된 코드·plan·계약·미확인 자료로 반대 관점을 검토할 수 있습니다. 단순 질의·태그/설명 변경을 운영 감사로 확대하지 않습니다.

- fresh-context 검토를 실제 지원하는 협업 도구로 수행한 경우 지정 범위·입력·결과를 기록합니다. 기능이 없거나 현재 실행 범위 밖이면 자기 검토와 독립 검토를 구분하고 독립 검토를 했다고 주장하지 않습니다. 원문이 모든 요청의 새 agent 발동 조건은 아닙니다.
- AWS/Terraform 확인은 Windows의 실제 CLI·profile·계정·리전·backend에서 승인된 읽기 범위에 한해 수행합니다. shell의 역슬래시 줄 연결 대신 PowerShell 인수 배열이나 한 줄 호출을 사용하며 자료·권한을 추정하지 않습니다. IAM 시뮬레이션과 plan 결과는 실제 서비스 동작 전체를 보장하지 않습니다.
- `terraform plan -detailed-exitcode`의 0은 변경 없음, 2는 변경 있음, 1은 오류입니다. 2를 실패나 안전 승인으로 처리하지 않으며 예상 변경·보안·의존성은 따로 검토합니다.
- 실제 위험은 구현/적용을 멈추고 보완합니다. 검증 필요 항목을 조회할 수 없으면 미확인과 영향·다음 증거를 남깁니다. 기존 사용자 승인은 유지하되 승인만으로 관찰되지 않은 검사를 통과 처리하지 않습니다.
- cycle 한도와 종료 조건은 원문대로 유지하되 이미 확인한 동일 항목을 반복하지 않습니다. 현재 사용자 범위에 맞는 판정을 보고하고 검토 완료를 apply·권한 변경·원격 게시로 확대하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## Overview

확신은 정확성이 아닙니다. 인프라 변경은 비가역적이고 블래스트 레디어스가 크므로, 비자명한 결정에 대해 fresh-context adversarial review를 수행합니다.

이 스킬은 `/review`가 아닙니다. `/review`는 완성된 산출물에 대한 판정입니다. 이 스킬은 **진행 중인 결정**에 대한 교차 검증입니다.

## When to Use

결정이 **비자명(non-trivial)** 한 경우:

- 프로덕션 환경 변경 (terraform apply to prd)
- IAM 정책 수정 (권한 확대/축소)
- Security Group 규칙 변경
- 네트워크 구조 변경 (VPC, Subnet, Route Table)
- 데이터베이스 변경 (엔진 업그레이드, 파라미터 변경)
- 비가역적 작업 (리소스 삭제, 데이터 마이그레이션)
- 익숙하지 않은 인프라 코드 수정

**적용하지 않는 경우:**

- 태그 변경, 설명 수정
- dev 환경 단일 리소스 변경
- terraform fmt, 변수명 리네이밍
- 사용자가 명시적으로 속도 우선을 요청한 경우

## The Process

```
Doubt cycle:
- [ ] Step 1: CLAIM — 변경 내용 + 왜 안전한지 주장 작성
- [ ] Step 2: EXTRACT — 변경 코드/plan 결과만 분리 (추론 과정 제거)
- [ ] Step 3: DOUBT — adversarial 관점에서 반박 시도
- [ ] Step 4: RECONCILE — 발견 사항 분류 및 대응
- [ ] Step 5: STOP — 종료 조건 충족 확인
```

### Step 1: CLAIM

변경 내용과 안전성 주장을 명시합니다.

```
CLAIM:
- 변경: prd-sg-web에 443 포트 인바운드 규칙 추가
- 안전성 주장: ALB에서만 접근하므로 source를 ALB SG로 제한
- 블래스트 레디어스: web tier만 영향
- 롤백: 규칙 제거 (terraform apply 이전 코드)
```

### Step 2: EXTRACT

terraform plan 결과 또는 변경 코드만 분리합니다. 자신의 추론 과정은 제거합니다.

```
ARTIFACT:
  resource "aws_security_group_rule" "web_https" {
    type              = "ingress"
    from_port         = 443
    to_port           = 443
    protocol          = "tcp"
    source_security_group_id = aws_security_group.alb.id
    security_group_id = aws_security_group.web.id
  }

CONTRACT:
  - 443 포트만 허용
  - source는 ALB SG만
  - web SG에만 적용
```

### Step 3: DOUBT

adversarial 관점에서 반박합니다.

질문 목록:

| 검증 항목   | 질문                                        |
|-------------|---------------------------------------------|
| 범위 초과   | 이 규칙이 의도하지 않은 접근을 허용하는가?  |
| 의존성      | ALB SG가 이미 과도하게 열려 있지 않은가?    |
| 순서        | 이 변경 전에 필요한 선행 조건이 있는가?     |
| 롤백        | 롤백 시 서비스 중단이 발생하는가?           |
| State       | terraform state와 실제 리소스가 일치하는가? |
| 암묵적 가정 | "ALB에서만 접근"이라는 가정이 검증되었는가? |

### Step 4: RECONCILE

발견 사항을 분류합니다.

| 분류        | 조치                      |
|-------------|---------------------------|
| 실제 위험   | 변경 중단, 수정 후 재시도 |
| 검증 필요   | 명령어로 확인 후 진행     |
| 사소한 우려 | 기록 후 진행              |

### Step 5: STOP

종료 조건:

- 모든 "실제 위험" 해소
- 모든 "검증 필요" 항목 확인 완료
- 3회 사이클 초과 시 사용자에게 판단 위임
- 사용자가 명시적으로 진행 승인

## Verification Commands

DOUBT 단계에서 사용하는 검증 명령어:

```bash
# SG 현재 상태 확인
aws ec2 describe-security-groups --group-ids <sg-id> \
  --query 'SecurityGroups[].IpPermissions'

# IAM 정책 시뮬레이션
aws iam simulate-principal-policy --policy-source-arn <role-arn> \
  --action-names <action> --resource-arns <resource>

# Terraform state vs 실제 비교
terraform plan -detailed-exitcode

# 네트워크 도달성 확인
aws ec2 describe-network-interfaces --filters Name=group-id,Values=<sg-id>
```

## Common Rationalizations

| Rationalization                    | Reality                                                                  |
|------------------------------------|--------------------------------------------------------------------------|
| "plan 확인했으니 안전합니다"       | plan은 논리적 정합성만 보여줍니다. 보안/의존성은 별도 검증이 필요합니다. |
| "dev에서 테스트했습니다"           | prd는 네트워크, 권한, 데이터가 다릅니다. 환경 차이를 검증합니다.         |
| "작은 변경이라 doubt 불필요합니다" | SG 규칙 1줄이 전체 네트워크를 노출할 수 있습니다.                        |
| "시간이 없습니다"                  | 5분 doubt가 수 시간 장애 복구를 방지합니다.                              |
| "이전에도 이렇게 했습니다"         | 이전 결정이 올바른지도 검증 대상입니다.                                  |

## Red Flags

- terraform apply 전에 DOUBT 사이클 미수행
- "안전하다"는 주장에 검증 명령어 결과가 없음
- 블래스트 레디어스 미파악 상태에서 진행
- 암묵적 가정을 명시하지 않음
- DOUBT 단계에서 발견된 위험을 무시하고 진행
- 롤백 계획 없이 비가역적 변경 수행

## Verification

DOUBT 사이클 완료 후:

- [ ] 모든 CLAIM에 대해 DOUBT 수행
- [ ] "실제 위험" 항목 0건
- [ ] "검증 필요" 항목 모두 명령어로 확인
- [ ] 블래스트 레디어스 명시
- [ ] 롤백 계획 수립
- [ ] 사용자 승인 획득 (prd 변경 시)
