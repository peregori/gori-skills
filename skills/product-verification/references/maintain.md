# Repair a verification contract

Use this during an authorized product change or an explicit verification audit.

1. Compare the affected flow entry and driver with current routes, controls, contracts, and tests. Trace the changed user path from source. For an audit, inventory every entry and choose coverage according to the requested scope; do not schedule a recurring scan.
2. Drive the affected path live. Doctor before the first drive and after a surprising failure. Reset to known state before retrying. Preserve evidence across retries and cleanup. If access, entitlement, OS, or external state blocks the path, record the exact prerequisite and attempted route.
3. Classify the finding: map drift, harness gap, product regression, or missing prerequisite. Correct map/harness drift at its owning location and re-drive it. Report product regressions as such; do not edit documentation to hide them. Keep product-code fixes within the selected task's scope.
4. Confirm the changed recipe, source paths, and index agree. Run relevant checks, capture revision-bound evidence, and state coverage honestly. Use existing issue/PR and release rules; this skill does not authorize task creation, Project changes, publishing, or deployment.
