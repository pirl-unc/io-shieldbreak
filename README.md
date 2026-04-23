# io-shieldbreak

> **WIP / experiment.** Curated collection of clinical trial tables on immune-checkpoint shield-breaking strategies.

The site is organized by **shieldbreak** — each shieldbreak is one research question with its own search parameters, extraction schema, and sortable trial table. The `trialist_screener` Claude Code subagent runs each shieldbreak end-to-end: elicits parameters interactively, queries the medical literature (NCBI-first), screens hits, extracts structured data, and publishes the resulting table.

**Site:** https://pirl-unc.github.io/io-shieldbreak/

## Architecture

- **Search** — PubMed → PMC → ClinicalTrials.gov → Europe PMC → web (NCBI-first); raw responses archived per run
- **Screen** — primary-research-only by default; per-shieldbreak inclusion/exclusion in `prompts/shieldbreaks/<slug>/search.md`
- **Extract** — per-shieldbreak column schema in `prompts/shieldbreaks/<slug>/extract.md`; rows appended to `data/shieldbreaks/<slug>/trials.jsonl`
- **Publish** — agent regenerates `docs/shieldbreaks/<slug>/index.md` from the JSONL; `pages.yml` deploys via `mkdocs gh-deploy`

The orchestrator is `.claude/agents/trialist_screener.md` — a project-scoped Claude Code subagent.

## Repo layout

```
.claude/agents/         # subagent definition (trialist_screener)
prompts/shieldbreaks/   # per-shieldbreak editorial specs
  <slug>/
    search.md           # search params, screening criteria
    extract.md          # extraction column schema
data/shieldbreaks/      # per-shieldbreak append-only ground truth
  <slug>/
    trials.jsonl        # one extracted trial per line
    schema.json         # machine-readable column schema
    searches/           # raw search responses, one file per run
docs/                   # MkDocs site (regenerable)
  index.md              # site landing
  methods.md            # shared methodology
  shieldbreaks/
    index.md            # directory of all shieldbreaks
    <slug>/
      index.md          # per-shieldbreak landing + trial table
scripts/                # pure-Python utilities
.github/workflows/      # site deploy
```

## Status

- **Phase A (current):** scaffold + agent definition; no shieldbreaks yet.
- **Phase B:** first shieldbreak — define a project, run the agent end-to-end.
- **Phase C:** scheduled refresh trigger across all shieldbreaks.
