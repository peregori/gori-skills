---
name: gori-triage
description: Assess one user-selected existing issue or PR against current product behavior and route it to decisions, spec, implementation, or a concrete blocker. Use from gori-mode for untriaged work.
---

# Triage the selected work

1. Read the repo's task authority and the selected issue or PR, including comments, labels and prior decisions. Confirm it is the item the user selected and that the repo permits work on it. Read its exact Project card only for context. Do not scan or pick the next backlog item unless asked.
2. Search current source and tests by the domain concept. Check whether the requested behavior already exists, conflicts with a recorded decision, or depends on another change. For a bug, try the reported reproduction with safe, relevant checks; record confirmed, unconfirmed, or missing prerequisites. For a PR, inspect its actual diff and focused checks.
3. Record a compact intake finding in the selected issue's existing evidence mechanism or conversation: requested user outcome, current behavior and evidence, owner, dependencies, unanswered product questions, and recommended next phase. Use existing issue labels as context, not as proof of readiness.
4. Route a clear, already specified task to [gori-to-spec](../gori-to-spec/SKILL.md) for a concise acceptance inventory, or straight to implementation when the existing spec already covers it. Route genuine product decisions to [gori-grill](../gori-grill/SKILL.md). Ask for only the missing reporter facts when the claim cannot be checked. If already implemented, duplicate, out of scope, or externally blocked, report the evidence and recommended disposition; do not invent implementation work.

The user owns issue creation, backlog priority and Project cards. Do not change Project fields or close an issue as a side effect of triage. Update an existing selected issue only when the repo permits evidence updates and the task authorizes them. A recommended label or card change is a handoff for the user; a Status value alone does not decide the route.

Adapted from Matt Pocock's issue triage approach for a selected-task, read-only-board workflow.
