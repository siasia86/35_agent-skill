---
name: git-commit-rule
description: "Prepare Git commits using Korean type-prefix messages, 50-character/no-period defaults, and repository-controlled branch and publishing rules."
---

# Git commit rule

Read repository guidance and inspect status and the intended diff before proposing a commit. Preserve unrelated user changes. Unless applicable higher-priority user or repository policy says otherwise, use this default message form:

```text
<type>: <Korean description>
```

Use one of `docs`, `fix`, `feat`, `refactor`, `chore`, or `style`; choose the principal change when several are present. Keep the entire subject, including the type prefix and Korean description, within 50 characters and omit the final period. Preserve a repository's stricter or different convention when it exists, and state the convention used.

Before commit or push, explicitly inspect the current branch, for example with `git branch --show-current`, and compare it with the applicable repository/profile policy. Stop on detached HEAD, a prohibited branch, or an unresolved branch restriction. If the current branch is allowed, keep it; do not invent or switch to a fixed branch merely because an old example used it.

Stage explicit intended files after inspecting status; avoid broad staging that could absorb unrelated work. Do not assume a branch name, remote, push permission, signing key, or release authority: branch/remote restrictions are profile or repository controlled. Separate unrelated changes into logical commits when practical. Before committing, summarize staged files and relevant validation. Commit, tag, push, or modify history only when the user explicitly authorizes that action; report the exact result rather than implying publication.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
