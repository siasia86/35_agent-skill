---
name: git-commit-rule
description: Defines git commit message format and conventions. Use when committing changes — Korean description, type prefix, 50 chars max, no period.
---

# Git 커밋 메시지 규칙

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 한국어 type 형식·50자·마침표 생략·변경 파일 명시 staging을 유지하되, 적용 저장소가 지정한 메시지/branch 규칙이 우선합니다. 원문의 32/sj_del·yunli는 해당 환경의 기본값입니다. 다른 저장소를 yunli로 강제 checkout하지 않습니다.
- 현재 저장소·원격·branch·승인된 게시 범위와 사용자 변경을 확인합니다. commit 요청은 별도 원격 push 권한을 자동 포함하지 않습니다. 이미 특정 branch push까지 승인되었다면 반복 확인하지 않습니다. 보호 브랜치·force/amend는 현재 저장소와 승인 범위에서 판단합니다.
- 원문 명령의 BASE 고정 경로는 현재 대상 경로로 대체하며 Markdown 검사는 동봉 스크립트로 실행할 수 있습니다. 읽기 전용 Git 관리 영역은 권한을 바꾸지 않고 승인 범위 안의 별도 작업본에서 게시합니다.

로컬 워크플로 대응(필요한 항목만 읽음):

- `skill://md-link-check` → [md-link-check](references/skills/md-link-check.md).

문서 스타일은 동봉 [STYLE.md](references/STYLE.md)를 사용합니다. `sia-md-*` 대신 동봉 스크립트를 Python 3.11 이상으로 실행합니다. 기본 OS/언어 runtime 외 pip·다른 저장소 설치는 필요하지 않습니다. 대상 저장소의 선택적 TOML 설정은 실제 존재할 때만 적용합니다.

- `python3 <SKILL_DIR>/scripts/md-style-check.py <target>`
- `python3 <SKILL_DIR>/scripts/md-heading-check.py <target>`
- `python3 <SKILL_DIR>/scripts/md-link-check.py <target>`

`<SKILL_DIR>`는 현재 복사된 스킬 폴더입니다. 원문의 fix_table_align/trim_diagram 외부 자동 수정기를 필수로 호출하지 않고, 보고된 표/다이어그램을 현재 파일에서 직접 수정한 뒤 다시 검사합니다. 외부 스크립트의 모든 옵션이 구현됐다고 주장하지 않습니다.

저장소 지침이 푸터·날짜·배지를 금지하면 style 검사에 `--no-footer`를 사용하고 그 적용 근거와 제외 범위를 기록합니다. 다른 검사는 계속 실행합니다. 정책상 금지된 푸터를 검사 통과 목적으로 추가하거나 그 결과를 미해결 오류로 취급하지 않습니다. 실제 내용 결함을 숨기기 위한 임의 skip은 하지 않습니다.

- 동봉 STYLE §12의 `readme-template` 참조는 [전체 readme-template 지침](references/skills/readme-template.md)으로 해석합니다. 대상 문서에 적용할 개인 푸터 기본값·원문 예외와 사용자/저장소의 상위 지침을 함께 확인하며, 형제 스킬 설치를 요구하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
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
