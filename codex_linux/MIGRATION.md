# 원문 대응과 Codex 호환 변경

## 1. 보존 방식

Kiro SKILL.md 19개 원문 전체를 각 스킬의 `references/kiro-original.md`에 동일 bytes로 보존합니다. 활성 `SKILL.md`도 원문 본문·예시·코드·체크리스트를 그대로 유지하며 H1 다음에 CODEX-COMPAT 주석으로 구분한 호환 절만 추가합니다. Bash·Python의 description은 YAML 파싱 오류를 고치기 위해 전체 값을 인용했고 값 자체는 같습니다. 이 두 frontmatter 인용 수정 외 원문의 삭제·대체 줄은 없습니다.

아래 전체 범위 대응이 모든 원문 조항·예시·코드·체크리스트에 적용됩니다. 원문 1–7행은 활성 1–7행(두 description 인용은 같은 3행)에 대응하며, 원문 8행부터 마지막 행까지는 호환 절의 추가 행 수만큼 이동합니다. `verification/verify_skills.py`는 호환 절·두 인용 수정만 제거한 활성 문서가 전체 원문 bytes와 같음을 검증합니다. 실제 `diff -u`도 수행하며 본문 감축이 없음을 확인합니다.

스킬 간 연결은 상대 링크로 동봉한 전체 지침 사본입니다. 각각 `references/skills/<이름>.md`와 비교용 `references/originals/<이름>.md`로 대응합니다. 원래 자기 본문을 참조로 옮겨 줄인 것은 없습니다. 순환 연결은 필요한 역할 전환에만 읽고 이미 읽은 본문을 반복 로드하지 않습니다.

## 2. 스킬별 원문과 분량

원문 경로는 `kiro/skills/<이름>/SKILL.md`, 활성 경로는 `codex/skills/<이름>/SKILL.md`입니다. 모든 스킬은 유지하며 설치 생략은 사용자의 환경별 선택입니다.

| 스킬                   | 원문 행 | 활성 행 | 추가 행 | 원문 8행 이후 대응 | 동봉 역할 수 |
|------------------------|---------|---------|---------|--------------------|--------------|
| bash-script-template   | 294     | 346     | 52      | 60–346             | 0            |
| code-review            | 118     | 135     | 17      | 25–135             | 0            |
| debugging-and-recovery | 209     | 230     | 21      | 29–230             | 1            |
| doubt-driven-infra     | 159     | 176     | 17      | 25–176             | 0            |
| git-commit-rule        | 94      | 129     | 35      | 43–129             | 2            |
| incremental-change     | 225     | 246     | 21      | 29–246             | 1            |
| kiro-lock              | 99      | 122     | 23      | 31–122             | 0            |
| md-link-check          | 289     | 325     | 36      | 44–325             | 2            |
| planning-and-breakdown | 212     | 233     | 21      | 29–233             | 2            |
| python-script-template | 389     | 515     | 126     | 134–515            | 0            |
| readme-template        | 67      | 99      | 32      | 40–99              | 2            |
| repo-governance        | 145     | 166     | 21      | 29–166             | 0            |
| security-tools         | 154     | 186     | 32      | 40–186             | 2            |
| shipping-checklist     | 130     | 153     | 23      | 31–153             | 3            |
| spec-driven-infra      | 253     | 275     | 22      | 30–275             | 3            |
| testing-guide          | 153     | 177     | 24      | 32–177             | 2            |
| using-skills           | 65      | 115     | 50      | 58–115             | 18           |
| work-rules             | 728     | 796     | 68      | 76–796             | 7            |
| zircon-readme-policy   | 44      | 80      | 36      | 44–80              | 9            |

## 3. 최소 호환 변경의 이유

