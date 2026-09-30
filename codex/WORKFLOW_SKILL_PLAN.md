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

## 5. 2026-09-30 개인 skill 설치 목록 정리

사용자는 Windows 설치 결함 수정·재검증과 공식 Codex skill 문서에 따른 과도한 개인 skill 제거를 요청했습니다. [공식 skill 안내](https://learn.chatgpt.com/docs/build-skills)와 [skill·prompt 재검토 안내](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)를 실제 열람했습니다. 짧고 구체적인 선택 조건, 관련 자료만 읽는 구조, 이미 가능한 일반 작업을 장황한 절차로 반복하지 않는 기준을 적용합니다. 아래 제외 목록은 이 저장소의 판단이며 공식 권장 삭제 목록이 아닙니다.

### 제외한 9개와 기능의 위치

- using-skills: 일반적인 skill 라우팅은 Codex 선택과 적용 지침에서 처리합니다. 개별 skill은 자신의 좁은 선택 조건을 유지합니다.
- planning-and-breakdown: 일반 작업 계획은 요청·저장소 정책에서 처리하고 중요한 인프라 사양은 spec-driven-infra에 남깁니다.
- incremental-change: 단계별 검증·중단·복구는 기존 작업 계획과 work-rules의 선택 참조를 사용합니다.
- doubt-driven-infra: 위험·승인·복구 검토는 spec-driven-infra·git-release와 적용 정책에 남깁니다.
- shipping-checklist: 별도 일반 출시 체크리스트 대신 요청된 release의 git-release와 저장소 release 정책을 사용합니다.
- readme-template: 일반 README 작성은 Codex와 저장소 문서 관례를 따르고 구조·링크 검사는 markdown-review·md-link-check를 사용합니다.
- testing-and-verification: 기존 검사 선택·결과 구분을 testing-guide에 짧게 통합하여 검사 실행과 test authoring을 한 진입점에서 구분합니다.
- kiro-lock: Codex에서 존재하지 않는 Kiro hook을 가정하지 않는 기준은 적용 AGENTS·저장소 coordination 정책에 남깁니다. 독립 개인 skill로 설치하지 않습니다.
- zircon-readme-policy: 특정 저장소만의 푸터·배지 예외는 해당 저장소 정책·선택 profile의 범위입니다.

마지막 payload bytes는 `archive/retired-payload/skills/<이름>/SKILL.md`에 보존합니다. 이 경로는 자동 발견·catalog·setup 선택 대상이 아닙니다. Kiro/GPT 원본·최초 baseline·기존 archive 원문은 보존합니다. 개인 홈의 기존 설치는 자동 삭제하지 않으며 기존 사용자 수정과 다른 의존성을 확인한 뒤 필요하면 runtime 검색 밖으로 격리합니다.

### 유지한 구체적 역할과 계약

현재 개인 skill 16개는 Ansible 검토, Bash/Python 양식, 직접 코드 검토, 디버깅·복구, 기술 사실 검증, 한국어 commit 양식, 요청된 release 준비, Markdown 형식/링크 검사, 로컬 지침 discovery, 보안 audit/도구 사용, 인프라 사양, 검사/테스트 선택, 선택형 개인 관례입니다. code-review는 사용자의 직접 검토에 사용하고 시스템 review-agent는 위임 검토 경로이므로 단순 이름 바꾸기·삭제로 통합하지 않습니다. fact-check는 OpenAI 전용 openai-docs와 범위가 다릅니다. setup은 로컬 bytes 검증을 제공하여 네트워크 기반 시스템 installer와 구분합니다. 개인 사용은 31을 필수 의존하지 않습니다.

agent 10개·개인 지침 한 개·동반 파일 4개는 유지합니다. catalog는 27 ID·31파일로 갱신하고 system-engineer·infra_worker의 optional skill 참조는 spec-driven-infra·testing-guide로 변경합니다. 과거 Batch 6의 25개·40파일 검증 수치는 당시 기록으로 보존합니다. 31 agent는 현재 catalog bytes로 pin을 재검토하고 제외 ID를 선택한 profile이 있다면 선택 이유·대체 경로를 검토합니다. 중앙 profile을 이 작업에서 수정하거나 승인하지 않습니다.

### 수정·검증·복구 범위

`.gitattributes`는 payload·catalog·governance template와 setup/test Python의 LF를 고정합니다. 정확한 bytes 해시 검증을 유지하고 CRLF를 설치기에서 조용히 정규화하지 않습니다. 이전 checkout은 사용자 변경을 보존하고 새 clone으로 대조합니다. 보존 원본과 archive에는 줄바꿈 정책을 적용하지 않습니다.

회귀 검사에 실제 Git core.autocrlf=true clone과 설치를 추가했습니다. 이 변경의 source·catalog·archive 보존·참조 및 Windows clone 재현 결과는 [추가 검증 기록](CODEX_GOVERNANCE_VERIFICATION.md#8-2026-09-30-windows-clone-수정과-skill-정리)에 남깁니다. 게시 전 복구는 이번 archive 이동·통합 skill·catalog·지침/문서·attributes 변경을 함께 검토해 되돌리며 사용자 변경은 보존합니다. 개인 runtime·commit·push·release는 수행하지 않습니다.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
