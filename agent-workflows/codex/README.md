# Codex 개인 적용본과 skill 확인

현재 원본은 [Linux 보존본](../../codex_linux/README.md)과 [Windows 전체 이관본](../../codex_windows/README.md)으로 구분합니다. 복사용 Windows 본문은 구현 폴더에 두고 개발 계획·검토·검증은 [Windows 작업 기록](windows/README.md)에서 관리합니다. 이전 이관 범위·검사는 [Windows 이관 기록](WINDOWS_MIGRATION_2026-10-03.md)을 따릅니다. [플랫폼 분리 기록](PLATFORM_SPLIT_2026-10-03.md)을 확인하며 아래 개인 설치 관찰 사본·inventory·당시 검증은 자동 갱신하지 않습니다.

현재 개인 7개·90파일의 기계 현황 원본은 [이번 after/inventory.json](2026-10-03-personal-skills-T-WIN-003/after/inventory.json)이며 `work-rules`와 신규 두 skill을 포함합니다. 기존 `pc01_codex-app-home/runtime_inventory.json`과 네 사본은 과거 관찰로 보존합니다.

1~4절과 기존 사본·JSON은 **2026-09-30의 역사적 관찰**입니다. 새 1.0.0 개인 스킬의 설치·발견·행동 결과가 아니며 자동 동기화하지 않습니다. 5절은 2026-10-02 당시 후속 기록 설계이며 새로운 설치 결과가 아닙니다. 현재 사용자 지정 업데이트별 백업 방식과 이번 관찰은 6절에서 연결합니다.

## 1. 원본과 개인 적용 사본

사용자가 선택한 환경 이름은 `pc01_codex-app-home`입니다. 실제 hostname·IP·계정명이 아닌 공개용 별칭이며 이전 `codex-windows-personal`과 같은 사용자 범위 환경입니다. 이름의 app은 현재 작업 도구를 나타내며 같은 사용자 홈을 사용하는 CLI의 skill 파일을 별도 설치로 복제하지 않습니다.

당시 구현 원본의 현재 보존 위치는 [codex/payload/skills](../../105_backup/codex/payload/skills/)입니다. 이곳에는 실제 개인 설치 파일과 일치하는 공개 가능 skill 사본을 보관합니다. 기존 구현은 codex_linux/skills에서 보존하고 Windows 전체 이관본은 codex_windows/에서 관리하며, 실제 설치·변경·제거 이후 관찰 갱신은 별도 확인 후 진행하며 사본을 독립 편집하거나 설치 입력으로 사용하지 않습니다.

`pc01_codex-app-home/`는 사용자 홈에 대응하고 그 아래 `.agents/skills/<이름>/`은 실제 설치 상대 경로와 같습니다. skill의 scripts·references·assets가 있으면 폴더 전체를 보존합니다. 숨김 폴더도 검사 대상입니다. 이 사본 아래를 Codex 실행 작업 디렉터리로 열면 저장소 범위 skill로 발견될 수 있으므로 검토는 35 루트에서 수행합니다.

## 2. 2026-09-30 적용 관찰 파일

| skill                  | 개인 설치 사본                                                                 | 설치·파일 일치 | 발견                | 대표 행동 |
|------------------------|--------------------------------------------------------------------------------|----------------|---------------------|-----------|
| code-review            | [SKILL.md](pc01_codex-app-home/.agents/skills/code-review/SKILL.md)            | 확인           | 당시 세션 목록 확인 | 미검증    |
| debugging-and-recovery | [SKILL.md](pc01_codex-app-home/.agents/skills/debugging-and-recovery/SKILL.md) | 확인           | 당시 세션 목록 확인 | 미검증    |
| markdown-review        | [SKILL.md](pc01_codex-app-home/.agents/skills/markdown-review/SKILL.md)        | 확인           | 당시 세션 목록 확인 | 미검증    |
| md-link-check          | [SKILL.md](pc01_codex-app-home/.agents/skills/md-link-check/SKILL.md)          | 확인           | 당시 세션 목록 확인 | 미검증    |

상태·경로·전체 파일 해시의 기계 원본은 [runtime_inventory.json](pc01_codex-app-home/runtime_inventory.json), 실행한 검사와 미실행 범위는 [VERIFICATION.md](VERIFICATION.md)입니다. skill의 본문은 위 사본에서 읽고 JSON에 복제하지 않습니다. 관찰 시점은 2026-09-30, 구현 기준 commit은 `4a5dfb17ccbd0dcb5d6da787e3c5133761c06261`입니다.

## 3. 갱신과 공개 범위

관찰 범위는 사용자가 선택한 네 standalone skill입니다. 내장·plugin skill 전체나 다른 계정·기기·cloud·일시적인 subagent 상태를 전수 조사한 결과가 아닙니다. 실제 개인 AGENTS·config·키·세션·로그·로컬 receipt·운영 자료는 복제하지 않습니다. 개인 AGENTS의 설치 여부와 비공개 상태만 metadata에 남깁니다.

새 개인 skill 생성·설치·수정·제거 시 공개 가능한 본문과 출처·현재 파일 목록·해시·확인일·설치/발견/행동 상태를 함께 갱신합니다. 원본과 다른 현장 변경은 차이로 기록하고 임의 덮어쓰지 않습니다. 자동 수집·동기화·drift 알림은 미구현이므로 마지막 관찰 이후 상태는 별도 확인이 필요합니다.

31은 저장소별 지침·skill 선택과 배치 후보를 관리하고 이 개인 관찰 원본으로 연결합니다. 이곳의 사본 게시로 하위 게임 저장소 설정이 적용되지는 않습니다. 기존 [Windows 현황 경로](../../105_backup/codex/windows_game_governance/README.md)는 연결 안내로 유지합니다.

