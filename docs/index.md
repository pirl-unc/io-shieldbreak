# io-shieldbreak

A curated, regularly-refreshed table of clinical trial reports relevant to **immune-checkpoint shield-breaking** strategies — combinations and modalities aimed at restoring response in tumors that resist single-agent checkpoint blockade.

## What's here

- **[Trials](trials.md)** — the table. Sortable, searchable, with source citations on every row.
- **[Methods](methods.md)** — search sources, inclusion criteria, and extraction schema.

## How it's maintained

Each row is screened and extracted by the `trialist_screener` Claude Code subagent against criteria the principal investigator sets in `prompts/search.md` and `prompts/extract.md`. Raw search responses are archived per run; the data file is append-only; corrections supersede prior rows rather than overwriting them.

## Status

Phase A — scaffold deployed; data set empty pending first run with real search parameters.
