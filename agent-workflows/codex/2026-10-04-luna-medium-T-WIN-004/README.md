# T-WIN-004 Luna medium 배정 수정

## 1. 변경 범위

사용자의 최신 요청에 따라 [work-rules](../../../codex_windows/skills/work-rules/SKILL.md)와 [운영 상세](../../../codex_windows/skills/work-rules/references/operating-details.md)의 단순 수집·정형 추출 배정을 `gpt-6-luna / medium`으로 변경합니다. 최저 effort 선택 기준을 제거하고 비용만을 이유로 low로 낮추지 않도록 명시합니다. 짧은 조회 직접 처리·묶음 추출·간결 반환·오류 인계·Sol 판단 기준은 유지합니다.

[이전 low 적용 기록](../2026-10-04-cost-routing-T-WIN-004/README.md)은 당시 이력으로 보존하며 이번 기준으로 대체합니다. 기존 T-WIN-004의 후속이며 새 Goal·모델 설정·다른 skill 변경은 포함하지 않습니다.

## 2. 검증과 적용

변경 전 원본·설치본 전체 44파일의 해시 일치와 로컬 차이 0건을 확인하고 Git 제외 private/before에 두 전체 폴더와 해시를 보존했습니다. 의미 검토에서 medium 지정과 지원 확인·오류 인계의 일관성을 확인했습니다. 원본·설치본 구조 검사와 변경 Markdown 3개의 링크·헤딩·표현 검사, git diff 검사를 통과했습니다. 기존 격리 검증 의존성을 재사용했고 skill 두 문서에는 기존 푸터 비강제 기준을 적용했습니다. work-rules 전체 44파일을 설치하고 원본·설치본의 파일 목록·SHA-256 일치를 확인했습니다. before/after 전체 사본과 로그를 이번 private에 보존했습니다. 이번 수정에서 실제 Luna 위임 실행이나 새 세션 자동 선택은 시험하지 않습니다.

## 3. 복구

현재 설치본과 이번 after 해시를 비교하여 이후 변경을 보존한 뒤 private/before의 지정 skill 폴더를 선택 복원하거나 병합합니다. 다른 skill·개인 설정은 복구 범위에 포함하지 않습니다. 공개 원본은 담당 변경만 검토한 revert로 복구합니다. 게시 SHA는 비공개 실행 기록과 완료 보고에 남깁니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
