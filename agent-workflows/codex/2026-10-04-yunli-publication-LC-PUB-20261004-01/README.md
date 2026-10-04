# LC-PUB-20261004-01 작업 완료 후 yunli 게시

## 1. 요청과 담당 범위

사용자가 개인 local Codex의 완료 절차에 항상 yunli commit·push와 사용자 확인을 추가하고 먼저 workflow를 출력하도록 요청했습니다. yunli가 branch임을 확인했고 작업 전 절차를 보고했습니다.

담당·예정 commit 파일은 Windows 배포 원본의 AGENTS, work-rules와 git-commit-rule의 SKILL.md, Windows PLAN·TODO, 루트 CHANGELOG와 이 업데이트의 README·validation.json입니다. 다른 저장소·Linux 및 비교 원문·중앙 정책은 이번 수정 대상이 아닙니다.

## 2. 적용 workflow

1. 실제 Git 루트·branch·기존 변경·현행 지침과 개인 설치본의 차이를 확인합니다.
2. 전체 이전 skill 폴더·개인 AGENTS와 파일 hash를 이 작업의 Git 제외 private에 보존합니다.
3. 35의 배포 원본에서 AGENTS·두 skill의 Windows 실행 본문을 수정하고 메타데이터·Markdown·참조·정책 사례·비밀값 검사를 수행합니다.
4. 검증된 전체 skill 폴더와 개인 AGENTS의 해당 항목을 로컬에 반영합니다. 기존 개인 경로 안내·다른 skill·system·config는 보존하고 전후 hash를 대조합니다.
5. 검증·기록 완료 후 검토한 담당 파일만 yunli에 commit·일반 push합니다. 원격 SHA를 대조하고 사용자에게 commit 링크와 수행·검증·미실행을 보고합니다.

## 3. 상시 완료 절차와 제외 범위

Git 변경이 있는 작업은 검증·기록 → 담당 파일만 yunli commit·일반 push → 원격 확인·사용자 commit 링크 보고까지 진행합니다. 이 범위의 승인은 반복 확인하지 않습니다. 현재 사용자의 별도 게시 제한·플랫폼 및 보호 branch 정책은 유지합니다. checkout이 다르면 기존 branch·사용자 변경을 보존한 게시용 작업본을 준비합니다.

읽기 전용·변경 0건에는 빈 commit을 만들지 않고 검증 실패·비밀값·다른 작업의 변경은 게시하지 않습니다. main 병합·force push·release·운영 적용은 포함하지 않습니다. 게시 실패는 원인과 미게시 상태를 보고하고 완료로 표시하지 않습니다. 과거의 고정 checkout 예시는 보존 비교 자료로 유지합니다.

## 4. 검증과 관찰 상태

원본·로컬 대조에서 work-rules 44개와 git-commit-rule 18개 파일은 모두 동일했습니다. 개인 AGENTS의 로컬 관리 경로 안내는 원본과 별도인 사용자 차이로 보존합니다. 원본 전체와 설치본 전체를 백업한 뒤 지정 범위만 갱신합니다.

전체 2개 skill 폴더 62개 파일과 개인 AGENTS의 해당 항목을 로컬에 반영했고 source/installed hash를 대조했습니다. 기존 관리 경로 안내·다른 개인 skill·system·config는 유지했습니다. 메타데이터 2개·Markdown 7개·파일 링크 63개·교차 앵커 13개의 검사와 공백·비밀값·Git 제외 검사를 통과했습니다. Luna는 지침 행동 사례 5개를 읽기 전용 검토했으며 실제 새 세션 행동 검사로 확대하지 않습니다.

공식 스킬 검사기의 첫 실행은 PyYAML 부재로 실패했습니다. 실패 기록을 유지하고 PyYAML 6.0.3을 Git 제외 task 전용 경로에만 준비해 검사 subprocess에서 사용한 뒤 메타데이터 검사를 통과했습니다. 일반 Python·개인 config·환경 설정은 바꾸지 않았습니다.

검증·설치 결과는 [validation](validation.json)에 기록합니다. 배포용 AGENTS·SKILL의 기존 양식은 푸터 없이 유지하고 작업 기록은 기존 푸터 양식을 따릅니다. 새 세션 자동 발견·실제 향후 작업에서의 정책 행동은 정적·설치 hash 검사와 구분하며 [Windows TODO](../windows/TODO.md)에 남깁니다. Git 게시와 CI·main 반영은 별도 상태입니다.

## 5. 복구와 게시 근거

private의 before와 현재 파일을 대조해 이번 담당 변경만 복구합니다. 로컬 전체 이전 폴더·개인 경로 안내·다른 작업 변경을 보존하고 게시 후에는 검토한 revert를 따릅니다. private의 원형 개인 지침·실제 경로·raw는 Git 제외 대상이며 원격 문서에 복사하지 않습니다.

이번 파일들의 실제 게시 commit은 yunli의 Git 이력과 최종 사용자 보고에서 확인합니다. 원격 SHA 대조 결과는 private 게시 receipt에 보존하며 미실행 CI나 사용자 확인을 완료로 바꾸지 않습니다.

---

**작성일**: 2026-10-04

**마지막 업데이트**: 2026-10-04

© 2026 siasia86. Licensed under CC BY 4.0.
