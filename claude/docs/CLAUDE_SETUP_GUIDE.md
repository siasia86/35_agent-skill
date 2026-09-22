# Claude 최초 적용 지침

Claude용 Agent·Skill·Prompt 최초 적용 adapter입니다. 공통 절차는 [공통 USER TODO](../../agent-workflows/common/USER_TODO.md)를 따릅니다.

공용 체크리스트는 원본으로 유지하고 사용자별 결과·백업·미완료 항목은 별도 작업 기록에 남깁니다. docs/는 runtime 설치 대상이 아닙니다.

## 목차

| 섹션                                                                          |
|-------------------------------------------------------------------------------|
| [1. 현재 상태](#1-현재-상태) / [2. 활성화 조건](#2-활성화-조건)               |
| [3. 적용 전 검증](#3-적용-전-검증) / [4. 중단과 rollback](#4-중단과-rollback) |

---

## 1. 현재 상태

현재 `claude/`는 예약 영역입니다. 실제 Claude payload·manifest·sync script·runtime target은 확정되지 않았습니다.

따라서 현재 단계에서는 Claude 파일을 사용자의 home directory에 복사하거나 자동 적용하지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 활성화 조건

- [ ] Claude source repository와 원본 경로를 확정합니다.
- [ ] 공개 allowlist와 제외 범위를 확정합니다.
- [ ] Skill·Agent·Prompt의 runtime target을 공식 문서로 확인합니다.
- [ ] 동기화 방식과 dry-run 명령을 작성합니다.
- [ ] owner·license·version·rollback 절차를 확정합니다.
- [ ] 검증 명령과 evidence 보존 방식을 정의합니다.
- [ ] 31 governance와 repository 운영 정책을 확인합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 3. 적용 전 검증

활성화 조건이 완료되기 전에는 다음 작업만 수행합니다.

- [ ] source 파일 목록과 license를 읽습니다.
- [ ] credential·private key·session data를 제외합니다.
- [ ] manifest 초안을 review합니다.
- [ ] 실제 적용하지 않는 dry-run 또는 static 검사를 준비합니다.
- [ ] Kiro·GPT/Codex 전용 명령을 Claude workflow에 복사하지 않습니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. 중단과 rollback

source·target·allowlist가 확정되지 않았거나 검증 명령이 없으면 적용하지 않습니다. 활성화 후에는 이전 release와 runtime backup으로 rollback할 수 있어야 합니다.

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
