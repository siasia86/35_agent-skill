# Windows 배포본과 이관 보존 검증

네이티브 Python 3.11 이상에서 저장소 루트 기준으로 실행합니다. 개발 검증 파일은 개인 skill 설치 의존성이 아닙니다. 현재 native 배포본의 [정리 기록](../../2026-10-10-windows-native-T-WIN-004/README.md)과 역사 [전체 출처 manifest](source_manifest.json)를 구분합니다.

## 1. 재현 명령

```powershell
python -X utf8 -B agent-workflows/codex/windows/verification/verify_current.py
python -X utf8 -B agent-workflows/codex/windows/verification/test_current.py
python -X utf8 -B agent-workflows/codex/windows/verification/test_markdown.py --skills codex_windows/skills
python -X utf8 -B agent-workflows/codex/windows/verification/test_runtime.py --skills codex_windows/skills
python -X utf8 -B agent-workflows/codex/windows/verification/test_patterns.py --skills codex_windows/skills --pattern-document codex_windows/skills/work-rules/references/windows/file-lock.md
```

Bash는 현재 Windows 배포본의 필수 조건이 아닙니다. 과거 Bash 도구를 별도로 검사할 때만 `test_runtime.py`에 실제 실행 파일을 가리키는 `--bash`와 보존 도구를 가리키는 `--legacy-bash-script`를 함께 명시합니다. 둘 중 하나만 지정하거나 지정 파일이 없으면 오류입니다. 이번 native 검사에서는 Bash를 실행하지 않으며 이를 Linux 검증 완료로 보고하지 않습니다. 세부 CLI는 각 스크립트의 `--help`를 따릅니다.

`verify_skills.py`는 최초 이관 당시 구조·본문을 검사하는 역사 도구입니다. 최초 이관 19개·파일 182개·설정 2개와 원문/보존 해시 368건은 유지합니다. STYLE 원문 7개의 [이전 보존 대응](../../2026-10-04-personal-routing-T-WIN-004/preservation-map.json)과 이번 [보존 대응표](../../2026-10-10-windows-native-T-WIN-004/preservation-map.json)를 순서대로 해석해 이동한 원형을 확인합니다. 과거 `active` 경로의 존재를 현재 배포 계약으로 강제하지 않습니다. 과거 manifest와 검사 결과는 변경하지 않습니다.

현재 배포는 별도 [current_inventory.json](current_inventory.json)에 선언한 **native 21개**입니다. Bash skill 하나는 보존 후 Windows에서 제외했고, 나머지 역사 skill의 공통 기능은 유지했습니다. 현재 검사기는 선언 목록·전체 본문·참조·메타데이터·Windows 도구를 검사합니다. 잠금 회귀는 현재 실제 예제를 명시합니다.

## 2. 검증 범위

