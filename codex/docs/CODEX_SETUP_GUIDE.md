# Codex 최초 적용 지침

GPT/Codex용 Agent·Skill·Prompt를 최초 적용할 때 사용하는 adapter입니다. 공통 절차는 [공통 USER TODO](../../agent-workflows/common/USER_TODO.md)를 따릅니다.

공용 체크리스트는 원본으로 유지하고 사용자별 결과·백업·미완료 항목은 별도 작업 기록에 남깁니다. docs/는 runtime 설치 대상이 아닙니다.

현재 전체 배포는 승인 release가 아닙니다. 이 문서는 선택 시험 전 점검 절차이며 적용 승인이 아닙니다. 실제 대상·권한·복구 범위를 별도로 확인하며 gpt/ 원본은 수정하지 않습니다.

## 목차

| 섹션                                                                      |
|---------------------------------------------------------------------------|
| [1. 현재 자산](#1-현재-자산) / [2. 적용 전 조건](#2-적용-전-조건)         |
| [3. Codex 적용](#3-codex-적용) / [4. 검증과 rollback](#4-검증과-rollback) |

---

## 1. 현재 자산

gpt/는 보존 원본이며 codex/는 개발 공간입니다. 현재 후보와 검증 상태는 [Codex README](../README.md), 선택 파일은 [설치 매핑](../PAYLOAD_MAP.md)을 기준으로 확인합니다. 전체 디렉토리를 복사하지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 적용 전 조건

- [ ] Codex client와 version을 확인합니다.
- [ ] 선택한 payload 지침와 선택한 payload skill의 적용 범위를 확인합니다.
- [ ] 프로젝트 로컬 설정과 user-level 설정을 구분합니다.
- [ ] 실제 target 경로는 현재 Codex 공식 문서와 실행 환경으로 확인합니다.
- [ ] Kiro 전용 `$HOME/.kiro`, `skill://`, `/agent swap`, Kiro hook을 사용하지 않습니다.
- [ ] source·staging·runtime target을 고정합니다.
- [ ] 기존 Codex 설정을 백업합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 3. Codex 적용

- [ ] `AGENTS.md`를 프로젝트 instruction으로 먼저 검토합니다.
- [ ] 선택한 payload skill의 Skill 이름·frontmatter·적용 조건을 확인합니다.
- [ ] 선택한 payload agent의 Agent 설정과 권한 범위를 확인합니다.
- [ ] prompt와 Skill이 실제 파일 경로를 참조하는지 확인합니다.
- [ ] Codex client가 지원하는 방식으로 staging에서 target에 적용합니다.
- [ ] 적용 전 dry-run 또는 파일 목록 비교를 실행합니다.
- [ ] 적용 후 대표 작업·검증·rollback을 확인합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 검증과 rollback

- [ ] Markdown·TOML·JSON·script 문법을 검사합니다.
- [ ] `AGENTS.md`에 Kiro 전용 명령이 들어 있지 않은지 확인합니다.
- [ ] Skill이 승인되지 않은 shell·credential·외부 전송을 요구하지 않는지 확인합니다.
- [ ] 적용 version·commit·checksum을 기록합니다.
- [ ] 문제가 있으면 적용 전 Codex 설정 backup으로 복구합니다.

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
