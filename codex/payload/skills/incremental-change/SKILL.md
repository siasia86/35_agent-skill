---
name: incremental-change
description: Execute an authorized infrastructure change plan with observable checkpoints and recovery conditions.
---

# Incremental change

Start from the confirmed current state and split the work into independently verifiable, reversible steps. Reuse the plan’s scope, expected change, validation, failure signal, recovery, and authorization; add missing details only for the current step. Prefer IaC and dry-run/plan modes when the project supports them.

After each authorized step, compare observed state with the expectation before continuing. Stop on unexpected output, broadened blast radius, missing backup, or failed validation; preserve evidence and switch to diagnosis. Never turn a proposed sequence into deployment authority. Finish with changed files/resources, validations, rollback status, and remaining follow-up.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
