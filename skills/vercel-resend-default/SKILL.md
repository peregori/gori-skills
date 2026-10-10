---
name: vercel-resend-default
description: "Record or verify a repo's chosen Vercel-managed Resend email setup when the user selects that provider path. Use for email delivery planning or setup, not ordinary email feature code."
---

# Vercel-managed Resend

Read the repo's `AGENTS.md` and canonical context. Confirm that Vercel-managed Resend is the selected provider path; an existing different provider decision takes precedence. Search current email configuration and documentation before changing either.

When the decision is authorized, record it once in the repo's canonical engineering context. The integration command is `vercel integration add resend`; the app should receive its `RESEND_API_KEY` through Vercel-managed configuration. Keep credentials out of Git and browser code. Update only the repo's existing verification recipe and relevant environment contract; do not create a parallel task or memory file.

For a documentation-only change, check consistency and the diff. For integration or runtime changes, verify the configured environment and an authorized end-to-end delivery path before claiming email works. Record what was proved and what still needs DNS, account access, or live delivery. Do not infer that a stored key or a passing mock proves receipt.
