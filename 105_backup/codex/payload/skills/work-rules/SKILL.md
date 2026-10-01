---
name: work-rules
description: Apply explicitly selected personal engineering conventions for document editing, data changes, or infrastructure operations.
---

# Work rules

Use when the user or repository selects these personal conventions. Reuse applicable AGENTS and policy already read in this session. Choose only the reference or references relevant to the current work:

- Data replacement, code changes, or shared working trees: [operating rules](references/operating-rules.md).
- Markdown editing or technical documentation: [documentation rules](references/documentation.md).
- Infrastructure, remote execution, Windows, or VM changes: [infrastructure rules](references/infrastructure.md).

For a selected personal script layout, use the available python-script-template or bash-script-template skill. Otherwise follow the project's existing conventions. A small edit does not require every reference or a new PLAN/TODO file.

Keep credentials and private keys out of commands, source, logs, examples, and work records; use clearly fictional placeholders in documentation. Do not automatically add broad secret-scanner allowlists for examples; inspect a false positive and use only a reviewed, narrowly scoped exception when needed. Redact scanner output before including findings in work records.

Current user scope and valid authorization govern execution. Apply repository-selected conventions and preserve user changes; these references do not grant extra permissions.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
