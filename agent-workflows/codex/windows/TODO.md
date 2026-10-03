# Codex Windows 현재 TODO

작업 기준은 **Linux의 전체 skill·설정 이관 → 검증 → yunli 게시 → 사용자 검증 → main 반영 → 최적화**입니다. 상세 본문은 [이관 기록](../WINDOWS_MIGRATION_2026-10-03.md)에 두고 이 문서는 상태와 후속을 연결합니다.

## 1. 전체 이관과 검증

- [x] Linux19개 이름·역할·182파일·54개 동봉 역할 대응.
- [x] 19개 Windows 활성 SKILL 전체본과 필요한 도구/자료 작성.
- [x] 공통 AGENTS·저장소 config2개 출처 보존과 Windows 예시 작성.
- [x] 원본 bytes·필수 참조·단독 폴더 실행·메타데이터·네이티브 실패/경쟁 검사.
- [x] Windows 제약·미제공 설정·미실행 범위·복구 기준 기록.

검토 가능한 전체 이관본을 yunli에 일반 commit·push하는 순서를 적용합니다. 실제 게시 SHA·remote 일치는 Git refs와 이번 작업 보고에서 확인하며 문서가 설치 완료를 의미하지 않습니다.

## 2. 사용자 검증과 실제 환경

- [ ] 사용자가 yunli의 19개와 설정 대응·대표 작업 결과를 검증.
- [ ] work-rules 외 추가 개인 skill·config 적용이 요청되면 기존 동명 사본을 비교·병합.
- [ ] 실제 Codex 새 세션의 발견·자동 선택·설정 로드 확인.
- [ ] 필요한 symlink·ACL/ADS/owner·SMB·WSL 등 추가 환경 검증.
- [ ] 다른 Linux home/원격의 실제 설정이 있으면 비공개 자료로 추가 대조.

## 3. main과 최적화

- [ ] 사용자 검증 완료 후 검증한 결과를 main에 반영·일반 push.
- [ ] 전체 이관 이후 사용 사례를 바탕으로 Windows 최적화 범위를 결정.

이번 이관에서 생략·축약·통합하지 않습니다. main·추가 홈 설치·운영 적용·release의 미실행을 문서 검사 성공으로 완료 처리하지 않습니다. work-rules와 개인 공통 요약의 지정 적용·검증 이력은 [공식 skill 재검토](SYSTEM_SKILL_REVIEW_2026-10-03.md#6-적용검증복구)에서 확인합니다.

## 4. 복사용 구성과 개선 검토

- [x] PLAN·TODO·ISSUE·REVIEW·개발 verification을 복사 영역 밖으로 이동.
- [x] 사용 안내·활성 Windows 본문의 이번 35 이관 관리 문구 정리.
- [x] [ISSUE W01](ISSUE.md#4-복사용-영역과-개발-기록-혼입-w01)과 루트 README·AGENTS에 원인·배치 규칙·재발 방지 기록.
- [x] 원문·19개 skill·동봉 자료 보존과 독립 복사·이동한 CLI 경로 검증.
- [x] [개선 검토](IMPROVEMENT_REVIEW_2026-10-03.md)의 W02–W10을 지정 범위에서 수정·새 회귀 확인.
- [x] work-rules·personal AGENTS에 시작/완료 보고·경로·가시성·성과/제약·채팅 `;` 구분 규칙 반영.

기존 보고 지침·helper 보완의 당시 검증은 [보고 지침과 helper 보완](REPORTING_REMEDIATION_2026-10-03.md), 공식 source 기준의 후속 보완·지정 개인 적용 이력은 [공식 skill 재검토](SYSTEM_SKILL_REVIEW_2026-10-03.md)를 따릅니다. 중앙 31의 35 정책은 구현 기준이며 문서 조회만으로 실제 홈 설치·자동 적용을 의미하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
