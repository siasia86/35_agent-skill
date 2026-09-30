# Codex governance 개선 검증 기록

## 1. 실행 범위와 결과

CG-20260929는 요청받은 Codex 이식·개인 자산·중앙 두 governance 역할의 개선 작업입니다. 계정 소유 독립 작업본에서 개발·검증한 뒤 사용자의 이번 1회 승인으로 root 30·31·35에 반영했습니다. 개인 runtime·기존 release·실제 consumer는 변경하지 않았습니다.

- 30: `python3 -m unittest discover -s tests -p 'test*governance*.py'` 회귀 103개 통과입니다. 새 codex_governance 17개와 기존 staging 13개가 포함됩니다. 전체 Python test suite·원격 CI 통과로 확대하지 않습니다.
- 35: 기존 payload skill 25개 quick_validate, agent TOML 10개, catalog 선택 ID 36개·파일 37개·동반 참조 inventory 및 SHA-256을 확인했습니다.
- 31: 공통·저장소별 정책과 template pin, 기존 v2 AI profile의 읽기 전용 plan 호환 및 draft manifest 66개 파일 hash·자체 checksum을 확인했습니다.
- 세 repository 후보: build·check·unchanged를 확인했습니다. 각 일곱 파일이며 draft·deployable false입니다. 후보 Markdown·skill 문법과 skill-relative 정책 참조·해시를 확인했습니다.
- companion 예시: 기존 skill·agent 네 자산의 plan을 대조한 후보가 통과했습니다. instruction을 함께 선택한 기존 v2 예시는 AGENTS 경로 충돌로 거부됐고 거부 전후 staging inventory·size·mtime은 동일했습니다.
- 변경 문서와 생성 후보의 style·heading·link, git diff --check·gitleaks를 통과했습니다. codex 전체 95개 Markdown의 로컬 링크 51개는 오류 0건입니다. 외부 URL 가용성 검사는 별도입니다.
- archive 35개 논리 자산의 original_path·original_sha256은 HEAD 원문 bytes와 일치합니다. 열람본의 이동 링크 세 곳과 문서 footer를 정리했고 해당 원문은 SKILL.md.original로 보관했습니다. baseline·Kiro/GPT 원본은 변경하지 않았습니다.

2026-09-29 root 반영본에서도 governance 회귀 103개·문법·변경 Markdown·payload/catalog 37파일·draft manifest 66파일·후보 생성/check/unchanged·companion 충돌 거부를 다시 통과했습니다. 비밀정보·diff 검사는 승인된 변경 대상에 한정했습니다. 전체 작업 트리 diff는 읽기 권한이 없는 기존 Kiro 세 파일 때문에 실패했으며 해당 변경을 commit에 포함하지 않습니다. root 전체나 최신 Kiro 대조가 통과했다고 해석하지 않습니다.

## 2. 독립 검토와 수정

TODO §8.3에 따라 구현 CG-30은 governance_generator, 정책·권한·forward-test 검토 CG-REVIEW는 governance_review에 위임했습니다. 요청 모델은 각각 gpt-5.6-terra medium, gpt-5.6-sol high입니다. canonical agent ID는 /root/governance_generator, /root/governance_review이며 실제 runtime 모델 ID는 독립적으로 확인하지 못했습니다. 동일 파일 작성자는 분리했고 주 agent가 결과와 회귀를 직접 확인했습니다.

독립 검토는 이동 링크, draft manifest 누락, 생성기·검증 모듈 provenance, skill routing 설명, 정책 읽기 실패 중단 조건, 31 문서 변경의 필수 읽기 누락, 기존 instruction의 교차 target 충돌을 발견했습니다. 상대 링크·원문 보존, metadata 등록, 실행 코드 내용 해시, binding 없는 경우의 discovery 설명, 영향받는 수정·완료 중단, 문서 정책·중앙 계약 읽기, companion plan 충돌 거부와 AGENTS 병합 계약으로 보완했습니다.

