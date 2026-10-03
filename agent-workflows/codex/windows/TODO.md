# Codex Windows 현재 TODO

작업 기준은 **Linux의 전체 skill·설정 이관 → 검증 → yunli 게시 → 사용자 검증 → main 반영 → 최적화**입니다. 상세 본문은 [이관 기록](../WINDOWS_MIGRATION_2026-10-03.md)에 두고 이 문서는 상태와 후속을 연결합니다. 완료 항목은 [완료 이력](../../history/2026-10-03/T-WIN-002-distribution-root.md#5-기존-완료-항목의-보존)에 보존하며 아래에는 미완료 행동만 유지합니다.

## 1. 사용자 검증과 실제 환경

- [ ] 사용자가 yunli의 19개와 설정 대응·대표 작업 결과를 검증.
- [ ] T-WIN-002 배포 원본 배치 교정을 사용자 확인 후 main에 반영 — [완료 구현·검증 이력](../../history/2026-10-03/T-WIN-002-distribution-root.md).
- [ ] work-rules 외 추가 개인 skill·config 적용이 요청되면 기존 동명 사본을 비교·병합.
- [ ] 실제 Codex 새 세션의 발견·자동 선택·설정 로드 확인.
- [ ] 필요한 symlink·ACL/ADS/owner·SMB·WSL 등 추가 환경 검증.
- [ ] 다른 Linux home/원격의 실제 설정이 있으면 비공개 자료로 추가 대조.

## 2. main과 최적화

- [ ] 사용자 검증 완료 후 검증한 결과를 main에 반영·일반 push.
- [ ] 전체 이관 이후 사용 사례를 바탕으로 Windows 최적화 범위를 결정.

이번 이관에서 생략·축약·통합하지 않습니다. main·추가 홈 설치·운영 적용·release의 미실행을 문서 검사 성공으로 완료 처리하지 않습니다. work-rules와 개인 공통 요약의 지정 적용·검증 이력은 [공식 skill 재검토](SYSTEM_SKILL_REVIEW_2026-10-03.md#6-적용검증복구)에서 확인합니다.


---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
