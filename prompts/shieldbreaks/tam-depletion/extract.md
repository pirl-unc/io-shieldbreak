# Tumor-associated macrophage modulation — extraction schema

**Shieldbreak:** `tam-depletion` (display title: "Tumor-associated Macrophage Depletion, Inhibition, or Repolarization")
**Schema version:** 1
**Row grain:** one row per (study × tissue × timepoint-cluster × dose-cohort-when-reported).

A single publication reporting tumor + PBMC + TDLN readouts at baseline + early + mid across two dose cohorts can yield 2 × 3 × 3 = 18 rows. That is intentional — the table's value is in the granular PD readouts.

## Scope framing (v1, 2026-04-23)

The table captures **depletion OR inhibition OR repolarization** of TAMs. The three modes are orthogonal:

- `intervention_class` — the **intent** of the agent (e.g., `csf1r-inhibitor`, `cd40-agonist`).
- `change_mechanism` — the **observed** effect in the paper (`absolute-reduction`, `ratio-shift`, `repolarization`, etc.).

A CSF1R inhibitor that only repolarizes TAMs (no count change) → `intervention_class: csf1r-inhibitor` + `change_mechanism: repolarization`.
A CD40 agonist that clears tumor macrophages → `intervention_class: cd40-agonist` + `change_mechanism: absolute-reduction`.

### Success-mechanism semantics

`depletion_success: succeeded` semantics vary by `change_mechanism`:

- `absolute-reduction` → count reduction (with either absolute count or frequency-of-myeloid + pre/post stat).
- `ratio-shift` → favorable ratio shift (M1:M2 up, or CD163:CD86 down).
- `repolarization` → **multi-marker** M1-direction shift (≥ 2 markers co-moving; e.g., CD163 ↓ AND CD86 ↑). Single-marker IHC alone is NOT sufficient for `succeeded` on a repolarization row.
- `functional-impairment-only` → assay-level functional change (phagocytosis assay, suppression assay, cytokine-secretion assay pre/post).
- `null-result` → never `succeeded`.

## Columns

| # | Column | Type | Source | Missing-value rule |
|---|---|---|---|---|
| 1 | `row_id` | string | generated: `<pmid_or_nct>-<tissue>-<timepoint_cluster>-<cohort>` | required |
| 2 | `supersedes` | string or null | row_id of any prior row this replaces | null unless correcting |
| 3 | `intervention` | string | paper / protocol | required |
| 4 | `intervention_class` | enum | paper | required; one of: `csf1r-inhibitor`, `pi3kg-inhibitor`, `ccr2-ccr5-inhibitor`, `bisphosphonate`, `trabectedin-lurbinectedin`, `cd47-sirpa-blockade`, `cd24-blockade`, `cd40-agonist`, `tlr-agonist`, `sting-agonist`, `clever1-marco-blockade`, `lilrb2-trem2-blockade`, `other-repolarizing`, `combo` |
| 5 | `combo_partners` | string or null | paper | null if monotherapy |
| 6 | `dose` | string or null | paper | null if not reported; note unit |
| 7 | `dose_cohort_label` | string or null | paper | e.g., "1000 mg", "DL3" |
| 8 | `indication` | string | paper | required; disease / condition |
| 9 | `patient_population` | string | paper | short phrase |
| 10 | `n_treated_with_tam_measurement` | integer | paper | required; ≥3 |
| 11 | `design_type` | enum | paper | `paired-pre-post`, `treated-vs-untreated`, `single-arm-descriptive`, `randomized-controlled`, `window-of-opportunity`, `case-series` |
| 12 | `phase` | enum or null | paper / registry | `1`, `1/2`, `2`, `2/3`, `3`, `4`, `translational`, `N/A` |
| 13 | `nct_id` | string or null | paper / registry | null if not registered |
| 14 | `tissue` | enum | paper | `tumor`, `PBMC`, `TDLN`, `bone-marrow`, `ascites`, `pleural-effusion`, `skin`, `other` |
| 15 | `tissue_detail` | string or null | paper | e.g., "on-treatment biopsy cycle 2 day 15" |
| 16 | `tam_definition` | string | paper | gating strategy, e.g., "CD68+CD163+", "CD14+HLA-DR+ myeloid cluster 3 (scRNA)" |
| 17 | `gating_quality` | enum | paper | `CD68-CD163-based`, `CD68-CD206-based`, `CD14-CD16-based`, `CD68-MHCII-based`, `scRNA-macrophage-cluster`, `mIF-multiplex`, `CyTOF`, `single-marker-only`, `mixed-or-unclear` |
| 18 | `readout_type` | enum | paper | `absolute-count`, `frequency-of-CD45`, `frequency-of-myeloid`, `frequency-of-live`, `ratio-M1-to-M2`, `polarization-marker-shift`, `phagocytosis-function`, `scRNA-cluster-shift`, `other` |
| 19 | `timepoint_cluster` | enum | paper | `baseline`, `early-on-treatment` (≤ day 28), `mid` (day 29–90), `late` (> day 90), `post-progression`, `off-treatment-recovery` |
| 20 | `timepoint_detail` | string or null | paper | exact timing text, e.g., "C2D1" |
| 21 | `baseline_value` | string or null | paper | report as given |
| 22 | `baseline_stat_type` | enum or null | paper | `mean-sd`, `median-iqr`, `median-range`, `range`, `point-estimate`, `geometric-mean`, `not-reported` |
| 23 | `post_value` | string or null | paper | post-treatment value |
| 24 | `post_stat_type` | enum or null | paper | same enum as baseline_stat_type |
| 25 | `change_direction` | enum | paper | `decrease`, `increase`, `no-change`, `mixed`, `not-reported` |
| 26 | `change_magnitude` | string or null | paper | e.g., "~60% reduction in CD163+ count", "M1:M2 ratio increased 3-fold" |
| 27 | `change_significance` | string or null | paper | e.g., "p=0.003", "n.s.", "not tested" |
| 28 | `change_mechanism` | enum | paper | `absolute-reduction`, `ratio-shift`, `repolarization`, `expansion-with-repolarization`, `functional-impairment-only`, `null-result` |
| 29 | `pct_change` | float or null | computed | Signed relative percent change in TAM measure (negative = reduction). Populated when the paper gives a clean single-number headline or unambiguous fold-change. Null when qualitative-only or when authors state no significant change. For repolarization rows with a single marker quantified (e.g., "CD163 ↓ 42%"), populate from that marker and cite the fragment. |
| 30 | `pct_change_stat` | enum or null | computed | `point`, `mean`, `median`, `range-midpoint`, `fold-derived` |
| 31 | `pct_change_source` | string or null | computed | Short string citing the text fragment that sourced `pct_change` |
| 32 | `durability_days` | integer or null | paper | days to recovery or last measured on-treatment timepoint |
| 33 | `durability_described` | string or null | paper | short phrase |
| 34 | `depletion_success` | enum | paper | `succeeded`, `partial`, `failed`, `not-assessed`. Success semantics vary by change_mechanism — see scope-framing section. |
| 35 | `clinical_correlate` | string or null | paper | e.g., "deeper CD163 reduction associated with clinical response (p=0.02)" |
| 36 | `intent_to_deplete` | enum | paper | `mechanism-targeted`, `pre-specified-endpoint`, `exploratory-but-prespecified`, `incidental-but-measured` |
| 37 | `notes` | string or null | paper | free text; caveats, null results, conflicts |
| 38 | `pmid` | string or null | PubMed | null only if source is not indexed |
| 39 | `pmcid` | string or null | PMC | null if no PMC record |
| 40 | `doi` | string or null | paper | null if unknown |
| 41 | `first_author` | string | paper | last name + initial |
| 42 | `last_author` | string or null | paper | senior author, when identifiable |
| 43 | `year` | integer | paper | publication year |
| 44 | `journal` | string | paper | short title |
| 45 | `title` | string | paper | full title |
| 46 | `source_type` | enum | generated | `pmc_full_text`, `europepmc_full_text`, `pubmed_abstract`, `ctgov_registry`, `other` |
| 47 | `source_url` | string | generated | canonical URL used |
| 48 | `fetch_timestamp_utc` | ISO-8601 string | generated | when the row was extracted |

