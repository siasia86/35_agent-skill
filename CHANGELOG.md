# Changelog

`35_agent-skill`의 주요 변경 사항을 기록합니다.

## [Unreleased]

### 사용자 지침 구조 정비 — 2026-09-22

- 도구별 USER_TODO·UPDATE_TODO 6개를 kiro/docs·codex/docs·claude/docs의 도구명_SETUP_GUIDE·도구명_UPDATE_GUIDE로 이동·정리했습니다.
- 공통 체크리스트와 SE 시험 기록은 agent-workflows에 유지하고 루트 README의 중복 Kiro 절차·이전 경로를 새 지침 링크로 대체했습니다.
- 공용 지침과 개인 실행 기록, 최초 적용과 선택 유지보수를 구분했습니다. 누락 참조·저작권 고지 자동 삭제와 전체 runtime 복사 안내를 제거했습니다.
- Codex 개발 후보·Claude 예약 상태를 유지하고 docs의 runtime 복사 제외 및 기존 Kiro 미리보기 출력의 chown 주의점을 명시했습니다.
- 사용자 승인 사유는 도구별 사용자 지침 구조 정비이며 이번 문서 변경·검증·commit·push 완료 시 직접 수정 예외가 종료됩니다. 운영 적용·agent·skill·설치 script 변경은 제외합니다.
- 변경 문서 12개의 스타일·헤딩·로컬 링크 검사와 diff 공백 검사를 통과했습니다. 설치·runtime 동작 시험은 수행하지 않았습니다. Kiro·Claude 하위 README는 파일 권한 제한으로 보존하고 루트 README와 공통 인덱스에서 새 지침을 연결했습니다.

### Governance design checkpoint — 2026-09-22

- gpt 원본 62개를 보존한 codex 개발본과 최초 출처·해시 기록을 작성했습니다.
- 최소 SE 공통 지침·저장소 지침을 마련하고 개인 지침 설치·CLI 로딩·합성 명령 결과를 확인했습니다. 설치 지침의 행동 수용·사용자 체감은 미완료로 구분했습니다.
- skill 25개·agent 10개의 정적 검토 후 fact-check·markdown-review와 reviewer·docs_reviewer를 별도 payload로 준비했습니다. 검토 시 자동 수정·Python 캐시 부작용 등 관찰된 문제를 보완하고 시험했습니다.
- 자산 5개의 목록·해시·설치 매핑, 비민감 로딩 판정과 Batch 2·4 검증 기록을 추가했습니다. 31 profile·30 읽기 전용 planner와 연동했으며 운영 실행기로 간주하지 않습니다.
- TODO에 중앙 설정 소유권, 설치·검증·활성화 분리, 개발·테스트 전체 권한 계획과 운영 실행 제한을 반영했습니다. 직접 명령 예외·운영 기록 위치는 미결정입니다.
- 이번 구조 설계 통합·기록·push에 한한 직접 수정 예외와, 이후 타당한 이유 없는 제한 해제는 수행하지 않는 지침을 추가했습니다.
- 30·31 기준 작업본에 계정 clone의 변경 부분을 통합하고 기존 sync 포함 테스트 40개, 31 draft 검사 45개 항목, 자산 5개 계획 연동을 확인했습니다. 30·31 설계 브랜치와 35 yunli에 게시하는 범위이며 보호 브랜치 통합·원격 CI·운영 적용은 별도입니다.
- 미완료: 나머지 자산 이식, 안전 실행 계약·Ansible 연결, 실제 신규 개인 설치·운영 활성화·복구·토큰 비교. 개발 후보를 승인 release로 표시하지 않습니다.

### Added

- 32 `system-engineering-resources/00_governance/02_kiro/`에서 Kiro 공개 mirror(49개 파일) 이관.
- 32 `00_governance/03_claude/README.md`의 Claude 예약 영역 이관.
- 저장소 루트 `README.md` 추가.
- `agent-workflows/` 아래 공통·Kiro·GPT/Codex·Claude용 `USER_TODO.md`와 `UPDATE_TODO.md` 추가.

### Changed

- `~/.kiro/02_home-sjyun-kiro.sh`의 동기화 target을 32 `00_governance/02_kiro/`에서 이 저장소 `kiro/`로 전환.
- 기존 root Kiro TODO를 `agent-workflows/kiro/`로 이동하고 도구별 workflow 인덱스를 추가.

---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
