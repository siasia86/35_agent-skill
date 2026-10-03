# Codex 개인 스킬 검증 기록

1~5절은 2026-10-01 당시의 검사 기록입니다. 최신 로컬 보완 결과는 6절을 따르며 과거 게시·모델 지정은 새 실행 권한이나 현재 검증 결과가 아닙니다.

## 1. 목적과 실행 범위

2026-10-01 작성한 19개 개인 스킬을 각 폴더 단독 복사 상태에서 검증합니다. Kiro 원문 보존·발견 가능한 frontmatter·내부 참조·도구 독립 실행과 실제 개인 규약 적용을 확인합니다. 주 agent의 정적/실행 검사와 Luna의 독립 사례를 구분합니다. 모든 변경/실행은 저장소와 격리 /tmp 프로젝트 안에서 수행했으며 개인 홈 설치·다른 저장소 수정·운영 적용은 수행하지 않았습니다.

요청 모델은 사용자 지정 Luna에 해당하는 `gpt-6-luna`, reasoning medium입니다. 협업 API에 이 값을 지정했으나 runtime 내부 모델명을 별도로 조회/증명할 수 없으므로 실제 backend 식별과 혼동하지 않습니다. 첫 문서/원문 조사 agent와 독립 사례 agent 3개를 사용했습니다. 독립 사례에는 해당 단독 skill 폴더·최소 raw fixture·실제 요청만 전달했고 정답·수정 가설·이전 결론은 주지 않았습니다. 최초 결과와 필요한 보완 후 재검사를 모두 보존합니다.

## 2. 주 agent 검사

- **통과**: frontmatter quick_validate 19개. Bash·Python의 원문 description은 YAML 파싱에 실패했고 내용 전체를 인용한 뒤 19개 모두 통과했습니다.
- **통과**: Kiro 원문 19개·동봉 워크플로 45개·비교 사본의 전체 bytes 대응. 호환 절과 두 description 인용만 되돌리면 원문과 같습니다. 실제 diff에서 본문 삭제·축약·통합이 없습니다. [MIGRATION](MIGRATION.md)에 원문 해시·행 대응·변경 이유를 기록합니다.
- **통과**: 각 폴더의 실제 로컬 링크 173개가 같은 폴더 안의 파일로 연결됩니다. symlink·형제 설치 폴더 의존이 없습니다. 활성 자료 73개에서 파일 링크 175개 정상입니다.
- **통과**: 원문 비교 자료까지 포함한 Markdown 139개·헤딩 2,764개에서 heading 검사 오류 0건입니다. 다른 파일 앵커는 별도 대조했고, README 사례의 깨진 `guide.md#missing-section`도 실제 대상 헤딩으로 수정했습니다.
- **통과**: 동봉 Python 파일 25개 구문 검사. 서로 격리한 단독 스킬 사본에서 `python3 -I`로 검사 도구 실행 35회(유효 문서 통과·잘못된 파일/앵커 검출·style CLI 접근)를 확인했습니다. 외부 pip·30 저장소 설치 없이 실행했습니다.
- **통과**: 잠금 경쟁 12개 프로세스에서 획득 성공 1개, 다른 토큰 해제 거부·자기 소유 확인/해제·손상 파일·symlink·남은 guard 보존 등 8개 실제 불변 조건. 참여 helper 간 보호이며 비협력 writer/네트워크 파일시스템 전체의 강제 격리는 주장하지 않습니다.
- **부분 검사**: 활성 스킬/자료 전체의 원시 style 결과는 234건입니다. 푸터가 없는 지침 파일에 일반 문서 푸터를 요구한 항목과 원문 예시의 경고를 포함합니다. 지침 파일의 푸터 금지 기준을 적용해 source와 동일하게 검사하면 기존 원문 경고 51건, 활성 경고 51건, 새 경고 0건입니다. 경고는 삭제/허위 통과로 바꾸지 않고 [style-baseline.json](verification/style-baseline.json)에 파일별 비교를 남깁니다. STYLE의 부정 예시·다이어그램 등 보존 내용을 임의로 고치지 않았습니다.
- **부분 검사**: 게시 clone의 전체 `git diff --cached --check`는 testing-guide 원문 118행의 후행 공백을 보존한 사본 4곳에서 보고합니다. 원문 동일 bytes 기준을 우선해 임의로 지우지 않았습니다. 보고된 네 줄이 그 원문과 같음을 확인했고, 후행 공백 항목만 제외한 검사에서는 다른 오류가 없습니다. 무조건 diff 검사 통과로 기록하지 않습니다.

개발 검사는 다음과 같이 다시 실행합니다. 첫 명령은 원문 대조·독립 복사·실제 잠금 검사를 포함하고 임시 검증 폴더만 생성합니다. 실제 개발 저장소의 원문이 필요하지만 복사한 개인 스킬의 사용 의존성은 아닙니다.

```bash
python3 codex/verification/verify_skills.py
python3 codex/skills/md-link-check/scripts/md-heading-check.py codex/skills
```

