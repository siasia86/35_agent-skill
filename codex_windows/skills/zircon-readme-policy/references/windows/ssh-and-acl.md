# Windows SSH·실제 권한·ACL

SSH 원격 실행·인코딩·인증·ACL을 다룰 때 읽습니다. 실제 계정과 현재 요청의 범위에서 점검합니다.

## 1. 실행 계층과 권한

- **§7 권한:** Windows 관리자 토큰·UAC·파일 ACL·서비스 권한과 원격 Windows 계정 권한은 별도입니다. 실제 권한·대상을 확인하고 필요한 추가 권한은 정상 승인 경로에서 다룹니다. 작업 파일 접근 거부, SSH 소유자 확인 실패가 ACL 변경·관리자 실행·sandbox 우회 권한이 아닙니다.

- **§18 SSH 인코딩:** local PowerShell → SSH client → 원격 기본 shell → 실제 powershell.exe/pwsh의 계층을 확인합니다. 원문의 `cmd /c chcp` 중첩 quote를 Windows 공통 필수 패턴으로 실행하지 않습니다. 원격 Windows PowerShell의 복잡한 스크립트에는 실제 지원하는 `-EncodedCommand`(UTF-16LE Base64)를 검토하고, 입력 데이터와 스크립트를 분리해 injection을 막습니다. 원격 실행 정책·host key·코드페이지·stdout/stderr·종료 상태를 실제 fixture로 확인하며 인코딩 옵션이 승인/권한을 우회하지는 않습니다.

- **§21 SSH 프로세스:** 시작 시 모든 SSH/PID를 일괄 kill하는 원문 예시는 실행하지 않습니다. 현재 작업이 시작한 process/session의 PID·소유·대상과 부분 실행을 확인해 정상 종료를 우선합니다. 필요한 `Stop-Process`는 그 작업의 확인된 PID·승인 범위에서만 사용합니다. 다른 사용자/작업·전체 ssh.exe·원격 서비스를 종료하지 않습니다.

## 2. 키와 ACL 점검

Windows OpenSSH user key·server host key·authorized_keys·관리자용 authorized_keys는 서로 다른 소유/ACL 대상입니다. 실제 계정·client/server·공식 설정·현재 ACL을 필요한 범위에서 확인하고 다른 플랫폼의 파일 권한 명령을 Windows ACL의 대체 절차로 적용하지 않습니다. 키 본문·다른 계정의 키를 출력하지 않으며 정상 인증 실패를 ACL 완화·host key 확인 생략으로 우회하지 않습니다.

개인 config의 기본값과 현재 세션 정책·추가 승인·파일 ACL을 구분합니다. 파일 읽기 실패만으로 관리자 권한·ACL 변경이 필요하다고 단정하지 않습니다. 실제 대상·계정·권한을 확인하고 요청 범위에 포함된 최소 변경만 수행합니다.

[Windows OpenSSH 키 관리](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement), [PowerShell EncodedCommand](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.2)의 대상 버전·공식 설정을 확인합니다.
