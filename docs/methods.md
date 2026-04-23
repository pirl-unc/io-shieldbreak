# Methods

## Search sources

In priority order:

1. **PubMed** — NCBI E-utilities (`esearch` + `efetch`)
2. **ClinicalTrials.gov** — API v2
3. **Europe PMC** — for full-text XML on open-access papers
4. **Web search** — fallback for grey literature, conference abstracts, press releases (treated as leads, not sources)

Raw responses for every run are archived in `data/searches/<query-slug>-<YYYY-MM-DD>.json` with the exact query string, hit count, and fetch timestamp.

## Inclusion / exclusion criteria

The current criteria live in [`prompts/search.md`](https://github.com/pirl-unc/io-shieldbreak/blob/main/prompts/search.md). They are set by the principal investigator and may evolve; criteria changes are recorded in commit history.

## Extraction schema

The current column schema lives in [`prompts/extract.md`](https://github.com/pirl-unc/io-shieldbreak/blob/main/prompts/extract.md), with the machine-readable version in [`data/schema.json`](https://github.com/pirl-unc/io-shieldbreak/blob/main/data/schema.json). Schema is versioned; added columns are backfilled by an explicit re-run, never silently.

## Provenance

- Every extracted value carries the source PMID, DOI, NCT ID, and fetch timestamp.
- Conflicts between sources for the same trial are surfaced, not hidden.
- Data is append-only — corrections appear as new rows that supersede prior ones via a `supersedes` field.
