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

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