## Missing-value rules

- Numeric fields not reported: `null` + note.
- Stat type must be specified whenever a value is given.
- Never guess. Bar-chart-only with no numeric: `null` + "graph-only, no numeric value reported".
- If only a percent change is given (no absolute values), populate `change_magnitude` and leave `baseline_value` / `post_value` null.

## Populating typed pct_change fields at extraction

- Signed percent (e.g., "~60% reduction"): `pct_change = -60.0`, `pct_change_stat: point`.
- Range (e.g., "30–70% reduction"): midpoint, `pct_change_stat: range-midpoint`.
- Fold-change: 3× reduction → `-66.7`, `pct_change_stat: fold-derived`.
- Repolarization with a single-marker quantification: use that marker's signed delta.
- Null result: leave `pct_change` null, set `change_mechanism: null-result`.
- Always populate `pct_change_source` with the verbatim text fragment.

## Side-list (not main table)

Systematic reviews and meta-analyses → `reviews.jsonl` with reduced schema: `pmid`, `pmcid`, `doi`, `first_author`, `year`, `journal`, `title`, `review_type`, `scope_summary`, `notes`, `fetch_timestamp_utc`.

## Exclusions side-list

Screened-out papers → `excluded.jsonl` with a first-line reason. One row per excluded PMID (not per PMID × tissue).

## Row-grain examples

- Emactuzumab Phase 1 in diffuse-type TGCT reporting tumor CD163+ and CD68+ at baseline + C1D14 + C3D1 across 3 dose cohorts: 1 tissue × 3 timepoint-clusters × 3 cohorts = 9 rows.
- Cabiralizumab + nivolumab in pancreatic cancer with tumor + PBMC at baseline + post-treatment: 2 tissues × 2 timepoint-clusters = 4 rows.
- CD40 agonist monotherapy with tumor scRNA cluster shift at baseline + C2D1 (single cohort): 2 rows.
- CD47 blockade (magrolimab + rituximab) reporting phagocytosis-function pre/post + tumor CD68 counts: 2 rows per timepoint (one `readout_type: phagocytosis-function` + one `readout_type: absolute-count`), disambiguated by `row_id` suffix.
