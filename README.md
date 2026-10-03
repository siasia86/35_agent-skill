# 35 `agent-skill`

현재 플랫폼 진입점은 [Linux 보존본](codex_linux/README.md)과 [Windows 전체 이관본](codex_windows/README.md)입니다. 19개 skill·필수 자료·현재 공통 설정을 모두 Windows에 이관하고 [검토 결과](codex_windows/REVIEW.md)·[TODO](codex_windows/TODO.md)를 확인합니다. 최적화는 이관 이후입니다. [분리 기록](agent-workflows/codex/PLATFORM_SPLIT_2026-10-03.md)에 경로 대응·검증·복구와 게시 상태를 남깁니다.

**저장소 버전: 1.0.0** — 2026-10-01 기존 Codex 개발본을 이력 보존 영역으로 옮기고 개인 스킬 모음을 새로 구성합니다. 버전은 [VERSION](VERSION)과 [CHANGELOG](CHANGELOG.md)에서 관리합니다. Git main 게시나 runtime 설치 상태를 뜻하지 않습니다.

## 1. 목적

각 AI 도구의 특성과 사용 환경에 맞게 에이전트 설정을 최적화합니다. 도구별 Agent·Skill·Prompt와 개인 규칙·템플릿·워크플로를 관리하고, 적용·업데이트·검증 절차를 정리합니다.

사용자의 명시 지시 > 적용 저장소 지침 > 개인 범용 스킬 기본값을 플랫폼 정책·현재 권한 안에서 적용합니다.

도구별 Agent·Skill·Prompt는 독립 사용을 기본으로 하며, 31 저장소의 설치·설정·실행 없이 사용할 수 있도록 구성합니다. 현재 작업공간에 31 저장소에서 관리하는 설정이 적용되어 있으면, 해당 설정을 확인하고 그 적용 범위와 지침에 따라 함께 사용합니다. 필요한 실행 도구와 버전은 도구별 안내에서 확인합니다.

개인 공통 구성과 저장소별 구성을 구분합니다. 구현 원본은 도구별 디렉토리에서 관리하고, 적용 절차와 환경·사용자·작업공간별 관찰 및 검증 결과는 `agent-workflows/`에서 관리합니다. 독립 사용은 저장소 전체의 설계 원칙이며 실제 구현·검증 상태는 도구별로 기록합니다.

## 2. 구성

- `kiro/`: 실제 Kiro 개인 스킬·prompt·스타일의 보존 원본.
- `gpt/`: 이전 GPT/Codex 이식의 보존 원본.
- [codex_linux/](codex_linux/README.md): 폴더 단위로 단독 복사하는 Codex 개인 스킬 19개, 선택적 개인 지침 예시와 검증 기록.
- [codex_windows/](codex_windows/README.md): Windows용 개인 skill19개 전체·동봉 자료·필요 도구·공통 지침/설정 예시·검증 결과.
- [105_backup/codex](105_backup/codex/README.md): 폐기한 개발본·payload·catalog·설치기·governance·검증 이력. 새 설치 원본으로 사용하지 않습니다.
- [agent-workflows](agent-workflows/README.md): 공통 적용 절차, 환경·사용자·작업공간별 관찰과 검증 기록 및 과거 설치 사본.
- `claude/`: 기존 예약 영역.
- [_reference](_reference/INDEX.md): 기존 참고 자료.

이동 전 루트 안내는 [보존 README](105_backup/codex/REPOSITORY_README.before-1.0.0.md)에 남겼습니다. 기존 30·31 연동은 과거 중앙 관리 개발 이력이며 새 개인 스킬의 필수 의존성이 아닙니다. 다른 저장소나 개인 홈은 이번 요청에서 변경하지 않습니다.

## 3. 개인 스킬의 사용 단위

기존 Linux 스킬은 `codex_linux/skills/<이름>/` 전체를 실행 사용자의 `~/.agents/skills/<이름>/`에 복사하는 형태로 작성합니다. 스킬 폴더 안에 필요한 자료를 포함하고 다른 스킬의 별도 설치·catalog·installer·30·31 저장소를 요구하지 않습니다. Git·Python·Terraform 같은 작업 도구와 해당 작업의 권한은 실제 실행 환경에서 확인합니다.

사용자 홈에 설치한 스킬은 같은 사용자로 작업하는 여러 저장소에서 사용할 수 있습니다. 저장소별 구성이 필요하면 해당 저장소의 `.agents/skills/<이름>/`에 선택한 폴더를 배치합니다. 같은 이름의 스킬이 여러 범위에 있으면 중복과 실제 선택 대상을 확인합니다. [Codex 적용 범위](codex_linux/README.md#21-적용-범위)와 [환경·작업공간별 기록 기준](agent-workflows/README.md#41-환경과-작업공간별-기록)을 따릅니다.

[수동 복사 안내](codex_linux/README.md#2-수동-복사), [원문 대응과 변경 이유](codex_linux/MIGRATION.md), [19개 스킬 검증 결과](codex_linux/VERIFICATION.md)를 확인합니다. 현재 Codex 개인 스킬 작업은 Kiro의 개인 규칙·템플릿·워크플로를 원문 보존 방식으로 이식한 것입니다. 이 이식 단계에서는 내용 삭제·축약·통합 없이 Codex 호환 절을 추가했으며, 경량화는 이후 별도 검토입니다. 실제 원본이 없는 개인 보안 도구의 배포·map 호환성은 별도 미검증으로 명시합니다.

스킬 생성과 폴더 복사 검증을 실제 개인 홈 설치·자동 발견·운영 적용으로 처리하지 않습니다. 기존 동명 스킬이 있으면 백업·비교하고 사용자 편집을 보존합니다. 개인 설정 예시와 실제 개인 config도 구분합니다.

## 4. 작업과 검증

- [Windows 전체 이관](agent-workflows/codex/WINDOWS_MIGRATION_2026-10-03.md): 19개·182파일·54동봉역할과 설정2개 대응, 최소 호환 수정·직접 검사·미실행 범위.

- [2026-10-03 skill 내용 검토](agent-workflows/codex/SKILL_REVIEW_2026-10-03.md): 19개 skill의 현재 수정 필요 14건과 실제 재현·미실행 범위. 원문·실행 코드 보완은 후속입니다.

- [세션 인계](agent-workflows/codex/HANDOFF.md): 마지막 게시 상태·미게시 변경·추가 검토 근거·다음 세션의 재개 순서. 플랫폼별 후속은 [Linux TODO](codex_linux/TODO.md)와 [Windows TODO](codex_windows/TODO.md)에서 확인합니다.
- [2026-10-03 병합 검토와 실제 통합](agent-workflows/codex/MERGE_REVIEW_2026-10-03.md): 전체 원격 브랜치의 검토 결과, 원문 보존·동작 제한과 후속 요청의 원격/로컬 main·yunli 통합 상태.
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

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
