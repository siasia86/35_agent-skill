# 개인 Codex 현황 검증

## 1. 확인한 사실

2026-09-30 사용자 요청으로 standalone 네 skill을 설치했습니다. [runtime_inventory.json](pc01_codex-app-home/runtime_inventory.json)의 파일 목록과 SHA-256은 고정 원본 commit 및 실제 개인 설치 폴더와 일치합니다. 설치 대상에 기존 네 폴더가 없었고 setup dry-run 후 선택 설치를 수행했습니다.

짧은 개인 AGENTS를 새로 작성했고 payload 개인 AGENTS·custom agent TOML·중앙 governance는 설치하지 않았습니다. 기존 config.toml은 변경하지 않았습니다. 로컬 receipt는 비공개로 유지합니다.

## 2. 저장소 검사와 게시

변경 Markdown 5개의 style·heading·로컬 링크, 원본과 설치 파일 inventory·해시 검사를 통과했습니다. 전체 저장소 Gitleaks v8.30.1 파일 검사에서 leak 0건이며 diff whitespace 검사를 통과했습니다. JSON·교차 앵커·게시 후 원격 SHA 일치의 최종 결과는 작업의 로컬 검증 receipt에 기록합니다. payload·catalog를 변경하지 않았다는 diff 범위도 확인합니다.

31은 저장소별 설정·선택의 중앙 원본이고 이 관찰 JSON을 deployment profile로 사용하지 않습니다. 사용자가 하위 게임 저장소 설정 적용을 보류했으므로 해당 파일은 설치·변경하지 않습니다. 최초 게시 대상은 작업 브랜치였고 이후 명시적 사용자 요청에 따라 이번 main 병합·일반 push를 추가합니다. [루트 CHANGELOG](../../CHANGELOG.md)의 이번 요청 기록을 따르며 integration·release·운영 배포는 포함하지 않습니다.

이번 원격 CI API 조회는 404 응답으로 미확인입니다. 로컬 검증과 원격 main SHA 일치를 구분해 기록하며 CI 통과로 보고하지 않습니다.

## 3. 최초 설치 시 검증 한계와 다음 관찰

최초 설치 관찰에서는 skill의 새 세션 발견·자동 선택·대표 작업 행동, 개인 AGENTS의 자동 로딩, named agent 위임과 중앙 runtime은 미검증입니다. 설치된 skill이 모든 실행에서 읽혔다고 보고하지 않습니다.

현재 현황은 동일 Windows 사용자 범위의 관찰입니다. 다른 계정·기기·cloud 상태나 실행 중 transient subagent 전체는 포함하지 않습니다. 이후 생성·설치·수정·제거가 있으면 재관찰해 확인일과 상태를 갱신합니다. 자동 동기화·drift 알림은 아직 구현하지 않았습니다.

## 4. 개인 홈 경로 사본과 현행 안내 정리

2026-09-30 후속 요청으로 `pc01_codex-app-home` 별칭과 실제 사용자 홈 상대 경로를 사용합니다. 네 skill의 실제 설치 폴더·고정 Git 원본·게시 사본의 전체 파일 집합과 bytes를 대조합니다. 줄바꿈 변환으로 관찰 해시가 바뀌지 않도록 사본 경로의 Git attributes를 고정합니다.

현재 세션의 available-skills metadata에서 네 이름과 설치 경로가 확인되어 발견 상태만 관찰 완료로 갱신합니다. 모든 세션 자동 로딩·자동 선택·대표 행동 검증이나 실제 개인 AGENTS 로딩 시험 완료를 뜻하지 않습니다.

기존 `codex/windows_game_governance`의 현행 JSON과 검증 본문을 이곳으로 통합하고 이전 README는 연결 안내로 유지합니다. 과거 설치·작업 branch·main 병합 기록은 위 절과 Git 이력에 보존합니다. 본문은 skill 사본, README는 진입 안내, JSON은 관찰 경로·해시·상태를 관리합니다.

변경 Markdown 11개의 style·heading·로컬 링크, 숨김 사본 네 폴더의 고정 Git 원본/실제 설치/사본 inventory·bytes·SHA-256, JSON과 31 개인 참조 9개를 검사해 통과했습니다. 31·35 변경 문서의 교차 앵커 35개에서 이슈 0건이며 두 저장소 전체 Gitleaks v8.30.1 파일 검사와 diff 검사도 통과했습니다. 게임 저장소 9개의 Git 상태·기존 AGENTS/override와 개인 AGENTS 해시가 작업 전과 같음을 확인했습니다. 원격 CI·운영 적용·중앙 runtime 검증은 미확인 또는 미실행으로 유지합니다.

게시 전 재검사에서 개인 config.toml의 해시가 작업 시작 시점과 달라졌습니다. 이번 작업의 파일 쓰기는 중앙 저장소와 로컬 검증 자료에만 한정했고 개인 홈에는 쓰지 않았습니다. 변경 원인은 조사하지 않았으며 현재 설정을 되돌리지 않고 보존합니다. 개인 설정의 기간 중 변경 관찰과 이번 작업의 설정 미수정을 구분하고 설정 본문·개인 해시는 게시하지 않습니다.

사용자는 이번 정리 결과를 새 branch 없이 31·35 main에 직접 commit·일반 push하도록 명시했습니다. 범위는 중앙 파일 사본·관리 metadata·진입 안내와 검증 기록이며 게임 저장소 적용·개인 재설치·config 변경·release·보호 정책 변경은 포함하지 않습니다. 게시 후 복구는 이번 변경 commit의 검토된 revert로 수행하고 runtime 파일은 건드리지 않습니다.

---

**작성일**: 2026-09-30

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
