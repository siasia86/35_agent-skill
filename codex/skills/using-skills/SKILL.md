---
name: using-skills
description: Maps incoming work to the right skill workflow. Use when starting a session, when deciding which skill applies, or when the task type is unclear.
---

# Using Skills

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 아래 트리·조합 표의 모든 스킬 지침은 동봉 로컬 참조로 제공됩니다. 다른 개인 스킬이 설치되어 있어야 한다는 전제는 없습니다. 현재 요청에 해당하는 참조만 읽고 단순 질의를 전체 스킬 체인·인프라 절차로 확대하지 않습니다.
- `.governance`는 저장소가 채택한 경우에 적용합니다. Codex의 적용 AGENTS.md도 저장소 지침입니다. 디렉토리가 없다는 이유만으로 새 정책 파일·중앙 31 저장소·설치기를 만들지 않습니다. 명시 승인된 행위를 같은 개인 스킬 확인 절차 때문에 다시 승인 요청하지 않습니다.
- 잠금 disabled 상태는 원문의 과거 관찰입니다. 현재 잠금 정책을 확인합니다. Zircon 예외는 그 대상 저장소만 해당하며 다른 README로 전파하지 않습니다.

로컬 워크플로 대응(필요한 항목만 읽음):

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

문서 스타일은 동봉 [STYLE.md](references/STYLE.md)를 사용합니다. `sia-md-*` 대신 동봉 스크립트를 Python 3.11 이상으로 실행합니다. 기본 OS/언어 runtime 외 pip·다른 저장소 설치는 필요하지 않습니다. 대상 저장소의 선택적 TOML 설정은 실제 존재할 때만 적용합니다.

- `python3 <SKILL_DIR>/scripts/md-style-check.py <target>`
- `python3 <SKILL_DIR>/scripts/md-heading-check.py <target>`
- `python3 <SKILL_DIR>/scripts/md-link-check.py <target>`

`<SKILL_DIR>`는 현재 복사된 스킬 폴더입니다. 원문의 fix_table_align/trim_diagram 외부 자동 수정기를 필수로 호출하지 않고, 보고된 표/다이어그램을 현재 파일에서 직접 수정한 뒤 다시 검사합니다. 외부 스크립트의 모든 옵션이 구현됐다고 주장하지 않습니다.

저장소 지침이 푸터·날짜·배지를 금지하면 style 검사에 `--no-footer`를 사용하고 그 적용 근거와 제외 범위를 기록합니다. 다른 검사는 계속 실행합니다. 정책상 금지된 푸터를 검사 통과 목적으로 추가하거나 그 결과를 미해결 오류로 취급하지 않습니다. 실제 내용 결함을 숨기기 위한 임의 skip은 하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
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
