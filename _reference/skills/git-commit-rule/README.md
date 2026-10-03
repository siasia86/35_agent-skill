---
name: git-commit-rule-source-notes
last_checked: 2026-10-03
sources:
  - codex_windows/skills/git-commit-rule/SKILL.md
  - codex_windows/skills/git-commit-rule/references/kiro-original.md
source_commit: 16817d70a753707aad8e12c9311076b3c387203f
---

# git-commit-rule 원본 연결

## 1. 출처와 역할

이 skill은 35 내부에서 관리하는 커밋 skill입니다. 입력 기준은 `35_agent-skill@16817d7`이며 이번 T-WIN-003에서 호출·참고 원본·작업 기록 안내를 보완합니다. 외부 독립 저장소 URL은 제공되지 않았으므로 같은 repo를 다시 clone하지 않습니다.

- [Windows 관리 원본](../../../codex_windows/skills/git-commit-rule/SKILL.md)
- [Kiro 비교 원문](../../../codex_windows/skills/git-commit-rule/references/kiro-original.md)
- [Linux 비교 원문](../../../codex_windows/skills/git-commit-rule/references/linux-original.md)
- [35 적용 작업](../../../agent-workflows/codex/2026-10-03-personal-skills-T-WIN-003/README.md)

## 2. 사용과 갱신

Windows 관리 원본의 폴더 전체를 개인 사용자 또는 해당 repo의 지원 skill 위치에 적용합니다. 명시 호출은 `$git-commit-rule`와 대상·결과 범위를 함께 지정합니다. 미설치 상태에서는 위 SKILL 경로를 읽어 적용하도록 요청하며 이를 설치·자동 발견으로 보고하지 않습니다.

참고·역사 사본은 독립 편집하거나 자동 실행하지 않습니다. 출처가 추가되면 URL·commit·확인일·라이선스·현재 실행본과의 차이를 기록하고 검증한 수정만 관리 원본에 반영합니다. 설치·이전본·해시·검증은 업데이트별 백업 폴더의 실제 관찰 기록을 따릅니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
