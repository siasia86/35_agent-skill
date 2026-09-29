---
name: markdown-review
description: Review Markdown structure, presentation, links, code examples, tables, diagrams, and consistency without changing files or verifying external facts.
---

# Markdown review

Review the requested Markdown files for clear, usable, internally consistent
documentation. This skill is for editorial and structural review; it does not
establish the truth of technical claims.

## Scope and safety

- Identify the requested files. If none are named, use the most recently
  discussed Markdown file only when it is unambiguous; otherwise ask which
  file to review.
- A review-only request is read-only. Do not edit files, apply patches, or
  start a review-and-fix loop.
- Make edits when requested, and continue until the scoped outcome is met.
  Respect an explicit review count or budget. If progress stalls without new
  evidence or a missing decision blocks work, report findings and the next step.
- Do not assume a repository's conventions from a file path, a previous
  project, or a personal preference. Apply project-specific requirements only
  when an applicable project policy explicitly states them.

## Review checks

Check the parts relevant to the document and report actionable findings with
file and line numbers where possible.

- Structure: heading hierarchy, table-of-contents entries and anchors, section
  order, and overall narrative flow.
- Content: typos, incomplete or broken sentences, duplication, contradictory
  statements, and examples that disagree with their surrounding explanation.
- Code blocks: appropriate language tags, balanced fences, syntax or commands
  that are visibly implausible, and expected output that conflicts with the
  example. Distinguish static concerns from behavior that was not executed.
- Links and images: malformed links, missing local targets, anchors that do
  not match headings, and links or image references that appear broken. Do not
  claim that an external destination is reachable unless it was checked.
- Tables: valid Markdown structure, readable alignment, and consistent cell
  widths when visual alignment is intended. For multilingual fixed-width
  tables, calculate display width rather than character count.
- Box diagrams: when box-drawing characters are used, verify matching borders,
  consistent interior row widths, sensible arrow direction, and labels that
  make the flow understandable.

## Policy-dependent checks

Only enforce the following when an explicit, applicable project policy defines
them. Otherwise, report them as optional observations at most; do not add,
remove, or normalize them.

- Required or prohibited badges, dates, licenses, footers, and reference-star
  ratings.
- Removal of internal-only headers, change histories, owners, feedback
  addresses, personal mentions, or author notes.
- A required language inside diagrams, including an English-only diagram rule.
- Special requirements for a named directory or document class, such as source
  frontmatter, traceable citations, `last_checked` dates, or unverified-claim
  labels.

## Factual verification routing

Treat RFC comparisons, product/version claims, numerical claims, and other
external factual assertions as out of scope for this skill. When such checking
is needed, first check whether a `fact-check` skill is available. If it is,
tell the user that those findings should be handled by that skill; do not
automatically delegate work or request permissions. If it is unavailable,
state the verification limitation and list the claims that remain unverified.

## Report format

Respond in the user's requested language; otherwise use the conversation's
working language. Report actionable findings with severity, `file:line` when
available, evidence, and a suggested fix. For a small review, a short findings
list and verification limits are sufficient. Use an area-by-area status table
only when the review scope benefits from it or the user requests it.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-29

© 2026 siasia86. Licensed under CC BY 4.0.
