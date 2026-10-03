# 35 AI 작업 탐색 색인

35의 구조·skill 구현·작업 기록을 찾을 때 사용하는 탐색 문서입니다. 상태 원본은 해당 TODO, 실행 기준은 적용 AGENTS와 선택한 SKILL입니다. 이 INDEX 자체는 Codex 자동 발견 문서나 설치 목록이 아닙니다.

## 1. 주요 경로

```text
35_agent-skill/
├── AGENTS.md                         # 저장소 지침·보존·게시 순서
├── codex_windows.md                  # 구조 설명·장단점·설계 보완
├── codex_windows/                    # Windows 복사·사용 구성
│   ├── personal/AGENTS.md            # 선택적 공통 지침 작성 원본
│   └── skills/<이름>/SKILL.md        # 독립 개인 skill 19개
├── codex_linux/                      # Linux 보존 구성
├── kiro/                             # Kiro 보존 원본
├── gpt/                              # GPT 보존 원본
├── 105_backup/                       # 과거 개발본: 현재 설치 입력 아님
└── agent-workflows/                  # 개발·적용·검토 기록
    ├── README.md                     # 관리 개요·사용 안내
    ├── INDEX.md                      # 이 탐색 문서
    └── codex/
        ├── HANDOFF.md                # 세션 재개 시 필요한 인계
        └── windows/
            ├── README.md            # Windows 검토·근거 연결
            ├── PLAN.md              # 큰 목표와 완료 조건
            ├── TODO.md              # Windows 작업 상태 원본
            ├── ISSUE.md             # 재발 방지·재개 조건
            └── verification/        # 검사 도구·정적 inventory·과거 증거
```

전체 파일과 보호 원문을 매번 읽지 않습니다. 보존 경로의 과거 지침은 현재 실행 지시로 적용하지 않습니다. 주요 관리 경로가 바뀌면 이 tree와 연결을 갱신하고 다른 README에 같은 현황표를 복제하지 않습니다.

## 2. 작업별 다음 문서

| 작업                  | 먼저 읽을 기준                                                                                                    | 조건                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| 현재 repo 규칙·게시   | [AGENTS](../AGENTS.md)                                                                                            | 해당 저장소 작업; 기존 승인·사용자 편집 확인                     |
| Windows 복사·사용     | [Windows README](../codex_windows/README.md)                                                                      | 실제 설치/적용 요청 범위가 있을 때                               |
| 개인 공통 규칙 작성   | [personal AGENTS](../codex_windows/personal/AGENTS.md), [work-rules](../codex_windows/skills/work-rules/SKILL.md) | 선택적 작성 원본과 실제 홈을 구분                                |
| 필요한 역할 선택      | [using-skills](../codex_windows/skills/using-skills/SKILL.md)                                                     | 역할 기준 원본; 개별 본문은 선택한 것만                          |
| repo 문서·결과물 구조 | [Workflow 참조](../codex_windows/skills/work-rules/references/repository-workflow.md)                             | INDEX/TODO/TASK·경로 예외·이력 설계                              |
| Windows 변경·재개     | [Windows TODO](codex/windows/TODO.md), [PLAN](codex/windows/PLAN.md)                                              | 관련 항목과 실제 Git·파일 상태를 대조                            |
| 반복 문제·제약        | [Windows ISSUE](codex/windows/ISSUE.md)                                                                           | 해당 문제와 필요한 재개 조건만                                   |
| 공식 system 기준·검증 | [공식 skill 재검토](codex/windows/SYSTEM_SKILL_REVIEW_2026-10-03.md)                                              | 고정 source·설치/발견/정적/행동 범위를 구분                      |
| 세션 인계             | [HANDOFF](codex/HANDOFF.md)                                                                                       | 재개 요청에 필요한 범위; 과거 승인을 새 권한으로 재사용하지 않음 |
| Linux 비교            | [Linux README](../codex_linux/README.md)                                                                          | 지정한 Linux 작업·원문 대조에 한정                               |

## 3. INDEX가 관리하지 않는 것

진행 상태·담당·다음 행동을 이 문서에 다시 적지 않습니다. skill 전체 본문·외부 공개 catalog를 통합하지 않습니다. 같은 이름의 plugin skill은 plugin과 실제 파일 경로를 함께 식별하고 tool이 지원하지 않는 호출 문법을 만들지 않습니다.

산출물·검증 원본은 해당 TASK·검토 문서에서 연결합니다. tool state·sealed bundle·제품 자산·개인 runtime 자료를 이 INDEX 위치로 옮기지 않습니다. 실제 개인 경로·계정·비공개 증거는 공개 색인에 복사하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
