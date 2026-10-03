# 개인 Codex 로컬 형식 관리 구성

> 2026-10-03 당시 구성·검증 기록입니다. 2026-10-04 이관 후 현재 상태·업데이트 절차는 [SMA 기록](../windows/records/2026-10-04-record-relocation-SMA-20261004-01/README.md)과 [Windows TODO](../windows/TODO.md)를 따릅니다. private의 과거 bytes와 관찰 시점은 유지합니다.

작업 ID는 `PCS-20261003-structure`입니다. 현재 사용자 홈의 `.codex/AGENTS.md`, `.codex/config.toml`, `.agents/skills/<이름>/` 형식을 관리 기록과 before/after 백업에도 유지합니다. 작업 상태는 [Windows TODO](../windows/TODO.md)에서 관리하고 이 문서는 범위·검증 근거·복구 방법을 보존합니다.

## 목차

- [1. 범위와 담당](#1-범위와-담당)
- [2. 업데이트 폴더와 백업](#2-업데이트-폴더와-백업)
- [3. 검증 결과](#3-검증-결과)
- [4. 복구와 한계](#4-복구와-한계)

## 1. 범위와 담당

담당 파일은 이 폴더, [당시 구조 색인](STRUCTURE_INDEX_2026-10-03.md), [백업 명령](../windows/verification/Snapshot-PersonalConfig.ps1), 루트 TODO의 이 작업 항목입니다. 현재 Git branch는 `main`이며 이 작업에서 branch 전환·staging·commit·push는 수행하지 않습니다.

다른 agent는 skill 개선·개인 설치를 진행 중입니다. 기존 변경이 있던 CHANGELOG, 개인 적용 README·VERIFICATION·runtime_inventory, md-link-check 구현·관찰 사본과 catalog는 그대로 보존합니다. 두 작업 사이에 개인 홈 내용이 바뀌면 snapshot 간 차이를 별도로 기록하며 이번 구조 작업의 수정으로 처리하지 않습니다.

이 작업은 관리 구조와 백업 명령을 추가합니다. 개인 홈의 파일 위치·지침 내용·model·reasoning·approval·sandbox·MCP·plugin 설정값을 수정하지 않습니다. 현재 설정 파일의 기본값과 이 세션에 적용된 관리 권한은 각각의 범위로 판단합니다.

## 2. 업데이트 폴더와 백업

`private/before/`와 `private/after/`가 각각 사용자 홈의 상대 경로를 그대로 담습니다. 이번 선택 대상은 `code-review`, `debugging-and-recovery`, `git-commit-rule`, `markdown-review`, `md-link-check`, `planning-and-breakdown`, `work-rules`의 전체 폴더 및 개인 설정 두 파일입니다. 인증·계정 DB·세션·로그·plugin·system 자료는 수집하지 않습니다.

[.gitignore](.gitignore)의 `/private/`를 복사 전에 `git check-ignore`로 확인합니다. 각 phase의 `manifest.json`에 시각·전체 파일 목록·bytes 길이·SHA-256을 기록하고 복사 후 다시 대조합니다. manifest 생성 전 실패한 snapshot은 완료된 백업으로 사용하지 않습니다.

다음 업데이트는 기존 폴더와 다른 이름을 선택하고 그 폴더에 `/private/`를 제외하는 `.gitignore`를 먼저 둡니다. PowerShell 7에서 35 Git 루트를 현재 경로로 두고 실행합니다. 아래 ID는 새 폴더를 가리키는 예시이며 자동 업데이트나 예약 실행을 만들지 않습니다.

```powershell
& './agent-workflows/codex/windows/verification/Snapshot-PersonalConfig.ps1' `
    -UpdateId 'YYYYMMDD-purpose-taskid' -Phase before
# 승인된 설정/skill 변경과 검증을 진행합니다.
& './agent-workflows/codex/windows/verification/Snapshot-PersonalConfig.ps1' `
    -UpdateId 'YYYYMMDD-purpose-taskid' -Phase after
```

대상 skill이 달라지면 `-SkillNames`에 실제 선택한 이름 배열을 명시합니다. 이 명령은 일반 사용자 홈의 현재 로컬 형식을 기준으로 하며, 별도 `CODEX_HOME` 환경은 경로·범위를 확인한 별도 대상입니다. 기존 phase 덮어쓰기, 빈 선택, 경로 이탈 및 reparse point를 거부합니다. 원본 목록·bytes가 수집 중 달라지면 복사하지 않고 실패합니다.

## 3. 검증 결과

2026-10-03 한국 시간 20:24:21의 before 90개 파일, 20:27:24의 after 91개 파일을 각각 보존했습니다. 두 사본 모두 개인 skill 7개와 설정 두 파일을 포함합니다. 181개 파일의 SHA-256·bytes 길이·전체 목록을 manifest와 다시 대조했고 두 config의 TOML 구문도 통과했습니다.

기존 파일의 내용 변경과 제거는 0개입니다. after에는 `md-link-check/scripts/__pycache__/md_common.cpython-314.pyc` 캐시 한 개가 추가됐습니다. 생성 주체는 확인하지 않았으며, 폴더 전체 보존 범위에 포함해 원형대로 기록했습니다. 개인 AGENTS·config 및 기존 skill 파일의 before/after bytes는 같습니다.

- PowerShell 7 문법 검사와 실제 before/after 생성·복사 후 해시 검증: 통과.
- 기존 phase 덮어쓰기·잘못된 작업 ID·빈 skill 선택 거부: 통과. 기존 manifest 해시도 유지했습니다.
- 개인 사본·manifest의 Git 제외와 `private/` 아래 Git 추적 파일 0개: 확인. 별도 비공개 검증 기록도 같은 제외 범위에 둡니다.
- Markdown 검사기 `26.10.03`의 고정 before 사본으로 담당 문서 3개 검사: 스타일 0건, 헤딩 52개·이슈 0건, 링크 40개·깨진 링크 0건.
- Git diff 공백 검사: 통과. 기존 파일의 줄바꿈 안내는 별도 관찰이며 다른 agent의 변경을 수정하지 않았습니다.

첫 Git 제외 집합 대조는 Git의 한글 경로 표시 방식 때문에 실패했습니다. NUL 구분 입력·출력으로 다시 대조해 모든 사본의 제외를 확인했습니다. 원문·설정값은 출력하지 않았고 검증 상세는 비공개 `private/verification.json`에 보존합니다.

## 4. 복구와 한계

이번 변경을 되돌릴 때는 관리 공간의 담당 파일과 TODO의 해당 항목만 대조합니다. 기존 기록·다른 agent 변경·개인 홈은 삭제하거나 덮어쓰지 않습니다. 개인 홈을 변경하지 않았으므로 이번 구조 변경을 취소하기 위해 runtime을 복구할 필요는 없습니다.

백업에서 개인 파일을 복구할 때는 해당 phase manifest와 실제 bytes의 일치를 확인하고 현재 파일과 비교합니다. 다른 작업의 새 변경이 있으면 복구 범위를 다시 판단한 뒤 승인된 파일·skill 폴더만 적용합니다. 자동 복구 명령·전체 홈 덮어쓰기·권한 변경은 추가하지 않았습니다.

사본은 파일 bytes와 전체 파일 목록을 보존합니다. ACL·ADS·빈 폴더·프로세스 상태·인증 자료의 복구를 보장하지 않으며, 여러 source 파일에 대한 OS 수준의 원자적 snapshot은 아닙니다. 수집 전후 목록·해시가 같음을 확인하는 범위입니다. 개인 홈에 실제 쓰는 복구 시험, 별도 새 세션의 자동 발견·선택·대표 행동 검증은 미실행입니다.

출처: 현재 로컬 파일의 지정 목록, [기존 개인 적용 안내](../README.md), [공식 지침 경로](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [공식 skill 경로](https://learn.chatgpt.com/docs/build-skills), [공식 설정 경로](https://learn.chatgpt.com/docs/config-file/config-basic). 공식 문서 확인일은 2026-10-03입니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
