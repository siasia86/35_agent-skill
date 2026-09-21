# Agent Workflows

AI 도구별 Agent·Skill·Prompt의 최초 적용과 업데이트 절차를 관리합니다. 공통 운영 원칙과 도구별 adapter를 분리하여 Kiro·GPT/Codex·Claude의 서로 다른 실행 구조를 혼합하지 않습니다.

## 목차

| 섹션                                                                    |
|-------------------------------------------------------------------------|
| [1. 구조](#1-구조) / [2. 공통 workflow](#2-공통-workflow)               |
| [3. 도구별 workflow](#3-도구별-workflow) / [4. 운영 원칙](#4-운영-원칙) |
| [5. 검증](#5-검증)                                                      |

---

## 1. 구조

```text
agent-workflows/
├── common/
│   ├── USER_TODO.md
│   └── UPDATE_TODO.md
├── kiro/
│   ├── USER_TODO.md
│   └── UPDATE_TODO.md
├── gpt/
│   ├── USER_TODO.md
│   └── UPDATE_TODO.md
└── claude/
    ├── USER_TODO.md
    └── UPDATE_TODO.md
```

- `common/`: 도구에 관계없이 적용하는 backup·staging·검증·rollback 원칙.
- `kiro/`: Kiro CLI·`$HOME/.kiro`·Kiro manifest에 맞춘 절차.
- `gpt/`: GPT/Codex의 `AGENTS.md`·`.agents/skills/`·`.codex/` 구조에 맞춘 절차.
- `claude/`: Claude source·allowlist·target이 확정된 뒤 활성화할 절차.

`kiro/`, `gpt/`, `claude/`는 실제 payload이고 `agent-workflows/`는 운영 문서입니다. workflow 문서를 runtime payload 디렉토리에 넣지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 공통 workflow

각 도구별 TODO는 다음 공통 단계를 따릅니다.

```text
source 확인
    v
version·manifest·license 검증
    v
staging 적용
    v
runtime backup
    v
dry-run
    v
도구별 runtime 적용
    v
검증·evidence 기록
    v
rollback 가능 상태 확인
```

공통 문서는 다음과 같습니다.

- [최초 적용 공통 TODO](common/USER_TODO.md)
- [업데이트 공통 TODO](common/UPDATE_TODO.md)

[⬆ 목차로 돌아가기](#목차)

---

## 3. 도구별 workflow

| 도구      | 최초 적용                        | 업데이트                             | 현재 상태                       |
|-----------|----------------------------------|--------------------------------------|---------------------------------|
| Kiro      | [USER_TODO](kiro/USER_TODO.md)   | [UPDATE_TODO](kiro/UPDATE_TODO.md)   | Kiro payload와 적용 script 존재 |
| GPT/Codex | [USER_TODO](gpt/USER_TODO.md)    | [UPDATE_TODO](gpt/UPDATE_TODO.md)    | payload는 작업 중·일부 미추적   |
| Claude    | [USER_TODO](claude/USER_TODO.md) | [UPDATE_TODO](claude/UPDATE_TODO.md) | source·allowlist 확정 전 예약   |

도구별 TODO는 공통 TODO의 원칙을 따르되, 다른 도구의 명령·경로·runtime 설정을 사용하지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 운영 원칙

- source·staging·runtime target을 서로 다른 경로로 관리합니다.
- runtime 적용 전 기존 설정을 백업하고 `dry-run` 결과를 검토합니다.
- version·commit·manifest·checksum을 기록합니다.
- 개인 설정·세션·credential·private key는 payload와 manifest에서 제외합니다.
- 도구별 payload는 각 도구의 공개 allowlist를 통해서만 배포합니다.
- 외부 Agent·Skill은 license·권한·외부 통신·유지보수 상태를 검토한 뒤 필요한 패턴만 반영합니다.
- AI skill·prompt는 보안 경계가 아니며, 실제 강제는 CI·IAM·runner·network policy에서 수행합니다.
- 기존 사용자 변경 사항과 미추적 파일을 확인하지 않고 삭제하거나 덮어쓰지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 5. 검증

workflow 문서 변경 후 저장소 루트에서 실행합니다.

```bash
sia-md-style-check agent-workflows/
sia-md-heading-check agent-workflows/
sia-md-link-check agent-workflows/
git diff --check
gitleaks detect --source . --no-git --no-banner
```

도구별 payload를 변경한 경우 해당 도구의 JSON·TOML·script·manifest 검증도 추가합니다.

[⬆ 목차로 돌아가기](#목차)

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-21

© 2026 siasia86. Licensed under CC BY 4.0.
