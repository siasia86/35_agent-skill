---
name: ansible-review
description: Review Ansible playbooks and roles for safety, idempotency, error handling, secrets, and check-mode behavior.
---

# Ansible review

Review the requested files, or ask for a target when it is unclear. Inspect repository guidance first.

Check YAML and module syntax; deprecated or shell-heavy tasks; least-privilege `become`; idempotency; handlers; `changed_when`/`failed_when`; `block`/`rescue`; undefined variables; retries; secret redaction (`no_log`, Vault); file modes; inventory scope; and `--check` compatibility. Treat unreachable hosts, permissions, and partial failure as cases to report, not reasons to run a deployment.

Also inspect `serial`/`forks`/`async` for concurrency and load, unnecessary `gather_facts`, `delegate_to`/`run_once` execution scope, nested-loop `loop_var`, sensitive-loop labels and redaction, and `loop_control.pause` or equivalent rate limiting. Review `max_fail_percentage`, disk-full cases, missing handler notifications, `ignore_errors` follow-up, and `rescue`/`always` behavior. Verify module and loop compatibility against the installed Ansible version rather than treating every older spelling as universally deprecated. Include Vault-prefixed values, Authorization headers, and sensitive registered results in secrecy checks.

Report in Korean unless requested otherwise, using per-item ✅ / ❌ / 🟡 status where useful, severity, `file:line`, evidence, and safe correction examples. Run only available read-only or explicitly authorized validation such as `ansible-playbook --syntax-check`; state checks not run and never apply a playbook merely to review it.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
