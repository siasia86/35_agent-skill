---
name: repo-governance
description: 저장소별 규칙을 담은 .governance/ 디렉토리를 탐색하고 전역 규칙과의 우선순위를 적용합니다. 어떤 저장소에서든 파일을 수정하거나 작업을 시작할 때 사용합니다.
---

# Repository Governance

<!-- CODEX-COMPAT-BEGIN -->
## Windows 호환 및 적용 규칙

이 절이 Windows에서 사용할 실행·경로·검증 기준입니다. 블록 밖의 원문·예시·코드·템플릿·체크리스트는 모두 보존했으며 충돌하지 않는 목적·개인 규약은 계속 적용합니다. POSIX/Bash 실행 방법은 비교 자료이며 Windows PowerShell에서 그대로 실행하지 않습니다. 필요한 원격 Linux 작업은 실제 대상·쉘·도구·권한을 확인한 별도 실행입니다. 아래에서 위험하거나 잘못된 과거 예시를 대체한 경우 원래 예시를 실행하지 않습니다.

### 적용 범위와 실제 환경

- 플랫폼·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침 > 개인 skill 기본값** 순서로 적용합니다. 작업별 필요한 skill·참조만 읽고 이미 읽은 본문·순환 참조를 반복하지 않습니다. 원문 보존을 전체 skill의 일괄 실행 조건으로 바꾸지 않습니다.
- 실제 작업 경로에서 `git -C <대상 디렉터리> rev-parse --show-toplevel`, `git -C <확인한 Git 루트> status --short`로 루트·기존 변경을 먼저 확인합니다. worktree의 `.git` 파일도 인정합니다. 적용 AGENTS/override·하위 지침과 실제 `.governance`의 범위만 따르며 다른 저장소 설정을 자동 적용하지 않습니다.
- Windows 네이티브 PowerShell과 실제 Python 3.11 이상을 사용합니다. PowerShell 5.1/7, `python.exe`/`py`의 실제 경로·버전을 확인하고 WindowsApps alias를 설치된 runtime으로 간주하지 않습니다. Python은 `-X utf8 -B`로 호출하고 작성하는 코드의 파일 읽기·쓰기도 `encoding='utf-8'`을 명시합니다. PowerShell 인코딩은 버전별로 확인하며 BOM/UTF-16/개행을 의도 없이 변경하지 않습니다.
- PowerShell의 파일 작업은 `-LiteralPath`, `Join-Path`, 확인한 절대 경로를 사용합니다. Linux의 `/root`, `/opt`, `$HOME`, `chmod`, `sudo`, `systemctl`, `fcntl`을 Windows 계정·경로·ACL·서비스로 이름만 치환하지 않습니다. WSL/Git Bash가 필요하면 명시한 Linux/Bash 역할로 구분하며 설치·활성화·권한 변경은 자동 수행하지 않습니다.
- 네이티브 CLI의 종료 상태는 해당 도구 계약으로 판정합니다. PowerShell cmdlet 오류와 `$LASTEXITCODE`를 혼동하지 않고 오류 로그만으로 성공 처리하지 않습니다. Terraform detailed exit code처럼 정상 차이를 뜻하는 상태는 일반 실패와 구분합니다.
- 이미 승인된 작업은 자율 진행합니다. 신규 파괴 작업·실제 운영 적용·키/ACL 변경·범위 밖 게시 등 추가 권한이 필요한 동작은 그 직전에 현재 승인 범위를 확인합니다. 경로 존재·과거 승인·원문 예시는 새 권한이 아닙니다. 기존 승인에 같은 확인을 반복 요구하지 않습니다.
- 구현·검사 완료, 모델 행동, 설치·새 세션 발견, 원격 적용, Git 게시를 각각 구분합니다. 이 파일의 작성은 개인 홈 설치나 실환경 검증 완료가 아닙니다. 한국어로 목적·관찰·다음 조치와 통과/부분 검사/실패/미실행을 간결하게 보고합니다.
- 사용자와 저장소가 지정한 게시 순서를 따릅니다. 이 스킬 모음의 원본인 35_agent-skill 저장소에서 이번 이관 작업을 완료한 후에는 검증한 변경을 **yunli에 push → 사용자 검증 → main 반영·push**합니다. 다른 저장소를 yunli로 강제 전환하거나 검토 요청을 commit/push로 확대하지 않습니다. 개인 홈·config·키·release·서비스 적용은 별도 요청 범위입니다.

### 단독 사용과 참조

폴더 전체가 사용 단위입니다. 이 폴더 안의 필수 참조·도구만 사용하며 중앙 catalog·installer·30/31 저장소나 다른 skill의 별도 설치를 요구하지 않습니다. `skill://`는 아래 동봉 대응으로 해석하고 Kiro URI/hook/memory API를 호출하지 않습니다. 개인 경로·계정·config 원문·자격증명·세션·raw 비공개 증거를 공개 자료에 복사하지 않습니다.

