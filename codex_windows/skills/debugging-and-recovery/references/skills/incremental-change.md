---
name: incremental-change
description: Delivers infrastructure changes incrementally. Use when making any IaC change that touches multiple resources, modules, or environments. Use when a Terraform/Ansible change feels too large to apply in one step.
---

# Incremental Change

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
- 사용자와 저장소가 지정한 게시 순서를 따릅니다. 이 스킬 모음의 원본인 35_agent-skill 저장소에서 이번 이관 작업을 완료한 후에는 검증한 변경을 **yunli에 push → 사용자 검증 → main 반영·push**합니다. 다른 저장소를 yunli로 강제 전환하거나 검토 요청을 commit/push로 확대하지 않습니다. 개인 홈·config·키·release·서비스 적용은 별도 요청 범위입니다.

### 단독 사용과 참조

폴더 전체가 사용 단위입니다. 이 폴더 안의 필수 참조·도구만 사용하며 중앙 catalog·installer·30/31 저장소나 다른 skill의 별도 설치를 요구하지 않습니다. `skill://`는 아래 동봉 대응으로 해석하고 Kiro URI/hook/memory API를 호출하지 않습니다. 개인 경로·계정·config 원문·자격증명·세션·raw 비공개 증거를 공개 자료에 복사하지 않습니다.

### Windows에서의 점진적 변경

Change/Plan/Apply/Verify/Commit/Next slice의 목적과 최소 변경·단순 작업 예외를 유지합니다. 로컬 코드 수정·계획만 요청한 경우 Apply를 실제 운영 변경으로 실행하지 않습니다. Windows에서 설치된 Terraform/AWS 도구와 WSL/원격 Linux의 Ansible·서비스 실행은 서로 다른 대상입니다.

- PowerShell에서는 실제 Terraform 실행 파일에 명시한 프로젝트/backend 인수를 전달합니다. plan과 saved plan은 비공개 대상에 보존하며 대상·예상 변경·현재 승인 범위를 확인한 뒤에만 적용합니다. plan 확인 자체가 apply 승인인 것은 아닙니다.
- Ansible controller는 네이티브 Windows 프로세스로 가정하지 않습니다. 현재 제공된 Linux/WSL/container/controller 중 사용자 범위에 포함된 실행 환경을 확인하고 실제 inventory·SSH/WinRM·become/runas·대상 OS를 구분합니다. 이를 위해 WSL·controller·키·권한을 자동 설치/변경하지 않습니다.
- 각 slice의 문법·영향·실제 서비스·모니터링을 해당 도구에서 확인합니다. 단순 코드 검토의 완료 조건에 remote apply·health·CloudWatch를 강제하지 않으며 적용되지 않는 항목의 이유를 기록합니다.

### 의존성과 복구의 활성 기준

- **R04 대체:** 원문의 Risk-First “RDS 엔진 업그레이드 → 성공 → 앱 호환성 변경” 순서는 호환성이 준비되지 않은 대상의 적용 순서로 실행하지 않습니다. 위험도 우선은 의존성과 현행 앱 호환성이 충족된 변경 사이의 우선순위입니다. 기존/새 엔진에 대한 앱·driver·데이터·연결 호환성을 검증하고 필요한 앱 준비를 엔진 적용의 선행 조건으로 둡니다. 위험한 변경을 먼저 조사/격리 검증하는 것과 운영 적용은 구분합니다.
- 매 slice 뒤 시스템 정상 유지와 복구 가능성을 확인합니다. 변경 전 코드로 돌아가는 것만으로 데이터·엔진·리소스가 복원되는 것은 아니므로 실제 rollback plan·데이터 영향·복원 가능성을 기록합니다. state를 과거로 덮어 리소스를 rollback하지 않습니다.
- state backup 명령은 비공개 backend 자료의 보존 예시입니다. 승인된 대상·출력 위치를 확인하며 state mv/import/target는 현재 정당한 목적과 도구 계약이 있는 경우만 사용합니다. `-target` 후에는 전체 plan을 확인하되 실제 전체 apply를 추가 승인 없이 실행하지 않습니다.
- 실패 시 필요한 debugging 참조만 읽고 같은 순환 참조를 재독하지 않습니다. commit/push는 실제 저장소 규약·게시 범위로 처리하며 각 slice의 운영 적용과 코드 게시 완료를 구분합니다.

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://debugging-and-recovery` → [debugging-and-recovery](../../SKILL.md).

