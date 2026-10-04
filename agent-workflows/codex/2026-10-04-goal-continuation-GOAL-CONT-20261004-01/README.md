# GOAL-CONT-20261004-01 목표 실행 skill

## 1. 범위와 원본

사용자 승인으로 [goal-continuation](../../../codex_windows/skills/goal-continuation/SKILL.md)·UI 메타데이터를 작성하고 [work-rules](../../../codex_windows/skills/work-rules/SKILL.md)에 목표 실행 선택 안내를 추가합니다. 현재 제공 목록은 최초 이관 19개와 fact-check·goal-continuation 2개를 구분해 21개로 갱신합니다. 이전 이관·검증 수치는 보존합니다.

공통 skill은 실행 전 대조·같은 Goal 유지·명시 요청 생성·준비된 승인 작업·실패 분석·최소 개입·정확한 상태 판정을 담당합니다. 기능 PLAN·TODO·보류·완료 조건은 각 저장소에 유지합니다. 이 작업에서 실제 기능 Goal·게임·DB·빌드·기동·runtime·다른 채팅 메시지를 실행하지 않습니다.

## 2. 담당·검증·설치

root가 source·목록·기록·설치·검증·게시를 담당합니다. 정형 조회 Luna에 변경 전 파일·해시 대조를 배정했고 대상 안내 작성 agent가 신규 skill을 독립적으로 검토합니다. 위임에 지정한 모델과 정확한 실행 모델 관찰은 구분합니다.

변경 전 work-rules source/installed 각각 44개 파일은 목록·해시 차이 0건이고 goal-continuation source/installed는 없었습니다. 전체 이전본·해시·다른 설치 폴더 목록은 이번 private에 보존합니다. 실제 Python 3.14.8을 확인했으며 global PyYAML 부재는 기존 격리 dependency를 재사용해 공식 quick_validate 두 skill의 통과를 확인했습니다. 새 dependency 설치는 하지 않았습니다.

독립 의미 검토 1회와 검토만 요청·기존 Goal·대기/독립 작업·실패·보류·동시 담당·도구 부재·upstream·Goal 조회 실패·다른 Goal의 가상 요청 10개를 대조했습니다. 기본 호출문의 모호성 1건은 metadata만 보완하고 영향받은 조건을 재확인했습니다. 실제 Goal 생성/실행 검증은 하지 않았습니다.

담당 Markdown 9개의 파일 링크·헤딩과 교차 앵커 14개를 검사했습니다. 표현 검사 종료 코드 1의 원인은 변경 전부터 있던 work-rules 푸터 경고 3건이며 새 결함은 없었습니다. 담당 공개 파일 11개의 비밀값 검사도 통과했습니다. 신규 goal-continuation 2파일·work-rules 44파일을 전체 폴더로 반영하고 source/installed 목록·해시 일치를 확인했습니다. 다른 설치 skill 6개와 개인 AGENTS/config 해시는 보존됐습니다. [validation](validation.json)에 범위와 결과를 기록합니다.

## 3. 게시와 후속

검토한 source·필요 안내·기록 11파일을 main에 commit·일반 push하고 원격 SHA 일치를 확인했습니다. [구현·지정 설치 기록 커밋](https://github.com/siasia86/35_agent-skill/commit/e1f66e54c4cc59e7679670dec85b26c0c5bcc19b)은 `e1f66e54c4cc59e7679670dec85b26c0c5bcc19b`입니다. 이 게시 관찰의 기록 갱신은 별도 문서 커밋으로 남깁니다. 설치 경로에 배치한 사실·파일 해시 일치·새 세션의 자동 발견·실제 선택·기능 실행은 각각 판정합니다.

실제 독립 세션의 발견·선택·목표 행동은 [현행 TODO](../windows/TODO.md)의 같은 ID 후속에 유지합니다. 이 작업의 예시 호출문이나 모의 시나리오로 실제 Goal을 생성하지 않습니다.

## 4. 보존과 복구

이번 private의 before/source·before/installed 전체 사본과 해시로 기존 상태를 보존했습니다. 적용 직전 동시 변경이 없음을 확인하고 검증한 신규 goal-continuation·work-rules 폴더만 반영했습니다. 원본·설치본의 전체 상대 파일 목록과 bytes를 검사하고 다른 설치 skill·개인 AGENTS/config의 해시 보존을 확인했습니다.

복구는 이전본과 현재 사용자 변경을 먼저 대조해 이번 범위만 수행합니다. 원형 사본·개인 경로·검사 로그·모의 입력/결과는 Git 제외 private에 보관하며 공개 기록에는 범위·상대 경로·해시·결과를 남깁니다. 게시 후 복구는 검토된 revert를 사용합니다. system/plugin·다른 skill·모델·config·fact-check 설치 대기는 변경하지 않습니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
