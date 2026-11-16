---
name: gori-code-review
description: Review a selected task's full diff against the original request and repository standards on separate axes. Use from gori-mode before executable verification and release.
---

# Review the full change

Part of Gori Skills, maintained by [Pere Gregori](https://github.com/peregori).

Pin the base commit and inspect committed, staged, unstaged and untracked changes. Read the original request, later decisions, issue and repo standards. Disclose whether the pass is self-review or independent review.

1. **Intent:** For every requested outcome, name its implementation and evidence, or mark it partial, missing or out of scope. Identify work the request did not authorize.
2. **Code:** Inspect behavior, edge cases, ownership and data boundaries, security, regressions and neighboring patterns. Check whether changed tests assert independent behavior. Separate tool-enforced style from judgment findings.
   For UI changes, use [gori-design](../gori-design/SKILL.md) to inspect the affected rendered surface against the product's accepted design guidance and realistic content. Keep visual findings distinct from behavior failures.
3. **Proof:** Check selected test counts, actual commands and results, affected user path, exact revision and dirty-tree match, and external prerequisites. A build, mock, screenshot or stale receipt proves only its own layer.

## Receiving feedback

When the user, a human reviewer, or a review bot comments on the change, read every item before acting. Restate each requirement in your own words. If any item is unclear, ask about it before implementing any of them, because items are often related. Check each against the repo: is it correct for this codebase and stack, would it break existing behavior, is there a reason for the current code, and is the suggested feature actually used? Treat the user's feedback as the authority on intent, but still verify the technical claim. Be skeptical of external and automated feedback. Push back with evidence, such as source, a test or a usage search, when an item is wrong, unused or conflicts with a recorded decision; bring that conflict to the user. Say when you cannot verify an item and what would settle it. Implement accepted items through [gori-implement](../gori-implement/SKILL.md) one at a time: blocking and security items first, then simple fixes, then larger changes, each with its affected checks. Acknowledge with what changed and where, not with agreement or thanks. If your pushback turns out wrong, say so in one line and fix it. Reply to inline review comments in their own thread. Answering feedback never creates new tasks; report out-of-scope suggestions for the user.

## Report

Report findings with severity and location. Recommend a refactor only when source evidence shows duplication, a brittle boundary, or verification friction; state the smallest useful scope. Fix supported findings through [gori-implement](../gori-implement/SKILL.md), rerun affected checks, then proceed to [gori-verify](../gori-verify/SKILL.md). The phase ends when the full requested diff has no unresolved supported finding.
