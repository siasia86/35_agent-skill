# Codex Windows 구조와 Workflow 보완안

Windows 개인 Codex의 복사·사용 구성, 저장소 작업 기록, 공통 workflow의 역할과 장단점을 설명합니다. 현재 안내는 `yunli@a6e3584` 이후의 배포 원본 배치 교정 T-WIN-002를 반영합니다. 완료 근거는 [배치 교정 이력](agent-workflows/history/2026-10-03/T-WIN-002-distribution-root.md)에 연결합니다.

이 문서는 구조 안내입니다. **현재 배치와 보완안을 구분**하며, 작성만으로 폴더 이동·전역 지침 설치·모델 설정·새 문서의 자동 로드가 적용되지는 않습니다. 실제 작업 상태는 해당 TODO, 실행 근거는 해당 검토·검증 기록에서 확인합니다.

## 1. 현재 구조

아래 tree는 Windows 관련 주요 경로입니다. `skills/<skill>/`은 실제 폴더들의 공통 형태이며 전체 파일 목록은 아닙니다.

```text
35_agent-skill/
├── AGENTS.md                            # 35 전용 작업·보존·게시 지침
├── CHANGELOG.md                         # 저장소 주요 변경 색인
├── codex_windows.md                     # 현재 구조와 보완안 설명: 이 문서
├── codex_windows/                       # 복사·사용 공간
│   ├── AGENTS.md                        # 개인 공통 지침의 단일 배포 원본
│   ├── README.md                        # 사용 안내
│   ├── personal/                        # 설정 예시·비교 자료·홈 적용 안내
│   │   ├── README.md
│   │   ├── config.example.toml
│   │   ├── config.shared.example.toml
│   │   └── references/                  # 보존 자료
│   └── skills/                          # SKILL.md를 가진 19개 폴더
│       ├── README.md
│       └── <skill>/
│           ├── SKILL.md                 # Windows 활성 절과 보존 원문
│           ├── scripts/                # 해당 skill이 제공하는 실행 도구
│           └── references/             # 해당 skill이 제공하는 동봉 참조
└── agent-workflows/                     # 개발·적용·검토 기록
    ├── README.md
    ├── INDEX.md                         # 35의 구조·조회 조건
    ├── history/                         # 완료 관리 기록
    │   └── 2026-10-03/
    │       └── T-WIN-002-distribution-root.md
    └── codex/
        ├── README.md
        ├── HANDOFF.md                   # 기존 세션 인계
        └── windows/
            ├── README.md               # 현재 Windows 문서 색인
            ├── PLAN.md
            ├── TODO.md
            ├── ISSUE.md
            ├── REVIEW.md               # 이관 당시 검토
            ├── IMPROVEMENT_REVIEW_2026-10-03.md
            ├── REPORTING_REMEDIATION_2026-10-03.md
            └── verification/           # 개발 검사 도구·과거 증거
```

`scripts/`·`references/`의 존재와 구성은 skill마다 다릅니다. 사용 단위와 필요한 도구는 [Windows 사용 안내](codex_windows/README.md)와 [19개 skill 목록](codex_windows/skills/README.md)을 확인합니다. 개인 지침·설정 예시는 [personal 안내](codex_windows/personal/README.md)에서 비교·병합 방법을 확인합니다.

| 영역                | 역할                                               | 구분 기준                                             |
|---------------------|----------------------------------------------------|-------------------------------------------------------|
| `codex_windows/`    | skill 폴더 전체와 필요한 동봉 자료를 복사하여 사용 | 개발 PLAN·TODO·ISSUE·REVIEW·검사 결과를 추가하지 않음 |
| `agent-workflows/`  | 개발·적용·검토·작업공간별 관찰 관리                | 실제 사용에 필수인 설치 의존성으로 만들지 않음        |
| 루트 `AGENTS.md`    | 이 저장소의 적용 지침과 게시 기준                  | 개인 홈 공통 지침과 역할 구분                         |
| 루트 `CHANGELOG.md` | 주요 완료 변경과 상세 기록 연결                    | 실행 원시 로그를 모두 중복 저장하지 않음              |
| 이 문서             | tree·역할·보완안·장단점 설명                       | 활성 작업 상태의 별도 원본으로 사용하지 않음          |