### Windows 저장소 지침 발견

PowerShell에서 실제 대상의 Git 루트를 확인하고 AGENTS/AGENTS.override·하위 지침과 `.governance`를 각 적용 범위로 확인합니다. 숨김 속성·선행 점 이름·`.git` 파일/디렉터리 차이 때문에 존재를 추정하지 않습니다.

```powershell
# $targetPath는 사용자 요청에서 확인한 대상 디렉터리입니다.
$gitRoot = git -C $targetPath rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0) { throw '대상 Git 루트를 확인하지 못했습니다' }
git -C $gitRoot status --short
if ($LASTEXITCODE -ne 0) { throw '기존 변경을 확인하지 못했습니다' }
$governanceDir = Join-Path $gitRoot '.governance'
if (Test-Path -LiteralPath $governanceDir -PathType Container) {
    Get-ChildItem -LiteralPath $governanceDir -Force
}
```

- 실제 GOVERNANCE·exceptions·verification이 있으면 필요한 범위를 읽습니다. 적용 지침에 지정한 파일이 읽기 실패한 경우 규칙이 없는 상태로 취급하지 않습니다. `.governance`가 없으면 실제 적용 AGENTS와 개인 기본값을 사용하고 새 정책 파일을 먼저 만들도록 요구하지 않습니다.
- 원문의 알려진 저장소·/root 경로·도입 완료 표는 당시 사례입니다. Windows 설치 상태·정책 소유권·권한을 뜻하지 않으며 다른 저장소를 필수로 준비하지 않습니다. 31의 현재 설정은 대상이 실제로 채택한 범위에서만 연결합니다.
- 신규 `.governance` 구성은 사용자가 정책 신규 작성/초기화를 요청한 범위에서만 수행합니다. 기존 저장소의 루트 문서를 자동 이동·덮어쓰거나 AGENTS와 개인 설정을 일괄 교체하지 않습니다.
- governance_template/verification_template은 대상 정책 templates의 조건부 입력입니다. 없고 필수로 지정되지 않았다면 확인된 사용자 요구로 초안을 만들고 미결 조건을 기록합니다. 필수 입력 접근 실패는 임의 대체하지 않습니다.
- ACL·관리자 권한·SSH/키·서비스·운영 설정은 지침 탐색으로 생기는 권한이 아닙니다. 실제 파일 읽기·변경 범위와 권한을 분리하고 저장소에서 정의한 예외만 해당 저장소에 적용합니다.

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 목적

저장소마다 성격이 달라 전역 규칙만으로 모두 다룰 수 없습니다. 저장소별 규칙은 해당
저장소의 `.governance/` 에 두고, 이 skill이 그 규칙을 찾아 전역 규칙과 조합합니다.

저장소별 skill을 계속 추가하는 방식을 대체합니다. 저장소가 늘어도 이 skill 하나로
처리하므로 전역 컨텍스트가 저장소 수에 비례해 커지지 않습니다.

## 탐색 절차

작업 대상 경로가 확인되면 저장소 최상위에서 `.governance/` 를 찾습니다.

```
1. 작업 대상 파일의 경로 확인
2. 상위로 올라가며 .git 이 있는 디렉토리(저장소 최상위) 탐색
3. 그 위치에 .governance/ 가 있는지 확인
4. 있으면 .governance/GOVERNANCE.md 를 읽음
5. exceptions.md, verification.md 가 있으면 함께 읽음
6. 없으면 전역 규칙만 적용
```

```bash
# 저장소 최상위 확인
git -C <path> rev-parse --show-toplevel

# .governance/ 존재 확인
ls -la "$(git -C <path> rev-parse --show-toplevel)/.governance/" 2>/dev/null
```

🟡 `.governance/` 는 숨김 디렉토리이므로 일반 `ls` 로는 보이지 않습니다. 존재 여부를
추측하지 말고 위 명령으로 확인합니다.

## 우선순위

| 순위 | 출처                      | 적용 범위        | 지속성            |
|------|---------------------------|------------------|-------------------|
| 1    | 사용자의 명시적 지시      | 해당 세션        | 세션 종료 시 소멸 |
| 2    | repo-local `.governance/` | 해당 저장소      | 저장소에 영속     |
| 3    | 전역 skill                | 모든 저장소      | 실행 환경에 영속  |
| 4    | 기본 동작                 | 규칙이 없는 판단 | 해당 없음         |

