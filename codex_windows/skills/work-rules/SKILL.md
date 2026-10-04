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
- 실제 대상에 적용된 운영·기록·검증·게시 규칙을 따릅니다. 31의 template/profile은 작성·배포 원본이며, 다른 repo의 profile이나 미배포 중앙 변경을 자동 적용하지 않습니다. 개인 skill에서 문서 역할·기록 위치·푸터를 재정의하지 않습니다. 게시 대상은 개인 공통 AGENTS의 현행 기본 브랜치·상시 게시 승인과 현재 사용자 지시를 확인해 아래 완료 절차를 적용합니다.
- 기존 기록·사용자 편집·비공개 증거를 보존하고 단순 작업에 빈 문서·폴더를 일괄 생성하지 않습니다. 고정 제품·도구·skill·sealed 자료·runtime 경로는 실제 계약을 유지합니다.

## 2. 실행과 검증

- Computer Use로 사용자와 같은 화면·입력을 제어하기 전 대상·예정 작업·대기 시간을 안내하고 5~10초 기다립니다. 안내 후 응답이 없으면 이미 승인된 범위에서 진행하며 매번 시작 확인을 요구하지 않습니다. 대기 중 중단·연기·수정 요청이 오면 이를 먼저 반영합니다. 무응답은 새 작업이나 필수 확인·승인이 필요한 행동의 승인으로 해석하지 않습니다. 작업 구간이 끝나면 사용자에게 제어 종료를 알리고 도구가 지원하는 세션 해제·초기화로 제어를 종료합니다. 다시 필요할 때 새 안내·대기 후 재개하고, 사용자가 진행 중 다시 입력하거나 제어 충돌이 확인되면 조작을 멈춰 상태를 확인합니다. 대상 업무 앱은 해당 작업에서 종료가 승인된 경우에만 닫습니다.

- Windows 파일 작업은 확인한 절대 경로와 PowerShell `-LiteralPath`를 사용하고 shell을 섞어 삭제·이동하지 않습니다. Linux/WSL/원격은 별도 실제 환경으로 확인합니다. config 기본값·현재 세션 정책·추가 승인·OS ACL을 구분합니다.
- 명확한 지정 자료·규칙의 간단한 수집·정형 추출은 Luna 6.0의 실제 지원 최저 reasoning effort로 배정합니다. 현재 위임 도구에서는 `gpt-6-luna / low`를 사용하며 미지원 `minimal`을 지정하지 않습니다. 검색·비교·선별·출처 확인은 Sol 6.1 medium, 복수 조건 이미지 판정·여러 repo 계획과 의존성 분석은 Sol 6.1 high, 중요한 최종 설계 판단은 Astra를 운영 기준으로 유지합니다. 실제 도구의 모델·effort 지원과 선택을 확인하며 main/config는 자동 변경하지 않습니다. 짧은 조회는 직접 수행하고 관련 추출은 묶어서 위임하며 근거·개수·예외만 간결하게 반환합니다. 같은 입력의 조사·통과 검사는 재사용합니다. 실제 분담에는 [운영 상세](references/operating-details.md)의 반환 근거·오류 처리 기준을 적용합니다.
- 사용자의 단일 창구인 orchestration root가 필요한 역할만 배정하고 최종 배정·검증·공통 파일 통합을 담당합니다. 큰 계획은 planner 초안과 root 통합을 분리하며 소유 영역의 기능 상태·원본은 소유 담당이 유지합니다. 업무 역할로 새 권한·직책별 필수 승인·자동 채팅/메시지·Goal·상시 감시를 추가하지 않습니다.
- 개인 skill 수정은 35_agent-skill의 관리 원본에서 진행하고 검증한 뒤 로컬 설치본에 반영합니다. 로컬만 단독 수정하지 않으며 기존 로컬 차이는 먼저 보존·대조하여 원본에 병합합니다. 갱신은 전체 폴더·사용자 차이·해시를 보존한 뒤 지정 대상만 교체합니다. 업데이트별 before/after·설정·검증·복구는 해당 작업 기록 공간에 묶고, 원형 개인 설정·raw의 실제 Git 제외를 확인합니다.
- repo 지정 검사기·버전·설정을 우선하고 변경 위험에 맞춰 관련 범위만 검사합니다. 일반 변경은 기존 기록의 짧은 결과로 마감하며 전체 조사·중복 검증표·새 결과 폴더를 상시 요구하지 않습니다. 새 변경·실패·미결 근거가 없으면 통과 검사를 반복하지 않습니다. 필수 도구 부재·읽기 실패·대상 0개·미실행은 통과가 아닙니다. 파일 링크·앵커·외부 도달성을 구분하고 마지막 성공으로 앞선 실패를 덮지 않습니다.
- 반복 실패에는 새 근거와 다른 접근을 사용하고 승인 범위를 확대하지 않습니다. 일반 개인 개발의 기본 작업·게시 브랜치는 `main`입니다. 필요한 검증·기록 후 검토한 담당 파일만 commit·일반 push하고 원격 SHA·commit 링크를 보고합니다. 이 완료 절차의 승인은 계속 적용하며 반복 사용자 확인을 요구하지 않습니다. 병렬 작업·격리·장기 실험에는 필요한 agent/task 브랜치·worktree를 사용하고 QA·Migration·복구 목적 브랜치와 upstream 읽기 전용 경계를 유지합니다. 작업 브랜치의 검증한 변경은 지정한 통합 대상에 반영하며 기존 브랜치를 자동 삭제하지 않습니다. 현재 사용자 제한과 원격 보호 규칙의 필수 PR·검사를 준수하며 우회하지 않습니다. 읽기 전용·변경 0건은 commit·push하지 않고 검증 실패·비밀값·다른 작업 변경은 게시하지 않습니다. force push·release·운영 적용은 별도 범위이며 게시 실패는 원인과 미게시 상태를 보고합니다. branch 전환 전 기존 변경·미병합 commit·refs를 확인하고 보존하며 다른 checkout의 branch를 강제로 전환하지 않습니다. 설치·발견·선택·행동·게시·운영 적용을 각각 관찰한 범위로 보고합니다.

