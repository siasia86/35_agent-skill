# Codex 개인 스킬 후속 확인

## 1. 다음 세션에서 이어갈 추가 검토

[세션 인계](../agent-workflows/codex/HANDOFF.md)의 범위·재개 순서·완료 조건을 따릅니다. 아래는 2026-10-02 추가 검토에서 남은 후보이며, 저장소에 보존한 [원시 결과](../agent-workflows/codex/reviews/2026-10-02/findings.json)를 현재 구현과 재대조합니다. 2026-10-03 보완·로컬 검사 완료 항목은 아래에 표시하고 [보완 기록](../agent-workflows/codex/REMEDIATION_2026-10-03.md)에 근거를 남깁니다. 1.0.0 당시의 검증 통과가 이 후보들의 해결을 뜻하지 않습니다.

- [x] 마지막 게시 커밋·미게시 문서 12개·추가 검토 근거·재개 순서를 저장소에 인계하고 AGENTS·README·TODO에서 연결합니다. 검토 JSON 두 개를 bytes 그대로 보존합니다.
- [x] Python 전체 템플릿의 무인수 parser 오류를 원문 보존 대체 블록으로 보완했습니다. 무인수/help/version/잘못된 옵션과 처리 분기를 회귀 검사했습니다.
- [x] Python `_atomic_write`의 POSIX mode·uid·gid 보존 범위를 정하고 대체 블록을 추가했습니다. 기존/새 파일·실패 시 원본 유지·symlink 거부를 검사했고 다른 소유의 실제 파일/ACL/Windows는 범위 밖으로 남깁니다.
- [x] Bash `run_msg_info`를 argv 실행·stderr 로그·실패 상태 반환으로 보완했습니다. 필수 호출부의 후속 차단과 set -e 유무를 회귀 검사했습니다.
- [x] work-rules의 Python flock 예시를 경로를 삭제하지 않는 context manager로 보완했습니다. 같은 inode의 waiter와 새 프로세스 배제·예외 해제를 검사했습니다. kiro-lock helper는 변경하지 않았습니다.
- [x] 중첩 펜스 뒤 링크 누락을 실행용 검사기 7개에 보완했습니다. 중첩/tilde/닫는 태그/들여쓰기·미닫힘 종료 2·기존 제외를 단독 사본에서 검사했습니다.
- [x] shipping-checklist의 code-review와 네 STYLE 역할의 readme-template·필요한 md-link-check를 전체 지침/원문으로 동봉했습니다. governance 템플릿은 대상 저장소의 조건부 자료로 구분했고 단독 폴더 참조를 검사했습니다.
- [ ] md-link-check·using-skills·zircon-readme-policy의 최종본 독립 사례를 확인합니다. 2026-10-03 기록된 검사 시점 해시와 현재 해시의 차이 및 후속 보고 부재를 확인했습니다. readme-template도 해시 차이가 있지만 후속 보고가 있으므로 같은 미검증 상태로 단정하지 않고 후속 입력 근거를 대조합니다. 독립 사례를 다시 수행한다면 현재 사용자 요청·모델·협업 도구 조건을 확인합니다.
- [x] 확정한 로컬 항목의 호환 규칙·예시·동반 자료를 보완하고 원문 대응·회귀·기본 검사를 완료했습니다. MIGRATION·VERIFICATION·TODO·CHANGELOG·인계를 갱신했습니다. 최종본 독립 모델 사례는 별도 미완료로 유지합니다.
- [x] 2026-10-02 미게시 문서 12개와 인계·병합 검토 자료를 구분해 검토한 뒤, 2026-10-03 사용자 요청 범위에서 yunli에 게시했습니다. `525f0e0`의 일반 push와 원격 SHA 일치, main·design 유지를 확인했습니다. 확인 결과를 담은 후속 문서 커밋은 같은 yunli에 게시합니다.
- [x] 2026-10-03 main·yunli·design 전체 원격 브랜치의 선후 관계와 격리 병합을 검토했습니다. 충돌·고유 커밋 유실은 없으며, 확인한 동작 결함과 판정 범위는 [병합 검토](../agent-workflows/codex/MERGE_REVIEW_2026-10-03.md)에 기록합니다. 실제 main·design 게시와 구현 보완은 완료 처리하지 않습니다.
- [x] 후속 사용자 요청의 원격 main·yunli와 로컬 main·yunli 네 브랜치를 `36cd9d3`으로 실제 통합하고 원격 SHA·로컬/추적 refs·clean 상태·파일 보존을 확인했습니다. 기본 스킬 검사도 통과했습니다. 확인 결과를 담은 후속 기록 커밋 역시 네 브랜치로 fast-forward하며 최종 SHA는 Git refs에서 확인합니다. [실제 병합 기록](../agent-workflows/codex/MERGE_REVIEW_2026-10-03.md#7-네-브랜치의-실제-병합)을 따르고 기존 스킬 문제의 보완은 미완료로 유지합니다.

- [ ] 2026-10-03 후속 사용자 요청의 보완 변경 yunli 게시와 main 병합을 수행하고 실제 원격·로컬 refs를 확인합니다. 승인 범위와 보존 절차는 [보완 기록](../agent-workflows/codex/REMEDIATION_2026-10-03.md#6-보완-변경-게시와-main-병합-승인)에 남깁니다.

## 2. 실제 사용자 환경

- [ ] 사용자가 고른 스킬을 기존 개인 편집과 비교·백업한 뒤 실제 홈에 복사하고 새 Codex 세션에서 발견·명시 호출·자동 선택을 확인합니다. 이번 작업은 저장소 작성과 격리 복사 검증입니다.
- [ ] 사용자가 지정한 여러 작업공간에서 개인 홈 공통 스킬과 저장소별 스킬의 설치 범위·동명 중복·적용 지침·31 설정 적용 여부를 확인하고, 설치 기록 참조와 발견·대표 행동 결과를 각각 남깁니다. 문서의 `repository1`·`qa-repostory2`는 설명용 예시이며 실제 적용 결과가 아닙니다.
- [ ] 실제 Windows에서 폴더 복사·Python 3.11 실행·PowerShell·Git worktree·잠금 파일을 확인합니다. Linux 결과로 Windows 동작을 완료 처리하지 않습니다.
- [ ] Terraform·Ansible·AWS·Docker·서비스 복구는 승인된 실제 환경에서 검증합니다. 계획/리뷰의 Luna 사례 결과와 운영 결과를 구분합니다.

## 3. 원문 도구와 잠금

- [ ] security-tools의 원래 마스킹/scanner/config가 필요하면 사용자 제공 원본·map fixture·정규식 명세를 확인하고 동일 인터페이스와 복원 호환성을 검사합니다. 현재 스킬의 설계·수동 점검과 기존 실행 도구의 배포를 구분합니다.
- [ ] 잠금은 참여 agent가 같은 프로토콜을 지킬 때 사용합니다. helper가 종료되기 전에 죽으면 `.kiro-lock.guard`가 남을 수 있습니다. 소유·실제 프로세스·사용자 승인 확인 후 복구하고 시간 경과만으로 삭제하지 않습니다.
- [ ] 잠금 API를 따르지 않는 외부 writer·네트워크 파일시스템·Windows 파일 잠금의 보장은 별도 확인합니다. 현재 helper의 gate·O_EXCL 검증을 임의 writer 전체의 격리 보장으로 확대하지 않습니다.

## 4. 별도 사용자 검토

- [ ] Kiro prompt 16개의 별도 Codex 스킬 추가 필요성을 사용자 작업 예시로 검토합니다. 현재 19개 스킬에서 필수 호출하는 prompt는 없으며 prompt 원문은 kiro에 유지합니다.
- [ ] 폐기본에만 있던 ansible-review·fact-check·markdown-review·git-release·security-audit의 추가 필요성을 별도로 검토합니다. 자동 추가·삭제하지 않습니다.
- [ ] 내용 축약·스킬 통합·중복 제거·본문 분할은 사용자가 별도로 선택한 후속 작업에서 검토합니다. 이번 모음은 원문 분량을 유지합니다.

현재 완료 상태와 실제 근거는 [VERIFICATION](VERIFICATION.md), 원문 대응과 변경 이유는 [MIGRATION](MIGRATION.md)에 기록합니다.

---

**작성일**: 2026-10-01

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
