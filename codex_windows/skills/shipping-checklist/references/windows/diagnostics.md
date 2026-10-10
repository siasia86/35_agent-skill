# Windows 장애 진단

실제 대상과 시간 범위를 먼저 확인합니다. 서비스·이벤트 채널 접근 권한이 없으면 그 검사를 미확인으로 표시합니다. 비밀값·개인 설정 전체를 로그에 복사하지 않습니다.

| 계층          | 승인된 읽기 전용 조사                                                     |
|---------------|---------------------------------------------------------------------------|
| 서비스        | 실제 이름의 `Get-Service -Name <name>`와 해당 이벤트의 `Get-WinEvent`     |
| 프로세스·자원 | `Get-Process`, `Get-PSDrive`, 필요한 CIM 정보·관련 이벤트                 |
| 연결          | `Get-NetTCPConnection`, 대상 DNS·listener·endpoint 구분                   |
| HTTP          | 실제 URL의 `Invoke-WebRequest`·`Invoke-RestMethod` 또는 확인한 `curl.exe` |
| 변경          | 관련 범위 `git log`·`git diff`, 실제 구성·배포 이력 전후 비교             |

PowerShell의 `curl` alias와 `curl.exe` 옵션을 혼동하지 않습니다. localhost 성공은 다른 대상 서비스의 건강 증거가 아닙니다. 서비스 재시작은 승인된 대상과 원인·복구 조건을 확인한 뒤에만 실행합니다.

Terraform 업무의 실패는 잠금 소유·동시 실행, provider 대상·인증·API 한도, 실제 리소스와 state 충돌, 의존성·순서, quota로 분류합니다. 오류 메시지의 force-unlock·import·교체 명령을 바로 실행하지 않습니다. 상세 종료 0은 변경 없음, 2는 변경 있음, 1은 오류입니다.

클라우드 업무는 403의 권한·리소스 정책·조직 정책, 503의 서비스 상태, timeout의 경로·접근 규칙·DNS, throttling의 호출 한도·백오프를 실제 증거로 좁힙니다. 자동 인증 변경·새 권한 부여는 포함하지 않습니다.

Docker 업무는 실제 Windows CLI와 승인된 daemon/context·컨테이너가 준비됐을 때 로그·inspect를 사용합니다. HEALTHCHECK가 없는 컨테이너는 건강 통과로 표시하지 않습니다. 채택하지 않은 도구의 검사를 모든 장애에 강제하지 않습니다.
