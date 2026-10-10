# Windows skill 목록

Windows 네이티브 실행 지침 21개를 제공합니다. 각 skill은 핵심 본문·UI 메타데이터와 실제 필요한 참조·도구를 동봉한 폴더 단위입니다. 현재 요청에 필요한 역할만 선택합니다.

## 1. 작업 수행과 판단

- [work-rules](work-rules/SKILL.md): 지속 작업의 범위·보고·모델 분담·검증·개인 skill 갱신.
- [status-report](status-report/SKILL.md): 별도 상황보고의 상태·근거·남은 조건·사용자 개입.
- [using-skills](using-skills/SKILL.md): 요청에 맞는 역할과 동봉 참조 선택.
- [repo-governance](repo-governance/SKILL.md): 실제 저장소 지침·예외·권한 확인.
- [planning-and-breakdown](planning-and-breakdown/SKILL.md): 큰 목표·의존성·실행 가능한 작업 분해.
- [goal-continuation](goal-continuation/SKILL.md): 승인된 목표의 대조·기존 Goal 유지·준비된 작업 이어가기.
- [fact-check](fact-check/SKILL.md): 요청 문서 각각의 전체 사실 검증; 수정 금지이면 검토만 수행.

## 2. 코드·시험·문서

- [code-review](code-review/SKILL.md): 코드·스크립트·IaC의 정확성·오류 처리·보안 검토.
- [testing-guide](testing-guide/SKILL.md): 변경 위험에 맞는 경계·실패·회귀 시험.
- [python-script-template](python-script-template/SKILL.md): Python 업무 골격·UTF-8·설정·종료 상태.
- [md-link-check](md-link-check/SKILL.md): Markdown 파일 링크·앵커·헤딩 검증 범위.
- [readme-template](readme-template/SKILL.md): 실제 적용된 README 양식과 검사 연결.
- [zircon-readme-policy](zircon-readme-policy/SKILL.md): 해당 저장소에서 채택한 Zircon 문서 기준.
- [git-commit-rule](git-commit-rule/SKILL.md): 커밋 제목·담당 파일·일반 게시 규약.

## 3. 인프라·보안·복구

- [spec-driven-infra](spec-driven-infra/SKILL.md): 요구·명세·설계·구현·검증 연결.
- [incremental-change](incremental-change/SKILL.md): 작고 검증 가능한 변경과 선행 호환성.
- [doubt-driven-infra](doubt-driven-infra/SKILL.md): 가정·반례·증거·가역성 검토.
- [debugging-and-recovery](debugging-and-recovery/SKILL.md): 장애 증거·원인·격리·복구.
- [security-tools](security-tools/SKILL.md): 실제 보안 도구·비밀정보·마스킹의 지원 범위.
- [shipping-checklist](shipping-checklist/SKILL.md): 배포 조건·시험·복구와 실제 운영 적용의 경계.
- [kiro-lock](kiro-lock/SKILL.md): 기존 이름을 유지한 Windows 협조자 잠금·소유 확인·해제.

기본 실행은 PowerShell·Git·Python 3.11 이상입니다. 필요한 추가 CLI는 해당 업무에서만 확인합니다. 단독 폴더 복사 후 필수 참조와 실제 도구를 검사하고, 설치·발견·선택·행동을 각각 기록합니다.

공통 지침은 [AGENTS.md](../AGENTS.md), 설정 예시는 [personal 안내](../personal/README.md), 복사·갱신은 [사용 안내](../README.md)를 따릅니다. 저장소별 문서 역할·위치·양식·상태·게시 규칙은 대상의 실제 지침을 우선합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-10

© 2026 siasia86. Licensed under CC BY 4.0.
