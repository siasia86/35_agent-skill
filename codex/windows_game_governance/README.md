# Windows 개인 Codex agent·skill 적용 현황

상태: 2026-09-30 관찰 초안. 사용자 요청 범위의 비식별 runtime `codex-windows-personal`을 기록합니다. 다른 사용자·기기·cloud 환경의 설치 상태를 전수 조사한 결과가 아닙니다.

## 1. 책임과 조회 원칙

35는 재사용 구현과 실제 설치 관찰을 연결합니다. 31은 저장소 이름별 설정·선택 skill의 원본을 관리하고 30은 검사·설치 실행 구현을 관리합니다. 이 디렉터리는 31 정책의 복사본이나 자동 설치 경로가 아닙니다.

어떤 agent 환경에 어떤 skill이 적용되는지 [runtime_inventory.json](runtime_inventory.json)으로 확인합니다. 설치·파일 검증·발견·작업 행동은 서로 다른 상태입니다. runtime ID는 계정명이나 세션 agent ID가 아닌 사용자 범위 적용 환경의 별칭입니다. 일시적인 subagent에게 해당 skill이 모두 로드됐다고 주장하지 않습니다.

## 2. 현재 개인 Codex 자산

| runtime                  | skill                                                                       | 설치·파일 일치 | 발견·대표 행동 |
|--------------------------|-----------------------------------------------------------------------------|----------------|----------------|
| `codex-windows-personal` | [code-review](../payload/skills/code-review/SKILL.md)                       | 확인           | 미검증         |
| `codex-windows-personal` | [debugging-and-recovery](../payload/skills/debugging-and-recovery/SKILL.md) | 확인           | 미검증         |
| `codex-windows-personal` | [markdown-review](../payload/skills/markdown-review/SKILL.md)               | 확인           | 미검증         |
| `codex-windows-personal` | [md-link-check](../payload/skills/md-link-check/SKILL.md)                   | 확인           | 미검증         |

원본 commit은 `4a5dfb17ccbd0dcb5d6da787e3c5133761c06261`이고 네 폴더 전체 inventory·SHA-256이 현재 설치 파일과 같습니다. [기존 setup helper](../scripts/setup_personal_skills.py)의 선택 설치를 사용했습니다. 사용자 범위 설치로 같은 사용자의 프로젝트들에서 사용할 수 있지만 저장소별 설정은 31의 해당 항목을 조회합니다.

개인 AGENTS는 31의 해당 profile 선택 조회와 최소 작업 원칙으로 새로 작성했습니다. payload의 개인 AGENTS를 그대로 복사한 것은 아닙니다. 개인 경로가 있어 본문은 게시하지 않습니다. 기존 config.toml의 model·reasoning·approval·sandbox·MCP·플러그인 값은 변경하지 않았습니다. custom agent TOML·다른 개인 skill·중앙 governance는 설치하지 않았습니다.

## 3. 생성·변경·제거 시 갱신

개인 skill 또는 agent 전용 skill을 새로 만들거나 설치·갱신·제거하면 현황을 함께 갱신합니다. 최소 필드는 runtime/agent 역할, asset ID, 적용 범위, 구현 출처, source commit, 실제 파일 inventory·해시, 확인일, 설치·발견·행동 검증 상태입니다.

새 skill을 만든 사실만으로 자동 선택·행동 검증을 완료 처리하지 않습니다. 사라진 파일·원본과 다른 현장 변경은 누락·drift로 기록하고 임의 덮어쓰지 않습니다. 개인 경로·실제 계정·API key·세션 기록·전체 config·운영 자료는 포함하지 않습니다.

실행기가 runtime을 자동 조회·동기화하는 기능은 아직 없습니다. 이 JSON은 마지막 확인 시점의 관찰이며 자동 발견되는 skill 목록을 생성하는 입력이 아닙니다. 이후 설치가 바뀌면 재관찰과 갱신이 필요합니다. 기기별 로컬 receipt는 비공개로 유지하고 중앙에는 비식별 상태만 반영합니다.

## 4. 다음 검증과 복구

다음 턴 또는 새 Codex 세션에서 네 skill의 발견·명시 호출과 관련 작업 선택을 확인합니다. [공식 skill 안내](https://learn.chatgpt.com/docs/build-skills)에 따라 메타데이터와 선택 본문을 구분하고 전부 매번 읽도록 요구하지 않습니다.

Markdown·JSON·설치 파일·비밀정보·diff 검증과 미실행 범위는 [VERIFICATION.md](VERIFICATION.md)에 기록합니다. 중앙 정책·agent 위임·게임 기능·배포를 이번 설치 검증으로 확대하지 않습니다.

복구는 비공개 로컬 receipt와 설치 파일 해시를 확인한 뒤 이번 신규 파일만 대상으로 합니다. 현장 수정이 있으면 보존하고 차이를 검토합니다. 기존 개인 config·저장소 AGENTS·보존 원본·release·tag를 덮어쓰거나 삭제하지 않습니다. 게시 문서는 검토된 revert로 되돌립니다.

---

**작성일**: 2026-09-30

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
