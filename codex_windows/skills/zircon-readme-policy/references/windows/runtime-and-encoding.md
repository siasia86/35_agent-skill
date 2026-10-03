# Windows runtime·인코딩·config와 상태

네이티브 실행 방법·인코딩·Python config/status를 다룰 때 읽습니다. 인코딩·실행 환경은 1절, Python config/status는 2절, VM은 3절만 확인합니다. Windows라는 이유만으로 다른 절까지 읽지 않습니다.

## 1. 실행 환경과 파일 처리

- Windows 네이티브 PowerShell과 실제 Python 3.11 이상을 사용합니다. PowerShell 5.1/7, `python.exe`/`py`의 실제 경로·버전을 확인하고 WindowsApps alias를 설치된 runtime으로 간주하지 않습니다. Python은 `-X utf8 -B`로 호출하고 작성하는 코드의 파일 읽기·쓰기도 `encoding='utf-8'`을 명시합니다. PowerShell 인코딩은 버전별로 확인하며 BOM/UTF-16/개행을 의도 없이 변경하지 않습니다.
- PowerShell의 파일 작업은 `-LiteralPath`, `Join-Path`, 확인한 절대 경로를 사용합니다. Linux의 `/root`, `/opt`, `$HOME`, `chmod`, `sudo`, `systemctl`, `fcntl`을 Windows 계정·경로·ACL·서비스로 이름만 치환하지 않습니다. WSL/Git Bash가 필요하면 명시한 Linux/Bash 역할로 구분하며 설치·활성화·권한 변경은 자동 수행하지 않습니다.
- 네이티브 CLI의 종료 상태는 해당 도구 계약으로 판정합니다. PowerShell cmdlet 오류와 `$LASTEXITCODE`를 혼동하지 않고 오류 로그만으로 성공 처리하지 않습니다. Terraform detailed exit code처럼 정상 차이를 뜻하는 상태는 일반 실패와 구분합니다.

- **§2 위험 작업·§3 삭제:** 현재 승인 범위를 동작 직전에 확인합니다. 대상·영향·복구 범위를 확인하고 Windows 삭제/이동은 절대 경로가 의도한 범위 안에 있는지 확인한 뒤 `Remove-Item`/`Move-Item -LiteralPath`로 수행합니다. 다른 shell이나 문자열 명령으로 권한/범위를 우회하지 않습니다. 이미 승인된 같은 동작은 재확인하지 않습니다.

PowerShell 5.1의 Out-File·리다이렉션과 PowerShell 7의 인코딩 기본값을 구분합니다. BOM/UTF-16/개행을 의도 없이 바꾸지 않고 Python 문서 입출력에 UTF-8을 지정합니다.

## 2. Python config와 종료 상태

- **§17 Python:** 구조·SAFETY·날짜 VERSION·argparse·docstring·최소 예외·필수 option/help와 검증 목적을 유지합니다. Windows에서는 실제 python.exe를 명시하고 JSON/TOML/config/status의 encoding·경로·최종 종료 상태를 명확하게 처리합니다. 파일 owner/mode·ACL·atomic replace는 같은 기능으로 간주하지 않습니다.

원문의 `load_config` 자동 발견은 현재 SCRIPT_DIR 아래 실제 설정 1개가 확인된 경우만 적용합니다. 경로를 주면 실제 지정 파일을 사용하고 TOML은 binary·JSON은 UTF-8로 읽으며 필수 키·타입·범위를 검증합니다. 다른 홈·config를 검색/복사하거나 모호한 첫 파일을 선택하지 않습니다.

```python
# 현재 코드의 SCRIPT_DIR·필수 키/범위 계약을 사용합니다.
import json
import tomllib
from pathlib import Path


def load_config(config_path=None):
    """Load one explicitly selected or unambiguous TOML/JSON config."""
    if config_path is None:
        candidates = sorted(Path(SCRIPT_DIR).glob('*config.toml'))
        candidates += sorted(Path(SCRIPT_DIR).glob('*config.json'))
        if len(candidates) != 1:
            raise FileNotFoundError('exactly 1 config file required')
        config_path = candidates[0]
    selected = Path(config_path)
    if selected.suffix.lower() == '.toml':
        with selected.open('rb') as stream:
            return tomllib.load(stream)
    if selected.suffix.lower() != '.json':
        raise ValueError('expected TOML or JSON config')
    with selected.open('r', encoding='utf-8') as stream:
        return json.load(stream)
```

이 config 함수는 기존 프로그램의 전달된 자료를 읽는 패턴입니다. 설정 병합·설치·실제 서비스 변경을 수행하지 않습니다. 신규 코드는 module import 순서 등 원문의 개인 양식을 함께 적용합니다.

원문의 `write_status(error_codes)` 목적은 모니터링 프로토콜의 상태 기록입니다. 실제 LOG_DIR/STATUS_FILE·오류 코드 의미를 확인하고 UTF-8로 기록합니다. 0 성공/비정상 실패 집계를 프로젝트 계약에 맞추고 실패를 status나 프로세스의 0으로 덮지 않습니다. `main()`의 최종 결과는 `sys.exit(main())`로 프로세스에 전달하며 R07 누락/혼합 입력과 R14 등록된 도움말 option을 함께 검사합니다.

[PowerShell 인코딩](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-5.1)의 실제 사용 버전과 파일 형식을 함께 확인합니다. Bash/POSIX/Kiro 예시는 비교 자료이며 Windows의 자동 실행 방법이 아닙니다.

## 3. VM 작업의 실행 범위

- **§20 VM:** 실제 VM 목록·대상·상태·삭제/중지/재생성 차이와 현재 승인 범위를 확인합니다. Hyper-V cmdlet·관리자 권한·vagrant provider는 실제 존재할 때만 사용합니다. 이미 대상까지 승인된 작업에 같은 삭제 승인을 반복 요구하지 않으며 범위 밖 VM은 변경하지 않습니다.
