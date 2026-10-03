---
name: kiro-lock
description: Prevents concurrent work in shared directories. Checks/acquires lock before file modifications, releases after completion.
---

# Kiro Lock

<!-- CODEX-COMPAT-BEGIN -->
## Windows Codex 실행 및 적용 규칙

이 절과 이 절에서 연결한 실행 도구가 Windows의 현재 실행 본문입니다. 아래 Linux/Kiro 원문의 코드·명령·경로는 전체 보존한 비교 자료이며 그대로 자동 실행하지 않습니다. 원문의 목적·예시·체크리스트는 유지하되 플랫폼 차이와 교정 사항은 이 절의 실행 계약을 적용합니다. Linux 본문은 `codex_linux/`에 보존되어 있으며 이번 이식은 경량화·통합 작업이 아닙니다.

- 시스템·개발자·관리 정책과 실제 권한 안에서 **사용자 명시 지시 > 적용 저장소 AGENTS > 개인 스킬 기본값**을 적용합니다. 이미 부여된 범위와 승인을 유지하고 다른 저장소·개인 홈·시스템·운영 환경의 수정 권한을 경로 존재로 추정하지 않습니다.
- 실제 Git 루트·branch·기존 변경을 먼저 확인합니다. 필요한 본문·동봉 참조만 읽고 다른 스킬·전체 작업 기록을 자동 로드하지 않습니다. 원문의 `skill://`는 아래 로컬 참조로 해석하며 URI 도구를 호출하지 않습니다.
- 이 폴더를 통째로 복사하는 개인 스킬입니다. 필수 참조는 아래 상대 링크를 사용합니다. 중앙 catalog·설치기·다른 저장소 또는 형제 스킬 설치를 필수로 요구하지 않습니다. 원문 `../originals/kiro-lock.md`는 비교 자료입니다.
- 네이티브 Windows 작업 셸은 PowerShell입니다. 파일 작업은 `-LiteralPath` 등 실제 대상 인자로 처리하며 셸 문자열·`eval`로 외부 입력을 재해석하지 않습니다. Python 3.11 이상을 `python -X utf8`로 실행하고 Python 하위 실행은 `[sys.executable, '-X', 'utf8', ...]` 인자 배열을 사용합니다. 실제 Python 위치·버전은 현재 환경에서 확인합니다.
- Bash 업무는 Git Bash 또는 승인된 WSL에서 유지합니다. PowerShell에서 Bash/POSIX 예제를 직접 실행하지 않습니다. 원문의 `/root`, `/var/log`, `/backup`, Kiro hook은 과거 환경 자료이며 Windows 개인 홈·시스템 경로로 자동 치환하지 않습니다.
- 검증은 **통과 / 부분 검사 / 실패 / 미실행**을 실행 목적·관찰·다음 조치와 함께 기록합니다. 경로 치환이나 과거 완료 기록을 현재 동작 통과로 사용하지 않습니다. 비공개 경로·계정·토큰·운영 자료를 공개 결과에 복사하지 않습니다.

### 현재 Windows 수동 잠금

잠금은 [lock.py](../../scripts/lock.py)로만 획득·확인·해제합니다. 아래 원문의 검사 후 `>` 쓰기, 무조건 `rm`, Kiro hook 토글은 비교 자료이며 Windows 실행 절차가 아닙니다. 실제 프로젝트 루트는 `.git` 디렉터리 또는 worktree의 `.git` 파일을 인정하고, 현재 저장소가 선택한 잠금 정책과 읽기 전용 예외를 적용합니다.

```powershell
# Repo와 SkillDir은 실제 대상, SessionToken은 현재 작업에서 생성해 유지합니다.
$SessionToken = [guid]::NewGuid().ToString('N')
python -X utf8 "$SkillDir/scripts/lock.py" acquire --root $Repo --token $SessionToken --task '현재 작업 요약'
if ($LASTEXITCODE -ne 0) { throw '잠금 획득 실패' }
python -X utf8 "$SkillDir/scripts/lock.py" check --root $Repo --token $SessionToken
if ($LASTEXITCODE -ne 0) { throw '잠금 소유 확인 실패' }
# 완료/오류 정리에서는 동일 토큰으로 자기 잠금만 해제합니다.
python -X utf8 "$SkillDir/scripts/lock.py" release --root $Repo --token $SessionToken
if ($LASTEXITCODE -ne 0) { throw '잠금 해제 실패: 소유/증거 확인 필요' }
```

- O_EXCL guard가 이 도구를 사용하는 협조자들의 획득·확인·해제를 직렬화하고, O_EXCL lock 획득은 기존 lock을 덮어쓰지 않습니다. 기존·타인·손상·노후 lock과 abandoned guard는 자동 삭제하지 않습니다. 30분 경과나 user/host 일치만으로 소유권을 인정하지 않습니다. 타인의 파일에 기록된 토큰을 자신의 토큰으로 채택하지 않습니다.
- 획득 중 JSON 쓰기·flush·fsync가 실패하면 그 호출이 독점 생성한 inode와 아직 일치하는 파일만 guard 안에서 정리합니다. 원래 있던 파일과 교체된 파일은 보존합니다. check/release는 토큰·현재 user·host·파일 동일성을 확인하고 POSIX에서 가능하면 uid도 확인합니다. Windows mode 0600을 NTFS ACL 보호라고 주장하지 않습니다. 토큰과 잠금 본문을 로그에 출력하지 않습니다.
- symlink/reparse 파일과 확인 가능한 부모/root reparse를 거부하고, lstat/open/fstat와 해제 전 inode를 대조합니다. 순수 stdlib Windows의 검사 사이 비협조 경로 교체·hard-link·네트워크 파일시스템·ACL 경계를 완전히 차단한다고 보장하지 않습니다. 그런 환경은 격리 작업본 또는 대상 저장소의 검증된 잠금 방식을 사용합니다.
- 주 agent가 범위·토큰·다른 파일 담당을 직접 공유했을 때만 하위 agent가 같은 잠금으로 작업합니다. 주 agent가 마지막에 동일 소유를 확인한 후 해제합니다. compaction/10분 경과 후 쓰기 전 소유를 다시 확인합니다. 읽기 전용 조회는 원문 예외를 유지합니다.
- stale/corrupt/manual recovery는 현재 소유와 사용자 요청을 확인하는 별도 조치입니다. 이 도구 실패를 권한 우회나 강제 삭제로 바꾸지 않습니다. 설치·개인 홈 hook·Kiro disabled 파일을 자동 생성하지 않습니다.

원문 비교 자료: [Kiro 원문](../originals/kiro-lock.md).
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
