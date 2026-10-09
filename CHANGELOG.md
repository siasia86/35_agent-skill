# Changelog

`35_agent-skill`의 주요 변경 사항을 기록합니다.

## [Unreleased]

- `FC-20261004-03·FCH-01`의 [53 문서 변경분 검증 결과](agent-workflows/codex/2026-10-05-fact-check-native-FC-20261004-03/FACTCHECK-53-DELTA-20261009.md)와 JSON을 인수했습니다. 15개 주장 중 확인 14·불일치 0·미확인 1 및 `V-D02` 한계를 공통 기록에 연결하고, 저장 계산 결과·소유 보고·실제 제품 검증의 범위를 구분했습니다.

- `T-WIN-004` 일반 완료·중단·인계 보고의 결론·결과물·4열 상태·다음 행동·실제 도구·토큰·시간 순서를 STYLE에 통합하고 SKILL의 연결을 정리했습니다. [원본·지정 설치·검증 기록](agent-workflows/codex/2026-10-09-report-format-T-WIN-004/README.md)에 측정 근거·집계 범위와 미제공 기준, 기존 실패·미검증을 연결했습니다.

- `T-WIN-004` 개인 상황보고를 `status-report`로 분리하고 AGENTS·skill 목록·일반 작업 보고 경계를 정리했습니다. [변경·설치·관찰 기록](agent-workflows/codex/2026-10-09-status-report-T-WIN-004/README.md)에 최초 실패와 한정 관찰, 미해결 검증 조건을 보존하고 Windows TODO·공통 HANDOFF에 총괄의 후속 배정 대상을 연결했습니다.

- T-WIN-004 / ZWS-TECH-20261005-01: 저장소 유무와 관계없는 지속 작업의 개인 work-rules 적용 안내와 보고 순서·첫 열 대표 상태·4열·행동 표시 예외를 보완한 원본 및 지정 로컬 적용 근거를 인수했습니다 — [변경·검증·복구](agent-workflows/codex/2026-10-09-report-visibility-T-WIN-004/README.md). 새 문맥의 자동 선택·전체 담당 행동은 미확인으로 유지합니다.

- T-WIN-004 / MD-LUNA-20261009-01: 정해진 검사·단순 스크립트·확정된 기계적 수정의 Luna `medium` 기본 위임을 총괄을 포함한 모든 역할에 적용하도록 원본을 갱신하고 지정 로컬 적용 근거를 인수했습니다. 의미·승인·게시 책임은 소유/통합 담당에게 유지합니다 — [변경·검증·복구](agent-workflows/codex/2026-10-09-markdown-luna-T-WIN-004/README.md). 공식 `quick_validate` 미확인과 부분 구조 확인을 구분합니다.

- 2026-10-04: FC-INSTALL-20261004-01에서 사용자 승인으로 fact-check 설치 보류를 해제하고 관리 원본 두 파일을 개인 스킬 경로에 적용했습니다. 전체 사본·source/설치본 해시·형식 검사와 기존 개인 스킬 101파일·설정 보존을 확인했습니다. 새 Luna 실행 문맥의 제공 목록 발견과 실제 호출 미실행을 구분합니다. [적용·검증·복구](agent-workflows/codex/2026-10-04-fact-check-install-FC-INSTALL-20261004-01/README.md).

- 2026-10-04: FC-20261004-03에서 명시 source의 공식 출처 시험으로 오류 2건을 최소 수정하고 미확인 1건을 보존했습니다. 통제 반복 시험은 2회에서 종료하고 잔여 오류 1건을 보고했습니다. root가 실제 bytes·로그·source 보존을 대조했으며 순서 이탈·비교 코드 실패와 설치·수신 인수의 미완료를 구분합니다. [후속 검증·02 반환안·복구](agent-workflows/codex/2026-10-04-fact-check-followup-FC-20261004-03/README.md).

- 2026-10-04: T-WIN-004 후속으로 정형 추출·자료 판단·계획·최종 설계의 모델 배정과 단일 통합 창구·계획 담당 분리를 보완했습니다. 지정 두 skill 53파일 및 개인 지침을 보존·병합·검증했고 설치본 해시 일치와 다른 skill/config 보존을 확인했습니다. 새 세션 암시적 선택·실제 분담·모델 성능 실측은 별도 미확인입니다. [검증·설치·복구](agent-workflows/codex/2026-10-04-orchestration-T-WIN-004/README.md).

- 2026-10-04: GOAL-CONT-20261004-01에서 공통 goal-continuation과 UI metadata를 작성하고 work-rules의 목표 실행 선택 안내·현재 제공 목록을 보완했습니다. 독립 의미 검토·가상 요청 10개 대조 후 지정 두 폴더 46파일을 반영하고 해시 일치와 다른 설치본·개인 설정 보존을 확인했습니다. 기존 Goal·승인·보류·실제 도구 계약을 유지하며 실제 Goal 실행·새 세션 선택은 미확인입니다. [검증·지정 설치·게시·복구](agent-workflows/codex/2026-10-04-goal-continuation-GOAL-CONT-20261004-01/README.md).

- 2026-10-04: BRANCH-POLICY-20261004-01에서 일반 main 작업·게시와 조건부 agent/task 브랜치, 목적 브랜치·기존 변경 보존을 개인 AGENTS·skill 4개 source 폴더의 관련 본문·참조와 35 지침에 반영했습니다. 원본 검사 후 로컬 두 skill 62파일·개인 게시 규칙 1줄을 적용하고 다른 설치본·외부 config 변경·fact-check 대기를 보존했습니다. 새 세션 행동·원격 CI는 미확인입니다. [범위·검증·설치·복구](agent-workflows/codex/2026-10-04-main-branch-policy-BRANCH-POLICY-20261004-01/README.md).

- 2026-10-04: MAIN-20261004-01에서 사용자 main 요청에 따라 LC-PUB·UA-MIN·fact-check 생성/보완 4개 커밋을 main에 fast-forward·일반 push하고 원격 SHA를 확인했습니다. 확인된 모순·의도 불일치 없음, 로컬 적용 보류와 미검증 항목 유지, checkout 줄바꿈 차이 9개 복구를 기록합니다. [병합·검증·복구](agent-workflows/codex/windows/records/2026-10-04-main-MAIN-20261004-01/README.md).


- 2026-10-04: FC-20261004-02에서 `fact-check`에 대상 문서의 새 내용·수식 추가 금지, 실제 도구 확인, ✅ / ❌ / 🟡 항목별 보고, 오류 diff, 최대 2회 검증·수정·재검증과 최종 집계를 반영합니다. 기존 출처·조건 추가 허용을 제거하고 미확인 내용 보존과 수정 금지를 유지합니다. 로컬 설치는 계속 대기합니다. [보완·검증·복구](agent-workflows/codex/2026-10-04-fact-check-rules-FC-20261004-02/README.md).

- 2026-10-04: FC-20261004-01에서 독립된 `fact-check` 스킬과 UI 메타데이터를 추가합니다. `PLAN TODO $fact-check`로 각 문서 전체의 사실을 검증하고 근거로 확정된 오류를 최소 수정·재검증하며, 수정 금지와 추론 금지를 명시합니다. 최초 이관 19개와 신규 1개의 수치를 구분해 현행 Windows 안내를 갱신합니다. 로컬 적용은 사용자의 대기 요청으로 수행하지 않습니다. [생성·검증·적용 대기·복구](agent-workflows/codex/2026-10-04-fact-check-FC-20261004-01/README.md).

