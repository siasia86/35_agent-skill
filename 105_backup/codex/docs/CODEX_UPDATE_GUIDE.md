# Codex 업데이트 지침

GPT/Codex용 Agent·Skill·Prompt 업데이트 adapter입니다. 공통 절차는 [공통 UPDATE TODO](../../agent-workflows/common/UPDATE_TODO.md)를 따릅니다.

공용 체크리스트는 원본으로 유지하고 사용자별 결과·백업·미완료 항목은 별도 작업 기록에 남깁니다. docs/는 runtime 설치 대상이 아닙니다.

현재 전체 배포는 승인 release가 아닙니다. 이 문서는 선택 시험 전 점검 절차이며 적용 승인이 아닙니다. 실제 대상·권한·복구 범위를 별도로 확인하며 gpt/ 원본은 수정하지 않습니다.

## 목차

| 섹션                                                                          |
|-------------------------------------------------------------------------------|
| [1. 변경 범위](#1-변경-범위) / [2. 호환성 검토](#2-호환성-검토)               |
| [3. staging 적용](#3-staging-적용) / [4. 검증과 rollback](#4-검증과-rollback) |

---

## 1. 변경 범위

- [ ] 선택한 payload 지침의 공통 지시와 프로젝트 지시를 구분합니다.
- [ ] 선택한 payload skill의 추가·수정·삭제 Skill을 확인합니다.
- [ ] 선택한 payload agent의 Agent 설정 변경을 확인합니다.
- [ ] 보존 prompt와 다른 도구용 prompt의 경계를 확인합니다.
- [ ] 현재 미추적 작업 파일을 보존하고 변경 owner를 확인합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 호환성 검토

- [ ] 현재 Codex client가 지원하는 Skill·Agent·Prompt 경로를 확인합니다.
- [ ] Kiro 전용 `skill://`, `/agent`, `$HOME/.kiro`, Kiro hook 참조를 제거하거나 분리합니다.
- [ ] shell·filesystem·network 권한이 필요한 Skill을 별도로 표시합니다.
- [ ] 공식 문서와 현재 실행 환경이 다른 부분을 기록합니다.
- [ ] license·source·commit·checksum을 기록합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 3. staging 적용

- [ ] 변경을 특정 commit 또는 release로 고정합니다.
- [ ] staging에서 Markdown·TOML·JSON·script 검사를 실행합니다.
- [ ] 대표 Codex 작업으로 Agent·Skill loading을 확인합니다.
- [ ] 기존 설정을 백업하고 dry-run 또는 파일 목록 비교를 실행합니다.
- [ ] runtime target에 적용한 version과 변경 파일을 기록합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 검증과 rollback

- [ ] secret·private key·개인 경로·세션 데이터 노출을 검사합니다.
- [ ] Skill이 임의 shell·credential·외부 endpoint를 사용하지 않는지 확인합니다.
- [ ] 대표 review·fact-check·testing 작업을 재실행합니다.
- [ ] 실패 시 이전 Codex 설정 backup 또는 release로 복구합니다.
- [ ] 적용 결과와 미해결 호환성 문제를 기록합니다.

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
