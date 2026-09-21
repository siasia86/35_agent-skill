# Codex 자산

Kiro에서 사용하던 system-engineer 중심 작업 방식과 사용자 커스텀 규칙을 보존한 Codex 자산입니다. 원본은 이 저장소의 `kiro/`입니다.

## 1. 구성

- `AGENTS.md`: 주 세션의 system-engineer 역할과 필수 지침 진입점입니다.
- `.agents/skills/`: 원본 19개 Skill과 이전 변환의 보조 Skill을 관리합니다.
- `.codex/agents/`: 원본 7개 역할과 이전 변환의 호환 역할을 관리합니다.
- `markdown/`: 원본 문서 스타일·푸터·링크 별점 기준입니다.
- `prompts/`: 원본 13개 요청 예시를 보존합니다. 자동 슬래시 명령 등록 파일은 아닙니다.
- `policies/`: Codex 호환성, 작업 문서 정책, 원본 해시 manifest입니다.
- `ISSUE.md`, `TODO.md`, `PLAN.md`, `CHANGELOG.md`: 문제·미완료·진행·완료 기록입니다.

## 2. 자동 검토 설정

현재 사용자 설정에 네 저장소를 trusted로 등록했고 각 저장소의 `.codex/config.toml`에 자동 검토를 설정했습니다. 새 세션에서 적용됩니다.

```bash
codex -C /root/35_agent-skill
```

30·31·32·35 경로를 함께 쓰려면 생성한 사용자 프로필을 선택합니다.

```bash
codex --profile se-repos -C /root/35_agent-skill/gpt
```

프로필은 `approval_policy = "on-request"`, `approvals_reviewer = "auto_review"`, `sandbox_mode = "workspace-write"`와 네 writable root를 설정합니다. 자동 검토가 거부하는 요청과 OS 파일 권한 제한은 남습니다. 기존 실행 세션에는 소급 적용되지 않습니다. 다른 시스템에서는 프로필과 경로를 별도로 구성해야 합니다.

## 3. 작업 지침과 호출

`gpt/`를 작업 디렉터리로 시작해 `AGENTS.md`와 하위 자산의 로딩 상태를 확인합니다. 상위 저장소에서 시작했다고 이 하위 지침까지 적용됐다고 가정하지 않습니다. 다른 저장소에 배포할 때는 같은 자산 구조를 보존하고 기존 AGENTS·설정을 먼저 병합 검토합니다.

```text
system-engineer 규칙으로 TODO의 미완료 항목부터 진행해.
$readme-template 규칙과 markdown/STYLE.md로 문서를 작성해.
$code-review로 변경을 검토해.
prompts/fact-check.md를 읽고 지정한 문서를 검증해.
```

Skill 본문에 남아 있는 Kiro 예시는 호환성 정책에 따라 해석합니다. Prompt의 `${1}` 등은 입력 자리표시자이며 자동 치환을 보장하지 않습니다. 별점은 도구 ★☆☆☆☆, 블로그 ★★☆☆☆, 공식 문서 ★★★☆☆, RFC·주요 도서 ★★★★☆를 기준으로 원본 STYLE을 적용합니다.

## 4. 검증과 남은 작업

원본 내용 보존, YAML·TOML, 원본 해시, Markdown·diff 검사와 런타임 동작 검증을 구분합니다. 정적 검사가 통과해도 자동 호출과 실제 hook 실행이 검증됐다고 보고하지 않습니다.

미지원 hook·외부 의존성·읽기 권한 문제와 원본 충돌은 [ISSUE.md](ISSUE.md)에 기록합니다. 진행 상태는 [TODO.md](TODO.md), 단계와 롤백은 [PLAN.md](PLAN.md), 완료 기록은 [CHANGELOG.md](CHANGELOG.md)에서 확인합니다.

---

## 통계

![GitHub stars](https://img.shields.io/github/stars/siasia86/system-engineering-resources?style=social)
![GitHub forks](https://img.shields.io/github/forks/siasia86/system-engineering-resources?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/siasia86/system-engineering-resources?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/siasia86/system-engineering-resources)
![License](https://img.shields.io/github/license/siasia86/system-engineering-resources)
![Actions](https://img.shields.io/github/actions/workflow/status/siasia86/system-engineering-resources/update-date.yml)

---

**작성일**: 2026-09-04

**마지막 업데이트**: 2026-09-21

© 2026 siasia86. Licensed under CC BY 4.0.
