# Codex governance 개선 작업 기록

## 1. 요청과 작업 경계

CG-20260929: 최신 Kiro 세 skill의 접근을 재확인하고 개인 Codex 자산 및 중앙 공통·저장소별 skill 구성을 개선하는 요청입니다. 35는 구현, 31은 정책·선택, 30은 생성·검증을 소유합니다. 과거 root 작업본 직접 수정 예외를 재사용하지 않고 계정 소유 독립 작업본에서 개발했습니다. 검증한 패치의 이번 1회 반영 승인에 따라 원래 30·31·35 작업본에 통합했습니다.

Kiro/GPT 원본과 기존 사용자 변경, 개인 runtime, 기존 release와 consumer 형식을 보존합니다. 개인 설치·운영 적용·release·OS 권한 변경은 제외합니다. 사용자 후속 승인에 따라 이번 개발 변경의 yunli commit·일반 push를 진행합니다. 이 기록은 실행 중에 작성했으며 작업 전 작성된 계획으로 소급 주장하지 않습니다.

## 2. 구현과 관찰

- 35 보존 skill 25개·agent 10개를 자동 발견 위치에서 archive로 이동하고 보존 원문 bytes를 확인했습니다. 독립 검토에서 이동 후 skill 간 상대 링크 세 곳을 발견하여 열람본의 경로만 수정하고 해당 원문도 함께 보관합니다. 최초 baseline은 보존하고 경로 대응표를 추가했습니다.
- 단계 수·고정 배치 강제, 전역 Markdown 양식, Python 개인 양식·로컬 build 재승인 문구를 적용 범위와 현재 승인 기준에 맞췄습니다. 기존 catalog ID 36개·payload 37개는 유지했습니다.
- 재사용 진입점 네 template와 31의 공통·30/31/35별 정책·profile, 31 루트 AGENTS bootstrap을 추가했습니다. 두 skill 역할은 governance-default·governance-repository입니다.
- 30의 별도 닫힌 draft 도구는 31 staging에만 파일 일곱 개를 생성·검사합니다. existing AGENTS의 병합·managed 파일 차이 검토가 필요하며 후보 생성으로 덮어쓰지 않습니다.
- 최초 검사는 source template의 미생성 참조와 보존 STYLE·INDEX의 예시·푸터 문제를 검출했습니다. 독립 검토는 이동 링크·필수 정책 중단 조건·31 문서 읽기·생성기 해시·기존 instruction 경로 충돌을 발견했습니다. 마지막 충돌은 기존 선택 plan과 새 후보 target을 대조해 거부하는 guard 및 호환 선택 예시로 보완합니다. 명시적인 skill-relative 경로, 예시 정합성·푸터를 수정하고 모든 입력 pin을 갱신했습니다.
- 홈 clone의 로컬 upload-pack 소유권 검사가 실패했습니다. 전역 Git 설정·OS 권한을 변경하지 않고 읽기 전용 Git bundle로 독립 작업본을 만들었습니다. clone에는 기존 root 작업본의 미커밋 Kiro 변경이 포함되지 않습니다.

## 3. 검증과 남은 항목

검증 상세는 [검증 기록](CODEX_GOVERNANCE_VERIFICATION.md)에 남깁니다. 이식 원본 세 파일은 OS 읽기 거부로 전체 내용 대조가 미완료입니다. 격리 후보의 정적·생성 검증을 실제 runtime 발견·정책 자동 로딩·hook·위임 동작으로 확대하지 않습니다.

root 작업본 통합은 현재 작업의 명시적 1회 승인으로 완료했습니다. yunli 게시까지 승인 범위를 연장했으며 완료·중단 시 예외는 만료됩니다. 미게시 변경은 해당 diff만 되돌릴 수 있고 기존 root 작업본·사용자 변경·release는 유지합니다. 게시 후 복구는 검토된 revert를 사용합니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
