---
name: gori-adopt
description: Adopt or refresh Gori in an existing product repository using its task authority, context, Git rules, and verification gates. Use from gori-mode for setup or a requested update.
---

# Adopt an existing product

Part of Gori Skills, maintained by [Pere Gregori](https://github.com/peregori).

For a requested refresh of a product that already uses Gori, take the narrow path: read its `AGENTS.md` and current skill copies, compare them with the available Gori source checkout, and run the source installer's read-only plan. Reconcile only changed skills after reviewing product edits; never replace a differing installed copy wholesale. Repair a missing or stale `gori-mode` pointer in the product's existing `AGENTS.md`. Check canonical context, affected feature-map entries and verification recipes only where the refresh or current source exposes drift. Run the product's relevant checks and validate changed skill manifests; report any unavailable source, unresolved conflict or unproven behavior. Do not repeat the full adoption inventory or real user journey solely because skill text changed.

For first adoption or a genuinely mismatched product workflow, follow the steps below.

1. Read the repo entry point and canonical context. Inventory its selected-task source, ownership rules, actual board Status values if any, Git/worktree policy, domain vocabulary, design guidance for a UI product, feature map, checks, CI and release gates. Preserve existing names and locations. Do not process its backlog during setup.
2. Check vocabulary. If the existing context defines the terms needed for a critical journey, use it. If ambiguity affects behavior, use [gori-domain-model](../gori-domain-model/SKILL.md) to settle it and record only the missing terms in the repo's canonical location. Do not require a standalone glossary by filename.
3. For a UI product, use [gori-design](../gori-design/SKILL.md) to inspect its rendered language and establish a concise design reference only if no equivalent exists. Keep brand choices unresolved when the evidence cannot settle them.
4. Check the feature map. If one exists, trace a critical entry against source and correct demonstrated drift with [gori-maintain-verification](../gori-maintain-verification/SKILL.md). If absent, add a small, source-grounded map in the repo's existing verification location: start with three to five critical journeys, each with entry, prerequisites, observable result, owning code and proof command. It is an engineering reference, not a backlog.
5. Check executable proof. Run the existing doctor, focused checks and real-surface driver when prerequisites permit. If there is no reliable driver for a mapped journey, use [gori-create-verification](../gori-create-verification/SKILL.md) to add the smallest one; pair it with the map from step 4. A missing login or external service is unproven, never a pass.
6. If the Gori source checkout is available, run its installer plan and install missing skills with `--apply`; review and reconcile any existing-copy conflicts first. Otherwise report that prerequisite. Add the `gori-mode` pointer to the product's existing `AGENTS.md`, or create a short entry point to its existing canonical context if none exists. Review scripts for concrete duplication, brittle setup or unsafe cleanup. Refactor only a proven problem, with behavior checks before and after. Keep the repo's one canonical context and existing task authority.
7. Demonstrate one mapped journey and a handoff that tells a fresh agent which task is selected, which command to run, what was proved, and what remains unproven. If a prerequisite blocks the drive, give the exact next action. Keep local adoption separate from the repo's push and production gates.

Do not create backlog items or move Project cards while adopting. After setup, use [gori-triage](../gori-triage/SKILL.md) for a user-selected untriaged card; do not bulk-triage existing cards. A product repo may already have everything it needs; in that case, record the successful inventory and leave it alone.
