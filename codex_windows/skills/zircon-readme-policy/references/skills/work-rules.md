---
name: work-rules
description: Apply personal operating rules when executing, reviewing or resuming repository work. Report scope and verification, preserve existing authorization, and select only task-relevant references. Keep simple questions lightweight.
---

# 개인 Codex Work Rules

<!-- CODEX-COMPAT-BEGIN -->
Windows 개인 작업의 공통 실행 기준입니다. 현재 사용자 요청·적용 repo 지침·플랫폼 정책과 실제 권한을 확인하고 이미 승인된 범위는 반복 확인하지 않습니다.

## 1. 시작과 보고

- 저장소 작업은 실제 Git 루트·branch·기존 변경·적용 AGENTS와 하위 지침을 확인합니다. 여러 세션이 함께 작업하면 작업ID·담당 파일·예정 commit 파일을 명시하고 다른 변경을 보존합니다. 단순 질문을 저장소 전체 조사로 확대하지 않습니다.
- 작업 전 대상·수행 내용·검증 방향을, 진행 중 의미 있는 관찰을, 완료 후 결과·검증·미실행·확인된 성과와 문제를 한국어로 간결하게 보고합니다. 큰 결과는 표·tree를 사용하고 결과물 설명 위에 실제 경로와 링크를 둡니다. 공개 문서에는 공개 가능한 상대 경로·별칭을 사용합니다.
- 채팅의 `;`는 여러 요청의 구분자입니다. 코드·명령·문자열·경로·인용문 안에서는 원래 문법을 유지하고 요청별 완료 여부를 확인합니다.
- 실제 대상에 적용된 운영·기록·검증·게시 규칙을 따릅니다. 31의 template/profile은 작성·배포 원본이며, 다른 repo의 profile이나 미배포 중앙 변경을 자동 적용하지 않습니다. 개인 skill에서 문서 역할·기록 위치·푸터·게시 branch를 재정의하지 않습니다.
- 기존 기록·사용자 편집·비공개 증거를 보존하고 단순 작업에 빈 문서·폴더를 일괄 생성하지 않습니다. 고정 제품·도구·skill·sealed 자료·runtime 경로는 실제 계약을 유지합니다.

## 2. 실행과 검증

- Windows 파일 작업은 확인한 절대 경로와 PowerShell `-LiteralPath`를 사용하고 shell을 섞어 삭제·이동하지 않습니다. Linux/WSL/원격은 별도 실제 환경으로 확인합니다. config 기본값·현재 세션 정책·추가 승인·OS ACL을 구분합니다.
- 범위와 판정 기준이 정해진 정형 검색·조회·대조는 지원되는 Luna에 우선 배정하고 main이 판단과 최종 검증을 담당합니다. 짧은 조회는 직접 수행하며 모델·설정은 자동 변경하지 않습니다.
- 개인 skill 수정은 35_agent-skill의 관리 원본에서 진행하고 검증한 뒤 로컬 설치본에 반영합니다. 로컬만 단독 수정하지 않으며 기존 로컬 차이는 먼저 보존·대조하여 원본에 병합합니다. 갱신은 전체 폴더·사용자 차이·해시를 보존한 뒤 지정 대상만 교체합니다. 업데이트별 before/after·설정·검증·복구는 해당 작업 기록 공간에 묶고, 원형 개인 설정·raw의 실제 Git 제외를 확인합니다.
- repo 지정 검사기·버전·설정을 우선하고 변경 위험에 맞춰 검사합니다. 필수 도구 부재·읽기 실패·대상 0개·미실행은 통과가 아닙니다. 파일 링크·앵커·외부 도달성을 구분하고 마지막 성공으로 앞선 실패를 덮지 않습니다.
- 반복 실패에는 새 근거와 다른 접근을 사용하고 승인 범위를 확대하지 않습니다. 검토한 담당 파일만 staging하며 승인된 branch의 일반 push 후 원격 commit을 확인합니다. 설치·발견·선택·행동·게시·운영 적용을 각각 관찰한 범위로 보고합니다.

## 3. 필요한 자료로 직접 이동

- 복잡한 보고·역할 분담: [운영 상세](../operating-details.md).
- 개인 skill·설정 갱신 또는 복구: [보존·교체 절차](../skill-maintenance.md).
- 검사기 호출·검증 실패·재개 판단: [검증·복구 상세](../validation-and-recovery.md).
- Windows 인코딩·Python config/status: [runtime 상세](../windows/runtime-and-encoding.md).
- SSH 원격 실행·ACL: [SSH 상세](../windows/ssh-and-acl.md).
- 파일/작업 잠금: [잠금 상세](../windows/file-lock.md).
- repo 기록 체계의 출처·충돌 확인: [저장소 지침 연결](../repository-workflow.md). 단순 재개는 대상 repo의 현재 작업 항목과 관련 근거로 바로 이동합니다.
- 문서 표현 양식이 필요한 경우: [STYLE](../STYLE.md). 문서 역할·파일명·푸터·배지·날짜는 대상의 적용 기준을 확인합니다.
- 큰 작업 분해·commit: 실제 선택한 planning-and-breakdown·git-commit-rule을 사용합니다. 분해 skill이 미설치라면 [동봉 planning 지침](../skills/planning-and-breakdown.md)을 참고하며 설치·발견으로 보고하지 않습니다. 사용자/repo가 지정한 출처를 우선하고 설치본과 동봉본을 중복 로드하지 않습니다.
- 점진적 변경·IaC가 실제 필요한 경우: [incremental-change](../skills/incremental-change.md), [spec-driven-infra](../skills/spec-driven-infra.md) 중 해당 자료만 선택합니다.
- 원문 비교가 요청된 경우: [보존 본문](../linux-skills/work-rules.md), [Kiro 원문](../originals/work-rules.md), [Linux 원문](../linux-skills/work-rules.md). 과거 고정 경로·branch·승인은 실행 기준으로 복원하지 않습니다.

## 4. 추가 읽기와 중단

참조는 해당 조건에 필요한 지침이며 링크가 있다는 이유로 연쇄 전체 읽기를 하지 않습니다. 선택한 지침이 실제 작업에 요구하는 필수 참조는 확인합니다. INDEX는 경로를 모를 때 관련 항목만 사용합니다. 이미 읽은 내용이 현재 문맥에 있고 변경 정황이 없으면 재사용하며 문서 변경·문맥 누락·repo 전환·충돌이 있을 때 필요한 지침을 다시 확인합니다. 범위·절차·검증 근거가 충분하면 추가 읽기를 끝내고 작업합니다. 필수 지침의 접근 실패를 규칙 부재로 처리하지 않습니다.

이 폴더는 필수 참조·도구를 동봉합니다. 31·다른 repo·catalog·installer·형제 skill 설치를 기본 실행의 선행 조건으로 만들지 않습니다. 개인 runtime은 중앙 정책의 별도 상위 원본이 아닙니다.
<!-- CODEX-COMPAT-END -->
