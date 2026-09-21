# Codex Skill Migration TODO

사용자 요청에 따라 기존의 선별·축약 계획을 원본 커스텀 규칙 보존 방식으로 변경했습니다. 이전 완료 표시는 아래 검증 범위로 정정합니다.

## 1. 완료한 변환

- [x] 기준 원본을 저장소 `kiro/`로 고정합니다.
- [x] 19개 Skill 본문을 보존하며 Skill URI와 자산 경로를 변환합니다.
- [x] 7개 Agent의 prompt와 역할을 보존하고 Codex TOML로 변환합니다.
- [x] 13개 Prompt와 Markdown 정책을 보존합니다.
- [x] system-engineer 중심 주 세션 지침과 상세 정책 연결을 복원합니다.
- [x] TODO·PLAN·ISSUE·CHANGELOG의 원본 역할·갱신 규칙을 연결합니다.
- [x] 불필요·미지원·충돌 후보는 삭제 대신 ISSUE에 기록합니다.
- [x] 네 저장소 자동 검토 설정과 사용자 프로필의 실제 로더 확인을 수행합니다.

## 2. 완료로 간주하지 않는 항목

- [ ] 원본의 모든 설명·예시를 현재 공식 문서와 대조합니다.
- [ ] 외부 스크립트·MCP·잠금·hook 의존성을 실행 환경에서 검증합니다.
- [ ] Skill 자동 선택과 명시 호출을 실제 모델 세션으로 검증합니다.
- [ ] 7개 Agent의 실제 위임 동작과 모델 상속을 검증합니다.
- [ ] 접근 불가한 agent-workflows/gpt 문서와 충돌을 대조합니다.
- [ ] Markdown 검사 잔여 사항을 원본 오류와 변환 오류로 분류합니다.

## 3. 완료 기준

모든 원본 자산이 대응표와 해시 manifest에 있고, 커스텀 규칙은 반영되거나 ISSUE에 미반영 근거가 있어야 합니다. 정적 확인·설정 로드·실제 모델 동작 검증을 구분합니다. 상세 진행은 [TODO.md](TODO.md)에서 이어갑니다.

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
