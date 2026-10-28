# Project lead adapter

Some projects keep their prospects in their own product, next to the customers they become, and expose a small command for this skill. When the project brief names one, that command is the system of record for prospect records. This skill stays project-independent: it calls whatever adapter the brief names and never assumes one exists.

## The contract

An adapter is one command with these operations. Arguments and output follow the project's own help text; read it (`<command>` with no operation) before the first use in a session.

| Operation | Use |
| --- | --- |
| `list [filters]` | Read the pool before researching, to skip known prospects and see status, source, play and do-not-contact. |
| `show <id>` | Read one prospect's details and timeline before preparing a play for it. |
| `import <file.jsonl \| ->` | Add reviewed prospects: one JSON object per line in the project's lead shape, with the source and play named. The adapter deduplicates and suppresses; report its created/merged/suppressed/rejected counts. |
| `status <id> <status>` | Record a qualification decision the founder made or approved. |
| `note <id> <text>` | Attach the evidence behind a decision: the source, date and claim, not private message text. |
| `export` | Read the whole pool for a learning or deduplication pass. |

## Rules

- **Preview, then import.** Show the founder the rows you will import, with each row's source and fit evidence. Import only reviewed rows. A research shortlist is still not send-ready.
- **No sending and no paid runs.** The adapter never sends email or starts paid data runs. Approved sends and data runs happen in the project's own panel, under the founder's approval and that product's safeguards. Do not look for a workaround.
- **Respect suppression.** A suppressed or do-not-contact prospect is reported, never re-added under another key. Do not record personal details a do-not-contact entry removed.
- **One record.** With an adapter, keep prospect records there and only research evidence and decisions in `research.md`, referring to the adapter's IDs. Do not keep a second contact list or send history in the workspace.
- **Fail visibly.** If the adapter refuses (no database, wrong project, invalid rows), stop and report the message. Do not fall back to writing prospects into workspace files silently.
- **Keep the project's boundaries.** The adapter runs on the founder's machine with that project's configuration. Never read or copy its credentials, and never point it at a database the brief does not name.
