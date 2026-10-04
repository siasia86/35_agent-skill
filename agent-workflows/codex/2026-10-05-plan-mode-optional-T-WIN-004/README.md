# T-WIN-004 계획 모드 필수 조건 해제

## 1. 변경과 범위

2026-10-05 사용자가 실제 Plan 모드 미반영으로 계획 작성이 중단된 결과를 확인하고, Plan 모드 없이 진행하도록 명시했습니다. [개인 지침](../../../codex_windows/AGENTS.md), [planning skill](../../../codex_windows/skills/planning-and-breakdown/SKILL.md), [work-rules](../../../codex_windows/skills/work-rules/SKILL.md)와 [동봉 planning 참조](../../../codex_windows/skills/work-rules/references/skills/planning-and-breakdown.md)에 이를 반영합니다.

planning-and-breakdown 사용은 유지하고 Plan 모드는 선택 사항으로 변경합니다. Default에서도 요청 범위의 계획·문서 작업을 진행하며 모드 전환만을 이유로 중단하지 않습니다. 실제 Plan 모드 제한과 사용자 읽기 전용 범위는 유지합니다. 계획 작성만으로 Goal·구현·게시의 승인을 확대하지 않습니다. [이전 필수화 기록](../2026-10-05-plan-mode-T-WIN-004/README.md)은 당시 이력으로 보존하며 현재 수행 기준은 이번 변경을 따릅니다.

## 2. 보존·검증·적용

변경 전 두 skill 전체 53파일의 원본·설치본 차이 0건을 확인하고 전체 사본·해시·개인 AGENTS·config를 Git 제외 private/before에 보존했습니다. 개인 AGENTS는 지정 문구만 병합하여 로컬 추가 내용을 유지합니다. 원본·설치본 두 skill의 구조 검사와 담당 Markdown 5개의 링크·헤딩·표현 검사를 통과했습니다. 개인 지침/skill에는 기존 푸터 비강제 기준을 적용했습니다. 지정 두 skill 전체 53파일의 설치 해시 일치, 개인 AGENTS의 추가 내용·config 불변과 COMPAT 밖 역사 본문의 byte 보존을 확인했습니다. 기존 검증 의존성을 재사용했고 패키지는 설치하지 않았습니다.

의미 검토는 Default의 계획 작성, 실제 Plan의 제한, 읽기 전용 요청, 승인된 문서 반영, 명시 요청 없는 Goal 생성 제외를 기준으로 수행합니다. 실제 모드를 변경하거나 새 세션 자동 선택을 확인했다고 보고하지 않습니다. 중앙 정책과 다른 skill·설정은 변경 범위 밖입니다.

## 3. 복구와 인계

복구 전 현재 파일과 after 해시를 대조하여 이후 변경을 보존합니다. private/before의 지정 skill과 개인 AGENTS 해당 문구만 선택 복원 또는 병합하며 config·다른 skill을 일괄 덮어쓰지 않습니다. 공개 원본 복구는 검토한 담당 revert로 수행합니다. 원격 SHA는 private 기록과 완료 보고에서 연결합니다.

계획 담당에는 모드 대기 조건을 해제하고 확보한 조사 결과를 재사용하여 기존 계획안·배정안·Goal 인계문 작성부터 이어가도록 전달합니다. 실제 기능 Goal 실행과 Migration·최적화 구현은 기존 승인·담당 확정 절차와 구분합니다.

---

**작성일**: 2026-10-05

**마지막 업데이트**: 2026-10-05

© 2026 siasia86. Licensed under CC BY 4.0.
