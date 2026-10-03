# 개인 Codex skill 내용 검토

## 1. 대상과 판정

2026-10-03 yunli의 71ed82272c7cedb9fed219fcfaed8eab24440df3을 기준으로 Linux skill 19개의 본문·필수 참조·동봉 도구를 검토했습니다. Windows 영역은 계획·문서 골격이며 Windows SKILL 구현이나 개인 설치본은 검토 대상에 존재하지 않습니다.

현재 수정 필요 항목은 **P1 1건·P2 11건·P3 2건, 총 14건**입니다. 아래는 현재 파일에서 확인한 문제이며 플랫폼 이동으로 생긴 신규 결함은 아닙니다. 원문 보존과 이미 해결한 과거 문제를 재검토 결함 수에 포함하지 않습니다. 실제 모델이 잘못된 절차를 선택했거나 운영 장애가 발생했다고 주장하지 않습니다.

이번 작업은 검토·기록입니다. skill 본문·동봉 실행 코드·설치본·설정은 수정하지 않았습니다. 해결 여부는 아래 후속 검사를 통과한 뒤 별도로 판정합니다.

## 2. 수정 필요 항목

### 2.1 R01 P1 — Terraform state 복원을 리소스 롤백으로 안내

위치: [debugging-and-recovery](../../codex_linux/skills/debugging-and-recovery/SKILL.md) 200행.

