# Personal infrastructure rules

## 1. Changes and authorization

Before operational changes, establish the current and intended state, affected resources, verification, recovery limits, and authorized scope. Prefer declarative configuration and available plan/check modes. A successful plan is evidence, not authorization to apply.

Reuse valid authorization for the identified targets. Obtain a decision for additional targets, missing authority, or irreversible effects. Do not infer privilege, credentials, hostnames, service names, or timeout values from examples.

## 2. Remote and Windows work

Use bounded remote commands. For Windows PowerShell over SSH, check the actual target's encoding and quoting with a harmless command before consequential operations. Do not copy a host-specific wrapper without inspecting its assumptions.

Before deleting a VM or comparable resource, identify the exact targets and confirm that deletion is authorized. Preserve required recovery material. Do not use generic process cleanup as a session-start ritual. After a timeout, inspect the owned process and remote job state before retrying; local termination may leave remote work running. Stop only identified resources within the authorized scope.

---

**작성일**: 2026-09-29

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
