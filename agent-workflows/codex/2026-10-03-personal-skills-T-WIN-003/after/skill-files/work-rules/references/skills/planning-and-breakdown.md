---
name: planning-and-breakdown
description: Breaks infrastructure work into ordered tasks. Use when you have requirements and need to decompose into implementable steps. Use when an infra change feels too large, when you need to estimate blast radius, or when changes span multiple environments.
---

# Planning and Breakdown

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

### Windows 계획과 실행 구분

원문의 읽기 전용 조사·의존성·수직 분할·태스크 양식·checkpoint·단순 작업 예외를 유지합니다. 사용자가 지정한 출력·기존 PLAN/TODO 위치와 개인 기본값의 관계를 먼저 확인합니다. 계획·명세·리뷰 완료를 운영 apply나 commit/push의 권한으로 처리하지 않습니다.

- Windows의 실제 파일·Git 변경·서비스/프로세스·제공 로그를 읽기 전용으로 조사합니다. Terraform state/AWS 콘솔은 대상 기술·접근 범위가 실제로 주어진 경우의 자료이며 모든 계획의 필수 도구가 아닙니다. 접근하지 못한 계정·리전·CIDR·규모·권한은 미결 사항으로 둡니다.
- 각 태스크에는 실행 주체와 플랫폼을 기록합니다: Windows PowerShell/Python 로컬 작업, Windows 네이티브 CLI, WSL/controller, 원격 Linux/Windows 대상 중 실제 해당 계층을 구분합니다. 도구 설치·계정·키/ACL·원격 권한 변경은 별도 의존 작업이며 자동 수행하지 않습니다.
- 의존성 우선으로 정상 상태가 유지되는 단위를 정합니다. 수직/위험/환경 분할을 상황에 맞게 조합하되 위험도 때문에 앱 호환성 같은 선행 조건을 뒤로 밀지 않습니다. checkpoint의 실제 검사·미실행과 rollback 범위를 명시합니다.
- 원문의 terraform apply·health·monitoring 완료 조건은 실제 Terraform 적용 태스크의 예시입니다. 계획 작성 태스크에는 명세·의존성·범위·검증 방법·미결 조건을 확인하며 실제 배포 성공으로 완료 표시하지 않습니다. 비적용 도구 항목은 이유를 기록합니다.
- 구현이 요청되면 해당 Windows incremental-change 참조를 적용합니다. 기록 번호·batch 형식은 사용자/저장소가 정한 체계를 우선하며 3개 태스크마다 새 문서·승인·agent를 자동 생성하지 않습니다.

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://incremental-change` → [incremental-change](../skills/incremental-change.md).

