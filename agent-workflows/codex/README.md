# Codex 개인 적용본과 skill 확인

이 문서와 사본·JSON은 **2026-09-30의 역사적 관찰**입니다. 새 1.0.0 개인 스킬의 설치·발견·행동 결과가 아니며 자동 동기화하지 않습니다.

## 1. 원본과 개인 적용 사본

사용자가 선택한 환경 이름은 `pc01_codex-app-home`입니다. 실제 hostname·IP·계정명이 아닌 공개용 별칭이며 이전 `codex-windows-personal`과 같은 사용자 범위 환경입니다. 이름의 app은 현재 작업 도구를 나타내며 같은 사용자 홈을 사용하는 CLI의 skill 파일을 별도 설치로 복제하지 않습니다.

당시 구현 원본의 현재 보존 위치는 [codex/payload/skills](../../105_backup/codex/payload/skills/)입니다. 이곳에는 실제 개인 설치 파일과 일치하는 공개 가능 skill 사본을 보관합니다. 새 구현 변경은 신규 codex/skills에서, 실제 설치·변경·제거 이후 관찰 갱신은 별도 확인 후 진행하며 사본을 독립 편집하거나 설치 입력으로 사용하지 않습니다.

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

- [공통 최초 적용·업데이트](../README.md): 실행 범위·백업·검증·복구 절차.
- [현재 저장소 안내](../../README.md#3-개인-스킬의-사용-단위): 신규 개인 스킬의 폴더 복사 기준.
- [현재 Codex 모음](../../codex/README.md): 스킬 19개·선택적 개인 지침·수동 복사. 위 2026-09-30 개인 사본과는 설치/관찰 시점을 구분합니다.
- [1.0.0 재작성 기록](REBUILD_1.0.0.md): 구현·검증·게시와 실제 설치의 구분.
- [공식 skill 경로](https://learn.chatgpt.com/docs/build-skills): 사용자 범위와 저장소 범위 발견 경로.

---

**작성일**: 2026-09-30

**마지막 업데이트**: 2026-10-01

© 2026 siasia86. Licensed under CC BY 4.0.
