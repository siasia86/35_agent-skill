# Codex 자산 정적 감사

## 범위와 판정 기준

이 문서는 `gpt/` 원본과 `codex/` 복사본의 skill 25개, agent TOML 10개를 **읽기 전용으로 정적 감사**한 기록입니다. 전체 포팅, 런타임 로딩, 권한·model·sandbox 동작 검증은 완료되지 않았습니다. 원본의 예제 명령과 지침은 실행하지 않았습니다.

모든 대응은 `gpt/<상대경로> → codex/<같은 상대경로>`입니다. 기준 출처·해시·초기 복사 상태는 [BASELINE_MANIFEST.json](BASELINE_MANIFEST.json)을 따릅니다. 아래 `개인`은 재사용 후보, `프로젝트`는 저장소 지침과 함께 제한할 후보입니다.

표기: `이식`은 재사용을 위한 이식 후보(완료 아님), `유지`는 원본 보존 우선, `제한`은 외부 의존 또는 적용 조건을 분리해야 하는 후보입니다. `상세prompt`는 `prompts/` 참조, `Kiro`는 hook/도구 비호환 가능성, `절대경로`는 개인 환경 의존을 뜻합니다.

## Skills — 일반 작업·검토

- `ansible-review` — `.agents/skills/ansible-review/SKILL.md`; 제한: 상세prompt `prompts/ansible-review.md`와 정책 참조가 있어 payload 단독 사용 불가; 프로젝트.
- `bash-script-template` — `.agents/skills/bash-script-template/SKILL.md`; 제한: 운영 경로·서비스·패키지 예제가 환경 의존이며 실행 지침으로 쓰면 안 됨; 프로젝트.
- `code-review` — `.agents/skills/code-review/SKILL.md`; 이식: 일반 코드·IaC 검토 checklist로 휴대 가능; 개인.
- `debugging-and-recovery` — `.agents/skills/debugging-and-recovery/SKILL.md`; 제한: AWS·Docker·system 명령 예제는 대상 환경 승인 후에만 사용; 프로젝트.
- `doubt-driven-infra` — `.agents/skills/doubt-driven-infra/SKILL.md`; 이식: 비자명 인프라 변경의 반대 검토·승인·롤백 절차; 프로젝트.
- `fact-check` — `.agents/skills/fact-check/SKILL.md`; 제한: 상세prompt `prompts/fact-check.md`와 정책 참조 필요; 프로젝트.
- `markdown-review` — `.agents/skills/markdown-review/SKILL.md`; 제한: 상세prompt `prompts/md-review.md`와 정책 참조 필요; 프로젝트.
- `md-link-check` — `.agents/skills/md-link-check/SKILL.md`; 이식: Markdown 링크·앵커 규칙은 재사용 가능하나 검사기 설치·경로는 별도 확인; 프로젝트.
- `planning-and-breakdown` — `.agents/skills/planning-and-breakdown/SKILL.md`; 이식: 인프라 작업 분해·완료 조건 절차; 개인.
- `testing-and-verification` — `.agents/skills/testing-and-verification/SKILL.md`; 유지: `testing-guide`와 정책을 다시 읽는 진입점이므로 단독 payload 후보 아님; 프로젝트.
- `testing-guide` — `.agents/skills/testing-guide/SKILL.md`; 제한: 외부 `file:///root/.../edge_case_testing.md` 참고가 있어 내용 확인 전 범위 제한; 프로젝트.
- `using-skills` — `.agents/skills/using-skills/SKILL.md`; 제한: Kiro lock 외에도 플랫폼·관리 정책을 빠뜨린 우선순위와 광범위한 skill 연쇄 적용 규칙을 수정해야 함; 개인 후보이나 현 상태 단독 설치 금지.

## Skills — 배포·저장소·보안

- `git-commit-rule` — `.agents/skills/git-commit-rule/SKILL.md`; 제한: 개인 절대경로와 고정 branch 금지·사용 값이 있으므로 저장소별 규칙으로만 사용; 프로젝트.
- `git-release` — `.agents/skills/git-release/SKILL.md`; 유지: `git-commit-rule`·`shipping-checklist`·정책을 연결하는 진입점; 프로젝트.
- `incremental-change` — `.agents/skills/incremental-change/SKILL.md`; 이식: 단계적 IaC 변경·검증·롤백 흐름; 프로젝트.
- `kiro-lock` — `.agents/skills/kiro-lock/SKILL.md`; 제한: `~/.kiro/hooks/kiro-lock.*` hook 의존이므로 Codex runtime 대체 설계 전 이식 금지; 프로젝트.
- `repo-governance` — `.agents/skills/repo-governance/SKILL.md`; 제한: `.governance/` 탐색은 유용하지만 개인 절대경로의 도입 현황은 환경 전용; 프로젝트.
- `security-audit` — `.agents/skills/security-audit/SKILL.md`; 유지: `security-tools`와 정책을 다시 읽는 얇은 진입점; 프로젝트.
- `security-tools` — `.agents/skills/security-tools/SKILL.md`; 제한: `/root/sj_del/` 마스킹·검사 스크립트와 설정 파일에 의존; 개인 도구 설치를 별도 검증한 뒤 프로젝트별 사용.
- `shipping-checklist` — `.agents/skills/shipping-checklist/SKILL.md`; 이식: production 배포 전 checklist이나 실제 배포 명령·승인은 대상 프로젝트에서 확정; 프로젝트.
- `spec-driven-infra` — `.agents/skills/spec-driven-infra/SKILL.md`; 이식: 대규모 인프라 스펙·gate·롤백 흐름; 프로젝트.
- `work-rules` — `.agents/skills/work-rules/SKILL.md`; 제한: `sudo`, 여러 `/root/` 도구·참조, Kiro hook, 고정 절차가 섞여 있어 최소 공통 원칙만 선별; 개인+프로젝트.

