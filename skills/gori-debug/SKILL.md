---
name: gori-debug
description: Find the root cause of a bug, failing check, incident or unexpected behavior before any fix is written. Use from gori-mode or gori-implement when the cause is not already proven.
---

# Find the root cause

Part of Gori Skills, maintained by [Pere Gregori](https://github.com/peregori).

No fix is proposed until the cause is proven. A cause is proven when a recorded hypothesis explains every observed symptom and a minimal test of it behaves as predicted. A simple-looking bug, time pressure or a failed earlier fix does not waive this; guessing is slower than tracing.

1. **Observe.** Read the full error, stack trace and warnings, and the repo's canonical context for the affected flow. Reproduce the symptom with exact steps and record whether it happens every time. If it does not reproduce, gather more evidence; do not guess. Check what changed: recent commits, dependency and config changes, environment differences between where it works and where it fails. For production, read logs, runtime errors and deployment history through the repo's authorized tools; diagnosis stays read-only, and any production change follows the repo's release gates.
2. **Locate.** In a system with several components, instrument each boundary once, logging what enters, what leaves and which config arrives, to find the layer where good data turns bad. When the error surfaces deep in a call chain, trace the bad value backwards to where it originates. Find similar working code in the repo and list every difference from the broken path, however small. Read a reference implementation completely before applying its pattern.
3. **Test one hypothesis at a time.** Write it down as "X causes this because Y". Make the smallest change or probe that would prove or disprove it, one variable at a time. If it fails, form a new hypothesis from what you learned; do not stack another change on top. When you do not understand something, say so and investigate further.
4. **Hand the fix to implementation.** Record the proven cause, its evidence and the failing reproduction in the selected issue, evidence location or conversation. Then use [gori-implement](../gori-implement/SKILL.md): a failing signal first, one fix at the source rather than the symptom, no unrelated changes in the same fix, then [gori-code-review](../gori-code-review/SKILL.md) and [gori-verify](../gori-verify/SKILL.md). Remove temporary instrumentation before review.
5. **Stop after three failed fixes.** If three fixes for the same symptom have failed, or each fix exposes a new problem somewhere else, stop fixing. Report the attempts and the shared state or coupling they revealed, and treat the design as the question: use [gori-to-spec](../gori-to-spec/SKILL.md) for a bounded redesign, or [gori-brainstorm](../gori-brainstorm/SKILL.md) when the approach itself is in doubt. Do not attempt a fourth fix without the user.

If a complete investigation shows the cause is external, environmental or timing-dependent, record what was checked and ruled out, add the handling the evidence supports, such as a bounded retry, a clear error or a condition-based wait instead of a fixed sleep, and add the logging that would catch it next time. Most "no root cause" findings are incomplete investigations; say which evidence is still missing.

Adapted from Jesse Vincent's Superpowers systematic-debugging skill.
