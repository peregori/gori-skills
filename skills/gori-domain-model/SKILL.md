---
name: gori-domain-model
description: Resolve consequential domain vocabulary and relationships while adopting an existing repo or specifying a selected task. Use only when terms affect behavior or design.
---

# Sharpen the domain model

1. Read the repo's canonical context, any existing glossary and decisions, the selected issue, source names and tests. Treat the repo's existing vocabulary location as authoritative; do not create a second context layout.
2. Identify a term or relationship whose ambiguity changes an observable rule. Show concrete edge cases and compare the user's meaning with current code. Resolve product meaning with the user only when source and prior decisions cannot settle it.
3. Record each settled term in the existing glossary or canonical context, with a short definition and any important distinction. If no glossary exists, create a small one in the repo's established docs location only when multiple terms need a durable shared vocabulary; link it from the entry point. A single clarification can live in the selected spec or existing context. Keep implementation choices and task progress out of the glossary.
4. Reflect changed meaning in the selected spec, code, tests and affected verification map when relevant. Record a separate decision note only for a consequential tradeoff that future readers could not infer from source. Cite remaining disagreements as unresolved; do not silently choose a meaning.

This phase is conditional. An absent `GLOSSARY.md` is not a setup failure, and an existing domain section can already satisfy the need. Adapted from Matt Pocock's domain-modeling approach.
