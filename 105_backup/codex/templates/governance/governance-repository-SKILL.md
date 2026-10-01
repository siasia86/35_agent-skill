---
name: governance-repository
description: Apply the centrally selected repository governance workflow for {{REPOSITORY_NAME}}, including ownership, work records, and verification commands.
---

# {{REPOSITORY_NAME}} governance 절차

이 skill 폴더를 기준으로 `references/default-policy.md`의 공통 정책과 `references/repository-policy.md`의 저장소 정책을 읽습니다. 공통 정책의 SHA-256은 `{{DEFAULT_POLICY_SHA256}}`이고 저장소 정책의 SHA-256은 `{{REPOSITORY_POLICY_SHA256}}`입니다. 적용 AGENTS가 이 세션에서 같은 정책·해시를 이미 읽고 확인했다면 중복 로딩하지 않습니다.

저장소 정책의 수정 범위·기록 위치·검증 기준을 현재 요청에 적용합니다. 기존 사용자 변경과 비관리 파일을 보존합니다. 정책에 없는 명령·예외·운영 권한을 추정하지 않습니다. 필요한 전문 skill을 작업별로 선택하며 중앙 원본의 변경을 현장 파일에 자동 역동기화하지 않습니다.

필수 참조를 읽을 수 없거나 고정 해시가 맞지 않으면 원인을 보고하고 해당 정책이 필요한 수정·완료 판정을 해결 전까지 중단합니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
