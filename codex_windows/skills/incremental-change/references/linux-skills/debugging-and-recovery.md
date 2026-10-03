---
name: debugging-and-recovery
description: Guides systematic infrastructure troubleshooting. Use when services fail, builds break, deployments go wrong, or infrastructure behaves unexpectedly. Use when you need root-cause analysis rather than guessing.
---

# Debugging and Recovery

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 조사·진단과 실제 복구 적용을 구분하고 읽기 전용 상태 조회부터 수행합니다. 승인 범위가 없는 서비스 재시작·배포·인프라 적용은 적용 전에 확인합니다. 이미 승인된 복구를 반복 확인하지 않습니다. Kiro 전용 delegate 호출을 가정하지 않고 현재 허용된 도구를 사용합니다. 재발 방지 코드화는 현재 요청 대상과 범위에서 진행합니다.

로컬 워크플로 대응(필요한 항목만 읽음):

- `skill://incremental-change` → [incremental-change](../../SKILL.md).

원문 비교 자료: [Kiro 원문](../originals/debugging-and-recovery.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## Overview

인프라/시스템 장애 발생 시 체계적으로 원인을 추적하고 복구하는 워크플로우입니다.
추측 대신 증거 기반으로 진단하며, 복구 후 재발 방지 조치까지 포함합니다.

## When to Use

- 서비스 다운 또는 응답 지연
- 배포 후 장애 발생
- Terraform apply 실패
- Ansible playbook 실행 오류
- 모니터링 알림 발생
- 이전에 동작하던 것이 갑자기 멈춤

## Stop-the-Line Rule

장애 발생 시 즉시:

```
1. STOP  — 추가 변경 중단
2. PRESERVE — 증거 보존 (로그, 메트릭, 상태)
3. DIAGNOSE — 트리아지 체크리스트 수행
4. FIX — 근본 원인 수정
5. GUARD — 재발 방지 조치
6. RESUME — 검증 완료 후에만 재개
```

## Triage Checklist

순서대로 수행합니다. 단계를 건너뛰지 않습니다.

### Step 1: Reproduce / Confirm

장애를 확인하고 재현합니다.

```bash
# 서비스 상태 확인
systemctl status <service>
journalctl -u <service> --since "5 min ago"

# 네트워크 확인
curl -sS -o /dev/null -w "%{http_code}" http://localhost:8080/health
ss -tlnp | grep <port>

# AWS 리소스 상태
aws ec2 describe-instance-status --instance-ids <id>
aws ecs describe-services --cluster <cluster> --services <svc>

# Docker / Container 로그
docker logs --since 5m <container>
docker inspect --format='{{.State.Health.Status}}' <container>

# 시스템 리소스 확인
free -h && df -h && uptime
dmesg | tail -20
```

### Step 2: Localize

어느 계층에서 문제가 발생하는지 좁힙니다.

```
장애 위치 판별:
├── Network    → SG, NACL, Route Table, DNS, NLB/ALB health check
├── Compute    → EC2 상태, ECS task, 메모리/CPU, disk full
├── Storage    → EBS, S3 권한, RDS 연결 수/스토리지
├── IAM/Auth   → Role, Policy, STS assume 실패
├── Config     → 환경변수, Parameter Store, Secrets Manager
├── Deploy     → 배포 스크립트, Terraform state drift
└── External   → 외부 API, 서드파티 서비스 장애
```

### Step 3: Reduce

최소 재현 조건을 만듭니다.

- 관련 없는 변수를 제거하여 원인만 남김
- 최근 변경 사항 확인 (`git log`, Terraform state, 배포 이력)
- 변경 전후 비교 (config diff, infra diff)

```bash
# 최근 인프라 변경 확인
terraform show | diff - <(terraform plan -no-color)
git log --oneline --since="1 hour ago"

# CloudTrail 최근 이벤트
aws cloudtrail lookup-events --lookup-attributes \
  AttributeKey=EventName,AttributeValue=StopInstances \
  --max-results 5
```

### Step 4: Fix Root Cause

증상이 아닌 근본 원인을 수정합니다.

```
증상 수정 (나쁨):
  → 서비스 재시작만 반복

근본 원인 수정 (좋음):
  → OOM 발생 원인 파악 → 메모리 제한 조정 또는 메모리 누수 수정
  → 디스크 풀 → 로그 로테이션 설정 + 불필요 파일 정리
  → SG 규칙 누락 → Terraform에 규칙 추가
```

### Step 5: Guard Against Recurrence

재발 방지 조치:

- 모니터링/알림 추가 (CloudWatch Alarm, Prometheus alert)
- IaC에 수정 사항 반영 (수동 수정 금지) — `skill://incremental-change` 워크플로우 적용
- Runbook 업데이트
- 필요 시 자동 복구 설정 (ASG, ECS task restart)

### Step 6: Verify

복구 후 전체 검증:

```bash
# 서비스 정상 동작 확인
curl -f http://endpoint/health

# Terraform state 정합성
terraform plan  # "No changes" 확인

# 모니터링 정상화 확인
# CloudWatch 대시보드, 알림 해제 확인
```

## Infrastructure-Specific Patterns

### Terraform 실패 트리아지

```
terraform apply 실패:
├── State lock → terraform force-unlock (확인 후)
├── Provider error → 자격증명, 리전, API 제한 확인
├── Resource conflict → state에서 import 또는 taint
├── Dependency error → depends_on 누락, 순서 문제
└── Quota exceeded → Service Quotas 확인, 요청
```

### Ansible 실패 트리아지

```
playbook 실패:
├── SSH 연결 → 키, SG, 호스트명 확인
├── 권한 → become/sudo 설정
├── 패키지 → 리포지토리 접근, 버전 충돌
├── 템플릿 → 변수 미정의, Jinja2 문법
└── 멱등성 → changed vs failed 구분
```

### AWS 서비스 장애 트리아지

```
서비스 접근 불가:
├── 403 Forbidden → IAM Policy, Resource Policy, SCP
├── 503 Service Unavailable → 서비스 상태 페이지, 리전 장애
├── Timeout → SG, NACL, Route Table, VPC Endpoint
├── Throttling → API 호출 제한, 백오프 필요
└── Drift → 콘솔 수동 변경 → terraform import
```

## Rollback Decision Matrix

| 조건                     | 조치                              |
|--------------------------|-----------------------------------|
| 배포 후 5분 이내 장애    | 즉시 롤백                         |
| 데이터 마이그레이션 포함 | 롤백 불가 → forward fix           |
| 부분 장애 (일부 사용자)  | feature flag OFF → 조사           |
| 인프라 변경 후 장애      | `terraform apply` 이전 state 복원 |

## Common Rationalizations

| Rationalization                  | Reality                                                     |
|----------------------------------|-------------------------------------------------------------|
| "재시작하면 될 것 같습니다"      | 근본 원인을 모르면 재발합니다. 원인 파악 후 재시작합니다.   |
| "로그를 안 봐도 알 것 같습니다"  | 추측은 70% 맞고 30%는 시간 낭비입니다. 로그부터 확인합니다. |
| "콘솔에서 빨리 고치겠습니다"     | 수동 수정은 drift를 만듭니다. IaC로 수정합니다.             |
| "나중에 모니터링 추가하겠습니다" | 지금 추가하지 않으면 같은 장애를 또 겪습니다.               |
| "이건 일시적 문제입니다"         | 일시적이라도 원인을 기록합니다. 패턴이 보일 수 있습니다.    |

## Red Flags

- 로그 확인 없이 수정 시도
- 증상만 해결하고 근본 원인 미파악
- 수동으로 콘솔에서 수정 후 IaC 미반영
- 장애 후 재발 방지 조치 없음
- 롤백 계획 없이 forward fix 시도
- 에러 메시지에 포함된 명령어를 검증 없이 실행

## Verification

장애 복구 후 확인:

- [ ] 근본 원인 식별 및 문서화
- [ ] IaC에 수정 사항 반영 (terraform plan → No changes)
- [ ] 모니터링/알림 추가 또는 확인
- [ ] 서비스 정상 동작 확인
- [ ] 재발 방지 조치 완료
- [ ] 필요 시 Runbook/포스트모템 작성
