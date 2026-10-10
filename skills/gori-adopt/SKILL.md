---
name: gori-adopt
description: Adopt Gori in an existing product repository by mapping its task authority, context, Git rules, and verification gates. Use from gori-mode for one-time setup or repair of a mismatched workflow.
---

# Adopt an existing product

1. Read the repo entry point and canonical context. Inspect its selected-task source, ownership rules, actual board Status values if any, Git/worktree policy, feature map, checks, CI and release gates. Preserve existing names and locations.
2. Trace one critical user path through source and the current verification recipe. Run the existing doctor, focused check and real-surface driver when prerequisites permit. Record missing proof as missing, not as a pass.
3. Add only the missing router pointer or verification capability. Use [gori-create-verification](../gori-create-verification/SKILL.md) when no reliable user-path driver exists. Use [gori-maintain-verification](../gori-maintain-verification/SKILL.md) for demonstrated drift. Keep the repo's one canonical context and existing task authority.
4. Review scripts for concrete duplication, brittle setup or unsafe cleanup. Refactor only the proven problem, with behavior checks before and after. Do not perform a broad rewrite as setup.
5. Demonstrate one mapped journey and a handoff that tells a fresh agent which task is selected, which command to run, what was proved, and what remains unproven. Keep local adoption separate from the repo's push and production gates.

Do not create backlog items or move Project cards while adopting. A product repo may already have everything it needs; in that case, record the successful inventory and leave it alone.
