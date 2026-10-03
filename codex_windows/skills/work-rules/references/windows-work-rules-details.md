# Windows work-rules 상세 대응

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
- 사용자와 저장소가 지정한 게시 순서를 따릅니다. 다른 저장소를 yunli로 강제 전환하거나 검토 요청을 commit/push로 확대하지 않습니다. 개인 홈·config·키·release·서비스 적용은 별도 요청 범위입니다.

### 작업 시작과 완료 보고

사용자가 한 채팅 안에서 여러 요청을 `;`로 구분하면 각각의 요청으로 이해하고 빠뜨리지 않도록 수행·검증·미실행 상태를 구분합니다. 요청 사이에 의존 관계가 있으면 그 순서에 맞춰 진행하고 독립된 작업은 함께 진행할 수 있습니다. 코드·명령어·인용문·경로 등 내용 안의 `;`는 원래 의미를 유지하며 기계적으로 요청을 나누지 않습니다. 구분이 실제 작업 범위에 영향을 주고 문맥으로 해결되지 않을 때만 필요한 내용을 확인합니다.

실제 실행·파일 변경 작업을 시작하기 전에 **대상 경로·무엇을 수행하는지·예상 결과**를 간결하게 알립니다. 큰 작업은 주요 단계·변경 범위·검증 방법도 안내하고, 진행 중에는 의미 있는 관찰·방향 변경·남은 조건을 공유합니다. 단순 질의·짧은 답변에는 불필요한 작업 계획이나 고정 양식을 붙이지 않습니다. 시작 안내를 이미 승인된 작업에 대한 반복 승인 질문으로 바꾸지 않습니다.

완료 보고는 핵심 결과부터 설명하고 다음 항목을 실제 근거에 따라 담습니다.

- **결과물과 경로:** 실제 결과물이 있으면 설명·표·폴더 구조 위에 기준 경로를 먼저 표시하고 파일은 클릭 가능한 경로로 연결합니다. 같은 기준 경로를 반복하지 않습니다. 로컬 사용자 보고에는 실제 경로를 쓰되 원격에 게시할 문서는 저장소 상대 경로·공개 가능한 별칭을 사용하며 개인 경로·계정·자격증명·운영 자료를 복사하지 않습니다.
- **수행과 검증:** 무엇을 변경·생성·실행했는지, 어떤 검사를 실행하고 어떤 결과를 관찰했는지 설명합니다. **완료 / 통과·부분 검사·실패 / 미실행·남은 작업**을 구분하고 파일 작성·실행 성공·사용자 확인·Git 게시·설치·배포를 각각의 실제 상태로 보고합니다.
- **큰 결과의 표현:** 비교·상태는 표, 순서는 번호 목록, 파일 구성은 트리를 사용합니다. 내용에 맞는 형식만 선택하고 깊은 `1. → 1) → a.` 중첩은 관계를 설명하는 데 필요할 때 사용합니다. 짧은 결과에 표·다이어그램·정해진 항목 수를 강제하지 않습니다.
- **잘된 점과 문제점:** 확인된 성과와 문제·제약·미확인 사항을 간단히 적고 필요한 다음 조치를 연결합니다. 성과·문제를 억지로 만들지 않으며 문제를 찾지 못했으면 검증 범위 안의 관찰로 설명합니다. 미검증을 ‘문제 없음’으로 바꾸지 않습니다.

이 절은 폴더 안에서 완결되는 사용 지침입니다. 보고하기 위해 중앙 저장소·다른 skill·별도 설치기 조회를 필수로 요구하지 않습니다. 요청한 읽기 전용 검토를 수정·게시·설치로 확대하지 않습니다.

### Luna 우선 배정과 main AI의 검증

