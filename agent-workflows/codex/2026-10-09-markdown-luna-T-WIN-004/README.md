# Markdown 검사·간단한 스크립트 위임 규칙 갱신

**작업 ID**: `T-WIN-004 / MD-LUNA-20261009-01`

**기준 HEAD**: `ddcf0a297e6fb65eac0574188a5c8e656fd71f68`

## 범위와 변경

사용자의 전역 요청에 따라 총괄을 포함한 모든 역할에서 정해진 검사, 정형 추출, 입출력 절차가 명확한 단순 스크립트 실행, 합의된 기계적 수정을 Luna 6.0 `medium` subagent에 작업 묶음 단위로 기본 위임하도록 지침을 갱신했습니다. 소유 담당자가 배정하고, 이미 배정받은 worker는 직접 실행해 재위임하지 않으며, 소유 담당자가 결과를 판정합니다. 검색·비교·추론·설계·상태·권한 판단은 기존 담당자가 계속 결정하며, 단순 실행은 기존 승인·권한을 확장하지 않습니다.

담당 변경 파일은 다음과 같습니다.

- `codex_windows/skills/work-rules/SKILL.md`: 전역 기본과 Markdown 세부 지침 연결
- `codex_windows/skills/work-rules/references/operating-details.md`: 배정·반환·오류 처리 기준
- `codex_windows/skills/md-link-check/SKILL.md`: Markdown 전용 검사 범위·정형 수정 기준
- `codex_windows/AGENTS.md`: 공통 선택 안내
- `agent-workflows/codex/2026-10-09-markdown-luna-T-WIN-004/README.md`: 이번 기록

Markdown 검사는 위 다섯 파일을 대상으로 저장소 지정 검사기·설정을 먼저 확인한 뒤 동봉 검사기로 실행했습니다. 대상별 파일 링크, 같은 파일 앵커, 교차 파일 앵커 검증 범위를 구분합니다. 원본 Kiro 본문과 기존 예시는 유지했으며 검사기·스크립트는 수정하거나 추가하지 않았습니다.

## 위임·보존·복구

위임 호출은 `gpt-6-luna / medium`으로 명시되었고 호출이 성공했습니다. 별도 모델 설정은 바꾸지 않았습니다. 설치 단계는 이미 배정된 Luna worker가 직접 수행했으며 재위임하지 않았습니다. 현재 총괄 세션에서 새 AGENTS 지침이 실제 context에 반영된 관찰을 확인했으나, 다른 채팅의 실제 실행은 관찰하지 않았습니다. 검토된 두 skill 폴더 전체를 설치했고 work-rules 44개, md-link-check 18개 원본 파일의 SHA-256이 설치본과 모두 일치합니다. md-link-check 설치 전용 캐시 3개는 기존 해시 그대로 보존했습니다. 개인 AGENTS에는 승인된 한 줄만 병합했으며 기존 로컬 관리 원본 위치 부록을 byte 단위로 보존했습니다. Git 게시·staging·commit·push는 아직 하지 않았습니다.

작업 전 원본과 설치본 해시·백업은 Git 제외 `private/`에 보존했습니다. `baseline.json`, `before-source/`, `before-installed/`, `before-source-personal-AGENTS.md`, `before-installed-personal-AGENTS.md`가 복구 비교 자료입니다. `before-source-operating-details.md`는 기준 HEAD에서 재구성한 원문 대조본입니다. 설치 후 전체 파일별 해시는 `after-install.json`에 저장했습니다. 기존 설치본 차이는 md-link-check의 Python 캐시 세 파일로 확인해 그대로 보존했습니다. 복구가 필요하면 현재 담당 diff를 기준 HEAD와 대조하고, 통합 담당자가 검토한 변경만 되돌립니다.

## 검사 기록

