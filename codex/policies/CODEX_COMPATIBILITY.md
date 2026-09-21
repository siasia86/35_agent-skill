# Codex 호환성 적용 규칙

## 1. 보존 원칙

기준 원본은 이 저장소의 `kiro/`입니다. 홈 디렉터리의 실행 환경으로 원본을 대체하지 않습니다. 문서 형식, 푸터, 별점, PLAN 오류 기록, TODO 배치, Git 메시지, 테스트 및 운영 규칙을 보존합니다. 원본과 대상 경로·SHA-256은 `MIGRATION_MANIFEST.json`에 기록합니다.

## 2. 실행과 승인

사용자가 승인한 범위의 읽기·편집·검증·기록 갱신은 중간 재확인 없이 진행합니다. 기존 승인 범위를 넘어서는 작업과 실제로 필요한 사용자 결정만 확인합니다. 진행 보고는 계속 제공합니다.

원본의 `항상 확인`과 `절대 묻지 않음`이 충돌하면 이미 승인된 범위와 현재 Codex 실행 정책을 기준으로 판단합니다. 설정의 자동 검토는 허용 가능한 실행 요청을 대신 판단하며, 권한을 무조건 부여하지 않습니다. 지침 파일로 현재 세션의 샌드박스·OS 권한을 우회하지 않습니다.

이전 세션의 종료되지 않은 SSH 프로세스를 일괄 종료하거나, 단순 지침 로딩을 이유로 서비스·VM·배포 명령을 실행하지 않습니다. 원본 예시는 작업 대상과 실행 권한이 확인된 경우에만 사용합니다. 원본 정책의 충돌은 `../ISSUE.md`에 보존합니다.

## 3. Codex 표현

- `skill://name`은 `$name`과 `.agents/skills/name/SKILL.md`로 대응합니다. 사용 전에 실제 Skill 파일을 읽습니다.
- `prompts/` 파일은 수동으로 읽는 요청 예시입니다. `${1}` 등은 자리표시자이며 Codex가 자동 치환한다고 가정하지 않습니다.
- `/agent swap`과 `/prompts`는 Kiro 문법입니다. 역할 이름을 자연어로 요청하거나 해당 지침 파일을 읽습니다.
- 원본 모델은 고정하지 않고 현재 Codex 모델·추론 수준을 상속합니다.
- Kiro의 `tools`, `allowedTools`, hooks, `TOOL_INPUT_path`는 Codex 설정으로 복사하지 않습니다. 목적과 미지원 상태는 ISSUE에 남깁니다.
- AWS CLI 또는 MCP, 외부 검사 스크립트, 잠금 기능은 실제 설치와 권한을 확인해야 합니다. 미설치 기능을 성공했다고 보고하지 않습니다.
- 개인 메모리·세션·키는 이식하지 않습니다. 원본의 메모리 관리 규칙은 보존하지만 실제 파일을 자동 생성하거나 읽지 않습니다.

## 4. 범위와 우선순위

플랫폼의 시스템·개발자 지침과 관리 정책 안에서 사용자 지시, 대상 저장소 규칙, 이식한 커스텀 규칙을 적용합니다. `31_governances`의 문서 정책은 `DOCUMENT_WORKFLOW.md`에 연결합니다. 변경 가능한 과거 사실은 원본에 남아 있어도 실제 환경에서 확인합니다.

원본의 특정 저장소 경로·branch·푸터 URL·모델 언급을 모든 저장소에 일반화하지 않습니다. 대상이 다르거나 충돌하면 ISSUE에 기록합니다. 사용하지 않는다고 판단한 Skill도 이슈 없이 제거하지 않습니다.

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
