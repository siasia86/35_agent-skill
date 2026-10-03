---
name: spec-driven-infra
description: Creates infrastructure specs before applying changes. Use when starting a new infra project, adding significant resources, or when requirements are unclear. Use when the change affects production or spans multiple services.
---

# Spec-Driven Infra

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

### Windows 명세 작성과 실행 플랫폼

원문의 SPECIFY/PLAN/TASKS/IMPLEMENT·양식·개인 규약·단순 변경 예외를 유지합니다. 요구사항·현재 상태·목표·영향·보안·검증·복구와 미결 사항을 명세에 포함하며 실제 구현/운영 적용과 분리합니다.

- Windows에서 읽기·명세·설계·검토를 수행할 수 있습니다. 도구·버전·계정·region·backend·대상 OS·실행 주체는 실제 자료로 확인하고 예시의 CIDR/AZ/버전/계정을 확정 설정으로 사용하지 않습니다.
- Windows PowerShell/Python 로컬 작업, 설치된 Windows Terraform/AWS CLI, Linux/WSL/container Ansible controller, 실제 SSH/WinRM 원격 대상을 구분해 명세합니다. Ansible을 네이티브 Windows controller로 가정하지 않으며 새로운 controller·WSL·서비스·키/권한을 자동 설치·변경하지 않습니다.
- Linux apt/dnf/systemd와 Windows 패키지/서비스·runas/ACL은 별도 역할입니다. Windows 대상을 관리할 때는 실제 사용한 Windows 지원 모듈·대상 버전·접속 방식·권한을 검토하고 Linux 모듈을 이름만 치환하지 않습니다.
- 비용·버전·권장 설정처럼 현재 확인이 필요한 자료는 공식 출처로 확인하고 미확인 수치를 명세의 사실로 쓰지 않습니다. 현재 저장소가 채택한 `_reference`/INDEX 구조만 갱신하고 다른 저장소를 준비하지 않습니다.

### 변경 전 상태를 보존하는 복구 계약

- **R03 대체:** 원문의 “패키지 rollback → state: absent”는 모든 패키지 복구에 적용하지 않습니다. 변경 전 미설치인 신규 설치만 제거 대상으로 판단하며 기존 설치의 업그레이드는 이전 버전/관련 구성/의존성으로 복구합니다. 설정만 변경한 경우에는 패키지를 제거하지 않고 검증한 설정 복원 절차를 적용합니다.
- Windows 패키지 도구·서비스·ACL·인증서의 변경 전 상태와 실제 복구 가능성도 각각 기록합니다. 제거·다운그레이드·서비스 재시작은 현재 승인 범위에서 선택하고 없는 이전 버전/백업을 있다고 가정하지 않습니다.
- 데이터 마이그레이션·엔진 업그레이드의 호환성과 가역성을 먼저 검증합니다. 상태 기록을 이전 값으로 바꾸는 것만으로 리소스·데이터가 복원되는 것은 아니며 위험도 때문에 의존성을 뒤로 미루지 않습니다.
- read-only 명세 리뷰의 gate는 명세·요구·계약의 검토입니다. plan/apply·health·실환경 보안 감사는 실제 구현 단계의 별도 검사이고 미실행을 명세 완료의 증거로 사용하지 않습니다. 구현이 요청되면 동봉 planning/incremental 참조로 이어갑니다.

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://incremental-change` → [incremental-change](references/skills/incremental-change.md).
- `skill://planning-and-breakdown` → [planning-and-breakdown](references/skills/planning-and-breakdown.md).

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## Overview

인프라 변경 전에 구조화된 스펙을 작성하는 워크플로우입니다.
스펙은 무엇을, 왜, 어떻게 변경하는지의 합의 문서이며, 변경의 블래스트 레디어스와 롤백 계획을 포함합니다.

## When to Use

- 새로운 인프라 구성 (VPC, 클러스터, 서비스)
- 프로덕션 환경 변경
- 여러 서비스에 영향을 주는 변경
- 요구사항이 모호하거나 불완전할 때
- 아키텍처 결정이 필요할 때

