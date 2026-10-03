---
name: zircon-readme-policy
description: Zircon 저장소 전용 Markdown 정책. 기존 규칙은 유지하고 푸터·통계만 금지합니다.
---

# Zircon README Policy

<!-- CODEX-COMPAT-BEGIN -->
## Codex Windows 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트를 전체 보존하며, 플랫폼·경로·권한 충돌과 Windows 직접 실행은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 원문 Zircon 절대 경로는 저장소 식별 예시입니다. 현재 작업이 그 저장소이거나 사용자/저장소 지침이 명시적으로 같은 예외를 채택한 경우에만 적용합니다. 일반 저장소 README에는 이 금지 목록을 적용하지 않습니다.
- 동봉 work-rules·STYLE·링크/헤딩 검사·Git·잠금 참조를 사용합니다. 별도의 전역 스킬 설치나 Kiro hook은 필요하지 않습니다. 푸터·통계 예외 이외의 문서 기준은 유지합니다.

로컬 워크플로 대응(필요한 항목만 읽음):

- `skill://git-commit-rule` → [git-commit-rule](references/skills/git-commit-rule.md).
- `skill://kiro-lock` → [kiro-lock](references/skills/kiro-lock.md).
- `skill://md-link-check` → [md-link-check](references/skills/md-link-check.md).
- `skill://readme-template` → [readme-template](references/skills/readme-template.md).
- `skill://work-rules` → [work-rules](references/skills/work-rules.md).

### Windows 네이티브 실행

이 Windows 활성본에서는 이 COMPAT 절의 실행 절차를 우선합니다. 아래 보존 본문의 POSIX 셸·`python3`·`/root/...`·Kiro 명령은 원문 비교 자료입니다. 원문의 목적·전체 체크리스트는 유지하고 Windows에서 실행할 때는 여기의 실제 도구·대상 확인 절차로 옮깁니다. 원문 예시를 PowerShell에 그대로 붙여 넣거나 이미 설치·검증된 결과로 취급하지 않습니다.

- 실제 Git 루트·현재 변경·해당 저장소 지침을 확인하고 현재 작업에 필요한 자료만 읽습니다. 다른 저장소 profile이나 30/31 관리 자료를 필수 의존성으로 삼지 않습니다. 이미 적용된 저장소 지침은 그 적용 범위 안에서 유지합니다.
- PowerShell에서 실제 Python 3.11 이상을 확인합니다. `Get-Command python`과 `python -X utf8 -B --version`을 사용하며 `python3` 별칭·WSL·pip 설치를 가정하지 않습니다. 존재하지 않으면 설치/환경 확인이 필요한 미실행으로 보고합니다.
- 파일 작업은 실제 Windows 절대 경로와 `-LiteralPath`를 사용합니다. 공백·한글 경로는 인수로 따로 전달하고, UTF-8 입출력을 명시합니다. 경로 값에 셸 코드를 결합하지 않습니다. 예시의 `$SkillDir`·`$Target`은 실제 확인한 폴더/파일로 지정하며 `$HOME`·`$CODEX_HOME`을 재할당하지 않습니다.
- 실행 스크립트가 동봉된 스킬은 이 폴더 안의 사본을 사용합니다. 세 Markdown 검사기가 동봉된 경우 `scripts/md_common.py`도 같은 폴더에 있어야 합니다. 스크립트가 없는 스킬에 실행 도구가 구현됐다고 가정하지 않습니다. 폴더 전체 복사 외 별도 중앙 설치·전역 alias가 필요하지 않습니다.
- PowerShell 문법 검사·Python AST 검사는 실제 프로그램 실행 결과와 구분합니다. 현재 대상·실행 도구·제외 설정·종료 코드를 기록하고 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다.

문서 스타일은 동봉 [STYLE.md](references/STYLE.md)를 사용합니다. `sia-md-*` 대신 동봉 스크립트를 Python 3.11 이상으로 실행합니다. 기본 OS/언어 runtime 외 pip·다른 저장소 설치는 필요하지 않습니다. 대상 저장소의 선택적 TOML 설정은 실제 존재할 때만 적용합니다.

```powershell
$SkillDir = 'C:\work\skills\zircon-readme-policy'  # 실제 복사된 해당 스킬 폴더
$Target = 'C:\work\repo\README.md'  # 현재 요청의 실제 대상
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-style-check.py') $Target
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-heading-check.py') $Target
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-link-check.py') $Target
```

각 호출 직후 `$LASTEXITCODE`를 확인합니다. 앞 명령이 실패한 결과를 마지막 호출의 성공으로 덮어 해석하지 않습니다. 명시한 미존재 입력은 종료 코드 `1`이며 유효 파일과 혼합돼도 실패입니다. 빈 디렉토리·설정상 제외된 파일은 실제 검사 수와 제외 이유를 함께 보고합니다.

파일 검사기는 inline Markdown 링크의 각괄호 목적지·공백·균형 괄호·URL 인코딩 경로를 처리합니다. reference-style 링크·네트워크 URL·다른 파일 내부 앵커는 별도 범위이며 모두 통과했다고 확장하지 않습니다. 같은 파일 헤딩 앵커는 실제 등장 순서의 중복 suffix를 확인하고, 중복 헤딩 정책 검사와 앵커 존재 검사를 구분합니다. 인용구·backtick·tilde 펜스의 예시는 코드로 제외합니다. 닫히지 않은 펜스가 있으면 링크 검사 종료 코드 `2`를 미완료로 보고합니다.


`<SKILL_DIR>`는 현재 복사된 스킬 폴더입니다. 원문의 fix_table_align/trim_diagram 외부 자동 수정기를 필수로 호출하지 않고, 보고된 표/다이어그램을 현재 파일에서 직접 수정한 뒤 다시 검사합니다. 외부 스크립트의 모든 옵션이 구현됐다고 주장하지 않습니다.

저장소 지침이 푸터·날짜·배지를 금지하면 style 검사에 `--no-footer`를 사용하고 그 적용 근거와 제외 범위를 기록합니다. 다른 검사는 계속 실행합니다. 정책상 금지된 푸터를 검사 통과 목적으로 추가하거나 그 결과를 미해결 오류로 취급하지 않습니다. 실제 내용 결함을 숨기기 위한 임의 skip은 하지 않습니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 적용 범위

이 정책은 다음 저장소 하위에만 적용합니다.

```text
/root/22_github_private/11_zircon/**
```

## 기존 규칙

이 저장소에도 다음 기존 규칙을 계속 적용합니다.

- `work-rules`
- `STYLE.md`
- Markdown H1/H2 번호 규칙
- 목차 및 앵커 링크 검증
- 표 정렬 규칙
- Markdown 링크 검사
- Git 커밋 규칙
- 저장소 잠금 규칙

## 저장소 전용 예외

이 저장소 하위의 모든 Markdown 문서에는 다음 항목을 추가하지 않습니다.

- 통계 섹션
- GitHub stars 배지
- GitHub forks 배지
- GitHub watchers 배지
- GitHub last commit 배지
- License 배지
- Actions 배지
- 작성일
- 마지막 업데이트
- 저작권 푸터

이 규칙은 전역 `readme-template` 규칙 중 푸터·통계 항목에만 적용되는 저장소 범위 예외입니다. 다른 저장소의 Markdown 문서에는 전역 `readme-template` 규칙을 그대로 적용합니다.
