# 작업 문서 정책

## 1. 원본과 적용 위치

원본은 `kiro/skills/repo-governance/SKILL.md`, `kiro/skills/work-rules/SKILL.md` §23·§26, `31_governances/.governance/repository/documentation_policy.md`입니다. 저장소별 `.governance/GOVERNANCE.md`, `exceptions.md`, `verification.md`를 우선 확인합니다.

일반 프로젝트는 `.governance/ISSUE.md`, `TODO.md`, `PLAN.md`를 사용하고 기존 저장소는 루트 문서를 허용합니다. 이번 마이그레이션은 사용자가 지정한 `gpt/`에 ISSUE·TODO·PLAN·CHANGELOG를 둡니다. 다른 작업의 루트 문서나 `agent-workflows/`를 덮어쓰지 않습니다.

## 2. 문서 역할

- ISSUE: 문제의 재현, 원인, 영향, 제안, 상태를 기록합니다.
- TODO: 미착수·미완료 작업과 검증 후 완료 상태를 기록합니다.
- PLAN: 진행 중인 복합 작업의 단계, 범위, 검증, 롤백을 기록합니다.
- CHANGELOG: 완료되고 검증된 변경을 최신순으로 기록합니다.

흐름은 `ISSUE → TODO → PLAN → 구현·검증 → CHANGELOG`입니다. 단순 변경은 TODO·CHANGELOG로 처리합니다. 세 단계 이상 작업에는 PLAN을 사용합니다. 활성 내용이 없어도 문서를 삭제하지 않고 `없음`을 기록합니다.

## 3. 원본 세부 규칙

PLAN 오류 기록은 work-rules §23을 그대로 적용합니다. 비자명한 오류, escaping 문제, 코드 수정에 따른 장애 등을 해결한 직후 기록하며 같은 증상의 기존 항목에 보강합니다. 계획 문서 자체 편집은 재귀 기록하지 않습니다. ISSUE에는 원인·영향, PLAN에는 작업 중 발견한 해결 과정과 검증을 기록합니다.

TODO 배치는 work-rules §26을 그대로 적용합니다. 기본 3개 단위, 세션 간 연속 배치 번호, 마지막 1~2개도 사전·사후 보고, reference 준비 후 작성, 표 정렬, 세 가지 Markdown 검사, 대상별 fact-check 회차, 검증 후 상태 갱신 순서를 유지합니다. 중단 후 다음 미완료 항목부터 재개합니다. README·CHANGELOG는 마지막 배치에서 갱신하고 보류 여부를 보고합니다.

일반 문서의 푸터·날짜·배지와 참고 링크 별점은 `markdown/STYLE.md`, `readme-template`에 따릅니다. Skill 정의·목록과 `_reference/` 예외를 일반 문서 전체에 확대하지 않습니다. 검사 예외는 원본 정책 또는 ISSUE의 명시적 근거가 있어야 하며, 검사 실패를 숨기기 위한 전체 비활성화는 하지 않습니다.

---

## 통계

![GitHub stars](https://img.shields.io/github/stars/siasia86/system-engineering-resources?style=social)
![GitHub forks](https://img.shields.io/github/forks/siasia86/system-engineering-resources?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/siasia86/system-engineering-resources?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/siasia86/system-engineering-resources)
![License](https://img.shields.io/github/license/siasia86/system-engineering-resources)
![Actions](https://img.shields.io/github/actions/workflow/status/siasia86/system-engineering-resources/update-date.yml)

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-21

© 2026 siasia86. Licensed under CC BY 4.0.
