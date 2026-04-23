# Runs

> _Auto-generated from `data/runs.jsonl`. One row per successful agent run, newest first._

| Date (UTC) | Agent | Shieldbreak | Action | Hits → Kept | Rows added / updated | Source tiers (PMC / EPMC / abstract) | Notes | Commit |
|------------|-------|-------------|--------|-------------|----------------------|--------------------------------------|-------|--------|
| 2026-04-23 19:05 | trialist_screener | [treg-depletion](shieldbreaks/treg-depletion/index.md) | refresh (scope-expansion) | 306 → 13 | 13 / 0 | 11 / 0 / 2 | Scope broadened from depletion-only to depletion OR inhibition OR destabilization. 11 new intervention-family queries (anti-TNFR2, anti-TIGIT, EP4-antagonist, DNMTi/HMA, HDACi, CELMoD/IKZF2, PI3Kδ, NRP1, GITR/OX40 function, FoxP3 destabilization, iberdomide). 13 clinical rows added across 11 new studies. 0 functional-impairment-only rows — no clinical paper reported suppressive function without a coincident count/frequency change. Honest gaps: anti-TNFR2 clinical PD literature does not exist in PubMed (Torrey 2019 Sézary is ex-vivo only); IKZF2-selective degraders, EP4 antagonists, NRP1, CCR8-CAR-T also 0 human rows. Surfaced surprises: CELMoDs (iberdomide) and DNMTi (decitabine) mostly INCREASE Tregs (Lipsky 2022 SLE +104.9% p<0.001; Han 2021 ITP Treg count+function up; Penter 2023 ipilimumab expanded BM Tregs in AML/MDS) — opposite to scope-expansion hypothesis. Context-dependent HDACi: entinostat/vorinostat DECREASE tumor Tregs (Terranova-Barberio 2020 11.8%→2.9%, p=0.0067); panobinostat INCREASES Tregs in HIV (Brinkmann 2018 +40%, p=0.003). Anti-TIGIT (Guan 2024 CITYSCAPE/GO30103) shows PBMC Treg decrease only, not tumor. | _pending_ |
| 2026-04-23 17:15 | trialist_screener | [treg-depletion](shieldbreaks/treg-depletion/index.md) | backfill | — | 0 / 38 | 28 / 0 / 10 | Full-text backfill pass; 28/38 rows now have baseline+post numerics (74%); 2 rows excluded to `excluded.jsonl` (Telang 2011 no Treg measurement; Galsky 2025 PORTER not Treg-targeted); Liao-ascites reclassified `succeeded`→`partial`; Hamid intent reclassified to `incidental-but-measured`; 6 new PMCIDs; new conflict Ager-vs-Sharma (Fc engineering reconciles) and Huang tremelimumab quantitative INCREASE in TI-Tregs corroborates Sharma null. | [0dd399c](https://github.com/pirl-unc/io-shieldbreak/commit/0dd399c) |
| 2026-04-23 16:36 | trialist_screener | [treg-depletion](shieldbreaks/treg-depletion/index.md) | new | 1178 → 27 | 40 / 0 | 0 / 0 / 40 | New shieldbreak; 27 studies screened; 40 rows at (study × tissue × timepoint-cluster) granularity; numeric values often abstract-only with notes; Attia-vs-Dannull DD conflict surfaced. | [6da20c2](https://github.com/pirl-unc/io-shieldbreak/commit/6da20c2) |

## What this page is

A cross-shieldbreak audit log of every successful agent run on this repo. Each row records what was done, against which shieldbreak, and where the data went.

- **Action** — one of `new` (new shieldbreak created), `refresh` (re-run of an existing shieldbreak), `backfill` (filling missing fields on existing rows), `schema` (schema bump only, no data changes).
- **Hits → Kept** — hits returned by the search vs. hits kept after deduplication and screening.
- **Source tiers** — counts of which full-text source was used per kept paper: PubMed Central / Europe PMC / PubMed abstract.
- **Notes** — schema bumps, conflicts surfaced, manual interventions.
- **Commit** — short SHA of the commit that recorded the run (links to GitHub).

Failed or aborted runs are not logged here — they leave their per-run search file in `data/shieldbreaks/<slug>/searches/` for postmortem.
