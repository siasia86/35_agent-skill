# Windows 전체 이관 기록

사용자가 Linux에서 사용하던 **skill과 설정을 먼저 모두 Windows에 이관하고 이후 최적화**하도록 요청했습니다. 이전 문서 골격 범위를 확대해19개 전체 본문·필요 자료·실행 도구와 현재 저장소의 공통 지침/설정을 작성했습니다. 이 문서가 이번 작업 기준·대응·검증·복구의 본문이며 [Windows TODO](windows/TODO.md)는 상태 안내입니다.

## 1. 출처와 보존 범위

기준 commit은 `63e382bd5433bc1572556a528920add0d974c6e3`의 yunli이며 작업 시작 시 변경 없이 깨끗했습니다. 원본은 `codex_linux/skills`19개·182파일, `codex_linux/personal/AGENTS.md`, 저장소 `.codex/config.toml`입니다. 구현은 `codex_windows`, 관찰은 이 문서에 기록합니다. 다른 저장소·개인 홈·보호 원본을 수정하지 않습니다.

19개 이름·역할은 [전체 대응표](../../codex_windows/skills/README.md)에 빠짐없이 연결합니다. Windows 활성 SKILL과 동봉 역할54개의 CODEX-COMPAT 밖 본문·frontmatter는 기존 Linux와 같으며 원문·예시·템플릿·체크리스트를 축약·삭제·통합하지 않았습니다. Windows 호환 절의 실행 계약이 플랫폼 충돌과 교정한 과거 예시를 대체합니다.

19개 Linux SKILL은 `references/linux-original.md`, 변경한 동봉 역할은 `references/linux-skills`, 기존25개 도구는 `references/linux-tools`에 bytes 그대로 보존합니다. Kiro19개와 기존 원문/스타일/경계 테스트 자료도 유지합니다. [source_manifest.json](windows/verification/source_manifest.json)은182개 전체의 원본 경로·활성 경로·보존 경로·SHA-256과 설정2개를 대조합니다. 비교용 코드·문서는 현재 실행 지시로 다시 사용하지 않습니다.

## 2. Windows 실행 대응과 최소 보완

기본 실행은 PowerShell·Git·Python3.11 이상이고 Python helper는 표준 라이브러리와 명시적 UTF-8을 사용합니다. Bash 역할은 Git Bash/WSL로 유지하며 Windows 서비스는 실제 PowerShell/현재 저장소의 절차로 처리합니다. Terraform/Docker/Ansible·원격 Linux·SSH/ACL은 실제 도구·대상·권한·계층을 확인합니다. `/root`·Kiro URI·hook·POSIX owner/flock을 Windows 기능으로 자동 치환하지 않습니다.

| 기존 검토           | Windows 현재 대응                                                                   | 검증 범위                             |
|---------------------|-------------------------------------------------------------------------------------|---------------------------------------|
| R01·R03·R04·R05·R06 | state와리소스복구 구분·변경전패키지상태·app호환선행·실제가역성·공개listener의정당화 | 실행절/독립사례; 운영apply 미실행     |
| R02                 | cp 실패를 원 종료상태로 반환; 후속 성공 차단                                        | 실제 Git Bash 일반/errexit            |
| R07·R14             | 누락/혼합입력 실패 집계·sys.exit 계약·등록된help만 광고                             | 실제 nativePython                     |
| R08                 | 새 own inode의 부분쓰기 실패만 정리; 기존/타인/손상 보존                            | JSON/fsync 실패·재획득·8프로세스 경쟁 |
| R09·R10·R11·R12     | 누락입력nonzero·정상destination·중복suffix·인용/tilde fence                         | 63개 Markdown fixtures                |
| R13                 | 실제 playbook/container 대상과health존재 조건                                       | 문서/구문; 외부CLI 미실행             |

상세 기존 문제는 [skill 내용 검토](SKILL_REVIEW_2026-10-03.md)에 그대로 둡니다. Linux 원본은 수정하지 않았고 Windows의 활성 절·도구에서 대응했습니다. 통합 검사에서 발견한 동봉 자기 참조·C:/J: 다른 drive relpath와 독립 사례의 Bash 옵션값 검증도 교정했습니다. 이는 이관의 실행 호환성과 실패 전파 보완이며 경량화 단계가 아닙니다.

새 전체 Python/Bash 템플릿을 각 역할과 using-skills에 동봉합니다. Python의 업무 변환은 원문에도 미정인 계약이므로 임의 기능을 만들지 않습니다. 기본 일반 실행은 미구현 실패1, dry-run은 입력/계획 확인입니다. helper34개Python·2개Bash를 제공하며 md_common도7개 폴더에 함께 넣었습니다.

