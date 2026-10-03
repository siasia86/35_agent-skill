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

공통 절차·기존 SE 시험 기록과 환경·사용자·작업공간별 관찰 및 공개 가능한 적용 사본을 보관합니다. Agent·Skill·Prompt의 구현 원본과 사용 안내는 각 도구 디렉토리의 README·docs/에서 관리합니다.

- common/: 공통 최초 적용·업데이트 체크리스트.
- gpt/: 기존 SE_PILOT.md·SE_PILOT_RESULTS.md 시험 기록. 경로와 과거 기록은 보존합니다.
- [codex/](codex/README.md): 과거 개인 홈의 skill 관찰 사본·inventory와 환경·작업공간별 후속 기록 기준. `pc01_codex-app-home`은 공개 별칭입니다.
- ../kiro/docs/: Kiro 사용자 지침.
- [../codex_linux/](../codex_linux/README.md): 현재 개인 스킬의 수동 복사·기존 편집 보존·검증 안내.
- [../codex_windows/](../codex_windows/README.md): Windows 전용 계획·골격과 후속 검증 안내.
- ../105_backup/codex/docs/: 폐기한 Codex 개발본의 역사적 적용 지침. 현재 설치 입력으로 사용하지 않습니다.
- ../claude/docs/: Claude 예약 영역의 적용 전 점검 지침.

도구 디렉토리 전체가 설치 payload인 것은 아닙니다. docs/와 개발·검증 기록은 runtime에 복사하지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 공통 workflow

각 도구별 지침는 다음 공통 단계를 따릅니다.

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

| 도구   | 최초 적용                                         | 업데이트                                                  | 현재 상태                     |
|--------|---------------------------------------------------|-----------------------------------------------------------|-------------------------------|
| Kiro   | [최초 적용](../kiro/docs/KIRO_SETUP_GUIDE.md)     | [업데이트](../kiro/docs/KIRO_UPDATE_GUIDE.md)             | 선택 적용 전 검토 필요        |
| Codex  | [수동 복사](../codex_linux/README.md#2-수동-복사) | [비교·백업 후 복사](../codex_linux/README.md#2-수동-복사) | 현재 모음·개인 설치 미실행    |
| Claude | [최초 적용](../claude/docs/CLAUDE_SETUP_GUIDE.md) | [업데이트](../claude/docs/CLAUDE_UPDATE_GUIDE.md)         | source·allowlist 확정 전 예약 |

새 Codex 개인 스킬은 폴더 전체의 수동 복사를 기본으로 하며 catalog·adapter·installer·30·31을 필수로 요구하지 않습니다. 기존 공통 체크리스트의 manifest·adapter 항목은 해당 구성이 실제 제공될 때만 적용합니다. [1.0.0 실행 기록](codex/REBUILD_1.0.0.md)을 확인합니다.

도구별 구성은 독립 사용을 기본으로 작성합니다. 현재 작업공간에 31에서 관리하는 설정이 적용되어 있으면 그 적용 범위와 지침을 확인해 함께 사용합니다. 실제 지원 설치 위치·설정 로딩·기능은 도구별 안내와 검증 결과를 따릅니다. Claude는 필수 원본과 적용·검증 방법이 확정될 때까지 예약 상태를 유지합니다.

폐기한 Codex의 [최초 적용](../105_backup/codex/docs/CODEX_SETUP_GUIDE.md)·[업데이트](../105_backup/codex/docs/CODEX_UPDATE_GUIDE.md) 문서는 과거 이력으로 보존합니다. 새 설치에 사용하지 않습니다.

도구별 지침는 공통 TODO의 원칙을 따르되, 다른 도구의 명령·경로·runtime 설정을 사용하지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 운영 원칙

- source·staging·runtime target을 서로 다른 경로로 관리합니다.
- runtime 적용 전 기존 설정을 백업하고 `dry-run` 결과를 검토합니다.
- version·commit·manifest·checksum을 기록합니다.
- 개인 설정·세션·credential·private key는 payload와 manifest에서 제외합니다. 사용자가 선택한 공개 가능 skill 폴더의 환경별 관찰 사본만 codex/에 보관하며 전체 홈·실제 AGENTS·전체 config는 복제하지 않습니다.
- 도구별 payload는 각 도구의 공개 allowlist를 통해서만 배포합니다.
- 외부 Agent·Skill은 license·권한·외부 통신·유지보수 상태를 검토한 뒤 필요한 패턴만 반영합니다.
- AI skill·prompt는 보안 경계가 아니며, 실제 강제는 CI·IAM·runner·network policy에서 수행합니다.
- 기존 사용자 변경 사항과 미추적 파일을 확인하지 않고 삭제하거나 덮어쓰지 않습니다.

새 Codex 모음은 선택한 스킬 폴더 전체가 공개 복사 단위이며 별도 allowlist 파일을 준비할 필요가 없습니다. 원문 대응·실제 파일·버전·commit·검증 범위를 확인합니다. 기존 manifest/adapter 기반의 도구는 그 도구의 실제 제공 구성을 따릅니다.

### 4.1 환경과 작업공간별 기록

- 실행 환경·사용자·도구·클라이언트 버전·적용 범위·작업공간을 구분하고 공개 기록에는 별칭을 사용합니다. 실제 경로·계정·자격증명의 공개 범위는 기존 제한을 따릅니다.
- 개인 홈의 공통 설치는 하나의 설치 기록으로 관리합니다. 각 작업공간은 그 기록을 참조하고, 해당 작업공간의 적용 지침·추가 스킬·31 설정 적용 여부와 발견·대표 행동 결과를 따로 남깁니다.
- 저장소에 직접 설치한 구성은 그 저장소의 별도 설치 기록으로 관리합니다. 사용자 홈과 저장소에 동명 구성이 있으면 각 출처·경로·선택 대상을 확인합니다. 발견·호출 방식은 도구별 지원 범위로 검증합니다.
- 출처 commit·version·전체 파일 해시·확인일과 설치·발견·대표 행동 상태를 기록합니다. 변경·제거 시 영향받는 설치 기록과 작업공간의 관찰 상태를 함께 갱신합니다. 과거 성공을 새 상태의 검증으로 재사용하지 않습니다.
- 구현 검증과 실제 사용자 환경 검증을 구분합니다. 설명용 예시에는 설치 완료 표시를 붙이지 않으며 관찰 사본을 독립 편집하거나 설치 입력으로 사용하지 않습니다.

Codex의 후속 기록 구조와 두 작업공간 예시는 [환경·작업공간별 기록 안내](codex/README.md#5-환경과-작업공간별-후속-기록)에 있습니다. 도구별로 확인한 지원 범위만 기록하며 자동 수집·동기화는 구현·검증한 결과가 있을 때만 완료로 표시합니다.

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

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
