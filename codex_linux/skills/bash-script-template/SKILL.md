---
name: bash-script-template
description: "Bash 스크립트 작성 시 표준 로깅 함수와 에러 처리 패턴을 적용합니다. 새 스크립트 생성 또는 기존 스크립트 개선 시 사용합니다. 이 skill을 참조할 때 응답 첫 줄에 \"🟡 참조: skill://bash-script-template\" 를 출력합니다."
---

# Bash Script Template

<!-- CODEX-COMPAT-BEGIN -->
## Codex 호환 및 적용 규칙

이 절은 원문을 축약하지 않고 추가한 Codex 호환 규칙입니다. 아래 Kiro 원문의 규칙·예시·템플릿·체크리스트는 계속 적용하되, 이 절에서 명시한 플랫폼·경로·권한 충돌은 이 절의 대체 절차를 따릅니다. 원문 코드 예시를 현재 작업 대상으로 자동 실행하지 않습니다.

- 시스템·개발자·관리 정책과 현재 권한 안에서 **사용자 명시 지시 > 적용 저장소 지침(AGENTS.md 등) > 개인 스킬 범용 기본값** 순으로 적용합니다. `>`의 왼쪽이 강한 규칙입니다. 사용자 지시도 상위 정책이나 실제 권한을 변경하지 않습니다.
- 저장소 지침은 고유 규칙, 개인 스킬은 범용 규약입니다. 이미 주어진 승인과 사용자 범위를 유지합니다. 권한 없는 동작은 바로 전 단계에서 확인하고, 경로가 존재한다는 이유로 다른 저장소·개인 홈·운영 환경을 수정하지 않습니다.
- 이 폴더 전체를 복사하면 지침·필수 참조를 사용할 수 있습니다. 중앙 catalog·manifest·설치기·30/31 저장소·다른 설치 스킬은 필요하지 않습니다. 다른 스킬 참조는 아래 로컬 사본을 읽습니다. 현재 작업에 필요한 참조만 읽고 순환 참조를 반복해서 읽지 않습니다.
- `skill://`·`file://~/.kiro`와 고정 `/root/...` 경로는 원문 환경의 별칭·예시입니다. `skill://`는 아래 대응으로 해석하며 Kiro URI 도구를 호출하지 않습니다. 출력 알림 문자열의 URI는 그대로 표시할 수 있습니다. 대상 파일/저장소 경로는 현재 요청의 실제 대상으로 확인합니다.
- 검증은 실행 목적·관찰·다음 조치와 함께 **통과 / 부분 검사 / 실패 / 미실행**을 구분합니다. 원문의 과거 완료·disabled 상태를 현재 관찰로 재사용하지 않습니다.

- 원문의 전체 Bash 템플릿·로깅·오류 처리 예시를 유지합니다. 사용자의 대상 OS·셸·저장소 규칙에 맞춰 적용하고 범위 밖 시스템 설정을 추가하지 않습니다. 설명의 skill:// 표시는 참조 알림 문자열이며 URI 접근 호출이 아닙니다.
- 원문의 복잡도 표로 간단/보통/복잡을 선택하고 간단한 단일 작업에는 무로깅 함수 예외를 유지합니다. 생성 후 원문의 헤더(작성자·작성일·날짜 버전·한 줄 설명)·입력 인용·오류 종료·복잡도에 맞는 로깅·번호를 대조합니다. 실제 작성자/날짜는 현재 대상 기준입니다.
- `/var/log`·`/backup` 등의 시스템 로그/백업 경로는 자동 생성하지 않습니다. 필요한 보통/복잡 작업에는 사용자가 허용한 작업 경로를 사용하고, stdout 데이터와 로그를 분리합니다. eval 예시는 외부 입력을 전달하지 않으며 인자 배열 실행을 우선합니다.

### Bash 실패 전파 보완

아래 원문의 `run_msg_info`와 문자열 호출 예시는 비교를 위해 보존합니다. 새 스크립트에서는 다음 함수를 적용하고, 호출부도 `번호 명령 인수...`로 바꿉니다. 셸 명령 문자열을 `eval`로 해석하지 않으며 공백·셸 기호가 든 인수도 인용하여 그대로 전달합니다.

