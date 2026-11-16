---
name: gori-brainstorm
description: Shape a new product or a major new direction into an approved design before any repo, issue or spec exists. Use from gori-mode when the intent, approach or architecture is still open.
---

# Brainstorm a new direction

Part of Gori Skills, maintained by [Pere Gregori](https://github.com/peregori).

Use this before work has a selected issue: a new product, or a direction in an existing product too large or unsettled for [gori-grill](../gori-grill/SKILL.md). A clear request with one sensible approach skips it; state the approach in a line and route on.

1. **Look before asking.** Read what the user pointed at, any existing repo's `AGENTS.md`, canonical context and affected source, and their default bootstrap path if one applies. Do the recon that facts can settle, including the web when prior art matters. Never ask what that material answers or reopen a recorded decision.
2. **Learn the why first.** Ask one question at a time, in the user's own terms, and say what the answer would change. Until the intent is clear, ask open questions without suggested answers; options steer. Cover, as territory rather than a script: what it is and for whom, why now and what success looks like, goals, non-goals and anti-goals, prior art, current state, and constraints such as budget, timeline and stack. Ask only when the answer changes what gets built; otherwise state a proposal with its reason so the user can correct it.
3. **Play back as you go.** When one part is understood, describe it back in a few short paragraphs, marking what the user said versus what you proposed, and ask what is wrong or missing. Sketch anything they will look at as a few lines of text. Use [gori-domain-model](../gori-domain-model/SKILL.md) when a term's meaning changes a rule.
4. **Lay out the approaches in a message of their own.** Generate real alternatives, drop those that work against the why or are ruled out by existing work, and sketch the two or three that remain with their trade-offs in user outcome, cost, operational risk and reversibility. Recommend one and let the user choose. If the user handed you the how, choose and say so. Resolve an observable uncertainty with a throwaway spike only when the user agrees; label it throwaway and bring what it taught back into the conversation.
5. **Write the design.** Record it once, in the repo's canonical context or established docs location, or in the conversation when no repo exists yet; do not create a parallel docs tree. Cover intent and why; goals, non-goals and anti-goals; constraints; the approaches considered and the one chosen with its reason; architecture and data decisions as decided; three to five critical user journeys, each with its observable result; open decisions with an owner; and what is left to the implementer. Mark each of your own calls as yours.
6. **Builder check.** Reread the design as a fresh implementer who has not seen the conversation, or ask one agent to when the client and user allow it, and disclose which happened. Put answers already given into the design, settle minor gaps yourself and mark them, and bring the remaining questions that change what gets built to the user in one message, most important first.
7. **Exit gate.** The phase ends when the user has approved the written design and a fresh implementer could say what to build first and how each critical journey will be observed. Until then, build nothing: no product code, scaffolding, dependency installs, repo creation or implementation skill. A spike the user accepted is the only exception, and keeping its output is a new request.

**Handoff.** For a new product, follow the user's authorized bootstrap path, record the approved design as the new repo's canonical context, then use [gori-adopt](../gori-adopt/SKILL.md) so the critical journeys seed its feature map and verification. For a direction in an existing product, record the design in its canonical context and send the first selected piece to [gori-to-spec](../gori-to-spec/SKILL.md). If the work splits into independent projects, agree an order and brainstorm them one at a time. Propose the first vertical slices in the handoff; the user creates any issue or card.

Adapted from Jesse Vincent's Superpowers brainstorming skill.