개인 설정의 지정 파일·skill 폴더 전체를 보존할 때는 [Snapshot-PersonalConfig.ps1](Snapshot-PersonalConfig.ps1)을 사용합니다. 업데이트 폴더는 `agent-workflows/codex/<날짜-목적-작업ID>/`에 먼저 준비하고 private의 Git 제외를 확인합니다. 기본 백업 루트는 스크립트 위치에서 두 단계 위의 codex이며 원래 기록 위치를 유지합니다. [PCS의 실행 예](../../20261003-native-layout-PCS-20261003-structure/README.md#2-업데이트-폴더와-백업), [위치 보정·검증](../records/2026-10-04-record-relocation-SMA-20261004-01/README.md)을 확인합니다.

- 현재 검사: 선언한 스킬 폴더의 누락·미등록 추가·SKILL.md 누락, name/description, 형식별 활성 본문과 native 인터페이스, 배포 참조·Python AST·helper 사본 동일성. 최초 이관의 본문·동봉 역할 동등성은 과거 verify_skills의 계약이며 개정한 활성 지침에 강제하지 않습니다.
- 목록·형식은 관찰한 폴더에서 자동 생성하지 않습니다. 새 스킬 승인 시 current_inventory를 담당 변경과 함께 명시적으로 개정·검토하고 회귀를 실행합니다. 역사 source_manifest와 원형 보존 자료는 개정하지 않습니다.
- 메타데이터는 현재 배포의 단일 행 name·description 문자열과 native agents/openai.yaml의 interface 세 문자열을 검사합니다. 선택적인 `policy.allow_implicit_invocation`의 Boolean도 처리하고 기존 호출 정책을 유지합니다. 임의 YAML 문법 전체의 파서는 아니며 공식 quick_validate는 별도 검사입니다.
- 현재 native는 폴더의 전체 Markdown 본문을 검사합니다. 인라인 파일 링크의 존재·폴더 밖 의존성·코드 펜스를 확인하며, 참조형 링크·앵커·외부 URL 도달성은 전체 검사로 주장하지 않습니다. Bash 실행·과거 Linux 파일 연결·배포 폴더 안의 보존 원문도 검사합니다.
- 각 폴더를 독립 TEMP에 복사한 뒤 실제 helper 실행. 형제 skill·원repo의 import를 이용하지 않습니다.
- 한국어·공백·CRLF·유효/깨진 링크·누락/혼합 입력·앵커 중복·인용/tilde fence의 정상·실패 반환.
- Python CLI와 원자 쓰기, 잠금 소유·경쟁·부분 쓰기 실패·기존 파일 보존. 과거 Bash 검사는 명시 선택 시에만 별도 실행합니다.

검사에 쓰는 fixtures는 새 TEMP 안에서 생성·정리합니다. 운영 리소스·개인 홈·네트워크·권한을 바꾸지 않습니다. 공식 `skill-creator`의 `quick_validate.py`도 별도 실행하며 PyYAML은 개발 검증용일 뿐 동봉 runtime 의존성이 아닙니다.

W02–W10의 과거 Markdown91조건·Python/Bash108조건은 당시 결과입니다. 현재 실행한 조건 수와 건너뛴 항목은 새 정리 기록에 남기고 과거 수치를 재사용하지 않습니다. 시작/완료 보고 규칙과 당시 판정은 [보고 지침과 helper 보완](../REPORTING_REMEDIATION_2026-10-03.md#3-현재-검증과-미실행)을 확인합니다.

[이번 교정·회귀·복구 기록](../records/2026-10-05-current-verifier-MAIN-20261004-01/README.md)은 현행 21개에서 재현한 실패와 수정 결과를 연결합니다. test_current는 안전한 TEMP 사본에서 누락·추가·잘못된 메타데이터·형식·링크·역사 자료 변조를 검사합니다. test_patterns도 같은 선언과 활성 본문 선택을 재사용합니다.

## 3. 결과와 한계

`results.json`·`input_hashes.json`·`behavior_summary.json`은 이관 커밋 `773a150`의 과거 검사 결과·입력 해시·사례 기록이며 당시 경로와 bytes를 보존합니다. [이관 결과](results.json)와 [당시 입력 해시](input_hashes.json)를 현재 파일의 검사 결과로 재사용하지 않습니다. 새 검사는 별도 결과 파일에 비식별 case·카운트·판정을 기록합니다. 개인 절대 경로·계정·토큰·원시 stdout은 로컬에 보존합니다. 검사 입력과 실제 결과가 바뀌면 새 결과를 기록합니다. 원문의 과거 Linux 결과는 Windows 최종본 결과로 바꾸지 않습니다.

실제 개인 홈 설치·Codex 검색/자동 선택·관리 sandbox 설정·NTFS ACL/ADS/owner 보존·SMB·비협조 writer·원격 인프라 적용·WSL 전체 동작은 별도 확인 대상입니다. stdlib의 파일 동일성 대조를 Windows 보안 경계 전체로 확대하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-10

© 2026 siasia86. Licensed under CC BY 4.0.
