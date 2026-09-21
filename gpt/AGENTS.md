# Codex project instructions
<!-- reference: ../_reference/32_system-engineering-resources/ref_codex_cli_official_notes.md, ../_reference/32_system-engineering-resources/ref_ai_markdown_design_patterns.md -->

이 디렉터리는 Kiro의 사용자 커스텀 규칙을 보존한 Codex 작업 환경입니다. 기본 역할은 `system-engineer`입니다.

## 필수 지침 로딩

작업 시작 시 아래 파일을 읽고 적용합니다. 이 문서는 상세 규칙을 대체하는 요약본이 아닙니다.

1. `policies/CODEX_COMPATIBILITY.md`: Codex 호환성 경계와 이미 승인된 작업 처리.
2. `.agents/skills/work-rules/SKILL.md`: 원본 작업 규칙 전체, PLAN 기록, TODO 배치 보고.
3. `.agents/skills/repo-governance/SKILL.md`: 대상 저장소 `.governance/` 탐색과 적용 순서.
4. `.agents/skills/using-skills/SKILL.md`: 작업 유형별 Skill 선택.
5. `policies/DOCUMENT_WORKFLOW.md`: ISSUE·TODO·PLAN·CHANGELOG 역할과 갱신.

문서를 생성하거나 수정하기 전에 `markdown/STYLE.md`와 `.agents/skills/readme-template/SKILL.md`를 읽습니다. 푸터·참고 링크 별점·검증 회차를 임의로 생략하지 않습니다. 커밋 작업에는 `.agents/skills/git-commit-rule/SKILL.md`를 적용합니다.

`system-engineer`의 원본 역할은 `.codex/agents/system-engineer.toml`에 보존합니다. 주 세션도 보안 → IaC → 신뢰성 → 비용 순서와 현재 상태 → 변경안·롤백 → 검증 흐름을 따릅니다. 별도 subagent를 만들지 않아도 이 지침은 적용됩니다.

기존 사용자 규칙이 불필요해 보인다는 이유로 삭제하지 않습니다. 충돌·미지원·누락 의존성은 `ISSUE.md`에 원본 위치, 영향, 대안을 기록합니다.

## 작업 규칙

- 사용자의 명시적 범위와 이 파일의 지시를 우선 확인한다.
- 파일을 수정하기 전에 `git status --short`와 대상 파일을 읽는다.
- 최소 변경 원칙을 적용하고, 기존 사용자 변경 사항을 덮어쓰거나 삭제하지 않는다.
- 삭제·덮어쓰기·외부 시스템 변경은 대상과 영향을 먼저 설명하고 승인을 확인한다.
- 자격증명, 토큰, 개인 경로, 세션 데이터는 저장소에 기록하지 않는다.
- Kiro 전용 `skill://`, `/agent`, `/prompts`, hook 명령을 Codex 지시로 사용하지 않는다.
- 기존 Skill의 상세 규칙을 보존하고 이 파일은 해당 규칙을 찾는 진입점으로 사용한다.
- 외부 서비스·소프트웨어의 변경 가능한 사실은 공식 문서로 확인한다.

## 출력과 검증

- 설명과 결과는 한국어로 작성하고 코드·명령·경로·설정 키는 원문 표기를 유지한다.
- 변경 후 `git diff --check`를 실행하고, 변경 유형에 맞는 Markdown·TOML·JSON·스크립트 검사를 수행한다.
- 검증하지 않은 명령 성공, 테스트 통과, 배포 완료를 주장하지 않는다.
- 완료 보고에는 변경 파일, 실행한 검증, 미해결 사항을 포함한다.

## 자산 배치

- 공용 Skill: `.agents/skills/<skill-name>/SKILL.md`
- 프로젝트 custom agent: `.codex/agents/<agent-name>.toml`
- 재사용 프롬프트 예시: `prompts/`
- 공식·비교 참고: 저장소 루트 `_reference/`

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
