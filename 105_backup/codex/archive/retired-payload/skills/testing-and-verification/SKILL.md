---
name: testing-and-verification
description: Select and interpret existing verification commands for a scoped change when check coverage or results need review.
---

# Testing and verification

Use this skill to select or interpret existing checks; test-case authoring follows the requested scope and repository policy. Derive checks from the changed behavior and repository guidance. Cover syntax/static checks, focused automated tests, error and boundary cases, integration or dry-run checks, and post-change observation as appropriate. For IaC, prefer validate/format/plan or check mode before any authorized apply; for scripts use available syntax/lint checks.

Do not run commands that alter production or external state just to claim verification. Record exact tests/checks, result, scope, and limitations. A green command does not prove unrelated behavior; distinguish passed, failed, skipped, unavailable, and not run. On failure, preserve evidence and diagnose before retrying.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
