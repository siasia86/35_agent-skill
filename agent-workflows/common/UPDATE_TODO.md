# 공통 UPDATE TODO

Kiro·GPT/Codex·Claude의 Agent·Skill·Prompt를 업데이트할 때 공통으로 수행하는 작업입니다. 실제 명령과 runtime 경로는 각 도구별 사용자 지침에서 결정합니다.

이 문서는 공용 체크리스트입니다. 결과는 별도 사용자 작업 기록에 남기며 공용 원본의 완료 상태를 변경하지 않습니다. 개발 후보·예약 영역의 적용 제한은 도구별 지침이 정한 범위를 따릅니다.

Codex의 독립 개인 스킬은 선택한 폴더 전체를 수동 복사할 수 있습니다. catalog·manifest·adapter 설치기가 없는 구성에서는 해당 검사 항목을 필수 의존성으로 만들지 않고 선택 폴더의 파일·해시·기존 설치·복구를 확인합니다. 실행 도구와 개인 runtime 적용 승인은 별도로 확인합니다.

## 목차

| 섹션                                                                    |
|-------------------------------------------------------------------------|
| [1. 변경 전 확인](#1-변경-전-확인) / [2. 변경 검토](#2-변경-검토)       |
| [3. staging과 regression](#3-staging과-regression) / [4. 적용](#4-적용) |
| [5. 검증과 rollback](#5-검증과-rollback) / [6. 완료 기록](#6-완료-기록) |

---

## 1. 변경 전 확인

- [ ] 도구별 adapter와 공통 workflow를 읽습니다.
- [ ] 현재 source·staging·runtime version을 기록합니다.
- [ ] Git branch·commit·working tree를 확인합니다.
- [ ] 기존 사용자 변경 사항과 미추적 파일을 보존합니다.
- [ ] 변경 대상·영향 범위·rollback version을 작성합니다.
- [ ] 개인 공통 구성의 변경이 영향을 주는 작업공간과 저장소별 추가 구성을 확인합니다.
- [ ] 각 작업공간의 적용 지침·31 설정 적용 여부·동명 구성의 선택 대상이 달라졌는지 확인합니다.
- [ ] 외부 자료의 license·보안·유지보수 상태를 확인합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 변경 검토

- [ ] Agent·Skill·Prompt의 역할과 권한 범위를 확인합니다.
- [ ] 도구 전용 경로와 다른 도구의 명령이 섞이지 않았는지 확인합니다.
- [ ] 사용하지 않는 script·hook·config 참조를 확인합니다.
- [ ] public payload에 private path·credential·session data가 없는지 확인합니다.
- [ ] manifest·allowlist·checksum 변경을 별도로 검토합니다.
- [ ] 기존 사용자 작업을 덮어쓰는 sync 방향이 없는지 확인합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 3. staging과 regression

- [ ] 변경 source를 특정 commit 또는 release로 고정합니다.
- [ ] staging release를 새로 생성합니다.
- [ ] JSON·TOML·Markdown·script 문법을 검사합니다.
- [ ] manifest 파일 존재와 제외 규칙을 검사합니다.
- [ ] 기존 Agent·Skill·Prompt와의 중복·충돌을 확인합니다.
- [ ] 대표 작업을 실행해 Agent loading·Skill loading·Prompt 동작을 확인합니다.
- [ ] 이전 release와 변경된 파일·권한·checksum을 비교합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 적용

- [ ] runtime target을 백업합니다.
- [ ] staging에서 runtime target으로 dry-run을 실행합니다.
- [ ] 변경 범위와 제외 범위를 검토합니다.
- [ ] 도구별 adapter script 또는 공식 적용 절차로 반영합니다.
- [ ] 적용 version·commit·checksum·실행자를 기록합니다.
- [ ] source repository의 미추적 파일과 변경 사항을 보존합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 5. 검증과 rollback

- [ ] Agent·Skill·Prompt가 정상적으로 로드됩니다.
- [ ] 대표 작업의 검증 결과를 확인합니다.
- [ ] security·secret·license 검사를 통과합니다.
- [ ] 문제가 있으면 이전 backup 또는 release로 복구합니다.
- [ ] 실패 원인과 재발 방지 작업을 기록합니다.
- [ ] 검증이 끝난 뒤에만 완료 상태로 변경합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 6. 완료 기록

변경한 설치의 출처·파일 해시·확인일을 갱신하고, 그 설치를 참조하는 작업공간에는 새 버전의 발견·대표 행동 검증 상태를 각각 기록합니다. 이전 버전의 성공 기록은 당시 관찰로 보존합니다. 상세 기준은 [환경·작업공간별 기록](../README.md#41-환경과-작업공간별-기록)을 따릅니다. 아래 공용 표에는 실제 사용자 결과를 누적하지 않습니다.

| 항목                   | 상태 | 검증일     | 비고                   |
|------------------------|------|------------|------------------------|
| source·version 확인    | [ ]  | YYYY-MM-DD | commit·release 기록    |
| 변경·권한·license 검토 | [ ]  | YYYY-MM-DD | public payload 확인    |
| staging regression     | [ ]  | YYYY-MM-DD | 이전 release와 비교    |
| runtime backup·dry-run | [ ]  | YYYY-MM-DD | rollback 경로 기록     |
| 적용·Agent loading     | [ ]  | YYYY-MM-DD | 도구별 adapter 사용    |
| 최종 보안·문서 검증    | [ ]  | YYYY-MM-DD | 실패 시 완료 처리 금지 |

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-10-02

© 2026 siasia86. Licensed under CC BY 4.0.