README 상대 링크 네 곳을 수정하는 현실적인 요청을 독립 검토에 직접 전달하여 필수 정책 읽기·기존 변경 보존·기록·검사·게시 경계를 확인했습니다. 단순 변경에 고정 단계 수 PLAN을 강제하지 않습니다. 이 검토는 지침을 수동 전달한 행동 검토이며 실제 Codex skill 자동 선택·agent 이름 기반 호출 시험이 아닙니다.

## 3. 최신 Kiro 대조 제한

다음 원본은 0600·nobody:nogroup이고 현재 계정으로 읽을 수 없습니다. Git 상태에는 기존 사용자 수정이 있으며 clone의 HEAD 원문을 최신 변경분 대조 자료로 사용하지 않았습니다.

- kiro/skills/md-link-check/SKILL.md.
- kiro/skills/repo-governance/SKILL.md.
- kiro/skills/work-rules/SKILL.md.

OS 권한·소유권을 변경하지 않았습니다. 최신 세 파일의 전체 내용 대조는 미완료입니다. 사용자가 원문을 제공하거나 정상 읽기 접근이 생긴 뒤 별도 대조해야 합니다.

## 4. 미실행과 복구

실제 개인 설치·새 세션 자동 정책 로딩·hook·위임·ACL·운영 적용·release는 미실행입니다. 사용자는 이번 변경의 root 반영과 yunli commit·일반 push를 승인했습니다. 게시 성공·원격 CI 결과는 실행 후 Git 및 별도 실행 기록에서 확인하며 사전 검사로 통과를 주장하지 않습니다. 현재 hash는 내용 식별이며 승인 서명·불변 Git source freeze·악의적인 동시 교체 격리를 대신하지 않습니다. logical target guard는 실제 runtime 경로 mapping·기존 AGENTS의 검토된 병합을 대신하지 않습니다.

미게시 변경은 해당 diff만 검토해 되돌립니다. 개인 홈과 consumer 파일의 복구를 수행한 것으로 기록하지 않습니다. 직접 수정 제한의 이전 예외를 재사용하지 않으며 현재 작업은 대상·범위·검증·복구·종료 조건을 갖춘 사용자 승인을 기록했고 종료 시 만료됩니다.


## 5. 2026-09-30 최신 Kiro 세 파일 대조와 보완

사용자 요청은 세 Kiro skill의 분석과 Codex skill 보완입니다. 작업 시작 시 yunli 작업 트리는 깨끗했고 세 원본을 읽을 수 있었습니다. 전체 본문을 대조했으며 HEAD와 동일한 bytes임을 확인했습니다. 과거 9월 29일의 읽기 실패는 당시 기록으로 유지합니다. 이번에는 codex 후보·관련 안내·TODO·CHANGELOG만 변경하고 Kiro/GPT 원본·권한·runtime·30/31 저장소는 변경하지 않습니다.

### 원본 식별

- kiro/skills/md-link-check/SKILL.md: `67bc59e6ca5432cd17ce0d13077cbaeaa51cc00c9c5764c8565323869d85aa05`.
- kiro/skills/repo-governance/SKILL.md: `ec70916e7a09db1f82c4c4882292b9cb1d1ed8d72ba7ed27008a366eb9e95e17`.
- kiro/skills/work-rules/SKILL.md: `a940ad7376aecac56a873671a3f77250fb6d4f6deb77598810bdfefd1420ed20`.

### 이식 결정

- md-link-check: 파일 링크·같은 파일 앵커·다른 파일 fragment·목차·style의 검사 범위를 구분합니다. 간이 slug 추정 대신 renderer/checker를 사용하고 코드 예시 제외·중첩 fence·경로 인자 처리·검토와 수정 권한을 보완합니다. 원본의 H2 번호·목차·문체 규칙은 선택 정책이 있을 때만 적용합니다. emoji·중복 앵커에 관한 원본 설명을 보편 규칙으로 복사하지 않습니다.
- repo-governance: 숨김 governance와 실제 entrypoint·예외·검사 정책을 발견하고 worktree의 .git 파일도 처리합니다. 필수 정책 실패와 선택 파일 부재를 구분하고 영향받는 수정·완료만 중단합니다. 고정 개인 경로·신규 governance 자동 생성·사용자 지시가 플랫폼보다 우선한다는 해석은 이식하지 않습니다.
- work-rules: 공유 값 교체의 누락·동시 변경·비밀 노출, timeout 후 부분 실행 상태, 소유 프로세스 확인, 권한 오류 구분, 예제 자격증명 allowlist, 기록 중복과 참조 provenance를 보완합니다. 일반 변경마다 재승인·sudo·광범위 kill·Kiro lock 활성화·다른 저장소 reference 자동 추가·memory 자동 수정·고정 3항목 배치/검토 회차는 이식하지 않습니다. 개인 Python 양식과 Windows 작업은 기존 선택형 skill/reference를 유지합니다.
- 동반 참조 3개를 필요한 작업에서만 읽는 구조와 36 ID·40파일을 유지합니다. catalog의 변경 SHA-256을 갱신합니다. 이전 README의 2개 skill·2개 agent 안내도 현재 후보 수에 맞춥니다.