검사 Python은 Windows에 이미 있는 Python 3.14를 `-X utf8 -B`로 실행했습니다. 검사 스크립트는 설치본 `md-link-check/scripts/`의 세 파일을 사용했습니다. style, heading, link 검사기의 SHA-256은 각각 `89a5bbf25979be2ccac556d1624e89dfbe1a2db132d9f3bd098ca98660574268`, `16c3de7712ef8987216b3b4e519d9bce5214fb15f78a69865e7441805bdf85d3`, `6991d56bf10c1ec6eaa8cbb9add5ff2e8bd3231a6cf8c534856736205983e5e6`입니다. 저장소 지정 도구·설정은 확인되지 않아 동봉 검사기를 사용했습니다.

각 파일을 세 검사기에 개별 지정해 호출했으며 매 호출 검사 파일 수는 1개입니다. 대상별 종료 코드·검사 결과는 다음과 같습니다.

- `work-rules/SKILL.md`: style 1(푸터 누락 3건), heading 0(헤딩 5개·이슈 0건), link 0(링크 19개·깨짐 0건)
- `work-rules/references/operating-details.md`: style 1(푸터 누락 3건), heading 0(헤딩 4개·이슈 0건), link 0(링크 0개·깨짐 0건)
- `md-link-check/SKILL.md`: style 1(푸터 누락 3건), heading 0(헤딩 26개·이슈 0건), link 0(링크 3개·깨짐 0건)
- `codex_windows/AGENTS.md`: style 1(푸터 누락 3건), heading 0(헤딩 2개·이슈 0건), link 0(링크 0개·깨짐 0건)
- 이번 `README.md`: style 0(이슈 0건), heading 0(헤딩 4개·이슈 0건), link 0(링크 0개·깨짐 0건)

기준 원본 네 파일(`work-rules/SKILL.md`, `md-link-check/SKILL.md`, `operating-details.md`, `codex_windows/AGENTS.md`)에도 같은 세 검사를 적용했습니다. 각 원본의 style는 같은 푸터 누락 3건, heading은 각각 5·25·4·2개 헤딩에 0건, link는 각각 19·3·0·0개 링크에 0건이었습니다. 따라서 푸터 3건씩은 기존 진단이며 새 헤딩·파일 링크 진단은 없습니다. 설치 후 파일 해시·개인 AGENTS 병합 검증에서도 신규 진단은 없습니다. 이번 변경은 새 교차 파일 앵커 연결을 만들지 않으며, md-link-check는 이미 제공될 때만 참고하는 선택 자료입니다.

개인 AGENTS 설치본과 배포 원본의 차이는 설치본에만 있던 다섯 줄의 로컬 관리 원본 안내입니다. 원본·설치본 모두 개인 경로가 포함될 수 있어 전후 파일은 Git 제외 `private/`에 보존하고 공개 기록에는 경로를 복사하지 않았습니다. 이 차이를 보존했습니다.

로컬 Python으로 `skill-creator`의 `quick_validate.py`를 실행했으나 `yaml`이 없어 import 단계에서 종료 코드 1을 반환했습니다. 번들 Python에서는 `yaml` 가져오기만 확인해 같은 모듈 부재를 관찰했습니다. 의존성은 설치하지 않았으며 공식 quick_validate 통과는 미확인입니다. 대신 `agent-workflows/codex/windows/verification/verify_current.py`의 stdlib 함수 `check_metadata`, `active_skill_body`, `markdown_helper`, `check_links`를 두 skill에 직접 적용했습니다. frontmatter는 기준 HEAD와 같고 name/description이 유효하며 COMPAT 블록과 동봉 파일 링크(work-rules 19개, md-link-check 3개)가 정상이고 교차 skill 상대 링크는 0개임을 확인했습니다. 현재 verify_current는 repo 전체 inventory 검사만 지원해 두 skill 지정 모드로 실행할 수 없으므로 이 결과는 부분 구조 확인이며 공식 검증 전체를 대신하지 않습니다.

작업 전후 원본의 기준·최종 SHA-256과 변경 diff는 root의 통합 검토에서 대조합니다. 설치·게시 완료 여부는 후속 소유자 검토와 별도로 판정합니다.

---

**작성일**: 2026-10-09

**마지막 업데이트**: 2026-10-09

© 2026 siasia86. Licensed under CC BY 4.0.
