# io-shieldbreak

A curated collection of clinical-trial tables and critical reviews of manuscripts on strategies to **overcome resistance to cancer immunotherapies** — combinations and modalities aimed at restoring response in tumors that resist immune checkpoint inhibitors, adoptive cell therapies (CAR-T, TIL), cancer vaccines, cytokine therapies, bispecifics, oncolytic viruses, and other immuno-oncology agents.

The site is organized by **shieldbreak** — each shieldbreak is one research question (one resistance axis, one class of intervention) with its own search parameters, extraction schema, sortable trial table, and manuscript critique.

## What's here

- **[Shieldbreaks](shieldbreaks/index.md)** — directory of all project queries, each with a trial table and a critique report
- **[Methods](methods.md)** — search sources, screening defaults, extraction conventions, critique conventions

## How it's maintained

Each shieldbreak is screened and extracted by the `trialist_screener` Claude Code subagent against criteria the principal investigator sets per project, then critically appraised by the companion `trialist_skeptic` subagent — which reads the ingested manuscripts in full, verifies that extracted values match the source, and publishes a structured methodological critique. Raw search responses are archived per run, data files are append-only, and corrections supersede prior rows rather than overwriting them.
