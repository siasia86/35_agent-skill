# Windows Zircon 문서 대상과 검사

```powershell
# $TargetPath는 현재 요청에서 확인한 실제 저장소 경로입니다.
$Repo = git -C $TargetPath rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0) { throw '대상 Git 루트 확인 실패' }
git -C $Repo branch --show-current
if ($LASTEXITCODE -ne 0) { throw '브랜치 확인 실패' }
git -C $Repo status --short
if ($LASTEXITCODE -ne 0) { throw '기존 변경 확인 실패' }
```

실제 적용 지침이 지정한 문서만 선택하여 읽습니다. 폴더 이름이나 과거 정책의 푸터 금지 목록은 현행 정책 증거가 아닙니다. 기존 작성일·사용자 편집·운영 경로·작업 ID를 보존하고 문서 역할·상태 원본을 임의 이동하지 않습니다.

파일 작업은 PowerShell `-LiteralPath`·`Join-Path`·확인한 절대 경로를 사용합니다. 인코딩과 개행을 확인하며 Python 도구가 필요하면 실제 Python 3.11 이상을 `python -X utf8 -B`로 실행합니다. 입력 경로를 셸 코드로 재해석하거나 환경 변수의 개인 경로를 공개 문서에 복사하지 않습니다.

## 검사 선택

저장소가 지정한 검사기·버전·설정을 우선합니다. 지정이 없는 경우에만 실제 동봉한 `scripts/md-style-check.py`, `scripts/md-heading-check.py`, `scripts/md-link-check.py`와 `scripts/md_common.py`를 사용합니다. 도구 부재는 미실행으로 보고하며 형제 skill·중앙 저장소 설치를 자동 수행하지 않습니다.

```powershell
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-style-check.py') $Target
$StyleExit = $LASTEXITCODE
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-heading-check.py') $Target
$HeadingExit = $LASTEXITCODE
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-link-check.py') $Target
$LinkExit = $LASTEXITCODE
```

각 도구의 종료 코드·대상 파일 수·설정·제외를 기록합니다. 표현 검사는 표·문체·푸터, 헤딩 검사는 같은 파일 앵커·번호·레벨·중복·목차, 링크 검사는 내부 파일 존재 범위입니다. 다른 파일 앵커·reference-style 링크·외부 도달성은 별도 확인합니다. 실제 대상의 푸터 금지에는 표현 검사의 `--no-footer`와 근거를 기록하고 다른 검사는 유지합니다. 검사 통과를 위해 정책·검사기를 바꾸거나 임의 제외하지 않습니다.

정해진 검사·정형 추출·합의된 의미 불변 수정은 지원되는 `gpt-6-luna / medium`에 문서 묶음으로 배정하며 배정된 worker는 직접 수행하고 재위임하지 않습니다. 미지원이면 이유를 남기고 담당자가 승인 범위에서 직접 진행할 수 있습니다. 반환에는 실제 명령·모델·범위·개수·종료 코드·진단·수정 diff·미검사를 담고 소유 담당자가 완료를 판정합니다.

닫히지 않은 펜스·대상 0개·읽기 실패·필수 도구 부재·미실행을 통과로 기록하지 않습니다. 실패 증거를 보존하여 원인을 분석하고 새 근거에 따른 수정 후 영향 범위만 재검증합니다. 문서 검사 완료와 운영 기능 완료·Git 게시 완료는 구분합니다.
