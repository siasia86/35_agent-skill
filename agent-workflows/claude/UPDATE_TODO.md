# Claude UPDATE TODO

Claude용 Agent·Skill·Prompt 업데이트 adapter입니다. 공통 절차는 [공통 UPDATE TODO](../common/UPDATE_TODO.md)를 따릅니다.

## 목차

| 섹션                                                                  |
|-----------------------------------------------------------------------|
| [1. 활성화 전 확인](#1-활성화-전-확인) / [2. 변경 검토](#2-변경-검토) |
| [3. release 준비](#3-release-준비) / [4. rollback](#4-rollback)       |

---

## 1. 활성화 전 확인

현재 `claude/`는 예약 영역이므로 실제 runtime 업데이트를 수행하지 않습니다.

- [ ] Claude source·runtime target을 확정합니다.
- [ ] 공개 allowlist·제외 범위·license를 확인합니다.
- [ ] 공식 문서와 현재 client의 Skill·Agent·Prompt 동작을 대조합니다.
- [ ] 동기화 script·manifest·검증 명령을 준비합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 2. 변경 검토

- [ ] 변경 파일·source commit·release version을 기록합니다.
- [ ] Kiro·GPT/Codex 전용 경로와 명령이 섞이지 않았는지 확인합니다.
- [ ] 개인 경로·credential·session data·외부 endpoint를 검토합니다.
- [ ] 권한 범위와 rollback 방법을 문서화합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 3. release 준비

활성화 조건을 충족한 뒤에만 수행합니다.

- [ ] staging release를 생성합니다.
- [ ] manifest·checksum·license를 검증합니다.
- [ ] Markdown·설정·script 검사를 실행합니다.
- [ ] dry-run과 runtime backup을 준비합니다.
- [ ] 대표 Claude 작업으로 loading·권한·결과를 확인합니다.
- [ ] 승인 후에만 runtime target 적용을 진행합니다.

[⬆ 목차로 돌아가기](#목차)

---

## 4. rollback

검증 실패·권한 오류·예상하지 못한 외부 통신·source 불일치가 발생하면 적용을 중단하고 이전 runtime backup 또는 release로 복구합니다.

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-21

© 2026 siasia86. Licensed under CC BY 4.0.