**적용하지 않는 경우:** 태그 변경, 단일 파라미터 수정, 명확한 버그 수정.

## Gated Workflow

```
SPECIFY ──→ PLAN ──→ TASKS ──→ IMPLEMENT
   │          │        │          │
   v          v        v          v
 Review     Review   Review    Verify
```

각 단계를 검증 없이 넘어가지 않습니다.

## Phase 1: Specify

### Assumptions 먼저 명시

```
ASSUMPTIONS:
1. VPC CIDR은 10.0.0.0/16 사용 (기존 네트워크와 충돌 없음)
2. Multi-AZ 구성 (ap-northeast-2a, 2c)
3. NAT Gateway는 AZ당 1개
4. Terraform backend는 기존 S3 + DynamoDB 사용
→ 확인 필요한 항목이 있으면 지적해 주세요.
```

### Spec Template

```markdown
# Infra Spec: [제목]

## 목적
[무엇을 왜 구축/변경하는지. 비즈니스 요구사항.]

## 현재 상태
[현재 인프라 구성. 다이어그램 포함 권장.]

## 목표 상태
[변경 후 인프라 구성. 다이어그램 포함.]

## 기술 스택
- IaC: Terraform 1.x / Ansible 2.x
- Provider: AWS (ap-northeast-2)
- 모듈: [사용할 모듈 목록]

## 리소스 목록

| 리소스           | 이름 규칙               | 수량 |
|------------------|-------------------------|------|
| VPC              | prd-vpc-main            | 1    |
| Subnet (Private) | prd-subnet-private-{az} | 2    |
| Security Group   | prd-sg-{service}        | N    |

## 네트워크 설계

| CIDR         | 용도           | AZ |
|--------------|----------------|----|
| 10.0.0.0/16  | VPC            | -  |
| 10.0.1.0/24  | Public Subnet  | 2a |
| 10.0.2.0/24  | Public Subnet  | 2c |
| 10.0.11.0/24 | Private Subnet | 2a |
| 10.0.12.0/24 | Private Subnet | 2c |

## 보안 요구사항
- [ ] 최소 권한 원칙 (IAM)
- [ ] 암호화 (at rest + in transit)
- [ ] 네트워크 격리 (Private Subnet)
- [ ] 감사 로그 (CloudTrail, VPC Flow Logs)

## 모니터링 요구사항
- [ ] CloudWatch Alarm: CPU, Memory, Disk
- [ ] 로그 수집: CloudWatch Logs / 외부 시스템
- [ ] 알림 채널: Slack / Email

## 블래스트 레디어스
- 영향 서비스: [목록]
- 다운타임: [예상 시간]
- 영향 사용자: [범위]

## 비용 추정
- 월간 예상 비용: [AWS Pricing Calculator 또는 infracost 결과]
- 기존 대비 증감: [+/- 금액]
- 비용 최적화: [Reserved/Spot/Savings Plan 적용 여부]

## Boundaries
- Always: IaC로만 변경, plan 확인 후 apply, 롤백 계획 수립
- Ask first: 프로덕션 apply, 데이터 마이그레이션, SG 삭제
- Never: 콘솔 수동 변경, 시크릿 하드코딩, 롤백 계획 없이 적용

## 성공 기준
- [ ] terraform plan → 예상 리소스만 생성
- [ ] 서비스 health check 통과
- [ ] 모니터링 알림 정상 동작
- [ ] 보안 감사 통과

## 미결 사항
- [확인 필요한 항목]
```

## Ansible Spec Template

Terraform/AWS가 아닌 Ansible role/playbook 설계 시 사용합니다.

