# Codex Windows 구조와 Workflow 보완안

Windows 개인 배포 원본과 조건별 읽기 구조입니다. 2026-10-04부터 저장소 문서 역할·결과물 배치·양식·게시 정책은 31에서 관리하고 대상에 실제 적용한 지침을 따릅니다. 개인 skill은 공통 실행 방법과 필요한 참조를 제공합니다.

## 1. 현재 구조

```text
codex_windows/
├── AGENTS.md                  개인 공통 지침의 배포 원본
├── README.md                  복사·사용 안내
├── personal/                  설정 예시·적용 안내·Linux 비교 원문
└── skills/                    20개 폴더 단위 자산
    └── work-rules/
        ├── SKILL.md           핵심 규칙과 직접 참조 조건
        ├── references/
        │   ├── operating-details.md
        │   ├── skill-maintenance.md
        │   ├── validation-and-recovery.md
        │   ├── windows/
        │   │   ├── runtime-and-encoding.md
        │   │   ├── ssh-and-acl.md
        │   │   └── file-lock.md
        │   ├── repository-workflow.md
        │   ├── windows-work-rules-details.md
        │   ├── STYLE.md
        │   ├── skills/        필요할 때 선택할 동봉 지침
        │   ├── originals/     비교용 원문
        │   ├── linux-skills/  Linux 비교 자료
        │   └── linux-tools/   보존 도구
        └── scripts/           실제 Windows helper
```

SKILL의 참조표가 work-rules 내부의 읽기 조건을 안내합니다. 별도 INDEX·PLAN·TODO·REVIEW·설치 inventory를 복사용 폴더 안에 추가하지 않습니다. 개발·검증·업데이트 기록은 [agent-workflows INDEX](agent-workflows/INDEX.md)에서 연결합니다.

최초 이관 19개에 [fact-check](codex_windows/skills/fact-check/SKILL.md)를 추가했습니다. `PLAN TODO $fact-check`는 각 문서의 사실 주장을 검증하며 전체 작업 상태 감사로 확대하지 않습니다.

## 2. Codex가 인식하는 Markdown

개인 공통 지침의 배포 원본은 [AGENTS](codex_windows/AGENTS.md), skill 본문은 [work-rules](codex_windows/skills/work-rules/SKILL.md)입니다. 실제 Codex home의 AGENTS와 skill 발견 위치는 다르므로 [복사 안내](codex_windows/README.md)를 따릅니다. INDEX·TODO 등은 지정 지침이 연결한 경우 읽는 관리 문서이며 이름만으로 자동 실행되지 않습니다.

[공식 skill 안내](https://learn.chatgpt.com/docs/build-skills)의 발견·선택·참조 읽기와 실제 관찰을 구분합니다. 본문 분리는 필요 자료만 읽는 조건을 제공하며 매 요청의 자동 선택을 보장하는 hook은 아닙니다.

## 3. 공통 규칙과 repo 기록의 연결 보완안

개인 AGENTS는 짧은 공통 원칙과 work-rules 선택을 안내합니다. work-rules는 범위·보고·실행·검증과 조건별 상세를 관리합니다. 대상 repo의 적용 AGENTS·운영 기준이 문서 위치·양식·검사·게시를 정합니다.

중앙 작성 원본은 [31 Codex 양식](https://github.com/siasia86/31_governances/tree/yunli/codex/template), 배포 원본은 [31 profile](https://github.com/siasia86/31_governances/tree/yunli/codex/profile)입니다. 일반 실행 때마다 중앙 자료를 내려받지 않으며 실제 배포 상태와 중앙 원본을 구분합니다. 35의 실제 작업 기록은 기존 agent-workflows를 유지합니다.

## 4. 작업 문서의 역할

README·INDEX·PLAN·TODO·TASK·ISSUE·CHANGELOG의 역할표와 결과물 tree를 이 문서나 개인 skill에서 별도로 갱신하지 않습니다. 대상 repo의 적용 지침을 기준으로 하고 중앙 개정이 필요한 경우 [31 template 안내](https://github.com/siasia86/31_governances/tree/yunli/codex/template)를 확인합니다. 이전 상세와 이번 분리 대응은 [T-WIN-004](agent-workflows/codex/2026-10-04-personal-routing-T-WIN-004/README.md)에 기록합니다.

## 5. 조회·위임·완료 처리

```text
현재 요청·적용 지침
└── work-rules 핵심 본문
    ├── 기존 작업 재개 → 해당 repo의 현재 작업과 관련 근거
    ├── 보고·분담 → operating-details
    ├── 개인 skill 갱신 → skill-maintenance
    ├── 검사·실패 대응 → validation-and-recovery
    ├── Windows 특수 처리 → windows의 해당 상세
    └── 과거 비교 → 필요한 보존 원문
```

INDEX는 경로를 모를 때 관련 항목만 사용합니다. 같은 내용이 현재 문맥에 있고 변경 정황이 없으면 반복 읽기를 피하며, 변경·문맥 누락·대상 전환·충돌이 있을 때 재확인합니다. 필수 참조가 없거나 읽기에 실패하면 누락을 숨기지 않습니다.

## 6. 장점과 단점

- 장점: repo별 정책 원본과 개인 실행 지침의 중복을 줄이고 기본 읽기에서 드문 Windows 상세를 분리합니다.
- 비용: 동봉 사본과 링크를 함께 갱신해야 하므로 독립 폴더 복사·내부 참조·원문 해시를 확인합니다.
- 한계: 문자 수 감소는 실제 토큰·비용 절감률이나 새 세션의 자동 선택 성공을 증명하지 않습니다.

## 7. 설계 검토와 적용 범위

기존 사용자 설정·system·plugin·모델·인증은 지정 범위 밖에서 바꾸지 않습니다. 역사 자료·이관 당시 manifest·검사 결과는 당시 증거로 유지합니다. 최신 구현·설치·검증·미실행은 [T-WIN-004](agent-workflows/codex/2026-10-04-personal-routing-T-WIN-004/README.md)에서 확인합니다.

35의 게시 순서는 [저장소 AGENTS](AGENTS.md)의 yunli 게시 → 사용자 검증 → main 반영입니다. 사용자 검증 전 main을 갱신하지 않습니다.

## 8. 공식 skill 기준의 후속 보완

[기존 공식 skill 검토](agent-workflows/codex/windows/SYSTEM_SKILL_REVIEW_2026-10-03.md)는 당시 근거입니다. 이번 재구성은 조건별 참조·폴더 독립 사용·실제 repo 지침 연결을 유지합니다. 새로운 scheduler·무인 반복·중앙 자동 동기화는 도입하지 않습니다.

## 9. 개인 Codex 업데이트별 백업

```text
agent-workflows/codex/<날짜>-<목적>-<작업ID>/
├── README.md                  대상·변경·검증·복구 안내
├── before/inventory.json      변경 전 파일 해시
├── after/inventory.json       변경 후 파일 해시
├── verification.json          공개 가능한 검증 결과
└── private/                   Git 제외: 전후 사본·설정·raw
```

다음 업데이트는 새 폴더에 기록하며 이전 사본·해시를 덮어쓰지 않습니다. 원형 백업은 발견 경로 밖에서 보존하고 Git 제외를 실제 확인합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
