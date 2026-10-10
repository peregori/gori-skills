---
name: factory-workflow
description: Route a selected product task from idea or issue through scoped implementation, review, verification, and authorized release, or adopt that workflow in an existing repo. Use as the one reusable entry point when the user wants predictable end-to-end product work without choosing skills.
---

# Factory workflow

The user selects the product and work. Start with the repo's `AGENTS.md`, canonical context, current source, and worktree. Resume a clearly in-flight selected task from its existing evidence; if several tasks could be meant, ask the user which one. Do not select new backlog work, create tasks, or alter Project cards. Use the smallest useful skill set; a skill's tracker or branch recipe cannot override repo policy or the user's authority boundary.

## Route the request

| Situation | Next action |
| --- | --- |
| Existing product needs this approach | Inspect its task authority, canonical context, Git policy, tests, and release contract. Add only missing tracker/domain pointers. Use `product-verification` → **Adopt** for missing executable proof; simplify scripts only when a concrete duplication or failure is found. |
| Idea or issue is not implementation-ready | Use `matt-engineering` → **Shape** to define observable outcomes, scope, and verification in the existing authorized issue or conversation. The user owns new task creation. |
| Ready feature, bug, or refactor | Use `matt-engineering` → **Implement** for a bounded slice, relevant behavior tests, caller migration, and bug reproduction. |
| Changed code needs review and proof | Use `matt-engineering` → **Review**, then `product-verification` → **Verify** and repair affected map/harness drift. Resolve supported findings before claiming completion. |
| Ready to ship | Follow the repo's full local, CI, deployment, production smoke, cleanup, rollback, and approval gates. Include review and proof in the existing PR/release format. |

For an authorized task, continue through implementation, review, and the relevant proof layers in the same chat. A spec, passing slice, or local receipt is progress, not completion. Stop only at a real authority, budget, or external prerequisite boundary, with exact evidence and next action.

## Atomic work and worktrees

Use one selected task per branch/worktree when isolation helps or the repo requires it. Record the base and protect existing dirty or concurrent work. Use the client's managed worktree flow when one is in use; otherwise follow repo Git policy. Keep changes reviewable and commits coherent. A worktree does not grant a new task, push, merge, or release. Resume from the existing issue, canonical context, Git state, and evidence; do not trust chat memory alone.

## Proof and token discipline

Read only relevant feature entries and source paths. Run focused checks after each implementation slice; drive the affected user journey before calling the task complete. Maintain the affected flow map or harness when behavior or controls change; reserve a full verification audit for an explicit request. Use the repo's full gate at its required point. Reuse scripts for repeated checks; add a helper only when it replaces repeated manual work and has a bounded, tested interface. During review, report a concrete refactor need when duplication, brittle boundaries, or verification friction is demonstrated, with its evidence and scope. Record actual command results and user-path observations against the exact revision/tree. Do not claim lower token usage or faster delivery without measurement.
