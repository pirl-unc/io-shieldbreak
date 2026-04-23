# Shieldbreaks

A "shieldbreak" is a single project query — one research question about a mechanism of resistance to a cancer immunotherapy (checkpoint blockade, adoptive cell therapy, vaccine, cytokine, bispecific, oncolytic virus, or other immuno-oncology modality), with its own search parameters, extraction schema, trial table, and manuscript critique. Each lives in its own subdirectory so it can evolve independently of the others.

## Active shieldbreaks

| Shieldbreak | Rows | Last updated |
|---|---|---|
| [Treg Depletion](treg-depletion/index.md) | 38 | 2026-04-23 |

## Adding a shieldbreak

Invoke the `trialist_screener` Claude Code subagent and answer "new shieldbreak" when prompted. The agent will:

1. Ask for a project name and propose a slug (kebab-case)
2. Elicit the search parameters → write to `prompts/shieldbreaks/<slug>/search.md`
3. Elicit the extraction schema → write to `prompts/shieldbreaks/<slug>/extract.md` and `data/shieldbreaks/<slug>/schema.json`
4. Run the search, screen, extract → append to `data/shieldbreaks/<slug>/trials.jsonl`
5. Generate `docs/shieldbreaks/<slug>/index.md` with the trial table
6. Add a row to this index page linking to the new project

Once a shieldbreak has trial rows, the companion `trialist_skeptic` subagent reads the ingested manuscripts in full, verifies the extracted fields against the source, and publishes `docs/shieldbreaks/<slug>/critique.md` — a per-paper and cross-paper methodological appraisal.
