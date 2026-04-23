# Treg depletion — search & screening spec

**Shieldbreak slug:** `treg-depletion`
**Research question:** Which clinical interventions reduce regulatory T cells (Tregs) — in absolute number, frequency, or functional dominance — in humans, and how durable / context-dependent is that effect?

## Topic

- **Target biology:** regulatory T cells (CD4+FOXP3+, CD4+CD25hiFOXP3+, CD4+CD25hiCD127lo, CCR4+, CCR8+, TNFR2+, Helios+, etc.). Includes effector/tissue-Treg subsets.
- **Population:** any human subjects — cancer patients, autoimmune/transplant patients, healthy volunteers in PD studies, infectious disease cohorts. No age/sex/geography restriction.
- **Interventions of interest (core list, confirmed):**
  - **Anti-CCR4** — mogamulizumab
  - **Anti-CD25** — daclizumab, basiliximab, camidanlumab tesirine (ADCT-301), RG6292 / vopikitug, other IL-2Rα-targeted agents
  - **Fc-enhanced anti-CTLA-4** — botensilimab (AGEN1181), quavonlimab, ONC-392 / gotistobart (pH-sensitive), BMS-986218, others designed for FcγR-mediated Treg depletion in TME
  - **Standard anti-CTLA-4** — ipilimumab, tremelimumab (ADCC-mediated intratumoral Treg depletion reported)
  - **Low-dose cyclophosphamide** — metronomic or single pre-treatment dose as Treg-depleting strategy
  - **Denileukin diftitox** (ONTAK / E7777 / I/ONTAK)
  - **IL-2 variants / "non-α" IL-2** — nemvaleukin alfa (ALKS 4230), bempegaldesleukin (NKTR-214) — bempegaldesleukin INCLUDED only via Treg-ratio / fraction-shift pathway (it expands Tregs in absolute terms; captured with `change_mechanism = ratio_shift`)
  - **Adenosine-axis** — anti-CD39, anti-CD73, A2AR antagonists — only when Treg is a pre-specified or reported PD endpoint
  - **Anti-CCR8** (ADDED) — e.g., BMS-986340, LY3475070, S-531011, FPA157, GS-1811
  - **Anti-GITR** (ADDED) — e.g., TRX518, MK-4166, MK-1248, BMS-986156, GWN323
  - **Anti-OX40** (ADDED) — when Treg PD is measured
  - **EZH2 inhibitors** (ADDED) — e.g., tazemetostat — when Treg PD is measured
  - **PI3Kδ inhibitors** (ADDED) — e.g., idelalisib, parsaclisib — when Treg PD is measured
  - **Chemo beyond cyclophosphamide** — INCLUDED only when Treg reduction is a pre-specified endpoint
  - **JAK inhibitors, HDAC inhibitors, hypomethylating agents (HMAs), radiation therapy** — INCLUDED only when Treg is an explicitly measured endpoint (not incidental)
- **Explicit exclusions (intervention class):**
  - **Fludarabine** (and fludarabine-containing lymphodepletion regimens in CAR-T/ACT) — OUT; sweeps in every adoptive-cell-therapy paper and Treg reduction is an expected pan-lymphocyte effect.
  - **Bempegaldesleukin as a Treg-reducer** — OUT (but included via ratio-shift path as noted above).
- **Comparators:** any (single-arm acceptable; paired pre/post acceptable; treated-vs-untreated acceptable — both designs flagged in the `design_type` column).
- **Outcomes of interest:** any reported Treg pharmacodynamic (PD) readout — absolute count, frequency (% of CD4+, % of lymphocytes), Treg:Teff ratio, functional suppressive capacity, tumor/blood/tissue compartment levels. Durability captured separately.

## Tissue compartments (in scope)

- Peripheral blood (PBMC)
- Tumor (intratumoral, including biopsy/resection/FNA)
- Tumor-draining lymph node (TDLN)
- Bone marrow, ascites, pleural effusion, CSF — when reported
- Skin (e.g., mogamulizumab PD studies in CTCL; autoimmune skin biopsies)
- **One row per (study × tissue × timepoint-cluster)** — a single paper with PBMC + tumor + TDLN readouts yields up to three rows.

## Filters

- **Date range:** 2000-01-01 → present (2026-04-23)
- **Language:** English only
- **Phases:** Phase 1, Phase 1/2, Phase 2, Phase 3, window-of-opportunity, translational sub-studies, healthy-volunteer PD, case series (flagged in `design_type`).
- **Geography:** any.
- **Study type allowed:** primary-research clinical reports with Treg PD data on ≥3 treated humans with Treg measurement.
- **Study type excluded from main table:** narrative reviews, editorials, commentaries, letters without primary data, preclinical-only reports, in vitro-only studies.
- **Side-list:** systematic reviews and meta-analyses — captured in a separate side-list (not main table) for PI follow-up.

## Screening — inclusion criteria

Include a report if ALL of the following hold:

1. Human subjects, N ≥ 3 treated patients (or volunteers) with at least one Treg measurement.
2. The intervention is on the in-scope list (core + additions) OR targets Treg reduction as a pre-specified or reported endpoint.
3. Reports at least one Treg PD readout in at least one in-scope tissue compartment.
4. Primary research (not review/editorial/commentary).
5. English, 2000–present.
6. **Intent-to-deplete gate:** the study either (a) uses an intervention whose mechanism is Treg-targeting, or (b) explicitly measures Treg as a pre-specified PD endpoint. Studies that report Tregs only incidentally without an intent-to-modulate-Treg rationale are EXCLUDED.
7. **Failed/null attempts are INCLUDED** — if the study tried to deplete Tregs and did not succeed, that result is valuable and belongs in the table.

