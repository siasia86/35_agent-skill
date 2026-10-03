---
name: using-skills
description: Maps incoming work to the right skill workflow. Use when starting a session, when deciding which skill applies, or when the task type is unclear.
---

# Using Skills

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

### Windows의 전체 19개 역할과 현재 작업 선택

이 skill 자체를 포함한 기존 19개 역할을 모두 유지합니다. 아래 동봉 대응에는 나머지 18개 지침이 있고 모음에서 어떤 역할도 누락·통합·선택 제외하지 않습니다. 필요한 역할만 읽는 것은 전체 모음의 삭제나 모든 역할의 실행을 뜻하지 않습니다.

- 저장소 규칙 발견: repo-governance. 현재 선택·조합: using-skills.
- 개인 운영 규약: work-rules. 참여 agent 잠금: kiro-lock.
- Bash 작성: bash-script-template. Python 작성: python-script-template.
- 코드 검토: code-review. 테스트 설계/작성: testing-guide.
- Markdown 링크·헤딩: md-link-check. 개인 문서/푸터: readme-template. 실제 Zircon 예외: zircon-readme-policy.
- 변경 게시 규약: git-commit-rule. 보안 도구/수동 점검: security-tools.
- 명세: spec-driven-infra. 작업 분해: planning-and-breakdown. 점진적 변경: incremental-change.
- 장애/복구: debugging-and-recovery. 중요한 결정 교차 검토: doubt-driven-infra. 배포 준비: shipping-checklist.

Windows에서도 원문의 발견 트리·구성·우선순위를 현재 요청 범위에 맞춰 적용합니다. Bash는 Git Bash/WSL/원격의 실제 Bash 역할로 유지하며 PowerShell 스크립트를 Bash 템플릿의 명칭만 바꿔 작성하지 않습니다. native PowerShell/Python과 필요한 원격 실행을 구분합니다.

- 실제 코드 리뷰는 수정·commit/push를 자동 포함하지 않습니다. 계획은 운영 적용을 자동 포함하지 않습니다. 수정·배포·복구가 승인된 경우에만 필요한 후속 체인을 선택합니다. 단순 질의나 제한된 변경을 모든 skill·검사·새 agent의 강제 발동으로 확대하지 않습니다.
- 새 정책·기록·catalog·installer 생성은 실제 요청이 있을 때만 수행합니다. 현재 AGENTS/하위 지침과 필요한 동봉 참조를 먼저 읽고 개인 규약은 사용자/저장소 범위에서 함께 유지합니다.
- 잠금 disabled·Kiro hook 상태는 과거 자료입니다. Windows에서는 현행 잠금 정책과 helper를 따릅니다. Zircon 예외는 실제 해당 저장소에서만 적용하고 다른 README에 전파하지 않습니다.
- 읽은 참조의 Windows 위험 대체 조건도 적용합니다. R01 state 복구·R03 패키지 복구·R04 의존성/호환성·R05 데이터/앱 복귀·R06 공개 SG는 과거 원문 예시로 되돌리지 않습니다. 오류 전파·입력 검증·파싱·잠금의 결과는 실제 실행을 근거로 판정합니다.

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://bash-script-template` → [bash-script-template](references/skills/bash-script-template.md).
- `skill://code-review` → [code-review](references/skills/code-review.md).
- `skill://debugging-and-recovery` → [debugging-and-recovery](references/skills/debugging-and-recovery.md).
- `skill://doubt-driven-infra` → [doubt-driven-infra](references/skills/doubt-driven-infra.md).
- `skill://git-commit-rule` → [git-commit-rule](references/skills/git-commit-rule.md).
- `skill://incremental-change` → [incremental-change](references/skills/incremental-change.md).
- `skill://kiro-lock` → [kiro-lock](references/skills/kiro-lock.md).
- `skill://md-link-check` → [md-link-check](references/skills/md-link-check.md).
- `skill://planning-and-breakdown` → [planning-and-breakdown](references/skills/planning-and-breakdown.md).
- `skill://python-script-template` → [python-script-template](references/skills/python-script-template.md).
- `skill://readme-template` → [readme-template](references/skills/readme-template.md).
- `skill://repo-governance` → [repo-governance](references/skills/repo-governance.md).
- `skill://security-tools` → [security-tools](references/skills/security-tools.md).
- `skill://shipping-checklist` → [shipping-checklist](references/skills/shipping-checklist.md).
- `skill://spec-driven-infra` → [spec-driven-infra](references/skills/spec-driven-infra.md).
- `skill://testing-guide` → [testing-guide](references/skills/testing-guide.md).
- `skill://work-rules` → [work-rules](references/skills/work-rules.md).
- `skill://zircon-readme-policy` → [zircon-readme-policy](references/skills/zircon-readme-policy.md).

