---
name: using-skills
description: Select the relevant Windows-native skill and bundled references for the current request. Use when task routing is unclear; do not load every skill for simple questions.
---

# Windows skill 선택

현재 요청의 목적과 실제 적용 지침에 맞는 역할만 선택합니다. 이 폴더는 필요한 지침·도구를 동봉하며 형제 skill이나 중앙 설치기를 준비할 필요가 없습니다.

## 1. 먼저 확인할 기준

- 사용자 요청·플랫폼 정책·실제 권한·적용 저장소 지침을 대조합니다. 계획·검토 요청을 구현·게시·운영 적용으로 확대하지 않습니다. 이미 승인된 범위는 반복 확인하지 않습니다.
- 실제 Git 루트·branch·기존 변경·AGENTS와 하위 지침을 확인하고 다른 작업·개인 차이·비공개 자료를 보존합니다. `.governance`는 실제 적용 범위에서 읽습니다.
- PowerShell·Git·실제 Python 3.11 이상을 사용합니다. Python은 `-X utf8 -B`, 파일 입출력은 UTF-8을 명시합니다. 파일 작업은 확인한 절대 경로와 `-LiteralPath`를 사용합니다.
- CLI 종료 코드와 PowerShell 오류를 구분하고 검사 대상 0개·읽기 실패·미실행을 성공으로 처리하지 않습니다. 설치·발견·선택·행동·게시·운영 적용은 실제 관찰별로 구분합니다.
- 문서 역할·위치·푸터·상태·게시 절차는 대상에 실제 적용한 지침을 따릅니다. 31의 미배포 template/profile이나 다른 repo의 규칙을 자동 적용하지 않습니다.
- 일반 개인 개발은 현재 승인과 원격 보호 규칙 안에서 검증·기록 후 담당 파일만 `main`에 일반 게시합니다. QA·복구·upstream의 경계와 사용자 제한을 유지합니다.

## 2. 필요한 역할 선택

- 지속 작업의 수행·검토·재개: `work-rules`; 별도 상황보고: `status-report`.
- 저장소 규칙과 예외: `repo-governance`; Zircon README의 실제 적용 기준: `zircon-readme-policy`.
- 큰 목표·의존성·실행 분해: `planning-and-breakdown`; 승인된 목표 이어가기: `goal-continuation`.
- 요청 문서의 전체 사실 검증: `fact-check`; Markdown 링크·앵커·헤딩: `md-link-check`; README 양식: `readme-template`.
- 코드·스크립트·IaC 검토: `code-review`; 시험 설계: `testing-guide`; Python 업무 골격: `python-script-template`.
- 인프라 명세: `spec-driven-infra`; 점진적 변경: `incremental-change`; 가정·불확실성 검토: `doubt-driven-infra`.
- 장애·복구: `debugging-and-recovery`; 배포 준비: `shipping-checklist`; 보안 도구·비밀정보: `security-tools`.
- 협조자 잠금: `kiro-lock`. 이름은 유지하며 실제 도구는 Windows 동봉 Python helper입니다.

단순 질문·제한된 수정은 필요한 역할만 사용합니다. PLAN·TODO·Goal·잠금·추가 agent를 모든 요청에 강제로 만들지 않습니다. PowerShell 업무를 다른 언어의 템플릿 이름으로 대체하지 않습니다.

## 3. 동봉 지침

아래 참조는 이 폴더 안에서 읽는 지침입니다. 원래 skill이 실제 설치되어 있고 사용자가 지정했다면 그 출처를 먼저 사용하며, 같은 본문을 두 번 읽지 않습니다. 필수 skill 사용·설치·자동 발견을 동봉 문서 읽기로 대신 보고하지 않습니다.

- [code-review](references/skills/code-review.md).
- [debugging-and-recovery](references/skills/debugging-and-recovery.md).
- [doubt-driven-infra](references/skills/doubt-driven-infra.md).
- [fact-check](references/skills/fact-check.md).
- [git-commit-rule](references/skills/git-commit-rule.md).
- [goal-continuation](references/skills/goal-continuation.md).
- [incremental-change](references/skills/incremental-change.md).
- [kiro-lock](references/skills/kiro-lock.md).
- [md-link-check](references/skills/md-link-check.md).
- [planning-and-breakdown](references/skills/planning-and-breakdown.md).
- [python-script-template](references/skills/python-script-template.md).
- [readme-template](references/skills/readme-template.md).
- [repo-governance](references/skills/repo-governance.md).
- [security-tools](references/skills/security-tools.md).
- [shipping-checklist](references/skills/shipping-checklist.md).
- [spec-driven-infra](references/skills/spec-driven-infra.md).
- [status-report](references/skills/status-report.md).
- [testing-guide](references/skills/testing-guide.md).
- [work-rules](references/skills/work-rules.md).
- [zircon-readme-policy](references/skills/zircon-readme-policy.md).

## 4. 조건별 도구와 상세

- 문서 표현이 필요할 때: [STYLE](references/STYLE.md).
- 실행 환경·인코딩: [Windows runtime](references/windows/runtime-and-encoding.md).
- Windows SSH·ACL: [SSH와 ACL](references/windows/ssh-and-acl.md).
- 잠금이 필요한 작업: [Windows 잠금](references/windows/file-lock.md)과 `scripts/lock.py`.
- 문서 검사: `scripts/md-style-check.py`, `scripts/md-heading-check.py`, `scripts/md-link-check.py`; 공통 파서는 `scripts/md_common.py`.
- Python 업무: `scripts/script_template.py`; 실패·경계 시험: [시험 상세](references/resources/edge_case_testing.md).

실제 필요한 도구만 실행하고 `--help` 성공을 전체 동작 시험으로 기록하지 않습니다. 정형 검사는 운영 상세의 Luna 배정과 현재 승인 범위를 따릅니다. 다른 실행 환경은 해당 플랫폼의 별도 지침을 사용합니다.
