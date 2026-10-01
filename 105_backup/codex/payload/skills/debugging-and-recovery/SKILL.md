---
name: debugging-and-recovery
description: Diagnose service, build, deployment, or infrastructure failures with evidence preservation, containment, recovery, and prevention.
---

# Debugging and recovery

First contain additional unintended change and preserve relevant logs, errors, timestamps, configuration state, and recent diffs. Confirm the symptom, then localize it by layer (client/network, compute, storage, identity, configuration, deployment, or dependency). Form and test hypotheses from evidence rather than applying speculative fixes.

Before a recovery action, identify target, expected impact, rollback, and required approval. Prefer the smallest reversible repair; do not restart services, change cloud resources, or delete data without authorization. After the repair, verify the original symptom, adjacent health signals, and recurrence risk. Report timeline, evidence, root cause or remaining hypotheses, action, validation, rollback status, and prevention follow-up.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
