---
name: gori-code-review
description: Review a selected task's full diff against the original request and repository standards on separate axes. Use from gori-mode before executable verification and release.
---

# Review the full change

Pin the base commit and inspect committed, staged, unstaged and untracked changes. Read the original request, later decisions, issue and repo standards. Disclose whether the pass is self-review or independent review.

1. **Intent:** For every requested outcome, name its implementation and evidence, or mark it partial, missing or out of scope. Identify work the request did not authorize.
2. **Code:** Inspect behavior, edge cases, ownership and data boundaries, security, regressions and neighboring patterns. Check whether changed tests assert independent behavior. Separate tool-enforced style from judgment findings.
   For UI changes, use [gori-design](../gori-design/SKILL.md) to inspect the affected rendered surface against the product's accepted design guidance and realistic content. Keep visual findings distinct from behavior failures.
3. **Proof:** Check selected test counts, actual commands and results, affected user path, exact revision and dirty-tree match, and external prerequisites. A build, mock, screenshot or stale receipt proves only its own layer.

Report findings with severity and location. Recommend a refactor only when source evidence shows duplication, a brittle boundary, or verification friction; state the smallest useful scope. Fix supported findings through [gori-implement](../gori-implement/SKILL.md), rerun affected checks, then proceed to [gori-verify](../gori-verify/SKILL.md). The phase ends when the full requested diff has no unresolved supported finding.