인프라 변경 후 장애에 apply 이전 state 복원을 안내합니다. 실제 리소스는 그대로인데 state만 과거로 바꾸면 변경한 객체와 기록의 관계가 어긋날 수 있습니다. state는 객체와 설정의 대응 기록이며 수동 push는 state를 덮어씁니다. [Terraform state](https://developer.hashicorp.com/terraform/language/state), [수동 state 쓰기의 위험과 보호 검사](https://developer.hashicorp.com/terraform/language/state/backends#manual-state-pullpush).

일반 장애 롤백은 이전 설정을 기준으로 실제 rollback plan과 복구 조건을 검토하는 절차로 보완해야 합니다. state 자체의 손상 복구는 현재 승인 범위와 별도 절차를 확인합니다. **정적 검토이며 Terraform 명령·state 변경은 미실행**입니다.

### 2.2 R02 P2 — Bash 백업 실패를 성공으로 보고

위치: [bash-script-template](../../codex_linux/skills/bash-script-template/SKILL.md) 183–184행, using-skills 동봉 참조도 동일.

backup_conf의 cp 실패가 다음 성공 로그의 종료 상태로 덮입니다. 현행 COMPAT wrapper와 실패 guard를 적용한 TEMP 사례에서 cp를 종료 7로 실패시키자 일반 실행·set -e 실행 모두 성공 로그·AFTER_BACKUP·종료 0을 보였습니다. 필요한 백업 없이 후속 변경을 진행할 수 있습니다.

helper 자체에서 cp 실패를 즉시 반환하고 성공한 경우에만 완료 로그를 남겨야 합니다. 일반·set -e 양쪽에서 실패 상태 전파와 후속 차단을 검사합니다. **실패 주입 재현이며 실제 업무 파일의 복사·변경은 미실행**입니다.

### 2.3 R03 P2 — 기존 패키지의 롤백도 제거로 안내

위치: [spec-driven-infra](../../codex_linux/skills/spec-driven-infra/SKILL.md) 213행.

패키지 롤백을 state: absent로 일괄 안내합니다. 변경 전 이미 설치된 패키지의 업그레이드·설정 변경을 이대로 복구하면 필요한 패키지가 제거됩니다. absent는 제거를 의미합니다. [Ansible package 상태](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/package_module.html#parameters).

변경 전 설치 여부·버전·설정을 기록하고 신규 설치 제거, 기존 버전 복구, 설정 복구를 구분해야 합니다. **정적 검토이며 패키지 제거는 미실행**입니다.

### 2.4 R04 P2 — 의존성보다 위험도 우선으로 엔진 적용

위치: [incremental-change](../../codex_linux/skills/incremental-change/SKILL.md) 91–97행, debugging-and-recovery 동봉 참조도 동일.

Risk-First 예시는 RDS 엔진 업그레이드를 먼저 적용하고 앱 호환성 변경을 다음 slice에 둡니다. 현재 앱이 새 엔진과 호환되지 않는 작업에서는 첫 slice부터 같은 문서의 시스템 정상 유지 조건을 깨뜨립니다. 이 문구가 모든 작업에서 운영 DB 업그레이드를 강제한다고 확대 해석하지 않습니다.

위험도 우선순위는 의존성과 기존 앱 호환성 조건을 충족한 변경 사이에서 정하고, 호환성 검증·필요한 앱 준비를 엔진 적용의 선행 조건으로 명시해야 합니다. **정적 검토이며 DB 변경은 미실행**입니다.

### 2.5 R05 P2 — 데이터 마이그레이션의 롤백을 일괄 배제

위치: [shipping-checklist](../../codex_linux/skills/shipping-checklist/SKILL.md) 127행, [debugging-and-recovery](../../codex_linux/skills/debugging-and-recovery/SKILL.md) 198행.

데이터 마이그레이션이 있으면 rollback 불가·forward fix로 판정합니다. 하위 버전과 호환되는 nullable 열 추가 뒤 새 앱만 실패한 사례에서도 검증한 앱 버전 복귀를 배제하게 됩니다.

데이터 손실·하위 버전 호환성·복원 가능성·검증한 계획에 따라 앱 복귀와 데이터 복구를 구분해야 합니다. **정적 검토이며 마이그레이션·롤백은 미실행**입니다.

### 2.6 R06 P2 — 공개 서비스도 SG 준비 검사에서 차단

위치: [shipping-checklist](../../codex_linux/skills/shipping-checklist/SKILL.md) 58행.

0.0.0.0/0 없음 조건은 필요한 공개 HTTPS 구성의 준비 완료 판정을 차단합니다. 필수 code-review 참조는 정당화 근거가 없는 공개 inbound를 지적하므로 두 기준도 맞지 않습니다. AWS는 인터넷 공개 ALB의 listener에 공개 접근을 허용하고 backend는 ALB SG로 제한하는 구성을 안내합니다. [AWS ALB 권장 SG 규칙](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html#security-group-rules).

공개 용도·포트·대상·최소 권한 근거를 검토하도록 보완하고 관리 포트나 backend의 불필요한 공개와 구분해야 합니다. **정적 검토이며 SG 변경은 미실행**입니다.

### 2.7 R07 P2 — Python의 누락 입력 오류가 종료 0

위치: [python-script-template](../../codex_linux/skills/python-script-template/SKILL.md) 65·71·78·85행, using-skills 동봉 참조도 동일.

단일 누락 target, dry-run 누락, 유효·누락 파일 혼합, 유효·누락 디렉토리 혼합의 네 사례가 ERROR를 기록하면서 종료 0으로 끝납니다. CI나 호출자는 작업 성공으로 처리할 수 있습니다.

입력·처리 오류를 집계해 main 반환값을 프로세스 종료 상태로 전달해야 합니다. 혼합 입력의 계속 처리 정책과 최종 실패 반환을 함께 검사합니다. **실제 parser/main의 TEMP 제어 흐름 재현이며 업무 처리는 stub**입니다.

### 2.8 R08 P2 — lock 생성 실패 뒤 손상된 잠금 잔류

위치: [kiro-lock 도구](../../codex_linux/skills/kiro-lock/scripts/lock.py) 70–75행.

JSON 부분 쓰기 후 OSError를 주입하면 acquire 실패 뒤 guard는 정리되지만 손상된 lock은 남습니다. 이후 acquire·check·같은 token의 release까지 모두 실패합니다. using-skills·work-rules·zircon-readme-policy의 실행 사본도 같습니다.

guard 안에서 이번 획득이 만든 파일의 소유·inode를 확인해 실패 시 해당 파일만 정리해야 합니다. 기존 다른 소유자의 잠금이나 시간 경과만으로 오래된 잠금을 삭제하는 복구는 추가하지 않습니다. **실제 helper 사본의 TEMP 실패 주입**입니다.

### 2.9 R09 P2 — 명시한 Markdown 입력이 없어도 성공

위치: [파일 링크 도구](../../codex_linux/skills/md-link-check/scripts/md-link-check.py) 68·177–178행, [헤딩 도구](../../codex_linux/skills/md-link-check/scripts/md-heading-check.py) 202행.

두 도구에서 명시한 missing.md 단독 입력과 valid.md·missing.md 혼합 입력 네 사례가 모두 종료 0입니다. 경로 오타나 이동 누락이 검사 성공이 됩니다. 빈 디렉토리 정책과는 별개입니다.

명시한 입력의 부재를 수집해 비정상 종료하고, 검사 가능한 다른 파일의 결과와 누락 오류를 함께 보고해야 합니다. **현재 동봉 CLI의 TEMP 재현**입니다.

### 2.10 R10 P2 — 유효한 Markdown 경로를 깨진 링크로 판단

위치: [파일 링크 도구](../../codex_linux/skills/md-link-check/scripts/md-link-check.py) 38·119행.

실존하는 파일의 꺾쇠·공백 목적지와 균형 괄호 목적지를 정상 파싱하지 못합니다. 전자는 꺾쇠가 경로에 남고 후자는 첫 닫는 괄호에서 경로가 잘려 두 사례 모두 종료 1입니다. [CommonMark 링크 목적지 문법](https://spec.commonmark.org/0.31.2/#links).

코드·외부 링크 제외 범위를 유지하면서 정상 목적지의 꺾쇠·공백·괄호·escape를 처리하고 잘못된 목적지 사례도 함께 검사해야 합니다. **현재 동봉 CLI의 TEMP 재현**입니다.

### 2.11 R11 P2 — 중복 헤딩 suffix 앵커를 거부

위치: [헤딩 도구](../../codex_linux/skills/md-link-check/scripts/md-heading-check.py) 238행.

Overview 두 개와 두 번째를 가리키는 overview-1 앵커가 종료 1입니다. number·level·duplicate·toc 검사를 끄고 anchor만 켜도 실패하므로 중복 헤딩 금지 정책의 판정과 구분됩니다. [GitHub의 중복 section link 생성](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links).

문서 순서대로 slug와 중복 suffix를 생성해야 합니다. **현재 동봉 CLI의 TEMP 재현**입니다.

### 2.12 R12 P2 — 코드 예시를 실제 Markdown 본문으로 검사

위치: [파일 링크 도구](../../codex_linux/skills/md-link-check/scripts/md-link-check.py) 94행, [style 도구](../../codex_linux/skills/md-link-check/scripts/md-style-check.py) 47행.

파일 링크 도구는 인용 컨테이너 안의 fenced code에 있는 예시 링크를 실제 링크로 검사합니다. style 도구는 tilde fence 안의 H1을 실제 H1으로 세므로 각각 종료 1입니다. 이전에 해결한 긴 backtick 중첩 문제와 다른 결함입니다. [CommonMark fenced code](https://spec.commonmark.org/0.31.2/#fenced-code-blocks).

인용 컨테이너·fence 문자와 길이를 처리해 코드 내용을 제외하고 정상 블록·미닫힘·진짜 코드 밖 오류를 함께 검사해야 합니다. **현재 동봉 CLI의 TEMP 재현**입니다.

### 2.13 R13 P3 — 검증 표의 필수 대상 인수 누락

위치: [testing-guide](../../codex_linux/skills/testing-guide/SKILL.md) 128–129·146행.

Ansible syntax/check 예시는 playbook, Docker inspect 예시는 container가 없어 그대로 실행하면 검사할 대상을 전달하지 못합니다. 대상 placeholder와 필요한 health check 조건을 명시해야 합니다. [ansible-playbook usage](https://docs.ansible.com/projects/ansible/latest/cli/ansible-playbook.html#synopsis), [docker inspect usage](https://docs.docker.com/reference/cli/docker/inspect/).

**문법·정적 검토이며 Ansible/Docker 실행은 미실행**입니다.

### 2.14 R14 P3 — Python 도움말의 미등록 옵션

위치: [python-script-template](../../codex_linux/skills/python-script-template/SKILL.md) 38행, using-skills 동봉 참조도 동일.

도움말의 원복 예시는 -r을 사용하지만 현행 parser에 등록되지 않아 종료 2입니다. 구현된 옵션에 맞춘 예시를 제공하고, 원복 기능이 필요한 작업이라면 그 옵션·처리 계약을 함께 정의해야 합니다. **실제 parser/main의 TEMP 재현**입니다.

## 3. 검증과 적용 범위

- **정적 확인:** 19개 SKILL 본문·필수 참조를 분담 검토했습니다. name 기본 형식·폴더명 대응·중복·description 존재 19개, 보존 원문 bytes 대응 19개, Python 도구 AST 25개는 정상입니다. 정식 YAML parser 검사는 실행하지 않았습니다.
- **사본 확인:** Markdown 도구 세 종류는 각각 7개 사본의 해시가 같고 lock helper는 4개가 같습니다. Python/Bash 함수는 using-skills 참조에도 있으므로 수정·검증 시 실제 동봉 사본을 함께 관리해야 합니다. 비교 원문은 보존합니다.
- **직접 실행:** Windows Python 3.14.8·UTF-8으로 Markdown CLI 10회, Python CLI 6회, lock 생성 실패 주입과 후속 재시도·확인·해제 4호출을 수행했습니다. Markdown 10회 중 reference-style 관찰 1회는 도구가 선언한 inline 범위 밖이어서 신규 결함 수에 넣지 않았습니다. Python 업무 처리 함수는 dispatch stub이며 실제 원자적 쓰기는 실행하지 않았습니다.
- **직접 실행:** Ubuntu TEMP에서 실제 Bash 함수의 cp만 종료 7 stub으로 바꾼 일반·set -e 사례 2회를 수행했습니다. 실제 백업·서비스 명령은 실행하지 않았습니다. 같은 Python 제어 흐름과 lock 실패도 Ubuntu Python 3.6.7에서 부분 재현했지만 요구 3.11+ 환경 전체의 통과로 취급하지 않습니다.
- **미실행:** 전체 Linux 3.11+ 회귀, 최종 모델 행동·자동 선택·개인 설치·발견·운영 적용·실제 Terraform/Ansible/Docker/DB 변경은 수행하지 않았습니다. 기존 보존 원문 링크 2건과 과거 완료 기록은 새 결함·새 성공으로 세지 않았습니다.
- **기록:** 입력 해시·stdout/stderr·원시 결과는 비공개 로컬 evidence로 보존합니다. 공개 자료에는 개인 절대 경로·계정·설정·raw 증거를 복사하지 않습니다.

## 4. 후속 순서와 게시

R01의 복구 안내를 우선 보완하고, R02–R08의 오류 전파·변경 전 상태·의존성·잠금 실패 정리를 처리합니다. 이어 R09–R12의 입력 검증과 Markdown 파싱을 보완하고 R13–R14의 안내를 맞춥니다. 각 수정은 실패 사례와 정상 제어 사례를 함께 검사합니다.

Linux 원문·비교 사본을 보존한 채 필요한 COMPAT 대체 절차·실행 도구를 보완하는 방식으로 진행할 수 있습니다. 이번 검토를 원문 삭제·축약·19개 Windows 자동 복제의 승인으로 사용하지 않습니다. Windows 재작성에서도 해당 실패 사례가 재발하지 않도록 [Windows PLAN](windows/PLAN.md)에 연결합니다.

기록·TODO 연결만 yunli에 일반 commit·push하고 사용자 검증을 기다립니다. main은 사용자 검증 완료 후 반영·push하며 검토 결과 게시를 결함 수정 완료나 운영 적용 완료로 처리하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
