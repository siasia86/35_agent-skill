# Batch 4 중앙 profile 연동 구현 기록

## 1. 작업 위치와 기준

2026-09-22 사용자 요청으로 31 계약 초안과 30 읽기 전용 planner를 실제 구현했습니다. 31 정책상 root mirror를 수정하지 않고 실행 계정 소유 clone을 준비했습니다. root의 30·31 작업 트리는 변경하지 않았습니다.

- 31 작업 clone: /home/siasia/workspaces/31_governances, siasia 브랜치, 기준 e77ca5b85057d8fb2e188ba197a30bae66b7f750.
- 30 작업 clone: /home/siasia/workspaces/30_sia-scripts, siasia 브랜치, 기준 6f29a8a6166b7b9b0891e89a1b0c6846d643f225.
- 35 개발 작업: 기존 미커밋 payload·문서 변경을 보존했습니다.
- 계정 브랜치는 앞서 조사한 root mirror와 commit이 다릅니다. 30 계정 브랜치에는 기존 governance_sync 모듈이 없으므로 이번 28개 테스트는 최신 sync와 통합된 회귀 시험이 아닙니다. 계정 브랜치 통합·CI는 후속 작업입니다.

홈 clone 생성·문서·코드 편집은 승인 절차로 수행했습니다. root ACL·소유권 변경, release 승인, commit·push는 하지 않았습니다.

## 2. 변경 파일과 역할

- 31: .governance/repository/central_configuration_contract.md, .governance/profiles/ai_document_review.draft.json, sync_policy.md의 전환 안내, PLAN·TODO·CHANGELOG.
- 30: src/governance_profile.py, tests/test_governance_profile.py, docs/governance_profile.md, PLAN·CHANGELOG.
- Terra(ID 01a0c6c1-bf48-7683-85da-7ccff8dd0715)는 30 구현·테스트만 담당했고 주 agent는 문서·계약·통합 검증을 담당했습니다. Sol(ID 01a0c6c1-6908-7063-b69f-287be00b740e)은 계약을 읽기 전용 검토했습니다.
- 주 agent 검토로 잘못된 자료형, bool과 숫자 구분, 디렉토리 읽기 실패, payload_root의 중간 symlink, 필수 동반 파일 누락 계획을 보완했습니다.
- Sol 의견으로 기존 v1 소유권 설명의 범위를 명시하고 활성화가 검증된 staging ID·파일 집합 해시와 결합되어야 한다는 후속 조건을 추가했습니다.

## 3. 실제 검증

30 clone 루트에서 다음을 실행했습니다.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests -v
```

총 28개 통과이며 그중 신규 planner 12개입니다. 테스트의 의도적인 오류 fixture 출력은 기대한 거부 결과입니다. 최초에 다른 작업 디렉토리에서 신규 테스트를 실행했을 때 src import가 실패했고, 문서의 실행 위치인 30 루트에서 재실행해 통과했습니다.

실제 profile 연동 명령:

```bash
python3 -B /home/siasia/workspaces/30_sia-scripts/src/governance_profile.py \
  --profile /home/siasia/workspaces/31_governances/.governance/profiles/ai_document_review.draft.json \
  --catalog /root/35_agent-skill/codex/ASSET_CATALOG.json
```

- 종료 0, 자산 5개, ID 정렬, warnings 빈 목록, deployable false, record_storage_decision pending.
- 같은 입력으로 두 번 실행해 표준 출력이 같고 profile·catalog·payload의 전후 해시가 같음을 확인했습니다.
- 출력 SHA-256: 2cb6366f2fef8323ce072b8862e99f6c8c1734ff25b0b807fa51850a3fb22e26. 출력 해시는 재현 증거이며 배포 승인 서명이 아닙니다.
- 신규 Python 두 파일은 bytecode를 쓰지 않는 compile 검사 통과입니다.
- 31 기존 manifest는 root mirror의 governance_sync check로 45개 draft 항목 검사를 통과했습니다. draft의 해시 일치 강제는 유보되며 새 profile은 기존 manifest의 승인 대상으로 추가되지 않았습니다.
- 30·31 clone의 Gitleaks 검사에서 탐지 0건, 추적 diff 공백 검사 통과입니다. 변경 문서는 Markdown 스타일·헤딩·링크를 검사했습니다.

## 4. 지원 범위와 남은 작업

planner는 자체 완결형 자산의 선택·파일 해시·상대 경로·중복·대상 충돌을 읽기 전용으로 검사합니다. 필수 동반 파일이 있으면 지원하지 않는 입력으로 거부하고 선택적 skill 누락은 경고합니다. unknown profile 필드는 무시하지 않고 거부합니다.

- 미지원: 실제 대상 쓰기·설치·override·관리 구간 병합·예외 및 명령 합성·승인 release 생성·runtime 활성화·rollback.
- 미검증: CI·release artifact, 최신 sync 브랜치와 통합 회귀, 운영 consumer·개인 설치·hook·이전 버전 복귀.
- 미결정: 운영 상태·검증 기록·snapshot의 최종 보관 위치. 기존 자료·경로를 유지했습니다.
- 다음 단계: 계정 브랜치와 통합 기준의 차이를 검토한 뒤 대상별 설정 합성·불변 출처 고정과 staging 준비를 연결합니다. 운영 적용 전 기존 예외 이관·권한·실패 복구 gate를 충족해야 합니다.

이번 코드와 계약은 세 저장소를 연결하는 첫 읽기 전용 단계입니다. 전체 중앙 관리 배포가 완료된 것은 아닙니다.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