- 범위와 판정 기준이 정해진 파일 목록·문자열 검색·지정 자료 조회·사실 추출·정형 대조는 **Luna에 우선 배정**합니다. 여러 독립 조회를 작은 작업 묶음으로 전달하고 필요한 입력·대상·출력 형식·완료 조건만 공유합니다. 기존 지침·권한·읽기/수정 범위는 그대로 적용합니다.
- 검색이라고 해도 질문 정의·자료 신뢰도와 상충 근거 판단·설계/원인 분석·수정 방향·권한 또는 운영 영향 판단·최종 검증은 main AI가 담당합니다. 수집과 판단을 나눌 수 있으면 Luna의 근거 수집 뒤 main AI가 판단합니다.
- 한두 줄 조회처럼 위임 준비·대기·회수 비용이 더 큰 작업은 main AI가 직접 수행할 수 있습니다. 단순한 작업을 작은 호출마다 새 agent로 나누거나 같은 파일을 반복 조회하지 않습니다. 모델 분담을 설명할 때 실제 선택과 예외를 간결하게 알립니다.
- 사용자가 지정한 모델과 현재 환경에서 실제 사용 가능한 **Luna 계열 모델**을 확인하고, 분담 도구가 모델 선택을 지원하면 해당 작업에 명시합니다. 명확한 단순 작업은 지원되는 낮은 reasoning effort부터 시작하며 고정 수치를 모든 환경에 강제하지 않습니다. 기본 main 모델·개인 config·승인·sandbox·MCP 설정을 자동 변경하지 않습니다. [공식 모델 선택 기준](https://learn.chatgpt.com/docs/models)
- 시작 보고에는 작업 묶음의 모델·수집 범위를, 완료 보고에는 실제 사용한 모델·수행 내용·근거와 미조회/실패를 구분합니다. 모델 지정을 요청한 상태와 실제 확인된 실행 상태를 구분하며 선택을 확인하지 못했다면 확인했다고 주장하지 않습니다. 지침 파일 작성만으로 자동 모델 전환·모든 세션 적용이 된 것은 아닙니다.
- Luna의 결과에는 파일 경로·행 또는 URL/출처, 조회 범위, 실제 개수·관찰 내용, 누락·오류를 필요한 만큼 포함합니다. 도구 오류·읽기 실패·검증하지 않은 검색 결과를 ‘없음’이나 확정 사실로 바꾸지 않습니다. 비밀정보·원시 비공개 자료를 전달/게시하지 않습니다.
- main AI는 결과의 핵심 근거와 누락·일관성을 재대조하고 최종 상태·수정·게시 판단을 담당합니다. 단순 도구 문법 오류는 방법을 교정해 제한적으로 재시도하되 반복 실패·상충·범위 확대·깊은 해석이 필요하면 main AI가 이어받습니다. 같은 결과를 여러 agent에게 무조건 중복 검사시키지 않습니다.
- Luna가 없거나 현재 도구가 모델 선택을 지원하지 않으면 그 한계를 명시하고 승인된 범위에서 main AI가 계속 진행합니다. Luna를 사용했다고 표시하거나 모델·플러그인 설치·외부 서비스 호출을 자동 수행하지 않습니다.

### 저장소 Workflow와 AI 산출물

- 상태·결정·완료 이력은 각 실제 repo 안에서 관리하고 기존 관리 경로를 재사용합니다. 관리 공간의 이름을 Codex 예약 디렉토리나 다른 repo의 강제 경로로 설명하지 않습니다.
- README는 개요·진입 안내, INDEX는 주요 경로·읽기 조건·관련 skill과 기준 문서 연결입니다. INDEX·TODO·일반 관리 Markdown은 기본 자동 발견 이름이 아니며 repo AGENTS와 필요한 skill에서 조회 조건을 연결합니다. 다운로드·설치·발견·선택·행동 검증을 구분하고 같은 이름의 skill은 plugin과 실제 경로로 식별합니다.
- 활성 작업 상태는 기존 TODO 등 한 기준 원본에서 관리하고 task 문서는 범위·입력·완료 조건·결과/검증 링크를 담습니다. 도구 JSON·실행 manifest·외부 tracker의 내부 상태를 TODO로 대체하지 않습니다.
- 일반 관리 기록과 자유롭게 위치를 지정할 수 있는 결과물은 repo 관리 공간에 모읍니다. 선택 skill·제품·도구의 고정 경로·sealed 자료·외부 앱 결과·개인 runtime 상태는 해당 계약을 유지하고 INDEX/TASK에서 연결합니다. 제품 소스·자산·DB·빌드 파일을 AI 결과라는 이유로 자동 이동하지 않습니다.
- 작은 작업에는 모든 관리 문서나 빈 폴더를 생성하지 않습니다. 완료 관리 기록을 먼저 보존하고 링크를 확인한 뒤 활성 목록을 정리하며 산출물·검증 원본은 안정적인 경로에 유지합니다. 비공개 raw/scratch는 Git 제외 여부를 확인합니다.
- 공식 예제도 현재 실제 도구·OS·의존성·사용자 승인·repo 게시 규칙과 대조합니다. 공개 예제의 반복 승인·삭제·main 직접 push·가상 도구 지시를 현재 작업에 자동 적용하지 않습니다.

지속 작업·구조 설계·작업 재개·산출물 정리에는 [저장소 Workflow 상세](repository-workflow.md)에서 문서 역할, TODO.md/TODO 디렉토리 선택, 작업별 tree와 경로 예외를 필요한 범위만 확인합니다.

### 개인 skill 원본·설치·이전본 기록

- 여러 세션이 함께 작업하면 작업ID·담당 파일·예정 commit 파일 목록을 먼저 명시하고 현재 Git 변경과 대조합니다. 다른 세션의 파일은 보존하고 검토한 담당 파일만 staging하며 충돌한 동일 파일의 작성자를 조정합니다.
- 재사용 skill의 관리 원본은 현재 플랫폼의 배포 폴더에 둡니다. `_reference`는 출처·고정 commit·비교용 원본을 관리하는 선택 공간이며 실제 실행본의 필수 의존성이 아닙니다. 외부 저장소 URL이 없는 내부 skill을 같은 repo의 중복 clone으로 보관하지 않습니다.
- 작업 분해가 필요한 큰 변경에는 설치된 `planning-and-breakdown`, 검증한 변경의 commit에는 `git-commit-rule`을 선택합니다. 명시 호출은 `$planning-and-breakdown`, `$git-commit-rule`로 요청 범위를 함께 지정합니다. 미설치 본문은 사용자가 지정한 source 경로에서 읽어 적용하고 설치·자동 발견으로 보고하지 않습니다.
- 설치·갱신은 폴더 전체를 단위로 처리합니다. 기존 동명 사본의 파일·출처·차이를 확인하고 승인된 이전본을 발견 경로 밖의 작업별 보관 폴더에 해시와 함께 보존한 뒤 교체합니다. 파일 작성 날짜나 source에 없다는 이유만으로 다른 개인 skill을 삭제하지 않습니다. system·plugin·인증·모델 설정은 지정한 개인 skill 교체와 구분합니다.
- 사용자가 개인 설정의 업데이트별 백업 폴더를 지정하면 기존 관리 공간 아래 고유한 날짜·목적·작업ID 폴더 하나에 변경 전·후 skill·설정 사본, 출처·해시·검증·복구 기록을 묶습니다. 다음 업데이트는 새 이름으로 추가하고 지난 사본은 갱신하지 않습니다. 활성 상태는 기존 TODO 한 곳에서 관리하며 다른 repo에 35의 경로나 별도 task/history 폴더를 강제하지 않습니다.
- 실제 홈의 원형 백업과 raw·개인 경로가 있는 기록은 Git 제외를 확인한 비공개 작업 폴더에 보관합니다. 사용자가 지정하고 개인정보 검사를 통과한 공개 가능 skill 전체 사본은 업데이트 before/after에 보존합니다. 공개 기록은 환경 별칭·skill 이름·상대 파일 목록·해시·출처·설치/발견/행동 검증 범위를 담고, 기존 사본·JSON·과거 검사 결과는 당시 상태로 유지합니다.

### 단독 사용과 참조

폴더 전체가 사용 단위입니다. 이 폴더 안의 필수 참조·도구만 사용하며 중앙 catalog·installer·30/31 저장소나 다른 skill의 별도 설치를 요구하지 않습니다. `skill://`는 아래 동봉 대응으로 해석하고 Kiro URI/hook/memory API를 호출하지 않습니다. 개인 경로·계정·config 원문·자격증명·세션·raw 비공개 증거를 공개 자료에 복사하지 않습니다.

### Windows 목적별 대응 — 원문 26절 전체

원문의 26절·예시·템플릿·체크리스트를 줄이지 않습니다. 아래 대응은 각 목적을 Windows에서 수행하기 위한 활성 기준이며 원문의 Bash/POSIX/Kiro 실행 방법은 비교 자료입니다.

1. **§1 승인·§1-1 장시간 실행:** 목적·범위를 간결하게 알리고 승인된 작업은 진행합니다. 도구의 비동기 세션/후속 상태 조회를 사용하며 짧은 timeout을 모든 명령에 강제하지 않습니다. timeout은 실패 확정이 아니므로 실제 소유 프로세스·부분 실행·로그를 먼저 확인합니다. 동일 접근 2회 실패 후 근본적으로 다른 접근을 검토하되 승인 밖 재시도·프로세스 종료를 자동 수행하지 않습니다.
2. **§2 위험 작업·§3 삭제:** 현재 승인 범위를 동작 직전에 확인합니다. 대상·영향·복구 범위를 확인하고 Windows 삭제/이동은 절대 경로가 의도한 범위 안에 있는지 확인한 뒤 `Remove-Item`/`Move-Item -LiteralPath`로 수행합니다. 다른 shell이나 문자열 명령으로 권한/범위를 우회하지 않습니다. 이미 승인된 같은 동작은 재확인하지 않습니다.
3. **§4 Markdown:** 한글·트리·표 display width·용어 설명·문체 기준을 유지하고 현재 사용자/저장소 예외를 함께 적용합니다. STYLE은 이 폴더의 동봉 자료로 읽습니다. 원문의 Kiro URI·개인 경로를 실제 Windows 의존 경로로 사용하지 않습니다.
4. **§5 명명·§6 기호·§9 보고:** 기존 개인 명명·허용 기호·간결 한국어 기본값은 유지하되 사용자/저장소의 명확한 고유 규칙이 우선입니다. 실행·정적 확인·미검증을 분리합니다.
5. **§7 권한:** Windows 관리자 토큰·UAC·파일 ACL·서비스 권한과 원격 Linux의 sudo/become는 별도입니다. 실제 권한·대상을 확인하고 필요한 추가 권한은 정상 승인 경로에서 다룹니다. `/root` 경로, 작업 파일 접근 거부, SSH 소유자 확인 실패가 ACL 변경·관리자 실행·sandbox 우회 권한이 아닙니다.
6. **§8 코드 범위·§14 정리:** 요청 범위와 기존 편집을 보존하고 이번 변경 때문에 생긴 불필요 요소만 정리합니다. 테스트는 사용자 범위·저장소 필수 검사·변경 위험에 맞게 수행하며 개인 기본값으로 필수 검증을 생략하지 않습니다. 다른 skill 전체를 일괄 적용하거나 인접 코드를 최적화하지 않습니다.
7. **§10 placeholder:** 원문의 표준 예시 값·비밀정보 금지 목적을 유지합니다. 실제 키·계정·IP·운영 자료를 placeholder에 채우지 않습니다. gitleaks allowlist를 필요 없이 자동 작성/확장하지 않고 실제 설정 범위와 오탐만 확인합니다.
8. **§11 Markdown 검사:** 저장소 지정 검사기를 우선하고 지정이 없으면 현재 변경한 문서에 동봉 Windows Python style/heading/link 도구를 사용합니다. `python -X utf8 -B`와 명시 대상·실제 종료 상태를 확인합니다. 외부 fix_table_align/trim_diagram 도구를 필수 설치하지 않고 보고된 문제를 범위 안에서 수정·재검사합니다. 파일 입력 누락·읽기 실패·미닫힘을 성공으로 처리하지 않습니다.
9. **§12 사후 검증:** 문법/변경 영향/건강/모니터링의 목적을 실제 기술에 맞춰 적용합니다. 코드/문서 검토 요청에 Terraform/AWS/서비스 실행을 강제하지 않습니다. plan/apply/운영 검사가 없거나 미실행이면 그 이유와 남은 조건을 보고합니다.
10. **§13 계획·§26 batch:** 작업에 필요한 계획·checkpoint·pre/post 보고를 현재 사용자·저장소 양식에 맞춰 작성합니다. 본문에 있는 과거 TODO §4·3항목 batch·모델 역할이 모든 새 작업의 강제 체계는 아닙니다. 채택한 batch에는 준비→작성→검사→사실 확인→상태 갱신과 미완료 재개 목적을 유지합니다.
11. **§15–16 reference·§24 GitHub 색인:** 공식 출처 확인·출처/확인일/미확인 구분·전파 범위 대조를 유지합니다. 현재 저장소가 채택한 `_reference`/INDEX/GitHub 목록만 필요한 범위에서 갱신하고 다른 저장소의 디렉터리를 생성/수정하지 않습니다. `lynx`, Bash curl pipeline은 Windows 필수 도구가 아니며 제공된 웹 도구/실제 curl.exe/PowerShell HTTP 도구로 공개 공식 자료를 확인합니다. 네트워크 실패·자료 부재는 미확인이고 추정으로 공식 사실을 만들지 않습니다.
12. **§17 Python:** 구조·SAFETY·날짜 VERSION·argparse·docstring·최소 예외·필수 option/help와 검증 목적을 유지합니다. Windows에서는 실제 python.exe를 명시하고 JSON/TOML/config/status의 encoding·경로·최종 종료 상태를 명확하게 처리합니다. 파일 owner/mode·ACL·atomic replace는 같은 기능으로 간주하지 않습니다.
13. **§18 SSH 인코딩:** local PowerShell → SSH client → 원격 기본 shell → 실제 powershell.exe/pwsh/Linux shell의 계층을 확인합니다. 원문의 `cmd /c chcp` 중첩 quote를 Windows 공통 필수 패턴으로 실행하지 않습니다. 원격 Windows PowerShell의 복잡한 스크립트에는 실제 지원하는 `-EncodedCommand`(UTF-16LE Base64)를 검토하고, 입력 데이터와 스크립트를 분리해 injection을 막습니다. 원격 실행 정책·host key·코드페이지·stdout/stderr·종료 상태를 실제 fixture로 확인하며 인코딩 옵션이 승인/권한을 우회하지는 않습니다.
14. **§19 치환 확인:** 치환 전 대상과 예상 건수를 확인하고 이후 관련 행·잔여 문자열·참조·영향 범위를 `rg` 또는 `Select-String -LiteralPath`로 대조합니다. 일괄 값 변경은 승인한 파일 목록에서 처리하며 로그/비밀정보를 공개 출력하지 않습니다. 0건 치환을 성공으로 처리하지 않고 의도된 0건과 실패를 구분합니다. sed 예시를 PowerShell에서 실행하지 않습니다.
15. **§20 VM:** 실제 VM 목록·대상·상태·삭제/중지/재생성 차이와 현재 승인 범위를 확인합니다. Hyper-V cmdlet·관리자 권한·vagrant provider는 실제 존재할 때만 사용합니다. 이미 대상까지 승인된 작업에 같은 삭제 승인을 반복 요구하지 않으며 범위 밖 VM은 변경하지 않습니다.
16. **§21 SSH 프로세스:** 시작 시 모든 SSH/PID를 일괄 kill하는 원문 예시는 실행하지 않습니다. 현재 작업이 시작한 process/session의 PID·소유·대상과 부분 실행을 확인해 정상 종료를 우선합니다. 필요한 `Stop-Process`는 그 작업의 확인된 PID·승인 범위에서만 사용합니다. 다른 사용자/작업·전체 ssh.exe·원격 서비스를 종료하지 않습니다.
17. **§22 잠금:** Kiro disabled 파일·hook을 생성/삭제하지 않습니다. 현행 저장소 정책을 확인하고 동봉 Windows kiro-lock helper의 root·task token으로 acquire/check/release합니다. token은 현재 작업에서 생성해 유지하고 타인의 token을 채택하지 않습니다. R08 부분 생성 실패 정리는 실제 helper의 소유·inode 확인 범위로 검증해야 하며 손상/오래된 lock을 시간 경과만으로 삭제하지 않습니다. 참여자 공유와 일반 파일 byte lock은 별도 프로토콜입니다.
18. **§23 PLAN 기록:** 비자명한 오류·원인·보완·재현·검증을 현재 저장소가 정한 실제 문서의 기존 항목과 연결합니다. 루트/하위 PLAN 선택과 번호는 현재 지침을 따르고 없으면 자동 governance 초기화를 하지 않습니다. 반복 항목을 중복 생성하지 않으며 Kiro hook 활성화가 기록의 선행 조건은 아닙니다.
19. **§25 memory:** Kiro memory API·개인 파일을 자동 만들지 않습니다. 사용자가 명시한 현재 기록/메모 경로에서만 보존·최대 분량·archive·동기화 목적을 적용합니다. 개인 메모·세션·실제 계정·비밀정보는 공개 Git에 복사하지 않고 요약 확인도 비공개 내용을 드러내지 않습니다.

### Windows Python config·status·종료 상태

원문의 `load_config` 자동 발견은 현재 SCRIPT_DIR 아래 실제 설정 1개가 확인된 경우만 적용합니다. 경로를 주면 실제 지정 파일을 사용하고 TOML은 binary·JSON은 UTF-8로 읽으며 필수 키·타입·범위를 검증합니다. 다른 홈·config를 검색/복사하거나 모호한 첫 파일을 선택하지 않습니다.

```python
# 현재 코드의 SCRIPT_DIR·필수 키/범위 계약을 사용합니다.
import json
import tomllib
from pathlib import Path


def load_config(config_path=None):
    """Load one explicitly selected or unambiguous TOML/JSON config."""
    if config_path is None:
        candidates = sorted(Path(SCRIPT_DIR).glob('*config.toml'))
        candidates += sorted(Path(SCRIPT_DIR).glob('*config.json'))
        if len(candidates) != 1:
            raise FileNotFoundError('exactly 1 config file required')
        config_path = candidates[0]
    selected = Path(config_path)
    if selected.suffix.lower() == '.toml':
        with selected.open('rb') as stream:
            return tomllib.load(stream)
    if selected.suffix.lower() != '.json':
        raise ValueError('expected TOML or JSON config')
    with selected.open('r', encoding='utf-8') as stream:
        return json.load(stream)
```

이 config 함수는 기존 프로그램의 전달된 자료를 읽는 패턴입니다. 설정 병합·설치·실제 서비스 변경을 수행하지 않습니다. 신규 코드는 module import 순서 등 원문의 개인 양식을 함께 적용합니다.

원문의 `write_status(error_codes)` 목적은 모니터링 프로토콜의 상태 기록입니다. 실제 LOG_DIR/STATUS_FILE·오류 코드 의미를 확인하고 UTF-8로 기록합니다. 0 성공/비정상 실패 집계를 프로젝트 계약에 맞추고 실패를 status나 프로세스의 0으로 덮지 않습니다. `main()`의 최종 결과는 `sys.exit(main())`로 프로세스에 전달하며 R07 누락/혼합 입력과 R14 등록된 도움말 option을 함께 검사합니다.

### Windows file lock의 실행 기준

원문의 `fcntl.flock`·정상 해제 시 경로 삭제 예시는 Windows에서 실행하지 않습니다. 아래는 Windows의 프로세스 중복 실행 방지를 위한 **별도 byte-lock 패턴**입니다. 공유 경로를 유지하고 각 참여자가 같은 byte 위치를 잠급니다. OSError를 모두 “already running”으로 바꾸거나 종료 0으로 처리하지 않습니다.

```python
import msvcrt
import os
from contextlib import contextmanager


@contextmanager
def exclusive_file_lock(lock_file):
    """Hold one Windows byte lock on a persistent local path."""
    flags = os.O_RDWR | os.O_CREAT | getattr(os, 'O_BINARY', 0)
    fd = os.open(lock_file, flags, 0o600)
    with os.fdopen(fd, 'r+b') as lock_fp:
        if os.fstat(lock_fp.fileno()).st_size == 0:
            lock_fp.write(b'\x00')
            lock_fp.flush()
        lock_fp.seek(0)
        msvcrt.locking(lock_fp.fileno(), msvcrt.LK_NBLCK, 1)
        try:
            yield lock_fp
        finally:
            lock_fp.seek(0)
            msvcrt.locking(lock_fp.fileno(), msvcrt.LK_UNLCK, 1)
    # Keep the path so every cooperating process locks the same file.
```

실제 호출부는 `with exclusive_file_lock(LOCK_FILE):` 안에서 작업하고 I/O·권한·이미 잠긴 경우의 실제 실패를 로그/비정상 상태로 전달합니다. path 존재만으로 잠금 여부를 판단하지 않습니다. 이 패턴은 참여자·동일 경로·로컬 Windows byte locking 범위이며 symlink/reparse point·교체 writer·네트워크 FS·ACL·비협력 프로세스의 보장이나 동봉 kiro-lock helper와의 호환을 주장하지 않습니다. 실제 대상 적용 전 별도 정상·경쟁·예외 검증이 필요합니다.

### Windows SSH·ACL와 문서 도구

Windows OpenSSH user key·server host key·authorized_keys·관리자용 authorized_keys는 서로 다른 소유/ACL 대상입니다. 실제 계정·client/server·공식 설정·현재 ACL을 필요한 범위에서 확인하고 원문의 chmod 600·경로 예시를 기계적으로 적용하지 않습니다. 키 본문·다른 계정의 키를 출력하지 않으며 정상 인증 실패를 ACL 완화·host key 확인 생략으로 우회하지 않습니다.

PowerShell 5.1의 `>`/Out-File·인코딩과 PowerShell 7의 기본값은 다릅니다. Python UTF-8 문서·state bytes·SSH stdout을 각각 확인합니다. 5.1에서 Set-Content -Encoding UTF8의 BOM 여부가 영향을 주는 경우 .NET의 명시적인 UTF8Encoding과 현재 파일 형식을 사용하며 전체 설정을 일괄 다시 저장하지 않습니다.

문서 도구 호출은 실제 runtime과 이 폴더 경로를 사용합니다. 원문의 `python3`/sia-md-* 이름이 Windows alias라는 이유로 설치/동작을 추정하지 않습니다. 사용자/저장소가 footer·날짜·배지를 금지하면 style의 footer 검사만 근거와 함께 제외하고 다른 검사를 유지합니다. 보존 원문 경고·새 경고·읽기 실패·부분 검사를 구분합니다.

공식 플랫폼 근거: [PowerShell 인코딩](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-5.1), [EncodedCommand](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.2), [Windows OpenSSH 키/ACL](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement), [Ansible controller 플랫폼](https://docs.ansible.com/projects/ansible/latest/os_guide/intro_windows.html).

### 동봉 Windows 역할 대응

현재 작업에 필요한 다음 전체 사본만 읽습니다. 형제 skill 별도 설치를 요구하지 않습니다.

- `skill://incremental-change` → [incremental-change](skills/incremental-change.md).
- `skill://kiro-lock` → [kiro-lock](skills/kiro-lock.md).
- `skill://planning-and-breakdown` → [planning-and-breakdown](skills/planning-and-breakdown.md).
- `skill://spec-driven-infra` → [spec-driven-infra](skills/spec-driven-infra.md).
- `skill://readme-template` → [전체 readme-template 지침](skills/readme-template.md).

문서 개인 양식은 [STYLE.md](STYLE.md)를 현재 사용자/저장소 예외와 함께 적용합니다.

### 동봉 도구 호출

다음 PowerShell 호출의 `$pythonExe`는 확인한 실제 Python, `$skillDir`는 현재 복사된 폴더, `$target`은 명시한 검사 대상입니다. 코드 작성과 실제 실행/설치 검증을 구분합니다.

```powershell
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/lock.py') --help
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-heading-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-link-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
& $pythonExe -X utf8 -B (Join-Path $skillDir 'scripts/md-style-check.py') $target
if ($LASTEXITCODE -ne 0) { throw '동봉 도구 실패 또는 검사 오류: 결과를 확인하세요' }
```

잠금 help 확인은 실제 acquire/check/release나 전체 실패/경쟁 검증이 아닙니다. 원문의 Kiro 실행 상태와 새 Windows 설치 상태를 혼동하지 않습니다.

원문 비교 자료: [Kiro 원문](kiro-original.md). 비교용 원문은 실행 지시로 다시 로드하지 않습니다.
