# P0 실행 및 검증 기록

## 1. 변경 범위

2026-09-21 사용자 요청으로 모델별 subagent 위임과 P0 구현을 진행했습니다. `gpt/`와 `kiro/` 원본은 수정하지 않았습니다. 이 기록은 전체 배포 release 인증이 아닙니다.

- 원본 복사: gpt 파일 62개를 codex에 복사하고 즉시 `diff -qr gpt codex`가 종료 코드 0임을 확인했습니다.
- 출처: [BASELINE_MANIFEST.json](BASELINE_MANIFEST.json)에 출발 commit·원본 Git 상태의 범위·파일별 SHA-256·복사 검증과 의도적인 후속 변경을 기록했습니다.
- 이식 시작: codex의 AGENTS·README만 개발 및 설치 경계에 맞게 변경했습니다. 과거 skill·agent·정책·작업 이력은 보존했습니다.
- 최소 payload: [개인 공통 지침](payload/personal/AGENTS.md)을 새로 작성했습니다. 다른 원본 저장소·개인 경로·필수 보조 문서 참조가 없습니다.
- 프로젝트 적용: 저장소 루트 AGENTS.md에 원본 보존·TODO 위임·배포 경계만 두었습니다. 개인 공통 지침이 로드되면 본문을 다시 읽지 않습니다.
- 개인 적용: 실행 사용자 `siasia`의 기본 Codex home에 AGENTS.md를 승인 절차로 신규 설치했습니다. 기존 AGENTS·override는 없었으며 모델·권한·승인 설정은 변경하지 않았습니다.

## 2. 위임과 결과 통합

- Terra 요청: `gpt-5.6-terra`, `medium`, agent `01a0c353-4e4f-7ee2-9e83-729f04b73598`. SE 파일럿 절차를 작성하고 문서 검사를 수행했습니다.
- Sol 요청: `gpt-5.6-sol`, `high`, agent `01a0c356-d777-7060-82c7-b9b0844ceee4`. 권한·배포 경계 검토에서 차단 이슈는 없었습니다. 시험 조건 고정 및 baseline 증거 명확화 의견을 주 agent가 반영했습니다.
- Luna 요청: `gpt-5.6-luna`, `medium`, agent `01a0c359-2877-7202-af6a-f3928f5218eb`. 격리 fixture에서 세 합성 사례를 실행했습니다.
- 주 agent는 파일 통합, 출처·해시·형식 검사, 실제 로딩 진단과 fixture 재확인을 수행했습니다. 위 모델명은 요청값이며 서버 내부 모델 식별자나 사용량은 별도 제공되지 않았습니다.

## 3. 로딩과 설치 증거

- 실행 계정: `siasia`(UID 1006), passwd 홈 `/home/siasia`, `CODEX_HOME` 미설정, CLI `0.155.1`입니다.
- 설치 위치: `/home/siasia/.codex/AGENTS.md`. 설치 전 해당 파일·심볼릭 링크·AGENTS.override.md가 없음을 확인했고 신규 생성만 수행했습니다.
- payload와 설치 파일 SHA-256: `cb24b8f0281382ea8fbf90075290cb98b5756b1d80338d9e509ef498159d28f7`입니다.
- 명령: `codex -C <경로> debug prompt-input 'SE instruction loading check only'`. 전체 prompt를 저장·출력하지 않고 JSON에서 지침 포함 여부만 확인했습니다. 모델 호출은 하지 않았습니다.
- 최초 sandbox 실행: 홈의 실행 상태 기록이 read-only 제한으로 실패했습니다. 지침 오류로 처리하지 않고 동일 진단을 승인 절차로 재실행했습니다.
- 개인 설치 전 격리 경로 `/tmp/se-pilot.l459bA`: 프로젝트 fixture의 공통 지침 로딩 성공, 저장소 전용 규칙 미포함입니다.
- 개인 설치 후 저장소 루트: 공통 지침 1회·저장소 전용 규칙 포함, 종료 코드 0입니다.
- 개인 설치 후 빈 경로 `/tmp/se-global-load.OuP66y`: 공통 지침 1회·저장소 전용 규칙 미포함, 종료 코드 0입니다. 원본 저장소 밖에서도 공통 지침이 로드됨을 확인했습니다.

## 4. 시험 및 정적 검증

- [파일럿 절차](../agent-workflows/gpt/SE_PILOT.md)와 [Luna 실행 결과](../agent-workflows/gpt/SE_PILOT_RESULTS.md)를 구분합니다.
- 정상 문서 변경: 오타 1곳 수정과 세 Markdown 검사 종료 코드 0입니다. 주 agent도 변경 내용·검사를 재확인했습니다.
- 합성 실패: 최초 probe 7, 대체 probe 0을 구분해 기록했습니다. 대체 성공은 최초 검증의 통과가 아닙니다.
- 실제 읽기 실패: 대상 2개 중 성공 1개·PermissionError 1개·probe 종료 코드 2입니다. 주 agent도 같은 fixture의 읽기 실패를 재확인했습니다.
- 최초 원본 파일 62개의 현재 SHA-256이 baseline과 동일합니다. 복사본 기존 파일의 변경은 manifest에 선언한 AGENTS·README 2개와 일치합니다.
- agent TOML 10개 파싱 및 필수 name·description·developer_instructions 확인을 통과했습니다. 실제 역할별 위임·권한 동작 시험은 아닙니다.
- 전체 복사본 헤딩·로컬 링크 검사를 실행했습니다. 새 문서는 별도 스타일 검사 대상이며 원본 복사 문서의 기존 스타일 이슈가 모두 해결됐다고 주장하지 않습니다.
- 최종 검사: 신규·수정 문서 9개의 스타일 이슈 0건, codex와 루트·파일럿 문서 58개의 헤딩 이슈·깨진 로컬 링크 0건입니다. 추적 파일 diff 및 신규 작성 파일의 공백 검사를 통과했고 codex에서 Gitleaks 탐지 0건을 확인했습니다.
- Terra의 [자산 정적 검토](ASSET_REVIEW.md)는 35개 전체 경로를 포함함을 주 agent가 재확인했습니다. 후보 분류와 실제 런타임 검증은 구분합니다.

## 5. 남은 범위와 복구

- 세 합성 사례의 결과 보고 검증과 CLI 로딩은 확인했습니다. 모든 클라이언트의 메시지 표시 순서·사용자 체감·장기 운영·토큰 A/B 비교는 미검증입니다.
- 전체 skill·agent 이식, hook 활성화, 30·31 변경, 전체 consumer 배포·복구는 미완료입니다.
- 개인 설치는 신규 파일 한 개입니다. 복구 시 설치 hash와 현재 내용을 비교하고 사용자 후속 수정이 없을 때 그 파일만 격리·제거하는 절차를 사용합니다. 기존 config·skills·agents는 복구 대상으로 삼지 않습니다.
- 저장소 루트 AGENTS도 신규 파일입니다. 후속 변경을 확인한 뒤 이번 추가분만 복구하며 전체 Git reset을 사용하지 않습니다.
- 임시 fixture는 재현 자료로 남겼으며 blocked.md의 mode 000은 의도적인 시험 상태입니다. 운영 파일의 권한은 변경하지 않았습니다. fixture 권한 복구 시험은 별도 항목입니다.

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-21

© 2026 siasia86. Licensed under CC BY 4.0.
