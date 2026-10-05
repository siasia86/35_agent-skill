# MAIN-20261004-01 현행 스킬 검증 계약 교정

## 1. 범위와 원인

담당은 12_github-main, 기존 ID는 SKILL-35:MAIN-20261004-01·T-WIN-002 후속, 재개 배정은 ZWS-RESUME-20261005-02입니다. 시작 기준은 main `18dbc416e171006a4f08732b55348089fea59a36`이며 작업 트리는 깨끗했습니다. 재시작 대기만 해제했으며 다른 담당 변경·기존 사용자 보류는 유지합니다. 활성 Goal은 없고 새 Goal을 만들지 않았습니다.

[기존 검증기](../../verification/verify_current.py)가 현재 스킬 목록과 최초 이관 19개를 동일하게 강제하고 모든 SKILL에 COMPAT 블록을 요구했습니다. 현재 배포 21개에서 `Current skill inventory differs`, 종료 코드 1을 재현하고 before 사본·로그를 보존했습니다. 단순 수량 변경으로 고치면 native 두 스킬의 형식을 잘못 검사하므로 계약을 분리했습니다.

## 2. 변경과 담당 파일

- [현재 목록](../../verification/current_inventory.json)은 검토한 이름과 COMPAT/native 형식을 명시합니다. 폴더 탐색으로 기대 목록을 자동 갱신하지 않아 누락·미등록 추가·SKILL 누락을 잡습니다.
- 검증기는 현재 21개와 역사 이관 19개를 분리합니다. source_manifest의 파일 182개·설정 2개·보존 해시 368건과 이동 7개는 유지하고 기존 역사 스킬이 현재 COMPAT 목록에 남아 있는지 확인합니다.
- COMPAT 19개는 한 쌍의 순서가 맞는 활성 블록과 현재 Windows 참조를, native fact-check·goal-continuation 2개는 전체 Markdown과 agents/openai.yaml 인터페이스를 검사합니다.
- [32개 회귀](../../verification/test_current.py)는 TEMP 사본의 누락·추가·메타데이터·형식·파일 링크·코드 예시/펜스·역사 파일/설정/이동 해시 변조를 검사합니다. [잠금 회귀](../../verification/test_patterns.py)도 같은 명시 목록과 활성 본문 선택을 재사용합니다. 이전 구현은 신규 native SKILL에서 COMPAT 분할에 실패할 수 있었습니다.
- [검증 안내](../../verification/README.md)와 [Windows TODO](../../TODO.md)의 관련 상태·근거만 갱신합니다. [다른 소유 담당의 운영 규칙 대조 기록](../../../2026-10-05-runtime-rules-followup-T-WIN-004/README.md)은 총괄이 반환한 후보를 내용·해시·공개 범위로 인수하고, 읽기 전용 대조를 직접 개정/설치로 오해하지 않도록 한 문단만 보완했습니다. 기존 44파일 대조는 입력 변경이 없어 재사용했습니다.

이번 commit 대상은 위 검증 파일 5개와 Windows TODO, 운영 규칙 대조 기록, 이 README·validation.json입니다. 02 공통 문서·Git index, 역사 manifest·원형 보존 자료, codex_windows의 skill·개인 설치본·config는 직접 수정하지 않습니다. 다른 담당의 fact-check 후속 기록은 아직 인수하지 않아 제외합니다.

## 3. 실제 검증과 검토

[검증 요약](validation.json)은 이번 입력에서 직접 실행한 결과입니다. 전체 현재 검사 21개, COMPAT 19개·native 2개·인터페이스 2개, 역사 해시 368건, 파일 참조 78개, Python AST 34개와 독립 helper 27개를 통과했습니다. mutation 회귀 32개, Markdown 91개, Python/Git Bash runtime 108개, Windows byte 잠금 7개와 공식 quick_validate 21개도 통과했습니다. 새 패키지는 설치하지 않고 기존 개발 검증 의존성을 재사용했습니다.

