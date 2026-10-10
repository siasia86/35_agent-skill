# Codex Windows 개인 스킬

이 폴더는 Windows 네이티브 개인 Codex에 복사하는 공통 지침·skill 21개·필수 동봉 도구·설정 예시의 배포 원본입니다. PowerShell·Git·Python을 기준으로 필요한 skill 폴더 전체를 선택합니다.

## 1. 사용할 파일

- [skill 목록](skills/README.md): 역할과 실행 조건을 확인합니다.
- [공통 지침](AGENTS.md): 기존 개인 AGENTS와 필요한 항목을 비교·병합합니다.
- [설정 적용 안내](personal/README.md): 예시와 실제 설정·세션 정책을 구분합니다.

`SKILL.md`는 현재 실행 지침입니다. 조건별 상세는 같은 폴더의 `references`, 실행 도구는 `scripts`, UI 메타데이터는 `agents/openai.yaml`에 있습니다. 각 폴더 안에서 필수 참조가 완결되며 형제 skill·중앙 설치기·다른 저장소를 준비할 필요가 없습니다.

개인 skill 적용 위치는 사용자 홈 `.agents/skills/<이름>/`, 공통 지침은 사용 중인 Codex home의 `AGENTS.md`입니다. 저장소별 skill은 해당 저장소의 `.agents/skills/<이름>/`에 적용합니다. 같은 이름의 기존 사본은 출처와 사용자 차이를 먼저 확인합니다.

개발 계획·검증 도구·결과·비교 원문은 이 배포 폴더에 포함하지 않습니다. 문서 역할·위치·양식·상태·게시 절차는 대상에 실제 적용된 지침을 따릅니다.

## 2. 실행 환경

기본 도구는 Windows PowerShell·Git·Python 3.11 이상입니다. 동봉 Python 도구는 표준 라이브러리만 사용하며 `python -X utf8 -B`로 실행합니다. 실제 도구 경로·버전·인코딩·종료 상태는 작업 환경에서 확인합니다.

Terraform·Docker·보안 CLI와 대상 언어의 시험 도구는 해당 업무에 필요한 경우에만 확인합니다. Windows에서 실행할 수 없는 기능은 지원 범위 밖으로 구분하고 다른 플랫폼의 명령을 이름만 바꾸어 실행하지 않습니다.

원격 Windows 업무의 SSH·ACL과 잠금·Python 설정은 work-rules의 해당 조건에서만 읽습니다. `--help` 성공은 실제 업무 실행이나 전체 동작 검증을 뜻하지 않습니다.

## 3. 폴더 복사와 갱신

복사 단위는 **skill 폴더 전체**입니다. 아래 예시는 이 codex_windows 폴더에서 기존 대상이 없을 때만 복사합니다.

```powershell
$skillName = 'work-rules'
$skillSource = Join-Path (Get-Location) "skills/$skillName"
$skillRoot = Join-Path $HOME '.agents/skills'
$skillTarget = Join-Path $skillRoot $skillName
if (-not (Test-Path -LiteralPath (Join-Path $skillSource 'SKILL.md') -PathType Leaf)) {
    throw 'codex_windows 폴더와 skill 이름을 확인하세요.'
}
if (Test-Path -LiteralPath $skillTarget) {
    throw '기존 폴더를 먼저 비교·백업하고 사용자 차이를 병합하세요.'
}
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse -ErrorAction Stop
```

갱신은 35 관리 원본 수정·검증 → 현재 설치된 관리 대상 반영 순서입니다. 기존 전체 폴더·사용자 추가 파일·해시·이전본을 먼저 보존합니다. 설정·권한·system/plugin skill은 별도 지정 범위를 따릅니다.

새 세션의 실제 발견·선택·도구 실행은 별도로 확인합니다. 파일 일치만으로 자동 선택이나 장기 행동의 성공을 보고하지 않습니다. 중앙 정책의 자동 배포·양방향 동기화는 현재 구성으로 가정하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-10

© 2026 siasia86. Licensed under CC BY 4.0.
