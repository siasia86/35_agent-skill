# Codex Linux 개인 스킬

이 디렉토리는 기존 `codex/`를 같은 깊이로 옮긴 Linux 원문 보존 이식본입니다. skill 19개·personal 자료·검증 JSON의 bytes를 유지하며 Windows 전용 재작성은 [Windows PLAN](../codex_windows/PLAN.md)에서 준비합니다. PowerShell 복사 예시는 Linux 원본 파일의 복사 안내이며 Windows 실행 호환성의 통과 근거가 아닙니다.

과거 검증 JSON의 `codex/` 입력 경로·해시·원시 명령은 바꾸지 않습니다. 현재 파일 대조에서는 첫 `codex/`만 `codex_linux/`로 대응합니다. [플랫폼 분리 기록](../agent-workflows/codex/PLATFORM_SPLIT_2026-10-03.md)에서 검증·복구·게시 상태를 확인합니다.

저장소 버전 **1.0.0**의 개인 스킬 복제본입니다. `skills/<이름>/` 폴더 전체를 복사하면 그 스킬의 지침·필수 참조를 사용할 수 있습니다. Kiro 스킬 19개의 본문·코드·예시·체크리스트를 줄이지 않고 Codex 호환 규칙을 추가했습니다.

작업을 이어갈 때는 [세션 인계](../agent-workflows/codex/HANDOFF.md)와 [현재 TODO](TODO.md)를 먼저 확인합니다. 2026-10-02 추가 내용 검토의 후보와 미게시 문서 변경을 1.0.0의 기존 완료 기록과 구분합니다.

## 1. 구조

```text
codex_linux/
├── README.md
├── MIGRATION.md                 원문 대응·변경 이유·해시
├── VERIFICATION.md              실제 검사와 Luna 사례 결과
├── TODO.md                      아직 실행하지 않은 후속 확인
├── personal/
│   └── AGENTS.md                선택적 개인 기본 지침 예시
├── verification/
│   └── verify_skills.py         개발 검증용, 설치에 불필요
└── skills/
    ├── bash-script-template/
    ├── code-review/
    ├── debugging-and-recovery/
    ├── doubt-driven-infra/
    ├── git-commit-rule/
    ├── incremental-change/
    ├── kiro-lock/
    ├── md-link-check/
    ├── planning-and-breakdown/
    ├── python-script-template/
    ├── readme-template/
    ├── repo-governance/
    ├── security-tools/
    ├── shipping-checklist/
    ├── spec-driven-infra/
    ├── testing-guide/
    ├── using-skills/
    ├── work-rules/
    └── zircon-readme-policy/
```

스킬마다 `SKILL.md`와 `references/kiro-original.md`가 있습니다. 실제 필요한 경우에만 `references/skills`, `references/STYLE.md`, `references/resources`, `scripts`를 포함합니다. 다른 스킬을 이어서 사용할 때는 같은 폴더의 전체 참조 사본을 읽습니다. 참조 사본은 `.md`이며 추가 설치 스킬로 중복 발견시키지 않습니다. 서로 다른 스킬을 이미 설치한 환경에서도 폴더 내부 참조로 완결됩니다.

`SKILL.md` 한 파일만 복사하면 동반 자료가 빠질 수 있습니다. **폴더 전체**가 복사 단위입니다. 중앙 catalog·manifest·installer·agent TOML·30/31 저장소는 필요하지 않습니다. 개발 검증용 파일과 MIGRATION 문서는 설치 의존성이 아닙니다. 현재 요청에 해당하는 참조만 읽습니다.

## 2. 수동 복사

### 2.1 적용 범위

- 개인 공통 구성(`USER`): 실행 사용자 홈의 `~/.agents/skills/<이름>/`에 설치합니다. 같은 사용자로 작업하는 여러 저장소에서 사용할 수 있습니다.
- 저장소별 구성(`REPO`): 대상 저장소의 `.agents/skills/<이름>/`에 설치합니다. 해당 저장소에서 작업할 때 발견하며, 하위 디렉토리별 검색 범위는 공식 스킬 안내를 확인합니다.
- 설치 위치와 실제 작업공간을 함께 기록합니다. 다른 사용자·기기·클라이언트에서의 발견과 동작은 각각 확인합니다.

예를 들어 설명용 환경 별칭 `PC-home-sjyun`에서 `repository1`과 `qa-repostory2`를 사용하면, 개인 홈의 공통 스킬은 한 번 설치하고 각 저장소의 적용 지침과 대표 행동은 따로 확인합니다. 두 저장소에 각각 설치한 스킬은 별도 설치로 기록합니다. 사용자 홈의 변경은 여러 작업공간에 영향을 줄 수 있으므로 업데이트 시 그 영향을 확인합니다.

같은 `name`의 스킬이 사용자 범위와 저장소 범위에 모두 있으면 Codex는 이를 자동 병합하지 않으며 선택 목록에 둘 다 나타날 수 있습니다. 경로·출처·역할을 확인해 사용할 스킬을 구분합니다. 저장소 지침의 우선순위를 스킬 파일의 자동 교체 규칙으로 해석하지 않습니다.

### 2.2 폴더 복사

개인 스킬의 기본 복사 위치는 실행 사용자 홈의 `~/.agents/skills/<이름>/`입니다. 이 저장소를 clone한 위치에서 아래 예시를 사용합니다. 기존 동명 폴더가 있으면 먼저 비교·백업하고 사용자 편집을 보존합니다. 예시는 기존 폴더를 덮어쓰지 않습니다.

