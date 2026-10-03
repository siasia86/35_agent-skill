# Codex system·공식 skill 기준 재검토와 개인 적용

검토일: 2026-10-03. 대상은 README/INDEX/AGENTS, repo별 작업 문서와 AI 산출물 구조, Windows 개인 work-rules입니다. 입력은 35의 yunli `3ca2d9d`와 아래 고정 공개 source입니다. 사용자 요청에 따라 개선 기준을 반영하고 검증 후 yunli 게시·실제 개인 skill 적용을 진행합니다.

## 1. 출처와 전체 조사 범위

| 구분                    | 확인한 범위                                                          | 판정                                                         |
|-------------------------|----------------------------------------------------------------------|--------------------------------------------------------------|
| 현행 공개 예제          | openai/plugins `5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f` 전체 clone | 62개 plugin 디렉토리, SKILL 문서 536개                       |
| 이전 공식 skill 저장소  | openai/skills `49f948faa9258a0c61caceaf225e179651397431` 전체 clone  | system 5·curated 39·experimental 0; README에 deprecated 안내 |
| 실제 로컬 system        | 설치된 .system의 SKILL 문서 5개                                      | 공개 source와 같은 제품 버전/구성이 아님                     |
| 로컬 OpenAI plugin 캐시 | bundled 2·curated-remote 32·primary-runtime 6                        | 40개 본문 읽기; 캐시 존재와 세션 활성은 구분                 |
| 35 개인 Windows         | 독립 skill 19개                                                      | 유지; 이번 적용은 work-rules와 동봉 대응 2곳·공통 지침       |

공개 예제의 536개는 직접 skills/<이름>/SKILL.md 502개, 중첩 문서 29개, 시험 fixture 4개, 저장소 개발 helper 1개입니다. 모두 UTF-8로 읽고 name·description 존재와 크기·SHA-256을 조사했습니다. 총괄 AI가 Git 추적 목록과 536개 파일 해시를 독립 재대조했습니다. YAML 전체 문법·모든 실행 절차의 동작 검증으로 해석하지 않습니다.

추가로 manifest 64개와 marketplace 2개를 정적으로 읽었습니다. manifest 작성자 표시는 OpenAI 계열 24개·다른 작성자 38개·시험 fixture 2개입니다. OpenAI가 관리하는 예제 목록에 있다는 사실을 개인 system 내장·OpenAI 작성·현재 설치·모든 OS 실행 보증과 동일하게 보지 않습니다.

현행 관련 SKILL 본문 44개를 심층 정독했습니다. Superpowers 14·Plugin Eval 5·repo plugin-creator 1, Notion 4·Product Design 10·Data Analytics 7·Codex Security 3입니다. 추가 2개는 관련 구간만 읽었으며 나머지 현행 문서는 전체 정적 inventory·패턴 추출 수준입니다. 이전 curated 39개는 전체 본문을 읽어 비교했습니다. 실제 benchmark·API·외부 앱 쓰기·536개 일괄 설치는 하지 않았습니다.

전체 공개 목록·분류·해시·동봉 디렉토리는 [정적 inventory CSV](verification/official-plugins-2026-10-03.csv)에 보존합니다. 원본 package와 라이선스·도구·참조는 로컬 분석 clone에 유지하고 공개 plugin payload를 35의 설치 영역에 재배포하지 않습니다.

