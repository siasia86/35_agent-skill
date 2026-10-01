---
name: security-audit
description: Audit code, configuration, and IaC for security risks using repository evidence and safe, non-destructive checks.
---

# Security audit

Define scope and threat context. Inspect for secrets, unsafe data exposure, injection, authentication and authorization gaps, excessive privilege, insecure network exposure, missing encryption, unsafe defaults, dependency risk, logging gaps, and destructive recovery paths. Use available repository scanners only when authorized and report tool availability honestly.

Rank findings by impact and exploitability. For every finding include `file:line` or other evidence, affected asset, impact, remediation, and verification. Do not expose discovered secrets in output; redact them and recommend rotation through the authorized process. This skill audits; it does not grant permission to scan external systems or change security controls.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
