# Codex 개인 스킬 동작 보완과 테스트

## 1. 요청 범위와 기준

사용자가 “보완 작업 진행 후 테스트까지”를 요청했습니다. 시작은 yunli `f66b5b8`의 clean 작업 트리입니다. 저장소 로컬 보완·임시 Linux fixture·관련 기록을 수행하며 commit·push·설치·운영 적용은 포함하지 않습니다. `.governance`는 없으며 현재 AGENTS·TODO2의 원문 보존 기준을 적용했습니다.

수정 전 파일 472개의 해시와 변경 대상 사본을 `/tmp/35-skill-remediation-zqwgd23p`에 보관했습니다. 미게시 복구는 현재 diff와 그 사본을 대조하여 이번 변경만 되돌리는 방법을 사용합니다. 사용자 변경·Git index·refs를 전체 reset하거나 정리하지 않습니다. 기존 Kiro/GPT·105_backup·개인 설치 사본과 과거 검토 자료는 유지합니다.

## 2. 수정 내용과 적용 위치

- Python: argparse가 namespace와 parser를 함께 반환하고 main이 같은 parser로 도움말을 출력하는 보완 블록을 추가했습니다. 기존 옵션·처리 분기와 원문 전체를 유지합니다.
- Python atomic write: POSIX 일반 파일의 mode·uid·gid를 임시 파일에 적용한 뒤 교체합니다. 메타데이터·쓰기·sync·replace 실패는 원본을 유지하고 임시 파일을 정리합니다. 새 파일은 0600이며 symlink와 디렉토리는 거부합니다.
- Bash: 명령과 인수를 별도로 실행하고 `if`에서 실패 상태를 확보한 뒤 stderr 로그와 원래 상태를 반환합니다. 필수 단계는 호출부의 `|| exit "$?"`로 다음 작업을 차단합니다. 문자열 eval 원문은 보존 자료로 유지합니다.
- flock: §17의 Python 예시를 보완하여 동일 경로를 유지하는 context manager를 추가했습니다. 정상 해제 시 경로를 삭제하지 않으므로 기존 waiter와 새 프로세스가 같은 inode를 사용합니다. 동봉 kiro-lock helper는 변경하지 않았습니다.
- 링크 검사기: 실행용 사본 7개에서 펜스 문자·길이·닫는 태그·최대 3칸 들여쓰기를 추적합니다. 미닫힘은 종료 2로 보고하고 다른 파일의 검사는 계속합니다. 검사기 날짜 버전은 `26.10.03`이며 외부 source는 변경하지 않았습니다.
- 참조 완결성: shipping-checklist의 code-review와 네 STYLE 역할의 readme-template·그 문서가 요구하는 md-link-check를 전체 지침과 비교 원문으로 동봉했습니다. governance 템플릿 이름은 대상 저장소가 채택한 조건부 입력으로 명시했습니다. 필수 자료 접근 실패를 자동 대체하는 규칙은 추가하지 않았습니다.

모든 보완 예시는 CODEX-COMPAT 절 안에 추가했고 실제 동봉 활성 사본에도 반영했습니다. Kiro의 본문·예시·템플릿·체크리스트는 삭제·축약·통합하지 않았습니다. [MIGRATION](../../codex/MIGRATION.md)의 행 대응 표는 현재본을 기준으로 갱신했습니다.

## 3. 실제 검증 결과

수정 전 재현 스크립트는 종료 0으로 기존 동작 문제 5개를 다시 확인했습니다. [baseline.json](reviews/2026-10-03-remediation/baseline.json)에 새 관찰을 보존하며 앞선 검토 JSON을 덮어쓰지 않았습니다.

- **통과:** [회귀 테스트](../../codex/verification/test_remediation.py) 16개·CLI 실행 120회입니다. Python의 무인수/help/version/잘못된 옵션/처리 분기, 네 파일 mode와 동일 uid/gid 보존, 새 파일 0600, 실패 시 원본 유지/임시 파일 정리, Bash의 일반/set-e 상태 7 전파/로그/후속 차단, argv 보존, flock의 waiter/새 프로세스 배제와 예외 해제를 검사했습니다.
- **통과:** 링크 검사기 7개를 각각 단독 폴더로 복사하여 중첩·tilde·더 긴 닫는 펜스·태그/다른 문자·들여쓰기·행 번호·미닫힘·혼합 파일·기존 외부/앵커/인라인 제외를 확인했습니다. 같은 오류 입력을 숨기는 종료 0은 없었습니다.
- **통과:** [기본 검사](../../codex/verification/verify_skills.py)에서 스킬 19개·전체 동봉 역할 54개·폴더 내부 참조 213개·Python 도구 25개·단독 도구 실행 35회·kiro-lock 조건 8개입니다. source 본문과 비교 원문의 bytes 대응도 확인했습니다.

