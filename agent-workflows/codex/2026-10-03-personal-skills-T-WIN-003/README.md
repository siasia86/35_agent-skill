# T-WIN-003 개인 Codex skill 업데이트 백업

## 1. 범위와 원본

입력은 `yunli@16817d7`입니다. 기존 개인 skill의 동명 Windows 사용본을 보완하고 `git-commit-rule`, `planning-and-breakdown` 두 skill을 추가합니다. 별도 `markdown-review`는 보존합니다. 35 내부 원본은 `_reference`에서 출처로 연결하며 중복 clone하지 않습니다. 관리 원본은 [Windows 배포](../../../codex_windows/README.md)에 둡니다.

사용자 지정에 따라 이번 업데이트는 `agent-workflows/codex/` 바로 아래 이 폴더 하나에서 전후 사본·설치·검증·복구를 관리합니다. 다음 업데이트는 날짜·목적·작업ID가 다른 새 폴더를 추가합니다. 기존 관찰 사본·JSON·Linux/Kiro 원문을 덮어쓰지 않습니다.

## 2. 폴더와 기록

```text
<업데이트 폴더>/
├── README.md                   # 범위·설치 결과·검증·복구
├── USE.md                      # 두 skill 호출·실제 적용 방법
├── before/inventory.json       # 이전 5개·상대 파일 해시
├── after/inventory.json        # 적용 후 7개·출처·상대 파일 해시
├── validation.json             # 공개 가능한 실제 검사 근거
├── before/skill-files/<이름>/   # 변경 전 skill 전체 사본
├── after/skill-files/<이름>/    # 변경 후 skill 전체 사본
├── AUDIT.md                    # 후속 검토·보완·미검증
└── private/                    # Git 제외: AGENTS/config 전후 원문·raw
```

- [사용 방법](USE.md)
- [이전 inventory](before/inventory.json), [적용 후 inventory](after/inventory.json)
- [검증 근거](validation.json)
- [공개 skill 이전 사본](before/skill-files/), [적용 후 사본](after/skill-files/)

보관 폴더는 `.agents/skills` 설치 경로가 아니며 현재 source나 자동 발견 목록으로 사용하지 않습니다. 실제 개인 AGENTS·config·개인 경로가 있는 로그는 private/에서 보존하고 Git 제외를 확인합니다. 전체 홈·인증·키·세션의 별도 파일은 수집하지 않습니다. 설정 원문에 포함된 개인 경로·민감 항목은 private/의 Git 제외를 적용합니다. 공개 skill 사본에는 출처와 전체 파일 해시를 기록하고 개인정보 검사를 통과한 자료만 게시합니다.

## 3. 설치와 검증

<!-- VALIDATION-BEGIN -->
실제 개인 skill은 이전 5개·39파일에서 7개·90파일로 적용했습니다. 기존 `code-review`, `debugging-and-recovery`, `md-link-check`, `work-rules` 4개를 갱신했고 두 요청 skill을 추가했습니다. 별도 `markdown-review`의 본문은 그대로 보존했습니다. 동명 이전 폴더는 활성 발견 경로에서 분리해 백업했습니다.

- 전체 runtime 파일과 after 사본·inventory 해시를 대조했습니다. 일반 실행으로 7개·90파일을 모두 읽었으며 접근 거부·해시 차이는 0건입니다.
- `markdown-review`의 기존 읽기 거부는 ACL을 private에 먼저 기록하고 작업 계정의 읽기·탐색만 추가해 해결했습니다. 다른 기존 ACL·소유권과 실행 정책은 보존했습니다.
- 개인 AGENTS의 기존 bytes를 유지한 채 선택 skill·전후 보관·세션 담당 파일 규칙 네 항목을 추가했습니다. config와 system 49파일은 기존 해시와 같으며 plugin·모델 설정은 바꾸지 않았습니다.
- Markdown·헤딩·파일 링크·교차 문서 fragment·공식 skill metadata·원문 보존 검사를 통과했습니다. 상세 범위는 [validation](validation.json)에 둡니다. snapshot은 Git 줄바꿈 변환을 끄고 원형 파일 해시를 보존합니다.
- 새 세션의 skill 자동 발견·선택·대표 행동과 모든 helper 실행은 미검증입니다. 동봉 link checker의 0개 대상은 exit 2로 보완했고 경계·회귀 10건을 통과했습니다. `work-rules`는 925줄·60,866바이트에서 53줄·7,682바이트로 줄였으며 Windows 상세·보존 본문은 references에 전체 보존했습니다.

[전달받은 검토 사항의 후속 대조](AUDIT.md)에서 읽기 권한·문서 크기·중앙 후보와 현장 상태·config와 세션 권한을 구분했습니다.
<!-- VALIDATION-END -->

Windows 관리 원본의 폴더 전체를 지원 개인 설치 위치에 적용하며 성공한 동명 교체의 이전본만 활성 경로에서 제거합니다. `markdown-review`, 내장 system·plugin·config·모델 설정은 보존합니다. 설치 파일 일치를 새 세션 자동 선택이나 전체 helper 실행 통과로 확대하지 않습니다.

## 4. 평가·복구·후속

잘된 점은 업데이트 하나의 전후 skill·설정·검증·복구 기록을 한 폴더에서 찾을 수 있다는 점입니다. 비용은 사본 저장량과 공개 자료·비공개 설정의 Git 제외를 계속 확인해야 하는 점입니다.

복구는 `before/inventory.json`과 before의 전체 폴더를 대조해 이번에 바꾼 동명 대상만 되돌립니다. 신규 설치는 이번 생성 대상인지 확인한 뒤 정리하고 보존한 다른 skill·사용자 변경을 덮어쓰지 않습니다. 개인 AGENTS는 백업한 원문과 이번 추가 절만 비교합니다. 설정 config는 바꾸지 않습니다. 게시 후 구현 복구는 검토한 revert를 따릅니다.

현재 사용자 검증·main 후속 행동은 [Windows TODO](../windows/TODO.md) 한 곳에서 관리합니다. Git 게시 순서는 yunli → 사용자 검증 → main입니다. 과거 업데이트 폴더는 수정하지 않고 다음 갱신은 새 이름으로 보존합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
