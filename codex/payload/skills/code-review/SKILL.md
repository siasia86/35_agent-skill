---
name: code-review
description: Review code, scripts, and IaC for correctness, security, reliability, maintainability, and missing tests.
---

# Code review

Establish the requested scope and inspect the actual diff and relevant context. Prioritize concrete defects: incorrect boundaries and error paths, secrets and injection, authorization and input validation, resource cleanup, concurrency, compatibility, and regressions. For IaC, also inspect least privilege, public exposure, encryption, lifecycle risks, state drift, and idempotency. For shell, inspect quoting, input validation, temporary files, cleanup, and privilege use.

Assess whether tests cover normal, error, boundary, and changed behavior; do not claim a test ran unless it did. Report only actionable findings, ordered by severity, with `file:line`, evidence, impact, and a specific remedy. Separate optional style suggestions from defects and say explicitly when no findings were found.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
