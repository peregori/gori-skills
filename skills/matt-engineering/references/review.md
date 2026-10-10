# Review one change

Pin the base commit or branch and include committed, staged, unstaged, and untracked changes in the review. Identify the originating request or spec. If the fixed point is unclear, infer it from the selected issue and branch history; ask only when multiple plausible bases would change the verdict.

Review three questions separately:

1. **Intent:** For each requested outcome, identify implementation and evidence, partial work, omissions, or scope creep. Quote the relevant requirement and code location for findings.
2. **Code:** Compare the diff with repo standards and neighboring patterns. Look for wrong behavior, edge cases, security/data boundaries, duplicated logic, shallow pass-through modules, and hard-to-test seams. Tool-enforced style is a gate result, not a judgment finding.
3. **Proof:** Check the commands actually run, selected test count, mapped user journey, revision/tree match, and unresolved external or production prerequisites. A receipt, screenshot, or passing build proves only its own layer.

Report findings by severity and location, then recommend a refactor only when a concrete pattern in the diff or callers justifies it. State its expected benefit and smallest scope. Disclose whether this is self-review or an independent pass. Fix supported findings and rerun affected checks before the release decision.

For a PR body, summarize the change, before/after evidence, blast radius, rollback, and unproven layers using the repo's existing template.
