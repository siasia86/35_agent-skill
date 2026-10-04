# main 기본 작업 정책 업데이트

## 1. 목적과 범위

BRANCH-POLICY-20261004-01은 사용자가 요청한 일반 개인 작업의 main 직접 개발·검증·commit·일반 push를 반영합니다. 필요한 agent/task 브랜치·worktree, QA·Migration·복구 목적 브랜치와 upstream 읽기 전용 경계는 유지합니다. 보호 규칙의 필수 PR·검사를 준수하며 읽기 전용·변경 0건은 게시하지 않습니다.

31의 [중앙 개정 기록](https://github.com/siasia86/31_governances/blob/main/.governance/history/2026-10-04_main-branch-policy.md)을 정책 원본으로 사용하고, 개인 구현은 [배포 AGENTS](../../../codex_windows/AGENTS.md)·work-rules·git-commit-rule과 두 동봉 참조에서 정리합니다. 초기 이관·LC-PUB의 당시 순서는 보존하고 현행 PLAN/TODO에서 대체 관계를 안내합니다.

## 2. 실행 순서와 담당

main agent는 판단·편집·최종 검증·게시를 담당하고 gpt-6-luna 지원 agent는 지침·브랜치 목록 대조와 정책 사례를 읽기 전용으로 검토합니다. 중앙 원본 검증·게시 → 대상 AGENTS의 필요한 구간 병합 → 35 원본 검증 → 지정 로컬 설치본 반영 → 담당 기록·main 일반 게시 순서입니다. 설정·모델 선택은 변경하지 않습니다.

## 3. 보존과 전환

관리 작업본 7곳은 clean·조상 관계를 확인한 뒤 main으로 준비했습니다. 02의 기존 계획 commit은 fast-forward로 포함했고 yunli와 다른 브랜치는 삭제·재작성하지 않았습니다. 41의 원격 기본 HEAD는 yunli로 관찰되어 로컬 main·게시 대상과 구분하며 원격 기본 설정은 변경하지 않습니다.

개인 skill 7개 전체 폴더와 수정 source 4개 폴더, 개인 지침·config·Git index·refs·문서 사본은 이 업데이트의 Git 제외 private에 보존합니다. 기존 설치 차이는 md-link-check에서 관찰했고 교체 대상에서 제외합니다. 실제 경로·raw·개인 설정은 게시하지 않습니다.

## 4. 검증과 실제 결과

[중앙 source commit](https://github.com/siasia86/31_governances/commit/5bc37da9aa43597a0ed59fc47aa23067368427d1)을 main에 게시·원격 SHA 대조한 뒤 현장 AGENTS와 운영 구간을 병합했습니다. 관련 Markdown·정책 사례 검사는 통과했습니다. 최초 이관 검사기는 19개만 허용해 현재 20개 inventory에서 중단되므로 원본을 변경하지 않고 작업용 호출에서 fact-check 추가를 인정한 뒤 최초 19개 검사를 수행합니다. fact-check 메타데이터와 설치 보류는 별도로 확인합니다. 최초 19개 skill 메타데이터·원문 368개 hash 대조·단독 참조 77개·Python 구문 34개·격리 helper 27회는 통과했습니다. 현재 20개 inventory와 fact-check 메타데이터를 별도 확인했습니다. work-rules·git-commit-rule 전체 62개 파일이 원본과 일치하고 개인 AGENTS는 게시 규칙 1줄만 변경해 나머지 사용자 안내를 보존했습니다. 설치하지 않은 5개 개인 skill 폴더는 전후 동일하고 fact-check 설치는 수행하지 않았습니다.

설치 전 실제 config의 외부 변경을 감지해 최초 사본과 별도로 보존했습니다. 이번 작업은 config를 쓰지 않았고 설치 직전·직후 hash 일치를 확인했습니다. 초기 거부 검사와 이후 구분 검증은 private에 남깁니다. [비민감 검증 집계](validation.json)와 실제 main 게시·원격 SHA는 완료 보고에서 확인합니다. 새 세션 행동·원격 CI는 별도 미확인입니다.

중앙 source 22개 Markdown과 최초 소비 문서 23개 Markdown의 관련 검사가 통과했습니다. 후속 인계·집계 수정은 변경 범위만 다시 검사합니다. 교차 파일 fragment 101개는 이슈 0건입니다.

| 대상         | 게시 브랜치 | 원격 SHA 대조 commit                                                                                            |
|--------------|-------------|-----------------------------------------------------------------------------------------------------------------|
| POLICY-31    | main        | [5bc37da](https://github.com/siasia86/31_governances/commit/5bc37da9aa43597a0ed59fc47aa23067368427d1)           |
| SKILL-35     | main        | [4c47824](https://github.com/siasia86/35_agent-skill/commit/4c4782493558665d6c6768b648964ccd24d02d16)           |
| ZWS-02       | main        | [654d097](https://github.com/siasia86/02_zircon-workspace-plan/commit/654d0973e1a9684a5c65586247aeeb187acb2050) |
| PARENT       | main        | [fa7a322](https://github.com/siasia86/12_github-main/commit/fa7a3225201a3dbf18090fe1822a22231e192413)           |
| SCRIPT-30    | main        | [88edcf4](https://github.com/siasia86/30_sia-scripts/commit/88edcf4a0b4cf25dbac71350fcd410fc850cc2ac)           |
| REFERENCE-41 | main        | [62cf46e](https://github.com/siasia86/41_clone-repo/commit/62cf46ed22344df0ade215d07bcf59ea49a447af)            |

관리 7개 작업본은 main이며 문서 변경이 있는 6개 저장소의 일반 push·원격 SHA를 확인했습니다. 32는 변경 0건으로 새 commit을 만들지 않았습니다. 게임 10개 작업본의 branch·HEAD·기존 변경·index를 보존하며 91·98의 기존 로컬 관리 문서에서 중앙 게시 경로 문구만 보완했습니다. 이 두 미게시 문서는 staging·commit·push하지 않았습니다. 31의 최종 종료 기록은 별도 문서 commit으로 연결합니다.

## 5. 미실행과 후속

게임 구현·자산·DB·빌드·기동·실행 환경·운영 적용·force push·branch 삭제·config·system/plugin은 범위 밖입니다. fact-check 로컬 적용 보류와 미확인 기능 상태를 유지합니다. 새 세션 암시적 발견·선택·행동과 원격 CI는 이번 정적 검사·설치·원격 SHA 확인으로 완료 처리하지 않습니다. 일반 작업은 필요한 검사와 기존 짧은 기록으로 마감하고 반복 사용자 검증·상세 폴더·전체 조사를 상시 요구하지 않습니다.

## 6. 복구

private의 before 전체 사본·해시·index·refs와 after 결과를 대조해 이번 담당 변경만 복구합니다. 로컬 사용자 차이를 유지하고 게시된 수정은 검토한 revert로 복구합니다. 과거 승인이나 보호 규칙 우회를 복구 권한으로 재사용하지 않습니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
