---
name: gori-maintain-verification
description: Reconcile affected feature maps and drivers with final source before each task ships, repairing drift when found. Use from gori-mode; run a broad audit only on explicit request.
---

# Maintain product verification

Part of Gori Skills, maintained by [Pere Gregori](https://github.com/peregori).

1. Before release of every selected change, compare the affected flow entries and drivers with final routes, controls, contracts and tests. Trace the changed user path from source. For an explicitly requested audit, inventory every mapped entry within the requested scope.
2. If the affected contract still matches source, record that inspection and let `gori-verify` drive the path once. If it drifted, classify the finding as map drift, harness gap, product regression or missing prerequisite. Correct map and harness at their owning location; report product regressions without hiding them in docs.
3. For a repaired recipe, run doctor and re-drive the affected path. On surprising failure, reset to known state and preserve failed-attempt evidence. A missing login, entitlement or external service is a prerequisite, not a pass.
4. Run affected checks and confirm index, source paths and instructions agree. Record revision-bound coverage and limits. Repeat the comparison after any later source change before release.

Adapted from Lauren Tan's `maintain-verification-skill`. Ordinary maintenance covers the affected path; a full sweep or recurring scan needs an explicit request.