현행 상태·검사·미실행은 [Windows 작업 색인](agent-workflows/codex/windows/README.md), [TODO](agent-workflows/codex/windows/TODO.md), [보고 지침과 helper 보완 기록](agent-workflows/codex/windows/REPORTING_REMEDIATION_2026-10-03.md)에서 확인합니다. 기존 이관 REVIEW와 후속 검토는 입력 시점·범위를 구분합니다.

현행 자료 탐색은 [AI 작업 INDEX](agent-workflows/INDEX.md)를 기준으로 합니다. 위 tree는 배포 원본과 관리 공간의 역할을 설명하며 INDEX의 조회 조건·TODO 상태와 같은 현황표를 별도 관리하지 않습니다.

## 2. Codex가 인식하는 Markdown

| 파일                 | 공식 동작                                                   | 구조에서의 역할                                                     |
|----------------------|-------------------------------------------------------------|---------------------------------------------------------------------|
| `AGENTS.md`          | Codex home와 프로젝트의 지정 경로에서 지속 지침으로 읽음    | 항상 필요한 요약·repo 규칙·관리 문서 조회 조건                      |
| `AGENTS.override.md` | 같은 위치의 AGENTS보다 우선 선택                            | 필요한 예외 지침에만 사용; 같은 위치의 두 파일을 합치는 용도가 아님 |
| `SKILL.md`           | 이름·설명을 먼저 확인하고 선택 시 전체 본문을 읽음          | 재사용 작업 절차와 필요한 동봉 참조·도구                            |
| `PLANS.md`           | 공식 Cookbook에서 AGENTS가 참조하도록 설정한 계획 형식 예시 | 선택 사항; 기존 PLAN의 이름만 바꿀 필요 없음                        |