- **통과:** Markdown 45개에서 source 대비 새 style 경고 0건, 헤딩 820개·파일 링크 163개·앵커 13개 오류 0건, frontmatter 19개 실패 0건, 변경 Python 9개 구문·diff 검사를 확인했습니다. 원시 style 경고 89건은 기존 source/푸터 경고로 유지합니다. 회귀 입력 80개의 해시는 현재 파일과 같고, 기존 추적 파일 472개 중 변경 33개 외 439개는 해시가 같습니다. 보호 원본 변경·누락은 0개이며 HEAD와 staged 상태도 유지했습니다.

문서·frontmatter·구문·diff·보존의 실제 명령과 결과는 [validation.json](reviews/2026-10-03-remediation/validation.json)에 남깁니다. 지침 style은 푸터를 포함한 원시 결과와 source 대응 비교를 구분하며 기존 원문 경고를 수정하거나 통과로 바꾸지 않습니다. 새 보완문은 source 대비 새 경고가 없어야 합니다.

처음 추가한 `불완전`은 style 검사기의 과장 표현 규칙에 걸려 “미완료”로 바꿨습니다. 검증 실패를 숨기기 위해 해당 검사를 제외하지 않았습니다. 문서 검증 스크립트의 첫 실행은 이전 읽기 검사에서 생성한 Python bytecode를 UTF-8로 읽다가 실패했습니다. 해당 생성물만 제거하고 스크립트의 비텍스트 처리와 bytecode 생성 방지를 보완한 뒤 재실행했습니다. [validation-initial-error.txt](reviews/2026-10-03-remediation/validation-initial-error.txt)에 실패 원인을 보존합니다.

[tests.json](reviews/2026-10-03-remediation/tests.json)에 최종 스킬 입력 해시·명령·종료 코드·stdout/stderr를 남깁니다. [basic-check.json](reviews/2026-10-03-remediation/basic-check.json)은 기본 검사 요약입니다.

## 4. 부분 검사와 미검증

소유 보존은 동일 uid/gid의 실제 파일과 fchown 권한 거부 주입으로 확인했습니다. 다른 소유의 실제 파일을 변경하거나 OS 소유 권한을 바꾸지 않았습니다. ACL·확장 속성·하드 링크·Windows 메타데이터·네트워크 파일시스템·비협력 writer는 검증하지 않았으며 보완 예시의 보장 범위에서 제외합니다.

Gitleaks 실행 도구가 없어 정규식 기반 비밀정보 검사만 부분 검사로 남깁니다. 새 최종본의 독립 모델 행동·개인 홈 설치/발견·Windows·운영 적용은 미실행입니다. 기존 Luna 기록의 입력 해시 차이는 로컬 코드 테스트로 해소했다고 처리하지 않습니다. commit·push·원격 재조회도 수행하지 않았습니다.

## 5. 재검사와 다음 작업

아래 명령은 개발용 검사이며 복사한 개인 스킬의 필수 의존성이 아닙니다. 새 실행 결과는 기존 원시 JSON을 덮어쓰지 않도록 다른 출력 경로에 저장합니다.

```bash
python3 codex/verification/test_remediation.py --output /tmp/35-remediation-tests.json
python3 codex/verification/verify_skills.py
python3 agent-workflows/codex/reviews/2026-10-03-remediation/validate_remediation.py --output /tmp/35-remediation-validation.json
```

다음 미완료 항목은 [Codex TODO](../../codex/TODO.md)의 최종본 독립 사례와 사용자가 선택한 실제 환경 확인입니다. 구현 보완·로컬 테스트 완료와 게시/설치 완료를 구분합니다. [HANDOFF](HANDOFF.md#9-동작-보완과-로컬-테스트-완료)의 최신 범위를 따릅니다.

## 6. 보완 변경 게시와 main 병합 승인

로컬 보완·테스트가 끝난 뒤 사용자가 “push 후 main 까지 병합 진행”을 요청했습니다. 이번 요청에 한해 검증한 변경과 게시 기록을 yunli에 일반 commit·push하고 main까지 병합합니다. 로컬 main·yunli도 파일을 보존하면서 게시 결과에 맞춥니다. 과거 승인 기록을 재사용하지 않으며 force push·release·다른 저장소·개인 홈·OS 권한 변경·운영 적용은 제외합니다.

게시 시작 기준은 원격·로컬 main/yunli 모두 `f66b5b8`입니다. sandbox 원격 조회는 DNS 제한으로 실패했고 승인된 네트워크 fetch는 종료 0으로 최신 refs를 확인했습니다. 독립 게시 clone `/tmp/35-remediation-publish-jsz86usw/publish`에서 명시적으로 이번 파일만 stage·commit합니다. 원래 Git index·refs·파일 498개의 해시와 게시 대상 59개를 같은 임시 작업의 backup에 보관했습니다.

원래 작업본은 Git 관리 영역이 읽기 전용이므로 해당 영역의 갱신은 파일 bytes 일치·조상 관계·staged 상태·백업을 확인한 후 승인된 실행 권한으로 진행합니다. 제한을 다른 파일이나 도구로 우회하거나 OS 권한을 바꾸지 않습니다. 원격/로컬 실제 완료 결과는 후속 기록으로 남기며, 실패하면 완료하지 않은 브랜치와 재개 지점을 구분합니다. 게시 후 복구는 검토된 revert를 사용합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