- 공통: 사용자 > 저장소 > 개인 기본값과 상위 정책·현재 권한을 명시합니다. 다른 저장소·개인 홈을 경로만으로 수정하지 않고 과거 완료 상태를 현재 검증으로 사용하지 않습니다.
- work-rules: 승인된 범위의 자율 진행과 위험 작업 확인을 일관되게 해석합니다. sudo·강제 SSH 종료·짧은 timeout의 무조건 적용을 대체하고 현재 프로젝트의 기록 체계만 사용합니다. Kiro hook/memory는 자동 실행하지 않습니다.
- kiro-lock: 검사 후 덮어쓰기 획득과 무조건 rm 예시는 실행하지 않습니다. 동봉 helper의 O_EXCL·gate·세션/사용자/호스트·inode 확인으로 자기 잠금만 처리합니다. 노후 시간은 해제 승인이 아니며 남은 gate/비협력 writer/파일시스템 범위는 후속 제한으로 기록합니다. hook 비활성화와 수동 정책은 구분합니다.
- using-skills·repo-governance: 원문 선택 트리와 범용 규약은 유지하고 적용 AGENTS.md·실제 governance를 확인합니다. 없는 중앙 정책을 자동 구축하지 않습니다. 당시 도입 현황 표는 현재 설치 결과로 사용하지 않습니다.
- readme-template·zircon-readme-policy·git-commit-rule: 현재 대상의 owner/repo·license·Actions·branch·권한과 고유 예외를 확인합니다. 다른 저장소에 고정 yunli·Zircon 예외를 강제하지 않습니다. 사용자 승인에 원격 push가 포함됐는지 확인합니다.
- Bash·Python: description의 `: ` 때문에 발생한 YAML 오류만 인용 처리합니다. 원문 복잡도별 로깅 예외와 필수 헤더·SAFETY·VERSION·help 규약을 적용하고 시스템 로그 경로를 자동 생성하지 않습니다. 1차 Luna 결과에서 누락된 개인 템플릿 요소를 확인해 원문 대조 안내를 보완했습니다.
- md-link-check: 동봉 도구의 파일 링크와 같은 파일 앵커 범위를 구분하고 다른 파일 앵커는 실제 대상 헤딩을 별도로 대조합니다. 푸터 금지 저장소에서는 근거를 기록하고 style의 footer 항목만 제외합니다. 1차 Luna의 푸터 충돌 기록을 근거로 보완했습니다.
- security-tools: 미제공 개인 도구를 필수 설치 조건으로 두지 않습니다. 전체 설계·옵션·수동 검사·복원 원칙을 유지하며 실제 도구의 정규식/기존 map 동등성은 미검증입니다. 도구 구현/원본 확인이 필요한 요청에서는 격리 검증 후 처리합니다. 부족한 명세를 추정으로 구현했다고 주장하지 않습니다.
- planning·spec·incremental·debugging·doubt·shipping·testing·review: 각 원문 역할·계획 양식·검증·중단 기준은 유지합니다. 현재 요청 대상·실제 도구·운영 권한을 확인하고 필요한 동봉 역할만 이어 읽습니다. 계획/수동 리뷰와 실제 운영 실행을 구분합니다.

## 4. 동반 자료와 출처

필수 style은 `kiro/markdown/STYLE.md`의 동일 bytes 사본입니다. Markdown 검사 세 도구는 작업 시작 시 존재한 30 저장소의 독립 Python 파일 전체를 필요한 폴더에 복사했습니다. 초기 사본은 Python 3.11 표준 라이브러리만 사용하므로 사용 시 30 저장소와 pip 설치는 필요하지 않습니다. 개인 스킬에는 실제 도구/문서 파일을 넣었으며 초기 source hash는 아래에 남기며 2026-10-03 링크 검사기 보완은 6절에서 구분합니다. 잠금 helper는 이번 작업에서 작성하고 실제 동시 획득·소유 검사를 수행했습니다.

testing-guide의 외부 5축 상세 문서는 전체를 동봉했습니다. 활성 edge case 문서의 BVA 링크만 같은 폴더의 testing-guide BVA 절로 연결했습니다. 그 문서의 비교용 원문은 동일 bytes로 별도 보존하며 원래 32 저장소의 상대 링크는 비교 자료 안에만 남습니다. 비교 자료를 실행 의존으로 로드하지 않습니다. 다른 참고 문서 체인을 전체 복제할 필요가 없습니다.

Kiro의 prompt 16개는 스킬 19개 본문에서 필수 호출하지 않습니다. kiro 원본에 그대로 보존하고 별도 신규 스킬 자동 생성은 하지 않습니다. 기존 개인 보안 script/config는 실제 원본이 없어 동봉했다고 표시하지 않습니다.

| 동반 원본                                                                                            | SHA-256                                                          |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| /root/35_agent-skill/kiro/markdown/STYLE.md                                                          | f2797a30aaf805f9ab3cf157fff2e7229ad99dfe5cc6785b01b734090701a46a |
| /root/30_sia-scripts/src/md-style-check.py                                                           | 21d70e4cc4e4e272cbe64fdf6957dd10592eb26267a96c01d503c8a519c5ba10 |
| /root/30_sia-scripts/src/md-heading-check.py                                                         | 53015d827dc7576dd4221c7accf7398a3be0e97d596b0b0b2951164397455df7 |
| /root/30_sia-scripts/src/md-link-check.py                                                            | 9790836669891291beb19659668e2ef7e878776df287ed2301f7425ebb91706f |
| /root/32_system-engineering-resources/01_fundamentals/cs/testing/04_test_design/edge_case_testing.md | ac3cf80fa5cf22f9027f81c4c1edd141a62271810b2f0225038f1fc897998aca |

## 5. Kiro 스킬 기준 해시

