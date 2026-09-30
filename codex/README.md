# Codex 재사용 배포본

사용자 지침: [최초 적용](docs/CODEX_SETUP_GUIDE.md) · [업데이트](docs/CODEX_UPDATE_GUIDE.md). docs/는 설치 payload가 아니며 아래 개발 상태와 설치 경계를 먼저 확인합니다.

## 1. 현재 상태

gpt 원본 62개 파일을 복사한 개발용 배포본입니다. 전체 skill·agent를 바로 설치할 수 있는 release는 아직 아닙니다. 원본은 gpt에 보존하며 최초 파일별 SHA-256과 출발 commit은 [BASELINE_MANIFEST.json](BASELINE_MANIFEST.json)에 있습니다.

현재 payload에는 [최소 SE 공통 지침](payload/personal/AGENTS.md), skill 16개, agent 10개와 work-rules의 작업별 참조 3개와 Python 코드 골격 1개가 있습니다. 자산 선택 ID는 27개, 설치 후보 파일은 31개입니다. 개인 홈에 설치한 것은 과거 P0 최소 지침뿐이며 이번에는 runtime을 변경하지 않습니다. 원본 대응·개인 및 프로젝트 설치 경로는 [설치 매핑](PAYLOAD_MAP.md), 이식 상태는 [Batch 6 기록](MIGRATION_BATCH6.md), 전체 진행은 [루트 TODO](../TODO.md)를 확인합니다.

## 2. 설치 경계

- 개인 skill 선택 설치는 [루트 README](../README.md#51-개인-codex-skill-직접-설치)의 Python setup·수동 복사 절차를 사용합니다. payload skill은 31 없이 사용할 수 있으며 중앙 정책 합성은 별도 선택 구성입니다.
- 개인 적용 후보: payload/personal/AGENTS.md를 실제 Codex home의 AGENTS.md에 병합합니다. 기본 홈 경로를 추정해 다른 계정에 설치하지 않습니다.
- 프로젝트 시험: 같은 최소 지침에 저장소 전용 범위를 더한 루트 AGENTS.md를 사용할 수 있습니다.
- 기존 AGENTS.md·AGENTS.override.md와 차이·우선순위·백업을 확인하고 새 세션에서 로딩과 동작을 검증합니다.
- 이 디렉토리 전체를 사용자 홈이나 consumer 루트에 덮어쓰지 않습니다. README·TODO·PLAN·이전 이력·BASELINE_MANIFEST는 설치 payload가 아닙니다.
- archive/skills, archive/agents, policies, markdown, prompts는 보존된 이식 후보입니다. 이전 경로는 archive/PATH_MAP.json으로 대응하며 자동 발견 경로에서 분리했습니다. 신규 자체 완결형 후보는 payload 아래에 분리했으며 보존 영역 전체를 활성화하지 않습니다.
- 복사된 과거 문서의 완료 표시는 gpt 이전 이력입니다. 다른 환경의 trusted·자동 승인·profile 설정이 현재 설치됐다고 가정하지 않습니다.

## 3. 원본 관리와 갱신

후속 개선은 codex에서 진행하며 gpt를 다시 복사해 덮어쓰지 않습니다. BASELINE_MANIFEST는 최초 복사 기준으로 유지하고 release manifest와 구분합니다. codex/AGENTS.md와 이 README는 배포본 개발·설치 경계를 위해 재작성했으며 원문은 gpt에 남아 있습니다.

개인 홈 설치와 전체 배포는 별도로 기록합니다. 문서·해시 검사 통과를 모델 행동·hook·복구의 실행 검증 완료로 확대하지 않습니다.

## 4. 근거

- Codex 지침: [공식 AGENTS.md 문서](https://learn.chatgpt.com/docs/agent-configuration/agents-md) — ★★★☆☆
- Subagents: [공식 위임 설정 문서](https://learn.chatgpt.com/docs/agent-configuration/subagents) — ★★★☆☆

## 5. 중앙 governance skill 후보

두 governance 역할의 소유권·필수 정책 읽기·발견 경로·초안 생성 범위는 [Codex governance 구성](CODEX_GOVERNANCE.md)을 따릅니다. 기존 독립 payload와 정책 합성 후보의 파일 집합을 구분합니다.

---

**작성일**: 2026-09-04

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
