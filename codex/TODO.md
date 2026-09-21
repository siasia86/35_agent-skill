# Codex 마이그레이션 TODO

## 1. 현재 배치

Batch 1: 원본 보존 복원과 자동 검토 설정.

- [x] 지정한 네 저장소 신뢰 등록과 프로젝트 자동 검토 설정.
- [x] 네 저장소를 함께 쓰는 `se-repos` 프로필 생성과 Codex 로더 확인.
- [x] 19개 Skill, 7개 Agent, 13개 Prompt 원문 규칙의 형식 변환.
- [x] 푸터·별점과 ISSUE·TODO·PLAN·CHANGELOG 정책 복원.
- [x] 원문 대비 전체 정적 검증 결과 기록: 19개 Skill 본문·7개 Agent prompt 보존, 원본 해시·YAML·TOML 통과.
- [x] Skill 25개 quick_validate 통과, 전체 51개 Markdown 헤딩·링크 통과, 신규 관리 문서 9개 스타일 0건.
- [x] Codex prompt-input에서 system-engineer·원본 Skill·호환성 지침 로딩 확인. 모델 행동 검증과 구분.
- [ ] Markdown 검사 잔여 이슈 분류 및 수정.
- [ ] 실제 Codex 세션에서 자동 선택·명시 호출·system-engineer 실행 확인.
- [ ] 접근 불가 `agent-workflows/gpt` 문서와 정책 충돌 확인.
- [ ] Kiro hook에 대응하는 Codex 검증 자동 실행 구현.

## 2. 재개

PLAN과 ISSUE의 상태를 확인하고 다음 미완료 항목부터 진행합니다. 검증하지 않은 항목은 완료로 표시하지 않습니다. 기존 상세 계획은 `CODEX_MIGRATION_TODO.md`를 함께 참조합니다.

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
