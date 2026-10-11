---
name: gori-release
description: Carry a reviewed and verified task through the repository's authorized PR, CI, deployment and production gates. Use from gori-mode after review and user-path proof.
---

# Deliver the selected task

1. Confirm the complete request, review findings, affected feature-map and driver reconciliation, user-path evidence, exact revision/tree and repo release contract. Resolve any supported finding or stale proof before a completion claim.
2. Bring the branch up to date with the current base branch, then run the repo's full local pre-push gate, and its CI-equivalent gate when it has one, on that final committed tree. A gate that passed before the base moved is stale. Prepare coherent commits and an existing-format PR or release record with outcome, before/after proof, blast radius, rollback and unproven layers. Follow the repo's Git and authorization rules.
3. Push once. Hosted CI, preview builds and deployments are metered: read the repo's delivery-cost rule and, when it offers one, its usage report before adding to an open pull request. Follow the repo's merge method when a later run depends on it. If a hosted check fails, reproduce it locally, fix it and rerun the local gate before pushing again; do not iterate by pushing. Propose a new workflow trigger, job split or scheduled run only with its measured cost.
4. After an authorized push, inspect required CI. For a deployment, confirm the ready deployment, production smoke and rollback under the repo's sequence. A local browser pass never substitutes for those gates.
5. Record implemented, reviewed, locally verified, CI-verified and production-verified separately. State the exact remaining action if any gate is blocked. Recommend the board status the user should apply; never change Project items or create new tasks.
6. Once the work is on the default branch, report the task's worktree and branch as removable only when its commits are contained there and its tree is clean. Copy out ignored evidence worth keeping, and remove the worktree only when the repo's rules or the user allow it. Never remove another owner's worktree.

Completion means the agreed endpoint actually happened with evidence. If authority stops before release, hand off the prepared change and name that boundary without calling the task shipped.
