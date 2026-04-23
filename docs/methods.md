# Methods

Methods are shared across all shieldbreaks; per-shieldbreak parameters live with each project under `prompts/shieldbreaks/<slug>/`.

## Search sources (NCBI-first)

In priority order:

1. **PubMed** (NCBI) — discovery via E-utilities (`esearch`, `esummary`, `efetch`)
2. **PubMed Central** (NCBI) — primary OA full-text source via `efetch db=pmc` using PMCIDs from PubMed
3. **ClinicalTrials.gov** (API v2) — registry-side ground truth on trial design, status, and posted results
4. **Europe PMC** — fallback for full text when PMC lacks the article
5. **Web search** — last-resort for grey literature, conference abstracts, press releases (treated as leads, not sources)

Raw responses for every run are archived in `data/shieldbreaks/<slug>/searches/<run-date>.json` with the exact query string, hit count, and fetch timestamp.

## Default screening rules (apply to every shieldbreak unless overridden)

- **Primary research only.** Narrative reviews, editorials, commentaries, and letters without primary data are excluded.
- **Systematic reviews and meta-analyses** are excluded from the trial table but surfaced separately as leads.
- The PI can opt in to including any of the above per shieldbreak during the elicitation step.

## Per-shieldbreak parameters

Each shieldbreak has its own:

- **`prompts/shieldbreaks/<slug>/search.md`** — indication, interventions, phases, dates, inclusion/exclusion
- **`prompts/shieldbreaks/<slug>/extract.md`** — column schema (and machine-readable mirror in `data/shieldbreaks/<slug>/schema.json`)

Both files are written by the `trialist_screener` agent during interactive elicitation. Hand-edits between runs are allowed; the agent surfaces the diff and confirms before treating them as authoritative.

## Provenance

- Every extracted value carries the source PMID, PMCID (when available), DOI, NCT ID, and fetch timestamp.
- The full-text tier used is recorded per row in `source_type`: `pmc_full_text`, `europepmc_full_text`, or `pubmed_abstract`.
- Conflicts between sources for the same trial are surfaced, not hidden.
- Data is append-only — corrections appear as new rows that supersede prior ones via a `supersedes` field.
