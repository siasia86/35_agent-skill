# 35 `agent-skill`

AI Agent skills repo. AI 도구별 공개 자료 미러를 관리합니다.

## 목차

| 섹션                                              |
|---------------------------------------------------|
| [1. 목적](#1-목적) / [2. 구성](#2-구성)           |
| [3. 운영 원칙](#3-운영-원칙) / [4. 검증](#4-검증) |
| [5. 활용](#5-활용)                                |

---

## 1. 목적

`35_agent-skill`은 AI 도구별 실행 환경(skill·agent·prompt·hook)의 공개 자료 mirror를 관리하는 저장소입니다. 도구별 원본과 공개 mirror의 관계는 하위 디렉토리별로 분리합니다.

저장소 운영 정책 자체는 [31 `governances`](https://github.com/siasia86/31_governances)를 따릅니다. 이 저장소에는 저장소 공통 policy를 다시 작성하지 않습니다.

## 2. 구성

| 디렉토리           | 역할                           | 원본·범위                        |
|--------------------|--------------------------------|----------------------------------|
| `kiro/`            | Kiro 공개 미러                 | `~/.kiro/` 허용 목록             |
| `gpt/`             | GPT/Codex 자산                | `AGENTS.md`·`.agents/`·`.codex/` |
| `claude/`          | Claude 공개 미러 예정          | 원본·허용 목록 미정              |
| `agent-workflows/` | 도구별 최초 적용·업데이트 TODO | common·kiro·gpt·claude           |
| `_reference/`      | Agent·Skill 개선 참고 문서     | 32 문서 복사본                   |

- [Kiro 미러](kiro/README.md): `~/.kiro/`에서 허용된 자료만 보존합니다.
- [GPT/Codex 자산](gpt/README.md): GPT/Codex Agent·Skill 자료를 관리합니다.
- [Claude 미러](claude/README.md): Claude 자료 추가를 위한 예약 영역입니다.
- [Agent workflow](agent-workflows/README.md): 공통 및 도구별 TODO를 관리합니다.
- [Agent 참고 문서](_reference/INDEX.md): 업데이트에 사용하는 참고 문서 색인입니다.

## 3. 운영 원칙

- 저장소 정책은 특정 AI 도구의 실행 환경과 분리합니다.
- 도구별 payload와 도구별 workflow를 분리합니다.
- 개인 설정, 세션 상태, 자격증명, 내부 환경 정보는 공개 미러에 포함하지 않습니다.
- 원본에서 공개 미러로의 동기화만 허용하며 자동 역동기화는 수행하지 않습니다.
- 공통 workflow는 `agent-workflows/common/`에 두고 도구별 명령은 각 adapter에 둡니다.
- 디렉토리 구조를 변경하면 이 `README.md`와 `CHANGELOG.md`를 함께 갱신합니다.

## 4. 검증

```bash
sia-md-link-check .
sia-md-heading-check .
sia-md-style-check .
git diff --check
gitleaks detect --source . --no-git --no-banner
```

도구별 payload를 변경한 경우 JSON·TOML·Bash·manifest 검증을 추가합니다. `kiro/`와 향후 `claude/`의 mirror 문서는 원본 형식을 보존할 수 있으므로 일반 Markdown 스타일 검사에서 별도 예외가 필요한지 확인합니다.

## 5. 활용

먼저 사용할 도구를 선택하고 `agent-workflows/`의 공통 TODO와 도구별 adapter TODO를 확인합니다. clone 저장소의 payload와 실제 사용자 runtime target을 혼동하지 않습니다.

### 5-1. Git clone 및 상태 확인

```bash
git clone <repository-url> <clone-path>
cd <clone-path>
git status --short --branch
```

### 5-2. 도구별 workflow 선택

- Kiro: [Kiro USER TODO](agent-workflows/kiro/USER_TODO.md)와 [Kiro UPDATE TODO](agent-workflows/kiro/UPDATE_TODO.md).
- GPT/Codex: [GPT USER TODO](agent-workflows/gpt/USER_TODO.md)와 [GPT UPDATE TODO](agent-workflows/gpt/UPDATE_TODO.md).
- Claude: [Claude USER TODO](agent-workflows/claude/USER_TODO.md)와 [Claude UPDATE TODO](agent-workflows/claude/UPDATE_TODO.md).
- 공통 원칙: [공통 USER TODO](agent-workflows/common/USER_TODO.md)와 [공통 UPDATE TODO](agent-workflows/common/UPDATE_TODO.md).

도구별 adapter가 정한 source·staging·runtime target과 backup·dry-run·rollback 절차를 먼저 수행합니다.

### 5-1. Git clone

```bash
git clone <repository-url> <clone-path>
cd <clone-path>
git status --short --branch
```

Git clone 직후에는 Kiro CLI를 실행하지 않습니다. 먼저 clone 저장소의 `kiro/` 내용을 확인하고 로컬 Kiro 실행 환경을 준비합니다.

### 5-2. Kiro Agent·Skill 사전 적용

`kiro/03_home-sjyun-kiro.sh`는 clone 위치를 계산한 뒤 실제 복사 전에 실행할 `rsync` 명령을 출력합니다. 스크립트 자체가 `$HOME/.kiro`를 자동으로 덮어쓰지는 않습니다.

```bash
bash kiro/03_home-sjyun-kiro.sh
```

현재 `$HOME/.kiro`를 백업한 뒤 `rsync --dry-run` 결과의 대상·제외 목록·변경 파일을 확인합니다.

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
SOURCE="$REPO_ROOT/kiro"
TARGET="$HOME/.kiro"
BACKUP="$HOME/.kiro.backup.$(date +%Y%m%d_%H%M%S)"

sudo cp -a "$TARGET" "$BACKUP"
rsync -av --dry-run \
    --exclude='.cli_bash_history' \
    --exclude='sessions' \
    --exclude='.local' \
    --exclude='*.swp' \
    "$SOURCE/" "$TARGET/"
```

변경 범위를 검토한 뒤에만 실제 복사를 수행합니다.

```bash
rsync -av \
    --exclude='.cli_bash_history' \
    --exclude='sessions' \
    --exclude='.local' \
    --exclude='*.swp' \
    "$SOURCE/" "$TARGET/"
```

대상 경로에 쓰기 권한이 없는 경우에만 동일한 `rsync` 명령 앞에 `sudo`를 사용합니다. 복사 후 `kiro/manifests/kiro_files.txt`와 실제 대상 파일 범위를 대조합니다.

### 5-3. Kiro 실행 및 TODO 순차 처리

Kiro Skill 적용이 끝난 뒤 Kiro CLI를 실행합니다.

```bash
kiro-cli chat
```

Kiro CLI에서 Agent를 전환합니다.

```text
/agent swap system-engineer
```

이제 적용된 Agent·Skill을 사용해 TODO를 순서대로 실행합니다.

```text
USER_TODO.md를 읽고 미완료 TODO를 순서대로 실행합니다.
Kiro Agent·Skill이 $HOME/.kiro에 사전 적용되었는지 먼저 확인합니다.
각 단계 전에 현재 상태, 변경 범위, 롤백 방법을 출력합니다.
작업 후 검증 결과를 USER_TODO.md의 완료 기록에 반영합니다.
```

초기 적용과 검증이 끝난 뒤 Agent·Skill·Prompt 개선 작업을 지시합니다.

```text
UPDATE_TODO.md와 _reference/INDEX.md를 읽고 미완료 TODO를 순서대로 실행합니다.
외부 Agent·Skill 저장소는 라이선스, 보안, 유지보수 상태를 검토한 뒤 필요한 패턴만 반영합니다.
각 단계 후 검증 결과와 변경 파일을 UPDATE_TODO.md의 완료 기록에 반영합니다.
모든 TODO 완료 후 @skill-review를 실행합니다.
```

### 5-4. 사후 검증 및 롤백

- `$HOME/.kiro/agents/`에 `system-engineer.json`이 존재하는지 확인합니다.
- `$HOME/.kiro/skills/`와 `$HOME/.kiro/prompts/`의 파일 범위를 clone 저장소와 비교합니다.
- Markdown·JSON·Bash·Git 검증을 다시 실행합니다.
- 문제가 발생하면 사전 생성한 백업으로 `$HOME/.kiro`를 복원합니다.
- 원본 clone 저장소가 아닌 `$HOME/.kiro`만 로컬 실행 환경으로 변경합니다.

---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-09-04

© 2026 siasia86. Licensed under CC BY 4.0.
