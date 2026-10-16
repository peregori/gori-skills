# Gori Skills

**A practical workflow for shipping product work with Codex.** Gori Skills is a collection of agent skills that takes one task you choose from idea to reviewed, verified change. It follows the product repository's existing decisions, task ownership, and release gates instead of bringing its own backlog.

Created and maintained by **[Pere Gregori](https://github.com/peregori)**, a developer building tools for more reliable product delivery. See [Pere's work on GitHub](https://github.com/peregori) or [get in touch on LinkedIn](https://www.linkedin.com/in/peregregori/).

## What it does

Start with `gori-mode`. It reads the selected task and the repository's own `AGENTS.md`, then uses only the steps that task needs:

1. Check the request against current product behavior and resolve missing decisions.
2. Write observable acceptance criteria, then implement in small, verifiable slices.
3. Review the complete change against the original request and code quality.
4. Update affected verification guidance, prove the user journey, and follow the repo's release gates.

Gori can also adopt an existing product repository by mapping its current context and verification. The owner keeps control of task selection, issue creation, and GitHub Project cards. Gori reports recommended card changes for the owner to make.

For example, ask **“Use gori-mode for issue #42.”** It checks the issue against current source, settles any missing acceptance, and returns the implemented change with review and verification evidence under that repo's rules.

## Install

You need Python 3, Git, and an existing product Git repository. Clone this source once, then run the installer against your product:

```sh
git clone https://github.com/peregori/gori-skills.git
python3 gori-skills/scripts/install.py /absolute/path/to/product
python3 gori-skills/scripts/install.py /absolute/path/to/product --apply
```

The first command from the installer shows a read-only plan. `--apply` copies the core skills into the product's `.agents/skills/` directory. The installer refuses to overwrite a differing copy. Review and commit the installed files in the product repo. Use `--all` to include the optional skills, or pass an optional skill name to install it alone.

Add this pointer to the product's existing `AGENTS.md` if it needs one:

> For selected product work, use `.agents/skills/gori-mode`; this repository's canonical context and release gates remain authoritative.

Then ask Codex to **“Use gori-mode to adopt Gori in this repo”** for initial setup, or **“Use gori-mode for [selected task]”** to work on one task. Installed skills are snapshots: updates to this repository do not silently change product copies. For a reviewed refresh, ask Codex to **“Refresh Gori in this repo.”**

If your product has the earlier `factory-workflow`, `matt-engineering`, or `product-verification` folders, review local changes and replace their old pointer before using `gori-mode`. The installer does not delete those folders.

## Included skills

The core workflow is installed by default. The other skills are available when requested.

<!-- BEGIN GENERATED SKILLS -->

### Core workflow

| Skill | What it helps with |
| --- | --- |
| [`gori-mode`](skills/gori-mode/SKILL.md) | Route one selected repository task through triage, decisions, spec, implementation, review, user-path verification, and release gates. |
| [`gori-adopt`](skills/gori-adopt/SKILL.md) | Adopt or refresh Gori in an existing product repository using its task authority, context, Git rules, and verification gates. |
| [`gori-triage`](skills/gori-triage/SKILL.md) | Assess one user-selected existing issue or PR against current product behavior and route it to decisions, spec, implementation, or a concrete blocker. |
| [`gori-grill`](skills/gori-grill/SKILL.md) | Resolve missing product decisions on a selected Inbox or Needs Grill issue before writing its spec. |
| [`gori-domain-model`](skills/gori-domain-model/SKILL.md) | Resolve consequential domain vocabulary and relationships while adopting an existing repo or specifying a selected task. |
| [`gori-design`](skills/gori-design/SKILL.md) | Establish and maintain product-specific UI design guidance, then check affected screens during selected UI work. |
| [`gori-to-spec`](skills/gori-to-spec/SKILL.md) | Turn settled decisions for a selected issue into an implementation-ready spec with observable acceptance and proof. |
| [`gori-implement`](skills/gori-implement/SKILL.md) | Implement one selected task in verifiable vertical slices, using bug reproduction and behavior tests where useful. |
| [`gori-code-review`](skills/gori-code-review/SKILL.md) | Review a selected task's full diff against the original request and repository standards on separate axes. |
| [`gori-create-verification`](skills/gori-create-verification/SKILL.md) | Create a repo-local executable user-path verification contract when an existing product has none. |
| [`gori-verify`](skills/gori-verify/SKILL.md) | Prove a selected change through relevant automated checks and the affected real user journey, with revision-bound evidence. |
| [`gori-maintain-verification`](skills/gori-maintain-verification/SKILL.md) | Reconcile affected feature maps and drivers with final source before each task ships, repairing drift when found. |
| [`gori-release`](skills/gori-release/SKILL.md) | Carry a reviewed and verified task through the repository's authorized PR, CI, deployment and production gates. |

### Optional

| Skill | What it helps with |
| --- | --- |
| [`gtm`](skills/gtm/SKILL.md) | Define and refine ICPs, research reachable markets, qualify prospects, and develop signal-based outbound plays and content through a repeatable, project-independent GTM workflow. |
| [`vercel-resend-default`](skills/vercel-resend-default/SKILL.md) | Record or verify a repo's chosen Vercel-managed Resend email setup when the user selects that provider path. |

<!-- END GENERATED SKILLS -->

## Ownership and attribution

Gori is Pere Gregori's maintained adaptation and synthesis. Some skills draw on work by [Matt Pocock](https://github.com/mattpocock/skills), [Lauren Tan and pstack](https://github.com/backnotprop/pstack), and other credited authors. These are Gori versions, not upstream releases or endorsements. [Third-party notices](THIRD_PARTY_NOTICES.md) give the exact sources and licenses. The repository is [MIT licensed](LICENSE).

## Keep this README current

The skill table above is generated from the manifests under `skills/` and the installer's core list. After changing either, run:

```sh
python3 scripts/update_readme.py
python3 -m unittest discover -s tests -v
```

CI runs `python3 scripts/update_readme.py --check` and fails if the committed table has drifted. The introduction and usage guidance are edited by a person when the product changes; the catalog needs no hand-maintained copy.
