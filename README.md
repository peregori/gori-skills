# gori-skills

Portable skills for one selected task at a time. The core combines an adapted [Matt Pocock engineering method](https://github.com/mattpocock/skills) for spec, vertical implementation and review with [Lauren Tan's verification approach](https://github.com/backnotprop/pstack) for executable user journeys and evidence. The repo supplies instructions and a safe installer; each product retains its own `AGENTS.md`, task authority, scripts and release gates.

## Skills

| Skill | Purpose | Default install |
| --- | --- | --- |
| `factory-workflow` | One entry point from selected task to proof and authorized release | Yes |
| `matt-engineering` | Shape, implement and review with adapted Matt methods | Yes |
| `product-verification` | Adopt, run and repair Lauren-style verification | Yes |
| `gtm` | Project-independent market research and outbound preparation | Optional |
| `vercel-resend-default` | Record and verify a chosen Vercel-managed Resend path | Optional |

The core is self-contained; Matt's separate plugin is not required. These are adaptations, not official Matt Pocock or Lauren Tan releases. [Third-party notices](THIRD_PARTY_NOTICES.md) record the upstream licenses and source revisions.

## Install into one product repo

Clone this repository once, then run the installer from it. Python 3 and Git are the only requirements.

```sh
git clone https://github.com/peregori/gori-skills.git ~/gori-skills
python3 ~/gori-skills/scripts/install.py /absolute/path/to/product
python3 ~/gori-skills/scripts/install.py /absolute/path/to/product --apply
```

The first command after cloning is a read-only plan. The second copies the three core skills into the product's `.agents/skills/`. Use `--all` before `--apply` to include GTM and Resend, or name one skill such as `gtm`; core dependencies are included automatically. The installer refuses to overwrite a differing skill, including local edits. Review and commit the copied files in that product repo.

Add one short pointer to the product's existing `AGENTS.md` when its own instructions do not already route selected work to `factory-workflow`, for example: “For selected product work, use `.agents/skills/factory-workflow` and follow this repo's context and release gates.” Keep repo-specific commands, feature maps, issue ownership and release gates in that product. [Codex's skill documentation](https://learn.chatgpt.com/docs/build-skills) describes `.agents/skills/` as a repository skill location; when the same skill name is also installed globally, both copies can appear in the selector.

Installed skills are snapshots. To update one, compare the new source with the product's copy and reconcile product-specific edits before replacing it; the installer will stop rather than overwrite them silently.

## Verification

```sh
python3 -m unittest discover -s tests -v
```

The tests exercise read-only planning, installation, repeat runs, and protection of modified product skills. Validate changed skill manifests with Codex's `skill-creator` validator when available, then inspect the public diff for machine paths, product data and secrets before publishing.

Verification runs in each implementation slice at the relevant seam; the affected real user path is driven before task completion. Flow maps and harnesses are maintained when that path changes. Broad audits run when requested. The router reports demonstrated refactor needs during review.
