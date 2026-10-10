---
name: product-verification
description: "Establish, run, or repair a repository's executable product verification: mapped user journeys, focused checks, real-surface proof, and revision-bound evidence. Use when adopting an existing product, verifying a selected change, or fixing verification drift."
---

# Product verification

Use the repository's `AGENTS.md` and canonical context first. Its verification commands, feature map, browser rules, and release gates take precedence. Keep one verification contract per repo; improve it in place. A feature map is a guide to user paths, not a task queue or proof by itself.

Choose the branch that matches the current authorized work:

## Adopt a product

Read [adopt.md](references/adopt.md) when an existing repo lacks a trustworthy way to drive and check its main user journey. Inventory what already works before adding files or dependencies. An existing `agent:verify`, `verify:changed`, or equivalent is a starting point, not a reason to scaffold a new skill directory. Prove one real mapped journey before calling adoption complete.

## Verify a selected change

1. Turn each requested observable outcome and material failure path into a check at the highest useful seam. Read only affected feature entries. Record the base revision and current dirty-tree state; account for committed, staged, unstaged, and untracked changes.
2. Run the repo's read-only doctor/plan, then the narrow meaningful test loop. A zero-test selection, skipped prerequisite, or stale receipt is inconclusive. Widen when source ownership or test selection is uncertain. Run the full repo gate at its required point, especially before a push or release.
3. Drive the affected user path through the repo-approved real surface. For web UI, follow the active client's approved browser workflow; exercise relevant interaction, narrow/mobile layout, accessibility, console, and network behavior. Use isolated test data and observe the resulting state. A screenshot or internal API call alone does not prove a user journey. For CLI, service, desktop, or mobile products, use the equivalent real entry point and observable side effect.
4. Capture sanitized evidence tied to the exact revision and source state: commands and exit codes; path, actions, and observed result; screenshots or transcripts where useful; cleanup; and any prerequisite that remained unproven. Keep automated, browser, database, external delivery, CI, and production claims distinct. Re-run affected checks after source changes.
5. Compare the evidence against every requested outcome. Report what passed, failed, or could not be exercised, with the next exact step. Do not turn a local pass into a shipping claim.

## Repair drift

Read [maintain.md](references/maintain.md) when a route, behavior, selector, script, or feature entry has changed, or when the user explicitly requests a verification audit. Update the affected map and harness alongside the product change. Broad recurring sweeps require an explicit request.

Adapted from Lauren Tan's [create-verification-skill](https://github.com/backnotprop/pstack/blob/main/skills/create-verification-skill/SKILL.md), [maintain-verification-skill](https://github.com/backnotprop/pstack/blob/main/skills/maintain-verification-skill/SKILL.md), and [behavior-level example](https://github.com/poteto/verification-skill-example). This adaptation preserves existing repo contracts and the user's task/Project authority.
