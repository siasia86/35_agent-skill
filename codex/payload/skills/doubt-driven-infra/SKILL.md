---
name: doubt-driven-infra
description: Challenge risky infrastructure changes before approval by testing assumptions, blast radius, rollback, and operational evidence.
---

# Doubt-driven infrastructure

Use for production, irreversible, security-sensitive, or poorly understood infrastructure changes. State assumptions and actively seek disconfirming evidence: target identity, current state, dependency graph, privileges, data effects, availability impact, monitoring coverage, cost, and rollback feasibility.

Classify risks and gates. Require explicit authorization for apply, deployment, credential changes, destructive actions, and any action outside the user’s scope. Prefer plan, diff, policy check, or isolated test over live mutation. A rollback plan must name its trigger, owner, prerequisites, and limitations; when rollback is unsafe, say so and propose a forward-fix path. Produce a go/no-go recommendation with evidence and unresolved questions.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
