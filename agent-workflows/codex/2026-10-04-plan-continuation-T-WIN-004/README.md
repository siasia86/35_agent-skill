# T-WIN-004 후속 개인 PLAN·TODO 연속 실행 기준

2026-10-04 사용자가 승인한 개인 PLAN·TODO 기본 규칙 상시화의 35 구현 기록입니다. 개인 공통 지침·skill의 관리 원본을 수정하고 지정한 설치본에 반영합니다. 중앙 공통 양식과 Zircon 저장소 문서 재구성의 상태는 각 관리 원본에서 유지합니다.

## 1. 범위와 연결

- 기존 작업 ID: T-WIN-004. [이전 조건별 읽기 갱신](../2026-10-04-personal-routing-T-WIN-004/README.md)과 이번 업데이트를 구분합니다.
- 관리 원본: [개인 AGENTS](../../../codex_windows/AGENTS.md), [planning-and-breakdown](../../../codex_windows/skills/planning-and-breakdown/SKILL.md), [work-rules](../../../codex_windows/skills/work-rules/SKILL.md), [미설치 시 planning 대체 참조](../../../codex_windows/skills/work-rules/references/skills/planning-and-breakdown.md).
- 담당 기록: [Windows PLAN](../windows/PLAN.md), [Windows TODO](../windows/TODO.md), [인계](../HANDOFF.md), 이번 폴더의 inventory·검증 결과.
- 예정 설치 범위: planning-and-breakdown·work-rules 전체 폴더와 개인 AGENTS의 관리 본문. 기존 로컬 전용 경로 안내는 유지합니다.

다른 개인 skill·system·plugin·모델·인증·config는 변경하지 않습니다. fact-check 로컬 적용 보류와 저장소별 기능 상태·운영 적용 경계를 유지합니다.

## 2. 적용 규칙

개인 AGENTS는 PLAN·TODO 생성·재작성에 planning 기준을 적용하도록 연결합니다. planning은 기존 ID·담당·의존성·다음 행동·완료 근거·검증·복구·사용자 개입 조건을 연결하는 기본값을 담당하고 work-rules는 필요한 planning 본문 하나로 이동합니다.

목표 실행 요청 시 준비된 우선순위 작업을 선택하여 승인된 실행·검증·상태 기록 후 다음 작업으로 이어갑니다. 보류·외부 입력 대기는 재개 조건을 남기고 독립 작업을 계속하며, 실패는 증거 보존·원인 분석 후 영향 범위만 재검증합니다. 이미 승인한 범위를 다시 확인하지 않고 자동 판정이 어려운 실제 결정만 묶어 요청합니다.

계획 작성은 Goal 생성·구현·게시의 새 승인이 아닙니다. 문서 완료·기능 완료·게시 완료를 구분합니다. 단순 작업의 전체 자료 재독·빈 문서 생성·고정 주기 추가 승인은 요구하지 않습니다. 중앙 자동 동기화·자동 감시·별도 채팅은 구성하지 않습니다.

## 3. 보존과 차이

변경 전 지정 설치 skill 전체·개인 AGENTS·config와 관리 원본을 Git 제외 private에 보존했습니다. 설치 skill의 source 대비 사용자 차이는 0건입니다. 개인 AGENTS의 관리 본문은 동일하고 로컬 경로 안내만 suffix에 있으므로 비공개 비교 사본에 보존하며 공개 원본에는 복사하지 않습니다.

공개 [이전 inventory](before/inventory.json), [갱신 원본 inventory](after/source-inventory.json), [설치 후 inventory](after/inventory.json)는 상대 파일 목록·bytes·SHA-256과 환경 별칭만 담습니다. 원형 AGENTS·config·절대 경로·차이·raw는 private에 두고 실제 Git 제외를 확인합니다. 이번 기록은 이전 업데이트의 사본과 검증 결과를 덮어쓰지 않습니다. planning의 보존 원문과 지정 범위 밖의 파일은 bytes로 대조합니다.

## 4. 검증과 상태

관리 원본 검사·독립 의미 검토 1회와 지정 설치를 완료했습니다. [검증 결과](validation.json)에 초기 실패·수정한 검사 범위·보존·설치 판정을 함께 기록합니다. 지정 skill 2개 전체 53파일의 source/installed 목록·bytes·SHA-256이 일치하고 개인 AGENTS의 관리 본문·로컬 suffix와 config·다른 개인 skill 48파일을 보존했습니다. 새 세션의 암시적 선택·실제 업무 행동은 미확인입니다.

구조 검사는 system skill-creator의 quick_validate를 사용합니다. PyYAML의 초기 전역 접근은 실패했으며 기존 업데이트의 비공개 격리 dependency로 검증합니다. 전역 Python·system skill·config를 수정하지 않습니다. Markdown 파일 링크·같은 파일 앵커·헤딩·표현·diff를 확인하고, 외부 URL의 도달성과 실제 새 세션의 암시적 선택은 별도 상태로 둡니다.

검증 통과: quick_validate 2개, 변경 Markdown 8개·파일 링크 99개·헤딩 83개, 활성 스타일·diff 검사입니다. 폴더 단독 활성 참조는 planning 8문서·10링크, work-rules 34문서·61링크가 통과했습니다. 기존 비교 사본 linux-original의 옛 상대 링크 10건과 원래 무푸터 4파일의 12진단은 baseline과 동일하게 보존했습니다. 링크 필터 -X 미지원 호출은 종료 코드 2로 보존하고 명시 파일 목록으로 수정했습니다.

대표 판단은 계획만 작성, 준비된 작업 연속 진행, 외부 입력 대기와 독립 작업, 검증 실패의 원인 분석, 기존 사용자 보류와 실제 개입 조건을 정적으로 검토했고 독립 의미 검토에서 새 문제는 없었습니다. 정적 판단 검토를 새 Codex 세션의 발견·자동 선택·실제 업무 행동 성공으로 처리하지 않습니다.

## 5. 복구와 다음 행동

독립 검토 후 승인된 설치 범위만 반영하고 source/installed 파일 목록·bytes·SHA-256을 대조했습니다. 게시 전 변경·검증을 재확인하고 검토한 담당 파일만 main에 commit·일반 push합니다. 원격 SHA·commit 링크를 기록하며 보호 규칙을 우회하지 않습니다.

복구 시 현재 설치본과 적용 후 inventory를 먼저 대조하여 이후 사용자 변경을 보존합니다. private의 이전 지정 전체 폴더와 개인 AGENTS를 선택 복원하거나 해당 변경을 병합합니다. 이번에 변경하지 않은 config·다른 skill은 일괄 복원하지 않습니다. 게시 후 관리 원본 복구는 검토된 revert를 사용합니다.

로컬 설치는 완료했습니다. 게시 결과는 아래 후속 확인에 기록하며 새 세션 암시적 행동·게임 구현·빌드·기동·DB·운영 적용은 미실행입니다. 새 세션 적용 확인은 Windows TODO의 기존 T-WIN-004 후속에 유지합니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
