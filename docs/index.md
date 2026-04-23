# io-shieldbreak

A curated collection of clinical trial tables on **immune-checkpoint shield-breaking** strategies — combinations and modalities aimed at restoring response in tumors that resist single-agent checkpoint blockade.

The site is organized by **shieldbreak** — each shieldbreak is one research question with its own search parameters, extraction schema, and sortable trial table.

## What's here

- **[Shieldbreaks](shieldbreaks/index.md)** — directory of all project queries
- **[Methods](methods.md)** — search sources, screening defaults, extraction conventions

## How it's maintained

Each shieldbreak is screened and extracted by the `trialist_screener` Claude Code subagent against criteria the principal investigator sets per project. Raw search responses are archived per run, data files are append-only, and corrections supersede prior rows rather than overwriting them.
