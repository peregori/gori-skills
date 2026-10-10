---
name: gori-mode
description: Route one selected repository task through its existing issue and board status, spec, implementation, review, user-path verification, and release gates. Use as the single entry point for product work or repo adoption.
---

# Gori mode

Read the repo's `AGENTS.md`, canonical context, selected request or issue, current source and Git state. The user selects work. If the repo uses a Project, match the selected issue to its exact card by issue URL or item ID, then read its **Status** and ownership; a thematic Phase field is not workflow status. If no card matches, say so and follow the repo's direct-task rule. Read issue labels according to the tracker contract; they do not override ownership. The board guides routing, while the issue, source, and repo gates define acceptance. Never create tasks or change Project cards or fields. Recommend status changes in the handoff for the user to apply.

For a nontrivial task, keep a short phase checklist in the existing issue, evidence location, or conversation. Record each phase as done, pending, blocked, or skipped with a reason. Load only the linked skill for the current phase. Continue an authorized task across phases even if the user has not moved its card. Recheck the original request at review; a slice or spec cannot silently narrow it.

| Observed state or request | Route |
| --- | --- |
| Existing product needs this workflow | [gori-adopt](../gori-adopt/SKILL.md). Create executable verification only if the repo lacks it. |
| Inbox, Needs Grill, unclear idea, or missing decisions | [gori-grill](../gori-grill/SKILL.md) to settle decisions, then [gori-to-spec](../gori-to-spec/SKILL.md) to record them. Skip grilling when the issue is already clear. |
| In Progress or implementation-ready task | [gori-implement](../gori-implement/SKILL.md). If a material decision is still missing, use `gori-grill` and `gori-to-spec` before that part. |
| In Review or completed implementation | [gori-code-review](../gori-code-review/SKILL.md) → [gori-maintain-verification](../gori-maintain-verification/SKILL.md) for affected maps and drivers → [gori-verify](../gori-verify/SKILL.md) → [gori-release](../gori-release/SKILL.md). Fix supported findings and repeat affected checks. |
| Done | Treat as historical evidence. A new request or explicit reopening defines new work. |
| Verification harness absent | [gori-create-verification](../gori-create-verification/SKILL.md) before claiming a real user-path pass. |
| Affected map or driver has drifted | Repair it with `gori-maintain-verification`, then re-drive the path with `gori-verify`. |

Those Status names are an example. Map each repo's own status vocabulary by meaning; do not add columns or force a Gori board. Route a directly authorized task without a board from its actual maturity. A status alone never proves a spec, code, review, or release is complete.

Use one selected task per branch or worktree when isolation helps and repo policy permits it. Choose a worktree explicitly in clients that support one; a new thread alone does not establish isolation. Confirm the base and preserve dirty or concurrent work. Run focused checks after each implementation slice. Before release, always reconcile the affected feature-map entries and verification driver with final source, then drive the affected real user path. Update the map or driver during the task when needed; the user need not request maintenance separately. Use the repo's full gates at their required points. Stop at an actual authority, budget, or external blocker with exact evidence and next action; do not silently start another task.