## 3. 설정 전체 대응

[personal 안내](../../codex_windows/personal/README.md)에서 출처·적용·복구를 관리합니다. Linux 공통 AGENTS23행은 전체 보존하고 Windows 적용 절을 추가했습니다. 공유 config의 approval_policy·approvals_reviewer·sandbox_mode 값은 유지하고 nativeWindows sandbox 예시만 추가했습니다. 실제 저장소 `.codex/config.toml`·사용자 홈 설정은 바꾸지 않았습니다.

현재 활성 Linux 모음에 별도 model/provider/MCP/agent/hook 설정은 없습니다. 로컬 WSL 두 배포판의 기본 Codex home에서도 config/AGENTS 부재를 존재 검사로 확인했습니다. 폐기한105_backup의 설정은 보존 이력이고 현재 설치 입력으로 부활시키지 않습니다. 다른 기기·다른 CODEX_HOME·원격 Linux의 실제 개인 설정은 제공되지 않았으므로 완료 범위에 포함하지 않습니다. 자격증명·개인 경로·raw 운영 자료를 공개 문서에 복사하지 않았습니다.

## 4. 최종 검사와 관찰

- 통과: 원본182파일·설정2개·19본문·54동봉역할 보존,214개호환절필수링크,34개Python AST,19폴더독립복사 후41회helper실행.
- 통과: 공식skill-creator quick_validate19/19. 필수PyYAML6.0.3은 작업TEMP에만 준비했고 Windows runtime 의존성/개인 홈 설치로 추가하지 않았습니다.
- 통과: nativeWindowsPython3.14.8 Markdown63/63; 한국어·공백·CRLF·다른drive·CLI/설정/문법/실패반환.
- 부분 검사: Python·lock·GitBash 79실행 조건 일치, symlink 1건 생성권한 부족으로SKIP.
- 통과: Windows inlinePython2개AST와byte-lock7조건; PowerShell13예제는구문만확인.

상세 수치와 비식별 사례는 [REVIEW](windows/REVIEW.md), [results.json](windows/verification/results.json)을 따릅니다. 실제 원시 입력·stdout/stderr·TEMP·개인 경로는 로컬 비공개 근거로 보존합니다. 과거LinuxJSON/모델사례를 새 Windows 결과로 바꾸지 않습니다.

미실행: 실제홈설치/config병합·Codex재시작발견/자동선택·관리sandbox실제준비·NTFS ACL/owner/ADS/SMB/비협조writer·원격운영/서비스·전체WSL환경. 코드작성·정적검사·협조자경쟁 성공을 전체OS보장이나설치완료로 보고하지 않습니다.

독립agent의6개요청사례와Bash/게시범위후속을 [비식별 요약](windows/verification/behavior_summary.json)에 기록했습니다. 기대답변이나개발검토를넘기지않고현재skill과필요참조로평가했으며, 단일평가자의수동사례·TEMP실행·정적판단을Codex재시작발견/전체실업무검증과구분합니다. baseline해시는관찰시점이고후속본문·도구변경해시와최종fixture결과는따로연결합니다.

게시 전 staged 경로318개와최종Windows입력309개해시를대조했습니다. 기존추적509개중연결안내14개만수정하고나머지495개bytes를보존했습니다. Git 공백검사의6건은기존 testing-guide 원문118행의같은후행공백을보존한사본이며새작성영역0건입니다. 원문보존을위해해당공백을삭제하지않았고다른변경을묵인하지않았습니다.

## 5. 게시와 복구

검증한 전체 이관본을 yunli에 일반commit·push하고 사용자 검증을 기다리는 순서를 적용합니다. main 반영·push와 최적화는 사용자 검증 후속입니다. 실제 게시 SHA와 원격 일치는 Git refs 및 작업 보고에서 확인합니다. 설치·release·운영 적용을 게시 승인으로 추정하지 않습니다.

미게시 복구는 이번 codex_windows 신규/변경과 연결 안내만 현재 사용자 변경과 대조해 복구합니다. Linux·Kiro·GPT·105_backup·과거 증거를 삭제하지 않습니다. 게시 후에는 검토한revert를 사용하고 force/reset/다른작업의일괄복구를 하지 않습니다. 실제홈 적용 시에는 해당 환경의 적용전비교/백업으로 이번병합분만 복구합니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
