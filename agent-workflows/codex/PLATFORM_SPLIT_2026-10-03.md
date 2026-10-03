# Codex Windows Linux 플랫폼 분리 기록

## 1. 목적과 허용 범위

사용자 요청으로 기존 `codex/`를 같은 깊이의 `codex_linux/`로 이동하고 `codex_windows/`에는 계획과 문서 골격만 준비합니다. Windows 전용 재작성은 [PLAN](windows/PLAN.md)과 [TODO](windows/TODO.md)에서 이어갑니다.

현재 작업은 경로 분리·현행 안내 연결·개발 검증 경로 정합화입니다. Windows skill 생성·Linux skill 본문 재작성·개인 홈 설치·설정·WSL 설치·운영 적용·release는 실행하지 않습니다. 저장소 VERSION 1.0.0은 유지합니다.

## 2. 새 구조와 작업 순서

- [codex_linux](../../codex_linux/README.md): 기존 개인 skill 19개·동반 도구·참조·개인 지침 예시·검증 자료.
- [codex_windows](../../codex_windows/README.md): Windows 계획·TODO·ISSUE·REVIEW와 skills·verification·personal 안내 골격. 설치 가능한 SKILL.md는 아직 없습니다.
- `agent-workflows/codex/`: 기존 적용 관찰·검증·인계의 기록 위치를 유지합니다.

Windows와 Linux의 현행 계획·검증은 플랫폼별로 관리합니다. 검증한 변경을 yunli에 commit·일반 push한 뒤 사용자 검증을 기다립니다. 사용자가 검증하기 전에는 main에 반영하지 않으며, 사용자 검증 완료 후에만 main 반영·일반 push를 진행합니다. 새 세션은 실제 Git 상태·현재 PLAN/TODO와 이 범위를 먼저 확인합니다.

## 3. 과거 검증 경로의 대응

과거 JSON의 `codex/` 입력 경로·SHA-256·원시 명령·관찰 시점은 그대로 보존합니다. 해당 입력을 현재 파일과 대조할 때 경로의 첫 `codex/`만 `codex_linux/`로 해석합니다. 해시 값은 변경하지 않습니다. 이 대응은 새 검증 통과나 설치·Windows 동작 완료를 뜻하지 않습니다.

기존 개발 검증기 두 파일의 `codex/skills` 고정 경로만 새 Linux 경로로 갱신합니다. `ROOT`의 부모 깊이는 유지합니다. workflow의 과거 reviews 재현기·검증기는 당시 입력과 실행 조건을 보존하며 현재 검사기로 자동 사용하지 않습니다.

## 4. 보존 범위

Linux의 `skills/`·`personal/`·`verification/*.json` bytes, Kiro·GPT·105_backup 원본, 저장소 `.codex/` 설정, 과거 개인 설치 관찰 사본과 inventory, workflow reviews 전체를 보존합니다. 기존 skill 내부의 상대 링크·참조·동봉 구조를 유지합니다. 과거 실행 사실·코드블록·SHA·승인 기록을 새 작업의 근거로 다시 쓰지 않습니다.

공개 기록에는 개인 절대 경로·계정·config 원문·자격증명·로컬 raw evidence를 복사하지 않습니다. 기존 기록 JSON을 새 결과로 덮어쓰지 않고 현재 검증·미실행 결과는 별도로 남깁니다.

## 5. 검증과 복구

이동 전 추적 파일 499개의 해시와 변경 파일 사본을 비공개 로컬 evidence에 보관했습니다. 기존 codex의 추적 파일 191개를 이동했고 문서·검증 경로를 수정한 16개 외 483개의 bytes가 같습니다. Linux skill 자료 182개·개인 지침 1개·검증 JSON 2개와 보호 영역 269개는 모두 일치하며 누락은 없습니다. 과거 회귀 입력 80개도 첫 경로 대응 후 해시가 모두 같습니다.

- **통과:** 변경 Markdown 22개의 style·헤딩·파일 링크 검사에 오류가 없습니다. 새 Windows 문서는 8개 모두 Markdown이며 SKILL.md·실행 코드·config는 없습니다.
- **통과:** 독립 검사에서 전체 대상 Markdown 192개·교차 앵커 116개를 확인했습니다. 새 깨진 파일 링크·앵커 오류·미완료 펜스는 0건입니다.
- **기존 문제 보존:** testing-guide·using-skills의 비교 원문 edge_case_testing.md에 있던 파일 링크 2건은 기준선과 같으며 원문 bytes를 보존했습니다.
- **통과:** 개발 검증기 두 파일의 구문을 확인했습니다. 변경은 skills 고정 경로 3곳이며 ROOT 부모 깊이는 유지합니다.
- **검사 범위:** UTF-8을 명시한 Windows 실행을 사용했습니다. 대표 Windows fixture 검사는 [Windows REVIEW](windows/REVIEW.md)에 별도로 기록하며 전체 skill 행동의 검증으로 확대하지 않습니다.
- **미실행:** 이번 이동 후 전체 Linux POSIX 회귀 실행·Windows 전용 구현·최종 모델 행동·개인 설치·Codex 발견·운영 적용은 수행하지 않았습니다. Gitleaks가 설치돼 있지 않아 자동 비밀정보 검사는 미실행이며 신규 문서와 추가 diff에서 개인 경로·자격증명 패턴을 제한적으로 확인합니다.

실패하면 추가 적용을 중단하고 이번 diff와 로컬 사본을 검토합니다. 이번 변경만 복구하며 기존 변경·Git 이력·개인 설정·설치 사본을 전체 reset하거나 일괄 교체하지 않습니다. 게시 후 복구는 검토한 revert로 수행합니다.

## 6. 게시와 사용자 검증 상태

플랫폼 분리·원문 보존·문서·개발 검증 경로 검사를 완료했습니다. 이번 변경의 게시 대상은 yunli이며 일반 commit·push 후 실제 origin/yunli와 최종 커밋의 일치를 확인합니다. 최종 SHA는 자기 참조하지 않고 Git refs와 사용자 보고에서 확인합니다.

사용자 검증·main 반영·push는 미실행입니다. 현재 main의 기준은 분리 전 13c44699cf2a431da59a470106212442901bf025이며 사용자 검증 완료 후 검증한 변경을 반영·push합니다. VERSION 1.0.0, 개인 설정·설치·운영 적용 상태는 유지합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
