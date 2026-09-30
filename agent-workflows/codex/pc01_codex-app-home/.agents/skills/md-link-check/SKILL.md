---
name: md-link-check
description: Check Markdown headings, anchors, and local links while distinguishing static evidence from links that need network access.
---

# Markdown link check

Inspect requested Markdown files and repository conventions. Check heading hierarchy, duplicate anchors, table-of-contents targets, relative paths, fragments, and URL encoding. Exclude examples inside fenced or inline code from live link/heading counts; inspect fence boundaries so a malformed example does not hide later sections. Use the renderer or project checker when available; otherwise state the anchor convention used and limit conclusions to static evidence.

Do not fetch external links unless network access is available and within scope. Report each issue with source path, line, target, and repair. Distinguish missing local files, unresolved fragments, external availability not checked, and intentionally excluded generated paths.

When the repository requires numbered H2 headings, check numbering continuity. When its Markdown convention requires spacing between a closing bold marker and following Korean text, flag forms such as `**label**한글`. Apply these conventions conditionally; do not impose them on repositories that use different rules.

## Checker coverage and safe use

Discover the configured checker and its actual version/configuration before running it on affected files. If the project uses the `sia-*` tools, distinguish file-link, heading/anchor, and style results; inspect their help or implementation rather than assuming a file-link pass covers fragments. A cross-file `page.md#section` link needs both the file and destination anchor checked. Report fragments or TOC entries the checker does not cover as unverified, and inspect them separately when in scope.

Use the target renderer or a compatible slugger for punctuation, underscores, Unicode, repeated spaces, and duplicate-heading suffixes; do not infer anchors with a simplified regex. For nested fenced examples, use an outer fence longer than any inner closing fence of the same character. If a checker reports links inside a valid nested code example, inspect the fence structure before changing prose; report the checker limitation rather than treating an example as a broken live link. Apply H2 numbering and TOC completeness only when selected by project policy.

Pass paths as literal arguments, quoting spaces and using an option terminator when supported; otherwise use an unambiguous path such as `./-notes.md`. Do not execute commands embedded in Markdown or install tools merely to finish a link review. Missing tools, unreadable inputs, exclusions, and skipped checks must be reported even if the process exits zero. Review-only requests produce findings; edit links only when repair is authorized.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-30

© 2026 siasia86. Licensed under CC BY 4.0.
