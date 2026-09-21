# AI 운영 설정 통합 관리 및 Codex 배포 TODO
<!-- reference: _reference/32_system-engineering-resources/ref_codex_cli_official_notes.md -->

작성일: 2026-09-21
마지막 업데이트: 2026-09-21

이 문서는 31에서 저장소별 AI 운영 구성을 통합 관리하고, 35의 재사용 지침·skill·agent와 30의 검사 도구를 조합하여 배포하기 위한 계획입니다. 사용자가 요청한 원본 보존과 복사 기반 사용을 기준으로 기존 TODO를 재정리했습니다.

이번 작업 범위는 이 TODO의 상세화와 전체 사실 검증입니다. `codex/` 생성, 개인 홈 설치, 30·31 수정, hook 활성화와 consumer 적용은 아래의 미완료 작업입니다. 여기서 consumer는 공통 설정을 적용받는 대상 저장소를 뜻합니다.

## 목차

- [1. 목표와 기존 판단 정정](#1-목표와-기존-판단-정정)
- [2. 확인된 현재 상태](#2-확인된-현재-상태)
- [3. 저장소별 책임과 통합 관리 구조](#3-저장소별-책임과-통합-관리-구조)
- [4. 저장소 유형별 구성과 예외](#4-저장소-유형별-구성과-예외)
- [5. gpt 보존과 codex 배포본 작성](#5-gpt-보존과-codex-배포본-작성)
- [6. 개인 공통 설치와 프로젝트 설치](#6-개인-공통-설치와-프로젝트-설치)
- [7. Skill과 subagent 재검토](#7-skill과-subagent-재검토)
- [8. Gitleaks와 Markdown 검사 및 hook 연결](#8-gitleaks와-markdown-검사-및-hook-연결)
- [9. 배포 계약과 갱신 및 복구](#9-배포-계약과-갱신-및-복구)
- [10. 실행 순서와 완료 조건](#10-실행-순서와-완료-조건)
- [11. TODO 전체 검토와 사실 검증 기록](#11-todo-전체-검토와-사실-검증-기록)

## 1. 목표와 기존 판단 정정

사용자가 설명한 31의 목적은 각 저장소 성격에 맞는 AI 운영 지침, 공통·전용 skill과 agent, 비밀정보 검사 설정, Markdown 검사 및 hook 설정을 중앙에서 관리하는 것입니다. 아래 설계는 그 목적을 구현하기 위한 제안이며, 이미 구축된 기능과 구분합니다.

- [x] `gpt/`의 agent·skill이 여러 환경에서 복사해 사용하는 재사용 자산이라는 목적을 반영했습니다.
- [x] 개인 표준이나 특정 경로 의존성만으로 skill을 삭제 후보로 분류했던 판단을 철회했습니다.
- [x] `gpt/`는 보존하고 `codex/`에서 이식성을 개선하도록 계획을 통일했습니다.
- [ ] 31에서 어떤 지침·skill·agent·검사·hook을 어느 저장소에 적용할지 관리하도록 구성 계약을 확장합니다.
- [ ] “복사 가능한 배포본”의 기준을 참조 파일 누락 없이 지정 위치에 배치 가능한 패키지로 정의합니다. 실행 도구 설치와 hook 신뢰 설정까지 파일 복사만으로 끝난다고 가정하지 않습니다.
- [ ] 개인 공통 설정과 저장소별 설정을 함께 지원하고, 기존 개인 규칙을 보존하면서 대상 저장소의 예외를 적용합니다.

기존 TODO의 “즉시 정리 후보”는 확정된 삭제 목록이 아닙니다. `kiro-lock`은 이식 검토, `zircon-readme-policy`는 적용 범위 제한, `security-tools`는 도구 의존성 정리 대상으로 다시 분류합니다.

## 2. 확인된 현재 상태

아래는 2026-09-21에 확인한 로컬 파일 기준입니다. 원격 최신 release나 실제 배포 성공을 뜻하지 않습니다.

### 2.1 35의 재사용 자산

- `gpt/.agents/skills/`에 `SKILL.md` 25개, `gpt/.codex/agents/`에 TOML 10개가 있습니다.
- [gpt/AGENTS.md](gpt/AGENTS.md)는 skill 외에도 `policies/`, `markdown/STYLE.md`를 참조합니다.
- [fact-check 진입점](gpt/.agents/skills/fact-check/SKILL.md)은 [상세 프롬프트](gpt/prompts/fact-check.md)를 상대 경로로 읽습니다. skill 디렉토리만 따로 복사하면 이 참조는 보장되지 않습니다.
- [이식 manifest](gpt/policies/MIGRATION_MANIFEST.json)는 기존 변환 이력을 기록합니다. 새 배포 이력은 별도로 관리할 계획입니다.
- 원본 파일명은 `docs-reviewer.toml`, `infra-worker.toml`이고 내부 `name`은 각각 `docs_reviewer`, `infra_worker`입니다.

### 2.2 31의 현재 계약과 확장 필요 영역

확인한 근거는 31의 `README.md`, `.governance/repository/consumer_bundle_contract.yaml`, `consumer_governance_structure.md`, `sync_policy.md`, `.governance/profiles/governance_manifest.json`입니다.

- 현재 bundle 계약에 `.gitleaks.toml`, `.md-style-check.toml`, `.md-heading-check.toml`, `.gitignore`, README 및 consumer governance 문서가 명시되어 있습니다.
- 이 계약의 payload 목록에는 아직 Codex `AGENTS.md`, skill·agent, AI hook 설정이 명시되어 있지 않습니다. 통합 배포 지원 여부는 계약과 실행 코드를 추가 검토해야 합니다.
- 로컬 manifest는 `release_status: draft`, `source_ref: v0.1.1-rc.19`입니다. 승인 배포가 완료됐다고 표시하지 않습니다.
- 31의 README와 sync 정책은 runtime 구현을 해당 runtime 저장소에서 관리하도록 구분합니다. AI 구성 선택·배포 관리와 구현 원본 소유권을 연결하는 방식으로 확장할 계획입니다.
- 31 자체 TODO·PLAN을 consumer에 복사하지 않고 consumer용 템플릿을 사용하는 원칙이 있습니다.

### 2.3 30의 검사·동기화 자산

30의 `src/`에는 `md-style-check.py`, `md-heading-check.py`, `md-link-check.py`, `governance_sync.py`가 있고, `src/bin/`에는 대응하는 `sia-*` wrapper가 있습니다.

30의 `docs/governance_sync.md`는 31 release 검사·적용·복구 계약을 설명합니다. 문서상 `check`는 draft를 검사할 수 있지만 `update`와 `update --dry-run`은 draft 적용을 허용하지 않습니다. 이 TODO 작성 중 실제 sync 실행이나 복구 시험을 수행한 것은 아닙니다.

## 3. 저장소별 책임과 통합 관리 구조

다음은 목표 책임 분담입니다. 새 profile 필드와 배포 디렉토리는 구현 전에 확정합니다.

| 영역 | 원본 관리 위치 | 책임 |
|---|---|---|
| 검사·배포 실행 코드 | 30_sia-scripts | Python 검사기, wrapper, 테스트, 배포·복구 실행 |
| 정책·구성 조합 | 31_governances | 공통 AI 운영 기준, 저장소 profile, 검사 설정, hook 연결 정책 |
| 재사용 AI 자산 | 35_agent-skill | 공통 지침, skill·agent, Codex·Kiro 등 도구별 배포본 |
| 실제 적용본·예외 | 각 consumer | 설치된 파일, 저장소 운영 명령, 적용 버전, local exception |

- [ ] 31 profile이 35 자산 버전과 30 도구 버전을 선택하도록 정의합니다.
- [ ] hook adapter 구현의 원본 관리 위치를 확정합니다. 공통 실행 코드는 30, 도구별 AI 설정 예시는 35, 적용 이벤트·검사 선택은 31로 나누는 안을 검토합니다.
- [ ] 31 배포 패키지에 30·35의 검증된 파일을 포함할 수 있도록 하되, 생성된 사본을 별도 구현 원본으로 수정하지 않습니다.
- [ ] 정책 변경은 31, 검사 로직 변경은 30, skill·agent 동작 변경은 35에서 수정하고 조합 버전을 갱신합니다.
- [ ] 31·30·35의 개발·검증이 서로의 최신 실행 환경에 의존하지 않도록 고정 버전과 시험용 입력을 사용합니다.
- [ ] 각 저장소에 필요한 후속 변경은 해당 저장소의 TODO·PLAN으로 연결하되, 31의 중앙 작업 목록 전체를 consumer에 배포하지 않습니다.

대상 저장소에는 `.governance/`를 운영 기준의 중심으로 두고, AI 진입 지침이 해당 문서를 읽도록 연결할 계획입니다. `.governance/`라는 이름만으로 AI·검사 도구가 자동 적용된다고 가정하지 않습니다.

## 4. 저장소 유형별 구성과 예외

아래 profile 이름은 설계 예시이며 현재 구현된 profile ID가 아닙니다.

| 구성 예시 | 선택할 AI 기능 | 검사·운영 기준 |
|---|---|---|
| 개인 공통 | 작업 규칙, 코드 검토, Git 규칙, 검증 | 사용자 선호와 공통 작업 원칙 |
| 문서 저장소 | 문서 작성·검토, fact-check | Markdown 구조·링크·비밀정보 검사 |
| 스크립트 저장소 | Bash/Python 템플릿, 코드 검토 | 구문·테스트·비밀정보 검사 |
| 인프라 저장소 | Ansible 검토, 변경 계획, 보안·복구 | lint·dry-run·권한·rollback 확인 |
| 특정 프로젝트 | 공통 구성에 필요한 전용 규칙 | 푸터 제외, 전용 명령, 적용 경로 |

### 4.1 31 profile에 정의할 정보

- [ ] 저장소 식별자, 유형, 대상 runtime, 개인 설치 또는 저장소 설치 범위를 정의합니다.
- [ ] 사용할 공통 지침·skill·agent 목록과 제외 사유를 기록합니다.
- [ ] 30·31·35 각각의 source commit 또는 release와 파일 checksum을 기록합니다.
- [ ] 검사별 대상 파일, 제외 범위, 설정 파일, 이벤트, 실행 명령, 작업 디렉토리, timeout, 실패 처리를 정의합니다.
- [ ] 최소 runtime·Python·검사 도구 조건을 실제 배포 시험으로 확정합니다.
- [ ] 예외의 범위, 사유, 책임자, 재검토 조건과 복구 방법을 기록합니다.
- [ ] 계정별 실제 홈 경로와 인증정보는 배포된 로컬 환경에서 해석하고 공통 payload에 고정하지 않습니다.

### 4.2 공통 규칙과 저장소 규칙의 관계

- [ ] 개인 공통값을 기본으로 하고 저장소의 명시적 예외를 반영하는 운영 규칙을 31에서 정의합니다.
- [ ] AI 지침의 우선순위, skill 검색, agent 선택, hook 결합을 각각 검증합니다. 모든 파일이 같은 방식으로 덮어써진다고 가정하지 않습니다.
- [ ] 운영 지침이 플랫폼 시스템·개발자 지침, 관리 정책, 실제 OS·sandbox 권한을 변경하는 것으로 표현하지 않습니다.
- [ ] `readme-template`의 배지 대상·라이선스·푸터 제외 규칙과 커밋·branch 규칙을 profile에서 선택할 수 있게 만듭니다.
- [ ] 소비 저장소에서 바꾼 예외는 그 저장소에 보존하고, 공통화할 사항만 원본 변경 절차로 반영합니다.

## 5. gpt 보존과 codex 배포본 작성

35의 목표 구조는 `kiro/` 원본, `gpt/` 변환 보존본, `codex/` 재사용 배포본입니다.

### 5.1 복사와 원본 추적

- [ ] 숨김 디렉토리를 포함해 `gpt/`를 `codex/`로 복사하고 최초 복사 결과를 대조합니다.
- [ ] 편집기 swap·임시 로그·개인 세션 파일은 배포 자산에서 제외하고 기존 파일을 임의 삭제하지 않습니다.
- [ ] 출발 commit과 파일 hash를 기록하고 이후 수정은 `codex/`에 적용합니다.
- [ ] `gpt/`의 원본 규칙·변환 manifest를 보존합니다. 배포 완료 후 원본을 삭제·덮어쓰는 이전 계획은 적용하지 않습니다.
- [ ] 배포본에서 변경한 규칙, 보존한 규칙, 적용 범위를 제한한 규칙의 대응표를 작성합니다.
- [ ] 이후 유지보수 기준을 `codex/`로 정하고, `gpt/`를 다시 일괄 복사해 개선 사항을 덮어쓰지 않도록 갱신 절차를 작성합니다.

### 5.2 패키지와 참조 파일

- [ ] 공통 지침, skill, subagent, 필요한 상세 정책·템플릿·프롬프트를 배포 목록으로 정의합니다.
- [ ] `fact-check` 등 외부 상세 문서를 참조하는 skill의 의존 파일을 포함하거나 skill 내부 `references/`로 옮겨 참조를 수정합니다.
- [ ] `markdown/STYLE.md`, `policies/`, `prompts/`를 누락한 상태에서 진입점만 배포하지 않습니다.
- [ ] 다른 저장소의 로컬 절대 경로는 설치 가능한 도구 명령, 패키지 내부 경로 또는 profile 설정으로 전환합니다.
- [ ] 실제 저장소의 README·TODO·PLAN·CHANGELOG를 배포본 관리 문서로 덮어쓰지 않도록 payload와 배포 설명서를 분리합니다.
- [ ] 배포본을 원본과 다른 임시 경로에 복사하고 원본 저장소 없이 모든 참조 파일에 접근되는지 시험합니다.

## 6. 개인 공통 설치와 프로젝트 설치

다음은 현재 공식 문서의 기본 경로입니다. Codex home을 변경한 환경은 실제 설정을 확인합니다.

| 자산 | 개인 공통 설치 | 프로젝트 설치 |
|---|---|---|
| 지침 | `~/.codex/AGENTS.md` | `<repo>/AGENTS.md` |
| Skill | `~/.agents/skills/<name>/` | `<repo>/.agents/skills/<name>/` |
| Subagent | `~/.codex/agents/*.toml` | `<repo>/.codex/agents/*.toml` |

근거: [공식 지침 문서](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [공식 skill 문서](https://learn.chatgpt.com/docs/build-skills), [공식 subagent 문서](https://learn.chatgpt.com/docs/agent-configuration/subagents).

- [ ] 개인용과 프로젝트용 복사 매핑을 각각 작성합니다. `codex/` 폴더를 임의 위치에 놓는 것과 검색 경로에 설치하는 것을 구분합니다.
- [ ] 프로젝트용 payload는 대상 저장소 루트에 상대 경로를 유지해 배치합니다.
- [ ] 개인 공통 payload는 사용자 홈의 두 경로 계열에 맞추고, runtime별 보조 파일의 위치도 명시합니다.
- [ ] 공통 지침에는 한국어 응답, 최소 변경, 사용자 변경 보존, 비밀정보 취급, 검증 보고와 governance 탐색을 포함합니다.
- [ ] 기존 `AGENTS.md`·설정·agent와 겹치면 차이를 보여주고 병합합니다. 소비 저장소의 고유 지침을 통째로 교체하지 않습니다.
- [ ] 개인·프로젝트에 같은 이름의 skill이 중복 설치되지 않도록 배포 목록을 검사합니다.
- [ ] 프로젝트 루트와 하위 디렉토리, 서로 다른 저장소에서 실제 로딩과 참조 경로를 시험합니다.

공식 skill 문서는 같은 이름의 skill을 자동 병합하지 않으며 둘 다 선택 목록에 나타날 수 있다고 설명합니다. 지침 파일의 가까운 경로 우선 규칙을 skill 덮어쓰기 규칙으로 일반화하지 않습니다. [공식 skill 검색 규칙](https://learn.chatgpt.com/docs/build-skills)

기존의 “전역 지침 32 KiB 제한”은 부정확합니다. 공식 설명은 지침 결합 크기에 적용하는 `project_doc_max_bytes`의 기본값이 32 KiB라는 것이며 설정할 수 있습니다. 공통 지침은 간결하게 유지하고 상세 절차를 별도로 읽게 할 계획입니다. [공식 지침 검색 규칙](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## 7. Skill과 subagent 재검토

### 7.1 Skill 25개 분류

아래는 삭제 결정이 아닌 배포 후보 분류입니다. 전역 설치 여부와 활성 범위는 31 profile에서 선택할 계획입니다.

- [ ] 공통 운영: `work-rules`, `using-skills`, `repo-governance`의 목적을 보존하고 역할 중복·지침 충돌을 정리합니다.
- [ ] 검토·검증: `code-review`, `security-audit`, `fact-check`, `testing-and-verification`, `testing-guide`를 재사용 후보로 유지합니다.
- [ ] 문서: `markdown-review`, `md-link-check`, `readme-template`를 유지 후보로 두고 검사 도구·배지·푸터 값을 분리합니다.
- [ ] Git: `git-commit-rule`, `git-release`를 유지 후보로 두고 한국어·길이 선호를 보존합니다. 원본에 고정된 branch 이동·push 대상은 저장소 설정으로 전환합니다.
- [ ] 스크립트: `bash-script-template`, `python-script-template`의 개인 표준을 보존합니다. 절대 경로, 작성자 예시, 응답 표식, Bash `eval` 사용 조건을 각각 검토합니다.
- [ ] 인프라: `ansible-review`, `debugging-and-recovery`, `doubt-driven-infra`, `incremental-change`, `planning-and-breakdown`, `shipping-checklist`, `spec-driven-infra`를 인프라 구성 후보로 유지합니다.
- [ ] 잠금: `kiro-lock`의 수동 잠금 절차와 Kiro hook 연결을 분리하여 이식 가능성을 검토합니다. 잠금 소유권·경쟁 조건·중단 후 복구를 검증하기 전 자동 활성화하지 않습니다.
- [ ] 도구 연결: `security-tools`의 도구 위치·설치 조건을 확인합니다. 개인 경로를 사용한다는 이유만으로 기능을 삭제하지 않습니다.
- [ ] 저장소 예외: `zircon-readme-policy`의 푸터 제외 목적을 보존하고 Zircon 구성에만 연결합니다.

각 원본은 [gpt skill 디렉토리](gpt/.agents/skills/)에서 확인합니다. `readme-template`에는 이미 푸터 제외 대상이 있으므로 “모든 Markdown에 예외 없이 강제”한다고 기술하지 않습니다.

### 7.2 Subagent 10개 분류

아래 파일명은 현재 원본을 기준으로 합니다.

- [ ] `reviewer.toml`, `code-reviewer.toml`: 일반 검토와 기술 영역별 검토의 차이를 대조하고 중복 기능만 정리합니다.
- [ ] `docs-reviewer.toml`, `doc-reviewer.toml`: 사실 검증 라우팅과 문서 형식 검사의 경계를 정의합니다.
- [ ] `security-auditor.toml`: 보안 전문 역할을 유지 후보로 둡니다. 일반 reviewer와 강제로 통합하지 않습니다.
- [ ] `markdown-writer.toml`: 문서 작성 역할을 보존하고 스타일·푸터·검사 경로를 선택 가능한 의존성으로 바꿉니다.
- [ ] `git-manager.toml`: 개인 Git 관례를 유지하면서 저장소 branch·실행 권한을 분리합니다.
- [ ] `system-engineer.toml`, `infra-worker.toml`: 인프라 판단·구현 역할과 위임 범위를 구체화합니다.
- [ ] `se-lite.toml`: 질의·분석 역할과 쓰기 권한을 정합하게 만듭니다. 현재 파일의 `sandbox_mode`는 `workspace-write`입니다.
- [ ] 검토용 agent의 실제 권한을 점검합니다. 현재 `reviewer.toml`과 `docs-reviewer.toml`은 `read-only`이고, 나머지 8개는 `workspace-write`입니다.
- [ ] `name`·파일명 대응, `description`, `developer_instructions`, 모델·추론·MCP 의존성을 검증합니다.
- [ ] model을 고정하지 않는 개인 기본값과 역할별 override를 구분하고, 배포 대상 runtime에서 실제 위임·권한 상속을 검증합니다.

근거: [현재 agent 파일](gpt/.codex/agents/)과 [공식 custom agent 문서](https://learn.chatgpt.com/docs/agent-configuration/subagents). 설치 파일이 있다는 사실만으로 주 세션 역할이나 subagent 실행 성공이 확정되지는 않습니다.

## 8. Gitleaks와 Markdown 검사 및 hook 연결

### 8.1 중앙 관리 대상

- [ ] 31에서 `.gitleaks.toml`, `.md-style-check.toml`, `.md-heading-check.toml`의 기본값과 소비 저장소별 예외를 관리합니다.
- [ ] 30 검사기 버전·설치 명령·호출 경로를 profile에 연결하고 Python 실행 조건을 검증합니다.
- [ ] 검사 설정과 실행 코드를 함께 제공하는 오프라인 패키지 또는 선행 도구 설치 방식 중 배포 형태를 명시합니다.
- [ ] 설치되지 않은 검사기를 건너뛴 결과를 통과로 기록하지 않고 미설치·미검증 상태를 보고합니다.
- [ ] 보안 검사에는 합성 시험 자료를 사용하고, 실제 자격증명이나 운영 로그를 테스트 자료로 복사하지 않습니다.

### 8.2 실행 시점별 구성안

- [ ] AI hook: 관련 편집 이벤트 뒤 변경 파일의 빠른 검사를 실행하도록 설계합니다.
- [ ] Git hook: 커밋 대상 내용과 작업 트리가 다를 때 검사 범위를 구분하도록 구현합니다.
- [ ] CI: 개인 환경과 별개로 공통 검사를 반복할 수 있는 workflow를 구성합니다.
- [ ] 세 경로가 같은 검사 코드와 profile 설정을 사용하고, 이벤트별 파일 선택 방식만 분리합니다.
- [ ] 삭제·이름 변경·공백 경로·하위 디렉토리 실행·검사 실패·timeout을 시험합니다.
- [ ] formatter나 자동 수정이 hook을 재호출하는 순환과 개인·프로젝트 hook의 중복 실행을 확인합니다.
- [ ] 기존 hook을 보존하면서 연결하는 절차와 비활성화·복구 방법을 문서화합니다.

이 항목들은 구현 목표이며 현재 자동 실행이 완료됐다는 의미가 아닙니다.

### 8.3 Codex hook 호환성

현재 공식 문서는 사용자·프로젝트의 `hooks.json` 또는 `config.toml` 내 hook 설정을 지원한다고 설명합니다. Kiro JSON을 그대로 복사하는 대신 이벤트·입력·종료 결과를 확인해 변환할 계획입니다. [공식 Hooks 문서](https://learn.chatgpt.com/docs/hooks)

공식 문서상 여러 출처의 일치하는 hook은 함께 실행되며, 상위 설정이 하위 hook을 단순 대체하지 않습니다. 비관리 hook은 정의에 대한 신뢰 확인이 필요하고 프로젝트 hook에는 프로젝트 신뢰 조건도 있습니다. 따라서 “복사만으로 자동 실행”을 완료 기준으로 삼지 않습니다. [공식 hook 검색·신뢰 규칙](https://learn.chatgpt.com/docs/hooks)

- [ ] 설치된 Codex 버전에서 지원하는 hook 이벤트·입출력·신뢰 절차를 확인하고 최소 지원 버전을 기록합니다.
- [ ] 개인 공통 hook과 프로젝트 hook의 중복·적용 범위를 점검합니다.
- [ ] Codex·Kiro용 adapter를 분리하고 검사 Python 코드의 불필요한 복제를 피합니다.
- [ ] 원본에 남은 “hook 미지원” 기록을 현재 기능과 대조하고, 보존본은 유지하면서 배포본의 설명을 갱신합니다.

## 9. 배포 계약과 갱신 및 복구

31의 현재 [sync 정책](../31_governances/.governance/repository/sync_policy.md)과 [bundle 계약](../31_governances/.governance/repository/consumer_bundle_contract.yaml)을 확장하는 계획입니다. 새 필드를 추가했다고 현재 30 도구가 이를 처리한다고 가정하지 않습니다.

- [ ] 31 계약에 AI 지침·skill·agent·hook 파일과 개인 설치 범위를 추가할 수 있는지 검토합니다.
- [ ] 자산별 source 저장소·commit·버전·상대 경로·checksum·대상 위치를 기록합니다. 초기 `gpt` 출처와 이후 `codex` 배포 commit을 구분합니다.
- [ ] 하나의 profile이 참조하는 30·31·35의 호환 조합을 고정합니다.
- [ ] 생성 파일, 공통 관리 구간, 사용자 소유 파일을 구분하고 충돌 시 자동 덮어쓰기 대신 차이를 보고합니다.
- [ ] dry-run에서 추가·변경·충돌·누락 의존성을 보여주고 실제 변경 여부를 구분합니다.
- [ ] 적용 전 기존 지침·skill·agent·hook·검사 설정과 적용 버전을 snapshot합니다.
- [ ] 동일 패키지를 재적용해도 변경이 누적되지 않도록 구현합니다.
- [ ] 여러 파일 적용 중 실패한 경우 전체 상태를 복구할 수 있게 합니다. 파일 하나의 atomic 교체만으로 전체 배포가 atomic하다고 표현하지 않습니다.
- [ ] 배포한 파일 목록과 hash를 기반으로 복구하고, 사용자 후속 수정과 원래 존재하던 파일을 보존합니다.
- [ ] 31의 draft 후보는 검사 대상으로 관리하고 기존 정책에 맞는 approved release에서 consumer 적용을 수행합니다.
- [ ] 검증·복구 결과는 소비 저장소의 governance 이력에 기록하고 기존 프로젝트 CHANGELOG를 통째로 덮어쓰지 않습니다.
- [ ] 처음에는 수동 복사 매핑과 검증 절차를 완성하고, 30의 자동 배포 확장은 계약 시험 후 연결합니다.

31과 consumer의 governance 문서가 위치상 가까워야 한다는 전제를 배포물에 넣지 않습니다. 위 상대 링크는 이 작업 환경의 검토 근거이며 consumer payload의 실행 의존성이 아닙니다.

## 10. 실행 순서와 완료 조건

### 10.1 우선 실행 순서

1. 35에서 `gpt/`를 보존하고 `codex/` 복사본과 원본 대응 목록을 작성합니다.
2. 35에서 모든 지침·skill·agent 참조 파일을 포함해 경로와 runtime 의존성을 정리합니다.
3. 31에서 개인 공통·문서·스크립트·인프라 profile과 소유권 계약을 구체화합니다.
4. 30·35 자산으로 선택된 profile의 개인용·프로젝트용 payload를 조립합니다.
5. 빈 시험 저장소에서 신규 설치, 기존 지침이 있는 시험 저장소에서 갱신을 확인합니다.
6. 지원 runtime에서 skill 호출·agent 위임·hook 실행·검사 실패 전달을 확인합니다.
7. 승인 후보의 checksum·복구 시험 결과를 기록하고 31의 배포 절차에 따라 적용합니다.

### 10.2 완료 조건

- [ ] `kiro/`·`gpt/` 원본과 기존 사용자 규칙의 보존 여부를 확인했습니다.
- [ ] 25개 skill과 10개 agent 각각의 유지·변환·profile 제한·보류 근거가 대응표에 있습니다.
- [ ] 배포본이 원본 저장소나 개인 절대 경로 없이 필요한 상세 문서를 읽습니다.
- [ ] 개인 공통 설정이 서로 다른 저장소에서 로드되고 저장소 예외가 의도한 범위에 적용됩니다.
- [ ] skill·agent·hook 각각의 이름 중복·권한·설정 결합 시험을 통과했습니다.
- [ ] 필요한 도구가 없는 환경에서 누락을 보고하며 검증 성공을 허위로 기록하지 않습니다.
- [ ] 신규 설치·재적용·기존 설정 충돌·실패 복구·이전 버전 복귀를 시험했습니다.
- [ ] 파일 복사, 활성화, 실제 동작 검증 상태를 따로 기록했습니다.
- [ ] 운영자 README에 설치 위치, 선행 조건, 사용 예, 검사·갱신·복구 절차를 포함했습니다.

## 11. TODO 전체 검토와 사실 검증 기록

### 11.1 검토 방법과 범위

검토일은 2026-09-21입니다. 지정한 [fact-check skill](gpt/.agents/skills/fact-check/SKILL.md)과 [상세 절차](gpt/prompts/fact-check.md)를 따라 TODO 전체의 사실 주장을 대조합니다.

이번 요청의 상세 계획 작성과 사실 검증 단계를 구분합니다. 상세 계획을 작성한 뒤에는 새 설계 내용을 사실 검증 명목으로 추가하지 않고, 오류 수정과 검증 상태 표시만 수행합니다.

`_reference`의 Codex 메모는 2026-09-03 확인 자료로 대조했으며, 새 skill·agent·hook 기능을 확정하는 근거로 확대하지 않았습니다. 현재 동작 주장은 아래 공식 문서, 저장소 현황 주장은 실제 로컬 파일을 기준으로 확인합니다.

### 11.2 1차 검토에서 바로잡은 항목

- ❌ 개인 규칙·절대 경로 때문에 불필요하다는 판단: 사용자 재사용 목적과 불일치하여 삭제 후보에서 유지·이식·범위 제한 후보로 수정했습니다. 근거는 이번 사용자 요구와 [원본 skill](gpt/.agents/skills/)입니다.
- ❌ `kiro-lock`을 hook 전용이라고 한 설명: 수동 잠금 절차도 있어 수정했습니다. 근거는 [원본 잠금 skill](gpt/.agents/skills/kiro-lock/SKILL.md)입니다.
- ❌ 모든 Markdown에 푸터가 강제된다는 설명: 명시된 제외 대상을 반영했습니다. 근거는 [원본 푸터 규칙](gpt/.agents/skills/readme-template/SKILL.md)입니다.
- ❌ `docs_reviewer.toml`·`infra_worker.toml` 파일명: 실제 파일명인 `docs-reviewer.toml`·`infra-worker.toml`과 내부 이름을 구분했습니다. 근거는 [agent 디렉토리](gpt/.codex/agents/)입니다.
- ❌ `se-lite`를 현재 읽기 전용 설정으로 볼 수 있는 표현: 현재 `workspace-write`이며 읽기 전용 전환은 TODO로 남겼습니다. 근거는 [se-lite.toml](gpt/.codex/agents/se-lite.toml)입니다.
- ❌ 전역 지침의 고정 32 KiB 제한: 결합 지침과 설정 가능한 기본값으로 수정했습니다. 근거는 [공식 지침 문서](https://learn.chatgpt.com/docs/agent-configuration/agents-md)입니다.
- ❌ 프로젝트 설정이 공통 설정을 일괄 덮어쓴다는 일반화: skill 중복과 hook 결합을 분리했습니다. 근거는 [Skills](https://learn.chatgpt.com/docs/build-skills)와 [Hooks](https://learn.chatgpt.com/docs/hooks)입니다.
- ❌ 복사만으로 hook 실행까지 완료된다는 해석: 설치·신뢰·runtime 확인을 별도 완료 조건으로 기록했습니다. 근거는 [공식 Hooks 문서](https://learn.chatgpt.com/docs/hooks)입니다.
- ❌ 보존본 `gpt/`를 전환 후 정리한다는 계획 충돌: 보존본 유지와 `codex/` 개선으로 통일했습니다. 근거는 사용자의 원본 보존 요청입니다.

### 11.3 재검증과 미검증 범위

- [ ] TODO 전체의 사실·설계·미완료 상태와 내부 참조를 다시 확인합니다.
- [ ] Markdown style·heading·link 및 whitespace 검사를 수행하고 결과를 기록합니다.
- [ ] 문서의 비밀정보 검사를 수행하고 결과를 기록합니다.

설치된 Codex의 기능별 동작, 소비 저장소 배포, runtime별 hook 활성화, 원격 release 승인, rollback 성공은 이번 문서 검토의 실행 검증 대상이 아닙니다. 이 항목들은 검증 완료로 표시하지 않습니다.

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-21
