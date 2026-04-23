# Runs

> _Auto-generated from `data/runs.jsonl`. One row per successful agent run, newest first._

| Date (UTC) | Agent | Shieldbreak | Action | Hits → Kept | Rows added | Source tiers (PMC / EPMC / abstract) | Notes | Commit |
|------------|-------|-------------|--------|-------------|------------|--------------------------------------|-------|--------|
| 2026-04-23 16:36 | trialist_screener | [treg-depletion](shieldbreaks/treg-depletion/index.md) | new | 1178 → 27 | 40 | 0 / 0 / 40 | New shieldbreak; 27 studies screened; 40 rows at (study × tissue × timepoint-cluster) granularity; numeric values often abstract-only with notes; Attia-vs-Dannull DD conflict surfaced. | [6da20c2](https://github.com/pirl-unc/io-shieldbreak/commit/6da20c2) |

## What this page is

A cross-shieldbreak audit log of every successful agent run on this repo. Each row records what was done, against which shieldbreak, and where the data went.

- **Action** — one of `new` (new shieldbreak created), `refresh` (re-run of an existing shieldbreak), `backfill` (filling missing fields on existing rows), `schema` (schema bump only, no data changes).
- **Hits → Kept** — hits returned by the search vs. hits kept after deduplication and screening.
- **Source tiers** — counts of which full-text source was used per kept paper: PubMed Central / Europe PMC / PubMed abstract.
- **Notes** — schema bumps, conflicts surfaced, manual interventions.
- **Commit** — short SHA of the commit that recorded the run (links to GitHub).

Failed or aborted runs are not logged here — they leave their per-run search file in `data/shieldbreaks/<slug>/searches/` for postmortem.
