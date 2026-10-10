# Independent project workspace

Use the project's existing GTM workspace. For a new one, default to `$HOME/.local/share/gori-skills/gtm/projects/<project-slug>/` unless the user chooses another private location. Never create a second copy in the product repository or a panel. A repository is an optional source of product evidence, not a prerequisite for GTM. Keep each project's data and decisions isolated.

## Resume or initialize

Read `project.md` and the latest run first. Load research, ideas, writing samples, or outcomes only as needed. Preserve existing IDs, sources, drafts, and historical runs. Do not invent a new backlog, create external tasks, or repeat answered setup questions.

For a new project, establish its identity, intended outcome, known audience hypotheses, offer/readiness evidence, founder time, and spending limit from available context. Ask only for missing decisions needed now. Geography, language, channels, and measurement can remain explicitly unknown during exploratory research. Writing samples matter when drafting, not when defining an ICP.

Create only the files needed for actual work:

| File | Ownership |
| --- | --- |
| `project.md` | Current goal and constraints, ICP matrix, source map, qualification/signal definitions, offer proof, channels, outcome sources, current stage and next step. |
| `research.md` | Sourced prospect observations and derived fit/timing decisions, when research begins. No operational send history. |
| `ideas.md` | Outbound plays and other candidate ideas with stable IDs, evidence, decisions, and experiment definitions. Existing social ideas remain valid. |
| `style.md` | Founder writing examples, approved preferences, avoided patterns, and pending proposals. |
| `outcomes.csv` | Published social-post metrics only, preserving the existing schema. |
| `runs/YYYY-MM-DD.md` | What was researched, recommended, selected, prepared, actually executed, observed, and left unresolved in that session. |

Use useful headings in `project.md`, preserving existing sections: `Goal and operating rhythm`, `Audience`, `Offer and live proof`, `Market sources and qualification`, `Channels and cadence`, `Communities and rules`, `Trusted sources`, `Creator inspiration`, `Analytics inputs`, `Constraints`, and `Current state and next step`. Keep detailed observations in research/runs. Date material decisions and label their status; founder-selected audiences remain hypotheses until tested.

No project-specific posting quota, budget, language, CRM, or product assumption belongs in the reusable skill. Set channel cadence independently in the project and subordinate it to founder time and useful material. If newer instructions change priorities, archive the old commitment in a run and update the current brief without erasing history.

## Evidence and ideas

Every usable observation names its source, observation date, event date if known, evidence status (`live`, `observed`, `hypothesis`, `unverified`), and the claim it supports. Record source accessibility and coverage limits. A public discussion proves the question was asked, not that an entire market shares it.

Use [market-research.md](market-research.md) for prospect records and [outbound-plays.md](outbound-plays.md) for campaign ideas. Simple social ideas need only an ID, audience problem, angle, source/date, evidence status, and decision (`new`, `selected`, `deferred`, `rejected`, with reason). Do not retroactively fabricate missing fields for old ideas.

In `style.md`, preserve `Own examples`, `Approved preferences`, `Avoid`, and `Proposed updates`. Cite the founder sample, explicit choice, or accepted edit supporting a preference. External techniques and AI judgments remain proposals until accepted; popularity is not proof that a technique works for this project.

## Results and spending

Keep campaign results with the play ID in the run: segment/rule version, channel, execution dates/status, measured sample and denominators, relevant replies, objections, useful product actions, repeat use or paid conversion when available, capture date, source, founder time, and cash spend. Mark counts as verified or founder-reported. Preserve zeros versus unavailable values. Do not collect private message text or personal customer details; de-identify feedback.

Store monthly spending as a compact ledger in the project's run records: currency, item/play, proposed/committed/actual amount, date, and receipt/source if available. Sum known spend and commitments without double counting; mark unknown charges and currency assumptions. Do not label unreported historical spending zero or calculate an exact remaining budget from incomplete data. A budget alone grants no spending authority.

For social metrics retain this schema:

```csv
run_date,source,source_post_id,channel,published_url,published_at,metrics_captured_at,metrics_updated_at,impressions,views,reach,likes,comments,shares,saves,clicks,engagement,engagement_rate,qualified_conversations,founder_assessment
```

Use [analytics-input.md](analytics-input.md) for source configuration and import/upsert rules. Leave missing values blank. Keep aggregate qualified conversations and campaign conversions in the run rather than inventing attribution to a post.

## Session record

Record only relevant sections: `Objective and scope`, `Evidence`, `ICP and qualification decisions`, `Candidates`, `Selected plays and drafts`, `Results and costs`, `Learning proposals`, and `Handoff`. Existing content-run headings remain readable; do not rewrite historical runs into a new schema. Multiple sessions on a date append clearly separated entries rather than overwriting prior work.

End with the current stage, what was actually completed, dependencies that remain unproven, and the exact next action. Distinguish a configured workflow, a research sample, a prepared campaign, and observed market results. Written instructions and a saved plan are not running automation or proof of successful GTM.
