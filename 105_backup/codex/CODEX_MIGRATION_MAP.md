# Kiro와 Codex 대응표

## 1. 원본 보존

19개 `kiro/skills/<name>/SKILL.md`는 같은 이름의 `gpt/.agents/skills/<name>/SKILL.md`로 대응합니다. 7개 `kiro/agents/<name>.json`은 같은 이름의 `gpt/.codex/agents/<name>.toml`로 대응합니다. 13개 원본 Prompt는 `gpt/prompts/`에 보존합니다.

개별 원본·대상 경로와 SHA-256은 [manifest](policies/MIGRATION_MANIFEST.json)에 기록합니다. 1차 구현에서 보류했던 bash/python template·잠금·저장소별 정책을 포함합니다.

## 2. 정책 연결

- work-rules, repo-governance, using-skills: AGENTS에서 먼저 읽도록 연결합니다.
- readme-template, markdown/STYLE.md: 일반 문서 작성 시 푸터·별점·스타일을 적용합니다.
- work-rules §23·§26: PLAN 즉시 기록과 TODO 배치 보고를 유지합니다.
- git-commit-rule: 기존 타입·한국어·길이·branch 규칙을 대상 저장소 정책과 대조합니다.
- system-engineer: 주 세션 역할을 유지하고 같은 이름의 custom agent도 제공합니다.

## 3. 호환성 변경

Skill URI·자산 경로와 Agent 설정 형식만 변환합니다. 모델은 현재 Codex 세션을 상속합니다. Prompt 자리표시자는 수동 입력입니다.

Kiro hooks, 개인 메모리, tools 목록, 특정 외부 경로의 실행 가능성을 보장하지 않습니다. 원문 규칙은 유지하고 [ISSUE.md](ISSUE.md)에 미지원 항목을 기록합니다.

## 4. 이전 구현과의 관계

이전 보조 Skill인 fact-check, markdown-review, ansible-review, security-audit, testing-and-verification, git-release와 역할 reviewer, docs_reviewer, infra_worker는 호환 진입점으로 남깁니다. 원본 상세 규칙을 우선 읽도록 연결하며, 원본 역할 이름 사용을 기본으로 합니다.

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
