---
name: shipping-checklist
description: Pre-deployment checklist for infrastructure changes. Use when deploying to production, launching new services, or performing staged rollouts.
---

# Shipping Checklist

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

### Windows 배포 준비·적용 범위

원문의 준비·보안·복구·모니터링·단계별 적용·검증을 실제 배포 검토 대상에 적용합니다. 배포 준비 체크 완료가 배포 승인인 것은 아닙니다. Windows에서 작성하는 계획/리뷰, Windows 실제 서비스 변경, Linux/클라우드의 실제 배포를 구분합니다.

- 실제 배포 기술·환경·사용자 범위에 해당하는 항목을 정합니다. Terraform/AWS를 쓰지 않는 DNS/인증서/feature flag 작업에 IAM/state/CloudWatch 검사를 강제하지 않습니다. 비적용은 사유를 남기며 실제 건강·모니터링·운영 검사를 미실행 상태로 통과 처리하지 않습니다.
- PowerShell/native CLI로 수행할 수 있는 사전 확인과 실제 controller/원격 대상에서 필요한 검사를 구분합니다. 서비스 이름·endpoint·계정·region·backend·정책·권한을 확인합니다. 팀 공지/알림은 실제 사용자 요청 또는 채택한 절차로 승인된 경우에만 전송합니다.
- state backup은 비공개 실제 backend 자료를 승인된 위치에 보존하는 조건부 작업입니다. PowerShell의 기본 `>` 인코딩으로 JSON/state bytes를 임의 변환하지 않습니다. 검증한 저장 방법과 출력 위치를 사용하며 backup을 resource rollback과 혼동하지 않습니다.
- 단계별 rollout은 실제 서비스와 시간·관찰 기준에 맞게 계획합니다. 예시의 30분/1시간 대기를 모든 작업에 강제하거나 자동 배포로 이어가지 않습니다. 각 단계의 건강·중단·복구 조건을 현재 승인 범위에서 확인합니다.

### 활성 보안·복구 기준

- **R06 대체:** “SG에 0.0.0.0/0 없음”을 모든 공개 서비스의 준비 완료 조건으로 사용하지 않습니다. 공개 HTTPS listener의 용도·포트·대상·정당화 근거를 검토하고 관리 포트/내부 backend의 불필요한 공개와 구분합니다. backend를 ALB SG로 제한하는 등 실제 아키텍처의 최소 권한을 평가합니다. 동봉 code-review의 “정당화 없는 공개 inbound” 기준과 맞춥니다.
- **R05 대체:** “데이터 마이그레이션 포함 → rollback 불가” 예시는 실행 판정으로 사용하지 않습니다. 데이터 손실·이전 버전 호환성·검증한 앱 복귀·데이터 복원·forward fix의 조건을 구분합니다. 실제 복구 계획·범위와 승인에 따라 선택하며 장애 직후 모든 대상에 일괄 rollback하지 않습니다.
- 코드는 동봉 code-review의 전체 필수 역할로 검토합니다. 실제 리뷰 근거가 없으면 완료 표시하지 않습니다. 배포 후 건강·plan·모니터링은 실행 증거가 있을 때만 통과이고 설치·운영 적용은 별도 결과입니다.

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://incremental-change` → [incremental-change](../skills/incremental-change.md).
- `skill://code-review` → [code-review](../skills/code-review.md).

원문 비교 자료: [Kiro 원문](../originals/shipping-checklist.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
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
