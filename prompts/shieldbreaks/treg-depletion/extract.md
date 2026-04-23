# Treg depletion and/or inhibition — extraction schema

**Shieldbreak:** `treg-depletion` (display title: "Treg Depletion and/or Inhibition")
**Schema version:** 2
**Row grain:** one row per (study × tissue × timepoint-cluster × dose-cohort-when-reported).

A single publication that reports PBMC + tumor + TDLN readouts at baseline + post-treatment, across three dose cohorts, can yield many rows. That is intentional — the table's value is in the granular PD readouts.

## Scope expansion (schema v2, 2026-04-23)

The table captures **depletion OR functional inhibition OR destabilization** of Tregs. Specifically, `change_mechanism: functional-impairment-only` is a **valid, wanted, first-class outcome** — not a consolation label. For inhibition rows:

- `depletion_success: succeeded` applies under functional-impairment-only **only if** the paper demonstrates a suppressive-function impairment (in vitro suppression assay, FoxP3 / TSDR / Helios destabilization readout). Frequency changes alone are not sufficient evidence for `succeeded` under this mechanism.
- `readout_type: suppressive-function` should be used for these rows.
- If the paper reports a quantitative fold-suppression change (e.g., "Treg suppression of CD8 proliferation dropped from 78% to 32%"), populate `pct_change` from the delta in suppression percentage, `pct_change_stat: point`, and cite the text fragment in `pct_change_source`.

## Columns

| # | Column | Type | Source | Missing-value rule |
|---|---|---|---|---|
| 1 | `row_id` | string | generated: `<pmid_or_nct>-<tissue>-<timepoint_cluster>-<cohort>` | required |
| 2 | `supersedes` | string or null | row_id of any prior row this replaces | null unless correcting |
| 3 | `intervention` | string | paper / protocol | required |
| 4 | `intervention_class` | enum | paper | required; one of: anti-CCR4, anti-CD25, Fc-enhanced-anti-CTLA-4, anti-CTLA-4, low-dose-cyclophosphamide, denileukin-diftitox, IL-2-variant, anti-CD39, anti-CD73, A2AR-antagonist, anti-CCR8, anti-GITR, anti-OX40, anti-TNFR2, anti-TIGIT, EP4-antagonist, EZH2i, PI3Kdelta-i, DNMTi, HDACi, HMA, JAKi, chemo-other, radiation, CAR-T-Treg-targeted, combo, other |
| 5 | `combo_partners` | string or null | paper | null if monotherapy |
| 6 | `dose` | string or null | paper | null if not reported; note unit |
| 7 | `dose_cohort_label` | string or null | paper | e.g., "3 mg/kg", "DL1" |
| 8 | `indication` | string | paper | required; disease / condition |
| 9 | `patient_population` | string | paper | short phrase |
| 10 | `n_treated_with_treg_measurement` | integer | paper | required; ≥3 |
| 11 | `design_type` | enum | paper | paired-pre-post, treated-vs-untreated, single-arm-descriptive, randomized-controlled, window-of-opportunity, healthy-volunteer-PD, case-series |
| 12 | `phase` | enum or null | paper / registry | 1, 1/2, 2, 2/3, 3, 4, translational, N/A |
| 13 | `nct_id` | string or null | paper / registry | null if not registered |
| 14 | `tissue` | enum | paper | PBMC, tumor, TDLN, bone-marrow, ascites, pleural-effusion, CSF, skin, other |
| 15 | `tissue_detail` | string or null | paper | e.g., "on-treatment cycle-1-day-15 biopsy" |
| 16 | `treg_definition` | string | paper | gating strategy, e.g., "CD4+CD25hiFOXP3+CD127lo" |
| 17 | `gating_quality` | enum | paper | FOXP3-confirmed, surface-only, functional-assay, mixed, unclear |
| 18 | `readout_type` | enum | paper | absolute-count, frequency-of-CD4, frequency-of-lymphocytes, frequency-of-CD3, ratio-to-Teff, ratio-to-CD8, suppressive-function, other |
| 19 | `timepoint_cluster` | enum | paper | baseline, early-on-treatment (≤ day 28), mid (day 29–90), late (> day 90), post-progression, off-treatment-recovery |
| 20 | `timepoint_detail` | string or null | paper | exact timing text, e.g., "C2D1" |
| 21 | `baseline_value` | string or null | paper | report as given |
| 22 | `baseline_stat_type` | enum or null | paper | mean-sd, median-iqr, median-range, range, point-estimate, geometric-mean, not-reported |
| 23 | `post_value` | string or null | paper | post-treatment value |
| 24 | `post_stat_type` | enum or null | paper | same enum as baseline_stat_type |
| 25 | `change_direction` | enum | paper | decrease, increase, no-change, mixed, not-reported |
| 26 | `change_magnitude` | string or null | paper | e.g., "~70% reduction", "2.1× increase", "suppression fell from 78% to 32%" |
| 27 | `change_significance` | string or null | paper | e.g., "p=0.003", "n.s.", "not tested" |
| 28 | `change_mechanism` | enum | paper | absolute-reduction, ratio-shift, expansion-with-ratio-shift, functional-impairment-only, null-result |
| 29 | `pct_change` | float or null | computed | Signed relative percent change in Treg measure (negative = reduction). Populated where `change_magnitude` contains a clean single-number headline or an unambiguous fold-change. For functional-impairment rows, use the delta in suppression percentage (e.g., 78%→32% = −46 pp ~ −59% relative if expressed relative; prefer −46 reported as `pct_change: -46` with `pct_change_stat: point` and text-fragment citation). Null when qualitative-only, proportional-only (e.g. 4/4 reduced), or authors explicitly state no significant change. |
| 30 | `pct_change_stat` | enum or null | computed | point, mean, median, range-midpoint, fold-derived |
| 31 | `pct_change_source` | string or null | computed | Short string citing the text fragment that sourced `pct_change`, for audit |
| 32 | `durability_days` | integer or null | paper | days to recovery or last measured on-treatment timepoint |
| 33 | `durability_described` | string or null | paper | short phrase |
| 34 | `depletion_success` | enum | paper | succeeded, partial, failed, not-assessed. For `functional-impairment-only` rows, `succeeded` requires suppressive-function assay evidence. |
| 35 | `clinical_correlate` | string or null | paper | e.g., "higher ORR in deep depleters (p=0.04)" |
| 36 | `intent_to_deplete` | enum | paper | mechanism-targeted, pre-specified-endpoint, exploratory-but-prespecified, incidental-but-measured |
| 37 | `notes` | string or null | paper | free text; caveats, null results, disagreements |
| 38 | `pmid` | string or null | PubMed | null only if source is not indexed |
| 39 | `pmcid` | string or null | PMC | null if no PMC record |
| 40 | `doi` | string or null | paper | null if unknown |
| 41 | `first_author` | string | paper | last name + initial |
| 42 | `year` | integer | paper | publication year |
| 43 | `journal` | string | paper | short title |
| 44 | `title` | string | paper | full title |
| 45 | `source_type` | enum | generated | pmc_full_text, europepmc_full_text, pubmed_abstract, ctgov_registry, other |
| 46 | `source_url` | string | generated | canonical URL used |
| 47 | `fetch_timestamp_utc` | ISO-8601 string | generated | when the row was extracted |