원문 비교용 `references/originals/edge_case_testing.md` 두 파일에 남은 과거 32 저장소 BVA 상대 링크는 현재 폴더에서 해석되지 않습니다. 비교 bytes를 유지하기 위한 역사 자료이며 실행/참조 의존이 아닙니다. 활성 edge case 문서의 링크는 같은 폴더로 교체하고 검사했습니다. raw 비교 자료를 포함한 링크 검사와 활성 링크 검사를 구분합니다.

## 3. Luna 사례 19개

아래 상태는 해당 fixture에서 관찰한 결과입니다. [luna-results.json](verification/luna-results.json)에 각 최초 보고·후속 보고·test 당시 skill 해시·실제 산출물 전체를 저장했습니다. 검사 도구가 필요하지 않은 계획/리뷰 스킬에 자동 문서 검사기를 필수 설치하지 않습니다.

| 스킬                   | 실제 요청/관찰                       | 결과와 제한                                                                |
|------------------------|--------------------------------------|----------------------------------------------------------------------------|
| bash-script-template   | 텍스트 파일 줄 수 CLI 작성·실행      | 후속 통과; 헤더/날짜·단순 예외, 빈/개행 없는 행·누락 입력                  |
| python-script-template | JSON 검사 CLI 작성·실행              | 후속 통과; SAFETY/VERSION/help·단순 예외·JSON 오류                         |
| code-review            | average 함수 읽기 전용 리뷰          | 통과; 빈 입력 나눗셈 오류 위치·영향, 코드 보존                             |
| testing-guide          | 범위 판정 함수의 unittest 작성·실행  | 통과; 4개 메서드, 경계·bool/타입·빈 값                                     |
| md-link-check          | 깨진 파일/교차 앵커 수정             | 통과; 파일·헤딩 검사와 대상 앵커 직접 대조                                 |
| readme-template        | 실제 cli.py 설치·실행 안내           | 후속 통과; 저장소 푸터 금지, 실제 도움말 확인                              |
| zircon-readme-policy   | 일반 fixture에 Zircon 예외 적용 여부 | 통과; 해당 저장소가 아니므로 예외 전파 없음                                |
| work-rules             | 승인된 README 한 문장 편집           | 후속 통과; 범위 준수·저장소 footer 예외 검사                               |
| using-skills           | 문서 링크 작업의 스킬 선택 설명      | 통과; 폴더 내 md-link-check 참조 선택, 파일 미지정 검사는 미실행           |
| repo-governance        | 현재 적용 지침 확인                  | 부분 검사; AGENTS 확인, 없는 Git/governance 초기화 없음                    |
| git-commit-rule        | README만 로컬 commit                 | 후속 통과; review branch 유지·단일 stage·한국어 메시지, push 없음          |
| kiro-lock              | 다른 세션 잠금 아래 편집 시도        | 보호 동작 확인; check 차단·타인 잠금/README 보존, 편집 미실행              |
| planning-and-breakdown | JSON 리포트 CLI 계획                 | 계획 작성 통과; 계약 선행·의존·완료/검증·복구, 자동 문서 검사 미실행       |
| spec-driven-infra      | 테스트 VPC 요구사항/설계             | 초안 작성 통과; 미확인 계정/CIDR/규모·권한 분리, cloud 미실행              |
| incremental-change     | Terraform 단일 값 변경               | 부분 검사; fmt 통과, provider 부재로 validate 실패, init/plan/apply 미실행 |
| debugging-and-recovery | 관찰 로그로 복구 제안                | 계획 작성 통과; DB 포트 가설·검증/복구, live 원인 확정 미실행              |
| doubt-driven-infra     | 단일 AZ NAT의 HA 주장 검토           | 리뷰 통과; 공통 장애점·주장 정정·추가 증거, cloud 미실행                   |
| shipping-checklist     | 제공 증거로 배포 준비 판정           | 판정 통과; 건강/모니터링 미확인으로 준비 미완료, 배포 없음                 |
| security-tools         | Dockerfile/JSON 수동 보안 감사       | 후속 통과; Docker 위험·placeholder 구분, 원문 scanner/마스킹 미실행        |

초기 Bash/Python CLI는 기능 검사를 통과했지만 필수 개인 헤더·SAFETY/VERSION/help 적용이 부족했습니다. 기능 성공을 개인 템플릿 적용 성공으로 사용하지 않고 스킬에 원문 대조 기준을 보완해 새 산출물과 실행 결과를 확인했습니다. 권한 거부 입력은 root의 chmod로 재현되지 않았고, 별도 사용자 실행도 격리 환경에서 그룹 변경이 거부되어 미실행입니다. 권한을 바꾸거나 우회하지 않았습니다.

초기 work-rules·Git·security 감사의 style checker는 저장소가 금지한 푸터를 요구했습니다. 실제 저장소 지침을 근거로 footer 검사만 제외하는 절차를 추가한 뒤 style·heading·link 검사가 통과했습니다. 원문 코드/체크리스트는 유지했습니다.