## Screening — exclusion criteria

Exclude if ANY of the following hold:

- No Treg measurement, or Treg measurement in < 3 treated subjects.
- Intervention is fludarabine-containing lymphodepletion without Treg-specific intent.
- Preclinical/animal/in vitro only.
- Review, editorial, commentary, letter (no primary data). Systematic reviews and meta-analyses go to the side-list, not the main table.
- Non-English.
- Study did not aim to modulate Tregs AND did not pre-specify Treg as a measured endpoint.

## Outcome definition — "reduction"

- **Any reduction of any duration** counts as a positive signal. Durability is captured separately (`durability_days`, `durability_described`).
- **Ratio / fraction shifts count** (e.g., CD8:Treg ratio increase with stable absolute Treg counts) — captured via `change_mechanism = ratio_shift`.
- **Expansion-as-reduction** is allowed: if Tregs expand in absolute terms but the study frames the readout as a functional/ratio reduction (e.g., bempegaldesleukin, some IL-2 agents), include it with `change_mechanism = expansion_with_ratio_shift`.
- Accept both **paired pre/post** and **treated-vs-untreated** designs; flag design in `design_type`.
- Report dose-cohort-level rows when multiple cohorts are reported.

## Sources (priority order, NCBI-first)

1. **PubMed** (esearch / esummary / efetch) — primary discovery
2. **PMC** (efetch db=pmc) — full-text extraction when PMCID available
3. **ClinicalTrials.gov** (v2 API) — cross-reference NCT IDs, design, results postings
4. **Europe PMC** — fallback full text
5. **WebSearch** — only if a grey-literature lead comes up (conference abstracts, press releases). Not used proactively.

Include `tool=trialist_screener&email=benjamin.g.vincent@gmail.com` on E-utilities calls. Stay under 3 req/sec.

## Per-run cap

- **Cap:** 50 kept items per run (user can raise on request).
- **Screening ratio target:** aim to screen ≥5× the cap so the kept set represents the best of the pool.

## Query strategy (PubMed; adapt per source)

Primary composite query (OR'd across intervention tokens, AND'd with Treg PD tokens AND human/clinical filters):

```
(
  ("mogamulizumab"[tiab] OR "anti-CCR4"[tiab] OR "CCR4 antibody"[tiab])
  OR ("daclizumab"[tiab] OR "basiliximab"[tiab] OR "camidanlumab"[tiab] OR "ADCT-301"[tiab] OR "RG6292"[tiab] OR "vopikitug"[tiab] OR "anti-CD25"[tiab])
  OR ("botensilimab"[tiab] OR "AGEN1181"[tiab] OR "quavonlimab"[tiab] OR "ONC-392"[tiab] OR "gotistobart"[tiab] OR "BMS-986218"[tiab] OR "Fc-enhanced CTLA-4"[tiab] OR "Fc-engineered CTLA-4"[tiab])
  OR ("ipilimumab"[tiab] OR "tremelimumab"[tiab]) AND ("regulatory T"[tiab] OR "Treg"[tiab] OR "FOXP3"[tiab])
  OR ("cyclophosphamide"[tiab] AND ("low-dose"[tiab] OR "metronomic"[tiab]) AND ("Treg"[tiab] OR "regulatory T"[tiab]))
  OR ("denileukin diftitox"[tiab] OR "ONTAK"[tiab] OR "E7777"[tiab])
  OR ("nemvaleukin"[tiab] OR "ALKS 4230"[tiab])
  OR ("bempegaldesleukin"[tiab] OR "NKTR-214"[tiab])
  OR ("anti-CD39"[tiab] OR "anti-CD73"[tiab] OR "A2AR"[tiab] OR "adenosine receptor"[tiab]) AND ("Treg"[tiab] OR "regulatory T"[tiab])
  OR ("anti-CCR8"[tiab] OR "CCR8 antibody"[tiab] OR "BMS-986340"[tiab] OR "LY3475070"[tiab] OR "S-531011"[tiab] OR "FPA157"[tiab] OR "GS-1811"[tiab])
  OR ("anti-GITR"[tiab] OR "TRX518"[tiab] OR "MK-4166"[tiab] OR "MK-1248"[tiab] OR "BMS-986156"[tiab] OR "GWN323"[tiab])
  OR ("anti-OX40"[tiab]) AND ("Treg"[tiab] OR "regulatory T"[tiab])
  OR ("tazemetostat"[tiab] OR "EZH2 inhibitor"[tiab]) AND ("Treg"[tiab] OR "regulatory T"[tiab])
  OR ("idelalisib"[tiab] OR "parsaclisib"[tiab] OR "PI3K delta"[tiab]) AND ("Treg"[tiab] OR "regulatory T"[tiab])
)
AND
("regulatory T"[tiab] OR "Treg"[tiab] OR "FOXP3"[tiab] OR "CD25"[tiab] OR "CD4+CD25"[tiab])
AND
("clinical trial"[pt] OR "humans"[mh] OR "pharmacodynamics"[tiab] OR "patients"[tiab] OR "phase"[tiab])
AND
("2000"[dp]:"3000"[dp])
AND
english[la]
```

In practice, run per-intervention-family queries (narrower, cleaner) and merge.

## Known watch-outs

- CAR-T papers will flood results via fludarabine lymphodepletion — filter aggressively.
- "Regulatory T cell" is used loosely in some papers (no FOXP3 confirmation); flag gating quality in `gating_quality` field.
- Older ipilimumab/tremelimumab intratumoral Treg depletion papers remain debated; include both supportive and null reports.
- Mogamulizumab in CTCL has rich skin + blood PD data — expect multiple rows per paper.
