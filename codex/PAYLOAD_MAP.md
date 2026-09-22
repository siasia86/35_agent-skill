# 선택형 payload 설치 매핑

## 1. 적용 범위

Batch 2·6 개발 후보입니다. 최소 개인 지침 외에는 실제 개인 홈 설치가 완료된 상태가 아닙니다. 원본 보존 영역인 .agents·.codex 전체를 복사하지 않고 아래 목록만 선택합니다. README·TODO·manifest는 운영 대상에 덮어쓰지 않습니다.

| 배포 원본                                     | 개인 설치 대상                                   | 프로젝트 설치 대상                       |
|-----------------------------------------------|--------------------------------------------------|------------------------------------------|
| payload/personal/AGENTS.md                    | 실제 Codex home의 AGENTS.md                      | 저장소 AGENTS.md에 필요한 공통 원칙 병합 |
| payload/skills/fact-check/                    | 실제 사용자 홈의 .agents/skills/fact-check/      | 저장소 .agents/skills/fact-check/        |
| payload/skills/markdown-review/               | 실제 사용자 홈의 .agents/skills/markdown-review/ | 저장소 .agents/skills/markdown-review/   |
| payload/agents/reviewer.toml                  | 실제 Codex home의 agents/reviewer.toml           | 저장소 .codex/agents/reviewer.toml       |
| payload/agents/docs-reviewer.toml             | 실제 Codex home의 agents/docs-reviewer.toml      | 저장소 .codex/agents/docs-reviewer.toml  |
| payload/skills/&lt;Batch 6 skill&gt;/SKILL.md | 실제 사용자 홈의 .agents/skills/&lt;name&gt;/    | 저장소 .agents/skills/&lt;name&gt;/      |
| payload/agents/&lt;Batch 6 agent&gt;.toml     | 실제 Codex home의 agents/&lt;name&gt;.toml       | 저장소 .codex/agents/&lt;name&gt;.toml   |

