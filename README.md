# 35 `agent-skill`

재사용할 AI 지침·skill·agent와 도구별 공개 미러를 관리합니다.

## 목차

| 섹션                                              |
|---------------------------------------------------|
| [1. 목적](#1-목적) / [2. 구성](#2-구성)           |
| [3. 운영 원칙](#3-운영-원칙) / [4. 검증](#4-검증) |
| [5. 활용](#5-활용)                                |

---

## 1. 목적

`35_agent-skill`은 도구별 보존 원본과 재사용 자산 개발 공간을 분리합니다. kiro/·gpt/는 보존 원본, codex/는 개선 공간, claude/는 예약 영역입니다. 개발 후보를 승인된 설치 release로 취급하지 않습니다.

저장소 운영 정책 자체는 [31 `governances`](https://github.com/siasia86/31_governances)를 따릅니다. 이 저장소에는 저장소 공통 policy를 다시 작성하지 않습니다.

## 2. 구성

| 디렉토리           | 역할                          | 원본·범위                     |
|--------------------|-------------------------------|-------------------------------|
| `kiro/`            | Kiro 공개 미러                | `~/.kiro/` 허용 목록          |
| `gpt/`             | GPT/Codex 보존 원본           | 개선 시 직접 수정하지 않음    |
| `codex/`           | 재사용 자산 개발·선택 payload | 전체 복사 설치 금지           |
| `claude/`          | Claude 공개 미러 예정         | 원본·허용 목록 미정           |
| `agent-workflows/` | 공통 안전 절차·시험 기록      | 도구별 사용자 지침은 각 docs/ |
| `_reference/`      | Agent·Skill 개선 참고 문서    | 32 문서 복사본                |

- [Kiro 미러](kiro/README.md): `~/.kiro/`에서 허용된 자료만 보존합니다.
- [GPT 보존 원본](gpt/README.md): 이식 출발 자료입니다.
- [Codex 개발본](codex/README.md): 선택 후보와 검증 상태를 확인합니다.
- [Claude 미러](claude/README.md): Claude 자료 추가를 위한 예약 영역입니다.
- [Agent workflow](agent-workflows/README.md): 공통 및 도구별 TODO를 관리합니다.
- [Agent 참고 문서](_reference/INDEX.md): 업데이트에 사용하는 참고 문서 색인입니다.

## 3. 운영 원칙

- 저장소 정책은 특정 AI 도구의 실행 환경과 분리합니다.
- 도구별 payload와 도구별 workflow를 분리합니다.
- 개인 설정, 세션 상태, 자격증명, 내부 환경 정보는 공개 미러에 포함하지 않습니다.
- 보존 미러는 원본에서 공개 미러 방향으로 관리하며 자동 역동기화하지 않습니다. codex/ 개선 작업과 구분합니다.
- 공통 절차는 `agent-workflows/common/`, 도구별 사용자 지침은 각 도구의 `docs/`에 둡니다. 문서는 runtime payload가 아닙니다.
- 디렉토리 구조를 변경하면 이 `README.md`와 `CHANGELOG.md`를 함께 갱신합니다.

## 4. 검증

```bash
sia-md-link-check .
sia-md-heading-check .
sia-md-style-check .
git diff --check
gitleaks detect --source . --no-git --no-banner
```

도구별 payload를 변경한 경우 JSON·TOML·Bash·manifest 검증을 추가합니다. `kiro/`와 향후 `claude/`의 mirror 문서는 원본 형식을 보존할 수 있으므로 일반 Markdown 스타일 검사에서 별도 예외가 필요한지 확인합니다.

## 5. 활용

먼저 사용할 도구의 지침을 읽고 참고만 할지, 자신의 환경에 선택 적용할지 결정합니다. 문서 열람과 clone은 설치·수정 승인이 아닙니다.

| 도구   | 최초 적용                                             | 업데이트                                              | 상태                         |
|--------|-------------------------------------------------------|-------------------------------------------------------|------------------------------|
| Kiro   | [Kiro 최초 적용](kiro/docs/KIRO_SETUP_GUIDE.md)       | [Kiro 업데이트](kiro/docs/KIRO_UPDATE_GUIDE.md)       | 선택 파일과 의존성 검토 필요 |
| Codex  | [Codex 최초 적용](codex/docs/CODEX_SETUP_GUIDE.md)    | [Codex 업데이트](codex/docs/CODEX_UPDATE_GUIDE.md)    | 개발 후보·전체 설치 금지     |
| Claude | [Claude 최초 적용](claude/docs/CLAUDE_SETUP_GUIDE.md) | [Claude 업데이트](claude/docs/CLAUDE_UPDATE_GUIDE.md) | 예약 영역·실제 적용 금지     |

- [공통 최초 적용](agent-workflows/common/USER_TODO.md)과 [공통 업데이트](agent-workflows/common/UPDATE_TODO.md): 백업·선택 목록·검증·복구 기준.
- [개발 TODO](TODO.md): 저장소의 미완료 개발 작업. 사용자 설치 순서와 구분합니다.
- [변경 이력](CHANGELOG.md): 완료된 저장소 변경.

공용 지침서의 체크리스트는 사용자별 작업 기록에 복사해 사용합니다. 개인 경로·백업·실행 결과를 공용 지침서에 누적하지 않습니다. docs/·개발 TODO·시험 기록은 runtime 복사에서 제외하고, 선택한 자산과 필수 의존성만 설치합니다.


---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