## Skills — 문서·템플릿·저장소 전용

- `python-script-template` — `.agents/skills/python-script-template/SKILL.md`; 제한: `/root/sj_del/` 참고 구현과 운영 예제를 분리해야 함; 프로젝트.
- `readme-template` — `.agents/skills/readme-template/SKILL.md`; 제한: 특정 GitHub badge·footer 값이 고정되어 있어 일반 payload에는 이식하지 않음; 프로젝트.
- `zircon-readme-policy` — `.agents/skills/zircon-readme-policy/SKILL.md`; 제한: `/root/22_github_private/11_zircon/**` 전용 footer·통계 예외이므로 해당 프로젝트에서만 유지; 프로젝트.

## Agents — 검토·문서

- `code-reviewer.toml` — `.codex/agents/code-reviewer.toml`; 제한: `workspace-write`, 다수 skill·정책 참조 및 Kiro 대체 문구가 있어 참조 해소 후 프로젝트; model 미지정(세션 상속).
- `doc-reviewer.toml` — `.codex/agents/doc-reviewer.toml`; 제한: `workspace-write`, `md-link-check`·`markdown/STYLE.md`·정책 참조 필요; 프로젝트; model 미지정(세션 상속).
- `docs-reviewer.toml` — `.codex/agents/docs-reviewer.toml`; 이식 후보: 읽기 전용 문서 검토 역할; `markdown-review`·`fact-check` skill 존재 확인 후 개인; `model_reasoning_effort=medium`, `sandbox_mode=read-only`는 정적값.
- `markdown-writer.toml` — `.codex/agents/markdown-writer.toml`; 제한: `workspace-write`, footer·검사기·다수 skill·`/root/.../INDEX.md` 참조가 있어 프로젝트별 정리 필요; model 미지정(세션 상속).
- `reviewer.toml` — `.codex/agents/reviewer.toml`; 이식 후보: 외부 경로 없이 읽기 전용 검토 지침; 개인; `model_reasoning_effort=high`, `sandbox_mode=read-only`는 정적값.

## Agents — Git·인프라·보안

- `git-manager.toml` — `.codex/agents/git-manager.toml`; 제한: `workspace-write`, git skill·정책 참조와 커밋 작업 범위가 있어 프로젝트; model 미지정(세션 상속).
- `infra-worker.toml` — `.codex/agents/infra-worker.toml`; 이식 후보: 명시 승인·검증·비밀 보호 원칙; 프로젝트; `model_reasoning_effort=high`, `sandbox_mode=workspace-write`는 정적값.
- `se-lite.toml` — `.codex/agents/se-lite.toml`; 제한: `workspace-write`, web/PowerShell 예시와 skill·정책 참조가 있어 개인 공통에는 최소 원칙만 선별; model 미지정(세션 상속).
- `security-auditor.toml` — `.codex/agents/security-auditor.toml`; 제한: `workspace-write`, `security-tools`의 개인 절대경로 의존을 분리한 뒤 프로젝트; model 미지정(세션 상속).
- `system-engineer.toml` — `.codex/agents/system-engineer.toml`; 제한: `workspace-write`, 다수 skill·`/root/.../INDEX.md`·web/PowerShell 예시 및 "승인 대기 금지" 문구가 있어 현재 권한 정책보다 우선할 수 없음; model 미지정(세션 상속).

## 외부 의존과 후속 확인

- 실제로 읽힌 절대경로 의존은 `/root/sj_del/`, `/root/32_system-engineering-resources/`, `/root/22_github_private/11_zircon/`, `/root/31_governances/` 및 agent의 `/root/.../INDEX.md` 참조입니다. 존재·내용·실행 가능 여부는 이번 범위에서 검증하지 않았습니다.
- 상세prompt 참조는 `ansible-review`, `fact-check`, `markdown-review`입니다. 내부 상대참조 `git-release`, `security-audit`, `testing-and-verification`도 대상 skill의 존재만 정적으로 확인했습니다.
- Kiro hook 의존은 `kiro-lock`과 `work-rules`에서 확인했습니다. Codex hook 등가물의 설치·활성화는 미검증입니다.
- branch/footer 고정값은 `git-commit-rule`, `readme-template`, `zircon-readme-policy`에서 확인했습니다. 개인 프로젝트에 자동 적용하지 않습니다.
- TOML의 model·sandbox 값은 위에 정적값으로만 기록했습니다. 실제 지원 모델, 유효 sandbox, 상속 설정은 런타임 검증 전 미확정입니다.

## 2026-09-22 재검토 보완

- 위 35개 목록은 자산별 1차 분류이며 전체 의존 그래프는 아직 검토 중입니다. 내부 진입점 세 개만으로 의존성 검토 완료를 판정하지 않습니다.
- planning-and-breakdown은 incremental-change, spec-driven-infra는 planning-and-breakdown·incremental-change, incremental-change는 장애 시 debugging-and-recovery를 참조합니다. using-skills는 여러 skill의 선택·연쇄 적용을 안내하므로 단독 자체 완결형 후보가 아닙니다.
- spec-driven-infra의 inventory에는 ~/.ssh/id_ed25519 예시가 있습니다. 필수 키 경로가 아닌 profile별 예제로 다루며 사용자 키의 존재나 사용 권한을 가정하지 않습니다.
- fact-check·markdown-review와 reviewer·docs_reviewer의 신규 후보는 [payload 매핑](PAYLOAD_MAP.md)에 분리했습니다. 본문의 보존 영역 분류와 신규 후보의 시험 상태는 구분합니다.

---

**작성일**: 2026-09-21

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