공식 기본 경로는 [Skills](https://learn.chatgpt.com/docs/build-skills), [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)에 근거합니다. 사용자 홈과 Codex home을 같은 변수로 가정하지 않습니다. agent 내부 이름은 TOML과 catalog에서 확인하며 모델 ID는 고정하지 않습니다. 개인·프로젝트 중 필요한 범위를 선택하고 중복 설치를 기본으로 하지 않습니다.

## 2. 원본 대응과 변경 사유

- fact-check: 기존 .agents/skills/fact-check 진입점과 prompts/fact-check의 사실 검증 항목을 통합했습니다. 외부 정책 파일 필수 참조를 없애고 검토와 수정 권한을 분리했습니다. 공식 근거·전체 대상 검토·최대 두 번 재검증 의도는 유지합니다.
- markdown-review: 기존 진입점과 prompts/md-review의 구조·링크·표·예시 검토를 자체 완결형으로 이식합니다. 프로젝트별 푸터·배지·내부 문서 규칙은 적용 정책이 있을 때만 사용합니다.
- reviewer: 기존 읽기 전용 역할을 보존하고 부작용 있는 명령·권한 변경·무단 재위임을 금지했습니다.
- docs_reviewer: 읽기 전용 검토를 유지하고 관련 skill이 없으면 실행한 것처럼 보고하지 않도록 합니다.
- Batch 6은 나머지 skill 23개와 agent 8개를 self-contained 후보로 이식했습니다. 모두 선택 후보이며 설치·활성화·release 승인은 수행하지 않았습니다. work-rules는 필수 references 파일을 함께 가지며 나머지 skill은 단일 SKILL.md입니다.  원본의 `prompts/`, `policies/`, Kiro hook, 절대 경로와 고정 branch·권한 지시는 portable 조건과 현재 repository guidance 확인으로 전환했습니다.

### 2.1 Batch 6 정확한 inventory

Static candidates: `ansible-review`, `bash-script-template`, `code-review`, `debugging-and-recovery`, `doubt-driven-infra`, `git-commit-rule`, `git-release`, `incremental-change`, `kiro-lock` (manual protocol only), `md-link-check`, `planning-and-breakdown`, `python-script-template`, `readme-template`, `repo-governance`, `security-audit`, `security-tools`, `shipping-checklist`, `spec-driven-infra`, `testing-and-verification`, `testing-guide`, `using-skills`, `zircon-readme-policy`.

`work-rules` is a companion-resource candidate: its entrypoint installs with `references/operating-rules.md` under the same skill folder. Its catalog v0.2-draft companion object uses the exact source-parent-relative layout required by the planner: `skills/work-rules/` + `references/operating-rules.md`. The planner selects the companion as a separate generated file entry while the original `work-rules` asset ID remains the selection ID. Kiro automatic hook behavior remains explicitly deferred.

Agents: `code-reviewer`, `doc-reviewer`, `git-manager`, `infra_worker`, `markdown-writer`, `se-lite`, `security-auditor`, `system-engineer`.

The exact payload path, SHA-256, target roots, companion inventory, and optional skill relationships are authoritative in [ASSET_CATALOG.json](ASSET_CATALOG.json). Targets are alternatives, not a command to install both. `user_home`, `codex_home`, and `repository` are resolved only by an approved installer or the user’s chosen runtime.

## 3. 설치·갱신·복구 조건

1. 실행 계정·runtime·홈·기존 override와 같은 이름의 skill·agent를 확인합니다. 지침 파일 존재만으로 설치 권한이 생기지 않습니다.
2. 위 목록의 선택 파일과 실제 목적지를 확정합니다. 기존 파일은 내용·해시·권한·소유권을 기록하고 승인된 백업 위치를 정합니다. 심볼릭 링크·권한 거부·동시 변경은 덮어쓰지 말고 원인을 확인합니다.
3. 신규 대상은 선택한 폴더 단위로 배치합니다. 기존 대상은 차이를 검토해 병합하며 전체 폴더 덮어쓰기·삭제 동기화는 하지 않습니다. 복사 전후 해시와 누락 파일을 확인합니다.
4. 새 세션에서 skill 발견과 agent 이름·설정 로딩을 확인합니다. 정적 파싱·수동 지침 전달·실제 이름 기반 위임은 서로 다른 시험입니다.
5. 검토만 요청한 사례, 필수 자료 접근 실패, 로컬 링크 오류로 실제 행동을 시험합니다. 실패하면 해당 설치분만 복구하고 사용자 후속 수정을 보존합니다.
6. 신규 설치 복구는 설치 목록과 현재 해시가 일치하는 파일만 격리하는 방식으로 준비합니다. 기존 파일 갱신 복구는 검증된 백업을 사용합니다. 여러 파일의 중간 실패·재적용·버전 복귀 시험 전에는 복구 보장을 주장하지 않습니다.

자동 설치기·hook·31 release 계약은 이번 목록에 포함하지 않습니다. 이 문서는 설치 절차와 후보 목록이지 실행 완료 증거가 아닙니다. 실제 선택·저장소별 설정·예외의 원본 소유자는 31이며 본 문서는 35의 자산 배치 후보를 설명합니다.

## 4. 중앙 관리 계약과 활성화 경계

- [통합 계약 초안](INTEGRATION_CONTRACT.md)에 따라 31이 선택 명세를 소유하고 30은 명시된 대상·병합·충돌·검증 정책을 실행합니다.
- [자산 목록](ASSET_CATALOG.json)은 35가 제공하는 경로·해시 목록입니다. 미커밋 개발 후보를 승인 release로 사용하지 않습니다.
- 관리 설정의 현장 변경은 보존하고 중앙 원본과 차이를 검출합니다. 31 반영 또는 승인본 재적용 결정 없이 덮어쓰거나 자동 역동기화하지 않습니다.
- 원본 복사와 runtime 설치를 구분합니다. 자동 발견 자산은 runtime 검색 밖 staging에서 검증한 뒤 최종 배치를 활성화로 취급합니다. hook 등록은 별도 검증·승인 단계입니다.
- 실제 적용 기록·운영 로그·snapshot의 최종 보관 위치는 미결정입니다. 기존 복구 자료를 유지하며 본 개발 기록으로 운영 배치를 확정하지 않습니다.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
