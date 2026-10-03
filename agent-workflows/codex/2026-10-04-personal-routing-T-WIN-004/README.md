# T-WIN-004 개인 skill 중복 정리와 조건별 참조

2026-10-04 사용자 요청에 따라 완료된 31의 중앙 문서 구조와 개인 skill을 대조하고, 35 관리 원본을 수정·검증한 뒤 로컬 Codex skill에 반영합니다. 31 변경을 CI/CD로 자동 적용하는 방식은 향후 계획이며 이번 작업에서 자동화를 구성하지 않습니다.

## 1. 범위와 출처

- 정책 대조: 31 `6cd7294c918d9b189421d713ea33da72e0de0942`의 [운영 기준](https://github.com/siasia86/31_governances/blob/6cd7294c918d9b189421d713ea33da72e0de0942/.governance/GOVERNANCE.md), [문서 양식](https://github.com/siasia86/31_governances/tree/6cd7294c918d9b189421d713ea33da72e0de0942/codex/template), [profile](https://github.com/siasia86/31_governances/tree/6cd7294c918d9b189421d713ea33da72e0de0942/codex/profile).
- 구현: [work-rules](../../../codex_windows/skills/work-rules/SKILL.md), [개인 AGENTS](../../../codex_windows/AGENTS.md), 문서 양식·commit 규칙과 그 동봉 사본, 현재 배포 안내.
- 개인 설치: 기존 7개 중 work-rules·git-commit-rule·md-link-check의 전체 폴더와 개인 AGENTS. 나머지 skill·system·plugin·모델·config·인증은 유지합니다.
- 31 자체 기록·대상 repo 문서·기존 업데이트·Linux/Kiro 원문은 수정하지 않습니다. 추가 skill을 설치하거나 repo별 profile을 배포하지 않습니다.

작업 ID는 T-WIN-004이며 담당 파일만 검토·staging합니다. 게시 순서는 35의 yunli → 사용자 검증 → main입니다. 이번에는 main 반영·push를 수행하지 않습니다.

## 2. 중복 제거와 보존 대응

- README·INDEX·PLAN·TODO·TASK·ISSUE·CHANGELOG의 역할표, tasks/outputs/history tree와 상태 처리 절차: 개인 활성 규칙에서 제거하고 실제 대상에 적용된 지침을 연결합니다. 31 양식을 개인 skill 안에 다시 복제하지 않습니다.
- 개인 공통 푸터·배지·날짜·고정 이미지 경로·파일명 규칙: 활성 STYLE과 README 지침에서 제거합니다. 기존 STYLE 원문은 각 폴더 references/originals/STYLE.md에 bytes로 보존합니다.
- 고정 repo/branch 표·일괄 yunli checkout·모든 main push 금지 예시: 활성 commit skill에서 제거합니다. 현재 repo의 게시 규칙을 따르고 기존 원문은 Kiro/Linux 비교 사본에 유지합니다.
- Zircon 문서 정책: 과거 경로·금지 목록을 별도 현행 원본으로 유지하지 않고 해당 repo의 실제 지침을 연결합니다.
- 보고·세미콜론·Luna 역할·기존 승인·변경 보존·검증 판단: 공통 핵심을 유지하며 상세는 조건별 참조로 분리합니다.
- skill 수정 경로: 35_agent-skill 관리 원본 수정·검증 → 로컬 Codex skill 반영을 개인 AGENTS·work-rules·갱신 상세에 명시합니다. 로컬 사용자 차이는 보존·대조 후 원본과 병합합니다.

기존 Windows 상세의 보고·Luna·명명·변경 범위·placeholder·계획·출처·기록·memory 대응은 operating-details, skill 원본·교체는 skill-maintenance, 장시간 실행·Markdown 검사·사후 검증·치환 검증은 validation-and-recovery로 이동했습니다. 실행 환경·삭제/이동·Python config/status·VM은 windows/runtime-and-encoding, SSH·권한·ACL·소유 프로세스는 windows/ssh-and-acl, 작업 잠금·byte lock 예제는 windows/file-lock에 유지했습니다. 기본 적용 범위와 필수 판단은 SKILL 본문에 남겼습니다.

현재 독립적인 동봉 폴더를 유지하기 위해 using-skills·zircon-readme-policy의 work-rules 참조와 필요한 자료도 함께 갱신합니다. 일반 실행에서는 선택한 skill만 읽으며 같은 설치본·동봉본을 중복 로드하지 않습니다.

## 3. 업데이트 폴더

```text
2026-10-04-personal-routing-T-WIN-004/
├── README.md
├── before/inventory.json
├── after/inventory.json
├── preservation-map.json
├── verification.json
└── private/                     Git 제외
    ├── before/                  이전 설치 skill·AGENTS·config 전체
    ├── after/                   적용 후 사본
    ├── source-before/           최초 관리 원본
    ├── source-files/            변경한 기존 배포 파일 원문
    └── 검증 도구·실행 로그·추가 비공개 증거
```

원형 설정·개인 경로·raw는 private 안에서만 보존하고 Git 제외를 실제 검사합니다. 공개 inventory는 환경 별칭·skill 상대 경로·bytes·SHA-256만 포함합니다. [이전 inventory](before/inventory.json), [적용 후 inventory](after/inventory.json), [원문 보존 위치](preservation-map.json), [검증 결과](verification.json)를 연결합니다.

## 4. 검증과 관찰

실제 적용 완료: 기존 개인 skill 7개 중 지정한 3개 전체 폴더와 개인 AGENTS를 갱신했습니다. 설치 파일 91개에서 100개로 변경되었으며 나머지 4개 skill과 config는 동일한 해시로 보존했습니다. work-rules 본문은 4,805자에서 3,506자로 변경되었으며 이는 토큰 수가 아닙니다.

검증: 공식 skill 검사 19개, 원문 해시 대조 368건, 7개 폴더의 단독 helper 사례 35건, 변경 Markdown 72개·링크 242개·헤딩 973개가 통과했습니다. 활성 문서 스타일은 기존 예시 진단 51건이 동일하게 남았고 새 진단은 0건입니다. 최종 판정은 verification.json의 실제 결과를 기준으로 합니다. 시스템 quick_validate, 변경 Markdown 링크·헤딩·표현, Kiro/Linux·도구 원문 해시, 전체 폴더 단독 복사, 동봉 helper 정상·실패 사례, 로컬 설치 해시·기존 사용자 차이·설정 보존을 확인합니다.

Luna는 정형 중복 후보와 중앙 대응 자료를 조회했습니다. main이 정책 적용 범위·중복 제거·수정·최종 검증을 담당했습니다. 독립 agent는 작업 재개·SSH 인코딩 원인 검토·개인 skill 갱신·푸터 없는 README 수정의 4개 읽기 경로를 정적으로 검토했습니다. 일반 재개와 README 소규모 수정에 전체 Workflow/STYLE을 강제하지 않았으며 SSH·교체 상세만 선택했습니다.

system quick_validate의 PyYAML 의존성은 초기 두 Python 환경에 없어 검사가 실행되지 않았습니다. 업데이트 private 안의 격리 경로에 PyYAML 6.0.3을 준비한 뒤 공식 검사기를 실행했습니다. 개인 Python 전역 패키지·system skill 파일은 수정하지 않았습니다.

과거 이관 검증기와 source_manifest는 당시 구조·본문 동등성을 검증하는 역사 자료입니다. 현재 STYLE의 원문 보존 위치 7개는 preservation-map으로 연결하며 과거 manifest를 새 결과로 덮어쓰지 않습니다. 이미 알려진 Markdown parser 경계 문제의 도구 수정은 이번 정책 분리 범위에 포함하지 않습니다.

## 5. 복구와 미실행

복구 전 현재 설치본과 after inventory를 대조하여 이후 사용자 변경을 식별합니다. private/before의 해당 skill 전체와 개인 AGENTS를 선택 복원하거나 현재 변경과 병합합니다. config는 이번에 바꾸지 않았으므로 일괄 덮어쓰지 않습니다. 게시 후 35 구현의 복구는 검토된 revert를 사용하고 원문·다른 작업은 보존합니다.

새 Codex 세션의 암시적 자동 선택·실제 사용자 업무 행동·토큰 절감률은 별도 검증입니다. 정적 읽기 평가·폴더 해시·문법 검사를 그 성공으로 보고하지 않습니다. 31 정책 배포·CI/CD 자동 적용·main 반영·운영 SSH/ACL 변경은 미실행입니다. 사용자 확인과 새 세션 검증은 [Windows TODO](../windows/TODO.md)에 유지합니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
