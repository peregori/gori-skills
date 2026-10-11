---
name: gori-verify
description: Prove a selected change through relevant automated checks and the affected real user journey, with revision-bound evidence. Use from gori-mode after implementation and review or for an explicit verification request.
---

# Verify the selected claim

1. Map each requested observable outcome and material failure path to a check. Reconcile affected flow entries and drivers with final source through [gori-maintain-verification](../gori-maintain-verification/SKILL.md). Capture the base revision and current committed, staged, unstaged and untracked state.
2. Run the repo's read-only doctor or plan, then focused meaningful checks. Widen when ownership or selection is uncertain. Zero tests, skipped prerequisites and stale receipts are inconclusive. Run full gates where the repo requires them. When the repo has a local command equivalent to its hosted CI, run it on the final committed tree before any push, so a hosted run confirms a pass instead of discovering a failure the machine could have found for free. If the local gate covers less than CI, name the uncovered checks as unproven.
3. Drive the affected path through the repo-approved real surface. For web UI, follow the active client's browser rules and inspect relevant interaction, narrow layout, accessibility, console and network behavior. For CLI, service, desktop or mobile, use the equivalent entry and observable side effect. Use isolated data and clean up what this run created.
4. Save sanitized evidence: exact commands and exit codes, actions and observed results, screenshots or transcripts where useful, revision/tree state, cleanup and unproven prerequisites. Keep unit, browser, database, provider, CI and production claims separate. Re-run affected checks after source changes.
5. Compare proof with every requested outcome. If a later source change stales the map, driver or receipt, reconcile and re-drive. Report pass, failure or blocked per outcome, then proceed to [gori-release](../gori-release/SKILL.md) under the repo's gates.

A screenshot or internal API call alone is not a user journey. Local proof is not production proof.
