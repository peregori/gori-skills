---
name: matt-engineering
description: "Shape, implement, or review one selected engineering task using adapted Matt Pocock methods: source-grounded spec, vertical TDD slices, deep interfaces, and separate standards/spec review. Use within factory-workflow when the relevant phase needs rigor."
---

# Matt engineering method

Read the repo's `AGENTS.md`, canonical context, and existing issue or request. Keep the repo's task authority and release gates. The user selects work; a skill does not create tasks, move Project cards, or force a new memory layout.

Choose the phase needed now:

- **Shape the task:** Read [spec.md](references/spec.md) when an idea or issue needs a source-grounded, implementation-ready spec. Record it in the existing authorized issue or conversation.
- **Implement or diagnose:** Read [implement.md](references/implement.md) for vertical slices, behavior tests, bug reproduction, and module seams.
- **Review:** Read [review.md](references/review.md) for separate standards and intent reviews, plus concrete refactor recommendations. Run `product-verification` for executable user-path proof.

These are portable adaptations of Matt Pocock's [engineering skills](https://github.com/mattpocock/skills/tree/main/skills/engineering), especially `to-spec`, `implement`, `tdd`, `codebase-design`, `diagnosing-bugs`, and `code-review`. They retain his issue-to-spec-to-code discipline while following the user's existing task and GitHub Project boundaries. See the repository's third-party notice for the MIT attribution.
