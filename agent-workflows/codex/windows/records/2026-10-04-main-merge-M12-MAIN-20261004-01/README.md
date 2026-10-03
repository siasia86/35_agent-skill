# M12 전체 main 병합 검토

## 1. 범위와 승인

2026-10-04 사용자가 12_github의 전체 저장소를 검토하고 main에 병합하도록 명시했습니다. 이번 요청으로 35의 현재 yunli와 완료된 SMA 기록 이관·현장 관리 문서를 독립 작업본에서 검토합니다. 기존 main과 design의 모든 commit은 yunli에 포함됩니다. 개인 홈 설치·자동 선택·19개 skill의 사용자 대표 행동을 완료한 것으로 간주하지 않습니다.

## 2. 확인한 문제와 보완

- 최초 이관 verify_skills는 T-WIN-004의 STYLE 원문 7개 이동·개인 AGENTS 이동·본문 개정 이전 계약입니다. 원문 manifest·과거 검사기는 보존하고 verify_current를 추가해 실제 368개 해시, 19개 skill, 배포 참조·독립 helper·설정 예제를 검사합니다.
- byte-lock 예제는 work-rules의 조건별 참조로 옮겨졌으므로 test_patterns에 명시적 문서 입력을 추가했습니다. 실제 예제의 경쟁·정상·예외 해제를 재검사합니다.
- link 검사 대상 0개는 현재 구현상 미완료 exit 2입니다. 오래된 test_markdown 기대값만 1에서 2로 갱신했습니다. skill helper 구현은 변경하지 않습니다.
- 공유 config 예제의 source .codex/config.toml은 Windows 자동 CRLF 변환으로 원문 해시가 달라졌습니다. 해당 한 파일의 LF attribute를 명시하며 설정 값은 보존합니다.

## 3. 검증과 제한

현재 원문 해시 368건·skill 19개·배포 로컬 참조 77개·Python 구문 34개·독립 helper 27회가 통과했습니다. 공식 quick_validate 19개는 기존 격리 PyYAML을 사용했으며 새 설치는 없습니다. Markdown 회귀 80개·Python/Bash 회귀 108개·byte-lock 7개가 통과했습니다. Snapshot 도구의 합성 입력 성공·정확한 bytes·manifest·기존 phase 거부·private 제외 필수·누락 거부·원문 보존 7건과 새 검증기의 원문 변조·현재 AGENTS 누락 실패 2건을 통과했습니다.

이번 수정 문서의 style·heading·파일 링크·교차 fragment와 staged diff·staged/outgoing/tree Gitleaks를 검사합니다. main 대비 전체 diff의 공백 진단 6건은 testing-guide 원문·이식 사본에 이미 존재한 동일 표 행이며 보존 계약에 따라 수정하지 않습니다. 전체 diff를 공백 오류 0건으로 보고하지 않습니다. T-WIN-004의 보존 예시 style 진단과 Markdown parser의 알려진 한계를 전체 문서 통과로 바꾸지 않습니다.

실제 개인 설치·Codex 새 세션의 암시적 선택·ACL/ADS·운영 SSH·SMB·WSL·runtime·release는 미실행입니다. 원격 CI는 원격 조회가 확인된 경우에만 성공으로 판정합니다.

## 4. 게시와 복구

검증한 담당 파일만 commit하고 yunli 일반 push·원격 확인 후 main을 fast-forward합니다. 기존 작업본의 branch·index·변경 해시와 비공개 자료를 보존하며 다른 세션 변경을 대조합니다. 게시 후 복구는 검토된 revert이며 과거 원문·개인 설치를 일괄 복원하지 않습니다. 최종 원격 SHA·실제 병합 여부는 [전체 통합 기록](https://github.com/siasia86/12_github-main/blob/main/.governance/outputs/M12-MAIN-20261004-01/20261004_markdown/REVIEW.md)에서 확인합니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
