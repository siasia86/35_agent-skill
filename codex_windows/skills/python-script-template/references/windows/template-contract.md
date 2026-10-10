# Python 템플릿 계약

```powershell
$Template = Join-Path $SkillDir 'scripts/script_template.py'
python -X utf8 -B $Template --help
python -X utf8 -B $Template -d -v $Target
```

각 호출 직후 `$LASTEXITCODE`를 확인합니다. 무인수 도움말·help·version 0, 잘못된 옵션 2, 누락·종류 오류·처리 실패 1, 사용자 중단 130입니다. 혼합 batch에서 하나라도 실패하면 전체 1이며 dry-run도 누락을 실패 처리합니다. 유효 입력을 먼저 처리했다는 이유로 전체 성공을 표시하지 않습니다.

`-f`는 파일 batch, `-D`는 디렉터리 batch, 위치 인수는 단일 파일/디렉터리이며 동시에 섞지 않습니다. 디렉터리는 바로 아래 파일만 처리하고 재귀를 광고하지 않습니다. `transform_content()`가 실제 업무로 구현되기 전 일반 실행은 실패합니다.

기본 로그는 stderr입니다. `--log-dir`를 명시한 승인 경로에만 UTF-8 월별 파일 로그를 만들고 생성 실패면 콘솔 경고와 콘솔 로깅을 유지합니다. 명시 입력이 활성·예정 로그 파일과 겹치면 로그 파일을 열기 전에 거부하고 디렉터리 처리에서는 활성 로그를 제외합니다. stdout 데이터와 로그를 구분합니다.

파일 저장은 일반 파일과 확인 가능한 부모 경로의 reparse를 검토하고 동일 디렉터리 임시 파일을 flush·fsync 후 `os.replace()`합니다. 교체 직전 파일 동일성을 확인하며 실패한 임시 파일을 정리합니다. 읽기 전용 mode는 가능한 범위에서 유지합니다.

NTFS ACL·owner·ADS·확장 속성·hard-link 관계·전원 장애 영속성 보존, 검사 사이 비협조 경로 교체 차단은 이 표준 라이브러리 템플릿의 보장이 아닙니다. 필요한 메타데이터·동시 writer 계약은 실제 프로젝트에서 구현·검증합니다.