### 관찰과 검증 범위

설치된 sia-md-link-check와 sia-md-heading-check를 임시 디렉토리의 정상 링크·파일 누락·같은 파일 앵커 누락·다른 파일 앵커 누락·중첩 fence 및 공백/한글/하이픈 파일명에 실행했습니다.

- 정상 같은 파일 앵커: 두 검사 exit 0.
- 없는 파일 링크: link exit 1, heading exit 0.
- 없는 같은 파일 앵커: link exit 0, heading exit 1.
- 기존 파일의 없는 fragment: 두 검사 exit 0. 목적지 앵커 검증 누락이며 전체 통과로 판단하지 않습니다.
- 유효한 네 backtick 외부/세 backtick 내부 예시: heading은 실제 헤딩 2개만 확인하고 exit 0, link는 예시 내부 absent.md를 실제 링크로 오탐하여 exit 1. 코드 예시 수정 대신 도구 한계를 기록합니다. 공백·한글·하이픈 경로는 절대 경로 인자로 전달됐습니다.

최종 정적 검사: skill-creator validator로 payload skill 25개, tomllib로 agent 10개, catalog 36 ID·40파일 SHA-256을 확인했습니다. 변경 Markdown 11개 style·heading·로컬 파일 link, git diff --check, codex 범위 Gitleaks 탐지 0건을 확인했습니다. 세 Kiro 원본은 HEAD bytes와 일치합니다. 로컬 파일 링크 통과를 cross-file fragment 전체 검증으로 확대하지 않습니다.

이 시험은 설치된 checker의 동작이며 Codex의 자동 skill 선택/행동 시험이 아닙니다. checker 구현 수정·30/31 고정 profile 해시 갱신·배포 연동·원격 CI·runtime 설치·hook 검증은 미실행입니다. 31의 기존 pin은 변경된 35 catalog와 다시 정합화해야 하며 이번 후보를 기존 승인 패키지에 자동 적용하지 않습니다. 미게시 복구는 이번 변경분만 되돌리고 skill·참조·catalog 해시를 함께 복원합니다.

## 6. 2026-09-30 31/35 중복 검토와 agent 인계

사용자 요청은 31과의 중복 확인 및 별도 31 agent가 이해할 인계 문서 보완입니다. 31은 읽기 전용으로 확인하고 35의 기존 governance 안내·작업 기록·TODO·CHANGELOG를 보완합니다. 31 기존 HANDOFF의 보완 패치는 준비했으나 원본에 적용하지 않았습니다. 이번 문서 변경의 미게시 복구는 해당 diff만 검토해 되돌립니다.

### 대상과 관찰

31의 AGENTS와 지정 운영·작업·검증·문서·중앙 계약 정책, Codex default policy·31/35 repository policy, 두 Codex profile·v2 AI profile·후보 계약, HANDOFF·PLAN·TODO를 대조했습니다. 35에서는 세 변경 skill·동반 참조·개인 AGENTS·governance template와 catalog를 확인했습니다. 보존 정책 전체의 중복 제거·모든 consumer·runtime 설치 목록 감사는 범위에 포함하지 않습니다.

31 HEAD는 `d733b83333b603792b16bb3c9e4c620233836fe6`이며 작업 트리 변경은 없었습니다. 최초 Git 상태 조회는 dubious ownership으로 거부됐습니다. 전역 설정·소유권을 바꾸지 않고 이후 읽기 명령과 패치 사전 검사에만 명령별 safe.directory를 지정했습니다. 35에는 앞선 미커밋 변경 12개가 있었고 이를 보존했습니다.

