#!/usr/bin/env bash
#### This template was created on 2026-10-03. version 26.10.03.
#### Bash 업무 템플릿 — Git Bash/WSL, 명시한 작업만 실행하고 실패를 전파합니다.
# 허용 도메인: 현재 업무가 정한 실제 대상만. 기본 네트워크/설치 작업 없음.
# 원문 helper 순서와 백업/서비스/디렉터리 역할을 유지합니다.

# ── 변수 ───────────────────────────────────────────────────
VERSION='26.10.03'
DATE=$(date +%Y%m%d_%H%M%S)
LOG_FILE01=${LOG_FILE01:-}                 # 사용자가 허용한 로그 파일만
BK_DIR=${BK_DIR:-}                         # 작업 전용 백업 루트(선택)
backup_status_log_dir=${backup_status_log_dir:-}
DRY_RUN=0

# ── 로그 디렉터리 초기화 ───────────────────────────────────
init_logging() {
    if [ -n "$LOG_FILE01" ]; then
        mkdir -p -- "$(dirname -- "$LOG_FILE01")" || return "$?"
        : >> "$LOG_FILE01" || return "$?"
    fi
    if [ -n "$backup_status_log_dir" ]; then
        mkdir -p -- "$backup_status_log_dir" || return "$?"
    fi
    # stdout은 업무 데이터용으로 유지합니다. 전역 exec 리다이렉트 없음.
}

# ── 로깅 함수 ──────────────────────────────────────────────
run_msg_info() {
    if [ "$#" -lt 2 ]; then
        printf 'run_msg_info: number and command required\n' >&2
        return 2
    fi
    local info_code=$1
    shift
    local status
    if "$@"; then status=0; else status=$?; fi
    if [ "$status" -eq 0 ]; then
        log_msg_info "$info_code" 'success.' || return "$?"
    else
        log_msg_error "$info_code" "failed with status $status." || :
    fi
    return "$status"
}

log_msg_info() {
    local info_code=$1
    local info_msg=$2
    local line
    line="$(date '+%Y-%m-%d %H:%M:%S') sj_scripts [info] code:${info_code} ${info_msg}"
    printf '%s\n' "$line" >&2 || return "$?"
    if [ -n "$LOG_FILE01" ]; then
        printf '%s\n' "$line" >> "$LOG_FILE01" || return "$?"
    fi
    return 0
}

log_msg_error() {
    local err_code=$1
    local err_msg=$2
    local line
    line="$(date '+%Y-%m-%d %H:%M:%S') sj_scripts [error] code:${err_code} ${err_msg}"
    printf '%s\n' "$line" >&2 || return "$?"
    if [ -n "$LOG_FILE01" ]; then
        printf '%s\n' "$line" >> "$LOG_FILE01" || return "$?"
    fi
    if [ -n "$backup_status_log_dir" ]; then
        printf '%s\n' "$err_code" > "$backup_status_log_dir/backup.status" || return "$?"
    fi
    # exit 여부는 호출부에서 결정합니다.
    return 0
}

# ── 설정 파일 백업 함수 ────────────────────────────────────
backup_conf() (
    # A subshell keeps this cleanup trap out of the caller's trap policy.
    local conf_file=$1
    local backup_file="${conf_file}_ORG_${DATE}"
    local stage_dir=''
    local status
    if [ ! -f "$conf_file" ]; then
        log_msg_info 0 "$conf_file not exists. skip backup."
        return "$?"
    fi
    if [ -e "$backup_file" ] || [ -L "$backup_file" ]; then
        log_msg_error 1 'backup target already exists; refusing overwrite' || :
        return 1
    fi
    if [ "$DRY_RUN" -eq 1 ]; then
        log_msg_info 0 "[dry-run] would backup: $conf_file -> $backup_file"
        return "$?"
    fi
    # GNU ln -T publishes without replacing an existing file/directory/link.
    # Same-filesystem hard links must be supported; never fall back to overwrite.
    # The payload is an independent cp -a snapshot, not a link to the live source.
    trap 'if [ -n "$stage_dir" ]; then rm -f -- "$stage_dir/payload"; rmdir -- "$stage_dir"; fi' EXIT
    trap 'exit 130' INT
    trap 'exit 143' TERM
    if stage_dir=$(mktemp -d -- "${backup_file}.stage.XXXXXXXX"); then :; else
        status=$?
        log_msg_error 1 "backup staging failed with status $status" || :
        return "$status"
    fi
    if cp -a -- "$conf_file" "$stage_dir/payload"; then :; else
        status=$?
        log_msg_error 1 "backup copy failed with status $status" || :
        return "$status"
    fi
    if ln -T -- "$stage_dir/payload" "$backup_file"; then
        log_msg_info 0 "backup: $backup_file"
        return "$?"
    else
        status=$?
        log_msg_error 1 "backup publication failed with status $status; destination preserved" || :
        return "$status"
    fi
)

