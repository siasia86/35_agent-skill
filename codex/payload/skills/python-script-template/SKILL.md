---
name: python-script-template
description: Create standalone Python CLI utilities using the personal template when selected, while following the target project’s existing layout and version conventions.
---

# Python script template

Use this skill for a new or materially revised Python command-line script. Read applicable repository guidance first; its explicit conventions take precedence over this template. Preserve a project’s established package layout when editing an existing program.

## Personal standalone template

Select this personal layout when requested or when the project chooses it. A safety switch, date-based version, and imports after VERSION are personal conventions; preserve an existing package’s import order, version scheme, and lint requirements. For a new standalone utility using this template, use:

1. `#!/usr/bin/env python3`
2. commented safety switch
3. module docstring, including purpose and safe usage
4. `VERSION = "YY.MM.DD"` (replace with the current date-based version)
5. standard-library imports, one per line and alphabetized; third-party imports after them
6. constants, compiled patterns, and optional color settings
7. logging/configuration helpers
8. focused functions with one-line docstrings
9. `parse_args()`
10. `main()`
11. guarded entry point with `KeyboardInterrupt` exit handling

The selected personal skeleton is in [assets/standalone.py](assets/standalone.py). Read or copy it when creating a utility with this layout; adapt its arguments to the requested operation.


The safety switch is intentionally commented: it is an emergency disable mechanism, not a statement that every script must be silently disabled. Do not add import-time side effects before it. If a script needs colors, keep ANSI escape constants centralized and disable color when output is not a terminal or when the project requires it.

## CLI, validation, and configuration

- Use `argparse`, not direct `sys.argv` parsing. Provide `-h/--help`, `-V/--version`, and paired short/long flags where they improve ordinary use.
- Keep parsing in `parse_args()` and validate required files, mutually exclusive options, ranges, and configuration keys before work starts.
- Use `pathlib.Path` or clearly documented path handling; do not embed user home, service, log, lock, or repository paths.
- Parse TOML with `tomllib` on supported Python versions, and JSON with `json`; validate the schema immediately. If configuration auto-discovery is useful, require exactly one unambiguous candidate or ask the caller to choose.
- Compile reusable regular expressions at module scope. Do not repeat imports or compilation inside hot-path functions without a reason.

## Writes, logging, and failures

- Prefer `logging` over ad-hoc prints for diagnostics. Configure console logging by default; make a file destination an explicit user/project option and create it only when authorized.
- Use context managers for files. For a replacement, write a sibling temporary file, flush as appropriate, validate content, then use an atomic replace when the filesystem supports it. Never silently continue after a zero-match transformation.
- Make `--dry-run` show intended changes without writes whenever the operation can alter data. For non-reversible work, require an explicit authorization boundary and document backup/rollback.
- Design deterministic transformations so the same input and configuration produce the same output. A repeated application must not duplicate edits, append repeated markers, or replace backups unnecessarily. Verify rerun safety on isolated fixtures when authorized; if an operation is inherently non-idempotent, state that exception and provide an explicit duplicate-execution guard.
- Return or raise clear errors with useful context. Do not use bare `except`; catch expected exceptions narrowly. The entry point maps `KeyboardInterrupt` to 130 and must not hide other failures.
- Use a file lock only when concurrent execution is a real requirement, document platform limits, and release it in `finally`. Do not assume a Linux lock path or monitoring status file.

## Proportionate validation

Run `python3 -m py_compile <script>` and `<script> --help` when safe. Also run the project formatter, linter, and focused tests when available. Report commands and results, and distinguish syntax success from behavior, filesystem, external-service, or production verification that was not run.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
