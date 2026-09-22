---
name: spec-driven-infra
description: Define an evidence-based infrastructure specification before significant, multi-service, production, or ambiguous changes.
---

# Spec-driven infrastructure

Use for significant infrastructure work, not a clearly scoped trivial edit. Document objective, current and target state, assumptions, affected systems, interfaces, resource and network design, identity and secret handling, observability, cost, blast radius, dependencies, rollout, rollback/forward-fix limits, success criteria, and unresolved decisions.

For Ansible, include target grouping, supported platforms, privilege model, idempotency, secret management, test/dry-run plan, and rollback. For Terraform or other IaC, include state and provider constraints without embedding real credentials or user key paths. Review and resolve material assumptions before implementation; changes to scope update the specification. The specification does not authorize apply or deployment.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
