# Codex Windows 제약과 후속 확인

전체 이관본에서 교정한 호환 문제와 아직 검증하지 않은 환경 보장을 구분합니다. 실제 근거는 [REVIEW](REVIEW.md)와 [이관 기록](../agent-workflows/codex/WINDOWS_MIGRATION_2026-10-03.md)을 따릅니다.

## 1. 교정하고 검사한 문제

- 기본 cp949 의존: helper의 UTF-8 입출력과 `python -X utf8 -B`를 적용해 한국어·공백·CRLF를 검사했습니다. 준비 단계의 실패 기록은 유지합니다.
- 누락 입력·실패 전파·부분 lock 쓰기: 실패를 0으로 보고하지 않고 자기 생성 파일만 정리합니다. 다른 파일·기존 lock을 보존했습니다.
- Markdown 정상 문법: 각괄호·균형괄호·인코딩 경로·중복 앵커·인용/tilde fence의 기대 결과를 검사했습니다. 전체 Markdown renderer나 reference-style/네트워크/다른 파일 앵커 완료로 확대하지 않습니다.
- 다른 드라이브: 상대 경로가 없는 C:/J: 조합의 표시에는 절대 경로 fallback을, 제외 판정에는 해당 기준만 건너뛰는 처리를 적용했습니다.
- 동봉 자기 참조: 부모 skill을 가리킬 때 그 폴더 SKILL.md로 연결해 단독 복사에서도 필수 자료가 해결됩니다.
- Bash 옵션값: 다른 옵션을 파일/서비스 값으로 소비하지 않고 잘못된 입력을 변경 전에 거부합니다.

## 2. 플랫폼 보장과 미검증

Windows mode를 NTFS ACL로 간주하지 않습니다. 원자 replace의 owner/ADS/확장 메타데이터·hard-link 관계·전원 장애 영속성, SMB·비협조 writer의 보안 경계는 별도 검증 대상입니다. 운영 파일·권한을 임의 변경하지 않습니다.

symlink/reparse 거부 코드는 작성했으나 실제 symlink 생성 fixture는 권한 부족으로 미실행입니다. 기존 파일 대조·실패 정리·협조자 경쟁 검증과 구분합니다. Kiro hook·POSIX service/flock/owner 예시는 비교 자료이며 현재 실행 절차를 사용합니다.

## 3. 실제 적용과 추가 설정

개인 홈 적용·Codex 새 세션 발견·사용자 검증·main 반영·최적화는 [TODO](TODO.md)의 후속입니다. 제공되지 않은 다른 Linux home/원격 기기의 개인 설정은 이관 완료로 주장하지 않습니다. 실제 설정이 제공되면 비공개 상태에서 필요한 Windows 대응만 검토하고 공개 원문에 자격증명·계정·개인 경로를 넣지 않습니다.

---

**작성일**: 2026-10-03

**마지막 업데이트**: 2026-10-03

© 2026 siasia86. Licensed under CC BY 4.0.