- 의미상 반복: 31 default policy와 35 work-rules의 권한·변경 보존·기록·검증 기준입니다. 중앙 원본은 31이고 35는 선택형 관례·실행 절차입니다. 전역 정책 사본으로 분리 배포하거나 두 문서의 기록 규칙을 이중 적용하지 않도록 인계에 명시했습니다.
- 역할 분리: repo-governance는 discovery·누락·충돌 조사, governance-repository는 고정 정책 적용입니다. md-link-check는 검사 절차이고 31 documentation 정책은 양식 선택입니다. 이번 대조 범위에서 서로 다른 중앙 원본을 소유하는 신규 충돌은 확인하지 않았습니다.
- target 중복: se-instructions와 생성 AGENTS의 기존 충돌은 계약에 명시돼 있습니다. companion 예시는 해당 instruction을 제외하며 실제 runtime 경로 mapping과 AGENTS 병합은 여전히 후속 gate입니다. 이번에 target 충돌 거부 시험을 재실행하지 않았습니다.
- 인계 누락: 31 HANDOFF의 9월 29일 최신 Kiro 전체 대조 미완료 안내에 이후 완료 상태가 없었습니다. 35 PLAN에도 같은 현재형 안내가 남아 날짜별 상태로 정정했습니다. 31의 과거 기록을 삭제하지 않고 후속 절을 추가하는 패치를 준비했습니다.

### 읽기 전용 연동 검사

31 `profiles/codex_governance.v1-draft.json`의 templates 네 개는 35 실제 bytes, default_policy와 repositories 세 개는 31 실제 bytes에 대해 SHA-256을 다시 계산했습니다. 총 8개 pin 모두 일치합니다. 이번 변경에 이 profile의 template·정책 pin 갱신은 필요하지 않습니다.

현재 35 catalog SHA-256은 `9a70dfbb8048618698f122edea54ffaedb568f32c800c819be43ff7c1bcf5f8f`입니다. 31 v2 profile의 catalog pin은 `495180b5613a9f6d402479b08027272a801a8102021045da00db120beded3e27`이며 불일치합니다. 30의 실제 planner에 다음 두 profile과 현재 catalog를 전달했습니다. 아래 변수는 각 승인된 작업본 루트입니다.

```bash
python3 "$SCRIPTS30/src/governance_profile.py" --profile "$SOURCE31/profiles/codex_companion_assets.v1-draft.json" --catalog "$ASSETS35/codex/ASSET_CATALOG.json"
python3 "$SCRIPTS30/src/governance_profile.py" --profile "$SOURCE31/profiles/ai_document_review.v2-draft.json" --catalog "$ASSETS35/codex/ASSET_CATALOG.json"
```

