# Agent Skill 업데이트 TODO

Git clone 후 `35-agent-skill`의 참고 문서를 읽고, 현재 Agent·Skill·프롬프트를 점진적으로 고도화하기 위한 작업 목록입니다.

> 이 문서는 Agent에게 작업 순서와 완료 조건을 지시합니다. 미완료 항목을 실행하기 전에 현재 상태, 변경 범위, 롤백 방법을 출력합니다.

## 목차

| 섹션                                                          |
|---------------------------------------------------------------|
| [1. 실행 방법](#1-실행-방법) / [2. 안전 원칙](#2-안전-원칙)   |
| [3. TODO 목록](#3-todo-목록) / [4. 검증](#4-검증)             |
| [5. 롤백](#5-롤백) / [6. 완료 기록](#6-완료-기록)             |
| [7. 완료 후 Skill·Agent Review](#7-완료-후-skillagent-review) |

---

## 1. 실행 방법

저장소를 clone한 뒤 Kiro CLI에서 다음과 같이 지시합니다.

```bash
git clone <repository-url> <clone-path>
cd <clone-path>
kiro-cli chat
```

```text
UPDATE_TODO.md와 _reference/INDEX.md를 읽고 미완료 TODO를 순서대로 실행합니다.
각 단계 전에 현재 상태와 변경 범위, 롤백 방법을 출력합니다.
작업 후 검증 결과와 변경 파일을 완료 기록에 반영합니다.
```

작업 대상은 두 영역으로 구분합니다.

| 영역                         | 역할                         |
|------------------------------|------------------------------|
| clone 저장소의 `kiro/`       | 공개 Agent·Skill·Prompt 원본 |
| 현재 사용자의 `$HOME/.kiro/` | 실제 Kiro 실행 환경          |

## 2. 안전 원칙

- clone 저장소와 `$HOME/.kiro`를 혼동하지 않습니다.
- 작업 전에 `git status --short`와 기존 `$HOME/.kiro` 파일을 확인합니다.
- `$HOME/.kiro`를 덮어쓰기 전에 timestamp 백업을 생성합니다.
- 원본 저장소의 기존 사용자 변경 사항을 삭제하거나 `reset --hard`하지 않습니다.
- 실제로 존재하지 않는 script·설정 파일을 전제로 Skill 내용을 유지하지 않습니다.
- 존재하지 않는 파일 참조는 해당 경로·명령·필수 설정만 제거합니다.
- 일반적인 CI·Gitleaks 개념과 보안 원칙은 실제 파일이 없다는 이유로 삭제하지 않습니다.
- Agent·Skill 파일의 footer·통계는 로컬 Skill 정책에 맞게 정리하되, `readme-template/SKILL.md`의 정책 설명은 보존합니다.
- 시크릿, 토큰, 개인 설정, 세션 상태를 공개 저장소에 추가하지 않습니다.

## 3. TODO 목록

### 3-1. 현재 상태 확인

- [ ] `git status --short --branch`로 clone 저장소 상태 확인.
- [ ] `find "$HOME/.kiro" -maxdepth 3 -type f`로 현재 실행 환경 확인.
- [ ] `kiro/agents/`, `kiro/skills/`, `kiro/prompts/`, `kiro/markdown/`의 현재 파일 목록 확인.
- [ ] 기존 변경 사항과 새로 변경할 파일을 구분.
- [ ] `$HOME/.kiro` 백업 경로를 생성하고 기록.

```bash
REPO_ROOT="$(pwd)"
printf 'repo: %s\n' "$REPO_ROOT"
git status --short --branch
find "$HOME/.kiro" -maxdepth 3 -type f -print 2>/dev/null | sort
```

### 3-2. 참고 문서 읽기

- [ ] `_reference/INDEX.md`의 문서 목록과 권장 읽기 순서 확인.
- [ ] `_reference/32_system-engineering-resources/ref_kiro_setup_guide.md`로 현재 Kiro 구조와 Skill 작성 규칙 확인.
- [ ] `_reference/32_system-engineering-resources/ref_kiro_cli_command_reference.md`로 CLI·Agent·컨텍스트 명령어 확인.
- [ ] `_reference/32_system-engineering-resources/ref_ai_markdown_design_patterns.md`로 Agent·Skill 문서 구조 확인.
- [ ] `_reference/32_system-engineering-resources/ref_harness_engineering.md`와 `_reference/32_system-engineering-resources/ref_loop_engineering.md`로 검증 루프와 반복 개선 방식 확인.
- [ ] `_reference/32_system-engineering-resources/ref_ai_development_request_template.md`로 Agent 작업 지시 형식 확인.
- [ ] 실제 변경 대상과 연결된 공식 참고 문서를 추가 확인.

### 3-3. Skill 개선

- [ ] 현재 `kiro/skills/*/SKILL.md`와 `$HOME/.kiro/skills/*/SKILL.md`의 차이 확인.
- [ ] 중복·충돌·오래된 지시를 식별하고 변경 이유를 기록.
- [ ] Skill의 frontmatter, 적용 조건, 단계별 절차, 검증, 롤백을 명확히 작성.
- [ ] 실제 존재하지 않는 script·TOML·Gitleaks 설정을 참조하는 문장을 검색.
- [ ] 누락된 외부 파일의 경로·실행 명령·필수 설정만 제거.
- [ ] 일반 개념·보안 원칙·대체 가능한 실행 방법은 보존.
- [ ] Kiro Skill 문서의 footer·통계 블록은 제거하되 Skill 본문은 보존.
- [ ] 변경 후 재실행해도 결과가 반복되지 않는지 확인.

### 3-4. Agent·Prompt 개선

- [ ] `kiro/agents/*.json`의 역할, 권한 범위, 리소스 연결을 확인.
- [ ] Agent의 작업 범위와 금지 사항을 명확히 작성.
- [ ] `resources`의 `skill://` 경로가 실제 `kiro/skills/`에 존재하는지 확인.
- [ ] Prompt가 파일 변경 전에 상태 확인·영향 범위·롤백·검증을 요구하는지 확인.
- [ ] Agent 간 역할 중복과 우선순위 충돌을 정리.
- [ ] JSON 문법과 파일명·Agent 이름의 일관성을 검증.

### 3-5. 로컬 실행 환경 적용

- [ ] 변경한 clone 저장소 파일을 먼저 검증.
- [ ] `kiro/03_home-sjyun-kiro.sh`의 대상 경로와 `rsync` 제외 목록 확인.
- [ ] `$HOME/.kiro` 백업을 확인한 뒤 변경 사항을 적용.
- [ ] Kiro CLI에 접속하고 `/agent swap system-engineer`를 실행.
- [ ] 변경된 Skill이 실제 Agent 응답에 반영되는지 확인.
- [ ] 원본 clone 저장소와 `$HOME/.kiro`의 변경 범위를 비교.


### 3-6. 외부 Agent·Skill 저장소 조사 및 선별

- [ ] GitHub repository search와 GitHub API를 사용해 공개 Agent·Skill 저장소를 조사합니다.
- [ ] 검색 결과를 별 개수만으로 결정하지 않고 최근 활동일, 유지보수 상태, 라이선스, 보안 이슈, 문서 품질, 실제 Agent·Skill 구조를 함께 평가합니다.
- [ ] 다음 후보를 우선 조사합니다.
  - `addyosmani/agent-skills` — Agent·Skill 구성 및 웹 개발 작업 패턴.
  - `obra/superpowers` — 개발 작업용 Agent Skill·워크플로우 패턴.
  - `mattpocock/skills` — 재사용 가능한 개발 Skill 구성 패턴.
  - `anthropics/skills` — 공식 공개 Skill 구조와 문서화 패턴.
  - `github/awesome-copilot` — Agent·Prompt·Instruction 사례와 선별 기준.
- [ ] 후보 저장소를 `git clone --depth 1`로 임시 디렉터리에 받아 실행하지 않고 구조만 검토합니다.
- [ ] Agent, Skill, Prompt, Hook, script의 역할·의존성·권한 범위·외부 통신·시크릿 처리 여부를 확인합니다.
- [ ] 각 저장소의 license 파일, 저작권 고지, commit SHA, 조사일, 적용 범위를 기록합니다. 라이선스가 불명확한 자료는 복사하지 않습니다.
- [ ] 현재 `kiro/agents/`, `kiro/skills/`, `kiro/prompts/`와 비교해 중복·충돌·누락·불필요한 복잡성을 기록합니다.
- [ ] 보안·신뢰성·재현성·Kiro 호환성을 검토한 뒤 적용할 패턴만 선택합니다. 저장소 전체를 무조건 복사하지 않습니다.
- [ ] 선택한 개선 내용을 현재 저장소의 Agent·Skill·Prompt에 반영하고 원본 저장소 링크와 출처를 문서화합니다.
- [ ] 외부 저장소 코드를 실행하거나 `$HOME/.kiro`에 적용하기 전에 dry-run, 백업, 롤백, Markdown·JSON·Git 검증을 수행합니다.
- [ ] 외부 후보 조사 및 반영 후 `@skill-review`를 실행합니다.

## 4. 검증

clone 저장소 루트에서 실행합니다.

```bash
python3 scripts/temp-md-link-check.py USER_TODO.md
python3 scripts/temp-md-heading-check.py USER_TODO.md
python3 scripts/temp-md-style-check.py USER_TODO.md
python3 scripts/temp-md-link-check.py UPDATE_TODO.md
python3 scripts/temp-md-heading-check.py UPDATE_TODO.md
python3 scripts/temp-md-style-check.py UPDATE_TODO.md
python3 -m json.tool kiro/agents/system-engineer.json >/dev/null
git diff --check
git status --short
```

Skill·Agent 변경 후 추가로 확인합니다.

```bash
python3 scripts/temp-md-style-check.py kiro/skills/
python3 scripts/temp-md-heading-check.py kiro/skills/
python3 scripts/temp-md-link-check.py kiro/skills/
```

`$HOME/.kiro/skills/`에서는 footer가 로컬 Skill 정책에 따라 제거된 상태를 정상으로 처리합니다. 저장소의 일반 문서는 footer 검사 대상입니다.

검증 실패 시 TODO를 완료로 표시하지 않고 실패한 단계부터 수정·재검증합니다.

## 5. 롤백

로컬 실행 환경 적용 전 생성한 백업을 사용합니다.

```bash
sudo mv "$HOME/.kiro" "$HOME/.kiro.failed"
sudo mv "$HOME/.kiro.backup.YYYYMMDD_HHMMSS" "$HOME/.kiro"
```

clone 저장소 변경은 변경 파일을 먼저 확인한 뒤 해당 파일만 복원합니다. 다른 변경 사항을 포함할 수 있으므로 `git reset --hard`와 전체 삭제를 사용하지 않습니다.

## 6. 완료 기록

검증이 끝난 항목만 `[x]`로 변경합니다.

| 항목              | 상태 | 검증일     | 비고                        |
|-------------------|------|------------|-----------------------------|
| 상태 확인         | [ ]  | YYYY-MM-DD | clone·`$HOME/.kiro` 비교    |
| 참고 문서 확인    | [ ]  | YYYY-MM-DD | `_reference/INDEX.md` 기준  |
| Skill 개선        | [ ]  | YYYY-MM-DD | frontmatter·절차·검증 확인  |
| Agent·Prompt 개선 | [ ]  | YYYY-MM-DD | JSON·resource·역할 확인     |
| 로컬 적용         | [ ]  | YYYY-MM-DD | 백업·Agent 전환·동작 확인   |
| 최종 검증         | [ ]  | YYYY-MM-DD | Markdown·JSON·Git 검증 통과 |


## 7. 완료 후 Skill·Agent Review

모든 업데이트 TODO를 완료하고 검증이 통과했다고 판단하면 Agent에게 다음 리뷰를 지시합니다.

```text
@skill-review
```

리뷰 대상:

- 참고 문서와 현재 `kiro/skills/` 개선 내용의 일치 여부.
- Agent의 역할 분리, 권한 범위, `resources` 경로, Prompt 지시의 충돌 여부.
- Skill의 frontmatter, 적용 조건, 절차, 검증, 롤백의 완결성.
- 실제로 존재하지 않는 script·TOML·Gitleaks 설정을 참조하는 stale reference.
- `$HOME/.kiro/` 적용 결과와 clone 저장소의 원본 차이.
- 추가된 문서와 Python 검사 스크립트의 링크·헤딩·footer 처리.

`@skill-review`에서 지적된 항목은 관련 TODO를 다시 미완료로 변경하고 수정한 뒤, 검증과 리뷰를 반복합니다.

---

## 참고 자료

- [`_reference/INDEX.md`](_reference/INDEX.md) — Agent Skill 참고 문서 색인.
- [`USER_TODO.md`](USER_TODO.md) — 최초 Kiro Skill 적용 작업.
- [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) — Agent·Skill 사례 조사 대상. — ★★★☆☆
- [`obra/superpowers`](https://github.com/obra/superpowers) — 개발 Agent Skill 워크플로우 조사 대상. — ★★★☆☆
- [`mattpocock/skills`](https://github.com/mattpocock/skills) — 재사용 Skill 구성 조사 대상. — ★★★☆☆
- [`anthropics/skills`](https://github.com/anthropics/skills) — 공식 Skill 구조 조사 대상. — ★★★☆☆
- [`github/awesome-copilot`](https://github.com/github/awesome-copilot) — Agent·Prompt 사례 조사 대상. — ★★★☆☆

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
