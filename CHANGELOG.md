# Changelog

`35_agent-skill`의 주요 변경 사항을 기록합니다.

## [Unreleased]

### 읽기 중심 위임 정책 후속 예약과 게시 — 2026-09-22

- 사용자 요청으로 TODO에 단일 작성자·읽기 중심 조사·리뷰·테스트 분석, 기본 2개·최대 3개 위임, worktree별 독립 구현과 최종 통합 기준을 예약했습니다. 기존 구현 위임 정책과의 정합화 및 영향 범위 재검증을 포함합니다.
- 순서는 7번 개발 검증 완료 → 8번 pilot → 위임 정책 정비·재검증 → 9번 release입니다. 이번 게시에서 공통 지침·agent 권한·개인 runtime은 변경하지 않습니다.
- 후속 사용자 요청으로 현재까지의 개발 변경과 TODO를 검증 후 기존 yunli에 commit·push합니다. 원격 결과는 해당 commit으로 확인하며 release·운영 적용·OS 권한 변경은 제외합니다.

### 작업 6 자산 이식과 5~7 연계 — 2026-09-22

- 보존 gpt·kiro·codex 원본 영역은 유지하고 payload를 지침 1개·skill 25개·agent 10개로 확장했습니다. work-rules 동반 참조 1개를 포함해 선택 ID 36개·파일 37개입니다. 개발 후보이며 실제 runtime에 설치하지 않았습니다.
- catalog 0.2-draft에 참조 파일의 source·relative target·SHA-256을 명시하고 30 planner·격리 패키지와 연결했습니다. 개인용·프로젝트용 모두 37개 파일 staging·설치·재적용 무변경을 확인했습니다.
- skill-creator 기준으로 범위·의존성을 정리했으며 개인 규칙을 일반론으로 축약한 초기 후보를 보완했습니다. 독립 검토에 따라 테스트 작성 승인, branch 확인, Python 멱등성, Ansible 상세 검사, masking·restore 불변식, container 검증, 문서 고유 검사와 optional 관계를 복원했습니다.
- 원본 62개 해시는 BASELINE_MANIFEST와 일치합니다. skill 25개 frontmatter와 agent 10개 TOML을 정적 검사했으며 실제 discovery·agent invocation·sandbox·자동 hook 동작을 대신하지 않습니다. Kiro 자동 hook 동등 동작은 명시적으로 보류했습니다.
- 이번 요청의 5~7번 개발·검증 범위이며 8번 실제 환경 pilot과 9번 release·운영 배포는 PLAN으로 남깁니다. Sol 독립 재검토와 합성 요청 3개를 통과했습니다. 30 전체 단위 시험 89개, 최종 catalog 개인·프로젝트 37개 파일 및 31 v2 profile 5개 파일의 격리 연동·재적용 검사를 통과했습니다. 게시 범위는 위 후속 요청 기록을 따릅니다.

### Governance 경로와 과거 기록 구분 — 2026-09-22

- TODO의 현재 manifest 안내를 31 최상위 profiles 경로와 개발 v2 소유권 계약에 맞췄습니다. Batch 4는 과거 검증 기록임을 명시하고 원본 명령·출처는 보존했습니다.
- 사용자 승인한 남은 9개 작업 중 1~4번 연계 정리 범위이며 gpt·kiro 원본과 배포 payload는 수정하지 않습니다. 원본 작업본의 Git 권한은 변경하지 않고 별도 clone에서 검증·게시합니다.

### 삭제 참조·사용자 지침 진입점 정리 — 2026-09-22

- 사용자가 삭제한 Kiro 미리보기 스크립트의 현재 사용 안내와 깨진 링크를 정리하고 ISSUE-1을 현재 작업본 기준 해결로 기록했습니다. 기존 Git 이력은 보존합니다.
- Codex ISSUE-006에 이동된 문서 경로와 현재 계정에서 읽기 가능한 사실을 추가하고 과거 실패·미검증 범위를 구분했습니다.
- Kiro·Claude 하위 README는 OS 쓰기 제한으로 agent가 갱신하지 못했으나 사용자가 지침 링크 4개를 직접 추가했습니다. 검사 후 ISSUE-2를 해결로 기록했으며 소유권·ACL은 유지했습니다.
- 승인 사유는 삭제된 Kiro 스크립트 참조 정리 및 사용자 지침 진입점·이슈 현황 정합성 보완입니다. 후속 사용자 요청으로 관련 문서와 사용자 삭제 변경의 commit·push를 포함합니다. 이번 작업 종료 시 예외는 만료되며 runtime 변경·다른 저장소 직접 수정으로 확대하지 않습니다.

### README 정합성 정비 — 2026-09-22

- 추가 요청에 따라 ISSUE를 정리해 정적 관찰·영향·임시 조치·해결 조건을 기록했습니다. README에서 해결한 설명 문제와 실행 코드·권한·전환 계약의 미해결 문제를 구분했습니다.

- 세 저장소의 역할·연결 흐름을 같은 책임 기준으로 정리하고 현재 구현과 목표 구조·미완료를 구분했습니다.
- 보존 원본·개발 후보·선택 payload·사용자 지침의 경계와 30·31 연결을 명시하고 기존 도구별 지침 링크를 유지했습니다. 검사 범위와 작업 예외·승인 조건을 정리했습니다.
- 사용자 승인 사유: 세 저장소 README의 역할·운영정책·구현 상태 정합성 정비. 이번 요청에 한해 root 작업본의 README·CHANGELOG 및 추가 요청한 ISSUE 수정·검증·commit·push를 허용하며 30·31은 기존 설계 브랜치, 35는 yunli에 게시합니다. 작업 종료·중단 시 예외는 만료됩니다.
- 실행 코드·기존 정책 원본·manifest·운영 환경은 변경하지 않습니다. 보호 브랜치 직접 push·release 승인·권한 확대는 제외하며 게시 후 복구는 검토된 revert로 수행합니다.
- 검증: ISSUE를 포함한 세 저장소의 변경 문서 9개 style·heading·로컬 link 검사, diff 공백 검사, 31 draft manifest 45개 항목·manifest checksum, profile과 자산 5개의 읽기 전용 계획 연동을 확인했습니다. 전체 unit test·Ansible 실행·운영 설치·원격 CI는 이번 문서 작업에서 재검증하지 않았습니다.

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