| 스킬                   | SHA-256                                                          |
|------------------------|------------------------------------------------------------------|
| bash-script-template   | 5156328e4a35f9765907910f0431f65b71a9a2bd0c86982cc7a7311465fdac2c |
| code-review            | 4517d03039faec289e326ca452de1f62e8434d7c2bb9dec7c03bb05ac99b47d6 |
| debugging-and-recovery | 10140924f539da68922ce66acd54d6d30e596059f377bdeeeecbd8e26400b11e |
| doubt-driven-infra     | f56cbf7786e794ee886bb5d7a86abaa568e0bd4db194eef275f0c62bf65b622c |
| git-commit-rule        | 9fecb39349ea2536bcb781cd6c551541dc6839cad32e454bd3d037d2078437c5 |
| incremental-change     | 73abe0ab80accaae28ff8a628e16412255867aaacf063d2ee10bddc34b661d86 |
| kiro-lock              | 207914bf93b04e9a201297def12cf0a0c512bd4fb10ef20c86e8a5ba57c10553 |
| md-link-check          | 67bc59e6ca5432cd17ce0d13077cbaeaa51cc00c9c5764c8565323869d85aa05 |
| planning-and-breakdown | 11ca00491de7ace22d02b633db071d7c46233e8678b58d3a6ab1ed223694925a |
| python-script-template | 8691f514f0ac0530807fd0cffdf38e4ad4fb7e66019629874bb360df04d219d9 |
| readme-template        | 754dd7ea3b7be8e968802990ac8e63a2239285567d5c6c0ff45d935e8abc5a9e |
| repo-governance        | ec70916e7a09db1f82c4c4882292b9cb1d1ed8d72ba7ed27008a366eb9e95e17 |
| security-tools         | d61f66ef4cae5d85b9b80a24167b39340ac5be299e8d602fe380644ac3579ae3 |
| shipping-checklist     | f6a291a8f7119b888daabe2491917b380ca5c84fa9dfc83966c4a5e4d899effd |
| spec-driven-infra      | e102ac0892303423279dc10afa24fbd7fa939042205776586b5fa8cd4d9419b2 |
| testing-guide          | 5bb3a1be05d470a8f58d1459bd6d9a31c85ba00de81ac1e9fb8359c814028fda |
| using-skills           | 1ded614abc90d43868e43306e3381af04948168f5e419bc9cd004e67daa0be75 |
| work-rules             | a940ad7376aecac56a873671a3f77250fb6d4f6deb77598810bdfefd1420ed20 |
| zircon-readme-policy   | ad8f3b767ac27577365701cb6a026041b57080d992a2aea1de16db43510732c7 |

실제 검증·Luna 재검증과 미실행 범위는 [VERIFICATION](VERIFICATION.md), 후속 환경 확인은 [TODO](TODO.md)에 기록합니다. 개발 검사 script는 복사한 개인 스킬의 실행 의존성이 아닙니다.

## 6. 2026-10-03 동작 보완과 참조 완결성

사용자 요청의 로컬 보완·테스트를 수행했습니다. 위 표는 이번 보완 후의 현재 행 대응이며 Kiro 원문·예시·템플릿·체크리스트는 모두 유지합니다.

- Python: 원문 argparse·main·Atomic Write 블록은 그대로 두고 호환 절에 parser 반환 계약과 POSIX mode·uid·gid 보존 대체 블록을 추가했습니다. 처리 옵션·로깅·main 분기는 유지합니다.
- Bash: 원문 함수·문자열 호출은 유지하고 호환 절에 argv 실행·stderr 로그·원래 종료 상태 반환·필수 호출부 종료 예시를 추가했습니다.
- work-rules: §17의 삭제 예시는 원문으로 보존하고 동일 inode의 잠금 경로를 유지하는 POSIX context manager를 추가했습니다. 동봉 kiro-lock helper는 변경하지 않았습니다.
- md-link-check: 원문 지침은 유지하고 실행용 링크 검사기 7개를 문자·길이·닫는 태그·들여쓰기 기준으로 수정했습니다. 미닫힘은 종료 `2`로 보고하며 활성 동봉 지침 사본에도 적용 기준을 반영했습니다. 초기 외부 source hash를 수정본 hash로 덮어쓰지 않습니다.
- 참조: shipping-checklist의 code-review와 네 STYLE 역할의 readme-template·필요한 md-link-check를 전체 지침과 비교 원문으로 동봉했습니다. 동봉 역할은 45개에서 54개로 늘었고 형제 설치 의존은 없습니다. repo-governance의 템플릿 이름은 대상 저장소의 조건부 입력으로 명시했습니다.

동작·최종 파일 해시·검사 범위는 [보완 기록](../agent-workflows/codex/REMEDIATION_2026-10-03.md)과 [회귀 원시 결과](../agent-workflows/codex/reviews/2026-10-03-remediation/tests.json)에 남깁니다. 실행용 검사기는 Codex 폴더의 지역 수정본이며 30 저장소의 원본은 변경하지 않았습니다.

---

**작성일**: 2026-10-01

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