AGENTS의 발견 경로·우선순위는 [공식 AGENTS 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md)를 따릅니다. SKILL은 `name`·`description` metadata와 실제 검색 위치·선택 조건이 필요합니다. [공식 skill 안내](https://learn.chatgpt.com/docs/build-skills)

`PLANS.md`는 제품의 기본 자동 발견 파일이라는 근거로 사용하지 않습니다. 해당 Cookbook은 실행 계획의 형식·사용 조건을 AGENTS로 연결한 예시이며 현재 archived 자료입니다. [공식 실행 계획 예시](https://developers.openai.com/cookbook/articles/codex_exec_plans)

README·INDEX·PLAN·TODO·TASK·REVIEW·DELEGATION·ISSUE·CHANGELOG·INTERVIEW는 기본 자동 발견 이름으로 공식 안내되지 않은 사용자 관리 문서입니다. 요청·AGENTS·선택 skill에 경로와 조회 조건을 명시합니다. `project_doc_fallback_filenames`는 AGENTS의 대체 지침 이름을 선택하는 설정이므로 관리 문서 전체를 로드하는 기능으로 사용하지 않습니다.

DELEGATION 기록은 실제 agent 호출·모델 선택·결과 회수와 구분합니다. 개인·프로젝트 custom agent 설정은 별도의 TOML 형식이며 문서 존재만으로 실행을 보장하지 않습니다. [공식 Subagents 안내](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## 3. 공통 규칙과 repo 기록의 연결 보완안

전역에는 공통 규칙·절차·문서 형식을 두고, 상태·결정·완료 이력은 **각 repo 안에서 관리**합니다. 31의 공통 안내를 다른 repo의 작업 상태 원본으로 사용하지 않습니다.

| 위치                | 권장 내용                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------|
| 개인 홈 `AGENTS.md` | 한국어 보고·실제 Git 상태 확인·필요 자료만 조회·Luna 수집과 총괄 AI 판단 등 짧은 공통 원칙 |
| 개인 work-rules     | 시작·계획·분담·실행·검증·이력 보존 절차; 상세 형식은 필요 시 읽는 동봉 참조                |
| 각 repo `AGENTS.md` | 해당 repo 규칙·관리 README 하나의 경로·조회/갱신 조건·검증/게시 기준                       |
| 각 repo 관리 README | 도구·플랫폼별 활성 PLAN/TODO와 관련 ISSUE·검토·완료 이력의 연결                            |

35에서 배포용 지침의 작성 위치는 [공통 AGENTS](codex_windows/AGENTS.md)와 [work-rules](codex_windows/skills/work-rules/SKILL.md)입니다. 파일을 준비한 상태와 실제 개인 홈 적용·새 세션의 발견/선택은 구분합니다. 기존 홈 지침·동명 skill을 일괄 교체하지 않습니다.

다음 tree는 관리 역할의 기준입니다. README·INDEX 진입점과 첫 history 기록은 35에 적용했으며 DELEGATION·INTERVIEW는 필요할 때 생성합니다. 기존 과거 자료는 일괄 이동하지 않습니다.

```text
35_agent-skill/
├── AGENTS.md                            # 관리 README 하나로 연결
├── CHANGELOG.md                         # 기존 완료 변경 색인 재사용
├── codex_windows/                       # 복사·사용 구성을 유지
└── agent-workflows/
    ├── README.md                        # 관리 공통 진입점으로 보완
    ├── codex/windows/
    │   ├── README.md                    # Windows 자료의 하위 색인
    │   ├── PLAN.md                      # 큰 작업이 있을 때
    │   ├── TODO.md                      # 활성 작업 상태의 기준
    │   ├── ISSUE.md                     # 오류·중요 제약이 있을 때
    │   ├── REVIEW.md                    # 실질적 검토가 있을 때
    │   ├── DELEGATION.md                # 복잡한 위임에만 추가: 미생성
    │   └── INTERVIEW.md                 # 설계 질문이 많을 때: 미생성
    └── history/                         # 완료 상세 기록
        └── YYYY-MM-DD/
            └── T-WIN-001-작업제목.md
```

관리 공통 README는 존재하는 자료에 연결하고, 상세 task 상태는 TODO에서 갱신합니다. 플랫폼 README는 하위 자료 색인이며 같은 상태 표를 복제하지 않습니다. 별도 WORKFLOW.md를 추가하기보다 기존 README의 역할을 보완합니다. 다른 repo에서는 기존 관리 경로와 완료 색인을 먼저 재사용합니다.

현재 35의 DELEGATION·INTERVIEW는 선택 문서이며 새 완료 기록은 agent-workflows/history에서 관리합니다. 보완안의 폴더 이름을 다른 repo에 강제하거나 보호된 Linux·원문·과거 증거를 자동 이동하지 않습니다.

## 4. 작업 문서의 역할

| 문서       | 기준 내용                                                                                | 사용 조건                                                |
|------------|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| README     | 현재 목표의 PLAN 링크·활성 TODO·막힌 ISSUE·최신 완료 기록 연결                           | 작업 시작/재개; 상세 상태의 별도 원본을 만들지 않음      |
| PLAN       | 큰 목표·범위·단계·완료 조건·주요 결정·연결 작업 ID                                       | 큰 작업·다단계 변경; 작은 상태는 TODO로 연결             |
| TODO       | 기본: ID·내용·상태·다음 행동. 필요 시 담당·PLAN ID·완료 조건·근거                        | 활성 작업; 작은 질의를 위해 새 파일을 강제 생성하지 않음 |
| REVIEW     | 대상·기준 commit·검토일·사실/추론·모순·잘된 점/문제·장단점·근거/한계·후속 ID             | 구조·주요 구현·결정의 검토; 확인한 범위만 기록           |
| DELEGATION | TODO ID·입력·허용 범위·동시 수정 금지 대상·완료 조건·실제 모델/실행 ID·결과·총괄 AI 판단 | 복잡한 다중 AI 작업; 단순 분담은 TODO의 담당·결과로 관리 |
| ISSUE      | 증상·재현·환경·근거·확정/추정 원인·교정·검증·재발 방지·재개 방법                         | 오류·막힌 작업·중요 제약; 해당 문제에 맞는 부분만 조회   |
| CHANGELOG  | 완료 요약·관련 ID·검증 범위·commit·상세 history 링크                                     | 완료 시; 기존 제품 release 로그가 있으면 그 용도를 존중  |
| INTERVIEW  | 여러 관점의 질문·답변/미확정·대안·결정·PLAN 연결                                         | 설계 불확실 시 선택; 채택한 결정의 현행 기준은 PLAN      |

`AI_TODO` 역할은 DELEGATION으로, `ITERVIEW` 이름은 INTERVIEW로 정리하는 제안입니다. 모든 repo에 8개 문서를 한꺼번에 만들지 않습니다. 지속 작업은 진입 README·활성 TODO·완료 이력으로 시작하고 나머지는 필요한 경우에 추가합니다.

작은 질문은 기존 PLAN이 있으면 미확정 항목으로 기록하고, 없으면 세션에서 처리합니다. 지속 추적이 필요할 때만 관리 문서에 남깁니다. 상세 결과는 한 기준 문서에 두고 다른 문서는 ID·링크로 연결합니다. 제품 설정과 workflow 기록도 구분합니다.

## 5. 조회·위임·완료 처리

1. 시작/재개: 실제 Git root·branch·기존 변경을 확인하고 적용 지침과 관리 README에서 관련 TODO/PLAN으로 이동합니다. 이미 로드한 지침과 전체 과거 기록을 매번 다시 읽지 않습니다.
2. 설계: 필요한 질문·대안을 INTERVIEW 또는 기존 PLAN에 정리하고 채택한 결정과 실행 항목을 PLAN/TODO에 연결합니다.
3. 위임: 범위·판정 기준이 정해진 수집은 사용 가능한 Luna에 우선 배정하고, 판단·상충 근거 해석·최종 검증은 총괄 AI가 담당합니다. 작은 호출의 위임 비용과 미지원 상태를 구분합니다. 실제 모델·오류·누락을 확인합니다.
4. 오류: 해당 ISSUE의 재발 방지·근거를 확인하고 필요한 교정 TODO와 실제 검증 결과를 연결합니다.
5. 완료: 완료 조건을 확인한 뒤 공개 가능한 상세 관리 내용을 같은 repo의 관리 경로에 먼저 보존합니다. 35의 완료 기록 위치는 `agent-workflows/history/`이며 다른 repo에서는 기존 관리 경로를 재사용합니다. 완료 요약은 CHANGELOG, 평가가 있으면 REVIEW에 남깁니다.
6. 정리: history로 들어오는 ID 링크와 history에서 근거 파일로 나가는 상대 링크·앵커를 확인한 뒤 완료 항목을 활성 TODO에서 제거합니다. 미완료 항목은 유지하고 전체 완료한 PLAN은 history로 이관합니다.

ID는 repo 안에서 유일하게 유지하고 재사용하지 않습니다. 여러 도구·플랫폼이 있는 35의 신규 항목은 `P-WIN-001`·`T-WIN-001`·`I-WIN-001`처럼 구분합니다. 기존 ID·보호 기록은 재번호하지 않습니다. history는 날짜·작업 ID·짧은 제목으로 이름을 정하고 같은 ID의 후속 기록은 짧은 commit 또는 순번으로 구분합니다.

구현·자동 검사·사용자 검증·Git 게시를 별도 상태로 기록합니다. 구현 항목이 끝나도 사용자 검증·게시 항목이 남으면 그 항목과 큰 PLAN은 활성 상태로 유지합니다. 35의 게시 순서는 [저장소 AGENTS](AGENTS.md)에 따라 **yunli 게시 → 사용자 검증 → main 브랜치 반영**입니다. 검증 대상 commit·변경 범위·결과를 기록하고 이후 실질적으로 변경된 범위는 다시 검증합니다. 총괄 AI와 Git의 main 브랜치를 용어로 구분합니다.

history에는 공개 가능한 상세 관리 기록을, CHANGELOG에는 완료 색인을 둡니다. REVIEW와 CHANGELOG의 요약 중복은 허용하되 같은 상세 결과를 두 곳의 현행 원본으로 유지하지 않습니다. 해결한 ISSUE의 재발 방지 기준은 계속 찾을 수 있게 연결합니다.

개인 경로·계정·자격증명·승인 대화 원문·비공개 raw 증거는 원격 기록으로 복사하지 않습니다. 보호된 원문·이전 검사 JSON/해시는 그대로 두고 새 연결 안내에서 기준 경로를 설명합니다. 과거 승인과 검사 결과를 새 실행 권한이나 현재 실행 결과로 재사용하지 않습니다.

## 6. 장점과 단점

| 대상                       | 장점                                               | 단점·비용                                | 보완 방법                                              |
|----------------------------|----------------------------------------------------|------------------------------------------|--------------------------------------------------------|
| 사용 공간과 개발 기록 분리 | 복사할 파일과 관리할 자료가 명확                   | 같은 역할의 동봉 사본 관리가 필요        | 폴더 단독 사용을 유지하고 변경한 사본의 일치 확인      |
| 전역 규칙·repo 상태 분리   | 개인 공통 원칙을 재사용하면서 프로젝트 상태를 보존 | repo별 기존 경로가 다름                  | repo AGENTS에서 관리 README 하나를 지정                |
| 단일 진입점·기준 문서      | 다음 세션 재개와 최신 상태 조회가 쉬움             | 큰 작업은 여러 문서 연결이 필요          | 상태는 TODO, 결정은 PLAN, 예방은 ISSUE, 평가는 REVIEW  |
| 완료 내용의 history 보존   | 활성 목록을 짧게 유지하고 과거 근거를 찾기 쉬움    | 이동 후 상대 링크·ID 참조가 깨질 수 있음 | 먼저 보존하고 들어오는/나가는 파일·앵커 링크 확인      |
| 조건부 문서 생성·조회      | 작은 작업의 기록·문맥 부담 감소                    | 어떤 자료를 읽을지 판단이 필요           | AGENTS·work-rules에 생성/조회 조건 명시                |
| 위임과 총괄 검증 분리      | 정형 조회를 분담하고 중요한 판단 근거를 확인       | 전달·대기·재검토 비용이 발생             | 의미 있는 작업 묶음으로 위임; 실제 모델·근거·실패 확인 |

현재 구성의 잘된 점은 복사용 영역과 개발 기록이 분리되고 원문·이전 검사 근거가 보존된 것입니다. 개선할 점은 여러 진입점과 시점이 다른 검토 자료에서 최신 상태를 찾는 부담입니다. 단일 진입점 보완과 기준 문서·입력 시점 표시로 해결하는 방향입니다.

## 7. 설계 검토와 적용 범위

앞선 보완안은 공식 문서 사실 대조와 독립적인 책임·모순·사용성 검토를 거쳤습니다. 다음 모호점을 구체화했습니다.

| 검토 항목                    | 보완한 기준                                          |
|------------------------------|------------------------------------------------------|
| 자동 인식과 관리 문서 혼동   | AGENTS·SKILL 동작과 사용자 문서의 명시적 조회를 구분 |
| 여러 README의 상태 중복      | 공통 README는 진입점, 플랫폼 README는 하위 색인      |
| 사용자 검증 범위             | 대상 commit·변경 범위·결과와 후속 실질 변경을 구분   |
| 완료 이동 후 참조            | 외부→history와 history→근거의 파일·앵커를 모두 확인  |
| 공개 상세 기록의 범위        | 공개 관리 기록과 비공개 raw 증거를 구분              |
| 작은 작업의 과도한 문서 작성 | 최소 TODO 필드와 선택 문서 사용                      |
| 플랫폼 간 ID 충돌            | repo 내 유일 ID와 신규 범위 접두어 사용              |

정적 설계 검토에서 근본적인 문서 책임 충돌은 확인하지 못했습니다. 실제 파일 이동·홈 지침 병합·새 세션의 발견/선택·모든 환경의 동작을 확인한 결과는 아닙니다. 구조 안내 작성과 실제 적용의 상태를 구분하며, 선택한 적용 범위에서 별도로 검증합니다.

최초 구조 안내 문서 추가 당시에는 기존 skill·개인 설정·활성 작업 문서·보호 원문을 개편하지 않았습니다. 기존 이관 검사 결과는 당시 증거로 유지합니다. 아래 후속 보완의 변경·검증·실제 개인 적용은 별도 검토 기록에서 확인하며 새 세션 동작과 구분합니다.

## 8. 공식 skill 기준의 후속 보완

[system·공식 skill 재검토](agent-workflows/codex/windows/SYSTEM_SKILL_REVIEW_2026-10-03.md)에서 현행 공개 plugin source 전체와 실제 local system·cache를 구분했습니다. 35의 AI 작업 INDEX를 추가하고 work-rules·공통 AGENTS에 아래 기준을 반영합니다.

- README는 개요·진입점, INDEX는 주요 tree·읽기 조건·기준 문서 연결입니다. 실제 router skill의 SKILL.md와 일반 INDEX.md를 구분하며 동명 skill은 plugin·파일 경로로 식별합니다.
- 기본은 짧은 TODO.md와 큰 작업의 tasks/<ID>/TASK.md입니다. TODO/ 방식은 각 작업 문서가 상태 원본이고 README는 링크 색인만 맡습니다. 두 상태 원본을 함께 운영하지 않습니다.
- TODO는 사용자 작업 상태를 관리하고 tool JSON·실행 manifest·외부 tracker의 내부 상태를 대체하지 않습니다. 단순 작업에는 전체 문서와 빈 폴더를 생성하지 않습니다.
- 일반 관리 기록과 자유롭게 저장할 수 있는 결과물은 각 repo의 기존 관리 공간에 묶습니다. design-qa.md·sealed scan bundle·제품 소스/자산·개인 runtime·외부 최종 URL 등 경로 계약은 원위치에서 연결합니다.
- 완료 관리 기록을 먼저 보존하고 링크를 확인한 뒤 활성 목록을 정리합니다. 산출물과 검증 원본은 안정적인 경로에 유지하고 공개 기록과 비공개 raw/scratch를 구분합니다.

이 후속 반영은 조회·기록 기준과 개인 skill 적용입니다. 기존 PLAN/TODO의 일괄 분할·이동, 모든 공개 plugin 설치·실행은 포함하지 않습니다. 구체적인 문서 역할·tree·예외는 [work-rules Workflow 참조](codex_windows/skills/work-rules/references/repository-workflow.md)를 기준으로 합니다.

## 9. 개인 Codex 업데이트별 백업

사용자 지정에 따라 이번 개인 설정 백업은 agent-workflows/codex 바로 아래 [2026-10-03-personal-skills-T-WIN-003](agent-workflows/codex/2026-10-03-personal-skills-T-WIN-003/README.md) 폴더 하나로 관리합니다. 다음 업데이트는 이름이 다른 폴더를 추가합니다.

```text
agent-workflows/codex/<날짜>-<목적>-<작업ID>/
├── README.md                  # 범위·설치 결과·검증·복구
├── USE.md                     # 호출·원본·적용 방법
├── before/                    # 이전 skill 전체 사본·inventory
├── after/                     # 실제 적용 후 skill 사본·inventory
├── validation.json            # 공개 검사 근거
└── private/                   # Git 제외: AGENTS/config·raw
```

장점은 업데이트 하나의 전후 상태와 복구 자료를 한 폴더에서 찾는 것입니다. 비용은 보관 용량과 개인정보·Git 제외 확인입니다. 새 사본은 `.agents/skills` 구조로 만들지 않아 runtime 발견 위치와 구분하고, 기존 관찰·JSON·이력 경로는 보존합니다. 배포 원본은 계속 codex_windows이며 이 백업을 독립 편집하거나 다음 설치 source로 사용하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
