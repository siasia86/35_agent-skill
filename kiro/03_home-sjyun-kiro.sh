#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

if [ "${EUID}" -eq 0 ] && [ -n "${SUDO_USER:-}" ] && [ "${SUDO_USER}" != root ]; then
    TARGET_USER="${SUDO_USER}"
    TARGET_HOME="$(getent passwd "${TARGET_USER}" | cut -d: -f6)"
    TARGET_GROUP="$(id -gn "${TARGET_USER}")"
else
    TARGET_USER="$(id -un)"
    TARGET_HOME="${HOME}"
    TARGET_GROUP="$(id -gn)"
fi

[ -n "${TARGET_HOME}" ] || { echo "ERROR: target home not found for ${TARGET_USER}" >&2; exit 1; }

printf -v source_path '%q' "${REPO_ROOT}/kiro/"
printf -v target_path '%q' "${TARGET_HOME}/.kiro/"
printf -v owner '%q' "${TARGET_USER}:${TARGET_GROUP}"

printf 'rsync -av %s %s --exclude=.cli_bash_history --exclude=sessions --exclude=.local --exclude="*.swp" -n && chown -R %s %s\n' \
    "${source_path}" "${target_path}" "${owner}" "${target_path}"
