# Codex Windows 개인 skill 준비

Windows 네이티브 PowerShell과 Python에서 사용할 개인 skill의 계획·기록 골격입니다. 현재 Windows `SKILL.md`, 실행 코드, 개인 config는 작성하지 않았으며 개인 설치·Codex 발견도 미실행입니다.

## 1. 원본과 작업 범위

[Codex Linux](../codex_linux/README.md)의 기존 19개 원문·예시·참조·검증 기록을 보존합니다. Linux 본문을 축약해 Windows 모음으로 복제하지 않습니다. Windows 전용 구현은 플랫폼 조건과 필요한 기능을 확인한 뒤 별도 작업합니다. 이번 범위는 문서·빈 구현 영역의 안내이며 구현 완료나 19개 스킬의 Windows 검증 완료를 뜻하지 않습니다. 전체 분리 범위는 [플랫폼 분리 기록](../agent-workflows/codex/PLATFORM_SPLIT_2026-10-03.md)을 따릅니다.

## 2. 문서와 구현 진입점

| 위치                                   | 역할                      | 현재 상태        |
|----------------------------------------|---------------------------|------------------|
| [PLAN](PLAN.md)                        | 의존 단계·검증·복구       | 계획             |
| [TODO](TODO.md)                        | 미완료 작업 색인          | 준비 단계        |
| [ISSUE](ISSUE.md)                      | 확인된 제약·문제          | 관찰 기록        |
| [REVIEW](REVIEW.md)                    | 직접 Windows fixture 검증 | 제한된 검사      |
| [skills](skills/README.md)             | 향후 독립 skill 폴더      | 구현 없음        |
| [verification](verification/README.md) | 향후 Windows 검사·근거    | 실행 코드 없음   |
| [personal](personal/README.md)         | 향후 선택적 개인 지침     | config·설치 없음 |

문서·개발 검증 자료를 개인 skill 설치 입력으로 사용하지 않습니다. 향후 설치 단위와 필수 동반 자료는 각 Windows skill에서 확정합니다.

## 3. Windows 실행 원칙

실제 PowerShell·Python 실행 경로와 버전을 확인합니다. `python3` 이름이 WindowsApps alias인지 확인하고 동작하는 Python 실행 파일을 사용합니다. 현재 직접 관찰한 Python 3.14.8은 기본 locale이 cp949입니다. 동봉 Markdown 검사기 대표 사본은 UTF-8을 명시한 실행에서 검사했으며 결과는 [REVIEW](REVIEW.md)에 기록합니다. 향후 Python 문서·실행 절차는 UTF-8 파일 읽기·쓰기와 출력을 명시하고, 호출 예시는 `python -X utf8 -B`를 기준으로 실제 환경에서 확인합니다. 이 문서가 시스템 환경 변수나 기존 Codex 설정을 변경하지는 않습니다. POSIX 파일 소유·flock·Bash 예제를 Windows 보장으로 사용하지 않습니다. Windows 메타데이터와 참여 agent 잠금은 플랫폼별로 검증합니다.

## 4. 완료와 게시 순서

작업 완료 후 검증한 변경을 yunli에 push하고 사용자 검증을 기다립니다. 사용자 검증 결과를 반영한 뒤 main에 반영·push합니다. yunli 게시를 사용자 검증이나 main 반영 완료로 표시하지 않습니다.

개인 홈 설치·설정 변경·새 세션 발견·운영 적용은 각각 명시된 범위에서 별도로 진행합니다. 개인 경로·계정·config 원문·raw 비공개 증거는 이 문서나 공개 저장소에 복사하지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
