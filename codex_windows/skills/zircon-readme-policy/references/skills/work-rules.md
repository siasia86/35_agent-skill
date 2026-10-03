---
name: work-rules
description: Apply personal operating rules for repository work, progress reports, scoped skill selection, task records, validation and artifact paths. Use when executing, reviewing or resuming repository tasks; preserve existing authorization and keep simple questions lightweight.
---


# 개인 Codex Work Rules

<!-- CODEX-COMPAT-BEGIN -->
지속적인 repo 실행·검토·재개에 적용합니다. 단순 질문에는 필요한 항목만 사용합니다. 현재 사용자 요청·적용 repo 지침·플랫폼 정책과 실제 도구 권한을 확인하고 이미 승인된 작업의 확인을 반복하지 않습니다.

## 1. 시작·범위·협업

- 실제 Git 루트·branch·기존 변경·적용 AGENTS/override를 먼저 확인합니다. 다른 repo의 profile과 과거 승인·예시는 자동 적용하지 않습니다.
- 작업ID·담당 파일·예정 commit 파일 목록을 명시하고 다른 세션의 변경을 보존합니다. 검토한 담당 파일만 staging합니다.
- 네이티브 Windows는 PowerShell과 확인한 Python을 사용합니다. 파일 작업은 LiteralPath와 검증한 절대 경로로 처리하며 다른 shell로 삭제·이동을 구성하지 않습니다. Linux/WSL/원격 실행은 별도 실제 환경으로 판단합니다.
- 개인 config 기본값, 현재 세션 정책, 추가 명령 승인과 OS ACL을 구분합니다. config만으로 세션 경계를 변경했다고 보고하지 않습니다.

## 2. 요청과 보고

- 채팅의 `;`는 여러 요청을 구분합니다. 코드·명령·문자열·경로·인용문의 세미콜론은 유지하고 요청별 완료 상태를 확인합니다.
- 작업 전 무엇을 수행하는지·대상·범위·검증 방향을 알립니다. 진행 중에는 의미 있는 결과·남은 조건을 공유합니다.
- 완료 후 수행·결과·검증·미실행·잘된 점과 문제를 한국어로 간결하게 보고합니다. 설치·발견·선택·행동·게시·운영 적용은 관찰별로 구분합니다.
- 결과물 설명 위에 실제 로컬 경로를 표시하고 파일을 링크합니다. 큰 결과는 비교 표·tree·필요한 단계 구조로 제시합니다. 원격 문서에는 상대 경로·공개 별칭만 사용합니다.

## 3. 상태·모델·skill

- 상태·이력은 각 실제 repo의 기존 관리 공간에서 유지합니다. README는 개요·진입점, INDEX는 구조·읽기 조건·skill 연결입니다. 기준 상태는 TODO 등 한 원본에 두고 완료 기록과 링크를 보존한 뒤 활성 목록을 정리합니다.
- 큰 작업만 범위·완료 조건·결과/검증 링크를 관리합니다. 작은 작업에 모든 문서·빈 폴더를 생성하지 않습니다. 고정 제품·skill 경로·개인 runtime·sealed 자료는 원위치에서 연결합니다.
- 정형 검색·조회·추출·대조는 현재 지원되는 Luna에 우선 배정합니다. main은 핵심 근거·설계·최종 검증을 담당합니다. 짧은 조회는 직접 할 수 있으며 실제 모델 선택을 확인하고 설정은 자동 변경하지 않습니다.
- 큰 분해는 [planning-and-breakdown](../skills/planning-and-breakdown.md), commit은 적용 repo 기준과 필요한 git-commit-rule을 선택합니다. 다른 skill 전체를 자동 로드하지 않습니다.
- 개인 skill은 전체 폴더가 사용 단위입니다. 기존 동명 전체 사본·차이·해시를 보존한 뒤 지정 대상만 교체하고 별도 skill·system·plugin·config는 해당 범위를 따릅니다.
- 사용자가 업데이트별 보관을 지정한 개인 skill·config 갱신에서는 해당 repo의 기존 관리 공간에 날짜·목적·작업ID별 폴더 하나로 before/after·설정·검증·복구를 보존합니다. 다음 업데이트는 새 이름을 사용합니다. 원형 홈 백업·개인 설정·raw는 실제 Git 제외를 확인하며 공개 가능한 skill 사본은 지정 범위와 개인정보 검사 후 보존합니다.

## 4. 검증·게시

- 검사기는 repo에 명시된 도구·버전·설정을 우선합니다. 지정이 없으면 실제 동봉 도구를 fallback으로 사용하고 선택 이유·경로·검사 수·종료 상태를 기록합니다. 다른 검사기로 필수 gate를 대체하거나 성공한 마지막 결과로 앞선 실패를 덮지 않습니다.
- Markdown 대상 0개는 검증 미완료입니다. 동봉 link checker는 exit 2를 반환합니다. 명시 입력·실제 선택 개수·읽기 실패를 확인하고 빈 대상을 성공으로 처리하지 않습니다. 파일 링크와 fragment·외부 도달성은 별도 검사 범위입니다.
- 변경 위험과 repo 필수 검사에 맞춰 검증합니다. 원문과 역사 자료의 보존을 확인하고 미실행을 완료로 바꾸지 않습니다. 반복 실패에는 새 근거와 다른 접근을 사용하며 승인 범위를 확대하지 않습니다.
- 승인된 branch의 검토한 파일만 commit·일반 push하고 원격 commit을 확인합니다. 해당 repo의 사용자 검증 순서를 지키며 force·보호 branch·release·운영 변경은 지정 범위를 확인합니다. 다른 repo에 35의 branch를 강제하지 않습니다.

## 5. 필요한 참조만 읽기

| 상황                                            | 참조                                                                                                                                                                                             |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Workflow 구조·상태·산출물 설계                  | [repository-workflow](../repository-workflow.md)                                                                                                                                                 |
| Windows 인코딩·config/status·SSH·원문 대응 상세 | [Windows 상세](../windows-work-rules-details.md)                                                                                                                                                 |
| 원문 비교·과거 예시 확인                        | [보존 본문](../legacy-work-rules.md), [Kiro 원문](../originals/work-rules.md)                                                                                                                    |
| 문서 개인 양식                                  | [STYLE](../STYLE.md)                                                                                                                                                                             |
| 변경 범위·잠금·IaC·README의 실제 필요           | [incremental-change](../skills/incremental-change.md), [kiro-lock](../skills/kiro-lock.md), [spec-driven-infra](../skills/spec-driven-infra.md), [readme-template](../skills/readme-template.md) |

Windows 상세는 해당 기능이 필요한 때 읽습니다. 보존 본문의 Bash/POSIX/Kiro 규칙·개인 경로·고정 branch·과거 승인 예시는 비교 자료이며 자동 실행·전체 읽기 조건이 아닙니다. 폴더 안의 필수 자료로 완결되며 중앙 catalog·installer·형제 skill 설치를 필수로 요구하지 않습니다.
<!-- CODEX-COMPAT-END -->