원문 비교 자료: [Kiro 원문](../originals/planning-and-breakdown.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.

### 호출·원본·기록

- 설치되어 현재 세션에 발견된 skill은 `$planning-and-breakdown 이 작업의 의존성과 완료 기준을 나눠 계획해줘`처럼 명시해 호출합니다. 미설치 상태에서는 사용자가 지정한 실제 `SKILL.md` 경로를 읽어 이 Windows 기준을 적용합니다. 경로 조회나 계획 작성 자체는 설치·구현·게시 승인이 아닙니다.
- `_reference` 원본은 비교·출처 확인 자료이며 지원되는 skill 발견 위치나 설치 완료 표시가 아닙니다. 35 저장소 안에 이미 있는 배포 원본을 다시 clone하지 않고 지정된 원본 폴더를 사용합니다.
- 실제 작업 repo의 기존 관리 기록에 목표·범위·의존성·완료 기준·다음 행동을 남깁니다. 사용자가 지정한 기존 관리·업데이트 기록 폴더가 있으면 재사용하고, 다른 repo에 35의 `agent-workflows` 경로를 강제하지 않습니다. 계획만 요청된 경우 계획 결과와 미실행 구현·commit·push를 구분합니다.
- 설치된 skill 교체는 이전 전체 폴더의 사본과 해시를 먼저 보존한 뒤 기존에 승인된 교체 범위에 따라 진행합니다. 동봉 참조·도구도 전체 폴더 단위로 함께 옮겨 서로 다른 버전을 섞지 않습니다.

<!-- CODEX-COMPAT-END -->


## Overview

인프라 작업을 작고 검증 가능한 단위로 분해하는 워크플로우입니다.
각 태스크는 명확한 완료 조건과 검증 방법을 가지며, 의존성 순서대로 정렬됩니다.

## When to Use

- 요구사항이 있고 구현 단위로 분해가 필요할 때
- 작업이 너무 크거나 모호하여 시작하기 어려울 때
- 여러 환경(dev/stg/prd)에 걸친 변경
- 블래스트 레디어스 파악이 필요할 때
- 작업 순서가 명확하지 않을 때

**적용하지 않는 경우:** 단일 리소스 변경, 범위가 명확한 단순 작업.

## The Planning Process

### Step 1: Read-Only Mode

코드를 작성하기 전에 읽기 전용으로 조사합니다.

- 현재 인프라 상태 확인 (terraform state, AWS 콘솔)
- 기존 모듈/패턴 파악
- 의존성 관계 매핑
- 리스크와 미지수 식별

### Step 2: Dependency Graph

의존성을 매핑합니다.

```
VPC / Network
    │
    ├── Subnet (Public / Private)
    │       │
    │       ├── Security Group
    │       │       │
    │       │       ├── EC2 / ECS
    │       │       │       │
    │       │       │       └── ALB Target Group
    │       │       │               │
    │       │       │               └── ALB Listener
    │       │       │
    │       │       └── RDS
    │       │
    │       └── NAT Gateway
    │
    └── Route Table
```

### Step 3: Vertical Slicing

수평(계층별)이 아닌 수직(기능별)으로 분할합니다.

```
나쁨 (수평):
  Task 1: 모든 SG 생성
  Task 2: 모든 EC2 생성
  Task 3: 모든 ALB 설정

좋음 (수직):
  Task 1: Web tier 전체 (SG + EC2 + ALB + health check)
  Task 2: App tier 전체 (SG + ECS + Service Discovery)
  Task 3: DB tier 전체 (SG + RDS + 백업 설정)
```

### Step 4: Write Tasks

각 태스크 구조:

```markdown
## Task [N]: [제목]

**설명:** 이 태스크가 완료하는 것.

**완료 조건:**
- [ ] 리소스 생성/변경 완료
- [ ] terraform plan → 예상 변경만 표시
- [ ] 서비스 정상 동작 확인

**검증:**
- [ ] terraform apply 성공
- [ ] health check 통과
- [ ] 모니터링 정상

**의존성:** Task N (또는 없음)

**영향 범위:**
- 리소스: aws_instance, aws_security_group
- 환경: dev
- 블래스트 레디어스: 해당 서비스만

**롤백:** terraform apply 이전 커밋 코드

**예상 소요:** [10분 / 30분 / 1시간]
```

### Step 5: Order and Checkpoint

정렬 기준:

1. 의존성 순서 (기반부터)
2. 각 태스크 후 시스템 정상 상태 유지
3. 2~3개 태스크마다 체크포인트
4. 고위험 태스크를 앞에 배치 (fail fast)

```markdown
## Checkpoint: Task 1-3 완료 후
- [ ] terraform plan → "No changes"
- [ ] 모든 서비스 health check 통과
- [ ] 모니터링 알림 없음
- [ ] 다음 단계 진행 전 확인
```

## Task Sizing

| 크기 | 리소스 수 | 범위          | 예시                    |
|------|-----------|---------------|-------------------------|
| S    | 1-3       | 단일 서비스   | SG 규칙 추가            |
| M    | 4-8       | 한 tier       | Web tier 전체 구성      |
| L    | 9-15      | 여러 tier     | VPC + 서브넷 + NAT 전체 |
| XL   | 15+       | **분할 필요** | —                       |

L 이상은 반드시 더 작은 단위로 분할합니다.

## Plan Template

```markdown
# 인프라 변경 계획: [제목]

## 개요
[무엇을 왜 변경하는지 1문단]

## 현재 상태
[현재 인프라 구성 요약]

## 목표 상태
[변경 후 인프라 구성]

## 블래스트 레디어스
- 영향 서비스: [목록]
- 영향 환경: [dev/stg/prd]
- 다운타임 예상: [있음/없음, 시간]

## Task List

### Phase 1: 기반
- [ ] Task 1: ...
- [ ] Task 2: ...

### Checkpoint: 기반 완료
- [ ] terraform plan → No changes
- [ ] 서비스 정상

### Phase 2: 서비스
- [ ] Task 3: ...
- [ ] Task 4: ...

### Checkpoint: 전체 완료
- [ ] 모든 검증 통과

## 리스크 및 대응

| 리스크               | 영향 | 대응                   |
|----------------------|------|------------------------|
| RDS 다운타임         | High | 유지보수 윈도우 예약   |
| SG 변경 시 접근 차단 | Med  | 기존 규칙 유지 후 추가 |

## 롤백 계획
[단계별 롤백 방법]

## 미결 사항
[확인 필요한 항목]
```

## Common Rationalizations

| Rationalization                     | Reality                                       |
|-------------------------------------|-----------------------------------------------|
| "간단한 변경이라 계획 불필요합니다" | 간단해도 블래스트 레디어스 파악은 필요합니다. |
| "머릿속에 다 있습니다"              | 문서화된 계획은 롤백 시 필수입니다.           |
| "계획은 오버헤드입니다"             | 10분 계획이 수 시간 장애 복구를 방지합니다.   |
| "한 번에 다 하면 빠릅니다"          | 장애 시 원인 파악이 불가능합니다.             |

## Red Flags

- 계획 없이 terraform apply 실행
- 완료 조건 없는 태스크
- 검증 단계 누락
- 모든 태스크가 XL 크기
- 체크포인트 없이 연속 적용
- 롤백 계획 미수립

## Verification

구현 시작 전 확인:

- [ ] 모든 태스크에 완료 조건 있음
- [ ] 모든 태스크에 검증 방법 있음
- [ ] 의존성 순서 정렬 완료
- [ ] 블래스트 레디어스 파악 완료
- [ ] 체크포인트 배치 완료
- [ ] 롤백 계획 수립 완료

구현 시 `skill://incremental-change` 워크플로우를 적용합니다.
