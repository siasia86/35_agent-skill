---
name: git-commit-rule
description: Defines git commit message format and conventions. Use when committing changes — Korean description, type prefix, 50 chars max, no period.
---

# Git 커밋 메시지 규칙

<!-- CODEX-COMPAT-BEGIN -->
## Windows Codex 실행 및 적용 규칙

이 절과 이 절에서 연결한 실행 도구가 Windows의 현재 실행 본문입니다. 아래 Linux/Kiro 원문의 코드·명령·경로는 전체 보존한 비교 자료이며 그대로 자동 실행하지 않습니다. 원문의 목적·예시·체크리스트는 유지하되 플랫폼 차이와 교정 사항은 이 절의 실행 계약을 적용합니다. Linux 본문은 `codex_linux/`에 보존되어 있으며 이번 이식은 경량화·통합 작업이 아닙니다.

- 시스템·개발자·관리 정책과 실제 권한 안에서 **사용자 명시 지시 > 적용 저장소 AGENTS > 개인 스킬 기본값**을 적용합니다. 이미 부여된 범위와 승인을 유지하고 다른 저장소·개인 홈·시스템·운영 환경의 수정 권한을 경로 존재로 추정하지 않습니다.
- 실제 Git 루트·branch·기존 변경을 먼저 확인합니다. 필요한 본문·동봉 참조만 읽고 다른 스킬·전체 작업 기록을 자동 로드하지 않습니다. 원문의 `skill://`는 아래 로컬 참조로 해석하며 URI 도구를 호출하지 않습니다.
- 이 폴더를 통째로 복사하는 개인 스킬입니다. 필수 참조는 아래 상대 링크를 사용합니다. 중앙 catalog·설치기·다른 저장소 또는 형제 스킬 설치를 필수로 요구하지 않습니다. 원문 `references/kiro-original.md`는 비교 자료입니다.
- 네이티브 Windows 작업 셸은 PowerShell입니다. 파일 작업은 `-LiteralPath` 등 실제 대상 인자로 처리하며 셸 문자열·`eval`로 외부 입력을 재해석하지 않습니다. Python 3.11 이상을 `python -X utf8`로 실행하고 Python 하위 실행은 `[sys.executable, '-X', 'utf8', ...]` 인자 배열을 사용합니다. 실제 Python 위치·버전은 현재 환경에서 확인합니다.
- Bash 업무는 Git Bash 또는 승인된 WSL에서 유지합니다. PowerShell에서 Bash/POSIX 예제를 직접 실행하지 않습니다. 원문의 `/root`, `/var/log`, `/backup`, Kiro hook은 과거 환경 자료이며 Windows 개인 홈·시스템 경로로 자동 치환하지 않습니다.
- 검증은 **통과 / 부분 검사 / 실패 / 미실행**을 실행 목적·관찰·다음 조치와 함께 기록합니다. 경로 치환이나 과거 완료 기록을 현재 동작 통과로 사용하지 않습니다. 비공개 경로·계정·토큰·운영 자료를 공개 결과에 복사하지 않습니다.

### 현재 Windows commit·검증·게시 절차

한국어 type·50자·마침표 생략과 명시적 파일 staging은 아래 개인 메시지 규칙대로 유지합니다. 현재 저장소의 branch·메시지 규칙과 이미 부여된 사용자 게시 범위가 우선합니다. 과거 `/root/32_*`, `sj_del`, `yunli` 고정 checkout, 모든 main 금지 예시는 보존 비교 자료이며 다른 프로젝트의 규칙으로 자동 적용하지 않습니다.

```powershell
git -C $Repo rev-parse --show-toplevel
git -C $Repo branch --show-current
git -C $Repo status --short
# 변경 Markdown과 실제 설정에 맞춰 필요한 검사만 실행합니다.
python -X utf8 "$SkillDir/scripts/md-style-check.py" $Target
if ($LASTEXITCODE -ne 0) { throw 'Markdown style 검사 실패' }
python -X utf8 "$SkillDir/scripts/md-heading-check.py" $Target
if ($LASTEXITCODE -ne 0) { throw 'Markdown heading 검사 실패' }
python -X utf8 "$SkillDir/scripts/md-link-check.py" $Target
if ($LASTEXITCODE -ne 0) { throw 'Markdown link 검사 실패' }
# 실제 검토한 파일과 승인된 branch를 명시한 뒤 commit/push합니다.
git -C $Repo add -- '<검토한 파일 1>' '<검토한 파일 2>'
git -C $Repo diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'staged 검증 실패' }
git -C $Repo commit -m '<type>: <한국어 설명>'
if ($LASTEXITCODE -ne 0) { throw 'commit 실패' }
```