Astra/high를 명시 선택하여 검증 계약과 위험을 읽기 전용 검토했습니다. 주석만 있거나 주석 뒤 자료형인 메타데이터를 문자열로 인정하는 문제와 URL 인코딩된 파일명 `#`를 앵커로 잘라내는 문제를 발견하여 수정·회귀에 추가했습니다. reviewer는 시험·수정·게시를 하지 않았으며 root가 수정된 구간과 최종 검사 결과를 통합했습니다. 초기 29개 회귀 통과와 보완 후 32개 통과를 구분합니다.

링크 검사는 인라인 파일 존재와 폴더 내부 의존성을 대상으로 합니다. 참조형 링크·다른 파일 앵커·외부 URL 도달성·역사 참조 전체는 완료로 확장하지 않습니다. 원본/설치본 대조 기록의 게시를 실제 독립 세션 선택·행동 완료로 바꾸지 않습니다.

## 4. 02 잔여 후보 읽기 전용 비교

02의 비교 기준은 main `238fa755c18d1ba391861b44478af8362658548f`, 잔여 yunli commit은 `4539f8169a08db07e3b485648bd5bb63b7e55cff`입니다. 원격을 새로 조회하지 않은 로컬 refs 비교이며 잔여 commit 하나만으로 내용 미반영을 단정하지 않습니다. 다섯 후보 경로에서 README·INDEX·CHANGELOG는 후속 구성으로 달라졌고 원래 분석/검증 결과 두 파일은 main의 원래 경로에 없습니다.

현행 GWS-20261004-01 분석·github INDEX/PLAN/TODO가 목적·역할·조사→clone→구현 흐름을 선별 재사용하고 출처 commit을 명시합니다. 따라서 과거 공통 문서 세 개의 델타를 그대로 병합하는 방식을 권하지 않습니다. 원래 결과 두 파일을 역사 자료로 보존할 필요가 있다면 해당 파일만 복원하는 후보 diff를 총괄이 검토할 수 있도록 Git 제외 증거에 반환했습니다. 적용·정책 판단·공통 문서 연결·02 게시는 총괄 소유이며 수행하지 않았습니다. 읽기 전용 비교 전후 02 Git index 해시 동일성을 확인했습니다.

## 5. 보존·게시·복구와 남은 조건

이번 지정 입력의 before 사본·현재 목록·검사 원형 로그·보호 파일 해시·담당 staging/게시 receipt는 Git 제외 `agent-workflows/codex/2026-10-05-current-verifier-MAIN-20261004-01/private/`에 보존합니다. 공개 요약에는 개인 경로·설정·계정·원시 stdout을 복사하지 않습니다. 보호 대상 647개 파일의 해시 차이 0건을 확인했습니다. 담당 Markdown 4개·파일 링크 48개·헤딩 19개와 교차 앵커 4개를 확인했고 표현·파일 링크·헤딩 검사는 각각 종료 코드 0입니다. 비밀정보·diff 검사와 실제 게시 근거는 최종 staging 및 원격 확인 결과로 연결합니다.

일반 main에서 검증한 담당 파일만 commit·일반 push하고 원격 SHA·commit 링크를 최종 보고합니다. 기록 commit의 실제 SHA는 Git 이력과 비공개 receipt로 확인하며 검사 기준 HEAD를 게시 commit처럼 표시하지 않습니다. 필요 시 현재 사용자 변경과 before 사본을 대조하고 담당 변경만 복원하며 게시 후에는 검토한 revert로 복구합니다. force push·다른 브랜치 삭제·설정 변경으로 되돌리지 않습니다.

개인 홈 설치·config 수정·새 세션의 암시적 발견/선택·실제 행동·ACL/ADS/SMB/WSL·게임/DB/runtime/release·02 수정은 미실행입니다. 기존 Windows TODO의 독립 실제 행동 후속과 총괄의 02 역사 자료 보존 판단은 남아 있습니다.

---

**작성일**: 2026-10-05

**마지막 업데이트**: 2026-10-05

© 2026 siasia86. Licensed under CC BY 4.0.
