---
name: kiro-lock
description: Prevents concurrent work in shared directories. Checks/acquires lock before file modifications, releases after completion.
---

# Kiro Lock

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- `.kiro-lock` 이름과 원문의 충돌·노후 잠금·읽기 전용 예외는 유지합니다. 프로젝트 root는 `.git` 디렉토리뿐 아니라 worktree의 `.git` 파일도 인정합니다. 다른 현행 저장소 잠금 정책이 있으면 그 정책을 따릅니다.
- §2의 검사 후 `>` 쓰기는 원자적 획득이 아닙니다. §2–3의 원문 명령은 과거 예시로 보존하며 실행하지 않습니다. 동봉 `scripts/lock.py`를 사용합니다. `acquire --root <repo> --token <session-token> --task <summary>`는 O_EXCL로 획득하고, `check`/`release`는 동일 토큰을 검증합니다. 토큰은 현재 작업에서 생성해 세션 전체에서 유지하고 파일에 노출된 타인의 토큰을 자기 토큰으로 채택하지 않습니다.
- `check`/`release` 전에 root와 토큰을 명시합니다. 잠금이 손상되었거나 다른 토큰·사용자·호스트·파일로 교체되면 작업/해제를 중단합니다. 30분 경과는 해제 승인이 아닙니다. 노후 잠금 해제는 현재 실제 소유 상태와 사용자 승인 후 별도로 처리합니다. 승인 없이 강제 해제하지 않습니다.
- §6의 하위 agent 예외는 주 agent가 잠금·작업 범위·서로 다른 파일 담당을 명시적으로 공유한 경우에만 적용합니다. 같은 user/host라는 이유만으로 잠금을 공유하지 않습니다. 주 agent가 마지막에 자기 잠금만 해제합니다.
- §7 hook 명령은 Kiro 환경 자료입니다. Codex에서는 실행하지 않습니다. hook이 없거나 꺼져 있어도 채택한 수동 잠금 정책은 계속 적용하며, 잠금 없이 진행할 수 있는지는 현재 저장소 지침과 사용자 지시로 판단합니다.

잠금 도구: [lock.py](../../scripts/lock.py). `python3 <SKILL_DIR>/scripts/lock.py --help`로 실제 인자를 확인합니다.

원문 비교 자료: [Kiro 원문](../originals/kiro-lock.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 1. Before starting work (mandatory)

Execute before any file modification task.

```bash
if [ -f .kiro-lock ]; then
    cat .kiro-lock 2>/dev/null || echo "⚠️ lock file unreadable — abort"
fi
```

- File exists + readable → show content + "Another task is in progress." + **abort immediately**
- File exists + unreadable → permission issue notice + **abort immediately**
- File absent → proceed to Lock acquisition

## 2. Lock acquisition

```bash
printf "user: $(whoami)\nhost: $(hostname)\nstarted: $(date -Iseconds)\nsession: $(date +%s)\ntask: <task summary>\n" > .kiro-lock
```

## 3. After work completion (mandatory)

Delete on both normal completion and error.

```bash
rm -f .kiro-lock
```

## 4. Rules

- Lock file path: `.kiro-lock` in **project root** (directory containing `.git`)
- No files shall be modified without acquiring lock
- Lock must be deleted even when errors occur during work
- Re-verify `.kiro-lock` ownership before each `fs_write`/write command (when 10+ minutes elapsed or after context compaction)
- Adding `.kiro-lock` to `.gitignore` is recommended

## 5. Stale lock handling

When `started` timestamp is 30+ minutes old:
1. Display confirmation request to the user
2. If user explicitly requests "release the lock", delete and proceed

## 6. Edge cases

### Own lock detection

When lock file `user` and `host` match current `$(whoami)`/`$(hostname)`:
- If `session` value matches current session → own lock (proceed normally)
- If `session` value differs → stale lock from previous session, ask "Previous session lock remains. Delete?" then proceed

### Corrupted lock file

When lock file exists but `user`/`started` fields cannot be parsed:
- Treat as stale lock
- Ask user "Lock file is corrupted. Delete?" then proceed

### Read-only operations

The following require no lock check/acquisition:
- `fs_read`, `grep`, `glob` and other read-only tools
- `git status`, `git log`, `git diff` and other query commands
- Status checks (`cat`, `ls`, `find`)

### Lock creation failure

When permission error occurs creating `.kiro-lock`:
1. Display error message
2. Do not proceed with work
3. Advise "Check project directory write permissions"

### Delegate invocations

When orchestrator (system-engineer) holds the lock and invokes sub-agents via delegate:
- Sub-agents do not re-check the lock (already acquired)
- Lock release is performed by orchestrator upon final work completion

## 7. Hook on/off

The preToolUse hook (`~/.kiro/hooks/kiro-lock.sh`) can be toggled without editing agent JSON.

```bash
# off
touch ~/.kiro/hooks/kiro-lock.disabled

# on
rm ~/.kiro/hooks/kiro-lock.disabled

# status
ls ~/.kiro/hooks/kiro-lock.disabled 2>/dev/null && echo "OFF" || echo "ON"
```

When disabled, the hook exits immediately (exit 0) — manual lock checks in SKILL.md §1–3 still apply.
