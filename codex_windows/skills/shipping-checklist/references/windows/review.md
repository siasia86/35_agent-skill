# Windows 상세 리뷰

- PowerShell cmdlet은 오류 처리·정리 경로를 확인합니다. `$ErrorActionPreference = 'Stop'`만으로 모든 외부 명령 실패가 전달된다고 가정하지 말고 각 native 호출 직후 `$LASTEXITCODE`를 확인합니다. 입력을 인자 배열로 전달하고 `Invoke-Expression` 등으로 재해석하지 않습니다.
- 파일은 확인한 절대 경로·`-LiteralPath`로 다룹니다. 삭제·이동을 다른 shell로 넘기지 않고 재귀 작업은 최종 대상이 승인된 루트 안인지 검증합니다.
- Python은 실제 지원 버전과 `-X utf8 -B`, UTF-8 파일 입출력, `[sys.executable, '-X', 'utf8', '-B', ...]` 하위 실행을 확인합니다.
- symlink·reparse·junction·hard-link, NTFS ACL·owner·ADS, 잠금·파일 공유·replace 실패, 공백/한글 경로·CRLF 차이는 명시 지원 계약에 따라 평가합니다. Windows mode 비트를 ACL과 동일시하지 않습니다.
- 잠금·부분 저장·정리 계약은 안전한 TEMP fixture로 확인합니다. 비협조 writer와 네트워크 파일시스템까지 보장한다고 확대하지 않습니다.
- IaC 검토는 실제 채택한 도구에만 적용합니다. 접근 정책의 와일드카드, 정당화 없는 공개 inbound, 암호화, 상태 데이터 삭제·교체 보호, 수동 변경 드리프트와 적용 순서를 평가합니다. 공개 웹 listener를 모두 금지하지 않습니다.
