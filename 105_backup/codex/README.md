# 폐기한 Codex 개발본의 이력 보존

2026-10-01 사용자가 기존 `codex/`를 `105_backup/codex/`로 이동했습니다. 이 디렉토리는 이전 개발·설치·검증 기록을 보존하는 자료입니다. 현재 개인 스킬의 설치 원본이나 실행 지침으로 사용하지 않습니다.

## 1. 보존한 자료

- [REVIEW.md](REVIEW.md): 개인 스킬 복제 의도 적합성과 16개 후보의 Kiro 원문 diff 리뷰. 이동 시 본문을 변경하지 않았습니다.
- [이동 전 Codex README](README.before-1.0.0.md): 이전 개발본 상태와 설치 경계.
- [이동 전 루트 README](REPOSITORY_README.before-1.0.0.md): 이전 payload·catalog·setup·중앙 연동 안내.
- [CHANGELOG](CHANGELOG.md), [TODO](TODO.md), [PLAN](PLAN.md), [검증 기록](CODEX_GOVERNANCE_VERIFICATION.md): 과거 완료·미검증·게시 이력.
- `payload/`, `archive/`, `prompts/`, `policies/`, `markdown/`, `templates/`, `scripts/`, `tests/`: 당시 구현과 참조 자료. 스킬 16개·agent 10개 등의 수치는 당시 범위입니다.

이동 직후 기존 추적 파일 131개가 Git 기준 `4227f1d`의 원문과 동일한 bytes임을 확인했습니다. 이 README는 보존 안내로 변경했고 이전 본문은 별도 보존했습니다. 그 밖의 기존 개발 파일·manifest·catalog·과거 해시는 유지합니다. 과거 문서 안의 경로는 당시 `codex/` 위치를 기준으로 읽습니다.

## 2. 현재 작업의 위치

[저장소 README](../../README.md)와 [TODO2](../../TODO2.md)가 새 개인 스킬 구성과 내용 보존 기준을 안내합니다. 이번 저장소 버전은 **1.0.0**입니다. 과거 파일에 기록된 버전·출처·검증 상태를 1.0.0 결과로 바꾸지 않습니다.

[이전 개인 적용 관찰](../../agent-workflows/codex/README.md)은 별도로 보존합니다. 이 보존본을 이동했다고 실제 개인 홈의 설치 파일이 변경된 것은 아닙니다.

## 3. 사용 제한

이 디렉토리의 과거 설치 명령·승인 예외·권한 예시·AGENTS·TODO를 현행 실행 지시로 사용하지 않습니다. 원문 비교나 역사 조사에 필요한 파일만 읽습니다. 복구가 필요하면 게시된 변경의 검토된 revert를 사용하고 사용자 변경을 보존합니다.

---

**작성일**: 2026-10-01

**마지막 업데이트**: 2026-10-01

© 2026 siasia86. Licensed under CC BY 4.0.