- 개인 공통 AGENTS와 대상 저장소의 현행 게시 기준을 확인합니다. 일반 개인 개발의 기본 작업·게시 브랜치는 `main`입니다. 필요한 검증·기록 후 검토한 담당 파일만 commit·일반 push하고 원격 SHA·commit 링크를 보고합니다. 이 완료 절차의 승인은 계속 적용하며 반복 사용자 확인을 요구하지 않습니다. 병렬 작업·격리·장기 실험에는 필요한 agent/task 브랜치·worktree를 사용하고 QA·Migration·복구 목적 브랜치와 upstream 읽기 전용 경계를 유지합니다. 작업 브랜치의 검증한 변경은 지정한 통합 대상에 반영하며 기존 브랜치를 자동 삭제하지 않습니다. 현재 사용자 제한과 원격 보호 규칙의 필수 PR·검사를 준수하며 우회하지 않습니다. 읽기 전용·변경 0건은 commit·push하지 않고 검증 실패·비밀값·다른 작업 변경은 게시하지 않습니다. force push·release·운영 적용은 별도 범위이며 게시 실패는 원인과 미게시 상태를 보고합니다. branch 전환 전 기존 변경·미병합 commit·refs를 확인하고 보존합니다. 원문의 고정 BASE를 현재 실제 대상 경로로 바꾸고 사용자 변경을 보존합니다.
- 원문의 `sia-md-*`, fix_table_align, trim_diagram 외부 도구의 존재를 가정하지 않고 repo 지정 검사기·버전·설정을 우선하며 지정이 없을 때 동봉 Python 검사와 직접 수정 후 재검사를 사용합니다. [STYLE.md](references/STYLE.md), [md-link-check](references/skills/md-link-check.md), [readme-template](references/skills/readme-template.md)은 필요한 항목만 읽습니다. Python 3.11+와 stdlib로 실행하며 선택 TOML 설정은 실제 대상에 있을 때만 적용합니다.
- 대상 경로가 실제 존재하는지 먼저 확인하고 missing target/빈 대상이 검증 완료로 보고되지 않는지 검사 결과 범위를 확인합니다. 코드/링크 검사 완료와 공개 문서 정책 통과를 구분합니다. 저장소가 푸터를 금지하면 style 검사에 `--no-footer`와 근거를 기록하며 다른 검사를 유지합니다. 외부 checker의 미구현 옵션을 주장하지 않습니다.
- 원격·추적 branch와 지정 게시 대상을 확인하고 일반 push 후 실제 원격 SHA를 대조합니다. 사용자에게 저장소·branch·commit 링크와 수행·검증·미실행을 보고합니다. 원격 게시 성공과 CI 결과는 구분하며 게시 실패는 원인·미게시 상태를 기록하고 완료로 표시하지 않습니다.
- 읽기 전용 Git 관리 영역은 권한을 바꾸지 않습니다. 승인된 별도 작업본이 필요하면 실제 사용자 변경과 refs를 보존하며 현재 범위에서 진행합니다. 공개 기록에는 개인 경로·계정·자격증명·raw TEMP 증거를 복사하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md).

### 호출·원본·기록

- 설치되어 현재 세션에 발견된 skill은 `$git-commit-rule 검증한 변경의 커밋 메시지를 작성해줘`처럼 명시해 호출합니다. 미설치 상태에서는 사용자가 지정한 실제 `SKILL.md` 경로를 읽어 이 Windows 기준을 적용합니다. 경로 조회나 메시지 작성 자체는 설치·commit·push 승인이 아닙니다.
- `_reference` 원본은 비교·출처 확인 자료이며 지원되는 skill 발견 위치나 설치 완료 표시가 아닙니다. 35 저장소 안에 이미 있는 배포 원본을 다시 clone하지 않고 지정된 원본 폴더를 사용합니다.
- 실제 작업 repo의 기존 관리 기록에 변경 범위·검증 근거·실제 commit과 게시 상태를 남깁니다. 사용자가 지정한 기존 관리·업데이트 기록 폴더가 있으면 재사용하고, 다른 repo에 35의 `agent-workflows` 경로를 강제하지 않습니다. 커밋 메시지는 기존 한국어 설명·type 접두사·50자 이내·마침표 없음 규칙을 유지합니다.
- 설치된 skill 교체는 이전 전체 폴더의 사본과 해시를 먼저 보존한 뒤 기존에 승인된 교체 범위에 따라 진행합니다. 동봉 참조·도구도 전체 폴더 단위로 함께 옮겨 서로 다른 버전을 섞지 않습니다.

<!-- CODEX-COMPAT-END -->


## 형식

```
<타입>: <설명>
```

## 타입

| 타입       | 용도                            |
|------------|---------------------------------|
| `docs`     | 문서 추가/수정                  |
| `fix`      | 오타, 깨진 링크, 버그 수정      |
| `feat`     | 새 기능 (Actions, 스크립트 등)  |
| `refactor` | 구조 변경 (디렉토리 이동/정리)  |
| `chore`    | 설정, 유지보수                  |
| `style`    | 포맷팅, 배지, 푸터 등 외형 변경 |

## 규칙
- 한글 설명 사용
- 50자 이내로 간결하게 작성
- 마침표 생략
- 여러 변경 시 가장 주요한 타입 사용

## 예시
```
docs: strace 가이드 추가
fix: README.md 디렉토리 경로 오타 수정
feat: GitHub Actions 날짜 자동 갱신 workflow 추가
refactor: 04/07 디렉토리 번호 swap
chore: .gitignore 업데이트
style: 전체 README 푸터 배지 통일
```

---

## Branch와 게시 기준

개인 공통 AGENTS와 위 Windows 완료 절차를 따릅니다. 기본은 `main`이며 필요한 agent 브랜치와 목적별 게시 경계를 유지합니다. 담당 파일만 staging하고 원격 commit·CI를 구분합니다. 원문 branch 표와 checkout 예시는 위 원문 비교 링크에서 보존합니다.
