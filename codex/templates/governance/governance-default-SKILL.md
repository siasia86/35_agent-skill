---
name: governance-default
description: Apply the configured common governance workflow to engineering changes and work records when the user or repository selects the central governance profile.
---

# 공통 governance 절차

이 skill 폴더를 기준으로 `references/default-policy.md`의 공통 정책을 읽습니다. 고정 SHA-256은 `{{DEFAULT_POLICY_SHA256}}`입니다. 적용 AGENTS가 이 세션에서 같은 정책·해시를 이미 읽고 확인했다면 중복 로딩하지 않습니다.

요청 범위·변경 위험·의존성을 확인하고 정책에 맞는 기록과 검증을 선택합니다. 승인된 작업을 진행하며 실제 관찰과 미확인을 구분합니다. 저장소별 설정은 해당 저장소의 governance-repository 참조를 확인합니다. 이 skill은 전문 개발·검토 절차를 전부 로딩하는 진입점이 아닙니다.

필수 참조를 읽을 수 없거나 고정 해시가 맞지 않으면 원인을 보고하고 해당 정책이 필요한 수정·완료 판정을 해결 전까지 중단합니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
