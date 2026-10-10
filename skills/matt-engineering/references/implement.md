# Implement one task

1. Confirm the selected task, base revision, worktree state, and relevant repo policy. Use one task per worktree when isolation helps. Trace affected callers and the feature path before editing.
2. For a bug, build a tight signal that can show the reported symptom before changing code. Preserve the failing observation and distinguish a missing prerequisite from a reproduction. For performance, measure a baseline against the actual user path.
3. Choose the highest useful test seam with the existing repo contract. When a meaningful regression can be pinned cheaply, run a vertical red → green loop: one behavior test, the minimum implementation, then the next slice. Assert user-visible or interface-visible results against independent expected values. Avoid tests that merely mirror the implementation or succeed with zero selected cases.
4. Keep module interfaces small and clear. Put complexity behind the interface, use existing adapters and dependencies, and remove an obsolete path when callers migrate. Refactor only when source evidence shows duplication, a brittle boundary, or verification friction relevant to this task.
5. Run focused checks after each slice, then review and drive the affected user journey with `product-verification`. Run the full gate where the repo requires it. Record results against the final source state and leave a clean, reviewable change or an exact blocker.

Keep implementation and proof distinct: a green unit test does not prove browser behavior or external delivery.
