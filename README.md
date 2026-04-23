# io-shieldbreak

> **WIP / experiment.** Curated clinical-trial tables and critical reviews of manuscripts on strategies to overcome resistance to cancer immunotherapies — immune checkpoint inhibitors, adoptive cell therapies, cancer vaccines, cytokines, bispecifics, oncolytic viruses, and other immuno-oncology modalities.

The site is organized by **shieldbreak** — each shieldbreak is one research question with its own search parameters, extraction schema, sortable trial table, and manuscript critique. Two Claude Code subagents split the work: `trialist_screener` elicits parameters interactively, queries the medical literature (NCBI-first), screens hits, extracts structured data, and publishes the resulting table; `trialist_skeptic` then reads the ingested manuscripts in full, verifies extracted values against the source, and publishes a per-paper and cross-paper methodological critique.

**Site:** https://pirl-unc.github.io/io-shieldbreak/

## Architecture

- **Search** — PubMed → PMC → ClinicalTrials.gov → Europe PMC → web (NCBI-first); raw responses archived per run
- **Screen** — primary-research-only by default; per-shieldbreak inclusion/exclusion in `prompts/shieldbreaks/<slug>/search.md`
- **Extract** — per-shieldbreak column schema in `prompts/shieldbreaks/<slug>/extract.md`; rows appended to `data/shieldbreaks/<slug>/trials.jsonl`
- **Publish** — agent regenerates `docs/shieldbreaks/<slug>/index.md` from the JSONL; `pages.yml` deploys via `mkdocs gh-deploy`
- **Critique** — `trialist_skeptic` reads the ingested papers in full, verifies extracted values against the source, and publishes `docs/shieldbreaks/<slug>/critique.md`; per-paper critiques persist in `data/shieldbreaks/<slug>/critiques.jsonl`

The orchestrators are `.claude/agents/trialist_screener.md` (search/extract) and `.claude/agents/trialist_skeptic.md` (critique) — project-scoped Claude Code subagents.

## Repo layout

```
.claude/agents/         # subagent definitions (trialist_screener, trialist_skeptic)
prompts/shieldbreaks/   # per-shieldbreak editorial specs
  <slug>/
    search.md           # search params, screening criteria
    extract.md          # extraction column schema
data/shieldbreaks/      # per-shieldbreak append-only ground truth
  <slug>/
    trials.jsonl        # one extracted trial per line (owned by screener)
    critiques.jsonl     # one manuscript critique per line (owned by skeptic)
    schema.json         # machine-readable column schema
    searches/           # raw search responses, one file per run
    full_text/          # cached PMC/Europe PMC full text used for critique
docs/                   # MkDocs site (regenerable)
  index.md              # site landing
  methods.md            # shared methodology
  shieldbreaks/
    index.md            # directory of all shieldbreaks
    <slug>/
      index.md          # per-shieldbreak landing + trial table
      critique.md       # per-paper + cross-paper methodological critique
scripts/                # pure-Python utilities
.github/workflows/      # site deploy
```

## Status

- **Phase A (current):** scaffold + agent definition; no shieldbreaks yet.
- **Phase B:** first shieldbreak — define a project, run the agent end-to-end.
- **Phase C:** scheduled refresh trigger across all shieldbreaks.
