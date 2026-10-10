# Windows Git 게시 절차

아래 변수는 사용자 요청에서 확인한 실제 대상입니다. 예시 문자열을 그대로 사용하지 않습니다. PowerShell 파일 작업은 확인한 절대 경로와 `-LiteralPath`·`Join-Path`를 사용하고 경로에 셸 코드를 결합하지 않습니다.

```powershell
git -C $Repo rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0) { throw 'Git 루트 확인 실패' }
git -C $Repo branch --show-current
if ($LASTEXITCODE -ne 0) { throw '브랜치 확인 실패' }
git -C $Repo status --short
if ($LASTEXITCODE -ne 0) { throw '기존 변경 확인 실패' }
```

## Markdown 변경 검사

저장소가 지정한 검사기·버전·설정을 우선합니다. 지정이 없으면 폴더에 실제 존재하는 동봉 도구를 Python 3.11 이상으로 실행합니다. 실행 전 `Get-Command python`과 `python -X utf8 -B --version`으로 실제 런타임을 확인하고 없는 도구는 미실행으로 기록합니다. WindowsApps 별칭을 설치 완료로 간주하지 않습니다.

```powershell
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-style-check.py') $Target
if ($LASTEXITCODE -ne 0) { throw '문서 표현 검사 실패 또는 미완료' }
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-heading-check.py') $Target
if ($LASTEXITCODE -ne 0) { throw '헤딩 검사 실패 또는 미완료' }
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-link-check.py') $Target
if ($LASTEXITCODE -ne 0) { throw '파일 링크 검사 실패 또는 미완료' }
```

`scripts/md_common.py`를 포함한 도구 묶음을 같은 폴더에 유지합니다. 표현 검사는 표·문체·푸터, 헤딩 검사는 같은 파일 앵커·번호·레벨·중복·목차, 링크 검사는 내부 파일 존재 범위입니다. 다른 파일의 앵커와 외부 도달성은 별도로 확인합니다. 대상 0개·필수 도구 부재·미실행은 통과가 아닙니다. 정책상 푸터가 금지되면 실제 지원하는 `--no-footer`를 표현 검사에 적용하고 근거를 남기며 다른 검사는 유지합니다. 검사 통과를 위해 금지된 푸터를 추가하지 않습니다.

정해진 검사·정형 결과 추출·확정된 의미 불변 수정은 소유 담당자가 지원되는 `gpt-6-luna / medium`에 문서 묶음으로 배정합니다. 이미 배정된 worker는 직접 실행하고 재위임하지 않습니다. 미지원이면 이유를 기록하고 담당자가 승인 범위에서 직접 실행하며 모델·config를 자동 변경하지 않습니다. 의미·상태·권한 판단과 게시 권한은 소유 담당자와 통합 담당자에게 유지됩니다.

## 담당 파일 staging

```powershell
git -C $Repo add -- '<검토한 담당 파일 1>' '<검토한 담당 파일 2>'
if ($LASTEXITCODE -ne 0) { throw 'staging 실패' }
git -C $Repo diff --cached --name-only
if ($LASTEXITCODE -ne 0) { throw 'staged 파일 확인 실패' }
git -C $Repo diff --cached
if ($LASTEXITCODE -ne 0) { throw 'staged 내용 확인 실패' }
git -C $Repo diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'staged 공백 검사 실패' }
git -C $Repo commit -m '<type>: <한국어 설명>'
if ($LASTEXITCODE -ne 0) { throw 'commit 실패' }
```

이미 staging된 다른 작업이 있으면 그대로 commit하지 않고 기존 index·사용자 변경을 보존하는 분리 방법을 선택합니다. 변경 0건이면 commit하지 않습니다. 읽기 전용 Git 관리 영역의 ACL을 바꾸지 않습니다.

## 일반 push와 원격 대조

실제 remote·추적 브랜치·지정 게시 대상을 먼저 확인합니다. 아래 `$Remote`·`$Branch`는 확인한 값이며 보호 규칙이 PR을 요구하면 해당 경로를 사용합니다.

```powershell
git -C $Repo remote -v
git -C $Repo rev-parse HEAD
if ($LASTEXITCODE -ne 0) { throw '로컬 SHA 확인 실패' }
git -C $Repo push $Remote $Branch
if ($LASTEXITCODE -ne 0) { throw '일반 push 실패' }
git -C $Repo ls-remote $Remote ('refs/heads/' + $Branch)
if ($LASTEXITCODE -ne 0) { throw '원격 SHA 조회 실패' }
```

push 응답만으로 동일 SHA를 주장하지 않고 조회한 원격 SHA와 로컬 SHA를 비교합니다. 실제 저장소·브랜치·commit 링크·검증 결과·CI 상태를 기록합니다. 개인 설정·계정·비공개 경로는 공개 기록에서 제외합니다.
