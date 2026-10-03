# Windows 개선·보완 검토 — 2026-10-03

검토 기준은 `yunli@773a150`의 Windows 전체 이관본입니다. 시작 시 실제 Git 루트와 clean 상태를 확인했습니다. 사용자 후속 지시에 따라 복사용 구성과 관리 기록의 혼입 W01을 교정했습니다. 실행 helper의 새 보완 사항은 **P2 6건·P3 3건**이며 구현 수정은 하지 않았습니다. 과거 Linux 비교본의 문제를 현재 Windows 결함으로 반복하지 않습니다.

후속 사용자 요청으로 W02–W10과 설명 예시를 수정했습니다. 아래 재현·미실행 문구는 이 검토 시점의 기록이며 현재 구현·검증은 [보고 지침과 helper 보완](REPORTING_REMEDIATION_2026-10-03.md)을 따릅니다.

## 1. 복사용 구성 W01

원인·교정·재발 방지의 기준 본문은 [ISSUE W01](ISSUE.md#4-복사용-영역과-개발-기록-혼입-w01)입니다. 관리 문서 4개와 verification 9개를 이 디렉터리로 옮기고 저장소 루트 README·AGENTS에 배치 규칙을 명시했습니다. 활성 호환 절 37곳과 개인 지침의 이번 35 이관 관리 문구만 정리했습니다. Windows 본체는 `README.md`, `skills/`, `personal/`로 구성하며 298개 파일·19개 skill·동봉 역할과 보존 원문을 유지합니다.

## 2. 수정이 필요한 실행 helper

### W02 P2 — Python 로그 파일이 업무 입력에 포함됨

위치: [Python 템플릿](../../../codex_windows/skills/python-script-template/scripts/script_template.py) 41–44행·168–174행. `-D` 입력 디렉터리와 `--log-dir`를 같게 지정하면 logger가 만든 월별 로그가 즉시 하위 파일 처리 입력에 포함됩니다. 기본 dry-run에서도 자기 로그의 처리 계획이 출력됐습니다. TEMP에 실제 업무 변환을 제공한 일반 실행에서는 데이터 파일을 먼저 바꾼 뒤 열려 있는 로그의 교체가 `PermissionError`로 실패하고 종료 1이 됐습니다. 업무 데이터와 실행 기록을 혼동하며 부분 변경 후 실패합니다.

수정 방향: 활성 FileHandler 경로를 처리 입력에서 제외하거나 입력/로그 경로 충돌을 변경 전에 거부합니다. 같은 디렉터리·명시한 로그 파일 입력·일반/dry-run을 회귀 검사합니다. `using-skills/scripts/script_template.py`도 동일한 실행 사본입니다.

### W03 P2 — 동시 Bash 백업이 완료된 복구본을 덮어씀

위치: [Bash 템플릿](../../../codex_windows/skills/bash-script-template/scripts/script_template.sh) 82–90행. 동일한 파일과 같은 초의 DATE로 두 호출이 겹치면 존재 검사와 `cp -a` 사이에 다른 호출이 백업을 완료할 수 있습니다. TEMP barrier로 첫 호출의 cp만 지연하고 두 번째 호출을 완료한 뒤 원본을 바꾸자, 첫 호출이 완료된 백업을 새 내용으로 덮어썼습니다. 양쪽 종료는 모두 0이었습니다. 단순 사전 존재 control은 종료 1과 기존 bytes 보존을 확인했으므로 남은 문제는 검사·쓰기 사이의 경쟁입니다.

수정 방향: 목적지의 독점 예약 후 완성본 게시 또는 협조자 잠금으로 검사와 복사를 함께 보호합니다. 이미 완료된 백업은 덮어쓰지 않고 실패를 전파하는 경쟁 회귀가 필요합니다. `using-skills/scripts/script_template.sh`도 같은 사본입니다.

### W04 P2 — 짝수 역슬래시 뒤 깨진 링크가 누락됨

위치: [md_common.py](../../../codex_windows/skills/md-link-check/scripts/md_common.py) 12행. 실제 역슬래시 두 개 바로 뒤에 `[Broken](missing.md)`를 두면 링크 시작 괄호가 escape되지 않았는데도 검사기는 링크 0개·문제 0개·종료 0으로 보고합니다. 정상 링크의 누락 검사가 건너뛰어집니다. 앞선 역슬래시 묶음의 홀짝을 판정하도록 보완해야 합니다. [CommonMark escape 규칙](https://spec.commonmark.org/0.31.2/#backslash-escapes)

### W05 P2 — 인라인 코드 예제를 실제 링크로 검사함

위치: [파일 링크 검사기](../../../codex_windows/skills/md-link-check/scripts/md-link-check.py) 40행 및 [헤딩 검사기](../../../codex_windows/skills/md-link-check/scripts/md-heading-check.py) 211행. 두 backtick으로 감싼 코드에 내부 single backtick과 링크 예제를 넣으면 파일 검사기가 예제 링크를 깨진 링크로 보고 종료 1이 됩니다. 헤딩 검사기는 단일 backtick 안의 `[literal](#absent)`도 실제 앵커로 보고 종료 1입니다. 두 사례의 기대 결과는 실제 링크/문제 0개·종료 0입니다.

수정 방향: 같은 길이의 backtick 묶음으로 code span을 찾고 파일/앵커 링크 스캔에서 일관되게 제외합니다. 헤딩 자체의 표시 텍스트는 slug 추출을 위해 별도로 유지합니다. [CommonMark code span 규칙](https://spec.commonmark.org/0.31.2/#code-spans)

### W06 P2 — Windows에서 슬래시 제외 경로가 적용되지 않음

위치: [헤딩 검사기](../../../codex_windows/skills/md-link-check/scripts/md-heading-check.py) 174행. 네이티브 Windows에서 TOML 또는 `-E nested/ignored`로 지정한 실제 상대 제외 경로가 적용되지 않았습니다. 제외한 폴더의 문제 문서까지 검사해 파일 2개·문제 1개·종료 1이 됐고, native separator control은 파일 1개·문제 0개·종료 0입니다.

수정 방향: 설정 경로와 비교 후보 경로를 동일한 방식으로 정규화합니다. TOML/CLI·단일 이름/중첩 경로·Windows/POSIX separator를 함께 확인합니다.

### W07 P2 — percent-encoded 한글 앵커를 거부함

위치: [헤딩 검사기](../../../codex_windows/skills/md-link-check/scripts/md-heading-check.py) 212행. `## 한글`과 연결하는 `#%ED%95%9C%EA%B8%80`을 앵커 없음으로 보고 종료 1입니다. 원 fragment와 UTF-8 percent-decoded fragment를 순서대로 비교하고 TOC 등 관련 비교에도 같은 기준을 적용해야 합니다. [HTML fragment 선택 기준](https://html.spec.whatwg.org/multipage/browsing-the-web.html#select-the-indicated-part)

### W08 P3 — 헤딩 끝의 닫는 #가 slug에 남음

위치: [헤딩 검사기](../../../codex_windows/skills/md-link-check/scripts/md-heading-check.py) 200행. `## Overview ##`와 `#overview` 연결은 유효하지만 닫는 문법을 제목 내용으로 남겨 앵커 문제·종료 1을 보고합니다. 공백/탭 뒤의 escape되지 않은 closing hash 묶음을 ATX 제목 추출에서 제거해야 합니다. [CommonMark ATX heading 규칙](https://spec.commonmark.org/0.31.2/#atx-headings)

### W09 P3 — 대문자 URL scheme을 로컬 파일로 처리함

위치: [파일 링크 검사기](../../../codex_windows/skills/md-link-check/scripts/md-link-check.py) 119행. `HTTPS://example.invalid/a`를 로컬 파일 링크로 세어 파일 없음·종료 1을 보고하며 lowercase control은 로컬 링크 0개·종료 0입니다. 제외하는 URI scheme을 대소문자와 무관하게 분류하고 실제 로컬 경로 문자열은 유지해야 합니다. 외부 사이트 도달성 검사는 실행하지 않았습니다. [RFC 3986 scheme 기준](https://www.rfc-editor.org/rfc/rfc3986.html#section-3.1)

### W10 P3 — 코드 블록 뒤 style 오류의 행 번호가 어긋남

위치: [스타일 검사기](../../../codex_windows/skills/md-link-check/scripts/md-style-check.py) 104행·401–402행. fenced code의 줄을 제거한 뒤 원래 문서의 줄 번호인 것처럼 진단합니다. TEMP 문서의 실제 6행 emoji 공백 오류가 3행으로 출력됐고 code fence 없는 control의 3행은 맞았습니다. 종료 1의 판정은 맞지만 사용자가 수정할 위치가 잘못 안내됩니다. code 행을 빈 줄로 바꿔 원본 행 수를 유지하도록 보완합니다.

W04–W10의 Markdown 도구는 `git-commit-rule`, `md-link-check`, `readme-template`, `security-tools`, `using-skills`, `work-rules`, `zircon-readme-policy`에 같은 사본이 있습니다. 수정 시 각 폴더의 독립 사용을 유지하면서 해당 사본을 함께 대조해야 합니다.

## 3. 설명 보완 후보

[readme-template](../../../codex_windows/skills/readme-template/SKILL.md) 39행, [security-tools](../../../codex_windows/skills/security-tools/SKILL.md) 37행, [zircon-readme-policy](../../../codex_windows/skills/zircon-readme-policy/SKILL.md) 43행의 예제 `$SkillDir`가 모두 `md-link-check` 폴더를 가리킵니다. 실제 자기 폴더로 바꾸라는 주석이 있어 외부 필수 의존성 결함으로 분류하지 않았습니다. 자기 폴더명 또는 중립 placeholder를 쓰면 복사 사용 안내가 더 정확합니다. 이번에는 본문을 고치지 않았습니다.

19개 활성 계약의 새 P1/P2 지침 결함은 확인하지 못했습니다. 이전 Terraform state 복구·패키지 제거·DB 호환성·공개 HTTPS 예시는 Windows 계약에서 이미 대체됩니다. 원문 축약·통합이나 모델/MCP 변경은 이번 검토에서 실행하지 않습니다.

## 4. 실행·검증·미실행

- 구성 검증 통과: 새 경로의 기본 verifier가 19개 skill·원본 182파일·설정 2개·동봉 역할 54개·필수 로컬 링크 214개·Python AST 34개·독립 helper 실행 41회를 확인했습니다.
- 복사 검증 통과: 전체 298파일을 TEMP에만 복사해 본체 구성과 안내 로컬 링크 26개·공식 metadata 19개를 확인했습니다. 이동한 개발 CLI 4개의 `--help`도 다른 CWD에서 통과했습니다. 활성 Python/Bash helper 36파일은 이관 커밋과 bytes가 같습니다.
- 문서 검증 통과: 관리·사용 안내 19개 문서의 파일 링크와 교차 앵커 42개에 누락이 없습니다. 새 PowerShell 복사 예제 1개는 parser 구문만 확인하고 실제 홈 복사는 실행하지 않았습니다.
- 새 실패 재현: Python 정상 변환/입력 로그 충돌과 dry-run, Bash 경쟁 및 사전 존재 control 총 4조건을 실행했습니다. Markdown은 16조건 중 control 7건 일치·새 불일치 9건을 7개 원인으로 분류했습니다. 성공한 포장 검사와 helper 실패 재현을 구분합니다.
- 환경: Windows Python 3.14.8·설치된 Git Bash를 사용했습니다. 원시 stdout·절대 개인 경로·실행 token은 로컬 비공개 TEMP 증거에 보존하고 원격 문서에 복사하지 않습니다.
- 미실행: helper 결함 수정·전체 기존 79/63 회귀 재실행·실제 개인 홈 설치/config 병합·새 Codex 발견/자동 선택·렌더러 UI 검증·symlink 추가 권한·ACL/ADS/owner/SMB·실제 서비스/원격 인프라·main 반영.

이관 당시 `results.json`·`input_hashes.json`·`behavior_summary.json`은 `773a150`의 과거 결과와 당시 경로를 보존합니다. 포장 변경에 맞춰 과거 해시를 다시 생성하거나 새 helper 검토 결과로 바꾸지 않았습니다. 당시 후속 수정의 완료 항목은 [보존 이력](../../history/2026-10-03/T-WIN-002-distribution-root.md#52-복사용-구성과-개선-검토)으로 이동했습니다. 현재 후속 행동은 [TODO](TODO.md)를 따릅니다.

## 5. 게시와 복구

이번 변경은 복사용 구성 정리와 검토·지침 기록입니다. 검증 후 yunli에 일반 commit·push하고 사용자 검증을 기다립니다. main·실제 설정·운영 적용은 별도 후속입니다. 게시한 변경의 복구는 검토한 revert를 사용하며 Linux·Kiro·GPT·105_backup·이전 증거·사용자 변경은 보존합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