명령을 `if` 안에서 실행하여 `set -e` 유무와 관계없이 종료 상태를 먼저 기록합니다. 로그는 stderr로 보내고 명령의 stdout은 유지하며, 원래 실패 상태를 반환합니다. 필수 단계의 호출부는 `|| exit "$?"`로 종료하여 다음 단계를 실행하지 않습니다. 함수 내부의 복합 작업도 실패를 명시적으로 반환해야 하며 `set -e`만으로 내부 실패 감지를 보장하지 않습니다.

```bash
run_msg_info() {
    if [ "$#" -lt 2 ]; then
        printf 'run_msg_info: number and command required\n' >&2
        return 2
    fi
    local info_code=$1
    shift
    local status

    if "$@"; then
        status=0
    else
        status=$?
    fi
    if [ "$status" -eq 0 ]; then
        printf '%s sj_scripts [info] code:%s success.\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$info_code" >&2
    else
        printf '%s sj_scripts [error] code:%s failed with status %s.\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$info_code" "$status" >&2
    fi
    return "$status"
}

# 실제 대상은 현재 요청 범위에서 정합니다. 아래는 출력만 하는 예시입니다.
run_msg_info 1 printf '%s\n' 'argument with spaces' || exit "$?"
```

원문 비교 자료: [Kiro 원문](references/kiro-original.md). 비교용 원문 파일은 실행 지시로 다시 로드하지 않습니다.
<!-- CODEX-COMPAT-END -->


## 기존 스크립트 패턴 참고 (sj_del)

실제 운영 스크립트에서 사용된 패턴입니다. 새 스크립트 작성 시 일관성을 유지합니다.

### 헤더 주석

```bash
#!/bin/bash
#### This script was created by sjyun on YYYY-MM-DD. version YY.MM.DD. Modified by sjyun on YYYY-MM-DD.
#### 스크립트 한 줄 설명
```

### 에러 처리 인라인 패턴

```bash
# 기존 패턴 (jenkins 스타일)
apt-get install jenkins -y || { echo "#### filed error code : $? ####" ; exit 1; }

# 로그 함수 적용 패턴
apt-get install jenkins -y || { log_msg_error 1 "jenkins install failed" ; exit 1; }
```

### 파일/디렉토리 존재 체크

```bash
if [ ! -f "/path/to/file" ]; then exit 1; fi
if [ ! -d "/path/to/dir" ]; then mkdir -p /path/to/dir; fi
```

### OS 버전 체크

```bash
version_id=$(grep -i version_ID /etc/os-release | awk -F '"' '{print $(NF-1)}')
if [ "$version_id" = "20.04" ]; then
    echo "20.04 OK"
else
    echo "failed"; exit 1
fi
```

---

## 로그 레벨 인라인 패턴

명령어 한 줄에 에러 처리를 붙이는 패턴입니다.

```bash
echo "test01" || { echo "$(date '+%Y%m%d-%H:%M:%S') - sj_scripts [info]:    sj_scripts-end. check. ---- error ----"   ; exit 1; }
echo "test02" || { echo "$(date '+%Y%m%d-%H:%M:%S') - sj_scripts [success]: sj_scripts-end. check. ---- success ----" ; exit 1; }
echo "test03" || { echo "$(date '+%Y%m%d-%H:%M:%S') - sj_scripts [error01]: sj_scripts-end. check. ---- error01 ----" ; exit 1; }
echo "test04" || { echo "$(date '+%Y%m%d-%H:%M:%S') - sj_scripts [failed]:  sj_scripts-end. check. ---- failed ----"  ; exit 1; }
```

---

## 표준 함수 기반 템플릿