```
사용자의 명시적 지시
       │  세션 한정, 근거 필요
       v
repo-local .governance/
       │  해당 저장소 범위
       v
전역 skill
       │  조직 공통 기본값
       v
기본 동작
```

### 적용 규칙

- 상위 순위가 하위 순위를 덮어씁니다.
- 사용자 지시가 하위 규칙과 충돌하면 지시를 따르되, 어떤 규칙과 충돌하는지 알립니다.
- 사용자 지시는 해당 세션에만 적용합니다. 영속 변경이 필요하면 `.governance/` 또는
  전역 skill을 수정하도록 안내합니다.
- `.governance/` 에 기술되지 않은 항목은 전역 규칙을 그대로 적용합니다.
- `.governance/` 가 전역 규칙 전체를 재정의하려 하면 그 범위가 과도한지 지적합니다.

## 안전 예외

다음 항목은 우선순위와 무관하게 항상 확인 절차를 거칩니다. 사용자 지시나
`.governance/` 설정으로도 생략할 수 없습니다.

| 항목           | 확인 대상                                           |
|----------------|-----------------------------------------------------|
| 비가역 작업    | 데이터 삭제, 이력 재작성, force push, 프로덕션 반영 |
| 자격증명 취급  | 키·토큰·인증서의 조회·출력·전송·삭제                |
| 권한 변경      | 인증·인가·접근제어 정책 수정                        |
| 영향 범위 확대 | 재귀 삭제, 대량 수정, 공유 시스템 변경              |

이미 승인된 작업을 반복 확인하지는 않습니다. 승인 범위를 넘어 확장될 때 다시 확인합니다.

## `.governance/` 구조

```
<repository-root>/
├── .governance/
│   ├── GOVERNANCE.md      신규 저장소 필수 — 저장소 성격과 예외 요약
│   ├── ISSUE.md           신규 저장소 필수 — 이슈 기록
│   ├── TODO.md            신규 저장소 필수 — 미완료 작업
│   ├── PLAN.md            신규 저장소 필수 — 진행 중인 복합 작업
│   ├── exceptions.md      선택 — 예외 상세
│   └── verification.md    선택 — 저장소 전용 검증 명령
└── ...
```

## 기술 범위 제한

`.governance/` 는 전역 규칙 대비 차이만 기술합니다.

| 기술 가능                         | 기술 불가                       |
|-----------------------------------|---------------------------------|
| 전역 규칙 중 특정 항목의 비활성화 | 전역 규칙 전체의 재정의         |
| 전역 규칙 값의 저장소별 조정      | 안전 예외 항목의 무력화         |
| 저장소 전용 검증 절차 추가        | 사용자 지시보다 우선한다는 선언 |
| 문서 역할·생명주기 예외           | 다른 저장소에 대한 규칙         |

`.governance/GOVERNANCE.md` 는 유지하는 전역 규칙과 예외를 모두 명시해야 합니다.
예외만 적혀 있으면 나머지 규칙의 적용 여부를 확인합니다.

## 알려진 저장소

| 저장소                                  | `.governance/` | 비고                             |
|-----------------------------------------|----------------|----------------------------------|
| `/root/31_governances`                  | 도입 완료      | 공통 정책 원본 (2026-08-31 이관) |
| `/root/32_system-engineering-resources` | 미도입         | 학습 문서 저장소, 정책은 31 참조 |
| `/root/22_github_private/11_zircon`     | 미도입         | 전역 skill에서 이관 예정         |
| Ansible 학습·자동화 저장소              | 도입 완료      | 저장소 규칙으로 이관 완료        |

이 표는 참고용입니다. 실제 존재 여부는 항상 탐색 절차로 확인합니다.

## 신규 작성 시

`.governance/` 문서를 새로 만들 때는 템플릿을 사용합니다. 템플릿은 저장소 정책
디렉토리의 `templates/` 아래에 있습니다.

| 대상 파일                     | 템플릿                     |
|-------------------------------|----------------------------|
| `.governance/GOVERNANCE.md`   | `governance_template.md`   |
| `.governance/verification.md` | `verification_template.md` |

신규 저장소는 `.governance/GOVERNANCE.md`, `ISSUE.md`, `TODO.md`, `PLAN.md`를 기본으로 생성합니다. 활성 항목이 없어도 문서를 삭제하지 않고 상태를 기록합니다.

`verification.md` 는 변경 유형이 여러 가지이고 각각 다른 검증이 필요할 때만 분리합니다. 기존 저장소는 migration 전까지 루트 `ISSUE.md`, `TODO.md`, `PLAN.md`를 legacy 위치로 허용합니다.

## 참조 정책

전체 정책은 다음 저장소에 있습니다.

```
https://github.com/siasia86/31_governances
.governance/repository/governance_precedence.md
```
