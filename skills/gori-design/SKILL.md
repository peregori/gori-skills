---
name: gori-design
description: Establish and maintain product-specific UI design guidance, then check affected screens during selected UI work. Use from gori-mode only for products with a user interface.
---

# Keep the product's UI coherent

Part of Gori Skills, maintained by [Pere Gregori](https://github.com/peregori).

Read the repo's `AGENTS.md` and its existing design source of truth. Use this phase during UI product adoption, before a selected UI change, and again when reviewing that change. Load only the affected surfaces; do not audit the whole product as routine maintenance.

1. **Find the actual system.** Trace the affected screen through its rendered layout, theme tokens, shared primitives, variants and neighboring screens. Inspect representative desktop and narrow layouts when browser access permits. An explicit product decision outranks an observed pattern; repeated implementation is evidence of current practice, not proof of intended brand. For user-supplied visual references, record which relationships to borrow and which to leave behind. Treat outside products as examples of alignment, density and hierarchy, never as a token or component source to copy.
2. **Establish durable guidance at adoption.** Reuse an existing design document or canonical context section. If a UI product has no equivalent and its current direction can be evidenced, create a concise `DESIGN.md` in the repo's normal docs location and link it from its entry point. Record the intended visual character only when the user or accepted context supplies it. Record governing token and component owners, typography roles, spacing and layout relationships, density, states, responsive rules and themes only where supported. Distinguish observed conventions from accepted decisions; leave contradictions or unchosen brand direction unresolved instead of turning them into rules. Do not duplicate a CSS variable inventory.
3. **Shape the selected UI task.** State which screens and states change and what a user should see. Identify the existing tokens, layout rails and component variants to reuse. For a consequential new visual direction that the repo cannot decide, present a small set of concrete choices to the user before encoding it. Do not add a dependency, token, variant, animation or shared abstraction just for polish.
4. **Review the affected result.** Compare the rendered change with the accepted design guidance and neighboring surfaces: shared edges, spacing rhythm, type hierarchy, density, color and elevation roles, interaction feedback and motion restraint. Drive plausible long and short content, empty/loading/error states, narrow width, keyboard focus and contrast; check alternate theme and reduced motion when the product supports them. Use the same browser journey and revision-bound evidence as `gori-verify`; avoid a second broad test run. If rendered access is blocked, label visual conclusions unproven.
5. **Maintain the contract.** Update the design reference when the selected task deliberately changes a product-wide rule, token owner or shared pattern. Repair supported drift within the authorized scope and recheck the affected surface. Report unrelated inconsistency as a recommendation for the user to prioritize, not as a new task or a reason to rewrite the UI.

This phase does not apply to a CLI or service without a UI. A `DESIGN.md` is useful only when it records actual product decisions and helps the next implementation; it never replaces source, rendered evidence or the repo's release gates.