```bash
#!/bin/bash
#### This script was created by sjyun on YYYY-MM-DD. version YY.MM.DD.
#### 스크립트 한 줄 설명
#
# 허용 도메인:
#   domain.com - 용도

# ── 변수 ───────────────────────────────────────────────────
DATE=$(date +%Y%m%d_%H%M%S)                        # 타임스탬프 (백업 중복 방지)
LOG_FILE01="/var/log/$(basename "$0" .sh).log"      # 스크립트명 기반 자동 지정
# LOG_FILE01="/var/log/rsync-backup-transfer.log"   # 직접 지정 시 위 줄 대체

BK_DIR="/backup/ORG"
backup_status_log_dir="/var/log/sj_scripts"

# ── 로그 디렉토리 초기화 ───────────────────────────────────
mkdir -p "$(dirname "${LOG_FILE01}")"
mkdir -p "${backup_status_log_dir}"
exec >> "${LOG_FILE01}" 2>&1

# ── 로깅 함수 ──────────────────────────────────────────────

# 명령어 실행 + 성공/실패 자동 로그
# 🟡 eval 사용 — 외부 입력값 직접 전달 금지, 스크립트 내부 명령어만 허용
run_msg_info() {
    local info_code=$1
    local info_msg=$2
    local status

    eval "${info_msg}"   # 따옴표로 word splitting 방지
    status=$?            # local 선언 전에 $? 저장 (local이 $?를 덮어쓰는 문제 방지)

    if [ "${status}" -eq 0 ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') sj_scripts [info] code:${info_code} success. ${info_msg}"
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') sj_scripts [error] code:${info_code} failed with status ${status}. ${info_msg}"
    fi
}

# 단순 메시지 로그 (명령어 실행 없음)
log_msg_info() {
    local info_code=$1
    local info_msg=$2

    echo "$(date '+%Y-%m-%d %H:%M:%S') sj_scripts [info] code:${info_code} ${info_msg}"
}

# 에러 기록 + status 파일 저장 (exit는 호출부에서 결정)
log_msg_error() {
    local err_code=$1
    local err_msg=$2

    echo "$(date '+%Y-%m-%d %H:%M:%S') sj_scripts [error] code:${err_code} ${err_msg}"

    if [ -n "${backup_status_log_dir:-}" ]; then
        echo "${err_code}" > "${backup_status_log_dir}/backup.status"
    fi
## exit "${err_code}";
}

# ── 설정 파일 백업 함수 ────────────────────────────────────
# 타임스탬프 포함으로 같은 날 중복 실행 시 덮어쓰기 방지
backup_conf() {
    local conf_file=$1
    if [ -f "${conf_file}" ]; then
        cp -a "${conf_file}" "${conf_file}_ORG_${DATE}"
        log_msg_info 0 "backup: ${conf_file}_ORG_${DATE}"
    else
        log_msg_info 0 "${conf_file} not exists. skip backup."
    fi
}

# ── 서비스 시작 함수 ───────────────────────────────────────
# OS init 시스템 자동 감지 (systemd / sysvinit / 없음)
service_start() {
    local svc=$1

    if command -v systemctl > /dev/null 2>&1; then
        systemctl daemon-reload
        systemctl enable "${svc}" || { log_msg_error 11 "${svc} enable failed" ; return 1; }
        systemctl restart "${svc}" || { log_msg_error 12 "${svc} restart failed" ; return 1; }
        systemctl status "${svc}" --no-pager || true
    elif command -v service > /dev/null 2>&1; then
        service "${svc}" restart || { log_msg_error 12 "${svc} restart failed" ; return 1; }
    else
        log_msg_error 10 "no init system found"
        return 1
    fi
    log_msg_info 0 "${svc} started"
}

# ── 디렉토리 생성 함수 ─────────────────────────────────────
ensure_dir() {
    local dir=$1
    local owner=${2:-root}
    if [ ! -d "${dir}" ]; then
        mkdir -p "${dir}"
        chown "${owner}" -R "${dir}"
        log_msg_info 0 "created: ${dir} (owner: ${owner})"
    fi
}

# ── 메인 ───────────────────────────────────────────────────
main() {
    log_msg_info 1 "script start"

    ensure_dir "${BK_DIR}"

    # 작업 내용
    # apt-get install -y package || { log_msg_error 1 "package install failed" ; exit 1; }
    # backup_conf /etc/service/service.conf
    # service_start service-name

    log_msg_info 99 "script end"
}

main "$@"
```

---

## 함수 사용 예시

```bash
# 명령어 실행 + 결과 자동 로그
run_msg_info 1 "apt-get install -y nginx"
run_msg_info 2 "systemctl restart nginx"

# 단순 메시지 로그
log_msg_info 1 "script start"
log_msg_info 2 "config updated"

# 에러 기록 후 exit (호출부에서 결정)
log_msg_error 1 "nginx install failed" ; exit 1

# 설정 파일 백업 (타임스탬프 포함)
backup_conf /etc/elasticsearch/elasticsearch.yml
backup_conf /etc/kibana/kibana.yml

# 서비스 시작
service_start elasticsearch
service_start kibana

# 디렉토리 생성 (소유자 지정)
ensure_dir /masang_vol1/mdf mssql:mssql
ensure_dir /backup/data
```

