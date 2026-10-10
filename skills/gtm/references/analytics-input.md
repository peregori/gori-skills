# Analytics inputs

Read this when reviewing published social results. The project's `project.md` → `Analytics inputs` names each approved source, access method, and expected publication set. Import available platform metrics first, then ask the founder once for missing metrics and human judgments. Other GTM outcomes belong in the run.

## Approved automatic source

Use only an origin, account, and read-only path explicitly configured in the project workspace. Verify the browser is on that origin before reading data; reject redirects or sign-in pages on another origin. Follow the active client's approved browser workflow. Never inspect, copy, or store cookies, local storage, passwords, tokens, or request headers. Do not publish, schedule, refresh connections, or mutate product data while importing metrics.

Map each published post to the `outcomes.csv` schema using a stable source post ID when available; otherwise use source, channel, public URL, and publication time. Record the metric capture time and any provider update time. An unavailable metric stays blank and a measured zero stays `0`.

Upsert by source and stable post ID; before inserting, also compare source, channel, public URL, and publication time. If a stronger ID appears later, upgrade the existing row. Replace only metrics present in a newer snapshot. An older snapshot must not overwrite newer values, and a changed metric must not create a second row.

If access or coverage is partial, import only confirmed rows and identify the missing posts or fields. Use prior final links or the founder's publication list to determine expected posts. If neither exists, state that coverage is unknown and ask once for the missing links and metrics.

## Manual sources and human outcomes

For manual sources, request one compact block per post: published URL and time, metric capture time, and available impressions, views, reach, likes, comments, shares, saves, clicks, engagement, or engagement rate. Do not require every metric.

Platform analytics do not identify qualified conversations or prove that the audience was useful. Ask for a de-identified qualified-conversation count and short founder assessment when available. Keep weekly aggregates in the run's `Evidence` section; do not invent post attribution.
