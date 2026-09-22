---
name: incremental-change
description: Implement infrastructure or operational changes in small reversible steps with validation and rollback checkpoints.
---

# Incremental change

Start from the confirmed current state and split the work into independently verifiable, reversible steps. For each step define scope, expected change, validation, failure signal, rollback, and authorization required. Prefer IaC and dry-run/plan modes when the project supports them.

After each authorized step, compare observed state with the expectation before continuing. Stop on unexpected output, broadened blast radius, missing backup, or failed validation; preserve evidence and switch to diagnosis. Never turn a proposed sequence into deployment authority. Finish with changed files/resources, validations, rollback status, and remaining follow-up.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