---

## 적용 규칙

- 반복되는 패턴(백업, 서비스 시작, 디렉토리 생성)은 함수로 추출
- `log_msg_error` 후 exit 여부는 호출부에서 결정 (`; exit N` 명시)
- `eval` 사용 시 반드시 따옴표 감싸기 (`eval "${cmd}"`), 외부 입력값 전달 금지
- `$?` 는 `local` 선언 전에 저장 (`local` 자체가 exit code 0을 반환하므로 덮어씀)
- `DATE`에 시분초 포함 → 같은 날 중복 백업 시 덮어쓰기 방지
- `backup_status_log_dir` 미정의 시 `log_msg_error`가 빈 경로에 쓰지 않도록 `${var:-}` 가드
- `systemctl enable` 실패도 에러 처리
- `main()` 함수로 진입점 통일, 함수 정의 후 마지막에 호출

## `main()` 함수 구조 규칙

- 단일 작업 스크립트: `main()` 하나로 충분 (굳이 분리하지 않음)
- 복합 작업 스크립트 (ELK 등 여러 서비스): `install_elasticsearch()`, `install_kibana()` 등 분리
- `main()`으로 감싸는 이유:
  - 로깅 함수가 `main` 호출 전에 정의되어야 하므로 순서 보장
  - `exec >>` 리다이렉트 후 실행 흐름 명확화
  - 나중에 함수 분리 시 구조 변경 없이 확장 가능
- `main "$@"` — 인수 없어도 습관적으로 사용 (향후 인수 추가 시 수정 불필요)

## 스크립트 복잡도 기준

| 복잡도 | 기준                                        | 로깅 함수                       | 구조                          |
|--------|---------------------------------------------|---------------------------------|-------------------------------|
| 간단   | 100줄 이하 또는 단일 패키지 설치            | 사용하지 않음                   | 인라인 `echo` + `\|\| exit`   |
| 보통   | 100~150줄 또는 여러 단계, 설정 변경 포함    | `run_msg_info` / `log_msg_info` | `main()`                      |
| 복잡   | 151줄 이상 또는 여러 서비스, 백업/롤백 필요 | 전체 함수 사용                  | `main()` + 서비스별 함수 분리 |

### 간단한 스크립트 예시 (로깅 함수 없음)

```bash
#!/bin/bash
#### This script was created by sjyun on YYYY-MM-DD. version YY.MM.DD.
#### Python 3.9 설치 — Ubuntu 20.04
#
# 허용 도메인:
#   archive.ubuntu.com

apt-get update -qq
apt-get install -y python3.9 || { echo "#### filed error code : $? ####" ; exit 1; }

if [[ ! -e /usr/local/bin/python3 ]]; then
    ln -s /usr/bin/python3.9 /usr/local/bin/python3
fi

echo "done: $(python3.9 --version)"
```

## 에러 코드 규칙 (순차 번호)

| 방식                 | 설명                                     |
|----------------------|------------------------------------------|
| 순차 (1, 2, 3, 4...) | 로그에서 빠진 번호로 실패 지점 즉시 파악 |

```bash
run_msg_info 1 "apt-get update -y"
run_msg_info 2 "apt-get install -y curl gnupg2"
run_msg_info 3 "apt-get install -y elasticsearch"
run_msg_info 4 "systemctl enable elasticsearch"
run_msg_info 5 "systemctl restart elasticsearch"
run_msg_info 6 "apt-get install -y kibana"
run_msg_info 7 "systemctl enable kibana"
run_msg_info 8 "systemctl restart kibana"
```

로그 확인:
```
code:1 success.
code:2 success.
code:3 success.
code:4 success.
code:6 success.   ← 5가 없음 → elasticsearch restart 실패
```

- `backup.status` 파일에 마지막 에러 코드 기록 → `cat backup.status`로 즉시 확인
- `0` = 정상, 그 외 = 해당 번호 단계에서 실패
- exit code는 0~255 제한 (bash), `backup.status`는 문자열이므로 제한 없음
- 스크립트 수정 시 번호 재정렬 필요 — 주석으로 번호-작업 매핑 유지 권장
