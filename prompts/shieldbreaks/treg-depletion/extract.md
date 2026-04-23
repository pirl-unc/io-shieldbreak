# Treg depletion — extraction schema

**Shieldbreak:** `treg-depletion`
**Schema version:** 1
**Row grain:** one row per (study × tissue × timepoint-cluster × dose-cohort-when-reported).

A single publication that reports PBMC + tumor + TDLN readouts at baseline + post-treatment, across three dose cohorts, can yield many rows. That is intentional — the table's value is in the granular PD readouts.

## Columns

| # | Column | Type | Source | Missing-value rule |
|---|---|---|---|---|
| 1 | `row_id` | string | generated: `<pmid_or_nct>-<tissue>-<timepoint_cluster>-<cohort>` | required |
| 2 | `supersedes` | string or null | row_id of any prior row this replaces | null unless correcting |
| 3 | `intervention` | string | paper / protocol | required |
| 4 | `intervention_class` | enum | paper | required; one of: anti-CCR4, anti-CD25, Fc-enhanced-anti-CTLA-4, anti-CTLA-4, low-dose-cyclophosphamide, denileukin-diftitox, IL-2-variant, anti-CD39, anti-CD73, A2AR-antagonist, anti-CCR8, anti-GITR, anti-OX40, EZH2i, PI3Kdelta-i, chemo-other, JAKi, HDACi, HMA, radiation, combo, other |
| 5 | `combo_partners` | string or null | paper | null if monotherapy |
| 6 | `dose` | string or null | paper | null if not reported; note unit |
| 7 | `dose_cohort_label` | string or null | paper | e.g., "3 mg/kg", "DL1" |
| 8 | `indication` | string | paper | required; disease / condition |
| 9 | `patient_population` | string | paper | short phrase, e.g., "R/R CTCL after ≥1 systemic" |
| 10 | `n_treated_with_treg_measurement` | integer | paper | required; ≥3 to be eligible |
| 11 | `design_type` | enum | paper | one of: paired-pre-post, treated-vs-untreated, single-arm-descriptive, randomized-controlled, window-of-opportunity, healthy-volunteer-PD, case-series |
| 12 | `phase` | enum or null | paper / registry | 1, 1/2, 2, 2/3, 3, 4, translational, N/A |
| 13 | `nct_id` | string or null | paper / registry | null if not registered |
| 14 | `tissue` | enum | paper | one of: PBMC, tumor, TDLN, bone-marrow, ascites, pleural-effusion, CSF, skin, other |
| 15 | `tissue_detail` | string or null | paper | e.g., "on-treatment cycle-1-day-15 biopsy" |
| 16 | `treg_definition` | string | paper | gating strategy, e.g., "CD4+CD25hiFOXP3+CD127lo" |
| 17 | `gating_quality` | enum | paper | one of: FOXP3-confirmed, surface-only, functional-assay, mixed, unclear |
| 18 | `readout_type` | enum | paper | one of: absolute-count, frequency-of-CD4, frequency-of-lymphocytes, frequency-of-CD3, ratio-to-Teff, ratio-to-CD8, suppressive-function, other |
| 19 | `timepoint_cluster` | enum | paper | one of: baseline, early-on-treatment (≤ day 28), mid (day 29–90), late (> day 90), post-progression, off-treatment-recovery |
| 20 | `timepoint_detail` | string or null | paper | exact timing text, e.g., "C2D1" |
| 21 | `baseline_value` | string or null | paper | report as given |
| 22 | `baseline_stat_type` | enum or null | paper | one of: mean-sd, median-iqr, median-range, range, point-estimate, geometric-mean, not-reported |
| 23 | `post_value` | string or null | paper | post-treatment value at this timepoint |
| 24 | `post_stat_type` | enum or null | paper | same enum as baseline_stat_type |
| 25 | `change_direction` | enum | paper | one of: decrease, increase, no-change, mixed, not-reported |
| 26 | `change_magnitude` | string or null | paper | e.g., "~70% reduction", "2.1× increase" |
| 27 | `change_significance` | string or null | paper | e.g., "p=0.003", "n.s.", "not tested" |
| 28 | `change_mechanism` | enum | paper | one of: absolute-reduction, ratio-shift, expansion-with-ratio-shift, functional-impairment-only, null-result |
| 29 | `durability_days` | integer or null | paper | days from last dose to recovery of Treg baseline (or last measured on-treatment timepoint) |
| 30 | `durability_described` | string or null | paper | short phrase, e.g., "recovered by day 84" |
| 31 | `depletion_success` | enum | paper | one of: succeeded, partial, failed, not-assessed |
| 32 | `clinical_correlate` | string or null | paper | e.g., "higher ORR in deep depleters (p=0.04)" |
| 33 | `intent_to_deplete` | enum | paper | one of: mechanism-targeted, pre-specified-endpoint, exploratory-but-prespecified, incidental-but-measured |
| 34 | `notes` | string or null | paper | free text; any caveats, null results, disagreements |
| 35 | `pmid` | string or null | PubMed | null only if source is not indexed |
| 36 | `pmcid` | string or null | PMC | null if no PMC record |
| 37 | `doi` | string or null | paper | null if unknown |
| 38 | `first_author` | string | paper | last name + initial |
| 39 | `year` | integer | paper | publication year |
| 40 | `journal` | string | paper | short title |
| 41 | `title` | string | paper | full title |
| 42 | `source_type` | enum | generated | one of: pmc_full_text, europepmc_full_text, pubmed_abstract, ctgov_registry, other |
| 43 | `source_url` | string | generated | canonical URL used |
| 44 | `fetch_timestamp_utc` | ISO-8601 string | generated | when the row was extracted |

## Missing-value rules

- Numeric fields not reported: `null` + `notes` mention.
- Stat type must be specified whenever a value is given.
- Never guess a value. If a paper shows a bar chart without numbers and the number is not in the text or supplement, set the value to `null` and note "graph-only, no numeric value reported".
- If the paper reports a percentage change without absolute values, populate `change_magnitude` and leave `baseline_value` / `post_value` null.

## Side-list (not main table)

Systematic reviews and meta-analyses are captured in a separate JSONL (`data/shieldbreaks/treg-depletion/reviews.jsonl`) with a reduced schema: `pmid`, `pmcid`, `doi`, `first_author`, `year`, `journal`, `title`, `review_type`, `scope_summary`, `notes`, `fetch_timestamp_utc`. These render as a trailing section on the shieldbreak page.

## Row-grain examples

- Mogamulizumab Phase 1 in CTCL, reports PBMC + skin + tumor at baseline + C1D15 + C3D1 for a single dose: 1 × 3 × 3 = 9 rows.
- Ipilimumab 3 mg/kg vs 10 mg/kg in melanoma, PBMC and tumor at baseline + post-treatment: 2 cohorts × 2 tissues × 2 timepoint-clusters = 8 rows (though often papers collapse timepoints — one row per reported cluster, not per scheduled visit).
- Low-dose cyclophosphamide + vaccine, PBMC only, single timepoint: 1 row.
