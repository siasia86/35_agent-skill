---
name: security-tools
description: Select and run available security checks or data-masking tools without assuming private scripts, configurations, or credentials exist.
---

# Security tools

First identify the requested objective: source secret scan, dependency scan, IaC policy review, log redaction, or data masking. Inspect repository guidance and installed tooling; do not rely on private paths or silently substitute a destructive tool. Confirm target scope, exclusions, backup needs, and whether a scan or transformation is authorized.

Prefer read-only scans. For masking or other writes, use copies or dry-run modes when available, preserve original data, validate output, and never claim reversibility without proof. Exclude credentials and unrelated private directories only through an explicit, reviewable scope. Report tool/version, command category, target, findings summary, redactions, and checks not available.

For reversible masking, preserve the mapping files after restoration and protect them as sensitive data. Verify source identity using the tool's documented hash/serial metadata before restoring; do not force past a mismatch. Back up a map before overwriting it, retain source modes and required metadata, and use validated temporary-file replacement only within the authorized scope. Repeated masking should add no further changes. Verify mask → restore round-trip and compatibility with existing maps in an isolated copy. Keep any emergency safety switch available and restore its original state after testing. Do not claim a replacement tool supports the original resource types, placeholders, map schema, or exclusion rules without checking those contracts.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
