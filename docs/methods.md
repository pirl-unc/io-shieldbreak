# Methods

Methods are shared across all shieldbreaks; per-shieldbreak parameters live with each project under `prompts/shieldbreaks/<slug>/`.

## Scope

Each shieldbreak targets a mechanism of resistance to a specific class of cancer immunotherapy. The site is not limited to immune checkpoint inhibitors: shieldbreaks may cover resistance and combination strategies for adoptive cell therapies (CAR-T, TIL, TCR-T), cancer vaccines, cytokine therapies, bispecific antibodies, oncolytic viruses, and other immuno-oncology modalities. The per-shieldbreak `search.md` defines exactly which interventions are in scope for that project.

## Two agents, two outputs

- **`trialist_screener`** — searches the literature, screens hits, extracts structured rows into `data/shieldbreaks/<slug>/trials.jsonl`, and publishes the sortable trial table at `docs/shieldbreaks/<slug>/index.md`.
- **`trialist_skeptic`** — reads the ingested manuscripts in full, verifies that extracted values match the source, critically appraises each paper's methods and claims, and publishes `docs/shieldbreaks/<slug>/critique.md` with per-paper critiques and a cross-paper synthesis. Persistent critique rows live in `data/shieldbreaks/<slug>/critiques.jsonl`.

The division of labor is strict: the screener owns `trials.jsonl`; the skeptic owns `critiques.jsonl` and `critique.md`. When the skeptic finds a discrepancy between an extracted value and the source, it flags the discrepancy in the critique rather than editing `trials.jsonl` directly.

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
