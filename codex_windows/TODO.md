# Codex Windows 미완료 작업

세부 단계는 [PLAN](PLAN.md), 확인된 제약은 [ISSUE](ISSUE.md), 현재 검증 범위는 [REVIEW](REVIEW.md)에 둡니다. 이 색인은 구현·설치의 자동 실행 지시가 아닙니다. 4절은 향후 Windows 구현의 게시 순서이며 이번 분리·골격 게시 상태는 [분리 기록](../agent-workflows/codex/PLATFORM_SPLIT_2026-10-03.md)에서 확인합니다.

## 1. 준비와 범위

- [x] Windows 계획·이슈·검토·구현 영역의 문서 골격을 작성합니다.
- [x] 직접 Windows fixture 검사와 미검증 범위를 구분해 기록합니다.
- [x] [Linux 원문](../codex_linux/README.md)의 이동 전후 보존과 활성 링크를 최종 확인합니다.
- [ ] Windows 실행 조건과 작업 예시를 확정합니다.
- [ ] 우선 skill·선택 이유·필수 동반 자료를 정합니다.
- [x] 기존 Linux skill 19개의 [검토 결과](../agent-workflows/codex/SKILL_REVIEW_2026-10-03.md)와 Windows 재작성에 반영할 실패 사례를 연결합니다.
- [ ] 선택한 Windows skill에 관련 복구·입력 검증·오류 전파·Markdown 실패 사례의 재발 방지 조건을 반영합니다.

## 2. Windows 구현

- [ ] 선택한 skill의 Windows `SKILL.md`와 원문 대응을 작성합니다.
- [ ] 필요한 PowerShell/Python 전용 코드와 자료를 작성합니다.
- [ ] UTF-8 읽기·쓰기·출력과 오류 전파를 명시합니다.
- [ ] POSIX 의존 기능의 대체·조건부 지원·미지원 범위를 정합니다.
- [ ] 각 폴더의 단독 사용과 내부 참조를 확인합니다.

## 3. 검증과 적용

- [ ] Windows 최종본의 정상·실패·한국어 문서 사례를 검사합니다.
- [ ] 대표 모델 행동과 실제 입력 해시를 확인합니다.
- [ ] 필요한 경우 Windows 메타데이터·동시 잠금 범위를 검증합니다.
- [ ] 사용자 선택 범위에서 개인 설치·새 세션 발견·명시 호출을 확인합니다.

## 4. 게시 순서

- [ ] 완료된 변경과 검사 결과를 yunli에 push합니다.
- [ ] 사용자의 검증 결과와 보완 여부를 기록합니다.
- [ ] 사용자 검증 후 main에 반영·push하고 결과를 확인합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
