---
name: repo-governance
description: Discover repository guidance when no governance binding is configured, or audit missing and conflicting guidance. Use governance-repository for an existing central binding.
---

# Repository governance

Use this discovery workflow when a repository has no configured governance binding or when auditing its guidance. If a governance-repository binding is present, read its selected local policy references and use this skill only to resolve missing or conflicting discovery. Before substantial work, locate applicable `AGENTS.md` and repository-local governance/configuration documents from the working path to the repository root. Apply platform and user instructions first, then the closest applicable repository instructions. Read only files that exist and are relevant.

Do not assume a `.governance` directory, its schema, or a central repository path. Treat existing governance documents as scoped rules, not permission to bypass platform policy or user authorization. Report missing, conflicting, or ambiguous rules and preserve user changes. Do not create governance files unless requested.

## Discovery and boundaries

Resolve the repository from the target file’s existing parent directory, using Git root discovery when available; a worktree may have a `.git` file rather than a directory. For non-Git targets, use an explicitly identified project root instead of searching unrelated parent directories. Inspect hidden governance paths explicitly. Read `.governance/GOVERNANCE.md` and applicable `exceptions.md`/`verification.md` when present, following the entrypoint’s actual paths rather than inventing a layout. Keep existing root work records in place until migration is requested.

A missing optional policy differs from a required policy that is missing, unreadable, or fails its configured hash check. Report the latter and stop the affected edits or completion claim until resolved; independent read-only investigation may continue. Do not fall back to unrelated policies or change ownership/permissions to make a required read succeed. Resolve symlinked or out-of-repository references against the authorized scope before reading or writing them.

Repository exceptions apply only to their stated targets and conditions. They cannot authorize changes to other repositories, weaken platform controls, or turn a validation command into deployment authority. Reuse valid approval for its existing scope and identify expired one-time exceptions; request a decision only for missing authority or added scope. Report conflicts against the applicable instruction hierarchy rather than treating every local document as an override.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
