# Windows Markdown 검사 실행

실제 Python 위치·버전과 도구·대상 존재를 확인합니다. PowerShell cmdlet 오류와 네이티브 CLI 종료 코드를 구분합니다. 파일 경로는 확인한 절대 경로를 인수로 따로 전달하고 `-LiteralPath`·`Join-Path`를 사용합니다. `$HOME`·`$CODEX_HOME`을 재할당하거나 경로 값을 셸 코드로 재해석하지 않습니다.

```powershell
Get-Command python
python -X utf8 -B --version
if ($LASTEXITCODE -ne 0) { throw 'Python 확인 실패' }
$SkillDir = 'C:\work\skills\md-link-check' # 실제 설치된 폴더로 지정
$Target = 'C:\work\repo\README.md' # 실제 검사 대상으로 지정
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-style-check.py') $Target
$StyleExit = $LASTEXITCODE
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-heading-check.py') $Target
$HeadingExit = $LASTEXITCODE
python -X utf8 -B (Join-Path $SkillDir 'scripts/md-link-check.py') $Target
$LinkExit = $LASTEXITCODE
```

각 호출 직후 종료 코드를 보존합니다. 마지막 성공으로 앞 실패를 덮지 않습니다. 도구 지원 옵션은 실제 `--help`·해당 설정에서 확인합니다. 지정된 검사기를 동봉 도구로 임의 교체하지 않습니다.

## 링크 검사 종료 상태

| 코드 | 의미                                                  |
|------|-------------------------------------------------------|
| `0`  | 실제 선택 파일의 파일 존재 검사 완료·통과             |
| `1`  | 깨진 링크·읽기 오류·유효 파일과 혼합된 미존재 입력    |
| `2`  | 선택 Markdown 0개 또는 닫히지 않은 펜스로 검사 미완료 |

빈 디렉터리·비Markdown·제외만·미존재만 입력은 검사 완료가 아닙니다. 검사 파일 수·제외 이유·종료 코드와 미검사 범위를 보고합니다. 이 표를 다른 도구의 종료 코드에 자동 적용하지 않습니다.

파일 검사기는 inline 링크의 각괄호 목적지·공백·균형 괄호·URL 인코딩 경로를 처리합니다. reference-style 링크·네트워크 URL·다른 파일 내부 앵커는 별도 범위입니다. 코드·인용구의 예시 링크는 실제 설치 의존성으로 취급하지 않습니다. 닫히지 않은 코드 펜스는 미완료로 보고합니다.

## 수정과 재검사

파일명 변경은 링크 텍스트와 목적지에 함께 반영합니다. 빠진 하위 경로를 보완하고 하위 문서에서 상위 문서를 참조하면 실제 위치에 맞는 `../`를 사용합니다. 외부 자동 수정기를 필수로 호출하지 않습니다. 합의된 표 정렬·공백·표기·목표가 명확한 링크 수정만 의미 불변으로 처리합니다.

공유 파일은 단일 담당자와 순서를 유지합니다. 지시 없는 전체 `--fix`·포맷·검사기 변경·임의 skip을 하지 않습니다. 정책에서 푸터를 금지하면 표현 검사의 `--no-footer`와 근거를 기록하고 다른 검사를 유지합니다. 검사 통과를 위해 정책상 금지된 푸터를 추가하지 않습니다. 수정 diff를 소유 담당자가 대조한 뒤 영향받는 부분만 재검사합니다.
