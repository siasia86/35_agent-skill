---
name: bash-script-template
description: Create or improve Bash scripts with safe argument handling, errors, logging, cleanup, and proportionate validation.
---

# Bash script template

Match local conventions after reading repository guidance. Use a portable shebang, a short purpose comment, a `main "$@"` entry point, quoted expansions, validated inputs, stderr diagnostics, and meaningful nonzero statuses. Keep complexity proportionate: a short single-purpose script may use direct guarded commands; a multi-step script should separate logging, validation, backup/cleanup, and service functions.

For multi-step work, use numbered steps in diagnostics so a failed stage can be located, capture a command status before another command can overwrite `$?`, and let the caller decide whether a logged error exits. If a configuration file may be replaced, take an explicitly named, timestamped backup only when the target project authorizes it. Use `mktemp` plus a cleanup trap for temporary resources. Check whether a service manager exists before suggesting service actions; never bake in a service, owner, package manager, log path, or host.

Avoid `eval`. A narrowly controlled internal command-string use must be justified, quoted, and must never receive external input; prefer arrays or direct function calls. Use `set -euo pipefail` only after considering expected nonzero commands, and handle those commands explicitly. Destructive, privileged, remote, install, restart, and network operations remain subject to current authorization.

Validate with `bash -n` and, when available and suitable, ShellCheck. Report commands run, their result, and any environment-specific validation left to the target project.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