```markdown
# Ansible Spec: [제목]

## 목적
[무엇을 왜 자동화하는지. 수동 작업 대비 이점.]

## 대상 환경

| 항목         | 내용                                    |
|--------------|-----------------------------------------|
| 대상 OS      | Ubuntu 22/24, Rocky 9, AmazonLinux 2023 |
| 연결 방식    | SSH / docker / winrm                    |
| 권한 상승    | become: true (sudo/runas)               |
| Ansible 버전 | 2.15+                                   |

## Inventory 구조

    [group_name]
    host1 ansible_host=10.x.x.x

    [group_name:vars]
    ansible_user=ansible
    ansible_ssh_private_key_file=~/.ssh/id_ed25519

## Role / Playbook 구조

    playbooks/
    ├── site.yml              # 전체 진입점
    ├── vars/
    │   ├── common.yml        # 평문 변수
    │   └── secrets.yml       # vault 암호화
    └── roles/
        └── role_name/
            ├── tasks/main.yml
            ├── handlers/main.yml
            ├── defaults/main.yml
            └── templates/

## 멱등성 보장 계획

| Task        | 멱등성 방법                      |
|-------------|----------------------------------|
| 패키지 설치 | `state: present`                 |
| 파일 생성   | `creates:` 또는 `stat` 선행 체크 |
| 서비스 시작 | `state: started`                 |
| 설정 변경   | `lineinfile` / `template`        |

## OS별 분기 계획

| 작업     | Debian | RedHat      |
|----------|--------|-------------|
| 패키지   | `apt`  | `dnf`/`yum` |
| 서비스명 | `ssh`  | `sshd`      |
| 그룹     | `sudo` | `wheel`     |

## 시크릿 관리
- vault 암호화 대상: [목록]
- vault password 관리 방법: [파일/환경변수/CI Secret]

## 테스트 계획
- [ ] `--syntax-check` 통과
- [ ] `--check` dry-run 통과
- [ ] Molecule 테스트 (대상 OS별)
- [ ] 실제 환경 적용 후 재실행 → changed=0 확인

## 롤백 계획
- 설정 파일: `backup: true` 옵션으로 자동 백업
- 패키지: `state: absent`로 제거
- 전체 롤백: [방법]

## 성공 기준
- [ ] 전체 OS `failed=0`
- [ ] 재실행 시 `changed=0` (멱등성)
- [ ] `--check` 모드 호환
- [ ] vault 시크릿 평문 노출 없음
```

## Phase 2: Plan

스펙 확정 후 기술 구현 계획을 작성합니다.

- 모듈 구조 결정
- 의존성 그래프 작성
- 환경별 적용 순서 결정
- 리스크 식별 및 대응 방안

## Phase 3: Tasks

`skill://planning-and-breakdown` 스킬을 사용하여 태스크로 분해합니다.

## Phase 4: Implement

`skill://incremental-change` 스킬을 사용하여 점진적으로 적용합니다.

## Spec as Living Document

- 결정 변경 시 스펙 먼저 업데이트
- 범위 변경 시 스펙에 반영
- 스펙을 버전 관리에 포함
- PR에서 스펙 섹션 참조

## Common Rationalizations

| Rationalization                         | Reality                                                         |
|-----------------------------------------|-----------------------------------------------------------------|
| "간단한 변경이라 스펙 불필요합니다"     | 간단해도 블래스트 레디어스와 롤백 계획은 필요합니다.            |
| "코드 먼저 작성하고 문서화하겠습니다"   | 그건 문서화이지 스펙이 아닙니다. 스펙의 가치는 사전 합의입니다. |
| "요구사항이 바뀔 텐데 스펙을 왜 씁니까" | 바뀌면 스펙을 업데이트합니다. 없는 것보다 낫습니다.             |
| "시간이 없습니다"                       | 15분 스펙이 수 시간 장애 복구를 방지합니다.                     |

## Red Flags

- 스펙 없이 terraform 코드 작성 시작
- 블래스트 레디어스 미파악
- 롤백 계획 없음
- 보안 요구사항 누락
- 모니터링 계획 없음
- "당연히 알겠지" 가정으로 진행

## Verification

구현 시작 전 확인:

- [ ] 스펙 6개 핵심 영역 작성 완료
- [ ] 블래스트 레디어스 파악
- [ ] 롤백 계획 수립
- [ ] 보안 요구사항 명시
- [ ] 성공 기준 구체적이고 검증 가능
- [ ] Boundaries 정의 완료
- [ ] 스펙 파일 저장소에 커밋