companion v1은 exit 0·deployable false로 통과했습니다. v2는 exit 2와 `catalog SHA256 does not match profile provenance`로 거부됐습니다. 원인은 catalog pin 불일치이며 전체 연동 통과로 기록하지 않습니다. catalog pin을 정합화한 뒤 재검사하고 선택 자산 변경·staging guard·생성/check·무변경 재생성·draft manifest checksum을 확인하는 순서를 [31 agent 인계](CODEX_GOVERNANCE.md#6-31-담당-agent-인계와-중복-판정)에 남겼습니다.

이번에 수정한 35 Markdown 5개의 style·heading·파일 link 검사와 git diff --check는 통과했고 codex 범위 Gitleaks는 탐지 0건입니다. 새 cross-file fragment는 목적지의 실제 절 제목과 대조했으며 file-link checker가 해당 fragment를 검증한 것으로 주장하지 않습니다.

31 HANDOFF 패치는 현재 파일에 대한 git apply --check를 통과했습니다. 임시 미리보기의 style·heading 검사는 exit 0입니다. 미리보기는 원래 상대 링크의 대상 트리가 없으므로 로컬 링크 검사는 31에서 적용 후 수행해야 합니다. 31 원본 수정·pin 갱신·manifest 변경·staging build/check·원격 CI·runtime·hook·commit·push·release는 미실행입니다.

## 7. 2026-09-30 독립 개인 skill setup

사용자 요청에 따라 README의 Linux·Windows 수동 복사 안내와 `scripts/setup_personal_skills.py`, 격리 시험 `tests/test_setup_personal_skills.py`를 추가했습니다. 경로는 이 codex 디렉토리 기준입니다. 기존 payload·catalog bytes와 앞선 사용자 변경은 보존했습니다. 35의 개인 bootstrap은 현재 사용자의 선택 설치만 담당하고 중앙 정책·profile·release 배포는 기존 30·31 계약에 남깁니다.

### 개인 사용과 의존성

payload skill 본문의 참조와 실제 파일 링크를 정적으로 대조했습니다. 31 고정 경로나 policy 참조를 필수로 읽는 독립 payload skill은 없으며 repo-governance의 governance-repository 안내는 중앙 binding이 있을 때의 조건부 경로입니다. Python 템플릿 asset과 work-rules 참조는 자체 폴더에 포함됩니다. 코드 검토·디버깅·테스트 선택·문서 검토·스크립트 작성은 개인 skill 절차로 사용할 수 있도록 README에 안내했습니다.

이 판단은 정적 참조와 독립 설치 시험에 근거하며 Codex가 모든 작업에서 skill을 자동 선택하거나 지침대로 행동했다는 검증은 아닙니다. Git·checker·프로젝트 테스트 등 작업별 실행 도구는 별도로 필요하고 해당 저장소가 필수 정책을 지정하면 그 지침은 따릅니다. 독립 사용을 이유로 필수 정책 실패를 우회하지 않습니다.

### 구현과 검사

setup은 Python 3.9 이상 표준 라이브러리와 이 저장소 catalog만 사용합니다. list, 명시적인 전체/선택 설치, 목적지 지정, 쓰기 없는 dry-run을 제공합니다. 선택 source의 inventory·SHA-256을 검사하고 읽어 검증한 bytes로 staging을 구성합니다. 기존 동일 파일은 건너뛰고 기존 수정·추가 파일·symlink·알 수 없는 선택·경로 탈출·중복 JSON/ID는 거부합니다. 자체 설치끼리 충돌을 줄이기 위해 목적지 옆에 lock을 만들며 다른 lock을 지우지 않습니다. 외부 작업자의 동시 교체나 여러 skill 전체의 원자적 배포를 보장하지 않습니다.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s codex/tests -p 'test_setup_personal_skills.py' -v
python3 codex/scripts/setup_personal_skills.py --help
python3 codex/scripts/setup_personal_skills.py list
```

위 명령은 35 루트에서 실행했습니다. Python 3.14.6에서 시험 9개를 통과했고 help·25개 skill 목록을 확인했습니다. 실제 홈 밖의 공백 포함 임시 경로에 catalog·payload·setup만 복사하여 30·31 없는 설치를 시험했습니다.

- 전체 25개 skill·동반 파일 4개 설치와 SHA-256, 재실행 시 파일·mtime 보존.
- dry-run에서 목적지·상위 디렉토리 미생성.
- 사용자 변경 충돌 시 신규 batch도 쓰기 전 중단, 기존 내용 보존.
- 원본 변조·동반 파일 누락·잘못된 선택·상위 탈출·중복 입력 거부.
- source·destination symlink와 기존 lock 보존·거부.
- 두 번째 폴더 배치 실패 주입 시 완료된 첫 폴더 보존, 미완료 폴더 미배치, 임시 staging·자체 lock 정리.

compile와 Python 3.9 문법 파싱은 통과했으며 실제 Python 3.9 실행 시험은 미실행입니다. Linux 수동 Bash 예시도 임시 경로에서 복사·동반 참조 보존·기존 설치 거부를 확인했습니다. payload Markdown 28개의 파일 link 검사와 catalog 36 ID·40파일 해시 확인은 통과했고 catalog digest는 §6의 값과 같습니다. 31 v2의 기존 pin 불일치는 이 setup 변경으로 해결하지 않았습니다.

변경 문서의 style·heading·파일 link와 diff, codex 범위 Gitleaks 탐지 0건을 확인합니다. Windows·PowerShell·Python 3.9 runtime·실제 sjyun 홈 설치·새 Codex 세션의 발견/행동·원격 CI·commit·push는 미실행입니다. 설치 중 실패 시 완료된 신규 폴더가 남을 수 있으므로 출력·현재 bytes를 확인한 뒤 해당 설치분만 검색 밖으로 격리하고 사용자 수정·기존 설치·백업은 보존합니다.

## 8. 2026-09-30 Windows clone 수정과 skill 정리

사용자 요청은 재현한 Windows 설치 결함 수정·재검증 및 공식 Codex 문서에 따른 불필요한 skill 제거입니다. 시스템 파일·개인 홈·Kiro/GPT 원본·31 원본은 수정하지 않습니다. skill-creator의 범위·구체적 역할·짧은 선택 조건 기준을 적용했고 실제 열람한 공식 문서와 9개 제외 판단·대체 경로는 [정리 기록](WORKFLOW_SKILL_PLAN.md#5-2026-09-30-개인-skill-설치-목록-정리)에 있습니다.

### 수정과 보존

수정 전 실제 Git core.autocrlf=true clone에서 payload가 CRLF로 변환되고 setup이 source hash mismatch·exit 1로 거부됨을 재현했습니다. `.gitattributes`에서 catalog·payload·governance template·setup/test Python의 LF를 고정했습니다. 설치기의 정확한 bytes 해시 검증은 유지합니다. Kiro/GPT·기존 archive에는 text/eol 속성을 지정하지 않습니다.

일반 라우팅·계획·단계별 진행·위험/출시 체크리스트·일반 README·중복 검증 진입점·Kiro lock·Zircon 예외의 skill 9개를 설치 목록에서 제외했습니다. 기존 payload bytes는 `archive/retired-payload/skills/`로 옮기고 HEAD bytes 동일성을 확인했습니다. 검증 선택은 testing-guide에 통합했고 catalog의 system-engineer·infra_worker optional 참조를 spec-driven-infra·testing-guide로 갱신했습니다. 실제 개인 홈의 기존 설치는 삭제하지 않습니다.

현재 skill 16개·agent 10개·개인 지침 한 개·동반 파일 4개이며 catalog는 27 ID·31파일입니다. 현재 catalog SHA-256은 `ccebd262ad7e8a14a418ff053999f953e28507bd0b5bb2aa7060c9316c528261`입니다. §5~§7의 25개·40파일 및 이전 catalog digest는 당시 검사 상태로 보존합니다. 현재 설치 목록과 31 후속 작업은 README·PAYLOAD_MAP·Codex 지침·governance 인계에서 갱신했습니다.

### 재검증 결과

- setup 회귀 10개 통과: 기존 9개와 실제 Git core.autocrlf=true clone 후 전체 skill 설치·원본 bytes 동일성 시험입니다. Git fixture는 임시 경로에서만 commit·clone하며 이 저장소나 원격에는 게시하지 않습니다.
- skill-creator validator 16개·agent TOML 10개·catalog 27 ID·31파일의 SHA-256·optional 참조 존재 검사 통과입니다. 제거 payload 9개의 bytes는 HEAD와 일치합니다.
- Python compilation·3.9 문법 파싱, 변경·신규 Markdown 27개의 style·heading·파일 link, git diff --check와 codex 범위 Gitleaks 탐지 0건을 확인했습니다. fragment는 검사 도구의 기존 한계를 유지하며 새 링크의 목적지 절 제목을 별도로 대조했습니다.
- Git check-attr에서 catalog·payload는 text/eol=lf, Kiro/GPT 원본은 unspecified입니다. 시스템 skill과 현재 개인 skill의 동일 이름 충돌은 없으며 역할 겹침을 실제 제공 범위로 판단했습니다.
- 30 planner에 현재 catalog와 31 companion v1을 읽기 전용으로 전달하여 exit 0·4개 선택·warnings 없음·deployable false를 확인했습니다. 31 v2 catalog pin은 여전히 이전 digest이며 31 담당 agent가 선택 ID·pin·manifest·staging을 정합화해야 합니다.

검사는 Linux Python 3.14.6에서 수행했습니다. Git 줄바꿈 변환은 실제 clone으로 검증했지만 Windows OS·PowerShell·Python 3.9 runtime·실제 sjyun 홈 설치·새 Codex 세션 발견/행동·경량화 품질/성능 측정·원격 CI·운영 적용·release·이 저장소 commit/push는 미실행입니다. 제거한 skill의 기능별 대체 경로는 정적으로 검토했으며 모델 행동 동등성을 주장하지 않습니다.

종료 전 31 status에서 별도 작업의 PLAN·CHANGELOG·계약·manifest 변경이 확인됐습니다. 이 세션은 31에 쓰지 않았으며 해당 변경을 통합·검증한 것으로 기록하지 않습니다. 31 HANDOFF용 패치는 현재 목록으로 갱신하고 apply --check를 통과했으며 원본에는 적용하지 않았습니다. 31 담당 agent는 자신의 최신 작업본을 기준으로 catalog·선택·pin을 확인합니다.

### 사용자 요청에 따른 마무리 점검

2026-09-30 최종 변경을 대상으로 설치 코드·시험·LF 규칙, 유지/제외 skill·catalog·현재 문서와 인계의 정합성을 검토했습니다. 추가로 수정할 결함은 발견하지 않았습니다. setup 회귀 10개, skill validator 16개·agent TOML 필수 필드와 ID 10개, catalog 27 ID·31파일의 해시·optional 참조와 실제 payload의 정확한 파일 집합을 확인했습니다. Python compilation·3.9 문법 파싱도 통과했습니다.

변경·신규 Markdown 27개 style·heading·파일 link, diff whitespace 검사와 codex 범위 Gitleaks 탐지 0건을 확인했습니다. 제외 payload 9개와 Kiro 세 원본 bytes는 HEAD와 같으며 Kiro/GPT의 Git 변경 목록은 없습니다. 31 HANDOFF 패치는 apply --check를 다시 통과했습니다. 현재 브랜치는 yunli이며 이 저장소의 stage·commit·push는 하지 않았습니다.

현재 개발·정적·격리 검사의 마무리는 완료했습니다. 실제 Windows OS·PowerShell·개인 runtime·skill 행동·31 최신 작업본의 profile pin/manifest/staging 정합화와 원격 CI는 별도 후속 항목이며 전체 운영 검증 완료로 표시하지 않습니다. CHANGELOG의 초기 9개 시험과 최종 10개 시험을 구분했습니다.


## 9. 2026-09-30 yunli 게시 승인과 절차

사용자가 마무리 검사 이후 “push 까지 진행”을 명시적으로 요청했습니다. 대상은 이 기록까지 포함한 35의 검증한 개인 setup·LF 규칙·skill 정리·Kiro 대조 보완·문서 변경이며 `origin/yunli`에 일반 commit·push합니다. 이번 게시 완료 또는 중단으로 승인 범위가 끝납니다. 이전 root 직접 수정 예외를 재사용하지 않고 실행 계정 소유의 독립 clone에서 게시합니다.

원격 yunli의 시작 commit은 `f884f9acc5ee46bdedbd3a33f1bdff54e2d40852`로 작업본 HEAD와 일치함을 확인했습니다. 기존 저장소의 Git 작성자 설정을 유지하고 변경 파일만 명시적으로 stage합니다. 독립 clone에 옮긴 bytes와 원래 검증 작업본을 대조하고 setup 회귀·diff·비밀정보 검사를 수행한 뒤 commit합니다. 일반 push 성공 이후 원격 SHA와 commit SHA의 일치로 게시를 확인하며 실제 결과는 사용자에게 별도로 보고합니다.

30·31 및 개인 runtime은 변경하지 않으며 main·integration·release·force push·운영 적용·권한 변경은 승인 범위에 없습니다. 공유 원본 작업본의 미commit 변경은 보존합니다. 게시 전 실패하면 독립 clone을 보존하여 재개하며, 게시 후 복구는 이번 commit의 검토된 revert로 수행합니다. §8의 commit/push 미실행 기록은 게시 요청 전 검사 상태입니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
