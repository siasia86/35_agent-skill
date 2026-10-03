# Codex Windows 전체 이관 검토

Linux skill **19개 전체**, 출처 파일 **182개**, 동봉 역할 **54개**, 설정 원본 **2개**를 Windows에 대응했습니다. 전체 원문·예시·템플릿·체크리스트와 비교 자료를 보존합니다. 최적화와 개인 홈 일괄 적용은 후속입니다. 상세 기준은 [이관 기록](../agent-workflows/codex/WINDOWS_MIGRATION_2026-10-03.md), 실제 비식별 결과는 [results.json](verification/results.json)에 있습니다.

## 1. 최종본 직접 검사

| 검사                         | 실제 결과                                     | 판정      |
|------------------------------|-----------------------------------------------|-----------|
| 원본·필수 참조               | 19개·182파일·54역할·설정2개·호환 절 링크214개 | 통과      |
| 공식 skill-creator validator | 실제 YAML·메타데이터19/19                     | 통과      |
| 활성 Python 구문             | 34개 AST                                      | 통과      |
| 단독 폴더 복사 후 실행       | 19개 폴더·41회 실제 helper 호출               | 통과      |
| Markdown native fixtures     | 63/63; 다른 드라이브 포함                     | 통과      |
| Python·lock·Bash fixtures    | 79회 기대 결과 일치; symlink 1건 SKIP         | 부분 검사 |
| Windows byte-lock 예제       | Python 구문2개·정상/경쟁/해제/예외 포함7조건  | 통과      |
| PowerShell 예제              | 13개 parser 구문; 명령 실행은 별도            | 정적 확인 |

네이티브 PowerShell·Python 3.14.8와 설치된 Git Bash를 사용했습니다. Markdown은 한글·공백·CRLF·각괄호/균형괄호/인코딩 링크·중복 suffix·인용/tilde fence·누락/혼합 입력·TOML·기존 CLI를 검사했습니다. C:와 J: 사이 상대 경로가 없는 경우의 표시·제외 판정도 직접 검사했습니다.

Python은 실제 변환 함수를 TEMP에서 제공한 경우의 멱등성·혼합 실패와 원자 replace 실패 시 원파일 보존을 검사했습니다. 업무 변환이 없는 기본 템플릿의 일반 실행은 1이며 dry-run만 입력/계획을 확인합니다. lock은 JSON/fsync 실패 후 자기 파일 정리·재획득, 기존/타인/손상/guard/다른 inode 보존, 8개 프로세스 경쟁의 단일 획득을 검사했습니다. Bash 백업 cp 실패는 일반·errexit 모두 원 종료7을 전파하고 후속 성공을 보고하지 않았습니다. 옵션값·플랫폼 미지원은 변경 전에 거부합니다.

독립 agent가6개 요청을 별도사례로 평가했습니다. Markdown/Python은TEMP에서실행하고 복구·IaC·Zircon범위는필요자료/판단을검토했습니다. 발견한Bash옵션값과게시대상표현은보완후각각후속확인을분리했습니다. [사례 요약](verification/behavior_summary.json)은단일평가자·6사례·관찰시점해시와한계를기록하며 실제Codex자동발견이나19개전부실업무검증을뜻하지않습니다.

## 2. 과거 준비 검사와 새 결과의 관계

준비 단계의 cp949 Markdown 실패11회·UTF-8 성공11회·기본 lock6회는 과거 관찰입니다. 이를 새 최종본의 결과로 바꾸지 않습니다. Windows helper는 UTF-8 읽기/쓰기/출력을 명시하고 네이티브 호출을 사용합니다. Linux 과거 모델·회귀 JSON도 그대로 보존합니다.

통합 중 발견한 동봉 자기 참조 경로와 다른 드라이브의 relpath 오류를 교정했습니다. 독립 사례에서 발견한 Bash 옵션값 검증도 별도 실패 fixture로 보완했습니다. 원문의 이미 알려진14건은 Windows 실행 절·도구의 대체 계약과 [기존 검토](../agent-workflows/codex/SKILL_REVIEW_2026-10-03.md)를 연결합니다.

## 3. 한계와 다음 확인

symlink fixture는 Windows 생성 권한이 없어 SKIP입니다. NTFS ACL/owner/ADS·network FS·비협조 writer·실제 서비스·Terraform/Ansible/Docker 운영 적용은 검증하지 않았습니다. 비교용 POSIX owner/flock 예제를 Windows 보장으로 보고하지 않습니다.

개인 홈 설치·기존 config 병합·Codex 새 세션 발견/자동 선택·관리 sandbox 실제 준비·전체 WSL 동작은 미실행입니다. [설정 안내](personal/README.md)에서 미제공 개인 설정과 현재 확인된 원본을 구분합니다. 사용자 검증 후 main 반영, 전체 이관 이후 최적화를 진행합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