출처: [현행 plugin source](https://github.com/openai/plugins/tree/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f), [이전 저장소의 안내](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/README.md).

## 2. system 기준 사실 대조

| 항목                  | 확인한 사실                                                | 적용 기준                                                             |
|-----------------------|------------------------------------------------------------|-----------------------------------------------------------------------|
| AGENTS                | home와 repo→작업 경로의 지침을 읽으며 override 우선        | 짧은 상시 원칙·해당 repo의 INDEX 조회 조건                            |
| SKILL                 | name·description으로 선택하고 선택한 본문·필요 참조를 읽음 | 모든 본문을 상시 읽거나 INDEX가 선택 정보를 대체하지 않음             |
| INDEX.md              | 기본 지침 자동 발견 이름으로 안내되지 않음                 | 선택한 경로·읽기 조건을 AGENTS와 skill에서 명시                       |
| index skill           | 실제 router는 skills/index/SKILL.md                        | 일반 INDEX.md와 구분; 실행 본문을 router에 복제하지 않음              |
| 동명 skill            | 서로 다른 plugin의 index 등 7종이 중복                     | plugin·실제 파일 경로로 식별; 표시를 새 호출 문법으로 보장하지 않음   |
| standalone 개인 skill | repo/사용자 .agents/skills에서 발견 가능                   | 전체 폴더와 필요한 동봉 자료를 복사; plugin 전환을 필수로 만들지 않음 |
| plugin package        | portable plugin.json과 compatibility overlay를 지원        | 개인 작업 이력 디렉토리와 설치 package를 구분                         |
| PLAN/TODO/history     | 이름·이관은 개인 workflow 규약                             | Codex 내장 자동 보관 기능으로 주장하지 않음                           |

공식 근거: [AGENTS](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Skills](https://learn.chatgpt.com/docs/build-skills), [Plugin package](https://developers.openai.com/plugins/build/plugins). package 문서는 root plugin.json을 설명하고 공개 예제·기존 scaffold는 .codex-plugin/plugin.json compatibility 형식을 사용합니다. 기존 형식의 지원 여부와 새 권장 형식을 구분하며 현재 개인 skill의 형식을 일괄 변환하지 않습니다.

## 3. 발견한 모순과 개선 판정

| 발견                                               | source 근거                                                           | 이번 보완                                                                           |
|----------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| INDEX에 상태·skill 본문을 다시 쓰면 원본이 늘어남  | data-analytics index 202행·product-design index 30행                  | INDEX는 주요 tree·읽기 조건·기준 문서 연결만 관리                                   |
| TODO가 모든 tool 상태를 대체할 수 없음             | codex-security validation 23행, track-findings 203행                  | TODO는 사용자 작업 상태; tool JSON/외부 tracker/실행 manifest는 해당 내부 상태 원본 |
| 모든 AI 문서를 한 위치로 이동하면 고정 계약과 충돌 | product-design design-qa 151행; scan-artifacts 5행                    | design-qa.md·sealed bundle·제품 자산·개인 runtime 상태는 원위치에서 연결            |
| 최종 결과가 외부 페이지일 수도 있음                | Notion skill, report-to-google-doc 53행                               | TASK/INDEX에서 로컬 경로와 검증된 외부 URL 모두 허용                                |
| 원문과 현재 실행 기준이 다른 예제                  | plugin-eval improve-skill 14행                                        | 개인 macOS 고정 경로 대신 실제 skill catalog·도구·OS 확인                           |
| dry-run 문서와 실제 CLI가 상충                     | plugin-eval evaluate-skill 49행 대 src/core/benchmark.js 497행        | 정적 검토를 benchmark 성공으로 바꾸지 않고 구현 계약을 대조                         |
| 현재 도구와 image 예제가 상충                      | product-design image-to-code 79행 대 현재 transparent_background 필드 | 실제 제공된 도구 schema를 우선; 실제 이미지 생성은 미실행                           |
| 반복 승인·일괄 적용 지시                           | Superpowers using-superpowers 11행·brainstorming 14행                 | 사용자 기존 승인·선택 skill·작은 작업의 최소 기록 유지                              |
| 원문·worktree·완료 기록 삭제 지시                  | Superpowers TDD 37행·SDD 482행·finishing 169행                        | 보호 원문과 다른 작업을 보존하고 완료 관리 기록을 먼저 보관                         |
| Windows 긴 경로로 초기 checkout 실패               | 현행 source clone의 긴 참조 경로                                      | 분석 clone 한정 core.longpaths 옵션으로 복구; OS/전역 설정 변경 없음                |

위 예제의 source 경로는 CSV와 고정 commit에서 확인합니다. 특히 [design-qa](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/product-design/skills/design-qa/SKILL.md#L151), [data router](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/index/SKILL.md#L202), [benchmark 구현](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/plugin-eval/src/core/benchmark.js#L497)을 정적으로 대조했습니다. source의 교정 후보를 발견한 것이며 외부 source를 수정·게시하지 않았습니다.

## 4. 확정한 개인 규칙과 구조

README는 개요·진입점, INDEX는 탐색, AGENTS는 상시 지침, SKILL은 재사용 실행 절차입니다. 지속 작업에서는 TODO를 현재 상태 원본으로 두고 큰 작업의 TASK에 범위·완료 기준·결과/검증 연결을 둡니다. TODO/ 디렉토리를 선택하면 각 작업 문서가 상태 원본이며 README는 ID·제목·링크 색인만 맡습니다. 두 방식의 상태 원본을 동시에 운영하지 않습니다.

```text
<각 실제 repo>/<기존 관리 공간>/
├── INDEX.md                    # 필요할 때: 구조·읽기 조건
├── TODO.md                     # 활성 사용자 작업 상태
├── tasks/
│   └── T-001-이펙트효과복원/
│       ├── TASK.md             # 범위·입력·완료 기준·결과 링크
│       ├── outputs/            # 위치를 지정할 수 있는 최종 결과
│       └── evidence/           # 해당 실행의 공개 가능한 검증 근거
├── history/                    # 완료된 관리 기록
└── local/                      # raw·scratch: 실제 Git 제외 확인
```

tree는 선택 구조입니다. 기존 경로를 먼저 재사용하고 작은 작업에는 문서·빈 폴더를 일괄 만들지 않습니다. 출력 옵션·사용자 지정·기존 제품·선택 skill의 계약을 확인하며 고정 경로와 외부 결과는 연결합니다. 완료 관리 기록을 먼저 보관하고 링크를 확인한 뒤 활성 TODO를 정리하며 산출물·검증 원본은 안정적인 경로에 유지합니다.

35는 agent-workflows를 재사용하고 [AI 탐색 색인](../../INDEX.md)을 추가합니다. 기존 PLAN/TODO를 자동 분할하거나 J 작업 공간·개인 Documents 결과물을 일괄 이동하지 않습니다. 복사용 codex_windows에는 재사용 지침·동봉 참조만 추가합니다. 상세 기준은 [work-rules 참조](../../../codex_windows/skills/work-rules/references/repository-workflow.md)를 한 작성 원본으로 사용하고 두 동봉 대응본의 bytes 일치를 확인합니다.

## 5. 장단점과 남은 조건

| 방향                   | 장점                                      | 비용·보완                                          |
|------------------------|-------------------------------------------|----------------------------------------------------|
| INDEX와 README 분리    | AI 탐색과 사용자 개요의 역할이 명확       | 단순 repo는 INDEX 생략; 전체 설명·상태 복제 금지   |
| TODO 요약과 TASK 상세  | 상태를 한눈에 보고 큰 작업을 독립 재개    | 상태·담당·다음 행동은 TODO 한 원본                 |
| repo별 관리 공간       | 소유 repo와 결과·이력이 연결              | workspace 전체를 한 Git repo로 가정하지 않음       |
| 경로 예외 연결         | 기존 skill·제품·도구 계약 보존            | 모든 결과의 물리적 단일 위치는 보장하지 않음       |
| history와 근거 분리    | 완료 이력을 짧게 조회하고 검증 근거 보존  | 상대 링크·sealed/개인 자료의 경로 계약 확인        |
| 선택한 개인 skill 적용 | 원문 보존과 현재 Windows 기준을 함께 유지 | 설치 일치와 새 세션 자동 선택·실서비스 검증은 별도 |

현재 잘된 점은 19개 원문·보존 자료와 복사용/개발 기록 구분이 유지되는 것입니다. 보완한 점은 INDEX의 발견 의미, TODO와 tool 상태의 책임, 산출물 고정 경로·외부 URL 예외, 현재 도구와 공개 예제의 모순입니다. 공개 문서의 권고 분량을 이유로 기존 원문을 축약하지 않았습니다.

## 6. 적용·검증·복구

<!-- IMPLEMENTATION-RESULT-BEGIN -->
사용자가 이번 보완의 검토·yunli 게시·실제 개인 skill 추가를 요청한 범위에서 실행했습니다. 35의 work-rules 작성 원본과 두 동봉 대응본, 공통 지침, AI INDEX·구조 안내·이력 연결을 보완했습니다. 기존 Windows TODO의 추가 개인 적용 항목을 남은 범위로 정리하고 HANDOFF에서 과거 개인 적용 대기 기록과 구분했습니다. 다른 repo의 산출물 일괄 이동·19개 skill 전체 설치는 수행하지 않았습니다.

| 대상                | 실제 결과                                                                 | 범위·한계                                                                              |
|---------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 문서 링크·헤딩      | 변경 Markdown 16개, 파일 링크 167개·헤딩 357개 정상                       | 동봉 검사기 26.10.03; 다른 파일 앵커 26개는 별도 대조                                  |
| 새 문서·안내 스타일 | 보존 SKILL 대응 3개를 제외한 13개 통과                                    | 16개 전체 검사에서는 기존 원문 3곳의 푸터 누락 9건 유지; baseline 대조에서 새 진단 0건 |
| 원문·보호 자료      | 보호 파일 442개·Windows 비교 원문 173개 SHA-256 일치                      | Kiro/GPT/Linux/backup, 3곳 COMPAT 밖 원문 유지; 독립 Windows skill 19개 유지           |
| 동봉 Workflow       | 작성 원본과 두 대응본 bytes 동일                                          | 같은 내용은 작성 원본에서 갱신하고 단독 복사용 대응본을 동기화                         |
| 조회 행동 평가      | 별도 fixture에서 AGENTS와 기존 TODO만 조회; 기존 6파일·Git 상태 불변      | config 내용·전체 기록을 읽지 않고 남은 T-002·사용자 확인 대기 T-003만 식별             |
| 완료 행동 평가      | 완료 이력 생성·왕복 연결 검증 후 T-001만 활성 TODO에서 제거               | 5관리 문서 검사·19개 왕복 링크/앵커 통과; 제품·고정 QA·외부 sealed 자료 보존           |
| 개인 work-rules     | 사용자 .agents/skills에 폴더 전체 35파일 추가; source와 SHA-256 전부 일치 | 설치한 활성 Markdown 10개·로컬 링크 25개 통과; Python 5개 AST 확인                     |
| 개인 공통 AGENTS    | 기존 본문 bytes를 보존하고 공통 요약만 추가                               | 개인 백업 보존; 기존 개인 skill 4개·system 파일 49개·config 해시 불변                  |
| 게시 자료 점검      | Gitleaks 8.30.1 디렉토리 검사 탐지 0건, diff 공백 검사 통과               | 비공개 분석 clone·홈 백업·raw 검사 로그는 repo에 포함하지 않음                         |

조회·완료 평가는 실제 격리 파일 조작이며 이전 완료·사용자 확인·plugin 검사 결과는 합성 입력입니다. 실제 plugin 실행이나 새 세션 자동 발견 성공으로 해석하지 않습니다. 설치 폴더 전체를 비교 원문까지 링크 검사하면 linux-original의 과거 상대 링크 8건이 존재하지 않지만, 실행하지 않는 보존 사본의 원래 경로입니다. COMPAT와 필요한 동봉 활성 문서의 25개 링크는 독립 복사 위치에서 모두 확인했습니다. 이를 숨기거나 보호 원문을 수정하여 통과 처리하지 않았습니다.

공개 inventory 수집에는 실제 Luna를 사용했고 총괄 AI가 536개 Git 경로·해시와 핵심 근거를 재대조했습니다. 관련 문서와 설치 의존성은 별도 AI의 읽기 전용 검토에서 차단 결함이 없었으며 과거/현재 반영 범위가 혼동되는 문구 한 곳을 교정했습니다.

이 기록의 게시 후보는 yunli이며 게시 commit·원격 일치는 실제 Git refs로 확인합니다. 사용자 검증과 main 반영, 새 세션의 skill 발견·자동 선택, 나머지 skill·config 설치, 외부 서비스와 전체 plugin 실행은 완료로 처리하지 않습니다.
<!-- IMPLEMENTATION-RESULT-END -->

개인 적용에서는 검증한 work-rules 폴더 전체를 사용자 skill 경로에 추가하고 기존 개인 AGENTS에 공통 요약만 병합합니다. 기존 네 개인 skill·system skill·config는 보존하며 개인 백업과 실제 절대 경로는 공개 기록에 넣지 않습니다. 복구는 설치 파일이 이번 사본과 같은지 확인한 뒤 이번 추가 폴더와 AGENTS 추가 절만 되돌리고 기존 사용자 편집을 보존합니다. 원격 게시 후 복구는 검토한 revert를 사용합니다.

게시 순서는 yunli 일반 push → 사용자 검증 → main 반영입니다. 새 세션 자동 선택·외부 서비스·536개 plugin 실행을 미검증 상태로 유지하며 파일 검사를 그 결과로 확대하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