원문 비교 자료: [Kiro 원문](../originals/incremental-change.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## Overview

인프라 변경을 작은 단위로 나누어 적용·검증·커밋하는 워크플로우입니다.
한 번에 대규모 변경을 적용하면 롤백이 어렵고 장애 원인 파악이 불가능합니다.
각 단계마다 시스템이 정상 상태를 유지해야 합니다.

## When to Use

- 여러 리소스를 동시에 변경하는 Terraform 작업
- 다수 호스트에 영향을 주는 Ansible playbook
- 환경 간 마이그레이션 (dev → stg → prd)
- 네트워크 구조 변경 (VPC, Subnet, SG)
- 데이터베이스 스키마 변경이 포함된 배포

**적용하지 않는 경우:** 단일 리소스 태그 변경, 단일 파라미터 수정 등 범위가 명확한 최소 변경.

## The Increment Cycle

```
┌──────────────────────────────────────────┐
│                                          │
│ Change ──→ Plan ──→ Apply ──→ Verify ──┐ │
│     ^                                  │ │
│     └────── Commit <───────────────────┘ │
│               │                          │
│               v                          │
│           Next slice                     │
│                                          │
└──────────────────────────────────────────┘
```

각 단계:

1. **Change** — 최소 단위의 IaC 코드 수정
2. **Plan** — `terraform plan` 또는 `ansible --check`로 영향 범위 확인
3. **Apply** — 변경 적용
4. **Verify** — 리소스 상태, 서비스 정상 동작 확인
5. **Commit** — 변경 사항 커밋 (롤백 포인트)
6. **Next slice** — 다음 단위로 이동

## Slicing Strategies

### Dependency-First (기본)

의존성 순서대로 적용:

```
Slice 1: VPC, Subnet 생성
    → terraform apply → 네트워크 리소스 확인

Slice 2: Security Group 생성
    → terraform apply → SG 규칙 확인

Slice 3: EC2/ECS 리소스 생성
    → terraform apply → 인스턴스 상태 확인

Slice 4: ALB + Target Group 연결
    → terraform apply → health check 통과 확인
```

### Risk-First

가장 위험한 변경을 먼저 적용:

```
Slice 1: RDS 엔진 업그레이드 (가장 위험, 롤백 어려움)
    → 성공 확인 후 다음 진행

Slice 2: 애플리케이션 호환성 변경
Slice 3: 모니터링 업데이트
```

### Environment-First

환경 순서대로 동일 변경 적용:

```
Slice 1: dev 환경 적용 → 검증
Slice 2: stg 환경 적용 → 검증 + 부하 테스트
Slice 3: prd 환경 적용 → 검증 + 모니터링 확인
```

## Implementation Rules

### Rule 1: Plan Before Apply

모든 apply 전에 plan을 확인합니다.

```bash
terraform plan -out=tfplan
# 변경 내용 확인 후
terraform apply tfplan
```

### Rule 2: One Logical Change Per Apply

하나의 apply에 하나의 논리적 변경만 포함합니다.

```
나쁨: SG 변경 + RDS 파라미터 변경 + EC2 타입 변경을 한 번에 apply
좋음: 각각 별도 apply → 문제 발생 시 어떤 변경이 원인인지 즉시 파악
```

### Rule 3: Verify After Every Apply

적용 후 반드시 검증합니다.

```bash
# 리소스 상태 확인
aws ec2 describe-instances --instance-ids <id> --query 'Reservations[].Instances[].State'

# 서비스 health check
curl -f http://endpoint/health

# Terraform state 정합성
terraform plan  # "No changes" 확인
```

### Rule 4: Rollback Plan Required

각 단계마다 롤백 방법을 명시합니다.

```
변경: SG에 인바운드 규칙 추가
롤백: terraform apply 이전 커밋의 코드로 재적용
검증: 서비스 접근 정상 확인
```

### Rule 5: No Manual Console Changes

IaC로 관리되는 리소스는 콘솔에서 수동 변경하지 않습니다.
긴급 상황에서 수동 변경 시, 즉시 IaC에 반영합니다.

## Terraform Specific

### State 안전 규칙

```bash
# state 백업 후 작업 (로컬)
terraform state pull > backup-$(date +%Y%m%d-%H%M%S).tfstate

# state 백업 (S3 원격 — versioning 활성화 확인)
aws s3api list-object-versions --bucket <tf-state-bucket> \
  --prefix <state-key> --max-items 3

# 리소스 이동 시
terraform state mv aws_instance.old aws_instance.new

# import 시
terraform import aws_instance.new i-1234567890abcdef0
```

### 대규모 변경 시 -target 활용

```bash
# 특정 리소스만 먼저 적용
terraform apply -target=aws_vpc.main
terraform apply -target=aws_subnet.private
terraform apply  # 나머지 전체
```

🟡 `-target`은 임시 수단입니다. 최종적으로 전체 `terraform apply`가 "No changes"여야 합니다.

## Ansible Specific

### 점진적 적용

```bash
# dry-run 먼저
ansible-playbook site.yml --check --diff

# 호스트 제한
ansible-playbook site.yml --limit "web-01"

# 확인 후 전체 적용
ansible-playbook site.yml
```

### 태그 활용

```bash
# 특정 역할만 적용
ansible-playbook site.yml --tags "nginx"

# 위험한 태그 제외
ansible-playbook site.yml --skip-tags "destructive"
```

## Common Rationalizations

| Rationalization                        | Reality                                                             |
|----------------------------------------|---------------------------------------------------------------------|
| "한 번에 apply 하면 빠릅니다"          | 장애 시 어떤 변경이 원인인지 모릅니다. 분리합니다.                  |
| "dev에서 됐으니 prd도 됩니다"          | 환경마다 다릅니다. 각 환경에서 검증합니다.                          |
| "plan 봤으니 apply 해도 됩니다"        | plan과 실제 apply 결과가 다를 수 있습니다. apply 후 검증합니다.     |
| "작은 변경이라 롤백 계획 불필요합니다" | 작은 변경도 연쇄 장애를 일으킬 수 있습니다. 롤백 계획은 필수입니다. |
| "콘솔에서 빨리 고치겠습니다"           | drift가 발생합니다. IaC로 수정합니다.                               |

## Red Flags

- `terraform apply` 전에 `terraform plan` 미확인
- 여러 논리적 변경을 한 번에 apply
- apply 후 검증 없이 다음 작업 진행
- 롤백 계획 없이 프로덕션 변경
- 콘솔 수동 변경 후 IaC 미반영
- `-target` 사용 후 전체 plan 미확인
- apply 후 장애 발생 시 → `skill://debugging-and-recovery` 전환

## Verification

모든 변경 완료 후:

- [ ] 각 단계별 개별 검증 완료
- [ ] `terraform plan` → "No changes"
- [ ] 서비스 health check 통과
- [ ] 모니터링 정상 (알림 없음)
- [ ] 모든 변경 사항 커밋 완료
- [ ] 롤백 계획 문서화