# ── 서비스 시작 함수 ───────────────────────────────────────
service_start() {
    local svc=$1
    local status
    case "$(uname -s)" in
        MINGW*|MSYS*|CYGWIN*)
            log_msg_error 10 'Linux init is unsupported in Git Bash; use native PowerShell for Windows service work' || :
            return 2 ;;
    esac
    if [ "$DRY_RUN" -eq 1 ]; then
        log_msg_info 0 "[dry-run] would enable/restart POSIX service: $svc"
        return "$?"
    fi
    if command -v systemctl >/dev/null 2>&1; then
        if systemctl daemon-reload; then :; else
            status=$?; log_msg_error 10 'daemon-reload failed' || :; return "$status"
        fi
        if systemctl enable "$svc"; then :; else
            status=$?; log_msg_error 11 "$svc enable failed" || :; return "$status"
        fi
        if systemctl restart "$svc"; then :; else
            status=$?; log_msg_error 12 "$svc restart failed" || :; return "$status"
        fi
        if systemctl status "$svc" --no-pager; then :; else
            status=$?; log_msg_error 13 "$svc status failed" || :; return "$status"
        fi
    elif command -v service >/dev/null 2>&1; then
        if service "$svc" restart; then :; else
            status=$?; log_msg_error 12 "$svc restart failed" || :; return "$status"
        fi
    else
        log_msg_error 10 'no init system found' || :
        return 1
    fi
    log_msg_info 0 "$svc started"
}

# ── 디렉터리 생성 함수 ─────────────────────────────────────
ensure_dir() {
    local dir=$1
    local owner=${2:-}  # Windows에 root/chown을 자동 적용하지 않습니다.
    local status
    if [ -n "$owner" ]; then
        case "$(uname -s)" in
            MINGW*|MSYS*|CYGWIN*) log_msg_error 2 'POSIX owner unsupported in Git Bash' || :; return 2 ;;
        esac
    fi
    if [ -d "$dir" ]; then return 0; fi
    if [ "$DRY_RUN" -eq 1 ]; then
        log_msg_info 0 "[dry-run] would create: $dir"
        return "$?"
    fi
    if mkdir -p -- "$dir"; then :; else
        status=$?; log_msg_error 2 'directory creation failed' || :; return "$status"
    fi
    if [ -n "$owner" ]; then
        if chown "$owner" -- "$dir"; then :; else
            status=$?; log_msg_error 2 'owner change failed' || :; return "$status"
        fi
    fi
    log_msg_info 0 "created: $dir${owner:+ (owner: $owner)}"
}

# ── 메인 ───────────────────────────────────────────────────
show_help() {
    printf '%s\n' \
        'Usage: script_template.sh [--dry-run] ACTION' \
        'Actions: --backup FILE | --ensure-dir DIR [--owner USER] | --service NAME' \
        'Options: --help | --version; default no args shows help only' \
        'Action/owner values must be nonempty and not another option; use ./--name for literal leading-dash paths.' \
        'Optional caller-selected LOG_FILE01 and backup_status_log_dir enable file logs.' \
        'No automatic package installation, service restart, ownership or system log creation.'
}

main() {
    local action=''
    local target=''
    local owner=''
    while [ "$#" -gt 0 ]; do
        case "$1" in
            -h|--help) show_help; return 0 ;;
            -V|--version) printf '%s\n' "$VERSION"; return 0 ;;
            -d|--dry-run) DRY_RUN=1; shift ;;
            --backup|--ensure-dir|--service)
                if [ "$#" -lt 2 ] || [ -n "$action" ] || [ -z "$2" ] || [[ "$2" == -* ]]; then show_help >&2; return 2; fi
                action=$1; target=$2; shift 2 ;;
            --owner)
                if [ "$#" -lt 2 ] || [ -z "$2" ] || [[ "$2" == -* ]]; then show_help >&2; return 2; fi
                owner=$2; shift 2 ;;
            *) show_help >&2; return 2 ;;
        esac
    done
    if [ -z "$action" ]; then show_help; return 0; fi
    if [ -n "$owner" ] && [ "$action" != '--ensure-dir' ]; then show_help >&2; return 2; fi
    if [ "$DRY_RUN" -eq 0 ]; then init_logging || return "$?"; fi
    log_msg_info 1 'script start' || return "$?"
    case "$action" in
        --backup) run_msg_info 2 backup_conf "$target" || return "$?" ;;
        --ensure-dir) run_msg_info 2 ensure_dir "$target" "$owner" || return "$?" ;;
        --service) run_msg_info 2 service_start "$target" || return "$?" ;;
    esac
    log_msg_info 99 'script end'
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    main "$@"
    exit "$?"
fi