- 2026-10-04: UA-MIN-20261004-01에서 사용자 요청의 테스트·개입 최소화 7개 규칙을 개인 AGENTS 배포 원본에 추가합니다. agent의 선행 검증·최소 사용자 확인·실행 경로/파일명 안내·실패 원인 분석·자율 후속을 명시하며 로컬 차이를 보존해 반영합니다. skill·도구·설정·게임 runtime은 변경하지 않습니다. [범위·검증·복구](agent-workflows/codex/2026-10-04-user-test-minimum-UA-MIN-20261004-01/README.md).

- 2026-10-04: LC-PUB-20261004-01에서 개인 AGENTS와 work-rules·git-commit-rule의 Windows 실행 본문에 작업 완료 후 담당 변경의 yunli commit·일반 push·원격 확인·사용자 commit 링크 보고를 상시 절차로 반영합니다. 읽기 전용·변경 0건, 검증 실패·비밀값·다른 작업 변경, 현재 사용자 제한과 main 별도 승인을 구분합니다. [범위·적용·검증·복구](agent-workflows/codex/2026-10-04-yunli-publication-LC-PUB-20261004-01/README.md).

- 2026-10-04: M12-MAIN-20261004-01 사용자 main 요청에 따라 현재 원문 보존·검증 진입을 보완하고 SMA 이관 및 관리 문서를 통합 검토했습니다. 개인 skill 구현·설치는 변경하지 않았습니다. [검사·기존 제한·게시 확인](agent-workflows/codex/windows/records/2026-10-04-main-merge-M12-MAIN-20261004-01/README.md).

- 2026-10-04: SMA-20261004-01에서 이전 작업본의 PCS 백업·PCR 검토를 현행 관리 공간으로 이관하고 과거 PLAN·관찰과 현재 Windows 상태를 구분했습니다. 백업 도구는 개발 검증 경로로 옮기며 업데이트 기본 위치를 유지합니다. [이관·스킬 수정 workflow·검증·복구](agent-workflows/codex/windows/records/2026-10-04-record-relocation-SMA-20261004-01/README.md). 개인 설치·설정과 다른 작업의 변경은 보존하며 Git 게시는 미실행입니다.

- 2026-10-03: 후속 검토를 반영해 work-rules 핵심 53줄·상세/원문 참조 분리, 동봉 link checker 0개 대상 exit 2와 선택 우선순위를 보완. 실제 7개·90파일 일반 읽기·해시와 전후 기록을 재대조하며 중앙의 역사 관찰과 현재 inventory 연결을 구분. [후속 감사](agent-workflows/codex/2026-10-03-personal-skills-T-WIN-003/AUDIT.md).

- 2026-10-03: 두 개인 skill의 호출·원본 연결과 기존 동명 Windows 사용본을 보완하고 업데이트별 전후 백업 폴더·설치 검증·복구 기록을 추가. [T-WIN-003](agent-workflows/codex/2026-10-03-personal-skills-T-WIN-003/README.md).

### Windows 배포 원본의 공통 지침과 관리 기록 — 2026-10-03

- 공통 지침을 codex_windows/AGENTS.md 한 곳으로 이동하고 personal은 설정·비교·홈 적용 안내로 정리했습니다. Windows 사용 안내·현재 tree·기존 이력의 파일 링크를 갱신합니다.
- agent-workflows를 35 자체 개발·검토·적용 기록 공간으로 명시하고 [T-WIN-002 완료 이력](agent-workflows/history/2026-10-03/T-WIN-002-distribution-root.md)에 검증·복구·미실행을 보존합니다. 다른 repo·실제 개인 홈은 기존 상태를 유지합니다.

### 공식 Codex skill 기준 Workflow 보완과 개인 적용 — 2026-10-03

- 현행 공개 plugin source의 SKILL 문서 536개와 이전 skill source·실제 system/cache를 구분하고 [정적 검토·현재 적용 범위](agent-workflows/codex/windows/SYSTEM_SKILL_REVIEW_2026-10-03.md)에 기록했습니다.
- [AI 작업 INDEX](agent-workflows/INDEX.md), work-rules의 선택적 Workflow 참조·동봉 대응, personal 공통 지침에 단일 상태 원본·작업별 결과·경로 예외·기존 승인·도구 계약을 반영합니다. 19개 원문과 기존 작업 기록은 보존합니다.
- 개인 work-rules와 공통 요약의 실제 적용·검증 상태는 위 검토 기록에서 확인합니다. Git 게시는 yunli → 사용자 검증 → main 순서를 유지합니다.

### Windows 구조와 Workflow 안내 — 2026-10-03

- 루트 [codex_windows.md](codex_windows.md)에 현재 tree·복사 사용/개발 기록의 구분·Codex Markdown 인식 방식·문서별 역할·보완안·장단점과 정적 검토 기준을 정리했습니다.
- 현재 배치와 미적용 보완안을 구분하며 기존 skill·설정·작업 문서의 이동이나 실제 홈 적용은 수행하지 않습니다.

### 단순 조회의 Luna 우선 배정 — 2026-10-03

