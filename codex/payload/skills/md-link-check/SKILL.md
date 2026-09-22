---
name: md-link-check
description: Check Markdown headings, anchors, and local links while distinguishing static evidence from links that need network access.
---

# Markdown link check

Inspect requested Markdown files and repository conventions. Check heading hierarchy, duplicate anchors, table-of-contents targets, relative paths, fragments, URL encoding, and links hidden by code blocks or generated content. Use the renderer or project checker when available; otherwise state the anchor convention used and limit conclusions to static evidence.

Do not fetch external links unless network access is available and within scope. Report each issue with source path, line, target, and repair. Distinguish missing local files, unresolved fragments, external availability not checked, and intentionally excluded generated paths.

When the repository requires numbered H2 headings, check numbering continuity. When its Markdown convention requires spacing between a closing bold marker and following Korean text, flag forms such as `**label**한글`. Apply these conventions conditionally; do not impose them on repositories that use different rules.

---

**작성일**: 2026-09-22

**마지막 업데이트**: 2026-09-22

© 2026 siasia86. Licensed under CC BY 4.0.
