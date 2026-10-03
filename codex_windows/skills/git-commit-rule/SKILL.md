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

한국어 type·50자·마침표 생략과 명시적 파일 staging은 아래 원문 규칙대로 유지합니다. 현재 저장소의 branch·메시지 규칙과 이미 부여된 사용자 게시 범위가 우선합니다. 과거 `/root/32_*`, `sj_del`, `yunli` 고정 checkout, 모든 main 금지 예시는 보존 비교 자료이며 다른 프로젝트의 규칙으로 자동 적용하지 않습니다.

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

- 이 절을 읽는 것은 commit/push·checkout 승인이 아닙니다. 이미 승인된 commit·특정 branch 일반 push는 반복 승인 질문 없이 수행하며 보호 branch·force/amend·release는 실제 저장소와 현재 요청 범위를 확인합니다. 현재 branch를 임의로 yunli로 전환하지 않습니다. 원문의 고정 BASE를 현재 실제 대상 경로로 바꾸고 사용자 변경을 보존합니다.
- 원문의 `sia-md-*`, fix_table_align, trim_diagram 외부 도구 대신 동봉 Python 검사와 직접 수정 후 재검사를 사용합니다. [STYLE.md](references/STYLE.md), [md-link-check](references/skills/md-link-check.md), [readme-template](references/skills/readme-template.md)은 필요한 항목만 읽습니다. Python 3.11+와 stdlib로 실행하며 선택 TOML 설정은 실제 대상에 있을 때만 적용합니다.
- 대상 경로가 실제 존재하는지 먼저 확인하고 missing target/빈 대상이 검증 완료로 보고되지 않는지 검사 결과 범위를 확인합니다. 코드/링크 검사 완료와 공개 문서 정책 통과를 구분합니다. 저장소가 푸터를 금지하면 style 검사에 `--no-footer`와 근거를 기록하며 다른 검사를 유지합니다. 외부 checker의 미구현 옵션을 주장하지 않습니다.
- 원격·추적 branch·허용 push 목적을 확인하고 일반 push 후 실제 원격 commit을 확인합니다. 현재 저장소에 yunli→사용자 검증→main 흐름이 지정되어 있으면 그 순서를 유지하고 사용자 검증 전 main 게시를 하지 않습니다. 이 개인 스킬을 다른 저장소의 main 금지 규칙으로 일괄 적용하지 않습니다.
- 읽기 전용 Git 관리 영역은 권한을 바꾸지 않습니다. 승인된 별도 작업본이 필요하면 실제 사용자 변경과 refs를 보존하며 현재 범위에서 진행합니다. 공개 기록에는 개인 경로·계정·자격증명·raw TEMP 증거를 복사하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md).
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

## Branch 규칙

| 리포지토리                              | 사용 branch | 금지 branch       |
|-----------------------------------------|-------------|-------------------|
| `/root/32_system-engineering-resources` | `yunli`     | `main`, `kiro`    |
| `/root/sj_del`                          | `yunli`     | `main`, `kiro` 외 |

- commit/push 전 반드시 현재 branch 확인
- `main` branch push 절대 금지
- `git add .` 지양 — 변경 파일 명시적 지정

## Commit & Push 절차

작업 완료 후 아래 순서를 반드시 따릅니다.

```
1. branch 확인
   git -C <repo> branch --show-current
   → yunli 아니면: git -C <repo> checkout yunli

2. 변경 파일 확인
   git -C <repo> status --short
   → 의도치 않은 파일 포함 여부 검토

3. Markdown 검사 0건 확인 (변경 .md 파일에 한해)
   BASE=/root/32_system-engineering-resources
   sia-md-style-check <path>
   sia-md-heading-check <path>
   sia-md-link-check <path>

4. stage (명시적 파일 지정)
   git -C <repo> add <file1> <file2> ...

5. commit
   git -C <repo> commit -m "<type>: <한글 설명>"

6. push
   git -C <repo> push origin yunli

7. 결과 확인
   git -C <repo> log --oneline -3
```

## 금지 사항

```
git push origin main          ❌
git push origin HEAD          ❌ (현재 branch가 main일 경우)
git add .                     ❌ (비관련 파일 혼입 위험)
git commit --amend --no-edit  ❌ (push된 커밋은 amend 금지)
git push --force              ❌ (명시적 허가 없으면 금지)
```