## 4. 기준 문서

- [세션 인계](HANDOFF.md): 다음 세션의 읽기 순서·현재 Git 상태·미완료 추가 검토와 저장소에 보존한 근거.
- [공통 최초 적용·업데이트](../README.md): 실행 범위·백업·검증·복구 절차.
- [현재 저장소 안내](../../README.md#3-개인-스킬의-사용-단위): 신규 개인 스킬의 폴더 복사 기준.
- [현재 Codex 모음](../../codex_linux/README.md): 스킬 19개·선택적 개인 지침·수동 복사. 위 2026-09-30 개인 사본과는 설치/관찰 시점을 구분합니다.
- [1.0.0 재작성 기록](REBUILD_1.0.0.md): 구현·검증·게시와 실제 설치의 구분.
- [공식 skill 경로](https://learn.chatgpt.com/docs/build-skills): 사용자 범위와 저장소 범위 발견 경로.

## 5. 환경과 작업공간별 후속 기록

[공통 기록 기준](../README.md#41-환경과-작업공간별-기록)에 따라 환경·사용자별 공개 별칭, Codex 클라이언트·버전, 설치 범위(`USER`/`REPO`), 작업공간별 별칭을 기록합니다. Agent·Skill·Prompt의 재사용 구현 원본은 플랫폼별 `codex_linux/`·`codex_windows/`에서 관리하며 이곳에는 실제 확인한 설치·적용·검증 결과를 남깁니다.

개인 홈의 공통 스킬은 설치 파일·출처 commit·version·전체 파일 해시·확인일을 한 번 기록합니다. 각 작업공간은 이 설치 기록을 참조하고 적용 지침·추가 스킬·31 설정 적용 여부와 발견·대표 행동 결과를 따로 남깁니다. 저장소에 직접 설치한 스킬은 그 작업공간의 별도 설치 목록과 사본으로 관리합니다.

다음은 향후 기록 구조의 예시입니다. 실제 환경을 확인한 뒤 필요한 폴더만 작성하며 기존 `pc01_codex-app-home` 사본·JSON·해시는 당시 상태로 보존합니다.

```text
agent-workflows/codex/<environment-alias>/
├── README.md
├── runtime_inventory.json
├── .agents/skills/
└── workspaces/
    ├── repository1/
    │   ├── README.md
    │   ├── runtime_inventory.json
    │   └── .agents/skills/
    └── qa-repostory2/
        ├── README.md
        ├── runtime_inventory.json
        └── .agents/skills/
```

환경 별칭 폴더의 `.agents/skills/`는 실제 개인 홈 설치 사본이며, 작업공간 폴더의 `.agents/skills/`는 그 저장소에 직접 설치한 스킬이 있을 때만 작성합니다. 공통 설치 사본을 작업공간마다 복제하지 않습니다. 작업공간별 inventory에는 공통 설치 기록의 참조와 해당 저장소의 추가 설치를 구분합니다. 공개할 수 있는 스킬 파일만 사본으로 남기며 개인 AGENTS·config·자격증명·세션은 기존 공개 제한을 따릅니다.

예를 들어 설명용 환경 별칭 `PC-home-sjyun`에서 `repository1`과 `qa-repostory2`를 사용하면 공통 스킬 설치 기록은 하나입니다. 두 저장소의 지침과 적용된 31 설정은 각각 확인하고, 같은 스킬이라도 각 저장소에서의 발견·행동 결과를 따로 남깁니다. 31 설정은 실제로 로드되거나 적용 지침이 참조하는 범위에서 사용하며, 연동이 없는 저장소에서도 독립 개인 스킬과 해당 저장소 지침을 사용합니다.

설치·변경·제거 후 실제 파일과 해시를 다시 확인하고 영향받는 기록을 갱신합니다. 공통 스킬이 변경되면 그 설치를 참조하는 작업공간의 기존 행동 결과는 변경 전 버전의 관찰로 유지하며 새 버전의 재검증 상태를 표시합니다. 자동 수집·동기화·다중 저장소 적용은 이 예시를 작성하는 것으로 구현되거나 완료되지 않습니다.

## 6. 업데이트별 개인 설정 백업

사용자 지정에 따라 개인 Codex 업데이트마다 codex 바로 아래 `<날짜>-<목적>-<작업ID>/` 하나를 새로 추가합니다. 현재 [T-WIN-003 백업](2026-10-03-personal-skills-T-WIN-003/README.md)은 전후 skill 전체 사본·inventory·사용·검증·복구를 묶고 실제 개인 AGENTS·config·raw는 그 폴더의 Git 제외 private/에서 보존합니다.

공개 환경 별칭은 `pc01_codex-app-home`을 유지합니다. before/after의 skill-files는 역사적 관찰·복구 자료이며 `.agents/skills` 자동 발견 구조로 만들거나 독립 수정·다음 설치 입력으로 사용하지 않습니다. 실제 설치 완료는 홈 파일과 해시를 확인한 after에서 기록하고 자동 선택·대표 행동은 별도로 관찰합니다.

앞선 5절의 예시와 기존 2026-09-30 사본·JSON은 당시 자료로 유지합니다. 같은 사용자 홈의 App·CLI에 공통 설치를 중복 작성하지 않으며 다른 repo의 작업 상태는 각각 해당 repo에 둡니다. 다음 업데이트는 이름이 다른 새 폴더를 만들고 지난 snapshot을 덮어쓰지 않습니다.

---

**작성일**: 2026-09-30

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
