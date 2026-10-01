# Codex 개인 스킬 후속 확인

## 1. 실제 사용자 환경

- [ ] 사용자가 고른 스킬을 기존 개인 편집과 비교·백업한 뒤 실제 홈에 복사하고 새 Codex 세션에서 발견·명시 호출·자동 선택을 확인합니다. 이번 작업은 저장소 작성과 격리 복사 검증입니다.
- [ ] 실제 Windows에서 폴더 복사·Python 3.11 실행·PowerShell·Git worktree·잠금 파일을 확인합니다. Linux 결과로 Windows 동작을 완료 처리하지 않습니다.
- [ ] Terraform·Ansible·AWS·Docker·서비스 복구는 승인된 실제 환경에서 검증합니다. 계획/리뷰의 Luna 사례 결과와 운영 결과를 구분합니다.

## 2. 원문 도구와 잠금

- [ ] security-tools의 원래 마스킹/scanner/config가 필요하면 사용자 제공 원본·map fixture·정규식 명세를 확인하고 동일 인터페이스와 복원 호환성을 검사합니다. 현재 스킬의 설계·수동 점검과 기존 실행 도구의 배포를 구분합니다.
- [ ] 잠금은 참여 agent가 같은 프로토콜을 지킬 때 사용합니다. helper가 종료되기 전에 죽으면 `.kiro-lock.guard`가 남을 수 있습니다. 소유·실제 프로세스·사용자 승인 확인 후 복구하고 시간 경과만으로 삭제하지 않습니다.
- [ ] 잠금 API를 따르지 않는 외부 writer·네트워크 파일시스템·Windows 파일 잠금의 보장은 별도 확인합니다. 현재 helper의 gate·O_EXCL 검증을 임의 writer 전체의 격리 보장으로 확대하지 않습니다.

## 3. 별도 사용자 검토

- [ ] Kiro prompt 16개의 별도 Codex 스킬 추가 필요성을 사용자 작업 예시로 검토합니다. 현재 19개 스킬에서 필수 호출하는 prompt는 없으며 prompt 원문은 kiro에 유지합니다.
- [ ] 폐기본에만 있던 ansible-review·fact-check·markdown-review·git-release·security-audit의 추가 필요성을 별도로 검토합니다. 자동 추가·삭제하지 않습니다.
- [ ] 내용 축약·스킬 통합·중복 제거·본문 분할은 사용자가 별도로 선택한 후속 작업에서 검토합니다. 이번 모음은 원문 분량을 유지합니다.

현재 완료 상태와 실제 근거는 [VERIFICATION](VERIFICATION.md), 원문 대응과 변경 이유는 [MIGRATION](MIGRATION.md)에 기록합니다.

---

**작성일**: 2026-10-01

**마지막 업데이트**: 2026-10-01

© 2026 siasia86. Licensed under CC BY 4.0.
