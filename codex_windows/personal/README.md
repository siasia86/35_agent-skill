# Windows 공통 지침과 설정 이관

현재 저장소에 존재하는 활성 원본 **2개**를 모두 이관합니다. 실제 홈의 개인 config를 수집·게시하거나 덮어쓰지 않습니다.

## 1. 출처와 결과

| 원본                             | Windows 결과                               | 보존과 변경                                                                                 |
|----------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------------|
| `codex_linux/personal/AGENTS.md` | [AGENTS.md](AGENTS.md)                     | 23행 원문 전체 + Windows 적용 절; [원문](references/linux-AGENTS.md) bytes 보존             |
| 저장소 `.codex/config.toml`      | [config.example.toml](config.example.toml) | 공통 3개 값 유지 + Windows sandbox 예시; [공통 원문](config.shared.example.toml) bytes 보존 |

공통값은 `approval_policy = "on-request"`, `approvals_reviewer = "auto_review"`, `sandbox_mode = "workspace-write"`입니다. `auto_review`는 승인 검토자를 선택하며 sandbox를 해제하지 않습니다. [공식 설정 기준](https://learn.chatgpt.com/docs/config-file/config-reference)

Windows 예시는 `[windows] sandbox = "elevated"`를 추가합니다. 해당 모드의 실제 준비·관리 정책을 확인하고 필요한 경우 허용된 fallback을 판단합니다. 이 설정 예시를 작성하는 것이 관리자 권한·OS 설정 변경을 실행한 상태는 아닙니다. [공식 Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox)

## 2. 이관 범위와 미제공 자료

활성 Linux 모음에는 별도 `config.toml`·agent TOML·MCP·hooks 설정이 없습니다. 로컬 WSL 두 배포판의 기본 Codex home에서도 `config.toml`·`AGENTS.md` 부재를 파일 존재 여부로 확인했습니다. 다른 기기·다른 `CODEX_HOME`·원격 서버의 실제 개인 설정은 제공되지 않았으며 이관 완료로 주장하지 않습니다. `105_backup/codex`의 폐기 설정은 이력으로 보존하며 현행 설정으로 부활시키지 않습니다.

모델·provider·MCP·SSH key·인증·개인 경로를 새 예시에 임의로 추가하지 않습니다. 기존 저장소 `.codex/config.toml`과 적용 중인 개인 설정을 유지합니다.

## 3. 실제 적용 절차

기본 개인 설정은 Codex home의 `config.toml`, 공통 지침은 `AGENTS.md`입니다. 기존 파일·override·관리 정책을 먼저 확인하고 필요한 항목만 비교·병합한 뒤 실제 로드 값과 행동을 확인합니다. 저장소 `.codex/config.toml`은 신뢰된 프로젝트에서 별도 계층으로 읽힙니다. [공식 config 계층](https://learn.chatgpt.com/docs/config-file/config-basic), [공식 AGENTS 발견](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

이관 파일의 생성·TOML 구문 검사는 실제 개인 홈 적용·Codex 발견을 대신하지 않습니다. 이번 작업은 저장소 이관과 검증이며 실제 홈의 일괄 교체는 미실행입니다. 되돌릴 때는 적용 전 비교·백업과 현재 사용자 변경을 대조해 이번 변경만 복구합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
