# Codex 마이그레이션 계획

## 1. 범위

`kiro/`의 커스텀 규칙을 보존해 `gpt/`에 변환합니다. 자동 검토 설정 대상은 사용자가 지정한 30·31·32·35 저장소입니다. 기존 Kiro 원본과 병행 작업 변경은 보존합니다.

## 2. 단계와 검증

1. 자동 검토: trusted 등록, 프로젝트 설정, 네 writable root 프로필을 TOML 및 Codex 로더로 확인합니다.
2. 원본 복원: Skill 본문과 Agent prompt를 보존하고 URI·경로·설정 형식을 변환합니다. 원본 SHA-256과 대응 경로를 manifest에 남깁니다.
3. 문서 정책: STYLE·푸터·별점·ISSUE/TODO/PLAN/CHANGELOG 흐름을 연결합니다.
4. 정적 검증: 원본 대비 변환 일치, YAML·TOML, 참조, Markdown, diff를 확인합니다.
5. 런타임 검증: 새 세션에서 로딩과 자동/명시 호출을 확인합니다. 정적 검사로 대체하지 않습니다.

## 3. 롤백

이번 추가 파일과 수정 diff만 검토해 개별 복원합니다. 다른 작업의 변경을 포함하는 전체 reset을 사용하지 않습니다. 자동 검토 해제는 이번 프로젝트 설정을 제거하거나 원래 값으로 복원하고 새 세션을 시작합니다. 사용자 기존 모델·TUI 설정은 유지합니다.

## 4. 이슈 기록

### 이슈 3: 원본 템플릿 YAML 파싱

- 증상: Bash·Python Skill description의 콜론이 YAML 구문 오류를 유발했습니다.
- 원인: 원본 description이 인용되지 않은 문자열입니다.
- 해결: 두 description 전체를 인용하고 의미와 본문을 유지했습니다.
- 검증: 원문 대조와 25개 Skill의 공식 quick_validate 통과입니다.

### 이슈 1: 설정 검증 명령 범위

- 증상: doctor에 profile을 전달하거나 debug에 strict-config를 전달하면 명령 자체에서 거부됩니다.
- 원인: 해당 옵션의 지원 범위가 명령별로 다릅니다.
- 해결: `codex --profile se-repos -C <repo> debug prompt-input`으로 모델 요청 없이 설정 로더를 확인했습니다. 출력은 폐기했습니다.
- 검증: sandbox 밖 실행 종료 코드 0. 현재 세션에서는 사용자 설정 디렉터리 쓰기 때문에 권한 상승이 필요했습니다.

### 이슈 2: 병행 변경과 OS 권한

- 증상: agent-workflows 문서가 sandbox 밖에서도 읽기 거부됩니다.
- 처리: ISSUE-006에 기록하고 독립적인 `gpt/` 작업을 진행합니다. 권한·소유자 변경은 수행하지 않습니다.

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
