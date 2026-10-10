# Codex Windows 구조와 읽기 흐름

개인 배포 원본은 [codex_windows](codex_windows/README.md), 구현·검증 원본은 35, 대상 저장소의 문서 정책은 실제 적용된 지침입니다. 현재 배포본은 PowerShell·Windows Python·Git 기준의 skill 21개입니다.

## 1. 배포 구조

```text
codex_windows/
├── AGENTS.md                  선택적 개인 공통 지침 원본
├── README.md                  폴더 복사·갱신 안내
├── personal/                  Windows 설정 예시·적용 안내
└── skills/                    Windows native 21개
    └── <skill>/
        ├── SKILL.md           핵심 지침·참조를 읽을 조건
        ├── agents/openai.yaml UI 메타데이터·기존 호출 정책
        ├── references/        실제 필요한 Windows 상세
        └── scripts/           실제 필요한 동봉 도구
```

모든 skill에 상세 폴더를 강제하지 않습니다. references와 scripts는 해당 기능에 필요한 경우에만 두며 폴더 전체가 단독 복사 단위입니다.

## 2. 읽기 흐름

```text
현재 요청·실제 적용 AGENTS
└── 필요한 skill 선택
    ├── 지속 작업 → work-rules
    │   ├── 보고·모델 분담 → operating-details
    │   ├── 개인 skill 갱신 → skill-maintenance
    │   ├── 검사·실패 대응 → validation-and-recovery
    │   └── Windows 특수 처리 → 필요한 windows 상세
    ├── 별도 상황보고 → status-report
    ├── 계획 작성 → planning-and-breakdown
    ├── 승인 목표 이어가기 → goal-continuation
    └── 선택이 불명확 → using-skills의 필요한 역할
```

INDEX는 실제 작업 공간에서 경로를 탐색할 때 사용합니다. 개인 skill 폴더에 별도 PLAN·TODO·INDEX·검증 결과를 강제로 만들지 않습니다. 필요한 참조만 읽고 유효한 기존 문맥은 재사용합니다.

## 3. 원본·보존·설치

- 현재 실행본: [Windows skill 목록](codex_windows/skills/README.md).
- Linux 원본: [codex_linux](codex_linux/README.md); 기존 원문 bytes 유지.
- 이번 이동·보존·검증: [Windows native 갱신 기록](agent-workflows/codex/2026-10-10-windows-native-T-WIN-004/README.md).
- 작업 공간 탐색: [agent-workflows INDEX](agent-workflows/INDEX.md).

과거 원문·비교 자료·개발 검사기는 Windows 복사 영역 밖에 둡니다. 누락된 Bash 도구는 Linux 보존 공간에 원형을 추가했으며 실제 Linux 실행 완료로 처리하지 않습니다.

갱신은 35 관리 원본 수정·검증 → 현재 설치된 관리 대상 반영 → Git 통합 담당의 main 일반 게시 순서입니다. 사용자 추가 파일과 기존 설정을 보존하며 31 정책의 자동 CI/CD 적용을 가정하지 않습니다.

## 4. 장점과 한계

- 장점: 실행 지침과 역사 자료를 분리하여 불필요한 읽기와 잘못된 플랫폼 명령 선택을 줄입니다.
- 장점: Windows 도구와 필수 참조를 동봉하여 skill 폴더 단위 복사가 가능합니다.
- 비용: 동봉 참조·도구·UI·현재 inventory를 함께 검증해야 합니다.
- 한계: 본문 분리·파일 일치는 자동 선택·장기 행동·실제 토큰 절감률의 검증 근거가 아닙니다.
- 한계: Windows에서 실행할 수 없는 기능은 해당 플랫폼의 별도 지침과 검증이 필요합니다.

설정·권한·system/plugin skill·31 정책 변경은 이번 정리와 별도 범위입니다. 완료 여부는 최신 갱신 기록의 실제 검사·설치·게시 근거를 따릅니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-10

© 2026 siasia86. Licensed under CC BY 4.0.