- Windows work-rules와 동봉 역할 2곳, personal AGENTS에 Luna 우선 배정·근거 수집·main AI 검증·지원 여부와 위임 비용 예외를 추가했습니다. 기본 모델·홈·config·중앙 정책은 변경하지 않습니다.
- workflow 문서 구조는 제안만 검토했으며 파일 배치·이동·역할 개편은 수행하지 않습니다. Luna 기준의 범위·검증·한계는 [후속 기록](agent-workflows/codex/windows/REPORTING_REMEDIATION_2026-10-03.md#5-luna-우선-배정-후속)에 구분합니다.

### Windows 공통 보고 지침과 helper 보완 — 2026-10-03

- work-rules·personal AGENTS에 시작/완료 보고, 결과 경로·가시성, 성과/제약, 채팅 `;` 요청 구분 규칙을 반영했습니다. 코드·명령어 등 내용 안의 기호는 원래 의미를 유지합니다.
- W02–W10과 자기 폴더 예시를 보완하고 원문·19개 독립 복사 구성을 보존했습니다. 현재 검사와 미실행은 [보완 기록](agent-workflows/codex/windows/REPORTING_REMEDIATION_2026-10-03.md)으로 연결합니다.
- 중앙 31의 35 정책은 구현 기준으로 정리하며 실제 홈 설치·자동 적용·main 반영과 구분합니다.

### Windows 복사용 구성과 개발 기록 분리 — 2026-10-03

- `codex_windows`에는 19개 skill·동봉 자료·선택적 개인 지침/설정과 사용 안내를 유지합니다. PLAN·TODO·ISSUE·REVIEW와 개발 verification은 `agent-workflows/codex/windows`로 이동합니다.
- 원문·이전 검사 JSON/해시를 보존하고 현재 링크·검증 실행 경로를 연결합니다. 구성 정리와 추가 개선 검토는 [Windows 작업 기록](agent-workflows/codex/windows/README.md)에서 확인합니다.
- 사용자 검증 전 main 반영·개인 홈 설치·운영 적용은 미실행입니다.

### Windows 전체 skill·설정 이관 — 2026-10-03

- Linux19개 skill·182개 출처파일·동봉역할54개와공통설정2개를Windows에대응했습니다. 원문·예시·템플릿·체크리스트를 보존하고 현재Windows실행절·필수도구를작성합니다. 최적화는후속입니다.
- UTF-8·누락입력/오류전파·Markdown문법·잠금부분쓰기·Bash백업·다른drive·단독복사를직접검사했습니다. 공식skill메타데이터19개검사를통과하고symlink/운영/홈적용등미실행을구분합니다.
- [이관 기록](agent-workflows/codex/WINDOWS_MIGRATION_2026-10-03.md)에출처·검증·복구범위를둡니다. yunli게시·사용자검증·main반영순서를유지하며실제개인홈/config·보호원본은변경하지않습니다.

### 개인 skill 내용 검토 — 2026-10-03

- Linux skill 19개의 본문·참조·동봉 도구를 검토해 P1 1건·P2 11건·P3 2건을 기록했습니다. 현재 원문 기준 문제이며 플랫폼 이동의 신규 결함은 아닙니다.
- TEMP에서 누락 입력·백업 실패·lock 부분 쓰기 실패·Markdown 정상 문법의 오판을 확인했습니다. 실제 모델 행동·전체 Linux 회귀·운영 적용은 미실행입니다.
- 상세 근거와 후속 보완은 [skill 검토](agent-workflows/codex/SKILL_REVIEW_2026-10-03.md)에 연결하며 skill 본문·도구·개인 설정은 수정하지 않았습니다. 검토 기록은 yunli 게시 후 사용자 검증을 거쳐 main에 반영합니다.

### Windows Linux 플랫폼 분리 — 2026-10-03

- 기존 codex를 codex_linux로 이동하고 Linux skill 19개·원문·동반 자료·개인 지침·검증 JSON을 보존합니다. 현행 안내와 개발 검증 경로를 새 위치로 연결합니다.
- codex_windows에는 Windows 전용 재작성의 PLAN·TODO·ISSUE·REVIEW와 문서 골격만 준비합니다. 설치 가능한 skill과 Windows 동작 검증은 후속입니다.
- 과거 JSON의 입력 경로·해시·원시 명령·개인 설치 관찰과 보호 원본은 유지합니다. 경로 대응·검증·복구·게시 상태는 [플랫폼 분리 기록](agent-workflows/codex/PLATFORM_SPLIT_2026-10-03.md)에 남깁니다.
- 설정·개인 홈 설치·WSL 설치·release·운영 적용은 수행하지 않고 VERSION 1.0.0을 유지합니다. 검증 후 yunli 게시·사용자 검증을 거쳐 main 반영을 진행하며 사용자 검증 전 main은 유지합니다.

### 보완 변경 yunli 게시와 main 병합 — 2026-10-03

- 후속 사용자 요청으로 보완 변경 59개를 `a010cc7`에 commit하여 yunli에 일반 push하고 main에 fast-forward 병합·push했습니다. 실제 원격 두 SHA 일치와 design 유지를 확인했습니다.
- 원래 로컬 main·yunli와 추적 refs도 같은 커밋으로 정합화하고 파일 498개 bytes·clean 상태를 보존했습니다. 확인 기록의 후속 커밋도 두 브랜치에 반영하며 최종 SHA는 Git refs에서 확인합니다. 근거는 [게시 결과](agent-workflows/codex/REMEDIATION_2026-10-03.md#7-yunli-게시와-main-병합-완료)에 남깁니다.
- force push·release·설치·운영 적용은 수행하지 않았으며 독립 모델 사례·실환경 확인은 미완료로 유지합니다.

### Codex 개인 스킬 동작 보완과 로컬 회귀 검사 — 2026-10-03

- Python parser 범위·원자적 쓰기 메타데이터, Bash 실패 전파, flock 경로 삭제, 중첩 펜스 뒤 링크 누락의 동작 문제 5개를 보완했습니다. Kiro 원문·예시·템플릿·체크리스트는 보존하고 호환 대체 블록과 실행용 검사기 7개에 반영했습니다.
- shipping-checklist의 code-review와 STYLE의 readme-template 참조를 필요한 전체 지침/원문으로 동봉하고 governance 템플릿의 환경 조건을 명시했습니다. 동봉 역할은 54개이며 형제 설치를 요구하지 않습니다.
- 회귀 테스트 16개·CLI 실행 120회와 기본 스킬 검사를 통과했습니다. 원시 입력·명령·종료·파일 해시와 한계는 [보완 기록](agent-workflows/codex/REMEDIATION_2026-10-03.md)에 남겼습니다. commit/push·설치·독립 모델 사례·운영 적용은 수행하지 않았습니다.


실제 개인 홈 설치·세션 발견·Windows·운영 환경과 별도 경량화는 후속 사용자 범위입니다. 저장소 버전 1.0.0의 개인 스킬 모음은 아래에 기록합니다.

### 원격·로컬 main과 yunli 실제 통합 — 2026-10-03

- 사용자가 네 브랜치의 검증 후 실제 병합을 추가 요청했습니다. 원격 main `4227f1d`·yunli `345a6be`, 원래 로컬 main `4227f1d`·yunli `4a5dfb1`의 조상 관계와 로컬 파일의 게시본 bytes 일치를 확인합니다.
- 로컬 refs·index·파일 해시를 백업하고 격리 복사본에서 read-tree와 main fast-forward가 파일을 보존함을 확인했습니다. 기록만 추가한 검증 커밋으로 원격 두 브랜치를 일반 push하고 로컬 두 브랜치와 index를 정합화합니다. design·보존 원본·스킬 구현·runtime·OS 권한은 유지합니다.
- `36cd9d3`의 원격 main·yunli atomic 일반 push와 두 SHA 일치를 확인하고 원래 로컬 main·yunli 및 origin 추적 refs를 같은 커밋으로 fast-forward했습니다. 파일 471개 bytes와 clean 상태, 승인된 문서 6개 외 기존 파일 464개 해시 보존을 확인했습니다. 원래 작업본의 기본 스킬 검사도 통과했습니다. 실제 결과를 담은 후속 기록도 네 브랜치에 반영하고 최종 SHA는 Git refs로 확인합니다.
- 통합 검증과 실제 결과는 MERGE_REVIEW_2026-10-03의 7절 및 four-branch-merge.json에 남겼습니다. 기존 동작 문제 5개와 실환경 검증은 계속 미완료이며 네 브랜치 병합만으로 해결 완료로 처리하지 않습니다.

### 인계 게시와 전체 브랜치 병합 검토 — 2026-10-03

- 사용자 요청으로 미게시 문서·인계·검토 자료를 yunli에 일반 commit·push하는 범위를 적용했습니다. main·yunli·design의 최신 원격 이력을 fetch하고 격리 작업본에서 병합 결과를 확인합니다. 실제 main·design 게시와 원래 root Git 관리 영역 변경은 이번 검토 결과로 처리하지 않습니다.
- main·design에 yunli 밖의 고유 커밋이 없고 fast-forward 병합의 tree가 yunli와 같음을 확인했습니다. Kiro·GPT·과거 개인 설치 사본을 보존하며 인계 변경은 스킬 구현을 바꾸지 않습니다. 기존 payload/catalog/installer 경로의 이력 보존 이동은 1.0.0의 의도한 구조 전환이며, 기존 경로를 사용하는 외부 호출의 호환성은 별도입니다.
- 격리 로컬 사례로 기존 템플릿·검사기의 동작 문제 5개와 동봉 검사기 7개의 영향을 재현했습니다. Luna 기록의 최종 해시 차이·참조 자료 조건도 구분해 MERGE_REVIEW_2026-10-03과 원시 결과·재현 스크립트에 기록했습니다. 구현 보완·새 모델 사례·실환경 검증은 TODO에 남깁니다.
- 게시 후보 검사: 안내 15개의 style·헤딩 161개·파일 링크 151개·앵커 86개에서 오류 0건, 전체 파일 Gitleaks 탐지 0건입니다. 문서 13개 수정과 인계·검토 파일 6개 추가 외 기존 추적 파일 452개를 보존했습니다. Git 관리·게시 결과는 병합 검토의 확인 기록으로 구분합니다.
- 인계·검토 커밋 `525f0e0`의 yunli 일반 push와 원격 SHA 일치를 확인했습니다. main·design은 유지됐으며 새 커밋의 세 브랜치 격리 병합 결과도 같은 tree이고 기본 스킬 검사를 통과했습니다. 실제 게시 확인 기록을 후속 문서 커밋으로 같은 yunli에 남깁니다.

### 세션 재개 인계 — 2026-10-03

- agent-workflows/codex/HANDOFF.md에 마지막 yunli 게시 기록·미게시 문서 12개·추가 검토 후보·다음 세션의 읽기 순서와 완료 조건을 기록했습니다. 루트 AGENTS·README·TODO, Codex README·TODO와 workflow 안내에서 연결합니다.
- 2026-10-02 내용 검토 원시 결과와 문서 범위 검증 JSON을 저장소에 bytes 그대로 보존했습니다. /tmp 경로는 과거 출처로만 남기며 새 세션의 필수 자료는 저장소에서 읽습니다.
- 이번 요청은 인계 문서와 근거 보존입니다. 추가 검토 후보는 재현·판정·보완 TODO로 남기고 기존 원문·스킬 구현·과거 검증 자료·설치 사본을 보존합니다.
- 검증: 문서 8개의 style·헤딩 114개·파일 링크 116개·앵커 30개, JSON 2개의 구문·출처 bytes, 변경 diff·비밀정보 검사를 통과했습니다. 수집한 기존 파일 425개 중 안내 7개 외 418개의 SHA-256과 Git branch·HEAD·index 보존을 확인했습니다. 추가 검토 후보의 구현 수정·새 동작 검증·게시·설치는 수행하지 않았습니다.

### 독립 구성과 환경·작업공간별 적용 기록 — 2026-10-02

- 루트 README·AGENTS에 도구별 구성의 독립 사용 원칙과 작업공간에 적용된 31 설정을 함께 사용하는 조건을 명시했습니다. 구현 원본과 적용·관찰 기록의 관리 위치를 구분했습니다.
- Codex 안내에 개인 홈 공통 설치와 저장소별 설치, 동명 스킬의 비병합·선택 확인, 작업공간별 지침·31 설정·발견·행동 검증을 추가했습니다. 여러 작업공간의 실제 적용 검증은 후속 TODO로 남깁니다.
- agent-workflows와 공통 체크리스트에 공통 설치 기록 참조·저장소별 추가 설치·변경 영향·버전별 관찰 기준을 추가했습니다. 다중 작업공간 기록 구조는 예시이며 과거 설치 사본·JSON·해시는 보존합니다.
- Claude 안내의 기존 31 기반 활성화 조건을 독립 구성과 적용된 31 설정의 조건부 활용으로 정리했습니다. 필수 원본·공개 범위·적용·검증 방법이 확정될 때까지 예약 상태를 유지합니다.
- 검증: 변경 문서 12개의 style·heading 검사, 활성 문서 101개의 파일 링크 339개·앵커 120개 검사, 변경 diff·비밀정보 검사를 통과했습니다. 원본·스킬 구현·검증 자료·과거 설치 사본 423개의 bytes 보존을 확인했습니다. 실제 사용자 환경 설치·다중 저장소 적용·자동 동기화는 실행하지 않았습니다.

### 저장소 목적 안내 정정 — 2026-10-02

- 루트 README의 목적을 각 AI 도구의 특성과 사용 환경에 맞는 에이전트 설정 최적화로 명시했습니다. Agent·Skill·Prompt와 개인 규칙·템플릿·워크플로의 관리 및 적용·업데이트·검증 절차를 포함합니다.
- Kiro 원문 보존과 Codex 호환 이식·경량화 보류 기준은 현재 Codex 개인 스킬 작업 범위로 구분했습니다.

## [1.0.0] — 2026-10-01

### 기존 Codex 개발본 보존과 개인 스킬 구성 전환

- 사용자가 이동한 기존 codex 131개 파일을 105_backup/codex에서 보존하고 이전 Git 원문과 동일한 bytes임을 확인했습니다. REVIEW를 보존본 아래로 이동하고 보존 README에서 명시했습니다.
- VERSION과 루트 README에 저장소 버전 1.0.0을 명시했습니다. 이동 전 루트·Codex README와 기존 개발·설치 기록은 보존합니다.
- 루트 지침·TODO·TODO2·workflow의 현재 안내와 이동된 경로를 정리합니다. 과거 개인 사본·JSON·해시·2026-09-30 관찰은 변경하지 않습니다.
- 이번 요청은 이력 정리 후 yunli 일반 commit·push, 새 개인 스킬 작성·Luna 검증 후 yunli 일반 commit·push를 포함합니다. main·tag·release·다른 저장소·개인 홈·권한 확대는 범위에 포함하지 않습니다.
- 내용 삭제·축약·통합은 하지 않고 Kiro 원문 19개와 필요한 자료를 기준으로 새 스킬을 작성합니다. 경량화는 후속 사용자 검토입니다.

### 원문 보존 개인 스킬 19개와 독립 검증

- codex/skills에 Kiro 스킬 19개의 전체 원문을 유지하고 Codex 호환 절을 추가했습니다. 두 description의 YAML 인용 오류를 고쳤으며 본문·예시·템플릿·체크리스트는 삭제·축약·통합하지 않았습니다.
- 각 폴더에 필요한 전체 로컬 워크플로·STYLE·검사 도구·5축 문서를 동봉했습니다. 원문 비교 사본과 행 대응·SHA-256을 MIGRATION에 기록하고 중앙 catalog·installer·다른 스킬 설치 없이 수동 복사하도록 작성했습니다.
- 우선순위·승인 범위·고정 경로·Kiro hook/memory·README 예외·branch·잠금을 현재 요청과 저장소 지침에 맞게 해석합니다. 잠금 helper의 원자적 획득과 자기 잠금 해제 범위를 실제 검사했습니다.
- Luna(gpt-6-luna 지정)로 19개 격리 사례와 우선순위 추가 사례를 수행하고 실제 산출물을 확인했습니다. YAML·문서 검사 예외·개인 템플릿 누락은 보완 후 필요한 사례를 재검증했습니다. 결과·실패·부분 검사·미실행은 codex/VERIFICATION과 이번 실행 기록에 남깁니다.
- 기존 보안 스크립트 원본/map 명세는 미제공입니다. 설계·수동 점검 지침을 유지하고 동일 실행 도구 배포/복원 호환성은 주장하지 않습니다. 개인 홈 자동 발견·실제 Windows·AWS/운영 적용은 이번 검사에 포함하지 않습니다.
- 이력/버전 정리 `f76d03d`와 새 스킬/검증 `ef438b7`을 yunli에 일반 push하고 원격 SHA를 확인했습니다. main은 `4227f1d`를 유지합니다. 게시 확인 결과는 이번 실행 기록과 별도 문서 commit으로 같은 yunli에 남깁니다.


### 개인 스킬 복제본의 사용 의도 적합성 리뷰 — 2026-10-01

- 사용자 지정 [REVIEW.md](105_backup/codex/REVIEW.md)에 Kiro처럼 복사해 사용하는 개인 스킬 모음이라는 목적을 기준으로 Codex 구성의 잘된 점·잘못된 점·재작성 기준을 기록했습니다. 개인 템플릿의 축약과 사용 안내의 복잡성을, 실제 복사 가능한 구현의 성과와 구분합니다.
- 격리 수동 복사로 16개 스킬·20개 파일·해시 20개·로컬 참조 4개를 확인하고 스킬 16개와 에이전트 TOML 10개의 정적 검사 및 기존 설치 테스트 10개를 통과했습니다. 실제 세션의 발견·호출·개인 워크플로 동등성은 미검증입니다.
- 후속 diff로 같은 이름의 Kiro 스킬 11개가 원문·본문 모두 다르고, 나머지 5개에는 동명 Kiro 스킬이 없음을 확인했습니다. 전체 304개 조합에서도 동일한 원문·본문은 0개입니다. 16개별 결과와 동반 파일·관련 prompt 대조를 리뷰 7.3절에 기록하고, 복사 가능성의 긍정 평가를 파일 구성으로 한정했습니다.
- 기존 Kiro·Codex 파일과 TODO2는 유지하며 이번 요청은 리뷰·변경 이력 작성으로 한정합니다. 폴더 폐기와 개인 설치는 실행하지 않았습니다.

### 개인 Codex 스킬 기본 구조 TODO — 2026-10-01

- 사용자 지정 [TODO2.md](TODO2.md)에 Kiro 기반 Codex 개인 스킬의 기본 구조, 설치 위치, 구성 대응 관계와 단계별 후속 작업·완료 조건을 기록했습니다.
- 현재 Kiro 스킬 19개·Codex 선택 후보 16개·에이전트 후보 10개와 신규 설정 예시 제안을 구분했습니다. 기존 루트 TODO의 배포 상태와 개인 runtime의 설치·발견·동작 검증은 별도로 유지합니다.
- 후속 요청으로 사용자 명시 지시 > 저장소 지침 > 개인 범용 스킬의 우선순위, 원문·예시·템플릿 보존과 이번 이식 단계의 분량 감축 금지를 TODO2 9절에 추가했습니다. work-rules의 호환성·승인·권한·경로·기록 관련 최소 수정과 원문 대응·동작 확인을 완료 조건으로 명시하고, 경량화는 사용자와의 별도 후속 검토로 보류했습니다.
- 마지막 검토에서 삭제 확정 스킬은 없으며 kiro-lock·zircon-readme-policy는 조건부 상시 설치 생략 후보로 구분했습니다. 계획·README·스킬 선택 및 서로 다른 인프라 역할은 유지하고, 잠금 원자성·비활성 의미·호출·환경·문서 부작용의 추가 확인을 TODO2 10절에 기록했습니다. 스킬 구현·설치·삭제·축약은 실행하지 않았습니다.
- 변경 문서 2개의 style·heading·로컬 링크·Gitleaks 검사, 기존 경로 26개와 후보 개수 대조, 후행 공백·diff 검사를 통과했습니다. 개인 설치와 설정 적용은 미실행입니다.

### 개인 홈 경로 skill 사본과 현행 안내 통합 — 2026-09-30

- 사용자 지정 `pc01_codex-app-home` 아래 실제 사용자 홈과 같은 `.agents/skills/<이름>/` 경로로 네 개인 skill의 전체 설치 사본 추가. 재사용 구현 원본은 codex/payload, 환경별 사본은 설치 관찰로 구분하며 같은 사용자 홈의 App·CLI 파일을 중복 관리하지 않습니다.
- README·JSON 중심의 이전 조회 안내를 실제 본문·진입 안내·단일 관찰 metadata 구조로 정리. 현행 runtime inventory와 검증 이력을 agent-workflows/codex로 통합하고 codex/windows_game_governance의 README는 연결 안내로 유지합니다.
- 실제 설치·고정 Git 원본·사본 inventory와 SHA-256을 검증하고 현재 세션의 네 skill 목록 발견을 관찰. 대표 행동·전 세션 로딩·원격 CI·자동 동기화·중앙 runtime·하위 게임 저장소 적용은 완료 처리하지 않습니다.
- 변경 Markdown 11개 style·heading·로컬 링크와 31·35 교차 앵커 35개, JSON·네 사본 전체 bytes·게임 상태 보존·전체 Gitleaks·diff 검사 통과. 31의 새 개인 관찰 참조 9개와 일치하며 게시 후 원격 main SHA는 별도 확인합니다. 재검사에서 개인 config 해시의 기간 중 변경을 관찰했으나 이번 작업은 개인 홈에 쓰지 않았고 현재 파일을 보존하며 원인·본문은 게시하지 않습니다.
- 사용자가 이번 구조 정리 결과를 새 branch 없이 31·35 main에 직접 commit·일반 push하도록 명시 승인. 범위는 중앙 사본·metadata·README/CHANGELOG와 검증 기록이며 개인 설정·payload·catalog·게임 코드·release는 유지합니다. 종료 시 이번 게시 권한은 만료하며 게시 후 복구는 이번 commit의 검토된 revert를 사용합니다.

### Windows 개인 현황 초안의 main 병합 — 2026-09-30

- 사용자가 이번 작업에 한해 31·35 각각 main까지 병합하도록 명시했습니다. 35의 최신 원격 main `4a5dfb1`에서 검증한 개인 현황 초안 `90a189e`와 이번 병합 기록까지 fast-forward하고 일반 push합니다. 이후 main 게시의 상시 권한으로 재사용하지 않습니다.
- 대상은 README·CHANGELOG·Codex 안내와 비식별 설치 현황입니다. payload·catalog·보존 원본·기존 사용자 설정을 유지하며 하위 게임 저장소 설정 적용·integration·release·운영 배포는 포함하지 않습니다.
- 기존 설치·해시 검증과 변경 문서·보안·diff를 확인합니다. 원격 CI API는 404 응답으로 미확인이며 통과로 기록하지 않습니다. 게시 후 원격 main SHA 일치와 시작 commit 보존 여부를 확인하고, 복구는 검토된 revert를 사용합니다.

### Windows 개인 agent·skill 적용 현황 원칙 — 2026-09-30

- README에 agent 환경별 skill 설치·발견·행동 검증을 출처·확인 시점으로 추적하는 원칙 명시. 설치·변경·제거·agent 전용 skill 생성 시 현황 갱신 의무와 실시간 자동 동기화 미구현의 한계를 구분합니다.
- `codex/windows_game_governance`에 비식별 개인 runtime 현황과 네 skill의 설치 파일 해시·원본 commit·발견/행동 상태 추가. 31은 저장소별 설정·선택 원본, 35는 구현·적용 관찰, 30은 실행 구현이라는 책임을 유지합니다.
- 사용자 요청 범위의 Windows 개인 환경에 code-review·debugging-and-recovery·markdown-review·md-link-check 설치 및 원본 파일 일치 확인. 짧은 개인 AGENTS를 추가하고 기존 model·approval·sandbox·MCP·플러그인 설정은 변경하지 않았습니다.
- 새 세션의 skill 발견·대표 작업 행동·중앙 governance 활성화·운영 적용은 미검증 또는 미실행입니다. 개인 경로·계정·config 본문·운영 증거는 원격 현황에 포함하지 않습니다. 기존 payload·catalog·agent TOML·보존 원본은 유지합니다.

### engineer ACL과 세 브랜치 통합 — 2026-09-30

- 사용자 요청으로 이번에 한해 로컬·원격 main·yunli·sjyun을 통합합니다. 기존 변경은 원격 main에 이미 포함됐으며 미커밋 상태를 stash로 보존하고 fast-forward 병합했습니다.
- engineer 쓰기 제한 파일 68개의 ACL과 계정별 Git 신뢰 설정을 보완했습니다. 구성원 5명의 파일·Git 접근, sjyun·yunli의 push 사전 검사와 setup 회귀 10개를 통과했습니다.
- [검증과 복구](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#11-2026-09-30-engineer-acl과-브랜치-통합)를 기록하며 게시 후 SHA 일치로 확인합니다.


### main 병합 일회성 승인 — 2026-09-30

- 사용자가 이번에 한해 게시된 yunli 변경의 main 병합·일반 push를 승인했습니다. main의 `f884f9a`에서 검증한 yunli `42ba33f`까지 충돌 없이 fast-forward 병합하고 이번 승인 기록을 추가했습니다. [병합 범위와 검증·복구](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#10-2026-09-30-main-병합-일회성-승인)를 확인합니다.
- 구현·payload는 기존 검증 commit과 같으며 추가 문서 2개의 style·heading·파일 link·diff 검사를 통과했습니다. 실제 runtime·30·31·release·운영 적용·force push·보호 설정 변경은 제외하며 완료 또는 중단 시 승인이 만료됩니다.



### 검증한 35 변경의 yunli 게시 — 2026-09-30

- 마무리 검사 뒤 사용자가 commit·push를 승인했습니다. 실행 계정 소유 독립 clone에서 검증한 변경과 기록을 `origin/yunli`에 일반 push하며 원격 commit SHA 일치로 확인합니다. [게시 범위와 복구](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#9-2026-09-30-yunli-게시-승인과-절차)를 기록했습니다.
- 아래 commit/push 미실행 문구는 게시 요청 전 검사 상태입니다. 30·31·개인 runtime·main·release·운영 적용은 이번 게시 범위에 포함하지 않습니다.


### Windows clone 결함 수정과 개인 skill 정리 — 2026-09-30

- `.gitattributes`로 payload·catalog·governance template의 LF를 고정하고 core.autocrlf=true 실제 clone 후 setup 설치 회귀를 추가했습니다. 정확한 해시 검증을 유지하며 setup 회귀 10개를 통과했습니다.
- 공식 Codex skill 문서와 skill-creator 기준에 따라 일반 절차·중복/특정 저장소 전용 skill 9개를 설치 목록에서 제외하고 마지막 payload bytes를 archive에 보존했습니다. 검증 절차를 testing-guide로 통합하고 catalog·agent optional 참조·현재 안내를 갱신했습니다. 현재 skill 16개·catalog 27 ID·31파일입니다.
- 문법·참조·해시·보존 bytes·Markdown·diff·비밀정보 검사와 31 companion v1 planner를 통과했습니다. 31 v2 pin 정합화·실제 Windows/runtime·경량화 효과·commit/push는 미실행입니다. [정리 근거](105_backup/codex/WORKFLOW_SKILL_PLAN.md#5-2026-09-30-개인-skill-설치-목록-정리)와 [검증 기록](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#8-2026-09-30-windows-clone-수정과-skill-정리)을 확인합니다.
- 사용자 요청에 따른 마무리 점검에서 추가 결함은 발견하지 않았습니다. setup 회귀 10개, skill 16개·agent 10개 문법, catalog와 실제 payload 31파일의 정확한 inventory·해시·참조, 변경 Markdown 27개와 diff·비밀정보 검사를 통과했습니다. 제외 payload 9개·Kiro 원본 세 파일의 bytes 보존과 31 HANDOFF 패치의 적용 사전 검사를 확인했습니다. 검사 통과를 게시·runtime 검증으로 확대하지 않습니다.


### Linux·Windows 독립 개인 Codex skill setup — 2026-09-30

- README에 계정 홈의 `.agents/skills`로 선택한 payload 폴더 전체를 복사하는 Bash·PowerShell·파일 탐색기 절차와 동반 파일·기존 설치 비교·발견 확인·복구 기준을 추가했습니다.
- Python 표준 라이브러리만 쓰는 [개인 setup](105_backup/codex/scripts/setup_personal_skills.py)의 list·선택/전체 설치·dry-run·catalog 해시 확인·동일 설치 건너뛰기·기존 수정 보존을 구현했습니다. 30·31·네트워크 없이 개인 skill을 사용할 수 있으며 중앙 profile·정책 합성은 별도 계약으로 유지합니다. 실제 sjyun 홈 설치·Windows runtime 검증은 수행하지 않았습니다.

- 초기 setup 단계에서 30·31이 없는 임시 작업본의 설치·재실행·dry-run·사용자 변경·경로/해시/링크 거부·부분 실패 시험 9개를 통과했습니다. 이후 Windows clone 회귀를 추가한 최종 시험 수는 10개입니다. [초기 검증 기록 §7](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#7-2026-09-30-독립-개인-skill-setup)에 당시 검사 범위와 미실행을 남겼습니다.

### 31/35 중복 검토와 후속 agent 인계 — 2026-09-30

- 31 중앙 정책과 35 skill 절차의 반복·역할 분리, AGENTS target 충돌 및 31 후속 실행 순서를 [기존 governance 안내](105_backup/codex/CODEX_GOVERNANCE.md#6-31-담당-agent-인계와-중복-판정)에 기록했습니다. 35 PLAN의 과거 원본 대조 미완료 안내를 날짜별 상태로 정정했습니다.
- template·정책 pin 8개 일치와 companion v1 planner 통과를 확인했습니다. v2 AI profile은 catalog pin 불일치로 거부됐으며 31 정합화·staging 검증을 미완료로 연결했습니다. 31 기존 HANDOFF 보완 패치는 준비·사전 검사했으나 31 원본·profile·manifest·runtime은 변경하지 않았습니다. 상세는 [검증 기록 §6](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#6-2026-09-30-3135-중복-검토와-agent-인계)에 있습니다.


### 최신 Kiro 세 skill 대조와 Codex 보완 — 2026-09-30

- 읽기 가능해진 Kiro md-link-check·repo-governance·work-rules 전체 본문을 현재 HEAD와 대조하고 원본을 보존했습니다. Codex 후보의 검사 범위·코드 예시 제외·정책 발견·필수 정책 실패·권한과 재시도·비밀정보 및 기록 기준을 보완했습니다.
- catalog 36 ID·40파일과 작업별 참조 선택을 유지하고 변경 해시를 갱신했습니다. README의 이전 2개 skill·2개 agent 안내와 현재 Kiro 대조 상태를 정정했습니다.
- skill 25개 문법·agent 10개 TOML·catalog 해시·변경 Markdown·diff·Codex 비밀정보 검사를 통과했습니다. 격리 checker 시험에서 cross-file fragment 누락과 유효한 중첩 코드 예시 오탐을 확인하고 [검증 기록](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md#5-2026-09-30-최신-kiro-세-파일-대조와-보완)에 남겼습니다.
- 실제 runtime·자동 hook·30 checker 구현·31 profile pin·배포 연동·commit·push는 수행하지 않았습니다. 기존 31 pin은 변경된 catalog와 후속 정합화해야 하며 이번 정적 검사를 운영 적용 근거로 사용하지 않습니다.


### sjyun·yunli·main 브랜치 통합 — 2026-09-29

- 사용자가 세 저장소의 개발 변경과 기준 브랜치를 정합화하기 위해 이번 1회에 한해 sjyun·yunli·main 병합·일반 push를 명시적으로 승인했습니다. 계정 소유 독립 clone에서 수행하며 완료·중단 시 예외가 만료됩니다. 이후 main 게시의 상시 권한으로 재사용하지 않습니다.
- 통합 전 원격 기준: sjyun 없음 · yunli 3179f95 · main c30c33f. 기존 각 브랜치의 모든 commit이 최신 yunli에 포함됨을 확인했습니다. 기존 sjyun이 없어 검증한 통합 commit에서 새로 생성합니다. 검증한 결과와 이 기록을 포함한 동일 commit으로 세 브랜치를 fast-forward합니다.
- 검증: 개발·배포 및 보완 열람 문서 40개 style, 이동 보존본 포함 62개 heading·link, 작업본 Gitleaks·diff 검사 통과. 보존본의 기존 서식 지적 64건은 전체 style 통과로 바꾸지 않으며 archive 원본 35개가 이전 main과 동일한 bytes임을 확인했습니다. catalog 36 ID·40파일과 개인·프로젝트 격리 설치·재적용 no-op 검사도 통과했습니다. 원격 브랜치 SHA 일치와 시작 commit 보존 여부로 게시를 확인합니다.
- 기존 사용자 변경·원본·release를 보존하며 보호 설정·자격증명·OS 권한·운영 적용은 변경하지 않습니다. 게시 후 복구는 검토된 revert로 수행합니다.


### 작업 기록 규약과 skill 경량화 — 2026-09-29

- 공통 번호 규약을 따르도록 문서 정책을 연결하고, 기존 Token·품질 비교 항목을 codex/tasks/01_TODO.md로 분리했습니다. 루트 TODO는 링크와 미완료 상태를 유지하고 governance 완료 체크리스트는 기존 CHANGELOG·검증 근거로 연결했습니다.
- work-rules를 작업별 참조 선택으로 바꾸고 Python 코드 골격을 asset으로 분리했습니다. 계획·실행·기존 검사·테스트 설계 skill의 선택 조건을 구분하고 고정 리뷰 횟수·일괄 상태표·중복 승인 요구를 완화했습니다.
- skill 25개·agent 10개·개인 지침 1개의 선택 ID 36개를 유지하며, 참조 3개와 Python 골격 1개를 포함한 전체 설치 후보는 40개 파일입니다. catalog와 31 연동 해시를 함께 갱신했습니다.
- 최종 검토 1회에서 발견한 35 단독 번호 규약·자격증명 비기록·복수 참조 선택 3건을 보완했습니다. 문서·skill·해시·보안 검사와 관련 회귀 54개, 40파일 격리 패키지·7파일 governance 후보 연동을 확인했으며 [작업 기록](105_backup/codex/WORKFLOW_SKILL_PLAN.md)에 결과와 제한을 남겼습니다. 실제 runtime 설치와 경량화 전후 품질·사용량 비교는 미실행이며 후속 TODO로 유지합니다.
- 이번 사용자가 개선·기록 정리·검토 후 push와 yunli 대상을 확인했습니다. 계정 소유 clone에서 작업하며 과거 root 직접 수정 예외를 재사용하지 않습니다.


### 검증한 Codex 개선 패치의 root 반영 — 2026-09-29

- 검증한 변경을 사용자의 해당 작업 1회 승인으로 원래 작업본에 반영하고 f3e29d7로 yunli에 게시했습니다. 당시 원격 HEAD 일치를 확인했으며 해당 직접 수정 예외는 종료됐습니다.
- 기존 사용자 변경과 Kiro/GPT 원본을 보존합니다. 개인 runtime·운영 적용·OS 권한·release·main/integration·force push는 포함하지 않으며 이번 작업 종료 시 예외가 만료됩니다.

### Codex governance 개선 후보 — 2026-09-29

- 계정 소유 독립 작업본에서 35 재사용 진입점·31 공통 및 저장소별 정책·30 생성 도구를 연결하는 별도 draft 구성을 작성했습니다. 기존 독립 payload 25 skill·10 agent·37파일은 유지합니다.
- Codex 보존 자산은 archive로 분리하고 35개 원문 bytes를 유지했습니다. 이동 후 상대 링크 세 곳은 열람본에서 정리하며 해당 원문도 별도로 보관했습니다. 최초 baseline·Kiro/GPT 원본은 유지합니다.
- 문서 계획·배치·개인 Markdown 및 Python 양식과 release 준비의 적용 범위를 현재 저장소·기존 승인 기준에 맞췄습니다. 필수 정책 누락·해시 불일치의 중단 조건과 기존 instruction의 AGENTS 경로 충돌 거부를 명시했습니다.
- 검증 범위·독립 검토·접근 제한은 [검증 기록](105_backup/codex/CODEX_GOVERNANCE_VERIFICATION.md)에 남깁니다. 최신 Kiro 세 skill의 전체 내용 대조는 OS 읽기 권한으로 미완료입니다. 위 독립 작업본 검사 시점에는 root 통합·commit·push를 수행하지 않았습니다. 이후 승인·반영은 위 최신 항목을 따르며 실제 runtime 설치·release는 미실행입니다.


### 게시·병합과 작업본 최신화 마감 — 2026-09-22

- 개발 자산과 후속 TODO를 9fe7fc4로 yunli에 게시하고 main에도 fast-forward로 반영했습니다. 충돌은 없었으며 기존 commit을 보존했습니다. 등록 CI workflow는 없어 로컬 자산·문서·보안 검사 결과를 사용했습니다.
- 사용자가 원래 작업본의 Git 기준을 최신화한 뒤 HEAD·origin/main·origin/yunli가 9fe7fc4로 일치하고 diff·미추적 파일이 없음을 확인했습니다. backup/pre-sync-20260922-35 복구 참조는 유지했습니다.
- 31 PLAN에 8번 pilot → 읽기 중심 위임 정책 정비·영향 범위 재검증 → 9번 release 순서를 연결하고 이 TODO와 정합화했습니다. 현재 agent 권한·runtime은 변경하지 않았습니다.
- 이번 사용자 요청의 범위는 게시 결과 문서 마감·검증 및 yunli commit·push입니다. 종료 시 수정 예외가 만료되며 main 재병합·운영 적용·OS 권한 변경은 제외합니다. 이번 문서 commit 이후 yunli와 main 사이의 문서 차이는 미병합 상태로 구분합니다.

### 읽기 중심 위임 정책 후속 예약과 게시 — 2026-09-22

- 사용자 요청으로 TODO에 단일 작성자·읽기 중심 조사·리뷰·테스트 분석, 기본 2개·최대 3개 위임, worktree별 독립 구현과 최종 통합 기준을 예약했습니다. 기존 구현 위임 정책과의 정합화 및 영향 범위 재검증을 포함합니다.
- 순서는 7번 개발 검증 완료 → 8번 pilot → 위임 정책 정비·재검증 → 9번 release입니다. 이번 게시에서 공통 지침·agent 권한·개인 runtime은 변경하지 않습니다.
- 개발 변경과 TODO를 검증 후 기존 yunli에 9fe7fc4로 commit·push했습니다. release·운영 적용·OS 권한 변경은 수행하지 않았습니다.

### 작업 6 자산 이식과 5~7 연계 — 2026-09-22

- 보존 gpt·kiro·codex 원본 영역은 유지하고 payload를 지침 1개·skill 25개·agent 10개로 확장했습니다. work-rules 동반 참조 1개를 포함해 선택 ID 36개·파일 37개입니다. 개발 후보이며 실제 runtime에 설치하지 않았습니다.
- catalog 0.2-draft에 참조 파일의 source·relative target·SHA-256을 명시하고 30 planner·격리 패키지와 연결했습니다. 개인용·프로젝트용 모두 37개 파일 staging·설치·재적용 무변경을 확인했습니다.
- skill-creator 기준으로 범위·의존성을 정리했으며 개인 규칙을 일반론으로 축약한 초기 후보를 보완했습니다. 독립 검토에 따라 테스트 작성 승인, branch 확인, Python 멱등성, Ansible 상세 검사, masking·restore 불변식, container 검증, 문서 고유 검사와 optional 관계를 복원했습니다.
- 원본 62개 해시는 BASELINE_MANIFEST와 일치합니다. skill 25개 frontmatter와 agent 10개 TOML을 정적 검사했으며 실제 discovery·agent invocation·sandbox·자동 hook 동작을 대신하지 않습니다. Kiro 자동 hook 동등 동작은 명시적으로 보류했습니다.
- 이번 요청의 5~7번 개발·검증 범위이며 8번 실제 환경 pilot과 9번 release·운영 배포는 PLAN으로 남깁니다. Sol 독립 재검토와 합성 요청 3개를 통과했습니다. 30 전체 단위 시험 89개, 최종 catalog 개인·프로젝트 37개 파일 및 31 v2 profile 5개 파일의 격리 연동·재적용 검사를 통과했습니다. 게시 범위는 위 후속 요청 기록을 따릅니다.

### Governance 경로와 과거 기록 구분 — 2026-09-22

- TODO의 현재 manifest 안내를 31 최상위 profiles 경로와 개발 v2 소유권 계약에 맞췄습니다. Batch 4는 과거 검증 기록임을 명시하고 원본 명령·출처는 보존했습니다.
- 사용자 승인한 남은 9개 작업 중 1~4번 연계 정리 범위이며 gpt·kiro 원본과 배포 payload는 수정하지 않습니다. 원본 작업본의 Git 권한은 변경하지 않고 별도 clone에서 검증·게시합니다.

### 삭제 참조·사용자 지침 진입점 정리 — 2026-09-22

- 사용자가 삭제한 Kiro 미리보기 스크립트의 현재 사용 안내와 깨진 링크를 정리하고 ISSUE-1을 현재 작업본 기준 해결로 기록했습니다. 기존 Git 이력은 보존합니다.
- Codex ISSUE-006에 이동된 문서 경로와 현재 계정에서 읽기 가능한 사실을 추가하고 과거 실패·미검증 범위를 구분했습니다.
- Kiro·Claude 하위 README는 OS 쓰기 제한으로 agent가 갱신하지 못했으나 사용자가 지침 링크 4개를 직접 추가했습니다. 검사 후 ISSUE-2를 해결로 기록했으며 소유권·ACL은 유지했습니다.
- 승인 사유는 삭제된 Kiro 스크립트 참조 정리 및 사용자 지침 진입점·이슈 현황 정합성 보완입니다. 후속 사용자 요청으로 관련 문서와 사용자 삭제 변경의 commit·push를 포함합니다. 이번 작업 종료 시 예외는 만료되며 runtime 변경·다른 저장소 직접 수정으로 확대하지 않습니다.

### README 정합성 정비 — 2026-09-22

- 추가 요청에 따라 ISSUE를 정리해 정적 관찰·영향·임시 조치·해결 조건을 기록했습니다. README에서 해결한 설명 문제와 실행 코드·권한·전환 계약의 미해결 문제를 구분했습니다.

- 세 저장소의 역할·연결 흐름을 같은 책임 기준으로 정리하고 현재 구현과 목표 구조·미완료를 구분했습니다.
- 보존 원본·개발 후보·선택 payload·사용자 지침의 경계와 30·31 연결을 명시하고 기존 도구별 지침 링크를 유지했습니다. 검사 범위와 작업 예외·승인 조건을 정리했습니다.
- 사용자 승인 사유: 세 저장소 README의 역할·운영정책·구현 상태 정합성 정비. 이번 요청에 한해 root 작업본의 README·CHANGELOG 및 추가 요청한 ISSUE 수정·검증·commit·push를 허용하며 30·31은 기존 설계 브랜치, 35는 yunli에 게시합니다. 작업 종료·중단 시 예외는 만료됩니다.
- 실행 코드·기존 정책 원본·manifest·운영 환경은 변경하지 않습니다. 보호 브랜치 직접 push·release 승인·권한 확대는 제외하며 게시 후 복구는 검토된 revert로 수행합니다.
- 검증: ISSUE를 포함한 세 저장소의 변경 문서 9개 style·heading·로컬 link 검사, diff 공백 검사, 31 draft manifest 45개 항목·manifest checksum, profile과 자산 5개의 읽기 전용 계획 연동을 확인했습니다. 전체 unit test·Ansible 실행·운영 설치·원격 CI는 이번 문서 작업에서 재검증하지 않았습니다.

### 사용자 지침 구조 정비 — 2026-09-22

- 도구별 USER_TODO·UPDATE_TODO 6개를 kiro/docs·codex/docs·claude/docs의 도구명_SETUP_GUIDE·도구명_UPDATE_GUIDE로 이동·정리했습니다.
- 공통 체크리스트와 SE 시험 기록은 agent-workflows에 유지하고 루트 README의 중복 Kiro 절차·이전 경로를 새 지침 링크로 대체했습니다.
- 공용 지침과 개인 실행 기록, 최초 적용과 선택 유지보수를 구분했습니다. 누락 참조·저작권 고지 자동 삭제와 전체 runtime 복사 안내를 제거했습니다.
- Codex 개발 후보·Claude 예약 상태를 유지하고 docs의 runtime 복사 제외 및 기존 Kiro 미리보기 출력의 chown 주의점을 명시했습니다.
- 사용자 승인 사유는 도구별 사용자 지침 구조 정비이며 이번 문서 변경·검증·commit·push 완료 시 직접 수정 예외가 종료됩니다. 운영 적용·agent·skill·설치 script 변경은 제외합니다.
- 변경 문서 12개의 스타일·헤딩·로컬 링크 검사와 diff 공백 검사를 통과했습니다. 설치·runtime 동작 시험은 수행하지 않았습니다. Kiro·Claude 하위 README는 파일 권한 제한으로 보존하고 루트 README와 공통 인덱스에서 새 지침을 연결했습니다.

### Governance design checkpoint — 2026-09-22

- gpt 원본 62개를 보존한 codex 개발본과 최초 출처·해시 기록을 작성했습니다.
- 최소 SE 공통 지침·저장소 지침을 마련하고 개인 지침 설치·CLI 로딩·합성 명령 결과를 확인했습니다. 설치 지침의 행동 수용·사용자 체감은 미완료로 구분했습니다.
- skill 25개·agent 10개의 정적 검토 후 fact-check·markdown-review와 reviewer·docs_reviewer를 별도 payload로 준비했습니다. 검토 시 자동 수정·Python 캐시 부작용 등 관찰된 문제를 보완하고 시험했습니다.
- 자산 5개의 목록·해시·설치 매핑, 비민감 로딩 판정과 Batch 2·4 검증 기록을 추가했습니다. 31 profile·30 읽기 전용 planner와 연동했으며 운영 실행기로 간주하지 않습니다.
- TODO에 중앙 설정 소유권, 설치·검증·활성화 분리, 개발·테스트 전체 권한 계획과 운영 실행 제한을 반영했습니다. 직접 명령 예외·운영 기록 위치는 미결정입니다.
- 이번 구조 설계 통합·기록·push에 한한 직접 수정 예외와, 이후 타당한 이유 없는 제한 해제는 수행하지 않는 지침을 추가했습니다.
- 30·31 기준 작업본에 계정 clone의 변경 부분을 통합하고 기존 sync 포함 테스트 40개, 31 draft 검사 45개 항목, 자산 5개 계획 연동을 확인했습니다. 30·31 설계 브랜치와 35 yunli에 게시하는 범위이며 보호 브랜치 통합·원격 CI·운영 적용은 별도입니다.
- 미완료: 나머지 자산 이식, 안전 실행 계약·Ansible 연결, 실제 신규 개인 설치·운영 활성화·복구·토큰 비교. 개발 후보를 승인 release로 표시하지 않습니다.

### Added

- 32 `system-engineering-resources/00_governance/02_kiro/`에서 Kiro 공개 mirror(49개 파일) 이관.
- 32 `00_governance/03_claude/README.md`의 Claude 예약 영역 이관.
- 저장소 루트 `README.md` 추가.
- `agent-workflows/` 아래 공통·Kiro·GPT/Codex·Claude용 `USER_TODO.md`와 `UPDATE_TODO.md` 추가.

### Changed

- `~/.kiro/02_home-sjyun-kiro.sh`의 동기화 target을 32 `00_governance/02_kiro/`에서 이 저장소 `kiro/`로 전환.
- 기존 root Kiro TODO를 `agent-workflows/kiro/`로 이동하고 도구별 workflow 인덱스를 추가.

---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-10-09

© 2026 siasia86. Licensed under CC BY 4.0.
