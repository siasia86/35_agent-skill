# 35 `agent-skill`

AI Agent skills repo. AI 도구별 공개 자료 미러를 관리합니다.

## 목차

| 섹션                                              |
|---------------------------------------------------|
| [1. 목적](#1-목적) / [2. 구성](#2-구성)           |
| [3. 운영 원칙](#3-운영-원칙) / [4. 검증](#4-검증) |

---

## 1. 목적

`35_agent-skill`은 AI 도구별 실행 환경(skill·agent·prompt·hook)의 공개 자료 mirror를 관리하는 저장소입니다. 도구별 원본과 공개 mirror의 관계는 하위 디렉토리별로 분리합니다.

저장소 운영 정책 자체는 [31 `governances`](https://github.com/siasia86/31_governances)를 따릅니다. 이 저장소에는 저장소 공통 policy를 다시 작성하지 않습니다.

## 2. 구성

| 디렉토리  | 역할                  | 원본·범위            |
|-----------|-----------------------|----------------------|
| `kiro/`   | Kiro 공개 미러        | `~/.kiro/` 허용 목록 |
| `claude/` | Claude 공개 미러 예정 | 원본·허용 목록 미정  |

- [Kiro 미러](kiro/README.md): `~/.kiro/`에서 허용된 자료만 보존합니다.
- [Claude 미러](claude/README.md): Claude 자료 추가를 위한 예약 영역입니다.
- [초기 적용 작업](USER_TODO.md): clone 후 Kiro Agent Skill을 적용하는 작업 목록입니다.
- [업데이트 작업](UPDATE_TODO.md): 참고 문서를 기반으로 Skill·Agent·Prompt를 고도화하는 작업 목록입니다.
- [Agent 참고 문서](_reference/INDEX.md): 업데이트에 사용하는 참고 문서 색인입니다.

## 3. 운영 원칙

- 저장소 정책은 특정 AI 도구의 실행 환경과 분리합니다.
- 도구별 원본 경로와 동기화 허용 목록을 별도로 관리합니다.
- 개인 설정, 세션 상태, 자격증명, 내부 환경 정보는 공개 미러에 포함하지 않습니다.
- 원본에서 공개 미러로의 동기화만 허용하며 자동 역동기화는 수행하지 않습니다.
- 디렉토리 구조를 변경하면 이 `README.md`와 `CHANGELOG.md`를 함께 갱신합니다.

## 4. 검증

```bash
sia-md-link-check .
sia-md-heading-check .
sia-md-style-check .
git diff --check
gitleaks detect --source . --no-git --no-banner
```

`kiro/`와 향후 `claude/`의 미러 문서는 원본 형식을 보존할 수 있으므로 일반 Markdown 스타일 검사에서 별도 예외로 관리합니다.

---

**작성일**: 2026-08-31

**마지막 업데이트**: 2026-09-04

© 2026 siasia86. Licensed under CC BY 4.0.
