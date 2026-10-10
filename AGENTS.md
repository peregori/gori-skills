# gori-skills agent entry point

[`README.md`](README.md) is this repository's canonical context. Portable skill sources live under `skills/`; `scripts/install.py` copies selected snapshots into a product repo. The product repo's own `AGENTS.md`, task authority and release gates govern each use. This repo holds no product backlog or customer evidence.

For changes here, preserve project independence, upstream attribution, and safe installer defaults. Run `python3 -m unittest discover -s tests -v`, validate changed skill manifests, inspect the full public diff for local paths and sensitive material, and report any unproven behavior. Do not publish an unreviewed skill or overwrite installed product copies.
