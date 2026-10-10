# Windows native skill 정리 기록

작업 ID는 `T-WIN-004`이며 관리 원본은 [codex_windows](../../../codex_windows/README.md)입니다. 사용자가 승인한 순서는 원형 보존 → Windows 본문·도구 정리 → 검사 → 현재 설치된 관리 skill 반영 → 지정 Git 통합 담당의 `main` 일반 게시입니다. 이 기록은 갱신 근거이며 활성 작업 상태는 기존 [Windows TODO](../windows/TODO.md)를 따릅니다.

## 1. 변경 범위

- 현재 배포본은 [current_inventory.json](../windows/verification/current_inventory.json)에 선언한 native 21개입니다. `bash-script-template`을 보존 후 제외하고 `using-skills`의 Bash 연결과 도구를 제거했습니다.
- 나머지 skill의 공통 기능을 Windows 본문·필수 참조로 유지했습니다. 조건별 상세만 읽으며 각 폴더를 단독 복사할 수 있도록 형제 skill·역사 보존 공간에 대한 실행 의존성을 제거했습니다.
- Windows 배포 README·구조 안내·설정 예시 안내·UI 목록을 맞췄습니다. `status-report`의 기존 호출 정책은 유지했습니다.
- STYLE은 이전 표현 교정을 보존하고 Bash 예시를 Windows 예시로 바꿨습니다. 배포본에서 이동한 원문을 읽으라는 비교 연결만 제거했으며 실제 표현 정책·푸터 적용 조건·금지 표현의 부정 예시는 유지했습니다.
- 현재 검사기는 역사 보존과 native 계약을 구분합니다. Bash 실행 파일은 native 회귀의 필수 조건이 아니며, 과거 Bash 회귀는 실행 파일과 보존 도구를 함께 명시할 때만 별도로 선택합니다.

설정·권한·system/plugin skill·31 정책·새 PowerShell 템플릿·운영 적용은 변경하지 않습니다. 실제 Linux 실행, 새 세션의 자동 발견·선택·장기 행동은 이번 파일·도구 검사와 구분합니다.

## 2. 원형 보존과 구조

```text
2026-10-10-windows-native-T-WIN-004/
├── README.md
├── preservation-map.json
├── archive/codex_windows/     배포본에서 제외·교체한 원형
└── private/                  Git 제외, 실제 경로와 raw 보존
    ├── before/               source·현재 설치본·계약 이전본
    └── after/                source·현재 설치본·해시 결과
```

[보존 대응표](preservation-map.json)는 이전 경로·보존 경로·bytes·SHA-256·Linux/Kiro 대응본의 독립 해시를 기록합니다. 현재 원형 190파일을 보존했습니다. 이름이 같거나 대응본이 존재한다는 이유만으로 서로 다른 Windows bytes를 폐기하지 않습니다. Windows 독자 사본은 독립적으로 보존합니다.

archive와 새 Linux migration 보존 공간의 `.gitattributes`는 텍스트·줄바꿈 변환을 끕니다. 게시 후 다른 checkout에서도 원형 bytes와 기록 해시를 유지하기 위한 좁은 적용이며 기존 Linux 실행본의 속성은 바꾸지 않습니다.

- Windows 전체 이전본은 338파일입니다. 기존 진행 중 STYLE 수정과 다른 담당 초안도 보존했습니다.
- 기존 Git 기준 Linux 191파일·Kiro 55파일의 원형을 유지합니다. Linux 쪽에 없던 Bash 도구 2개는 출처별 경로로 `codex_linux/references/windows-migration`에 추가했습니다. 기록한 Linux inventory 193파일에는 이 신규 보존 2개도 포함됩니다. 두 도구의 SHA-256은 `9dfad74864d159ae08fb8a98af207c1463e24ba17a05ddfd91e20d7173af39db`입니다. 이 보존을 Linux 실행 검증으로 처리하지 않습니다.
- 역사 [source_manifest.json](../windows/verification/source_manifest.json)의 182파일·설정 2개와 source/보존 해시 368건을 유지합니다. STYLE 이전 이동 7개와 이번 보존 대응표를 순서대로 해석합니다. Windows 절차로 재작성한 `edge_case_testing.md` 두 문서의 역사 원문도 별도 보존했습니다.
- 과거 work-rules 사본 3개와 Linux AGENTS 대응 자료를 배포 폴더 밖에 원형 보존했습니다.

## 3. 검증과 알려진 한계

공식 `quick_validate.py`는 Python 3.12.14·PyYAML 6.0.3의 격리 가상 환경에서 21개 모두 종료 코드 0입니다. PyYAML은 개발 검사 환경에만 준비했으며 배포 runtime·system/plugin 파일은 바꾸지 않았습니다.

현재 검사 명령과 범위는 [검증 안내](../windows/verification/README.md)를 따릅니다. 최종 비식별 수치는 [검증 요약](validation-results.json)에 남깁니다.

