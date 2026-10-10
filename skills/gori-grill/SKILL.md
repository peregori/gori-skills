---
name: gori-grill
description: Resolve missing product decisions on a selected Inbox or Needs Grill issue before writing its spec. Use from gori-mode when the user outcome, scope, or acceptance is genuinely unclear.
---

# Grill the selected idea

1. Read the original request, issue and comments, repo context, source and existing behavior. List decisions already made, facts that can be observed, and genuine choices only the user can make.
2. Investigate facts and test observable alternatives before asking. For a consequential interface or flow choice, show the simplest plausible options and their effect on the user and release risk. Use a cheap prototype only when it can settle the question.
3. Ask the smallest useful set of product questions. When a domain term changes the rule, use [gori-domain-model](../gori-domain-model/SKILL.md) to test edge cases and record the settled meaning. Preserve the user's answers and the reason for each decision in the existing issue or conversation. Do not re-ask settled questions or turn routine code choices into a pause.
4. End when the intended user outcome, scope boundaries, dependencies and material failure paths are decided enough to state acceptance. Send the settled decisions to [gori-to-spec](../gori-to-spec/SKILL.md). If a decision remains external, name its owner and what independent work can proceed.

The user owns task creation and Project status. Report when the issue is ready for the next column; do not move it.
