---
name: shipping-checklist
description: Pre-deployment checklist for infrastructure changes. Use when deploying to production, launching new services, or performing staged rollouts.
---

# Shipping Checklist

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 원문의 배포 준비·검증·복구 체크리스트를 배포 검토 요청에 적용합니다. 체크리스트 작성/준비 완료가 실제 배포 승인인 것은 아닙니다. 승인된 대상·환경·게시 범위만 적용하며 실제 건강 상태·모니터링·운영 검사는 실행 증거가 있을 때만 통과로 기록합니다.

로컬 워크플로 대응(필요한 항목만 읽음):

- `skill://incremental-change` → [incremental-change](references/skills/incremental-change.md).

- 원문 코드 준비의 `code-review` 항목은 필수 리뷰 역할입니다. 형제 설치를 요구하지 않고 동봉 [code-review](references/skills/code-review.md)의 전체 체크리스트를 적용하며, 실제 리뷰 증거가 없으면 완료 표시하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## Overview

인프라 변경을 프로덕션에 배포하기 전 수행하는 체크리스트입니다.
배포는 코드 작성보다 위험하므로, 구조화된 검증 없이 진행하지 않습니다.

## When to Use

- terraform apply to prd
- 새 서비스 런칭
- 인프라 마이그레이션 완료 단계
- feature flag 활성화
- DNS 변경, 인증서 교체

**적용하지 않는 경우:** dev/stg 환경 변경, 태그/설명 수정.

## Pre-Deploy Checklist

### 1. 코드 준비

- [ ] 모든 변경 사항 커밋 완료
- [ ] code-review 스킬 적용 완료
- [ ] terraform plan → 예상 변경만 표시
- [ ] 불필요한 리소스 삭제/변경 없음 확인

### 2. 보안 검증

- [ ] IAM 최소 권한 확인
- [ ] SG 규칙 검토 (0.0.0.0/0 없음)
- [ ] 시크릿 하드코딩 없음
- [ ] 암호화 설정 확인 (at rest + in transit)

### 3. 롤백 계획

- [ ] 롤백 방법 문서화
- [ ] 롤백 소요 시간 추정
- [ ] 롤백 트리거 조건 정의
- [ ] state 백업 완료

```bash
# Terraform state 백업
terraform state pull > backup-$(date +%Y%m%d-%H%M%S).tfstate
```

### 4. 모니터링 준비

- [ ] CloudWatch Alarm 설정 확인
- [ ] 로그 수집 경로 확인
- [ ] 알림 채널 동작 확인 (Slack/Email)
- [ ] 대시보드 준비

### 5. 배포 실행

- [ ] 유지보수 윈도우 확인 (필요 시)
- [ ] 관련 팀 사전 공지 (필요 시)
- [ ] 단계별 적용 (`skill://incremental-change`)
- [ ] 각 단계 후 health check

### 6. Post-Deploy 검증

```bash
# 서비스 health check
curl -f http://endpoint/health

# 리소스 상태
aws ec2 describe-instance-status --instance-ids <id>
aws ecs describe-services --cluster <cluster> --services <svc>

# Terraform 정합성
terraform plan  # "No changes"

# 모니터링 정상
# CloudWatch 대시보드 확인, 알림 없음
```

## Staged Rollout

대규모 변경 시 단계별 배포:

```
Phase 1: Canary (1개 인스턴스/AZ)
    → 30분 관찰 → 이상 없으면 진행

Phase 2: 50% 배포
    → 1시간 관찰 → 이상 없으면 진행

Phase 3: 100% 배포
    → 모니터링 안정화 확인
```

## Rollback Decision

| 조건                      | 조치                    |
|---------------------------|-------------------------|
| 배포 후 5분 이내 장애     | 즉시 롤백               |
| 메트릭 이상 (에러율 증가) | 즉시 롤백               |
| 부분 장애                 | feature flag OFF → 조사 |
| 데이터 마이그레이션 포함  | forward fix (롤백 불가) |

## Common Rationalizations

| Rationalization                      | Reality                                                      |
|--------------------------------------|--------------------------------------------------------------|
| "dev에서 됐으니 바로 prd 적용합니다" | 환경 차이가 있습니다. 체크리스트를 수행합니다.               |
| "급해서 롤백 계획은 나중에 세웁니다" | 롤백 계획 없이 배포하면 장애 시 복구 시간이 배로 늘어납니다. |
| "모니터링은 배포 후 설정합니다"      | 배포 시점에 모니터링이 없으면 장애를 감지할 수 없습니다.     |

## Red Flags

- 체크리스트 미수행 상태에서 prd apply
- 롤백 계획 없음
- state 백업 없음
- 모니터링/알림 미설정
- 단계별 검증 없이 전체 한 번에 배포

## Verification

배포 완료 후:

- [ ] 서비스 정상 동작 (health check 통과)
- [ ] terraform plan → "No changes"
- [ ] 모니터링 정상 (알림 없음)
- [ ] 롤백 계획 유효성 확인
- [ ] 배포 완료 기록 (커밋, 시간, 담당자)
