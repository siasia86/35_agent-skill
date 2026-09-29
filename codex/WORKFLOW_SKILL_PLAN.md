# 작업 기록과 skill 경량화

## 1. 범위와 완료 조건

2026-09-29 사용자 요청에 따라 번호 규칙·skill 경량화 개선을 반영하고 CHANGELOG와 같은 맥락의 TODO를 정리합니다. 계정 소유 독립 clone에서 작업하며 사용자가 이번 게시 대상을 yunli로 확인했습니다. 변경 파일·정책·동반 파일 해시·참조 검증, 최종 검토 1회와 발견사항 보완 후 일반 push를 완료 조건으로 합니다.

31은 공통 문서 규약·독립 후보용 발췌·profile, 35는 skill 구현·catalog·작업 기록을 소유합니다. 30의 기존 실행기로 후보와 격리 패키지를 검증합니다. Kiro/GPT 원본과 기존 사용자의 변경은 보존합니다.

## 2. 변경과 판단

- NN_TODO[-SS] 규약과 최소 필드·선행 조건·기존 색인 유지·선택 읽기를 31 정책에 정의합니다.
- work-rules는 작업별 참조를 선택하고 Python 골격은 asset으로 분리합니다. 일반 skill의 선택 조건·보고 형식·반복 종료 조건을 작업 범위에 맞춥니다.
- 사실 검증과 문서 검토의 고정 반복 횟수는 명시한 횟수·예산 또는 완료·진행 정체 조건으로 대체합니다. 이번 요청의 최종 검토 1회는 그대로 적용합니다.
- 기존 Token 비교 TODO를 작업 01로 옮기고 루트는 링크를 유지합니다. 과거 governance 완료 체크리스트는 CHANGELOG로 연결하며 Kiro 대조·runtime·효과 측정은 미완료로 남깁니다.
- 실제 성능·사용량 개선은 측정 전이며 파일 길이나 정적 검사 결과로 주장하지 않습니다.

## 3. 검증과 최종 검토

변경 Markdown·skill 문법·catalog 및 동반 파일 inventory·31 profile/manifest 해시·30 생성/계획/격리 패키지 연동·보안·diff를 검사합니다. 최종 검토는 변경 전체를 대상으로 1회 수행하고 발견사항의 영향 범위만 재검증합니다.

상태: 구현·최종 검토 1회·발견사항 3건 보완·영향 범위 재검증 완료. 게시 대상은 yunli이며 실제 게시는 원격 Git 결과와 최종 보고로 확인합니다.

- 독립 검토: 요청 모델 gpt-5.6-sol/high, agent workflow_final_review. 실제 runtime 모델 식별은 확인할 수 없으므로 요청 모델과 구분합니다. 읽기 전용 검토이며 추가 검토 회차는 수행하지 않습니다.
- 발견·보완: 35 단독 clone의 번호 규약 누락을 최소 발췌로 보완했고, work-rules 공통 진입점에 자격증명 비기록 규칙을 복원했으며, 혼합 작업에서 필요한 복수 참조 선택을 허용했습니다.
- 초기 검사: 변경 Markdown 28개 style·heading·link, skill 25개 문법, agent 10개 TOML, 변경 diff·Gitleaks 통과. 31 전체 style 57개·heading/link 82개와 전체 작업본 Gitleaks 통과. 생성 후보를 포함한 실제 검사 파일 수입니다.
- 연동: 30 기존 profile·package·Codex governance 회귀 54개 통과. catalog 36 ID·40파일과 모든 동반 해시, 31 manifest 66개 해시·checksum, 개인·프로젝트 격리 40파일 설치·재적용 no-op, v2 profile 5개 선택·catalog 결속을 확인했습니다.
- 후보: 30·31·35 profile별 7파일 build·check·unchanged, 추출 Python 골격의 기존 코드 동일성·AST·help 검사를 통과했습니다. 실제 runtime에 설치한 결과가 아닙니다.
- 최종 보완 후 변경 Markdown 28개·skill 25개·diff·Gitleaks와 catalog/manifest 해시·개인/프로젝트 40파일 설치 및 no-op·세 저장소 7파일 후보 연동을 재검증해 통과했습니다. 실행기 코드가 같으므로 회귀 54개는 불필요하게 반복하지 않았습니다.
- 검사 중 조치: 문서 표 패딩 1칸 오류를 수정했습니다. 임시 연동 검사 스크립트의 Python import 경로와 profiles/ 접두어 누락은 검사 입력을 수정한 뒤 통과했습니다. 실행기 코드는 변경하지 않았습니다.
- 미실행: 실제 skill 자동 선택·개인 runtime·Kiro 최신 원문 대조·경량화 품질 및 사용량 비교. GitHub CLI 미인증으로 원격 CI는 게시 후 확인 가능 범위를 따로 보고합니다.

## 4. 복구

게시 전에는 이번 diff만 검토해 되돌립니다. 게시 후에는 해당 commit의 검토된 revert를 사용합니다. 이전 정책·catalog·동반 파일을 함께 되돌려 해시 일치를 유지하며 runtime 적용·release는 별도 작업으로 남깁니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