- 현재 검사: native 21개·UI 21개·보존 해시 368건·archive 190개·Linux 도구 2개를 통과했습니다. Python 구문 34개와 단독 복사한 도구의 도움말 실행 27개도 통과했습니다.
- 회귀: 현재 계약 40조건, Markdown 91조건을 통과했습니다. Python·잠금 기능은 54조건 통과, Bash 미선택·심볼릭 링크 생성 능력은 2조건 건너뜀입니다. Windows 잠금 예시의 7조건도 통과했습니다.
- 문서: 188문서의 파일 링크 264개와 헤딩 904개에 오류가 없습니다. 파일 fragment 40개 중 교차 앵커 11개를 별도 확인하고 같은 파일 29개는 헤딩 검사로 확인했습니다. 외부 링크 13개는 도달성을 검사하지 않았습니다.
- Windows 예시: 배포 문서 185개에서 PowerShell fence 42개·고유 예시 12개를 구문 분석해 오류 0건입니다. 예시를 실행하거나 실제 서비스·SSH·운영 환경을 검사한 결과는 아닙니다.
- 표현: 68문서의 표 정렬 952건을 셀 내용·순서·비표 행을 유지하며 교정했습니다. 해당 문서의 표현·링크·헤딩은 모두 통과하고 변경된 SKILL 6개는 공식 검사를 추가 통과했습니다. 전체 181 skill 문서와 별도 목록 README를 확인했습니다.
- Git 보존: 원형 190개와 신규 Linux 도구 2개에서 실제 SHA-256·Git 필터 전후 객체 해시가 일치했습니다. 기존 Linux 원문과 Kiro 파일의 변경은 0건입니다.

앞선 검사 실패도 보존합니다. 초기 archive 경로 조합 오류는 source 변경 전에 중단했습니다. 첫 통합 검사는 Windows 독자 사본과 Linux 대응본의 해시 차이 처리 오류를 발견했고, 다음 검사는 역사 자원 문서의 이동 대응 누락을 발견했습니다. 회귀의 첫 실행은 격리 import 문제로 본문 실행 전에 실패했습니다. 각각 원인을 교정한 뒤 영향 검사를 다시 수행하며 이전 실패를 최종 성공으로 덮지 않습니다.

Markdown 회귀 첫 실행은 91조건 중 90개가 통과했습니다. 실패는 이미 이전 `main`과 before에서 `26.10.05`인 표현 검사기의 버전을 테스트가 `26.10.03`으로 기대한 항목입니다. 구현을 변경하지 않고 기대 버전을 실제 확정 계약에 맞췄으며 출력 버전의 정확 일치도 검사하도록 보강했습니다.

기존 STYLE의 금지 표현 부정 예시 진단은 동일한 7사본에 각 1건이며 전체 표현 검사의 종료 코드 1을 그대로 기록합니다. 변경하지 않은 배포 AGENTS의 기존 푸터 진단 3건도 유지합니다. SKILL·상세 참조에는 실제 STYLE 12절에 따라 공통 푸터를 자동 추가하지 않는 검사 범위를 적용했습니다. 이번 신규 표현 오류는 0건입니다. ASD-STE100 기술 판단은 별도 담당의 검토 범위이며 이번 정리에서 준수를 인증하거나 검사 정책을 완화하지 않습니다.

## 4. 로컬 반영과 게시

현재 설치된 35 관리 대상은 code-review, debugging-and-recovery, fact-check, git-commit-rule, goal-continuation, md-link-check, planning-and-breakdown, status-report, work-rules의 9개입니다. 다른 12개를 일괄 신규 설치하지 않습니다. 전체 설치 이전본 108파일과 사용자 추가 캐시 4개를 보존했습니다. 변경 직전 차이를 재대조하고 관리 대상만 반영하며 사용자 추가 파일은 유지합니다.

지정 9개에 반영했고 관리 파일 source 79개·local 79개의 경로·bytes·SHA-256이 일치합니다. 이전 관리 source에서 제거한 파일 53개만 정리했으며 캐시 4개와 범위 밖 markdown-review는 보존했습니다. after 사본은 배포 source 242파일·local 83파일이며 실제 파일과 일치합니다. 첫 설치 guard는 로컬 전체와 지정 9개를 혼동해 쓰기 전에 중단했습니다. 다음 helper는 설치 후 비교에 캐시를 포함해 중단했고, 재복사 없이 읽기 전용 대조로 정확한 관리·캐시 범위를 확인한 뒤 after를 보존했습니다.

구현 담당의 최종 후보 SHA·쓰기 종료 후 `35 · Git 통합` 담당이 기존 PLAN/TODO/HANDOFF/CHANGELOG를 연결하고 검토한 파일만 `main`에 일반 commit·push합니다. 게시 결과는 소유 상태 문서와 [완료 이력](../../../CHANGELOG.md)의 최종 영수증을 따릅니다. 다른 담당의 계획 초안과 private·실제 개인 설정은 게시 후보에서 제외합니다. 실제 원격 SHA와 commit 링크가 확인되기 전 게시 완료로 기록하지 않습니다.

사용자 요청에 따라 `02 · 총괄`과 `02 · 기술 검토`에 이번 범위·진행·검증·STYLE 해시와 담당 경계를 공유했습니다. 현재 사용자 확인 요청은 없습니다.

## 5. 복구

복구 전 현재 파일·사용자 추가 차이·해시를 before와 대조합니다. 이번 관리 변경만 선택 복원하고 이후 사용자 변경·다른 skill·설정·system/plugin은 보존합니다. archive와 Linux 추가 자료의 해시가 맞지 않으면 영향 단계만 중단합니다. 게시 후 복구는 검토한 revert로 수행하며 원격 보호 규칙을 우회하지 않습니다.

---

**작성일**: 2026-10-10

**마지막 업데이트**: 2026-10-10

© 2026 siasia86. Licensed under CC BY 4.0.
