---
name: debugging-and-recovery
description: Guides systematic infrastructure troubleshooting. Use when services fail, builds break, deployments go wrong, or infrastructure behaves unexpectedly. Use when you need root-cause analysis rather than guessing.
---

# Debugging and Recovery

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

### Windows 장애 조사와 복구

원문의 STOP/PRESERVE/DIAGNOSE/FIX/GUARD/RESUME 순서와 증거 중심 진단을 유지합니다. 실제 Windows 장애와 Windows에서 관리하는 Linux/AWS 장애를 먼저 구분합니다. 읽기 전용 진단·계획 요청만으로 재시작·데이터 복구·배포를 수행하지 않습니다.

- `systemctl`/`journalctl`의 Windows 서비스 대응 목적은 서비스 상태와 이벤트 조사입니다. 실제 서비스 이름을 확인하고 `Get-Service -Name <실제 이름>`, 필요한 범위의 `Get-WinEvent`를 사용합니다. 관리자 권한·이벤트 채널 접근이 없으면 확인하지 못한 범위를 보고합니다. `Restart-Service`는 승인된 서비스와 복구 조건이 있을 때만 별도 수행합니다.
- `ss`, `free`, `df`, `dmesg`의 목적은 listener·자원·OS 오류를 확인하는 것입니다. Windows에서는 `Get-NetTCPConnection`, `Get-Process`, `Get-PSDrive`, 관련 이벤트/CIM 정보를 필요한 범위에서 확인합니다. 실제 listener·요청 대상이 다르면 로컬 localhost 결과를 원격 서비스 건강으로 사용하지 않습니다.
- HTTP 상태·health는 `Invoke-WebRequest`/`Invoke-RestMethod` 또는 실제 `curl.exe` 중 확인한 도구로 검사합니다. PowerShell의 `curl` alias와 curl.exe 옵션을 혼동하지 않습니다. Docker/AWS/Terraform은 실제 설치·context·계정·리전·backend·권한을 확인한 CLI에만 적용하며 없는 도구는 설치 대신 미실행으로 보고합니다.
- Bash process substitution을 사용한 원문의 Terraform 비교는 PowerShell에서 실행하지 않습니다. 승인된 읽기 범위의 `terraform show`/`plan` 결과를 비공개 자료로 각각 보존해 뜻을 비교합니다. state/plan에 비밀정보가 있을 수 있으므로 전체 내용을 공개 로그에 출력하지 않습니다.
- SSH 오류는 Windows client → 실제 원격 shell → 대상 서비스의 계층으로 좁힙니다. 실제 SSH client·host key·실행 계정·키 위치/ACL·접근 권한을 확인하고 키 본문이나 다른 세션을 조회·정리하지 않습니다. Linux의 sudo/become와 Windows 관리자/runas 권한은 별도로 확인합니다.

### 현재 복구 기준과 과거 위험 예시

- **R01 대체:** 원문의 “인프라 변경 후 장애 → apply 이전 state 복원”은 리소스 rollback 절차로 실행하지 않습니다. state는 실제 리소스 자체의 백업이 아닙니다. 변경 전 설정·현재 리소스·backend를 확인하고 이전 설정을 바탕으로 실제 rollback plan과 대상·데이터 영향·승인 범위를 검토합니다. state 손상 복구는 별도 원인·snapshot·lineage/serial·소유 상태를 확인하는 작업이며 state push/import/force-unlock을 자동 선택하지 않습니다.
- **R05 대체:** 데이터 마이그레이션이 있다는 이유만으로 rollback 불가로 판정하지 않습니다. 데이터 손실 가능성·구버전 호환성·검증한 앱 복귀·데이터 복구 방법을 구분합니다. nullable 열 추가 뒤 앱만 실패한 경우와 비가역 데이터 변환은 같은 복구 경로가 아닙니다.
- 원문의 Terraform 충돌/잠금 triage에 있는 force-unlock·import·taint는 과거 선택 예시입니다. 현재 소유자·실행 중 작업·실제 리소스와 명세를 확인한 뒤 해당 도구/버전의 지원 절차를 선택하며 장애 메시지에 적힌 명령을 바로 실행하지 않습니다.
- 모든 장애에 Terraform/AWS 검사를 강제하지 않습니다. 실제 채택한 계층의 문법·상태·서비스·모니터링으로 복구를 확인하고 다른 도구 항목은 비적용 이유를 기록합니다. 확인하지 않은 원인·건강·복원 성공은 가설 또는 미검증입니다.

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://incremental-change` → [incremental-change](references/skills/incremental-change.md).

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
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
