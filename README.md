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

### 세 저장소의 책임

| 저장소         | 책임                                                      | 담당하지 않는 것        |
|----------------|-----------------------------------------------------------|-------------------------|
| 35_agent-skill | 재사용 지침·skill·agent 구현과 자산 목록                  | 대상별 적용 승인        |
| 31_governances | 공통 정책과 저장소별 관리 설정·자산 선택·예외의 중앙 원본 | 실행 코드·자격증명 보관 |
| 30_sia-scripts | 검증·계획·설치·갱신·복구 실행 도구                        | 명세에 없는 정책 추정   |

위 표는 중앙 관리 목표의 책임 구분입니다. 31의 기존 v1과 중앙 소유 전환 계약은 구분하며, 기존 대상 저장소의 예외를 자동 덮어쓰지 않습니다. 35는 구현 원본과 선택 후보를 제공하고 적용 대상·예외·승인을 자체 결정하지 않습니다.

현재 연결은 35 자산 목록 + 31 draft profile → 30 읽기 전용 planner → 설치 불가 계획 출력입니다. 검증된 staging의 활성화와 운영 복구 통합은 후속 작업입니다.

저장소 공통 정책의 원본은 [31 governances](https://github.com/siasia86/31_governances), 실행 도구는 [30 sia-scripts](https://github.com/siasia86/30_sia-scripts)에서 관리합니다. 이 저장소의 작업 범위·보존 규칙·예외는 [AGENTS.md](AGENTS.md)를 따릅니다. 아래 내용은 진입 안내이며 상세 정책 원본을 대체하지 않습니다.

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
- [Agent workflow](agent-workflows/README.md): 공통 체크리스트·도구별 지침 색인·기존 SE 시험 기록을 관리합니다.
- [Agent 참고 문서](_reference/INDEX.md): 업데이트에 사용하는 참고 문서 색인입니다.

### 개발 상태와 설치 경계

- codex/payload에는 최소 SE 지침, 검토 skill 2개와 읽기 전용 agent 2개가 있습니다. [자산 목록](codex/ASSET_CATALOG.json)은 개발 목록이지 승인 release manifest가 아닙니다.
- 최소 지침의 기존 개인 설치 시험 기록과 신규 사용자의 설치 완료는 다릅니다. skill·agent 후보의 정적·격리 검사를 전체 runtime 검증으로 확대하지 않습니다.
- 현재 선택 파일과 검증 범위는 [설치 매핑](codex/PAYLOAD_MAP.md), [Batch 2 기록](codex/BATCH2_VERIFICATION.md), [개발 TODO](TODO.md)에서 확인합니다.
- gpt/·kiro/ 보존 영역을 일괄 활성화하지 않습니다. claude/는 source·허용 목록·설치 대상이 확정되기 전까지 적용하지 않습니다.
- docs/·TODO·시험 기록은 설치 payload가 아닙니다. 보존 미러의 허용 목록과 runtime 설치 목록도 구분합니다.

## 3. 운영 원칙

- 저장소 정책은 특정 AI 도구의 실행 환경과 분리합니다.
- 도구별 payload와 도구별 workflow를 분리합니다.
- 개인 설정, 세션 상태, 자격증명, 내부 환경 정보는 공개 미러에 포함하지 않습니다.
- 보존 미러는 원본에서 공개 미러 방향으로 관리하며 자동 역동기화하지 않습니다. codex/ 개선 작업과 구분합니다.
- 공통 절차는 `agent-workflows/common/`, 도구별 사용자 지침은 각 도구의 `docs/`에 둡니다. 문서는 runtime payload가 아닙니다.
- 디렉토리 구조를 변경하면 이 `README.md`와 `CHANGELOG.md`를 함께 갱신합니다.

### 변경 절차와 예외

1. 작업본·브랜치·기존 변경과 저장소 지침을 확인합니다.
2. 복합 개발 작업은 [TODO](TODO.md)에 범위·검증·복구를 정리하고 보존 원본 대신 codex/에서 개선합니다. 사용자 지침 변경과 runtime 변경은 구분합니다.
3. 변경 파일의 문법·참조·해시·비밀정보를 검사하고 완료 내용을 CHANGELOG에 기록합니다.
4. 승인된 작업 브랜치에 commit·push합니다. 개발 후보 게시를 release 승인이나 개인 홈 설치 승인으로 처리하지 않습니다.

직접 수정 제한의 예외는 타당한 이유·명시적 범위·종료 조건·검증·복구 방법이 있어야 합니다. 예외는 해당 작업 종료 시 만료되며 다음 작업에 재사용하지 않습니다. ACL·소유권·자격증명·운영 권한을 자동 확대하지 않습니다. 게시 후 복구는 검토된 revert로 수행하고 사용자 변경을 보존합니다.

AI 지침과 skill 자체는 명령 차단을 강제하는 보안 장치가 아닙니다. 개발·테스트의 넓은 권한도 실행 승인과 구분하며 운영 강제는 실행 도구와 실제 권한·검사 체계에서 검증해야 합니다.

## 4. 검증

```bash
sia-md-link-check README.md CHANGELOG.md
sia-md-heading-check README.md CHANGELOG.md
sia-md-style-check README.md CHANGELOG.md
git diff --check
gitleaks detect --source . --no-git --no-banner
```

위 명령은 루트 문서 변경의 기본 검사입니다. 다른 문서를 변경하면 해당 파일도 검사하고, 검사 도구 미설치·읽기 실패·부분 검사를 전체 통과로 처리하지 않습니다. 도구별 payload를 변경한 경우 JSON·TOML·Bash·manifest 검증을 추가합니다. `kiro/`와 향후 `claude/`의 mirror 문서는 원본 형식을 보존할 수 있으므로 일반 Markdown 스타일 검사에서 별도 예외가 필요한지 확인합니다.

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
- [운영 이슈](ISSUE.md): 관찰된 문제·임시 조치·해결 조건.

공용 지침서의 체크리스트는 사용자별 작업 기록에 복사해 사용합니다. 개인 경로·백업·실행 결과를 공용 지침서에 누적하지 않습니다. docs/·개발 TODO·시험 기록은 runtime 복사에서 제외하고, 선택한 자산과 필수 의존성만 설치합니다.


---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
