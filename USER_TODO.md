# USER TODO

`35_agent-skill`을 clone한 사용자가 Kiro Agent에게 로컬 적용 작업을 지시할 때 사용하는 작업 목록입니다.

> 이 문서를 읽은 Agent는 미완료 TODO를 순서대로 확인합니다. 파일 변경이나 삭제 전에 현재 상태, 변경 범위, 롤백 방법을 먼저 제시합니다.

## 목차

| 섹션                                                              |
|-------------------------------------------------------------------|
| [1. 사용 방법](#1-사용-방법) / [2. 작업 전 조건](#2-작업-전-조건) |
| [3. TODO 목록](#3-todo-목록) / [4. 검증](#4-검증)                 |
| [5. 롤백](#5-롤백) / [6. 완료 기록](#6-완료-기록)                 |
| [7. 완료 후 Skill Review](#7-완료-후-skill-review)                |

---

## 1. 사용 방법

저장소를 clone한 뒤 Kiro Agent에게 다음과 같이 지시합니다.

```text
USER_TODO.md를 읽고 미완료 TODO를 순서대로 실행합니다.
각 단계 전에 현재 상태와 변경 범위를 확인하고, 삭제 또는 덮어쓰기 작업에는 롤백 방법을 제시합니다.
작업 후 검증 결과를 USER_TODO.md의 완료 기록에 반영합니다.
```

기본 작업 순서는 다음과 같습니다.

1. 저장소와 대상 경로의 현재 상태 확인.
2. Kiro 파일 적용 명령의 `dry-run` 결과 확인.
3. Kiro Agent를 `system-engineer`로 전환.
4. 로컬 실행 환경에만 필요한 문서 정리.
5. Skill 내 누락 파일 참조 정리.
6. 검증 및 완료 기록 작성.

## 2. 작업 전 조건

- clone 원본 경로와 현재 사용자 로컬 대상 `$HOME/.kiro`를 구분합니다.
- 원본 저장소의 파일은 로컬 정리 작업 때문에 삭제하거나 수정하지 않습니다.
- 기존 Git 변경 사항과 미추적 파일을 먼저 확인하고 보존합니다.
- `$HOME/.kiro`를 덮어쓰기 전에 timestamp 백업을 생성합니다.
- `kiro/03_home-sjyun-kiro.sh`는 현재 `rsync -n`을 포함한 미리보기 명령을 출력하므로, 출력 결과를 실제 적용 명령으로 오인하지 않습니다.
- 삭제 대상이 없으면 오류로 처리하지 않고 `skip`으로 기록합니다.

## 3. TODO 목록

### 3-1. Kiro Agent Skill 파일 적용

- [ ] clone 경로와 Git 상태 확인.
- [ ] `kiro/03_home-sjyun-kiro.sh` 실행 후 출력된 `rsync` 대상과 제외 목록 확인.
- [ ] 현재 사용자의 `$HOME/.kiro` 기존 내용을 백업.
- [ ] 검토한 명령으로 Kiro 파일을 적용.
- [ ] 적용 후 대상 파일과 `kiro/manifests/kiro_files.txt`의 범위를 비교.

```bash
cd "$(git rev-parse --show-toplevel)"
sudo bash kiro/03_home-sjyun-kiro.sh
```

### 3-2. Kiro Agent 전환

- [ ] Kiro CLI에 접속.
- [ ] `system-engineer` Agent가 정상적으로 로드되는지 확인.
- [ ] 현재 Agent를 `system-engineer`로 전환.

```bash
kiro-cli chat
```

Kiro CLI에서 실행합니다.

```text
/agent swap system-engineer
```

### 3-3. 현재 사용자 Kiro Skill 정리

- [ ] 현재 로그인한 사용자의 `$HOME` 경로 확인.
- [ ] `$HOME/.kiro/skills/` 아래 `*.md` 파일 목록 확인.
- [ ] README 푸터·통계 배지 블록이 포함된 파일과 줄을 먼저 출력.
- [ ] `$HOME/.kiro` 전체를 timestamp 백업.
- [ ] Agent에게 지정한 footer 블록만 제거하도록 지시.
- [ ] YAML frontmatter, Skill 본문, 코드 블록, 운영 규칙은 보존.
- [ ] `readme-template/SKILL.md`의 footer 템플릿 정책 설명은 보존.
- [ ] 변경 후 대상 파일과 남은 footer 패턴을 다시 확인.
- [ ] 원본 clone 디렉터리의 파일이 변경되지 않았는지 확인.

Agent에게 다음처럼 지시합니다.

```text
현재 로그인한 사용자의 `$HOME/.kiro/skills/` 아래 Markdown 파일을 확인합니다.

1. 대상 파일 목록과 README footer·통계 블록 위치를 먼저 출력합니다.
2. 다음으로 구성된 footer 블록만 제거합니다.
   - `## 통계`
   - GitHub badge
   - `작성일`
   - `마지막 업데이트`
   - 저작권 문구
3. 일반 본문에 포함된 통계 설명은 삭제하지 않습니다.
4. YAML frontmatter, Skill 본문, 코드 블록, 운영 규칙은 보존합니다.
5. `readme-template/SKILL.md`의 footer 템플릿 정책 설명은 보존합니다.
6. `$HOME/.kiro`를 timestamp 백업한 뒤 변경합니다.
7. 변경 결과, 백업 경로, 남은 footer 패턴을 보고합니다.
8. 원본 clone 디렉터리는 수정하지 않습니다.
```

🟡 `통계`라는 단어가 포함된 모든 문장을 삭제하지 않습니다. `## 통계`, 배지, 날짜, 저작권으로 구성된 정확한 footer 블록만 처리합니다.

### 3-4. Skill 내 누락 파일 참조 정리

- [ ] 저장소 검증용 파일과 로컬 Kiro Skill 내용을 구분.
- [ ] 현재 사용자의 `$HOME/.kiro/skills/**/*.md`에서 외부 script·설정 파일 참조를 확인.
- [ ] `.github/`, Gitleaks 설정, CI 전용 `*.toml` 및 관련 script의 실제 존재 여부를 확인.
- [ ] 대상 파일이 존재하면 목록과 용도를 출력하고 해당 Skill 참조를 유지.
- [ ] 대상 파일이 존재하지 않으면 Skill 내용에서 해당 파일 경로·실행 명령·필수 설정 참조를 삭제.
- [ ] 일반적인 CI·Gitleaks 개념 설명이나 보안 원칙까지 일괄 삭제하지 않음.
- [ ] CI 전용이 아닌 일반 TOML 설정이나 실제 존재하는 파일의 참조는 삭제하지 않음.
- [ ] 변경 전 `$HOME/.kiro` 백업과 롤백 경로를 확인.
- [ ] 변경 후 누락 파일 참조가 남아 있지 않은지 검증.
- [ ] 원본 clone 저장소의 파일은 수정하거나 삭제하지 않음.

Agent에게 다음처럼 지시합니다.

```text
현재 사용자의 `$HOME/.kiro/skills/` 아래 Markdown Skill 내용을 확인합니다.

확인 대상:
  - `.github/` 경로 참조
  - Gitleaks 설정 파일 참조
  - CI 전용 `*.toml` 참조
  - Skill이 실행하도록 안내하는 외부 script 경로와 명령

1. 각 참조의 실제 파일 존재 여부와 참조 위치를 먼저 출력합니다.
2. 참조 대상 파일이 실제로 존재하면 파일 목록과 용도를 보고하고 Skill 참조를 유지합니다.
3. 참조 대상 파일이 존재하지 않으면 Skill 내용에서 해당 파일 경로,
   실행 명령, 필수 설정 등 누락된 리소스에 의존하는 부분을 삭제합니다.
4. 일반적인 CI·Gitleaks 개념, 보안 원칙, 실제 존재하는 파일의 참조는 삭제하지 않습니다.
5. 변경 전 `$HOME/.kiro`를 timestamp 백업합니다.
6. 변경 후 누락 파일 참조 검색 결과와 롤백 백업 경로를 보고합니다.
7. 원본 clone 저장소는 수정하거나 삭제하지 않습니다.
```

## 4. 검증

작업 완료 후 다음 검증을 수행합니다.

```bash
cd "$(git rev-parse --show-toplevel)"
bash -n kiro/03_home-sjyun-kiro.sh
git diff --check
python3 scripts/temp-md-link-check.py USER_TODO.md
python3 scripts/temp-md-heading-check.py USER_TODO.md
python3 scripts/temp-md-style-check.py USER_TODO.md
git status --short
```

검증 실패 시 TODO를 완료로 표시하지 않고 원인을 수정한 뒤 실패한 검증부터 다시 실행합니다.

## 5. 롤백

로컬 Kiro 적용 전에 생성한 백업을 사용합니다.

```bash
sudo cp -a "$HOME/.kiro" \
    "$HOME/.kiro.backup.$(date +%Y%m%d_%H%M%S)"
```

적용 후 문제가 발생하면 대상 경로를 백업으로 복원합니다. 실제 백업 경로를 확인한 뒤 실행합니다.

```bash
sudo mv "$HOME/.kiro" "$HOME/.kiro.failed"
sudo mv "$HOME/.kiro.backup.YYYYMMDD_HHMMSS" "$HOME/.kiro"
```

저장소 원본에 대한 삭제나 강제 초기화로 롤백하지 않습니다. 다른 사용자의 변경 사항을 덮어쓸 수 있기 때문입니다.

## 6. 완료 기록

각 TODO는 검증이 끝난 뒤에만 `[x]`로 변경합니다.

| 항목       | 상태 | 검증일     | 비고                        |
|------------|------|------------|-----------------------------|
| Kiro 적용  | [ ]  | YYYY-MM-DD | 대상 경로와 manifest 대조   |
| Agent 전환 | [ ]  | YYYY-MM-DD | `system-engineer` 로드 확인 |
| 문서 정리  | [ ]  | YYYY-MM-DD | dry-run 및 원본 보존 확인   |
| 파일 정리  | [ ]  | YYYY-MM-DD | allowlist 및 롤백 확인      |
| 최종 검증  | [ ]  | YYYY-MM-DD | 전체 검증 명령 통과         |


## 7. 완료 후 Skill Review

모든 TODO 항목을 완료하고 최종 검증이 통과했다고 판단하면 Agent에게 다음 리뷰를 지시합니다.

```text
@skill-review
```

리뷰 대상:

- `kiro/skills/`의 Skill 구조, 적용 조건, 중복, 충돌, 누락된 검증.
- `kiro/agents/`의 역할, 권한 범위, `resources` 연결, JSON 문법.
- `kiro/prompts/`의 작업 지시와 실제 파일 구조의 일치 여부.
- `$HOME/.kiro/` 적용 결과와 clone 저장소 원본의 차이.
- 존재하지 않는 script·TOML·Gitleaks 설정 참조와 stale reference.
- footer·통계 제거 범위가 Skill 정책과 일치하는지 여부.

`@skill-review`에서 지적된 항목은 TODO를 다시 미완료로 변경하고 수정한 뒤, 관련 검증과 리뷰를 반복합니다.

---

## 통계

![GitHub stars](https://img.shields.io/github/stars/siasia86/system-engineering-resources?style=social)
![GitHub forks](https://img.shields.io/github/forks/siasia86/system-engineering-resources?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/siasia86/system-engineering-resources?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/siasia86/system-engineering-resources)
![License](https://img.shields.io/github/license/siasia86/system-engineering-resources)
![Actions](https://img.shields.io/github/actions/workflow/status/siasia86/system-engineering-resources/update-date.yml)

---

**작성일**: 2026-09-04

**마지막 업데이트**: 2026-09-04

© 2026 siasia86. Licensed under CC BY 4.0.
