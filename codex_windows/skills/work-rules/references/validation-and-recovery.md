# 검증 도구와 실패 복구

검사기를 호출하거나 검증 실패·재개를 판단할 때 읽습니다. 대상 repo의 필수 도구·버전·설정을 우선하며 이 문서로 gate를 대체하지 않습니다.

## 1. 검사 선택과 실패 처리

- **§1 승인·§1-1 장시간 실행:** 목적·범위를 간결하게 알리고 승인된 작업은 진행합니다. 도구의 비동기 세션/후속 상태 조회를 사용하며 짧은 timeout을 모든 명령에 강제하지 않습니다. timeout은 실패 확정이 아니므로 실제 소유 프로세스·부분 실행·로그를 먼저 확인합니다. 동일 접근 2회 실패 후 근본적으로 다른 접근을 검토하되 승인 밖 재시도·프로세스 종료를 자동 수행하지 않습니다.

- **§11 Markdown 검사:** 저장소 지정 검사기를 우선하고 지정이 없으면 현재 변경한 문서에 동봉 Windows Python style/heading/link 도구를 사용합니다. `python -X utf8 -B`와 명시 대상·실제 종료 상태를 확인합니다. 외부 fix_table_align/trim_diagram 도구를 필수 설치하지 않고 보고된 문제를 범위 안에서 수정·재검사합니다. 파일 입력 누락·읽기 실패·미닫힘을 성공으로 처리하지 않습니다.

- **§12 사후 검증:** 문법/변경 영향/건강/모니터링의 목적을 실제 기술에 맞춰 적용합니다. 코드/문서 검토 요청에 Terraform/AWS/서비스 실행을 강제하지 않습니다. plan/apply/운영 검사가 없거나 미실행이면 그 이유와 남은 조건을 보고합니다.

- **§19 치환 확인:** 치환 전 대상과 예상 건수를 확인하고 이후 관련 행·잔여 문자열·참조·영향 범위를 `rg` 또는 `Select-String -LiteralPath`로 대조합니다. 일괄 값 변경은 승인한 파일 목록에서 처리하며 로그/비밀정보를 공개 출력하지 않습니다. 0건 치환을 성공으로 처리하지 않고 의도된 0건과 실패를 구분합니다. sed 예시를 PowerShell에서 실행하지 않습니다.

파일 링크·같은 파일 앵커·다른 파일 앵커·외부 도달성은 별도 범위입니다. 대상 0개는 미완료이며 동봉 link checker는 exit 2입니다. 0은 완료한 파일 존재 검사 통과, 1은 깨진 링크/읽기 오류, 2는 빈 대상·미닫힌 펜스 등 검사 미완료입니다. 적용 repo의 재시도·중단 조건을 따르고 같은 실패에 새 근거 없이 명령만 반복하지 않습니다.

## 2. 동봉 Markdown 도구

현재 폴더의 실제 Python 3.11+와 명시 대상을 사용합니다. 저장소 지정 도구가 없을 때만 동봉 도구를 선택하고 경로·버전·선택 이유·개수·종료 상태를 기록합니다. 푸터·날짜·배지는 repo가 채택한 경우만 검사하며 개인 기본값으로 강제하지 않습니다.

```powershell
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-heading-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '헤딩 검사 실패: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-link-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '링크 검사 실패 또는 미완료' }
# repo가 푸터를 채택하지 않은 경우에만 --no-footer를 사용합니다.
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-style-check.py') --no-footer $target
if ($LASTEXITCODE -ne 0) { throw '문서 표현 검사 실패' }
```

누락·미닫힘·읽기 오류를 성공으로 처리하지 않습니다. 외부 checker에만 있는 옵션을 동봉 도구도 지원한다고 가정하지 않습니다. 도구별 상세가 필요할 때 [md-link-check](skills/md-link-check.md)를 확인합니다. 도구 구현의 미지원 Markdown 문법은 별도 점검하고 검사 성공을 전체 Markdown 검증으로 확대하지 않습니다.
