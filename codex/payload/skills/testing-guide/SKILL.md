---
name: testing-guide
description: Design tests using behavior, error paths, boundaries, equivalence classes, and relevant operational edge cases.
---

# Testing guide

Start from requirements and the changed behavior. Distinguish running existing tests from authoring new test code; use the personal explicit-request default unless applicable repository policy requires test changes. When test authoring is in scope, use arrange-act-assert with happy path, invalid/empty input, exceptions, boundaries, equivalence classes and defect regressions. Mock external systems at the boundary, not pure business logic, and keep tests isolated and repeatable.

For infrastructure or scripts, select safe validation such as syntax, lint, dry-run, idempotency checks, and controlled health checks based on available tools. Consider environment, state, time/concurrency, and resource exhaustion where relevant. Do not assert arbitrary coverage targets or claim a live verification occurred without evidence.

For container-related changes, consider Dockerfile lint, image build, container health/startup, Compose configuration, and intended port exposure. A build or container start can execute code, use a daemon, download dependencies, or publish ports: perform these only in an authorized isolated environment. Separate static lint/configuration checks from actual build, health, and connectivity results, and report skipped checks.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
