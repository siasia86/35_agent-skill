# 35 `agent-skill`

**저장소 버전: 1.0.0** — 2026-10-01 기존 Codex 개발본을 이력 보존 영역으로 옮기고 개인 스킬 모음을 새로 구성합니다. 버전은 [VERSION](VERSION)과 [CHANGELOG](CHANGELOG.md)에서 관리합니다. Git main 게시나 runtime 설치 상태를 뜻하지 않습니다.

## 1. 목적

Kiro에서 사용하던 개인 규칙·템플릿·워크플로를 Codex에서 유지합니다. 사용자의 명시 지시 > 적용 저장소 지침 > 개인 범용 스킬 기본값을 플랫폼 정책·현재 권한 안에서 적용합니다. 이식 단계에서 내용 삭제·축약·통합을 하지 않습니다. 경량화는 이후 별도 검토입니다.

## 2. 구성

- `kiro/`: 실제 Kiro 개인 스킬·prompt·스타일의 보존 원본.
- `gpt/`: 이전 GPT/Codex 이식의 보존 원본.
- [codex/](codex/README.md): 폴더 단위로 단독 복사하는 Codex 개인 스킬 19개, 선택적 개인 지침 예시와 검증 기록.
- [105_backup/codex](105_backup/codex/README.md): 폐기한 개발본·payload·catalog·설치기·governance·검증 이력. 새 설치 원본으로 사용하지 않습니다.
- [agent-workflows](agent-workflows/README.md): 적용 절차와 과거 환경별 설치 관찰.
- `claude/`: 기존 예약 영역.
- [_reference](_reference/INDEX.md): 기존 참고 자료.

이동 전 루트 안내는 [보존 README](105_backup/codex/REPOSITORY_README.before-1.0.0.md)에 남겼습니다. 기존 30·31 연동은 과거 중앙 관리 개발 이력이며 새 개인 스킬의 필수 의존성이 아닙니다. 다른 저장소나 개인 홈은 이번 요청에서 변경하지 않습니다.

## 3. 개인 스킬의 사용 단위

새 스킬은 `codex/skills/<이름>/` 전체를 실행 사용자의 `~/.agents/skills/<이름>/`에 복사하는 형태로 작성합니다. 스킬 폴더 안에 필요한 자료를 포함하고 다른 스킬의 별도 설치·catalog·installer·30·31 저장소를 요구하지 않습니다. Git·Python·Terraform 같은 작업 도구와 해당 작업의 권한은 실제 실행 환경에서 확인합니다.

[수동 복사 안내](codex/README.md#2-수동-복사), [원문 대응과 변경 이유](codex/MIGRATION.md), [19개 스킬 검증 결과](codex/VERIFICATION.md)를 확인합니다. 원문 본문은 유지하고 Codex 호환 절을 추가했습니다. 실제 원본이 없는 개인 보안 도구의 배포·map 호환성은 별도 미검증으로 명시합니다.

스킬 생성과 폴더 복사 검증을 실제 개인 홈 설치·자동 발견·운영 적용으로 처리하지 않습니다. 기존 동명 스킬이 있으면 백업·비교하고 사용자 편집을 보존합니다. 개인 설정 예시와 실제 개인 config도 구분합니다.

## 4. 작업과 검증

- [TODO2](TODO2.md): 원문 보존·최소 호환성 수정·후속 경량화 검토 기준.
- [실행 기록](agent-workflows/codex/REBUILD_1.0.0.md): 이번 6개 작업의 순서·권한·검증·게시·복구.
- [기존 TODO](TODO.md): 이전 중앙 배포 작업의 역사 기록. 과거 다음 단계는 이번 개인 스킬 작업의 자동 실행 지시가 아닙니다.
- [REVIEW](105_backup/codex/REVIEW.md): 폐기한 Codex 개발본의 리뷰와 원문 diff 결과.
- [AGENTS](AGENTS.md): 저장소 보존·작업·권한 기준.

문서의 style·heading·link, 비밀정보와 Git diff를 검사합니다. 새 스킬은 원문 대응·단독 복사·내부 참조·frontmatter와 Luna의 독립 사례 수행을 확인합니다. 통과·부분 검증·실패·미실행을 구분합니다. Terraform/AWS/배포·실제 Windows·개인 홈 설치는 별도 실행 범위입니다.

## 5. 과거 개인 적용 관찰

[Codex 관찰 자료](agent-workflows/codex/README.md)의 네 스킬 사본과 JSON은 2026-09-30에 확인한 상태입니다. 원본 commit·해시·사본을 보존하며 새 스킬 1.0.0이 해당 개인 환경에 설치됐다고 주장하지 않습니다. 사본은 독립 수정하거나 새 설치 입력으로 사용하지 않습니다.

---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-10-01

© 2026 siasia86. Licensed under CC BY 4.0.
