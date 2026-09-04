# Agent Skill 업데이트 참고 자료

`35_agent-skill`의 Agent·Skill·프롬프트를 업데이트할 때 사용하는 참고 문서 목록입니다. 원본 문서는 `/root/32_system-engineering-resources`에서 복사했으며, 원본 저장소의 문서 내용을 임의로 변경하지 않습니다.

## 목차

| 섹션                                                        |
|-------------------------------------------------------------|
| [1. 사용 원칙](#1-사용-원칙) / [2. 문서 목록](#2-문서-목록) |
| [3. 권장 읽기 순서](#3-권장-읽기-순서)                      |

---

## 1. 사용 원칙

- `UPDATE_TODO.md`를 실행하기 전에 이 색인을 먼저 확인합니다.
- 공식 참고 문서는 기능명, 명령어, 옵션, 보안 권고를 확인하는 근거로 사용합니다.
- 일반 설계 문서는 Agent·Skill의 구조와 운영 절차를 개선하는 참고 자료로 사용합니다.
- 문서 내용과 현재 Kiro CLI 동작이 다르면 현재 실행 환경을 우선 확인하고 차이를 기록합니다.
- 참고 문서를 그대로 Skill에 복사하지 않고, 현재 저장소의 목적과 파일 구조에 맞게 반영합니다.

## 2. 문서 목록

| 분류     | 파일                                                                                                               | 활용 목적                             |
|----------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| 공식     | [`ref_ai_coding_tools_official_notes.md`](32_system-engineering-resources/ref_ai_coding_tools_official_notes.md)   | AI 도구·모델·Kiro 공식 정보 확인      |
| 공식     | [`ref_codex_cli_official_notes.md`](32_system-engineering-resources/ref_codex_cli_official_notes.md)               | Agent CLI 운영·보안·설정 비교         |
| 공식     | [`ref_gitleaks_official_notes.md`](32_system-engineering-resources/ref_gitleaks_official_notes.md)                 | 시크릿 탐지와 Gitleaks 설정 확인      |
| 비교     | [`ref_ai_coding_tools_comparison.md`](32_system-engineering-resources/ref_ai_coding_tools_comparison.md)           | AI 코딩 도구의 기능과 운영 방식 비교  |
| 프로세스 | [`ref_ai_development_request_template.md`](32_system-engineering-resources/ref_ai_development_request_template.md) | Agent 작업 요청과 요구사항 구조화     |
| 설계     | [`ref_ai_markdown_design_patterns.md`](32_system-engineering-resources/ref_ai_markdown_design_patterns.md)         | Agent·Skill Markdown 구조와 로딩 설계 |
| 설계     | [`ref_harness_engineering.md`](32_system-engineering-resources/ref_harness_engineering.md)                         | Agent 실행 루프·검증·저장소 지식 설계 |
| Kiro     | [`ref_kiro_agent_lock.md`](32_system-engineering-resources/ref_kiro_agent_lock.md)                                 | 공유 디렉터리 동시 작업 잠금 설계     |
| Kiro     | [`ref_kiro_cli_command_reference.md`](32_system-engineering-resources/ref_kiro_cli_command_reference.md)           | Kiro CLI 명령어·컨텍스트·Agent 사용법 |
| Kiro     | [`ref_kiro_model_guide.md`](32_system-engineering-resources/ref_kiro_model_guide.md)                               | 모델 선택과 Agent별 모델 운영         |
| Kiro     | [`ref_kiro_setup_guide.md`](32_system-engineering-resources/ref_kiro_setup_guide.md)                               | Kiro 디렉터리·Skill·Agent 설정        |
| 설계     | [`ref_loop_engineering.md`](32_system-engineering-resources/ref_loop_engineering.md)                               | 반복 개선 루프·Skill·Sub-agent 운영   |

## 3. 권장 읽기 순서

1. [`ref_kiro_setup_guide.md`](32_system-engineering-resources/ref_kiro_setup_guide.md) — 현재 Kiro 파일 구조와 Skill 작성 방식 확인.
2. [`ref_kiro_cli_command_reference.md`](32_system-engineering-resources/ref_kiro_cli_command_reference.md) — CLI 명령어와 Agent 운영 방식 확인.
3. [`ref_ai_markdown_design_patterns.md`](32_system-engineering-resources/ref_ai_markdown_design_patterns.md) — Agent·Skill 문서 구조 확인.
4. [`ref_harness_engineering.md`](32_system-engineering-resources/ref_harness_engineering.md) — 검증 루프와 저장소 지식 적용 방식 확인.
5. [`ref_loop_engineering.md`](32_system-engineering-resources/ref_loop_engineering.md) — 반복 업데이트 및 피드백 루프 확인.
6. [`ref_ai_development_request_template.md`](32_system-engineering-resources/ref_ai_development_request_template.md) — TODO 작업 지시 형식 개선.
7. 공식 참고 문서 — 변경할 기능과 보안 관련 사실 재확인.

---

## 통계

![GitHub stars](https://img.shields.io/github/stars/siasia86/system-engineering-resources?style=social)
![GitHub forks](https://img.shields.io/github/forks/siasia86/system-engineering-resources?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/siasia86/system-engineering-resources?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/siasia86/system-engineering-resources)
![License](https://img.shields.io/github/license/siasia86/system-engineering-resources)
![Actions](https://img.shields.io/github/actions/workflow/status/siasia86/system-engineering-resources/update-date.yml)

---

**작성일**: 2026-09-04

**마지막 업데이트**: 2026-09-04

© 2026 siasia86. Licensed under CC BY 4.0.
