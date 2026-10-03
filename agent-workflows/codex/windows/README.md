# Windows 개발 작업 기록

`codex_windows/`는 Windows 개인 Codex용 루트 AGENTS·skill·필수 자료·설정 예시·사용 안내의 배포 원본입니다. 이 디렉터리는 35 저장소의 Windows 개발 계획·검토·검증용이며 설치 또는 사용 의존성이 아닙니다.

## 1. 작업 문서

- [PLAN](PLAN.md): 이관과 후속 작업 순서.
- [기존 자료 이관·스킬 수정 workflow](records/2026-10-04-record-relocation-SMA-20261004-01/README.md): PCS·PCR의 현재 위치·과거 기록 구분·검증·복구.
- [T-WIN-002 배포 원본 배치 교정](../../history/2026-10-03/T-WIN-002-distribution-root.md): 루트 공통 지침·관리 역할·현재 검사와 미실행.
- [공식 skill 재검토와 개인 적용](SYSTEM_SKILL_REVIEW_2026-10-03.md): 전체 공개 source 조사·INDEX/TODO/산출물 예외·현재 검증·설치 범위.
- [AI 작업 INDEX](../../INDEX.md): 주요 구조와 작업별 기준 문서 연결.
- [TODO](TODO.md): 완료·미실행·사용자 검증 상태.
- [ISSUE](ISSUE.md): 호환 교정과 환경 제약.
- [보고 지침과 helper 보완](REPORTING_REMEDIATION_2026-10-03.md): 현재 공통 보고 규칙·W02–W10 수정·새 검증과 미실행.
- [개선 검토](IMPROVEMENT_REVIEW_2026-10-03.md): 구성 정리와 보완 전 재현 근거.
- [이관 REVIEW](REVIEW.md): `773a150` 이관 당시 검사와 한계.
- [개발 검증 도구](verification/README.md): 현재 실행 경로와 과거 결과의 구분.
- [이관 기록](../WINDOWS_MIGRATION_2026-10-03.md): 전체 출처·보존·검증·복구 기준.
- [복사용 Windows 구성](../../../codex_windows/README.md): 실제 사용할 폴더.

## 2. 관리 원칙

검증한 변경을 yunli에 일반 commit·push하고 사용자 검증을 기다립니다. 사용자 검증 완료 후에만 검증 결과를 main에 반영·push합니다. 실제 개인 홈 설치·설정 병합·발견·운영 적용은 별도 요청·검증 범위입니다.

이관 당시 결과 JSON·입력 해시는 당시 경로와 bytes를 보존합니다. 관리 문서 이동으로 이전 검사를 새 결과로 바꾸지 않습니다. 후속 검사·개선 사항은 별도 기록에서 관리합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
