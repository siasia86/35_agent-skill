# Codex 공통·저장소별 governance 구성

## 1. 두 역할과 소유권

- governance-default는 개인 공통 정책을 적용하는 skill입니다.
- governance-repository는 각 저장소가 선택한 정책·검증·업무 기록을 적용하는 skill입니다. 이름은 같고 내용과 해시는 저장소 profile에 따라 달라집니다.
- 35의 templates/governance는 재사용 진입점 구현입니다. 31이 정책·저장소별 profile을 소유하고 30의 codex_governance.py가 고정 입력을 검증해 완결된 후보를 생성합니다.

현재 [payload catalog](ASSET_CATALOG.json)는 기존 독립 skill 25개·agent 10개·개인 지침 한 개와 work-rules 동반 파일을 유지합니다. 새 두 skill은 31의 정책을 합성하는 별도 초안 계약으로 생성하며 catalog의 단일 파일 자산으로 취급하지 않습니다. 관련 정책을 제외한 SKILL만 설치하지 않습니다.

## 2. 필수 지침과 발견 경로

개인 AGENTS는 실제 Codex home에, 개인 skill은 실제 사용자 홈의 .agents/skills에 배치하는 후보를 만듭니다. 사용자 홈과 CODEX_HOME은 구분합니다. 저장소 AGENTS는 루트에, 커스텀 skill은 해당 저장소의 .agents/skills/governance-repository에 배치하는 후보입니다. [공식 skill 발견 경로](https://learn.chatgpt.com/docs/build-skills)와 [AGENTS 읽기 규칙](https://learn.chatgpt.com/docs/agent-configuration/agents-md)을 기준으로 합니다.

AGENTS가 고정 해시의 로컬 정책을 필수로 읽고 skill은 작업 절차를 안내합니다. implicit skill 선택이 필수 정책 읽기를 보장한다고 가정하지 않습니다. 이미 읽은 동일 파일·해시는 세션에서 재사용합니다. 누락·권한 거부·불일치는 영향 범위를 보고합니다.

기존 보존 skill·agent는 [archive](archive/README.md)에 두어 개발 디렉토리에서 우연히 발견되는 일을 방지합니다. main 세션의 개인 SE 지침은 AGENTS로 정하며 [custom agent TOML](https://learn.chatgpt.com/docs/agent-configuration/subagents)은 위임 세션 역할입니다. Kiro의 resources·allowedTools·hooks·primary agent 변경은 각각 대응 구현과 동작 검증이 필요합니다.

## 3. 생성·검토·적용

31의 profiles/codex_governance.v1-draft.json은 네 진입점 template와 공통 정책·각 저장소 정책의 source·SHA-256을 고정합니다. 30 도구의 build·check는 31 .staging/codex-governance 아래에만 후보를 만들고 확인합니다. 결과의 personal/codex_home, personal/user_home, repository는 경로 역할을 표시하는 staging 디렉토리이며 실제 runtime 경로가 아닙니다.

각 선택 저장소에는 파일 일곱 개를 생성합니다. 개인 AGENTS·default SKILL·공통 정책 세 개와 저장소 AGENTS·repository SKILL·공통 정책·저장소 정책 네 개입니다. 양쪽 AGENTS는 initialize_once로 기록하고 기존 파일이 있으면 비교·병합합니다. managed 표기도 덮어쓰기 권한을 부여하지 않습니다.

생성 후 Markdown·skill 문법·정책 해시·참조·거부 사례·무변경 재생성을 검사합니다. 후보는 draft·deployable false이며 실제 개인 홈 설치·운영 적용·release는 별도 gate입니다. 해시와 개발 기준 commit 기록은 승인 서명이나 현재 Git 내용의 동일성 검증을 대신하지 않습니다.

## 4. 이식 대조 제한

최신 Kiro의 md-link-check·repo-governance·work-rules 원본은 이번 재확인에서도 OS 읽기 권한이 없어 전체 내용을 대조하지 못했습니다. 보존 원본의 권한·소유권·내용을 변경하지 않습니다. 현재 Codex 수정과 정적·격리 검증은 이 제한을 포함해 기록합니다.

## 5. 개인 자산과의 AGENTS 합성

기존 catalog의 se-instructions와 새 governance 후보의 AGENTS를 같은 대상에 따로 설치하지 않습니다. 새 후보는 필수 정책 진입점 구성안이며 기존 개인 SE 지침은 실제 적용 전에 비교·병합해 하나의 AGENTS로 유지합니다. 현재 생성기는 그 설치·병합을 실행하지 않습니다.

35 자산을 함께 선택하면 30의 --ai-profile guard로 기존 선택 plan과 새 일곱 파일의 logical target을 대조합니다. AGENTS 등 중복 target은 후보 생성 전에 거부합니다. 31의 codex_companion_assets.v1-draft.json은 instruction을 제외한 호환 예시이며 통과한 plan·입력 해시를 candidate manifest에 기록합니다. 실제 경로 mapping과 runtime 중복·병합 검증은 활성화 gate입니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
