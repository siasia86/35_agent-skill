# 35 `agent-skill`

재사용할 AI 지침·skill·agent와 도구별 공개 미러를 관리합니다.

## 목차

| 섹션                                              |
|---------------------------------------------------|
| [1. 목적](#1-목적) / [2. 구성](#2-구성)           |
| [3. 운영 원칙](#3-운영-원칙) / [4. 검증](#4-검증) |
| [5. 활용](#5-활용)                                |

---

## 1. 목적

`35_agent-skill`은 도구별 보존 원본과 재사용 자산 개발 공간을 분리합니다. kiro/·gpt/는 보존 원본, codex/는 개선 공간, claude/는 예약 영역입니다. 개발 후보를 승인된 설치 release로 취급하지 않습니다.

### 세 저장소의 책임

| 저장소         | 책임                                                      | 담당하지 않는 것        |
|----------------|-----------------------------------------------------------|-------------------------|
| 35_agent-skill | 재사용 지침·skill·agent 구현과 자산 목록                  | 대상별 적용 승인        |
| 31_governances | 공통 정책과 저장소별 관리 설정·자산 선택·예외의 중앙 원본 | 실행 코드·자격증명 보관 |
| 30_sia-scripts | 검증·계획·설치·갱신·복구 실행 도구                        | 명세에 없는 정책 추정   |

위 표는 중앙 관리 목표의 책임 구분입니다. 31의 기존 v1과 중앙 소유 전환 계약은 구분하며, 기존 대상 저장소의 예외를 자동 덮어쓰지 않습니다. 35는 구현 원본과 선택 후보를 제공하고 적용 대상·예외·승인을 자체 결정하지 않습니다.

현재 연결은 35 자산 목록 + 31 draft profile → 30 계획 검증 → 격리 fixture용 패키지 시험입니다. payload는 지침 1개·skill 16개·agent 10개와 동반 파일 4개로 구성한 개발 후보이며 실제 runtime 배포가 아닙니다. 검증된 staging의 운영 활성화·권한·Ansible 시험과 release는 8·9번 PLAN으로 남깁니다.

저장소 공통 정책의 원본은 [31 governances](https://github.com/siasia86/31_governances), 실행 도구는 [30 sia-scripts](https://github.com/siasia86/30_sia-scripts)에서 관리합니다. 이 저장소의 작업 범위·보존 규칙·예외는 [AGENTS.md](AGENTS.md)를 따릅니다. 아래 내용은 진입 안내이며 상세 정책 원본을 대체하지 않습니다.

## 2. 구성

| 디렉토리           | 역할                          | 원본·범위                     |
|--------------------|-------------------------------|-------------------------------|
| `kiro/`            | Kiro 공개 미러                | `~/.kiro/` 허용 목록          |
| `gpt/`             | GPT/Codex 보존 원본           | 개선 시 직접 수정하지 않음    |
| `codex/`           | 재사용 자산 개발·선택 payload | 전체 복사 설치 금지           |
| `claude/`          | Claude 공개 미러 예정         | 원본·허용 목록 미정           |
| `agent-workflows/` | 공통 안전 절차·시험 기록      | 도구별 사용자 지침은 각 docs/ |
| `_reference/`      | Agent·Skill 개선 참고 문서    | 32 문서 복사본                |

- [Kiro 미러](kiro/README.md): `~/.kiro/`에서 허용된 자료만 보존합니다.
- [GPT 보존 원본](gpt/README.md): 이식 출발 자료입니다.
- [Codex 개발본](codex/README.md): 선택 후보와 검증 상태를 확인합니다.
- [Claude 미러](claude/README.md): Claude 자료 추가를 위한 예약 영역입니다.
- [Agent workflow](agent-workflows/README.md): 공통 체크리스트·도구별 지침 색인·기존 SE 시험 기록을 관리합니다.
- [Agent 참고 문서](_reference/INDEX.md): 업데이트에 사용하는 참고 문서 색인입니다.

### 개발 상태와 설치 경계

- codex/payload에는 최소 SE 지침, skill 16개·agent 10개와 동반 파일 4개가 있습니다. [자산 목록](codex/ASSET_CATALOG.json)은 개발 목록이지 승인 release manifest가 아닙니다.
- 최소 지침의 기존 개인 설치 시험 기록과 신규 사용자의 설치 완료는 다릅니다. skill·agent 후보의 정적·격리 검사를 전체 runtime 검증으로 확대하지 않습니다.
- 현재 선택 파일과 검증 범위는 [설치 매핑](codex/PAYLOAD_MAP.md), [Batch 6 기록](codex/MIGRATION_BATCH6.md), [경량화 기록](codex/WORKFLOW_SKILL_PLAN.md), [개발 TODO](TODO.md)에서 확인합니다.
- gpt/·kiro/ 보존 영역을 일괄 활성화하지 않습니다. claude/는 source·허용 목록·설치 대상이 확정되기 전까지 적용하지 않습니다.
- docs/·TODO·시험 기록은 설치 payload가 아닙니다. 보존 미러의 허용 목록과 runtime 설치 목록도 구분합니다.

## 3. 운영 원칙

- 저장소 정책은 특정 AI 도구의 실행 환경과 분리합니다.
- 도구별 payload와 도구별 workflow를 분리합니다.
- 개인 설정, 세션 상태, 자격증명, 내부 환경 정보는 공개 미러에 포함하지 않습니다.
- 보존 미러는 원본에서 공개 미러 방향으로 관리하며 자동 역동기화하지 않습니다. codex/ 개선 작업과 구분합니다.
- 공통 절차는 `agent-workflows/common/`, 도구별 사용자 지침은 각 도구의 `docs/`에 둡니다. 문서는 runtime payload가 아닙니다.
- 디렉토리 구조를 변경하면 이 `README.md`와 `CHANGELOG.md`를 함께 갱신합니다.

### 변경 절차와 예외

1. 작업본·브랜치·기존 변경과 저장소 지침을 확인합니다.
2. 복합 개발 작업은 [TODO](TODO.md)에 범위·검증·복구를 정리하고 보존 원본 대신 codex/에서 개선합니다. 사용자 지침 변경과 runtime 변경은 구분합니다.
3. 변경 파일의 문법·참조·해시·비밀정보를 검사하고 완료 내용을 CHANGELOG에 기록합니다.
4. 승인된 작업 브랜치에 commit·push합니다. 개발 후보 게시를 release 승인이나 개인 홈 설치 승인으로 처리하지 않습니다.

직접 수정 제한의 예외는 타당한 이유·명시적 범위·종료 조건·검증·복구 방법이 있어야 합니다. 예외는 해당 작업 종료 시 만료되며 다음 작업에 재사용하지 않습니다. ACL·소유권·자격증명·운영 권한을 자동 확대하지 않습니다. 게시 후 복구는 검토된 revert로 수행하고 사용자 변경을 보존합니다.

AI 지침과 skill 자체는 명령 차단을 강제하는 보안 장치가 아닙니다. 개발·테스트의 넓은 권한도 실행 승인과 구분하며 운영 강제는 실행 도구와 실제 권한·검사 체계에서 검증해야 합니다.

## 4. 검증

```bash
sia-md-link-check README.md CHANGELOG.md
sia-md-heading-check README.md CHANGELOG.md
sia-md-style-check README.md CHANGELOG.md
git diff --check
gitleaks detect --source . --no-git --no-banner
```

위 명령은 루트 문서 변경의 기본 검사입니다. 다른 문서를 변경하면 해당 파일도 검사하고, 검사 도구 미설치·읽기 실패·부분 검사를 전체 통과로 처리하지 않습니다. 도구별 payload를 변경한 경우 JSON·TOML·Bash·manifest 검증을 추가합니다. `kiro/`와 향후 `claude/`의 mirror 문서는 원본 형식을 보존할 수 있으므로 일반 Markdown 스타일 검사에서 별도 예외가 필요한지 확인합니다.

## 5. 활용

먼저 사용할 도구의 지침을 읽고 참고만 할지, 자신의 환경에 선택 적용할지 결정합니다. 문서 열람과 clone은 설치·수정 승인이 아닙니다.

| 도구   | 최초 적용                                             | 업데이트                                              | 상태                         |
|--------|-------------------------------------------------------|-------------------------------------------------------|------------------------------|
| Kiro   | [Kiro 최초 적용](kiro/docs/KIRO_SETUP_GUIDE.md)       | [Kiro 업데이트](kiro/docs/KIRO_UPDATE_GUIDE.md)       | 선택 파일과 의존성 검토 필요 |
| Codex  | [Codex 최초 적용](codex/docs/CODEX_SETUP_GUIDE.md)    | [Codex 업데이트](codex/docs/CODEX_UPDATE_GUIDE.md)    | 개발 후보·전체 설치 금지     |
| Claude | [Claude 최초 적용](claude/docs/CLAUDE_SETUP_GUIDE.md) | [Claude 업데이트](claude/docs/CLAUDE_UPDATE_GUIDE.md) | 예약 영역·실제 적용 금지     |

- [공통 최초 적용](agent-workflows/common/USER_TODO.md)과 [공통 업데이트](agent-workflows/common/UPDATE_TODO.md): 백업·선택 목록·검증·복구 기준.
- [개발 TODO](TODO.md): 저장소의 미완료 개발 작업. 사용자 설치 순서와 구분합니다.
- [변경 이력](CHANGELOG.md): 완료된 저장소 변경.
- [운영 이슈](ISSUE.md): 관찰된 문제·임시 조치·해결 조건.

공용 지침서의 체크리스트는 사용자별 작업 기록에 복사해 사용합니다. 개인 경로·백업·실행 결과를 공용 지침서에 누적하지 않습니다. docs/·개발 TODO·시험 기록은 runtime 복사에서 제외하고, 선택한 자산과 필수 의존성만 설치합니다.

### 5.1 개인 Codex skill 직접 설치

AI 호출 없이 Git clone 또는 ZIP으로 받은 저장소에서 필요한 skill 폴더를 복사할 수 있습니다. 원본은 `codex/payload/skills/<이름>/`, 개인 설치 대상은 사용자 홈의 `.agents/skills/<이름>/`입니다. [공식 skill 경로 안내](https://learn.chatgpt.com/docs/build-skills)와 [선택형 설치 매핑](codex/PAYLOAD_MAP.md)을 기준으로 합니다. 이 문서는 개발 후보의 개인 선택 설치 방법이며 실제 설치 완료 기록은 아닙니다.

`SKILL.md`만 복사하지 않고 선택한 폴더 전체를 복사합니다. `work-rules/references/`의 파일 3개와 `python-script-template/assets/standalone.py`도 해당 skill과 함께 배치해야 합니다. `codex/` 전체·archive·templates·agent TOML·개인 AGENTS는 아래 복사 대상에 포함하지 않습니다. 중앙 구성의 governance-default·governance-repository는 31 정책과 30 생성기가 필요한 [별도 계약](codex/CODEX_GOVERNANCE.md)을 따릅니다.

현재 설치 후보는 skill 16개이며 일반 절차·중복 역할 9개는 [정리 기록](codex/WORKFLOW_SKILL_PLAN.md#5-2026-09-30-개인-skill-설치-목록-정리)에 따라 archive로 보존했습니다. 기존 개인 홈의 제외된 skill은 자동 삭제하지 않습니다. 새 목록으로 전환하려면 사용자 수정·다른 의존성을 확인한 뒤 해당 폴더를 runtime 검색 밖에 보관합니다.

#### Python — clone 후 설치

[개인 skill setup 스크립트](codex/scripts/setup_personal_skills.py)는 Python 3.9 이상과 표준 라이브러리만 사용합니다. Git clone 또는 ZIP을 푼 뒤 저장소 루트에서 실행합니다. 30·31 저장소, profile, 인터넷 연결, AI 호출은 필요하지 않습니다. Linux에서는 Codex를 사용하는 sjyun 계정으로 실행하고 Windows에서는 자신의 Codex 사용자 계정으로 실행합니다.

```bash
python3 codex/scripts/setup_personal_skills.py list
python3 codex/scripts/setup_personal_skills.py install --all --dry-run
python3 codex/scripts/setup_personal_skills.py install --all
```

이 저장소의 `.gitattributes`는 payload·catalog·governance template의 LF bytes를 고정하여 Windows의 `core.autocrlf=true` clone에서도 해시를 유지합니다. 이전 checkout에서 해시 오류가 발생하면 변경·백업을 확인한 뒤 최신본을 새 경로에 clone합니다. 검증을 통과시키려고 catalog 해시를 임의로 다시 계산하지 않습니다.

Windows PowerShell에서는 같은 인자를 사용하고 `python3` 대신 `py -3`을 사용합니다. Python launcher가 없다면 설치된 Python 3.9 이상의 `python` 명령을 사용합니다.

```powershell
py -3 codex/scripts/setup_personal_skills.py install --all --dry-run
py -3 codex/scripts/setup_personal_skills.py install --all
```

필요한 것만 설치하려면 `--all` 대신 `--skills`로 지정합니다. 다음 예시는 코드 검토·오류 조사·검증·문서 작업·Python 작성에 사용할 개인 skill을 선택합니다.

```bash
python3 codex/scripts/setup_personal_skills.py install --skills code-review debugging-and-recovery testing-guide markdown-review md-link-check python-script-template work-rules
```

기본 대상은 실행 계정의 `~/.agents/skills/`이며 `--dest <경로>`로 변경할 수 있습니다. 스크립트는 35 catalog의 선택 skill·동반 파일 목록과 SHA-256을 확인하고 검증한 bytes를 임시 위치에 준비한 뒤 폴더별로 배치합니다. 동일한 기존 설치는 건너뛰고 사용자 수정·추가 파일·심볼릭 링크·해시 불일치는 덮어쓰기 전에 거부합니다. `--dry-run`은 목적지와 lock도 만들지 않습니다. 여러 skill 전체의 원자적 설치·복구를 보장하지 않으며 중간 실패 시 완료된 신규 폴더가 남을 수 있습니다. 출력에서 설치분을 확인하고 아래 복구 기준을 따릅니다. 설치 중 다른 도구로 같은 목적지를 수정하지 않습니다.

개인 skill만으로 코드 검토·디버깅·문서 검토·스크립트 작성 절차를 사용할 수 있습니다. 작업 대상 저장소에 적용되는 지침이 있으면 따르되 31 정책을 새로 생성하거나 필수로 다운로드하지 않습니다. `repo-governance`는 로컬 지침 발견을 돕고 중앙 binding이 있을 때만 해당 고정 정책 경로를 사용합니다. checker·Git·프로젝트 테스트 등 작업에 필요한 실행 도구는 별도로 준비하며, 없는 검사 도구는 미실행으로 보고합니다. skill 설치는 도구 설치나 운영 권한 부여를 뜻하지 않습니다.

#### Linux — sjyun 계정의 Bash

Codex를 사용하는 `sjyun` 계정으로 터미널을 열고, 그 계정이 읽을 수 있는 35 저장소 루트로 이동합니다. 다음 명령의 `$HOME`은 실행 계정의 홈이므로 목적지는 보통 `/home/sjyun/.agents/skills/`입니다. root나 sudo로 실행하지 않습니다. 저장소가 `/root` 아래에 있어 읽을 수 없다면 계정 소유 위치에 clone하거나 ZIP을 풀어 사용합니다.

다음 예시는 세 skill을 선택하며 `skill_names`를 필요한 폴더 이름으로 바꿀 수 있습니다. 같은 이름의 설치가 있으면 복사 전에 중단합니다.

```bash
(
    set -eu
    repo_dir="$PWD"
    skill_root="$HOME/.agents/skills"
    skill_names=(md-link-check repo-governance work-rules)

    for skill_name in "${skill_names[@]}"; do
        skill_src="$repo_dir/codex/payload/skills/$skill_name"
        skill_dst="$skill_root/$skill_name"
        test -f "$skill_src/SKILL.md" || { printf '원본 없음: %s\n' "$skill_src"; exit 1; }
        if [ -e "$skill_dst" ] || [ -L "$skill_dst" ]; then
            printf '기존 설치를 먼저 비교하세요: %s\n' "$skill_dst"
            exit 1
        fi
    done

    mkdir -p -- "$skill_root"
    for skill_name in "${skill_names[@]}"; do
        skill_src="$repo_dir/codex/payload/skills/$skill_name"
        skill_dst="$skill_root/$skill_name"
        cp -R -- "$skill_src" "$skill_root/"
        diff -r -- "$skill_src" "$skill_dst"
        printf '복사·내용 비교 완료: %s\n' "$skill_dst"
    done
)
```

#### Windows — PowerShell

Windows의 Codex 사용자 계정에서 PowerShell을 열고 `repoDir`를 내려받은 저장소 경로로 바꿉니다. 개인 설치 대상은 `$HOME\.agents\skills\`이며 보통 `C:\Users\<사용자>\.agents\skills\`입니다. 관리자 실행 없이 사용합니다. WSL에서 Codex를 실행한다면 Windows 경로 대신 WSL 안의 사용자 홈에서 위 Linux 절차를 사용합니다.

```powershell
$ErrorActionPreference = 'Stop'
$repoDir = 'C:\workspaces\35_agent-skill'
$skillRoot = Join-Path $HOME '.agents\skills'
$skillNames = @('md-link-check', 'repo-governance', 'work-rules')

foreach ($skillName in $skillNames) {
    $skillSrc = Join-Path $repoDir "codex\payload\skills\$skillName"
    $skillDst = Join-Path $skillRoot $skillName
    if (-not (Test-Path -LiteralPath (Join-Path $skillSrc 'SKILL.md') -PathType Leaf)) {
        throw "원본 없음: $skillSrc"
    }
    if (Get-Item -LiteralPath $skillDst -Force -ErrorAction SilentlyContinue) {
        throw "기존 설치를 먼저 비교하세요: $skillDst"
    }
}

New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
foreach ($skillName in $skillNames) {
    $skillSrc = Join-Path $repoDir "codex\payload\skills\$skillName"
    $skillDst = Join-Path $skillRoot $skillName
    Copy-Item -LiteralPath $skillSrc -Destination $skillRoot -Recurse
    foreach ($file in Get-ChildItem -LiteralPath $skillSrc -Recurse -File) {
        $relative = $file.FullName.Substring($skillSrc.Length + 1)
        $copied = Join-Path $skillDst $relative
        if ((Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne
            (Get-FileHash -LiteralPath $copied -Algorithm SHA256).Hash) {
            throw "복사 해시 불일치: $copied"
        }
    }
    Write-Output "복사·해시 비교 완료: $skillDst"
}
```

파일 탐색기로도 가능합니다. `%USERPROFILE%\.agents\skills\`를 만든 뒤 `codex\payload\skills\` 아래에서 필요한 폴더를 선택해 복사합니다. 같은 이름의 폴더가 있으면 교체·병합을 바로 선택하지 말고 기존 폴더를 별도 백업한 뒤 내용을 비교합니다. `$HOME`과 `%USERPROFILE%`이 다르게 설정된 환경에서는 실제 Codex 실행 계정의 홈을 확인합니다.

#### 발견 확인과 업데이트

복사 후 새 Codex 세션에서 `/skills`로 선택한 이름이 나타나는지 확인합니다. 나타나지 않으면 Codex를 재시작하고 실행 계정·홈·`<이름>/SKILL.md` 구조를 확인합니다. 파일 복사와 해시 일치는 지침의 실제 행동 검증을 대신하지 않습니다.

기존 설치 갱신은 먼저 대상 폴더를 runtime 검색 밖에 백업하고 원본과 변경점을 비교한 뒤 필요한 변경을 반영합니다. `.codex/skills`·프로젝트 `.agents/skills`·plugin 등에 같은 이름이 있는지도 확인합니다. 같은 이름의 skill이 여러 경로에 있다고 자동 병합되는 것은 아닙니다. 실패하거나 복사가 중간에 멈추면 이번에 추가한 파일을 확인해 runtime 검색 밖으로 이동하고 기존 사용자 변경과 백업을 보존합니다. 자세한 갱신·복구 기준은 [설치 매핑 §3](codex/PAYLOAD_MAP.md#3-설치갱신복구-조건)을 따릅니다.


---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
