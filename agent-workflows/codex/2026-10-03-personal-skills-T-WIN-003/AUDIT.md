# T-WIN-003 후속 검토 대조

## 1. 개인 skill와 권한

기존 소형 skill 네 개는 일반 읽기가 거부됐지만 승인된 읽기는 성공했습니다. 이번 전체 폴더 적용 후 관리 대상 6개·87파일은 일반 읽기를 통과했고 보존한 `markdown-review` 한 파일에 기존 거부가 남았습니다. 해당 폴더·파일의 ACL을 private에 보존한 뒤 작업 계정에 읽기·탐색만 추가했습니다. 최종 일반 실행은 7개·90파일 모두 읽기와 inventory 해시 일치에 성공했습니다. 별도 skill 본문·소유권·전역 ACL·실행 정책은 변경하지 않았습니다.

`work-rules/SKILL.md`는 925줄·60,866바이트에서 최종 53줄·7,682바이트로 분리했습니다. Windows 상세는 `references/windows-work-rules-details.md`, 블록 밖 보존 본문은 `references/legacy-work-rules.md`에 두고 전체 해시를 대조했습니다. 필요한 때만 참조를 읽으며 두 동봉 mirror도 같은 구조와 각자의 올바른 work-rules 원문 링크를 사용합니다. 공식 [skill 안내](https://learn.chatgpt.com/docs/build-skills)는 목록 metadata와 선택 시 본문 읽기를 구분합니다.

## 2. 중앙 후보와 현장

중앙 registry의 등록 대상은 9개이며 현재 문서에 모두 미적용으로 명시되어 있습니다. 실제 상위 작업 공간과 아래 Git 루트를 읽기 전용으로 확인했고 등록 상대 경로와 모두 일치했습니다. status 항목 수는 조회 시점의 tracked·untracked 변경 수이며 작업량이나 완료 상태가 아닙니다.

| Repo ID | Root AGENTS.md | Root override | Status 항목 수 |
|---------|----------------|---------------|----------------|
| 11      | 없음           | 없음          | 4              |
| 12      | 없음           | 없음          | 1              |
| 21      | 없음           | 없음          | 4              |
| 22      | 없음           | 없음          | 1              |
| 31      | 없음           | 없음          | 5              |
| 32      | 없음           | 없음          | 2              |
| 91      | 있음           | 없음          | 13             |
| 98      | 있음           | 없음          | 61             |
| 99      | 있음           | 없음          | 0              |

11·12·21·22·31·32의 root 지침 부재는 확인했지만 하위 지침·runtime 적용을 대신 판정하지 않았습니다. 91·98·99의 기존 본문은 이 조회에서 수정·병합하지 않았습니다. QA의 역할·검증·DB 경계를 먼저 비교하는 pilot이 타당하며 실제 적용은 이번 35 작업 범위 밖입니다. 중앙의 네 skill 안내와 기존 runtime_inventory는 이전 관찰입니다. 현재 7개 현황은 이번 after/inventory.json 한 원본에 두며 중앙은 최신 기록으로 연결하는 별도 검증 변경을 진행합니다. 게임 repo의 사용자 변경·index·refs는 보존합니다.

## 3. config와 실제 세션

기존 config의 두 값은 `approval_policy = "never"`, `sandbox_mode = "danger-full-access"`입니다. 이번 실제 도구 세션은 `workspace-write`와 제한된 쓰기·네트워크, `auto_review`를 사용합니다. 파일 기본값을 실제 세션의 무제한 권한으로 보고하지 않으며 config 값은 그대로 유지했습니다. 사용자의 전체 허용 의향은 반복 확인 없이 유지하되 실제 세션 변경은 앱 입력창 아래 permission control에서 Full access를 선택하는 방식입니다. 현재 agent 도구에는 이 메뉴를 변경하는 API가 없어 변경 완료로 보고하지 않습니다. 관리 요구사항은 기본값보다 우선합니다. [공식 Sandbox 안내](https://learn.chatgpt.com/docs/sandboxing), [설정 우선순위](https://learn.chatgpt.com/docs/config-file/config-basic).

AGENTS는 공식 [탐색 규칙](https://learn.chatgpt.com/docs/agent-configuration/agents-md)에 따라 root에서 실제 작업 CWD까지 적용됩니다. 여러 repo를 포함한 상위 폴더에서 모든 하위 AGENTS가 자동 로드된다고 가정하지 않습니다. 파일 존재·중앙 후보 조회·현재 지침 전달·새 세션 적용을 별개로 기록합니다.

## 4. 세션 충돌과 평가

work-rules·배포 AGENTS·개인 AGENTS에 작업ID·담당 파일·예정 commit 파일 목록을 먼저 명시하고 검토한 파일만 staging하는 규칙을 추가했습니다. 이번 담당은 T-WIN-003의 Windows 실행 규칙, 출처 연결, 업데이트 폴더, 개발 기록 경로, 실제 개인 skill과 공통 AGENTS 추가절입니다. 기존 Linux/Kiro·과거 백업·관찰 JSON·다른 repo 변경은 담당 commit에서 제외합니다.

잘된 점은 읽기 실패를 실제 일반 실행으로 재현·해결했고 설치·발견·세션 권한을 나눠 기록한 점입니다. 남은 항목은 새 세션의 두 skill 발견·행동 미검증과 중앙 후보의 미적용 상태입니다. 후속 상태는 [Windows TODO](../windows/TODO.md)에서 관리합니다.


## 5. 검사기 0개 대상과 선택

구형 동봉 link checker는 빈 디렉터리에 exit 0을 반환하는 것을 재현했습니다. Windows 활성 사본 7개를 같은 bytes로 보완했고 보존 Linux 사본 7개는 그대로 유지했습니다. 대상 0개는 빈·비Markdown·제외만·미존재만 입력을 포함해 exit 2와 검사 미완료 메시지를 반환합니다. 검사할 파일이 있으면 valid=0, broken·읽기 실패·유효 파일과 혼합된 미존재 입력=1, 미닫힘 fence=2입니다. 경계·회귀 검사 10건을 통과했으며 실제 실행은 대표 helper, 나머지 6개는 바이트 동일성으로 확인했습니다.

저장소 지정 도구·버전·설정을 우선하고 지정이 없을 때 동봉 도구를 fallback으로 선택합니다. 선택 이유·경로·실제 검사 수·exit 상태를 기록하며 다른 checker 성공으로 필수 repo gate를 대체하지 않습니다. 이 기준은 핵심 work-rules와 관련 Windows 본문·동봉 대응 20곳에 반영했습니다. 중복 전달된 동일 검토는 이 항목에서 한 번만 관리합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
