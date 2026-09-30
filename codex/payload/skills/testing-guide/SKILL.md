---
name: testing-guide
description: Select verification checks or design test cases for requested testing and coverage review.
---

# Testing guide

Start from requirements and the changed behavior. Distinguish running existing tests from authoring new test code; use the personal explicit-request default unless applicable repository policy requires test changes. When test authoring is in scope, use arrange-act-assert with happy path, invalid/empty input, exceptions, boundaries, equivalence classes and defect regressions. Mock external systems at the boundary, not pure business logic, and keep tests isolated and repeatable.

For verification, derive proportionate existing checks from the changed behavior. Report commands, coverage, failures, missing tools, and unrun checks; a passing command does not establish unrelated behavior. Use IaC validate/format/plan or check mode before an authorized apply. Do not change production state merely to obtain test evidence.

For infrastructure or scripts, select safe validation such as syntax, lint, dry-run, idempotency checks, and controlled health checks based on available tools. Consider environment, state, time/concurrency, and resource exhaustion where relevant. Do not assert arbitrary coverage targets or claim a live verification occurred without evidence.

For container-related changes, consider Dockerfile lint, image build, container health/startup, Compose configuration, and intended port exposure. A build or container start can execute code, use a daemon, download dependencies, or publish ports: perform these only in an authorized isolated environment. Separate static lint/configuration checks from actual build, health, and connectivity results, and report skipped checks.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