## 4. 우선순위 추가 사례

- 사용자 > 저장소: 저장소의 푸터 기본값이 있어도 사용자 요청이 푸터·배지·날짜를 금지한 fixture에서 생략하고 CLI·문서 검사를 통과했습니다.
- 저장소 > 개인: README/work-rules/Git/security fixture의 AGENTS 금지 규칙에 따라 개인 푸터 기본값을 적용하지 않았습니다. 다른 검증은 수행했습니다.
- 개인 기본값: 별도 AGENTS가 없는 fixture에 개인 목차·번호·통계·날짜·라이선스 양식을 적용했습니다. 첫 입력은 저작권/작성일 등 확인 자료가 부족해 부분 검사였으며 기존 날짜·LICENSE를 제공한 추가 fixture에서 작성일 보존·업데이트 날짜·owner/repo 배지·라이선스를 확인해 문서/CLI 검사를 통과했습니다. 없는 Actions는 만들거나 있다고 주장하지 않았습니다.

## 5. 현재 완료와 미실행

저장소 모음 작성·원문 대응·단독 복사·로컬 실행·각 역할의 Luna 사례를 완료했습니다. 실제 개인 홈의 설치/새 세션 발견/자동 선택, Windows·PowerShell, AWS·Ansible·Docker build·서비스 적용, 원래 보안 실행 도구/map 호환성은 미실행 또는 미검증입니다. [TODO](TODO.md)에 남기며 Linux fixture 결과를 이 항목의 완료 근거로 사용하지 않습니다.

루트 문서·workflow·Git diff·원본 보존·Gitleaks와 게시 검사는 [이번 실행 기록](../agent-workflows/codex/REBUILD_1.0.0.md)에 기록합니다. 원본 main 작업본의 Git 관리 영역을 수정하지 않고 독립 게시 clone에서 승인된 yunli 일반 push를 수행합니다.

## 6. 2026-10-03 로컬 보완과 회귀 검사

- **통과:** 수정 전 최소 재현으로 동작 문제 5개를 다시 확인했습니다. [baseline.json](../agent-workflows/codex/reviews/2026-10-03-remediation/baseline.json)은 새 관찰이며 기존 재현 JSON은 보존합니다.
- **통과:** 보완 후 unittest 16개와 실제 CLI 실행 120회입니다. Python 무인수/help/version/잘못된 옵션·처리 분기, 기존 파일 mode/uid/gid·새 파일 0600·실패 시 원본 유지/임시 파일 정리, Bash 상태 7 전파/로그/후속 차단·인수 보존, flock inode 유지/프로세스 간 배제/예외 해제, 링크 검사기 7개의 중첩·tilde·들여쓰기·미닫힘·기존 제외를 확인했습니다. [회귀 스크립트](verification/test_remediation.py)와 [원시 결과](../agent-workflows/codex/reviews/2026-10-03-remediation/tests.json)에 입력 해시·명령·종료·stdout/stderr를 남깁니다.
- **통과:** 기존 기본 검사에서 스킬 19개·동봉 역할 54개·폴더 내부 링크 213개·Python 도구 구문 25개·단독 도구 실행 35회·kiro-lock 조건 8개를 확인했습니다. Kiro 원문 bytes와 전체 본문 대응도 유지합니다. [기본 검사 결과](../agent-workflows/codex/reviews/2026-10-03-remediation/basic-check.json)를 참고합니다.
- **통과:** 새 문서 style 경고 0건·앵커 13개·frontmatter 19개·변경 Python 구문·diff·보호 원본 보존을 확인했습니다. 원시 style 경고 89건은 source/푸터의 기존 경고이며 전체 style 무경고 통과로 기록하지 않습니다. 회귀 입력 해시 80개도 현재본과 같습니다.
- **검증 범위:** 소유 보존은 동일 uid/gid의 실제 교체와 fchown 거부 주입으로 검사했습니다. 다른 소유의 실제 파일·ACL·확장 속성·하드 링크·Windows 메타데이터 보존은 검증하지 않았으며 POSIX 대체 예시의 범위에서 제외합니다.
- **미실행:** 최종본의 독립 모델 행동 사례·개인 홈 설치/발견·Windows·운영 적용·commit/push입니다. 기존 Luna 결과를 새 수정본의 독립 행동 통과로 사용하지 않습니다. Gitleaks 실행 도구가 없어 정규식 검사만 별도 부분 검사로 기록합니다.

문서 검사·보존·변경 파일과 남은 항목은 [보완 기록](../agent-workflows/codex/REMEDIATION_2026-10-03.md)에 남깁니다. 기본 검사와 회귀 검사는 각각의 범위를 확인하며 실제 사용자 환경 전체를 보장하지 않습니다.

```bash
python3 codex/verification/test_remediation.py --output /tmp/35-remediation-tests.json
python3 codex/verification/verify_skills.py
```

---

**작성일**: 2026-10-01

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
