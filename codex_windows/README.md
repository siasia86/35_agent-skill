# Codex Windows 개인 스킬

Linux에서 사용하던 **19개 skill 전체와 현재 저장소의 설정 원본 2개**를 Windows용으로 이관합니다. 스킬 이름·원문·예시·템플릿·체크리스트·동봉 역할·자료를 모두 유지하고 Windows 실행 절차와 도구를 별도로 제공합니다. 최적화는 전체 이관과 사용자 검증 이후 단계입니다.

## 1. 구성과 대응

- [전체 19개 대응표](skills/README.md): 모든 폴더와 Windows 사용 조건.
- [공통 지침과 설정](personal/README.md): 원본·Windows 예시·실제 적용 범위.
- [검증 실행](verification/README.md), [검토 결과](REVIEW.md), [남은 조건](ISSUE.md).
- [계획](PLAN.md), [현재 TODO](TODO.md), [이관 기록](../agent-workflows/codex/WINDOWS_MIGRATION_2026-10-03.md).
- [Linux 보존본](../codex_linux/README.md): 기존 실행 코드와 과거 관찰은 그대로 유지합니다.

활성 `skills/<이름>/SKILL.md`의 Windows 호환 절이 현재 실행 계약입니다. 그 밖의 Linux/Kiro 본문·예시도 삭제하지 않고 보존하되 OS별 명령은 현재 호환 절의 대응을 사용합니다. 각 폴더의 `references/linux-original.md`와 `references/kiro-original.md`는 비교 자료입니다. 동봉 역할 54개에도 Windows 절을 적용했습니다. 기존 Linux 소스 182개 파일은 [출처 manifest](verification/source_manifest.json)에서 활성 경로·보존 경로·SHA-256으로 모두 대응합니다.

## 2. 필요한 실행 도구

Windows 네이티브 기본은 PowerShell·Git·Python 3.11 이상입니다. Python 도구는 표준 라이브러리만 사용하며 `python -X utf8 -B`로 실행합니다. 실제 검증 환경과 범위는 REVIEW를 따릅니다. Bash 스킬은 Git Bash 또는 WSL의 Bash 역할을 그대로 유지합니다. Terraform·Docker·Ansible·보안 CLI는 해당 작업에 실제 필요한 환경에서만 확인합니다. Ansible controller·Linux 서비스 조작을 Windows PowerShell에서 직접 실행한다고 가정하지 않습니다. 이관 과정에서 이 도구들을 일괄 설치하지 않습니다.

## 3. 폴더 복사와 실제 적용

복사 단위는 **스킬 폴더 전체**입니다. 다른 개인 스킬·중앙 설치기·31 저장소가 없어도 필수 참조와 Python 도구가 폴더 안에서 해결됩니다. 개발 검증용 manifest는 설치 의존성이 아닙니다.

Codex의 개인 검색 위치는 사용자 홈의 `.agents/skills`, 저장소 검색 위치는 `.agents/skills`입니다. 같은 이름을 여러 범위에 설치하면 자동 병합되지 않으므로 기존 폴더의 출처·편집을 비교해 사용 대상을 정합니다. [공식 skill 검색 안내](https://learn.chatgpt.com/docs/build-skills)

아래는 저장소 루트에서 실행하는 수동 복사 예시입니다. 기존 동명 폴더는 덮어쓰지 않습니다. 실제 홈 적용은 현재 이관 결과와 별도로 검증합니다.

```powershell
$skillName = 'work-rules'
$skillSource = Join-Path (Get-Location) "codex_windows/skills/$skillName"
$skillRoot = Join-Path $HOME '.agents/skills'
$skillTarget = Join-Path $skillRoot $skillName
if (Test-Path -LiteralPath $skillTarget) {
    throw '기존 폴더를 비교·백업한 후 필요한 변경을 병합하세요.'
}
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse -ErrorAction Stop
```

모음에는 19개를 모두 유지합니다. 실제 설치 범위는 대상 작업공간에서 결정합니다. 저장소에 파일이 있다는 사실을 홈 설치·현재 세션 발견 완료로 보고하지 않습니다.

## 4. 게시 순서

검증한 변경을 yunli에 일반 commit·push하고 사용자가 검증합니다. 그 결과를 확인한 후 main에 반영·push합니다. 개인 홈 적용·설정 병합·release·운영 적용은 각각의 실제 요청·검증 범위로 기록합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
