# T-WIN-002 Windows 배포 원본 배치 교정

## 1. 대상과 완료 기준

입력은 35의 yunli a6e3584입니다. 사용자 요청에 따라 35부터 Windows 배포 원본과 개발·검토·적용 기록의 역할을 적용합니다. 공통 지침은 배포 루트 한 곳에 두고 현재 안내·단독 복사·기존 이력의 연결을 확인하며 원문·19개 skill·개인 홈을 보존합니다.

## 2. 변경과 역할

| 위치                     | 이번 변경·기준                                                                 |
|--------------------------|--------------------------------------------------------------------------------|
| codex_windows/AGENTS.md  | 이전 personal/AGENTS.md의 지시사항을 보존해 이동; 제목·소개·업데이트 날짜 정리 |
| codex_windows/personal/  | 설정 예시·비교 원문·개인 홈 적용 안내; AGENTS 본문 중복 없음                   |
| codex_windows/skills/    | 기존 19개 전체 폴더·원문·helper·참조 유지                                      |
| agent-workflows/         | 35 자체 원본 개발·검토·적용·완료 기록; 다른 repo의 상태·결과는 해당 repo 소유  |
| agent-workflows/history/ | 새 완료 기록 보관; 기존 이력·JSON·해시는 원위치에서 연결                       |

35 루트 AGENTS는 저장소 유지보수 지침이고 codex_windows/AGENTS는 복사·병합할 개인 공통 지침입니다. 배포 원본 배치와 사용자 home의 실제 로딩·설치는 구분합니다. 기존 개인 AGENTS·config·skill을 이번 배치 변경으로 일괄 교체하지 않습니다.

## 3. 검증과 한계

<!-- VALIDATION-BEGIN -->
| 항목                         | 실행 결과                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------|
| Markdown 형식·헤딩·로컬 링크 | 17개 문서, 150개 헤딩·256개 파일 링크에서 오류 0건                                        |
| 파일 간 heading fragment     | 39개 target anchor 존재 확인                                                              |
| Windows 배포 전체 단독 복사  | 301개 파일이 원본과 동일; 주요 안내 4개 문서의 로컬 링크 31개가 복사 영역 안에서 연결됨   |
| 배포 영역의 개발 기록        | PLAN·TODO·ISSUE·REVIEW·DELEGATION·INTERVIEW·CHANGELOG 이름의 파일 0개                     |
| 지침·skill 보존              | 이전 공통 지시 본문 유지; 19개 skill의 294개 payload 파일 해시 동일                       |
| 이력·보호 범위               | 기존 JSON·CSV 15개와 보호 대상 442개 파일 동일; 허용한 변경 외 baseline 보존              |
| 개인 사용 환경               | 실제 홈의 AGENTS·config·개인 skill·system 파일 90개 변경 없음                             |
| 비밀·diff 검사               | Gitleaks 8.30.1의 저장소 directory 검사 발견 0건; Git diff 공백 검사 오류 0건             |
| 독립 검토                    | 배포·관리 역할과 링크 검토에서 차단 문제 없음; Windows 업데이트 안내 보완                 |
| 미실행                       | 추가 개인 홈 적용·전체 helper 재실행·새 세션 자동 선택/설정 로딩·운영 환경 검증·main 반영 |
<!-- VALIDATION-END -->

Luna는 현재 링크·경로를 수집하고 총괄 AI가 역사적 경로와 활성 연결을 구분해 수정·검증합니다. 이전 설치·536개 공식 source 조사는 [앞선 검토](../../codex/windows/SYSTEM_SKILL_REVIEW_2026-10-03.md)의 당시 범위로 보존하며 이번 결과로 다시 집계하지 않습니다.

## 4. 평가와 재개·복구

잘된 점은 공통 지침의 작성 원본과 배포 파일 위치가 일치하고 사용 구성·35 유지보수 기록·다른 repo의 작업 기록이 구분되는 것입니다. 비용은 파일 이동 때 README·tree·과거 문서의 활성 링크를 함께 갱신해야 하는 점이며 당시 원시 경로·검사 JSON을 현재 배치로 덮어쓰지 않아야 합니다.

남은 사용자 확인·main 반영 상태는 [Windows TODO](../../codex/windows/TODO.md) 한 곳에서 관리합니다. 완료 구현·검증 상세를 TODO에 다시 운영하지 않습니다. 새 작업에서 공통 지침을 편집할 때는 [배포 AGENTS](../../../codex_windows/AGENTS.md), 적용 방법은 [배포 README](../../../codex_windows/README.md), 재발 방지는 [W11](../../codex/windows/ISSUE.md#6-배포-원본의-공통-지침-배치-w11)에서 확인합니다.

게시 대상은 yunli이며 원격 일치는 실제 Git refs로 확인합니다. 사용자 확인 이후 main 반영 순서를 유지합니다. 미게시 복구는 이번 이동·소개·링크 변경만 이전 입력과 대조해 되돌리고 사용자 편집을 보존합니다. 게시 후에는 검토한 revert를 사용합니다.

## 5. 기존 완료 항목의 보존

Windows TODO에 있던 완료 목록을 이곳으로 옮겼습니다. 아래는 당시 완료 표시와 설명을 보존한 기록이며, 현재 남은 행동은 Windows TODO 한 곳에서 관리합니다.

### 5.1. 전체 이관과 검증

- [x] Linux19개 이름·역할·182파일·54개 동봉 역할 대응.
- [x] 19개 Windows 활성 SKILL 전체본과 필요한 도구/자료 작성.
- [x] 공통 AGENTS·저장소 config2개 출처 보존과 Windows 예시 작성.
- [x] 원본 bytes·필수 참조·단독 폴더 실행·메타데이터·네이티브 실패/경쟁 검사.
- [x] Windows 제약·미제공 설정·미실행 범위·복구 기준 기록.

검토 가능한 전체 이관본을 yunli에 일반 commit·push하는 순서를 적용합니다. 실제 게시 SHA·remote 일치는 Git refs와 이번 작업 보고에서 확인하며 문서가 설치 완료를 의미하지 않습니다.

### 5.2. 복사용 구성과 개선 검토

- [x] PLAN·TODO·ISSUE·REVIEW·개발 verification을 복사 영역 밖으로 이동.
- [x] 사용 안내·활성 Windows 본문의 이번 35 이관 관리 문구 정리.
- [x] [ISSUE W01](../../codex/windows/ISSUE.md#4-복사용-영역과-개발-기록-혼입-w01)과 루트 README·AGENTS에 원인·배치 규칙·재발 방지 기록.
- [x] 원문·19개 skill·동봉 자료 보존과 독립 복사·이동한 CLI 경로 검증.
- [x] [개선 검토](../../codex/windows/IMPROVEMENT_REVIEW_2026-10-03.md)의 W02–W10을 지정 범위에서 수정·새 회귀 확인.
- [x] work-rules·개인 공통 AGENTS에 시작/완료 보고·경로·가시성·성과/제약·채팅 `;` 구분 규칙 반영.

기존 보고 지침·helper 보완의 당시 검증은 [보고 지침과 helper 보완](../../codex/windows/REPORTING_REMEDIATION_2026-10-03.md), 공식 source 기준의 후속 보완·지정 개인 적용 이력은 [공식 skill 재검토](../../codex/windows/SYSTEM_SKILL_REVIEW_2026-10-03.md)를 따릅니다. 중앙 31의 35 정책은 구현 기준이며 문서 조회만으로 실제 홈 설치·자동 적용을 의미하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
