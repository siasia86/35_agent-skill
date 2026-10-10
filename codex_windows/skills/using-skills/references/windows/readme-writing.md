# README 작성과 양식 적용

README의 역할이 탐색용 인덱스인지 사용 안내인지 대상 지침에서 확인합니다. PLAN·TODO·ISSUE·검증 기록을 README로 합치거나 기존 원본을 이동하지 않습니다. 기존 관리 기록의 링크로 연결하고 상태 원본은 지정 문서에 유지합니다.

아래는 양식이 지정되지 않았을 때 필요한 절만 골라 쓰는 골격입니다. 빈 절을 일괄 생성하지 않습니다. 푸터·배지·날짜·라이선스는 실제 대상에서 채택한 값과 형식이 있을 때만 추가합니다.

```markdown
# 프로젝트 이름

프로젝트의 목적과 사용 대상을 간결하게 설명합니다.

## 시작하기

현재 지원하는 실행 환경·선행 조건·검증한 실행 방법을 적습니다.

## 사용 방법

실제 사용자가 수행할 순서와 예상 결과를 적습니다.

## 문서 안내

관리 문서와 상세 안내를 실제 존재하는 상대 링크로 연결합니다.

## 확인된 제한

현재 근거가 있는 제한과 미확인 항목만 적습니다.
```

PowerShell 예시는 Windows에서 실제 실행 가능한 명령과 확인한 경로를 사용합니다. Python 예시에는 `python -X utf8 -B`를 사용하고 필요한 런타임을 실제 확인합니다. 변수 값에 셸 코드를 합치지 않습니다. 파일 읽기·쓰기의 인코딩과 기존 개행을 보존합니다.

## 검사와 마감

저장소가 지정한 검사기·설정이 없을 때 아래 동봉 도구를 사용합니다. `$SkillDir`·`$Target`은 확인한 실제 폴더·대상입니다.

```powershell
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-style-check.py') $Target
$StyleExit = $LASTEXITCODE
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-heading-check.py') $Target
$HeadingExit = $LASTEXITCODE
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-link-check.py') $Target
$LinkExit = $LASTEXITCODE
```

각 결과를 따로 기록합니다. 푸터가 금지된 대상은 표현 검사의 실제 지원 옵션 `--no-footer`를 적용하고 근거를 남깁니다. 내부 파일 링크·같은 파일 앵커·표현 검사의 범위를 각각 확인하고 다른 파일 앵커·외부 도달성을 별도로 대조합니다. 검사 0건·도구 부재·읽기 실패·닫히지 않은 코드 펜스는 완료로 처리하지 않습니다. 도구의 기본 제외와 TOML 설정 적용을 기록하며 검사 통과를 위해 정책이나 검사기를 바꾸지 않습니다.

게시가 요청·승인된 작업은 실제 대상의 게시 규칙에 따라 검토한 담당 파일만 commit·일반 push하고 원격 SHA와 CI를 구분합니다. 읽기 전용·초안만 요청된 작업은 그 범위를 유지합니다. 개인 경로·계정·자격증명·전체 설정·운영 자료를 공개 README에 복사하지 않습니다.
