# 공통 USER TODO

Kiro·GPT/Codex·Claude의 Agent·Skill·Prompt를 최초 적용할 때 공통으로 수행하는 작업입니다. 도구별 명령과 runtime 경로는 각 사용자 지침에서 결정합니다.

이 문서는 공용 체크리스트입니다. 결과는 별도 사용자 작업 기록에 남기며 공용 원본의 완료 상태를 변경하지 않습니다. 개발 후보·예약 영역의 적용 제한은 도구별 지침이 정한 범위를 따릅니다.

Codex의 독립 개인 스킬은 선택한 폴더 전체를 수동 복사할 수 있습니다. catalog·manifest·adapter 설치기가 없는 구성에서는 해당 검사 항목을 필수 의존성으로 만들지 않고 선택 폴더의 파일·해시·기존 설치·복구를 확인합니다. 실행 도구와 개인 runtime 적용 승인은 별도로 확인합니다.

## 목차

| 섹션                                                                            |
|---------------------------------------------------------------------------------|
| [1. 적용 전 확인](#1-적용-전-확인) / [2. source와 staging](#2-source와-staging) |
| [3. 백업과 적용](#3-백업과-적용) / [4. 검증](#4-검증)                           |
| [5. rollback](#5-rollback) / [6. 완료 기록](#6-완료-기록)                       |

---

## 1. 적용 전 확인

- [ ] 사용할 도구를 선택합니다: `kiro`, `codex`, `claude`.
- [ ] 해당 도구의 [adapter USER TODO](../README.md#3-도구별-workflow)를 확인합니다.
- [ ] source repository의 branch·commit·working tree를 확인합니다.
- [ ] 기존 사용자 변경 사항과 미추적 파일을 보존합니다.
- [ ] 도구의 source·staging·runtime target 경로를 확정합니다.
- [ ] 실행 환경·사용자·도구·적용 범위(개인 공통/저장소별)·작업공간을 확인합니다.
- [ ] 작업공간의 적용 지침과 31 설정 적용 여부·참조 범위를 확인합니다. 연동이 없는 경우 도구별 독립 적용 절차를 사용합니다.
- [ ] 개인 공통 구성과 저장소별 구성의 동명 중복·출처·실제 선택 대상을 도구별 지원 범위로 확인합니다.
- [ ] 원본·공개 allowlist·license·owner를 확인합니다.
- [ ] credential·token·private key·session data가 대상에 포함되지 않는지 확인합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. source와 staging

권장 경로는 다음 세 단계입니다.

```text
source repository
      v
validated staging release
      v
selected runtime target
```

- [ ] source는 특정 commit 또는 release로 고정합니다.
- [ ] manifest·allowlist에 등록된 파일만 staging에 반영합니다.
- [ ] staging에 version·commit·checksum·적용일을 기록합니다.
- [ ] source와 staging의 파일 목록을 비교합니다.
- [ ] staging을 직접 수정하지 않고 source를 수정한 뒤 새 release를 만듭니다.

[⬆ 목차로 돌아가기](#목차)

---

## 3. 백업과 적용

- [ ] runtime target의 현재 상태를 출력합니다.
- [ ] timestamp가 포함된 backup을 생성합니다.
- [ ] target·제외 목록·변경 파일이 표시되는 dry-run을 실행합니다.
- [ ] dry-run 결과를 검토한 뒤에만 적용합니다.
- [ ] 적용은 도구별 adapter script와 allowlist를 사용합니다.
- [ ] source repository가 아닌 runtime target만 변경되는지 확인합니다.
- [ ] 적용된 version·commit·checksum·실행자를 기록합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 검증

- [ ] Agent 설정의 JSON·TOML 문법을 검사합니다.
- [ ] Skill·Prompt Markdown의 heading·link·style을 검사합니다.
- [ ] manifest 파일 존재와 제외 규칙을 검사합니다.
- [ ] shell·Python script 문법을 검사합니다.
- [ ] secret·private key·credential 유사 문자열을 검사합니다.
- [ ] 도구를 실제로 실행해 Agent·Skill 로딩을 확인합니다.
- [ ] 변경 파일·검증 명령·미해결 사항을 기록합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 5. rollback

- [ ] 적용 전 backup 경로를 확인합니다.
- [ ] 적용 실패 시 runtime target을 backup으로 복구합니다.
- [ ] source repository의 기존 변경 사항을 reset하거나 삭제하지 않습니다.
- [ ] 실패한 release를 재사용하지 않고 원인을 기록합니다.
- [ ] 수정된 source로 새 staging release를 만들어 다시 검증합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 6. 완료 기록

개인 홈의 공통 설치는 하나의 기록으로 관리하고, 각 작업공간의 적용 지침·추가 설치·발견·대표 행동 결과는 공통 설치 기록을 참조하여 따로 남깁니다. 상세 기준은 [환경·작업공간별 기록](../README.md#41-환경과-작업공간별-기록)을 따릅니다. 아래 공용 표에는 실제 사용자 결과를 누적하지 않습니다.

| 항목                  | 상태 | 검증일     | 비고                       |
|-----------------------|------|------------|----------------------------|
| 도구·경로 확인        | [ ]  | YYYY-MM-DD | source·staging·target 기록 |
| manifest·license 확인 | [ ]  | YYYY-MM-DD | 공개 범위와 제외 목록 확인 |
| runtime backup        | [ ]  | YYYY-MM-DD | backup 경로 기록           |
| dry-run               | [ ]  | YYYY-MM-DD | 변경 파일 검토             |
| 적용 및 로딩 확인     | [ ]  | YYYY-MM-DD | 도구별 adapter 사용        |
| 검증 및 rollback 확인 | [ ]  | YYYY-MM-DD | 실패 시 복구 경로 확인     |

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-10-02

© 2026 siasia86. Licensed under CC BY 4.0.
