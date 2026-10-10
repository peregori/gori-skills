---
name: gori-to-spec
description: Turn settled decisions for a selected issue into an implementation-ready spec with observable acceptance and proof. Use from gori-mode after gori-grill or when the issue is already clear.
---

# Shape the selected task

1. Read the original request, later decisions, existing issue, relevant domain context, source and neighboring tests. Confirm ownership and dependencies. Synthesize settled decisions; use [gori-grill](../gori-grill/SKILL.md) only for a genuinely unresolved product choice, and [gori-domain-model](../gori-domain-model/SKILL.md) only when terminology changes a rule.
2. State the user's problem and every requested observable outcome. Trace affected callers and data flow; sketch the desired interface when architecture matters. Compare a simpler option and use a small experiment for an observable uncertainty.
3. Preserve any unresolved decision explicitly; a tentative assumption is not approval to drop requested behavior. Do not restart the interview to write a spec.
4. Record the compact spec in the selected issue or existing evidence location, or in conversation for directly authorized work. Include outcome, scope, material failure and empty paths, dependencies, constraints, acceptance checks, highest useful test seam, real-surface proof, and external or production prerequisites. For UI work, identify affected screens, states and accepted design guidance with [gori-design](../gori-design/SKILL.md); do not substitute a generic style preference for a product decision. Avoid volatile file paths unless the shape itself is the decision.
5. Check the spec against the original request. The phase ends when a fresh implementer can say what to build and how each outcome will be observed. Recommend the appropriate board status to the user; do not move the card or create tickets.

For a large existing issue, propose vertical, independently verifiable slices and blocking relationships in the conversation. The user owns any new issue or subtask creation.
