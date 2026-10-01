# Codex 공통·저장소별 governance 구성

## 1. 두 역할과 소유권

- governance-default는 개인 공통 정책을 적용하는 skill입니다.
- governance-repository는 각 저장소가 선택한 정책·검증·업무 기록을 적용하는 skill입니다. 이름은 같고 내용과 해시는 저장소 profile에 따라 달라집니다.
- 35의 templates/governance는 재사용 진입점 구현입니다. 31이 정책·저장소별 profile을 소유하고 30의 codex_governance.py가 고정 입력을 검증해 완결된 후보를 생성합니다.

현재 [payload catalog](ASSET_CATALOG.json)는 기존 독립 skill 16개·agent 10개·개인 지침 한 개와 work-rules의 참조 3개와 Python 코드 골격 1개를 포함합니다. 선택 ID 27개가 전체 선택 시 31개 파일로 확장됩니다. 새 두 skill은 31의 정책을 합성하는 별도 초안 계약으로 생성하며 catalog의 단일 파일 자산으로 취급하지 않습니다. 관련 정책을 제외한 SKILL만 설치하지 않습니다.

## 2. 필수 지침과 발견 경로

개인 AGENTS는 실제 Codex home에, 개인 skill은 실제 사용자 홈의 .agents/skills에 배치하는 후보를 만듭니다. 사용자 홈과 CODEX_HOME은 구분합니다. 저장소 AGENTS는 루트에, 커스텀 skill은 해당 저장소의 .agents/skills/governance-repository에 배치하는 후보입니다. [공식 skill 발견 경로](https://learn.chatgpt.com/docs/build-skills)와 [AGENTS 읽기 규칙](https://learn.chatgpt.com/docs/agent-configuration/agents-md)을 기준으로 합니다.

AGENTS가 고정 해시의 로컬 정책을 필수로 읽고 skill은 작업 절차를 안내합니다. implicit skill 선택이 필수 정책 읽기를 보장한다고 가정하지 않습니다. 이미 읽은 동일 파일·해시는 세션에서 재사용합니다. 누락·권한 거부·불일치는 영향 범위를 보고합니다.

기존 보존 skill·agent는 [archive](archive/README.md)에 두어 개발 디렉토리에서 우연히 발견되는 일을 방지합니다. main 세션의 개인 SE 지침은 AGENTS로 정하며 [custom agent TOML](https://learn.chatgpt.com/docs/agent-configuration/subagents)은 위임 세션 역할입니다. Kiro의 resources·allowedTools·hooks·primary agent 변경은 각각 대응 구현과 동작 검증이 필요합니다.

## 3. 생성·검토·적용

31의 profiles/codex_governance.v1-draft.json은 네 진입점 template와 공통 정책·각 저장소 정책의 source·SHA-256을 고정합니다. 30 도구의 build·check는 31 .staging/codex-governance 아래에만 후보를 만들고 확인합니다. 결과의 personal/codex_home, personal/user_home, repository는 경로 역할을 표시하는 staging 디렉토리이며 실제 runtime 경로가 아닙니다.

각 선택 저장소에는 파일 일곱 개를 생성합니다. 개인 AGENTS·default SKILL·공통 정책 세 개와 저장소 AGENTS·repository SKILL·공통 정책·저장소 정책 네 개입니다. 양쪽 AGENTS는 initialize_once로 기록하고 기존 파일이 있으면 비교·병합합니다. managed 표기도 덮어쓰기 권한을 부여하지 않습니다.

생성 후 Markdown·skill 문법·정책 해시·참조·거부 사례·무변경 재생성을 검사합니다. 후보는 draft·deployable false이며 실제 개인 홈 설치·운영 적용·release는 별도 gate입니다. 해시와 개발 기준 commit 기록은 승인 서명이나 현재 Git 내용의 동일성 검증을 대신하지 않습니다.

## 4. 이식 대조 제한

2026-09-29에는 최신 Kiro 세 파일의 OS 읽기 권한이 없어 대조하지 못했습니다. 2026-09-30에는 세 파일 전체를 읽고 현재 HEAD와 동일한 bytes임을 확인하여 Codex 후보와 대조했습니다. 검사 범위·정책 발견·권한 및 재시도 안전 기준을 보완했으며 상세 근거와 도구 한계는 [추가 검증 기록](CODEX_GOVERNANCE_VERIFICATION.md#5-2026-09-30-최신-kiro-세-파일-대조와-보완)에 있습니다. Kiro 원본·권한·소유권은 변경하지 않았고 runtime 설치·자동 hook은 별도 미검증입니다.

## 5. 개인 자산과의 AGENTS 합성

기존 catalog의 se-instructions와 새 governance 후보의 AGENTS를 같은 대상에 따로 설치하지 않습니다. 새 후보는 필수 정책 진입점 구성안이며 기존 개인 SE 지침은 실제 적용 전에 비교·병합해 하나의 AGENTS로 유지합니다. 현재 생성기는 그 설치·병합을 실행하지 않습니다.

35 자산을 함께 선택하면 30의 --ai-profile guard로 기존 선택 plan과 새 일곱 파일의 logical target을 대조합니다. AGENTS 등 중복 target은 후보 생성 전에 거부합니다. 31의 codex_companion_assets.v1-draft.json은 instruction을 제외한 호환 예시이며 통과한 plan·입력 해시를 candidate manifest에 기록합니다. 실제 경로 mapping과 runtime 중복·병합 검증은 활성화 gate입니다.

## 6. 31 담당 agent 인계와 중복 판정

2026-09-30 현재 31 작업본의 정책·profile·기존 `.governance/HANDOFF.md`와 35 변경 후보를 대조했습니다. 31에는 이미 역할·후속 gate 안내가 있으므로 새 중앙 계약을 만들지 않고 기존 계약과 인계 문서를 보완합니다. 관찰·검사 결과는 [검증 기록 §6](CODEX_GOVERNANCE_VERIFICATION.md#6-2026-09-30-3135-중복-검토와-agent-인계)에 있습니다. 아래 경로는 각 저장소 루트 기준이며 다른 저장소를 자동 로딩하는 runtime 참조가 아닙니다.

### 역할과 반복되는 기준

- 31의 `.governance/repository/codex/default_policy.md`와 35의 `work-rules`에는 요청 범위·사용자 변경 보존·검증 구분·기록 기준이 반복됩니다. 중앙 구성에서는 31 정책이 기준이고 35는 교체 검증·timeout 후 상태 확인·문서 검사 같은 실행 절차를 제공합니다. `work-rules`는 사용자나 저장소가 선택한 개인 관례이며 별도의 중앙 정책 원본으로 배포하지 않습니다. 중앙 정책을 바꾸려면 31에서 검토하고 35에는 필요한 절차와 참조만 반영합니다.
- 31이 선택하는 `governance-repository`와 35의 `repo-governance`는 이름과 목적이 다릅니다. 전자는 고정 정책 적용, 후자는 binding 부재 또는 누락·충돌 조사입니다. binding이 있으면 `repo-governance`로 별도 정책을 다시 선택하거나 필수 참조 실패를 우회하지 않습니다.
- 31의 문서 정책·검사 설정은 적용할 양식을 선택하고 35의 `md-link-check`는 검사 절차·도구 한계를 안내합니다. H2 번호·목차·문체를 전문 skill에서 전역 정책으로 다시 정의하지 않습니다. checker 구현 결함은 30이 수정합니다.
- `se-instructions`와 생성 AGENTS는 동일 target을 사용할 수 있어 함께 별도 설치하지 않습니다. 기존 지침을 보존하고 최종 AGENTS를 비교·병합합니다. 선택 companion 네 자산은 governance skill 이름과 겹치지 않지만 실제 경로 확정 후 충돌 검사는 여전히 필요합니다.

### 31에서 이어서 할 작업

1. 31의 `AGENTS.md`와 지정된 governance·agent workflow·verification·documentation·central configuration 정책을 읽고 계정 소유 독립 작업본과 현재 승인 범위를 확인합니다. 기존 `.governance/HANDOFF.md`, `.governance/PLAN.md`, `.governance/TODO.md`, `profiles/codex_governance_contract.md`를 진입점으로 사용합니다. 과거 직접 수정·게시 예외를 새 작업에 승계하지 않습니다.
2. 35의 [9월 30일 대조 기록](CODEX_GOVERNANCE_VERIFICATION.md#5-2026-09-30-최신-kiro-세-파일-대조와-보완)을 확인하고 31 HANDOFF의 최신 Kiro 전체 대조가 남았다는 안내를 날짜별 기록으로 정정합니다. 31 PLAN·TODO에는 catalog pin 정합화의 완료 조건을 연결하고 검증 전 완료 표시하지 않습니다.
3. [개인 skill 정리 기록](WORKFLOW_SKILL_PLAN.md#5-2026-09-30-개인-skill-설치-목록-정리)의 제외 ID·대체 경로를 확인하고 실제 선택 profile에 제외 ID가 있으면 검토합니다. 현재 catalog는 27 ID·31파일입니다. `profiles/ai_document_review.v2-draft.json`의 `provenance.catalog_sha256`을 검토한 35 catalog bytes에 맞춥니다. 현재 값은 불일치하며 30 planner가 거부합니다. 35 후보는 미커밋이므로 먼저 작업본·자산 해시·내용을 확인합니다. 실제 게시 후 개발 기준 commit을 기록하되 mutable 파일의 동일성·release 승인을 주장하지 않습니다.
4. `profiles/codex_governance.v1-draft.json`은 네 template와 정책 해시를 고정하며 catalog pin을 갖지 않습니다. 이번 template·정책 해시는 모두 일치하므로 이 profile의 pin을 일괄 변경하지 않습니다. companion v1은 catalog digest pin이 없지만 planner의 현재 자산 해시 검사를 통과해야 합니다. 실제 선택 집합을 바꾸려면 중앙 profile에서 검토합니다.
5. 30 작업본의 `src/governance_profile.py --profile ... --catalog ...`로 v2와 companion을 재검사합니다. 이후 `src/codex_governance.py build/check --source ... --assets ... --repository 31_governances --ai-profile profiles/codex_companion_assets.v1-draft.json`을 승인된 staging에서 실행합니다. 기존 instruction 포함 profile의 target 충돌 거부, 무변경 재생성, manifest 입력·출력 해시와 문법·참조도 확인합니다. 이번 인계 작업에서는 staging build/check를 실행하지 않았습니다.
6. 31의 draft manifest에 포함된 파일을 변경하면 해당 파일 해시와 자체 checksum을 함께 갱신하고 verification 정책의 검사를 수행합니다. HANDOFF에는 실제 검증 결과·미실행을 남기고 상세 원인은 한 곳에서 관리합니다. 필수 정책 로딩·실제 runtime·hook·consumer 적용·release는 기존 후속 gate에서 별도로 검증합니다.

31 HANDOFF 반영 패치는 별도로 준비하며 31 원본에 적용하지 않았습니다. 적용 전 대상 파일의 변경 여부와 패치를 검토하고 `git apply --check`를 실행합니다. 미게시 복구는 해당 문서·profile·draft manifest의 이번 변경분만 되돌리고 기존 후보와 사용자 변경을 보존합니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