## Missing-value rules

- Numeric fields not reported: `null` + `notes` mention.
- Stat type must be specified whenever a value is given.
- Never guess. Bar-chart-only with no numeric: `null` + "graph-only, no numeric value reported".
- If only a percent change is given (no absolute values), populate `change_magnitude` and leave `baseline_value` / `post_value` null.

## Populating the typed pct_change fields at extraction time

Prefer to populate these at extraction rather than relying on the post-hoc normalizer:

- If `change_magnitude` contains an unambiguous signed percent (e.g., "~61% reduction", "35% decrease at day 28"), set `pct_change` to the signed value and `pct_change_stat: point`.
- If a range is given (e.g., "26–76% reduction"), use the midpoint and set `pct_change_stat: range-midpoint`.
- If a fold-change is given (e.g., "3-fold reduction"), convert: 3× reduction → pct_change = `-66.7`, `pct_change_stat: fold-derived`. 2.1× increase → `+110.0`.
- For functional-impairment rows, if the paper reports "suppression dropped from A% to B%", use `pct_change: (B − A)` (the percentage-point delta) with `pct_change_stat: point` and a text-fragment citation. This is an acceptable schema-v2 convention for functional readouts — the stat column disambiguates.
- If authors report "no significant change" with a null result, leave `pct_change` null and use `change_mechanism: null-result`.
- Always populate `pct_change_source` with the verbatim text fragment when any of the above applies.

## Side-list (not main table)

Systematic reviews and meta-analyses → `reviews.jsonl` with reduced schema: `pmid`, `pmcid`, `doi`, `first_author`, `year`, `journal`, `title`, `review_type`, `scope_summary`, `notes`, `fetch_timestamp_utc`. Rendered as trailing section on the shieldbreak page.

## Row-grain examples

- Mogamulizumab Phase 1 in CTCL reporting PBMC + skin + tumor at baseline + C1D15 + C3D1 for a single dose: 1 × 3 × 3 = 9 rows.
- Ipilimumab 3 mg/kg vs 10 mg/kg in melanoma, PBMC and tumor at baseline + post-treatment: 2 cohorts × 2 tissues × 2 timepoint-clusters = 8 rows (papers often collapse timepoints — one row per reported cluster).
- Low-dose cyclophosphamide + vaccine, PBMC only, single timepoint: 1 row.
- Anti-TIGIT monotherapy with PBMC count data (absolute + frequency) AND in vitro suppression assay on sorted post-treatment Tregs: yields 2 rows per timepoint — one `readout_type: absolute-count` + `change_mechanism: absolute-reduction` (or null-result), and one `readout_type: suppressive-function` + `change_mechanism: functional-impairment-only`. Both carry same PMID/tissue but different readout_type values, disambiguated in `row_id` via a suffix.
