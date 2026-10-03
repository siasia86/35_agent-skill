# Windows 이관 검증

네이티브 Python 3.11 이상에서 저장소 루트 기준으로 실행합니다. 개발 검증 파일은 개인 skill 설치 의존성이 아닙니다. [실제 결과](../REVIEW.md)와 [전체 출처 manifest](source_manifest.json)를 함께 확인합니다.

## 1. 재현 명령

```powershell
python -X utf8 -B agent-workflows/codex/windows/verification/verify_current.py
python -X utf8 -B agent-workflows/codex/windows/verification/test_markdown.py --skills codex_windows/skills
python -X utf8 -B agent-workflows/codex/windows/verification/test_runtime.py --skills codex_windows/skills
python -X utf8 -B agent-workflows/codex/windows/verification/test_patterns.py --skills codex_windows/skills --pattern-document codex_windows/skills/work-rules/references/windows/file-lock.md
```

Bash 조건은 `test_runtime.py`에서 `--bash '<현재 Git Bash의 bash.exe 경로>'`로 추가합니다. 설치된 실제 실행 파일을 확인합니다. Git Bash 실행은 WSL·Linux 전체 환경 검증과 별도입니다. 세부 CLI는 각 스크립트의 `--help`를 따릅니다.

`verify_skills.py`는 최초 이관 당시 구조·본문을 검사하는 역사 도구입니다. T-WIN-004 이후 STYLE 원문 7개는 [보존 대응](../../2026-10-04-personal-routing-T-WIN-004/preservation-map.json), 개인 AGENTS는 배포 루트에 있습니다. 현재 검사는 원문 368개 해시 대조·19개 skill·독립 helper·배포 참조를 확인합니다. 잠금 회귀는 이동한 실제 예제를 명시합니다. 과거 manifest·검사 결과와 skill 구현은 수정하지 않습니다.

## 2. 검증 범위

개인 설정의 지정 파일·skill 폴더 전체를 보존할 때는 [Snapshot-PersonalConfig.ps1](Snapshot-PersonalConfig.ps1)을 사용합니다. 업데이트 폴더는 `agent-workflows/codex/<날짜-목적-작업ID>/`에 먼저 준비하고 private의 Git 제외를 확인합니다. 기본 백업 루트는 스크립트 위치에서 두 단계 위의 codex이며 원래 기록 위치를 유지합니다. [PCS의 실행 예](../../20261003-native-layout-PCS-20261003-structure/README.md#2-업데이트-폴더와-백업), [위치 보정·검증](../records/2026-10-04-record-relocation-SMA-20261004-01/README.md)을 확인합니다.

- 현재 검사: 19개 skill, 출처 182개 파일·설정 2개의 원문/보존 해시 368건, 배포 참조·Python AST·helper 사본 동일성. 최초 이관의 본문·동봉 역할 동등성은 과거 verify_skills의 계약이며 개정한 활성 지침에 강제하지 않습니다.
- 각 폴더를 독립 TEMP에 복사한 뒤 실제 helper 실행. 형제 skill·원repo의 import를 이용하지 않습니다.
- 한국어·공백·CRLF·유효/깨진 링크·누락/혼합 입력·앵커 중복·인용/tilde fence의 정상·실패 반환.
- Python CLI와 원자 쓰기, 잠금 소유·경쟁·부분 쓰기 실패·기존 파일 보존, 선택 Bash 백업 실패 반환.

검사에 쓰는 fixtures는 새 TEMP 안에서 생성·정리합니다. 운영 리소스·개인 홈·네트워크·권한을 바꾸지 않습니다. 공식 `skill-creator`의 `quick_validate.py`도 별도 실행하며 PyYAML은 개발 검증용일 뿐 동봉 runtime 의존성이 아닙니다.

W02–W10의 신규 회귀는 Markdown91조건, Python/Bash108조건으로 확장했습니다. 시작/완료 보고 규칙과 현재 판정·미실행은 [보고 지침과 helper 보완](../REPORTING_REMEDIATION_2026-10-03.md#3-현재-검증과-미실행)을 확인합니다.

## 3. 결과와 한계

`results.json`·`input_hashes.json`·`behavior_summary.json`은 이관 커밋 `773a150`의 과거 검사 결과·입력 해시·사례 기록이며 당시 경로와 bytes를 보존합니다. [이관 결과](results.json)와 [당시 입력 해시](input_hashes.json)를 현재 파일의 검사 결과로 재사용하지 않습니다. 새 검사는 별도 결과 파일에 비식별 case·카운트·판정을 기록합니다. 개인 절대 경로·계정·토큰·원시 stdout은 로컬에 보존합니다. 검사 입력과 실제 결과가 바뀌면 새 결과를 기록합니다. 원문의 과거 Linux 결과는 Windows 최종본 결과로 바꾸지 않습니다.

실제 개인 홈 설치·Codex 검색/자동 선택·관리 sandbox 설정·NTFS ACL/ADS/owner 보존·SMB·비협조 writer·원격 인프라 적용·WSL 전체 동작은 별도 확인 대상입니다. stdlib의 파일 동일성 대조를 Windows 보안 경계 전체로 확대하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
