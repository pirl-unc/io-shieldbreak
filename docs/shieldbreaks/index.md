# Shieldbreaks

A "shieldbreak" is a single project query — one research question about a mechanism of resistance to a cancer immunotherapy (checkpoint blockade, adoptive cell therapy, vaccine, cytokine, bispecific, oncolytic virus, or other immuno-oncology modality), with its own search parameters, extraction schema, trial table, and manuscript critique. Each lives in its own subdirectory so it can evolve independently of the others.

## Active shieldbreaks

| Shieldbreak | Rows | Last updated | Critique |
|---|---|---|---|
| [Tumor-associated Macrophage Depletion, Inhibition, or Repolarization](tam-depletion/index.md) | 37 | 2026-04-24 | — |
| [Treg Depletion and/or Inhibition](treg-depletion/index.md) | 51 | 2026-04-23 | [critique](treg-depletion/critique.md) |

## Adding a shieldbreak

Invoke the `trialist_screener` Claude Code subagent and answer "new shieldbreak" when prompted. The agent will:

1. Ask for a project name and propose a slug (kebab-case)
2. Elicit the search parameters → write to `prompts/shieldbreaks/<slug>/search.md`
3. Elicit the extraction schema → write to `prompts/shieldbreaks/<slug>/extract.md` and `data/shieldbreaks/<slug>/schema.json`
4. Run the search, screen, extract → append to `data/shieldbreaks/<slug>/trials.jsonl`
5. Generate `docs/shieldbreaks/<slug>/index.md` with the trial table
6. Add a row to this index page linking to the new project

Once a shieldbreak has trial rows, the companion `trialist_skeptic` subagent reads the ingested manuscripts in full, verifies the extracted fields against the source, and publishes `docs/shieldbreaks/<slug>/critique.md` — a per-paper and cross-paper methodological appraisal. The skeptic also assesses, for every paper, **counter-productive mechanisms** by which the intervention's MoA may undermine the shieldbreak's broader target effect (e.g., anti-CCR4 depleting CCR4+ CD8 effector-memory cells alongside Tregs) even when the proximal endpoint is met.

With the screener and skeptic runs complete, the `trialist_prescriber` subagent then synthesizes a top-level narrative: it reads `trials.jsonl` and `critiques.jsonl`, groups rows into interventions or intervention classes under PI-confirmed granularity, and for each selected intervention (3–7 total) writes a short section covering evidence base, likelihood of the desired effect, toxicity profile, counter-productive mechanisms, practical considerations, and a ranked-position rationale. The output is published as `docs/shieldbreaks/<slug>/scope_summary.md` and inlined at the top of the shieldbreak page under the `## Scope summary` heading; a Ranked prioritization table at the end weighs Likelihood × Toxicity × Counter-productive MoA into an Overall column. Rankings reflect the shieldbreak's Target effect as written; re-scoping it toward a downstream goal shifts the weights.
