---
name: kiro-lock
description: Coordinate concurrent edits with a repository-approved lock protocol; do not assume a Kiro hook or lock-file format exists.
---

# Concurrent-edit coordination

Before changing a shared working tree, inspect repository guidance for a supported ownership or lock protocol. If one exists, follow it and verify that it covers the intended files; if not, do not invent a global lock or assume a Kiro hook is installed. Coordinate with the user or active collaborators when ownership conflicts.

Record or release a lock only under the repository’s documented procedure and only after confirming ownership and recovery behavior. Do not delete another worker’s lock. On interruption, report the acquired state and the safe handoff or cleanup required. Runtime hook installation or activation is outside this skill.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
