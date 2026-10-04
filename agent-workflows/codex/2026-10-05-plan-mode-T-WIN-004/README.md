# T-WIN-004 실제 계획 모드와 planning skill 필수화

## 1. 요청과 적용 범위

사용자의 2026-10-05 요청에 따라 PLAN·TODO 생성·계획 내용 재작성은 실제 계획 모드와 planning-and-breakdown을 함께 사용합니다. [개인 지침](../../../codex_windows/AGENTS.md), [planning skill](../../../codex_windows/skills/planning-and-breakdown/SKILL.md), [work-rules](../../../codex_windows/skills/work-rules/SKILL.md)와 그 [동봉 planning 참조](../../../codex_windows/skills/work-rules/references/skills/planning-and-breakdown.md)를 수정합니다. 기존 T-WIN-004의 계획 수행 기준 보완이며 기능 상태나 Goal은 생성하지 않습니다.

실제 모드 전환이 확인되지 않으면 사용자에게 계획 모드 전환을 요청하고 읽기 전용 조사만 진행합니다. 일반 모드의 계획 작성이나 메시지 전달을 실제 모드 전환으로 보고하지 않습니다. 계획 모드에서는 채팅 계획안을 검토하고, 승인된 문서 반영은 실행 가능한 모드에서 수행합니다. 기존 TODO의 상태·검증 근거·다음 행동 갱신만 하는 일상 기록은 별도 계획 수립으로 취급하지 않습니다.

필수 skill이 없으면 동봉 지침은 조사 참고로만 사용하고 실제 skill 사용 완료로 보고하지 않습니다. 자동 설치하지 않습니다. 이미 승인된 계획의 파일 반영을 위해 같은 계획 검토나 승인 질문을 반복하지 않으며 Goal·구현·게시의 기존 승인 범위를 구분합니다.

## 2. 보존·검증·설치

원본·설치본 work-rules와 planning-and-breakdown 전체 53파일의 차이 0건을 확인하고 두 전체 폴더·개인 AGENTS·설정을 Git 제외 private/before에 보존했습니다. 개인 AGENTS는 지정 PLAN/TODO 문구만 병합하여 설치본의 추가 내용을 유지합니다. source의 COMPAT 밖 역사 본문은 보존합니다.

의미 검토에서 실제 Plan 모드·Default 모드·필수 skill 미설치·승인 후 문서 반영·일상 상태 갱신의 경계를 확인했습니다. 원본 및 설치본 두 skill의 구조 검사, 담당 Markdown 5개의 파일 링크·헤딩·표현 검사를 통과했습니다. 개인 지침/skill 네 문서는 기존 푸터 비강제 기준을 적용했습니다. 두 skill 전체 53파일의 설치 후 SHA-256 일치, 개인 AGENTS의 지정 문구 외 추가 내용 보존, config 불변과 COMPAT 밖 역사 본문의 byte 보존을 확인했습니다. 패키지를 설치하지 않고 기존 검증 의존성을 재사용했습니다. 실제 계획 모드 전환·새 세션의 자동 선택·기능 Goal 실행은 문서 검사나 설치 완료로 판정하지 않습니다. 중앙 정책과 다른 skill·모델 설정은 이번 수정 범위 밖입니다.

## 3. 복구와 후속

복구 전 현재 폴더와 이번 after 해시를 비교하여 이후 사용자 변경을 보존합니다. private/before의 지정 두 skill 전체와 개인 AGENTS의 해당 문구만 선택 복원 또는 병합하며 config·다른 skill을 일괄 교체하지 않습니다. 공개 원본은 담당 변경만 검토한 revert로 복구합니다. 게시 SHA는 이번 private 실행 기록과 완료 보고에서 연결합니다.

진행 중 계획 담당에게 최신 사용자 지시를 전달해 Default의 계획안 작성 대체를 철회하고 실제 모드 확인 전 읽기 전용 조사로 한정했습니다. 전달은 실제 협업 모드 변경과 구분합니다. 새 세션에서의 실제 선택·수행은 기존 T-WIN-004 후속에서 확인할 범위로 유지합니다.

---

**작성일**: 2026-10-05

**마지막 업데이트**: 2026-10-05

© 2026 siasia86. Licensed under CC BY 4.0.
