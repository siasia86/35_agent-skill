# Personal operating rules

## 1. Data changes and recovery

Before destructive replacements, identify concrete targets, expected impact, and applicable authorization. Reuse valid authorization for that scope. Preserve originals through the project's backup, version-control, or reversible workflow where appropriate.

Detect zero-match transformations. Inspect changed lines and related references, and validate output before replacing the original. Use safe temporary files and retain required metadata. Repeated application must not silently duplicate changes or overwrite recovery material. For shared values, inventory the affected references before replacement and check for stale references afterward within the requested scope. Do not print sensitive values while proving the replacement or overwrite concurrent user edits.

## 2. Verification and coordination

Distinguish running existing checks from writing tests. The personal default is to write or change test code when explicitly requested, unless applicable repository policy requires it. Choose existing checks proportionate to the change and report missing coverage and unrun checks.

Follow an existing repository coordination or lock protocol. Do not invent global locks, remove another worker's lock, or assume the original Kiro pre-tool hook is active. Its Codex runtime equivalence remains unverified.

If an operation stalls or repeatedly fails without new evidence, diagnose before retrying. Identify ownership before killing processes, restarting services, or cleaning another worker's resources. Keep long-running commands observable through separate status calls, choose operation-appropriate timeouts, and inspect logs and partial state after interruption. A timeout does not prove the operation stopped or rolled back; do not blindly rerun a state-changing command or kill processes by a broad name match. On interruption, retain the acquired state and the next safe action. Permission failures require distinguishing OS access from sandbox policy; do not automatically use sudo, chmod, or chown to bypass them.

## 3. Work records

Use the repository's existing record locations. For a non-trivial investigation, record symptom, cause, resolution, verification, and remaining work promptly after resolution, and link from the task index. Update an existing matching issue instead of duplicating it; do not create a recursive issue merely for editing the record itself. Do not create persistent memory or extra record files merely because an operation has multiple steps. Batch size and review count follow explicit requirements and meaningful progress.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
