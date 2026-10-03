---
name: incremental-change
description: Delivers infrastructure changes incrementally. Use when making any IaC change that touches multiple resources, modules, or environments. Use when a Terraform/Ansible change feels too large to apply in one step.
---

# Incremental Change

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 현재 승인된 대상에서 작은 단위의 변경·검증·기록을 수행합니다. 다른 저장소나 운영 환경을 예시 경로만으로 수정하지 않습니다. 로컬 무해한 코드 수정은 운영 apply 절차로 확대하지 않습니다. 장애 전환은 필요한 debugging 참조만 읽고, 그 참조의 복귀 링크를 이유 없이 반복 추적하지 않습니다.

로컬 워크플로 대응(필요한 항목만 읽음):

- `skill://debugging-and-recovery` → [debugging-and-recovery](debugging-and-recovery.md).

원문 비교 자료: [Kiro 원문](../originals/incremental-change.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
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
