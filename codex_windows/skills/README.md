# Windows skill 목록

19개 skill의 원문·예시·체크리스트·필요 자료를 보존합니다. 활성 Windows 절과 동봉 도구를 실행 기준으로 사용하고 필요한 폴더 전체를 복사합니다.

## 1. 전체 19개

| skill                                                     | 유지한 역할                          | Windows 실행 조건·도구                        |
|-----------------------------------------------------------|--------------------------------------|-----------------------------------------------|
| [bash-script-template](bash-script-template/SKILL.md)     | Bash 전체 템플릿·백업·실패 전파      | Git Bash 또는 WSL; native 서비스는 PowerShell |
| [code-review](code-review/SKILL.md)                       | 코드·스크립트·IaC 검토               | Git·대상 언어 도구; 실행한 검사만 보고        |
| [debugging-and-recovery](debugging-and-recovery/SKILL.md) | 증거 수집·장애 격리·복구             | Windows 서비스/로그 또는 확인한 원격 Linux    |
| [doubt-driven-infra](doubt-driven-infra/SKILL.md)         | 비가역 변경의 가정·증거·복구 검토    | 대상 인프라 CLI와 현재 권한 확인              |
| [git-commit-rule](git-commit-rule/SKILL.md)               | 커밋·PR·변경 기록                    | Git·Python Markdown 도구                      |
| [incremental-change](incremental-change/SKILL.md)         | 작은 변경·선행 호환성·검증           | Git·대상 IaC/서비스 도구                      |
| [kiro-lock](kiro-lock/SKILL.md)                           | 협조자 잠금·소유 확인·해제           | Python 동봉 lock; ACL/SMB 보장 별도           |
| [md-link-check](md-link-check/SKILL.md)                   | Markdown 파일 링크·앵커·헤딩         | Python 검사기 3개 + md_common.py              |
| [planning-and-breakdown](planning-and-breakdown/SKILL.md) | 목적·범위·의존성·실행 순서           | 현재 저장소 문서 체계; 고정 외부 도구 없음    |
| [python-script-template](python-script-template/SKILL.md) | 전체 Python 템플릿·UTF-8·원자 쓰기   | Python; 실제 업무 변환은 대상에서 구현        |
| [readme-template](readme-template/SKILL.md)               | README 구조·표·푸터 규칙             | Python Markdown 도구; 저장소 예외 우선        |
| [repo-governance](repo-governance/SKILL.md)               | 저장소 지침·예외·권한 확인           | Git·현재 AGENTS와 채택된 정책                 |
| [security-tools](security-tools/SKILL.md)                 | 비밀정보·보안 도구·마스킹 검토       | Python·실제 제공된 보안 CLI; 개인 map 비공개  |
| [shipping-checklist](shipping-checklist/SKILL.md)         | 배포 조건·검증·가역성·복구           | 실제 배포 대상 CLI; 요청 범위 확인            |
| [spec-driven-infra](spec-driven-infra/SKILL.md)           | 인프라 명세·설계·구현·검증           | Terraform/Docker/원격 Ansible 등 대상별 확인  |
| [testing-guide](testing-guide/SKILL.md)                   | 테스트 설계·경계·실패·운영 지표      | 대상 언어 도구·명시한 playbook/container      |
| [using-skills](using-skills/SKILL.md)                     | 전체 19개 역할 대응·필요 참조 선택   | 동봉 역할 18개·현재 작업 도구                 |
| [work-rules](work-rules/SKILL.md)                         | 전체 공통 작업·문서·파일·서비스 규약 | PowerShell·Git·Python; Linux 업무 계층 구분   |
| [zircon-readme-policy](zircon-readme-policy/SKILL.md)     | Zircon 대상 README 정책·예외         | 명시 채택 저장소에서만; 동봉 Python 도구      |

## 2. 단독 사용과 보존

폴더 전체를 복사하면 동봉 참조·필요 helper를 사용할 수 있습니다. 다른 개인 skill 설치는 필요하지 않습니다. 실제 작업에 필요한 참조만 읽고 순환 참조를 반복하지 않습니다. 동봉 역할 54개도 Windows 본문으로 대응합니다.

`references/kiro-original.md`는 Kiro 원문, `references/linux-original.md`는 Linux 활성 원문입니다. 동봉 역할의 Linux 원문과 기존 도구는 각각 `references/linux-skills/`, `references/linux-tools/`에 bytes로 보존합니다. 비교용 Python 파일은 실행 도구가 아니며 `scripts/`의 Windows 사본을 사용합니다.

공통 지침은 상위 [AGENTS.md](../AGENTS.md), 설정 적용은 [personal 안내](../personal/README.md)를 확인합니다. 각 skill의 Windows 절에서 해당 역할의 실행 조건과 제한을 확인합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
