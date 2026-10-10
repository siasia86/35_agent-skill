# Windows 설정 예시와 개인 홈 적용 안내

공통 지침의 작성 원본은 상위 [AGENTS.md](../AGENTS.md) 한 곳입니다. 이 폴더는 Windows 개인 홈 적용 방법과 설정 예시를 제공합니다. 기존 개인 지침·config·override·관리 정책을 확인하고 필요한 항목만 비교·병합합니다.

## 1. 제공 파일

| 파일                                                     | 용도                                 |
|----------------------------------------------------------|--------------------------------------|
| [공통 AGENTS.md](../AGENTS.md)                           | 공통 작업 기본값과 Windows 적용 지침 |
| [config.example.toml](config.example.toml)               | 공통 설정과 Windows sandbox 예시     |
| [config.shared.example.toml](config.shared.example.toml) | 기존 공통 설정 원본                  |

공통값은 `approval_policy = "on-request"`, `approvals_reviewer = "auto_review"`, `sandbox_mode = "workspace-write"`입니다. `auto_review`는 승인 검토자를 선택하며 sandbox를 해제하지 않습니다. [공식 설정 기준](https://learn.chatgpt.com/docs/config-file/config-reference)

위 값은 배포 예시의 기본값입니다. 현재 개인 설정이나 실제 세션의 권한을 나타내지 않으며, 이번 skill 정리에서 설정과 권한은 변경하지 않습니다.

Windows 예시는 `[windows] sandbox = "elevated"`를 추가합니다. 실제 환경·관리 정책·지원 모드를 확인한 뒤 필요한 경우 허용된 fallback을 판단합니다. 예시 파일 자체가 OS 준비나 관리자 권한을 부여하지 않습니다. [공식 Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox)

## 2. 기존 설정에 적용

기본 개인 설정과 공통 지침은 Codex home의 `config.toml`과 `AGENTS.md`입니다. 기존 파일을 보존하고 선택한 항목만 병합합니다. 저장소 `.codex/config.toml`은 신뢰된 프로젝트에서 별도 계층으로 읽힙니다. [공식 config 계층](https://learn.chatgpt.com/docs/config-file/config-basic), [공식 AGENTS 발견](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

모델·provider·MCP·SSH key·인증·개인 경로는 사용 중인 환경의 값을 유지합니다. 적용 후 실제 로드 값과 대표 작업을 확인하고, 복구가 필요하면 적용 전 비교·백업과 현재 사용자 변경을 대조해 이번 병합분만 되돌립니다.

## 3. 작업 보고 기준

[공통 AGENTS.md](../AGENTS.md)의 작업 시작·완료 보고는 대상 경로·목적·예상 결과와 실제 완료·검증·미실행을 구분합니다. 큰 결과는 표·번호 목록·트리로 보여주고 확인된 성과·문제·제약과 다음 조치를 간단히 남깁니다. 주로 사용하는 [work-rules](../skills/work-rules/SKILL.md)의 해당 절에 역할별 사용 기준이 있습니다. 기존 지침과 비교해 필요한 항목만 병합하며 이 파일 준비를 실제 홈 적용·발견 완료로 보고하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-10

© 2026 siasia86. Licensed under CC BY 4.0.
