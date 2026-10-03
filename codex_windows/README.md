# Codex Windows 개인 스킬

이 폴더는 Windows에서 복사하여 사용하는 19개 개인 skill과 선택적 공통 지침·설정 예시를 제공합니다.

## 1. 사용할 파일

- [skill 목록과 실행 조건](skills/README.md): `skills/<이름>/` 전체를 복사합니다.
- [공통 지침과 설정](personal/README.md): 기존 설정과 비교해 필요한 항목만 병합합니다.

활성 `SKILL.md`의 Windows 호환 절과 `scripts/`가 현재 실행 기준입니다. 각 폴더의 Linux/Kiro 원문·예시·체크리스트는 보존 자료이며 OS별 명령을 그대로 자동 실행하지 않습니다. 필요한 참조만 읽습니다.

## 2. 필요한 실행 도구

기본은 PowerShell·Git·Python 3.11 이상입니다. 동봉 Python 도구는 표준 라이브러리만 사용하며 `python -X utf8 -B`로 실행합니다. Bash 업무에는 확인한 Git Bash 또는 WSL을 사용합니다. Terraform·Docker·Ansible·보안 CLI는 해당 업무에 실제 필요한 경우에 확인합니다. Linux 서비스나 Ansible controller를 네이티브 PowerShell에서 실행한다고 가정하지 않습니다.

## 3. skill 폴더 복사

복사 단위는 **skill 폴더 전체**입니다. 동봉 참조와 helper가 각 폴더 안에 있으며 형제 skill·중앙 설치기·다른 저장소를 준비할 필요가 없습니다.

Codex의 사용자 범위와 저장소 범위 검색 위치는 각각 사용자 홈과 저장소의 `.agents/skills`입니다. 같은 이름의 skill이 여러 범위에 있으면 기존 출처·편집을 비교해 사용할 대상을 정합니다. [공식 skill 검색 안내](https://learn.chatgpt.com/docs/build-skills)

아래 예시는 현재 디렉터리가 이 `codex_windows` 폴더일 때 선택한 skill 한 개를 복사합니다. 기존 동명 폴더가 있으면 비교·백업 후 병합합니다.

```powershell
$skillName = 'work-rules'
$skillSource = Join-Path (Get-Location) "skills/$skillName"
$skillRoot = Join-Path $HOME '.agents/skills'
$skillTarget = Join-Path $skillRoot $skillName
if (-not (Test-Path -LiteralPath (Join-Path $skillSource 'SKILL.md') -PathType Leaf)) {
    throw 'codex_windows 폴더에서 skill 이름과 원본을 확인하세요.'
}
if (Test-Path -LiteralPath $skillTarget) {
    throw '기존 폴더를 비교·백업한 후 필요한 변경을 병합하세요.'
}
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse -ErrorAction Stop
```

복사 후 실제 Codex 새 세션에서 발견·선택·필요 도구 실행을 확인합니다. 공통 지침과 설정 예시는 선택적으로 적용하며 기존 사용자 설정을 일괄 교체하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