아래 명령은 개인 공통 구성의 예시입니다. 저장소별로 설치할 때는 확인한 대상 저장소의 `.agents/skills/<이름>/`을 목적지로 사용하고, 같은 폴더 전체 복사·비교·백업 기준을 적용합니다. 적용 결과는 [환경·작업공간별 기록 기준](../agent-workflows/codex/README.md#5-환경과-작업공간별-후속-기록)에 따라 남깁니다.

```bash
skill_name=work-rules
skill_target="$HOME/.agents/skills/$skill_name"
if [ -e "$skill_target" ]; then
    printf '기존 스킬을 먼저 비교·백업하세요: %s\n' "$skill_target"
else
    mkdir -p "$HOME/.agents/skills"
    cp -a "codex_linux/skills/$skill_name" "$skill_target"
fi
```

Windows PowerShell에서는 다음과 같습니다.

```powershell
$skillName = 'work-rules'
$skillRoot = Join-Path $HOME '.agents/skills'
$skillTarget = Join-Path $skillRoot $skillName
if (Test-Path $skillTarget) {
    Write-Output "기존 스킬을 먼저 비교·백업하세요: $skillTarget"
} else {
    New-Item -ItemType Directory -Force $skillRoot | Out-Null
    Copy-Item -Recurse "codex_linux/skills/$skillName" $skillTarget
}
```

원하는 스킬만 고릅니다. `using-skills`는 전체 작업 매핑과 동봉 참조를 제공하며, 다른 18개를 전부 설치해야 하는 조건은 없습니다. `kiro-lock`은 수동 잠금이 필요한 경우, `zircon-readme-policy`는 해당 저장소/명시 채택 범위에서 선택합니다. 둘 모두 모음에는 유지합니다.

설치 후 새 세션에서 목록과 `$work-rules` 등 명시 호출을 확인합니다. 이름·description은 발견 정보이며 본문은 스킬을 선택할 때 적용합니다. 모든 개인 규칙이 매 요청마다 자동 로드된다고 가정하지 않습니다. 이번 작업에서는 실제 개인 홈에 설치하지 않았습니다.

## 3. 개인 기본값과 저장소 규칙

플랫폼 정책·현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침 > 개인 스킬 범용 기본값**을 적용합니다. 저장소는 고유 규칙과 예외를 정의하고 개인 스킬은 계획·문서 양식·선택·검증·코드 골격을 제공합니다.

현재 작업공간에 31 저장소에서 관리하는 설정이 적용되어 있으면, 해당 설정을 확인하고 그 적용 범위와 지침에 따라 함께 사용합니다. 적용 여부는 도구가 실제로 로드한 설정과 저장소 지침이 참조하는 파일을 확인해 판단합니다. `repository1`의 설정을 `qa-repostory2`의 설정으로 간주하지 않습니다. 31 연동이 없는 작업공간에서도 개인 스킬과 해당 저장소의 적용 지침을 사용합니다.

예를 들어 개인 README 기본값에 푸터가 있어도 `repository1`의 지침이 푸터를 금지하면 그 항목만 제외합니다. `qa-repostory2`에 같은 금지 규칙이 없다면 해당 작업의 사용자 지시와 개인 기본값을 확인해 적용합니다. 두 저장소의 결과는 각각 검증하며 스킬 원본을 그 예외 때문에 변경하지 않습니다.

[personal/AGENTS.md](personal/AGENTS.md)는 선택적 예시입니다. 개인 지침을 상시 제공하고 싶을 때 기존 `~/.codex/AGENTS.md` 또는 사용자 지정 CODEX_HOME의 AGENTS.md와 비교하여 필요한 규칙을 병합합니다. 기존 개인 지침을 통째로 덮어쓰지 않습니다. 각 스킬에도 필요한 우선순위·범위 규칙이 있어 이 예시를 설치할 필요는 없습니다. API key·모델·MCP·권한 설정을 강제하지 않습니다.

## 4. 도구와 호환 범위

동봉 Markdown 검사 스크립트는 Python 3.11 이상의 표준 라이브러리만 사용합니다. 해당 스킬의 실제 위치를 `<SKILL_DIR>`에 넣고 현재 수정한 문서만 검사합니다. `python`/`python3` 실행 이름은 현재 환경에서 확인합니다. 일반 CLI·Git·Terraform·AWS·Bash 등 작업 도구와 작업 권한은 요청별 실행 환경에서 확인합니다.

Kiro hook·memory와 과거 `/root/...` 경로는 원문으로 보존하며 Codex 호환 절에서 대체 동작을 명시합니다. `security-tools`의 기존 개인 마스킹 도구 원본은 제공되지 않았습니다. 이 스킬은 설계·검증·수동 보안 점검을 수행하며 기존 도구와 동일한 실행·map 호환성을 주장하지 않습니다. 마스킹 실행은 실제 도구/형식 확인과 격리 검증 후 진행합니다. 없는 도구의 결과를 통과로 기록하지 않습니다.

단독 폴더 복사·로컬 도구·Luna 사례 결과는 [VERIFICATION](VERIFICATION.md), 원문 대응은 [MIGRATION](MIGRATION.md), 실제 세션·Windows·운영 미실행 항목은 [TODO](TODO.md)에 기록합니다. [폐기한 Codex 개발본](../105_backup/codex/README.md)은 역사 자료입니다.

공식 복사/발견 방식은 [Skills 문서](https://learn.chatgpt.com/docs/build-skills), 개인·저장소 지침의 적용 방식은 [AGENTS.md 문서](https://learn.chatgpt.com/docs/agent-configuration/agents-md)를 확인했습니다.

---

**작성일**: 2026-10-01

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
