# Personal operating rules

## 1. Data changes and recovery

Before destructive replacements, identify concrete targets, expected impact, and applicable authorization. Reuse valid authorization for that scope. Preserve originals through the project's backup, version-control, or reversible workflow where appropriate.

Detect zero-match transformations. Inspect changed lines and related references, and validate output before replacing the original. Use safe temporary files and retain required metadata. Repeated application must not silently duplicate changes or overwrite recovery material.

## 2. Verification and coordination

Distinguish running existing checks from writing tests. The personal default is to write or change test code when explicitly requested, unless applicable repository policy requires it. Choose existing checks proportionate to the change and report missing coverage and unrun checks.

Follow an existing repository coordination or lock protocol. Do not invent global locks, remove another worker's lock, or assume the original Kiro pre-tool hook is active. Its Codex runtime equivalence remains unverified.

If an operation stalls or repeatedly fails without new evidence, diagnose before retrying. Identify ownership before killing processes, restarting services, or cleaning another worker's resources. On interruption, retain the acquired state and the next safe action.

## 3. Work records

Use the repository's existing record locations. For a non-trivial investigation, record symptom, cause, resolution, verification, and remaining work once, and link from the task index. Do not create persistent memory or extra record files merely because an operation has multiple steps. Batch size and review count follow explicit requirements and meaningful progress.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
