---
name: gori-implement
description: Implement one selected task in verifiable vertical slices, using bug reproduction and behavior tests where useful. Use from gori-mode for In Progress or implementation-ready work.
---

# Implement the selected task

1. Read the selected issue and acceptance inventory, canonical context, affected flow, Git base and worktree state. For UI work, read the affected design guidance through [gori-design](../gori-design/SKILL.md). Protect existing dirty and concurrent work. Use a separate worktree when isolation helps and the repo permits it.
2. For a bug, establish a failing signal for the reported symptom before editing. For a refactor, pin current behavior at the useful interface. For a feature, choose the highest meaningful test seam already available.
3. Build one user-visible vertical slice at a time. Use a red → green loop when an independent expected result can be asserted cheaply. Run focused checks after each slice; zero selected tests or skipped prerequisites are inconclusive. Commit passing slices locally. Do not push or open a pull request to see how a slice fares: hosted runs are for the finished task.
4. Keep interfaces small, reuse existing dependencies, migrate callers and remove obsolete paths together. Refactor only a demonstrated duplication or brittle boundary within the selected task. Preserve every original outcome across slices.
5. When behavior, route or control changes, use [gori-maintain-verification](../gori-maintain-verification/SKILL.md) for the affected map and driver. Hand the complete diff to [gori-code-review](../gori-code-review/SKILL.md), then [gori-verify](../gori-verify/SKILL.md).

The implementation phase ends with code and focused checks for the complete selected scope. A green slice is progress, not a completion claim.
