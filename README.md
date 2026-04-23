# io-shieldbreak

> **WIP / experiment.** Curated, regularly-refreshed table of clinical trial reports relevant to immune-checkpoint shield-breaking strategies.

A web-published, sortable table of clinical trial reports. The `trialist_screener` Claude Code subagent searches the medical literature on demand, screens hits against user-defined inclusion criteria, extracts structured data per a user-defined column schema, and appends the results to an append-only data file. The site is regenerated from the data on every commit.

**Site:** https://pirl-unc.github.io/io-shieldbreak/

## Architecture

- **Search** — PubMed (E-utilities), ClinicalTrials.gov (API v2), Europe PMC; raw responses archived per run in `data/searches/`
- **Screen** — inclusion/exclusion criteria in `prompts/search.md`
- **Extract** — column schema in `prompts/extract.md`; rows appended to `data/trials.jsonl`
- **Publish** — `scripts/build_table.py` regenerates `docs/trials.md` from the JSONL; `pages.yml` deploys via `mkdocs gh-deploy`

The orchestrator is `.claude/agents/trialist_screener.md` — a project-scoped Claude Code subagent.

## Repo layout

```
.claude/agents/     # subagent definition (trialist_screener)
prompts/            # editorial specs (search criteria, extraction template)
scripts/            # pure-Python utilities (search fetch, table build)
data/               # append-only ground truth
  trials.jsonl       # one extracted trial per line
  searches/          # raw search responses, one file per run
  schema.json        # current extraction schema
docs/               # MkDocs site (regenerable from data/)
.github/workflows/  # site deploy
```

## Status

- **Phase A (current):** scaffold + agent definition; empty data set.
- **Phase B:** first search run with real parameters; populate `prompts/search.md` and `prompts/extract.md`.
- **Phase C:** scheduled refresh trigger.