## 3. 필요한 자료로 직접 이동

- 복잡한 보고·역할 분담: [운영 상세](references/operating-details.md).
- 개인 skill·설정 갱신 또는 복구: [보존·교체 절차](references/skill-maintenance.md).
- 검사기 호출·검증 실패·재개 판단: [검증·복구 상세](references/validation-and-recovery.md).
- Windows 인코딩·Python config/status: [runtime 상세](references/windows/runtime-and-encoding.md).
- SSH 원격 실행·ACL: [SSH 상세](references/windows/ssh-and-acl.md).
- 파일/작업 잠금: [잠금 상세](references/windows/file-lock.md).
- repo 기록 체계의 출처·충돌 확인: [저장소 지침 연결](references/repository-workflow.md). 단순 재개는 대상 repo의 현재 작업 항목과 관련 근거로 바로 이동합니다.
- 문서 표현 양식이 필요한 경우: [STYLE](references/STYLE.md). 문서 역할·파일명·푸터·배지·날짜는 대상의 적용 기준을 확인합니다.
- PLAN·TODO 생성·재작성과 큰 작업 분해: 실제 선택한 planning-and-breakdown의 실행 가능한 계획·연속 실행 기준을 적용합니다. 계획 작성만으로 Goal 생성·구현·게시를 시작하지 않으며 목표 실행 요청과 기존 승인을 구분합니다. 단순 질문·짧은 작업은 필요한 기준만 적용합니다. commit은 실제 선택한 git-commit-rule을 사용합니다. 분해 skill이 미설치라면 [동봉 planning 지침](references/skills/planning-and-breakdown.md)을 참고하며 설치·발견으로 보고하지 않습니다. 사용자/repo가 지정한 출처를 우선하고 설치본과 동봉본을 중복 로드하지 않습니다.
- 목표 실행·재개가 요청되면 실제 제공된 goal-continuation을 선택해 사전 대조와 기존 Goal 확인 후 준비된 승인 작업을 이어갑니다. 미제공이면 현재 작업 지시와 위 기본 규칙을 따르며 자동 설치하거나 Goal 생성 승인을 추론하지 않습니다.
- 점진적 변경·IaC가 실제 필요한 경우: [incremental-change](references/skills/incremental-change.md), [spec-driven-infra](references/skills/spec-driven-infra.md) 중 해당 자료만 선택합니다.
- 원문 비교가 요청된 경우: [보존 본문](references/legacy-work-rules.md), [Kiro 원문](references/kiro-original.md), [Linux 원문](references/linux-original.md). 과거 고정 경로·branch·승인은 실행 기준으로 복원하지 않습니다.

## 4. 추가 읽기와 중단

참조는 해당 조건에 필요한 지침이며 링크가 있다는 이유로 연쇄 전체 읽기를 하지 않습니다. 선택한 지침이 실제 작업에 요구하는 필수 참조는 확인합니다. INDEX는 경로를 모를 때 관련 항목만 사용합니다. 이미 읽은 내용이 현재 문맥에 있고 변경 정황이 없으면 재사용하며 문서 변경·문맥 누락·repo 전환·충돌이 있을 때 필요한 지침을 다시 확인합니다. 범위·절차·검증 근거가 충분하면 추가 읽기를 끝내고 작업합니다. 필수 지침의 접근 실패를 규칙 부재로 처리하지 않습니다.

이 폴더는 필수 참조·도구를 동봉합니다. 31·다른 repo·catalog·installer·형제 skill 설치를 기본 실행의 선행 조건으로 만들지 않습니다. 개인 runtime은 중앙 정책의 별도 상위 원본이 아닙니다.
<!-- CODEX-COMPAT-END -->