문서 개인 양식은 [STYLE.md](references/STYLE.md)를 현재 사용자/저장소 예외와 함께 적용합니다.

### 동봉 도구 호출

다음 PowerShell 호출의 `$pythonExe`는 확인한 실제 Python, `$skillDir`는 현재 복사된 폴더, `$target`은 명시한 검사 대상입니다. 코드 작성과 실제 실행/설치 검증을 구분합니다.

```powershell
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/lock.py') --help
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-heading-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-link-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-style-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
```

잠금 help 확인은 실제 acquire/check/release나 전체 실패/경쟁 검증이 아닙니다. 원문의 Kiro 실행 상태와 새 Windows 설치 상태를 혼동하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## Overview

작업이 도착하면 적절한 스킬을 식별하여 적용하는 메타 스킬입니다.

## Skill Discovery

```
Task arrives
    │
    ├── 저장소 파일 수정/작업 시작?  → repo-governance (.governance/ 우선 확인)
    ├── 새 인프라 구축/대규모 변경?  → spec-driven-infra
    ├── 작업 분해 필요?              → planning-and-breakdown
    ├── IaC 코드 작성/수정?          → incremental-change
    ├── 장애/오류 발생?              → debugging-and-recovery
    ├── Python 스크립트 작성?          → python-script-template
    ├── Bash 스크립트 작성?            → bash-script-template
    ├── 협업 디렉토리 파일 수정?      → kiro-lock (현재 disabled — 협업 시 enable 필요)
    ├── 코드/스크립트 리뷰?          → code-review
    ├── 보안 검토/마스킹?            → security-tools
    ├── 프로덕션/비가역 변경?        → doubt-driven-infra
    ├── 배포/런칭?                   → shipping-checklist
    ├── 테스트 작성?                 → testing-guide
    ├── Git 커밋/PR?                 → git-commit-rule
    ├── 마크다운 문서 작성?          → work-rules + STYLE.md
    ├── 마크다운 링크·앵커 검증?     → md-link-check (링크·앵커·헤딩 구조 규칙)
    ├── README 푸터/배지 적용?       → readme-template
    └── 위 해당 없음?               → work-rules 기본 규칙 적용
```

## Skill Composition

스킬은 단독 또는 조합으로 사용합니다.

| 시나리오           | 스킬 체인                                                       |
|--------------------|-----------------------------------------------------------------|
| 새 인프라 프로젝트 | spec-driven-infra → planning-and-breakdown → incremental-change |
| 프로덕션 변경      | doubt-driven-infra → incremental-change → shipping-checklist    |
| 장애 대응          | debugging-and-recovery → incremental-change                     |
| 코드 리뷰 후 수정  | code-review → incremental-change → testing-guide                |

## Precedence

스킬 적용 전에 규칙 우선순위를 확인합니다.

```
사용자의 명시적 지시  >  repo-local .governance/  >  전역 skill  >  기본 동작
```

안전 관련 항목(비가역 작업 승인, 자격증명 취급)은 우선순위와 무관하게 항상 확인
절차를 거칩니다. 상세는 `skill://repo-governance` 를 참고합니다.

## Rules

- 저장소 작업 시작 시 `.governance/` 존재를 먼저 확인합니다
- 스킬이 적용 가능하면 반드시 사용합니다
- "작아서 스킬 불필요"는 잘못된 판단입니다
- 여러 스킬이 해당되면 체인으로 연결합니다
- 스킬 내 verification 단계를 건너뛰지 않습니다
