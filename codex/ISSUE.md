# Codex 마이그레이션 이슈

## 1. 상태와 처리 원칙

커스텀 규칙은 원본을 보존합니다. 호환성 변경은 근거와 함께 기록하고 기능이 미검증이면 완료로 표시하지 않습니다.

## 2. 열린 이슈

### ISSUE-008: 원본 스타일과 검사기 적용 범위

- 검사: 전체 50개 Markdown 파일에서 137건입니다. 푸터 117건, H1 10건, 다이어그램 한글 4건, 과장 표현 2건, 종결어미 2건, 이모지 2건입니다.
- 원인: 원본 형식을 보존한 Skill·Prompt·정책 예시에 일반 문서 검사가 적용됩니다. SKILL.md 푸터 제외는 원본 readme-template에 명시돼 있습니다. 나머지 원본 표현과 예시는 임의로 삭제하지 않습니다.
- 처리: 새 관리 문서 9개는 검사 예외 없이 0건입니다. 전체 검사를 통과로 표시하지 않으며 원본 정책과 검사기 범위를 별도로 정합화해야 합니다.
- 상태: 원문 보존, 검사 정책 정합화 미완료.

### ISSUE-009: 원본 YAML description 구문

- 원본: bash-script-template, python-script-template의 description 안 `참조:` 문자열입니다.
- 증상: 따옴표로 감싸지 않은 YAML 값 안의 콜론 때문에 YAML parser가 거부합니다.
- 조치: Codex 대상 파일에서 description 전체를 인용 문자열로 감싸고 원문 문구는 보존했습니다.
- 검증: 25개 Skill이 YAML 검사와 skill-creator quick_validate를 통과했습니다.
- 상태: 해결. Kiro 원본은 변경하지 않았습니다.

### ISSUE-001: 이전 변환의 누락과 완료 표시

- 원본: `kiro/skills/`, `kiro/agents/`, `kiro/prompts/`.
- 원인·영향: 1차 축약에서 푸터·별점·문서 생명주기 및 일부 Skill이 누락됐고 전체 읽기·실행 검증이 완료로 표시됐습니다.
- 조치: 19개 원본 Skill과 7개 Agent, 13개 Prompt의 본문을 보존하고 기계적 경로 변환을 적용합니다. 실제 실행 검증은 별도로 남깁니다.
- 상태: 정적 복원 완료, 동작 검증 진행 필요.

### ISSUE-002: Kiro hooks와 도구 설정

- 원본: `kiro/agents/*.json`, `kiro/hooks/md-style-check.sh`.
- 영향: Kiro 이벤트·변수·tools 목록은 Codex에서 그대로 실행되지 않습니다. 감사 로그·diff 출력·자동 Markdown 검사 hook의 동등 동작은 미구현입니다.
- 대안: 지침에서 변경 후 검사 의무를 유지합니다. Codex hook API를 검증한 뒤 별도 구현합니다. AWS는 실제 CLI/MCP 연결이 필요합니다.
- 상태: 미해결. 원본 hook을 실행 가능한 Codex hook이라고 등록하지 않습니다.

### ISSUE-003: 확인 질문·프로세스 종료·잠금 규칙 충돌

- 원본: `work-rules` §1-1·§2·§21·§22, `repo-governance`, `kiro-lock`.
- 영향: 재확인 요구와 확인 금지가 충돌하며, 시작 시 잔존 SSH 종료는 다른 작업을 방해할 수 있습니다. 잠금 스크립트가 Codex에 구현됐다고 가정할 수 없습니다.
- 적용: 기존 승인 범위는 재확인하지 않습니다. 프로세스 소유·작업 범위를 확인하지 않은 일괄 종료는 실행하지 않습니다. 잠금 기능은 실제 의존성을 확인합니다.
- 상태: 원문 보존, 호환성 지침으로 실행 경계 명시.

### ISSUE-004: 외부 의존성과 특정 저장소 값

- 원본: `readme-template`, `git-commit-rule`, `security-tools`, `work-rules`, `zircon-readme-policy`.
- 영향: 푸터 URL, `yunli` branch, `/root/sj_del` 스크립트, Actions 날짜 자동 갱신은 모든 저장소에서 유효하지 않습니다. 별점 표와 예시도 일치 여부를 확인해야 합니다.
- 처리: 원문 보존. 대상 저장소 정책·실제 파일·workflow를 확인한 후 적용합니다. 예시 값만 보고 실행·설치·branch 전환을 하지 않습니다.
- 상태: 저장소별 실행 확인 필요.

### ISSUE-005: 개인 메모리와 모델

- 원본: Agent resources의 `.kiro/.local/memory.md`, 원본 모델명, work-rules §25.
- 처리: 개인 데이터는 복사하지 않습니다. 규칙은 보존하되 자동 메모리 연결은 미구현입니다. Agent 모델·reasoning effort는 현재 Codex 세션에서 상속합니다.
- 상태: 모델 변환 완료, 메모리 연동 보류.

### ISSUE-006: 병행 작업 문서의 접근 권한

- 대상: 저장소 `agent-workflows/gpt/USER_TODO.md`, `UPDATE_TODO.md`.
- 증상: 일반 읽기와 sandbox 밖 읽기 모두 OS Permission denied입니다.
- 영향: 이 문서들과 이번 산출물의 정책 중복·충돌 검증은 미완료입니다.
- 상태: 미해결. 해당 파일과 다른 작업의 루트 변경을 보존합니다.

### ISSUE-007: 자동 검토와 현재 세션

- 설정: 네 저장소의 `.codex/config.toml`, 사용자 `se-repos.config.toml`.
- 결과: 자동 검토 프로필은 Codex 설정 로더로 확인했습니다. 이미 실행 중인 세션의 권한과 OS 파일 권한은 바뀌지 않습니다.
- 처리: 새 세션에서 적용합니다. `never`나 전역 full-access로 변경하지 않습니다. 31의 root 공유 workspace 정책과 이번 명시적 사용자 요청의 차이를 이 이슈에 기록합니다. ACL·소유자는 변경하지 않습니다.
- 상태: 설정 완료, 실제 자동 승인 동작은 새 세션에서 확인 필요.

---

## 통계

![GitHub stars](https://img.shields.io/github/stars/siasia86/system-engineering-resources?style=social)
![GitHub forks](https://img.shields.io/github/forks/siasia86/system-engineering-resources?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/siasia86/system-engineering-resources?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/siasia86/system-engineering-resources)
![License](https://img.shields.io/github/license/siasia86/system-engineering-resources)
![Actions](https://img.shields.io/github/actions/workflow/status/siasia86/system-engineering-resources/update-date.yml)

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-21

© 2026 siasia86. Licensed under CC BY 4.0.
