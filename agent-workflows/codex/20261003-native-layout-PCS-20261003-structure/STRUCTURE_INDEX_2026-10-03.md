# Codex 개인 설정 관리 색인

> 2026-10-03의 구조 예시·관찰을 보존한 색인입니다. 아래 tree는 당시 배치이며 현행 경로는 [SMA 이관 tree](../windows/records/2026-10-04-record-relocation-SMA-20261004-01/README.md#2-현재-자료-배치)에서 확인합니다.

현재 로컬 홈과 같은 `.codex`·`.agents` 형식으로 설정과 skill을 관리합니다. 실제 홈 파일은 원위치에서 사용하고, 업데이트 기록은 날짜·목적·작업 ID가 다른 폴더로 보존합니다.

```text
사용자 홈/
├── .codex/
│   ├── AGENTS.md                # 개인 공통 지침
│   └── config.toml              # 개인 설정
└── .agents/skills/<이름>/       # SKILL.md와 동반 파일 전체

agent-workflows/codex/
├── INDEX.md
├── Snapshot-PersonalConfig.ps1
├── pc01_codex-app-home/         # 기존 공개 관찰 사본·당시 inventory
└── <날짜-목적-작업ID>/
    ├── README.md               # 범위·출처·검증·복구
    ├── .gitignore              # private/ 제외
    └── private/
        ├── before/             # .codex/·.agents/·manifest.json
        └── after/              # .codex/·.agents/·manifest.json
```

- 구조·백업 방법과 이번 검증: [PCS-20261003-structure](README.md).
- 실제 작업 상태의 원본: [Windows TODO](../windows/TODO.md). 이 색인은 상태를 별도로 관리하지 않습니다.
- 기존 공개 관찰 사본의 출처·확인 시점: [기존 개인 적용 안내](../README.md). 새 백업을 기존 mirror에 덮어쓰지 않습니다.
- 개인 설정 백업: [Snapshot-PersonalConfig.ps1](../windows/verification/Snapshot-PersonalConfig.ps1). 선택한 skill 폴더 전체와 개인 지침·설정 두 파일을 복사하며 source는 변경하지 않습니다.

구조 변경·업데이트·복구 작업일 때 이 색인을 읽습니다. 일반 게임 개발에는 필요한 저장소 지침과 선택 skill을 사용합니다. INDEX를 Codex의 자동 발견 파일로 등록하거나 개인 홈에서 필수 조회하도록 설정하지 않았습니다. `.agents/skills`를 담은 사본 하위에서 작업을 시작하면 저장소 skill로 발견될 수 있으므로 검토는 35 루트에서 진행합니다.

개인 설정 원문과 백업은 `private/`에 두고 실제 Git 제외를 검사합니다. 공개 문서에는 사용자 홈의 절대 경로·계정·전체 config·credential·세션을 옮기지 않습니다. 인증 자료·runtime 로그·system/plugin skill은 이번 백업 대상에 포함하지 않습니다.

글로벌 지침과 사용자 skill 위치는 [공식 AGENTS 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [공식 skill 안내](https://learn.chatgpt.com/docs/build-skills)와 대조했습니다. 설정 파일 경로와 우선순위는 [공식 config 안내](https://learn.chatgpt.com/docs/config-file/config-basic)를 따릅니다. 파일 사본 생성과 새 세션의 발견·선택·실제 행동 검증은 구분합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
