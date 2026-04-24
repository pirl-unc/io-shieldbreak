# Tumor-associated Macrophage (TAM) modulation — search & screening spec

**Shieldbreak slug:** `tam-depletion` (path frozen for URL stability; display title is "Tumor-associated Macrophage Depletion, Inhibition, or Repolarization")
**Schema version:** 1 (initial run 2026-04-23)

**Research question:** Which clinical interventions deplete, inhibit, or repolarize tumor-associated macrophages (TAMs) in humans, and how durable / context-dependent is that effect?

## Scope framing

Three orthogonal modulation modes are all in scope:

1. **Depletion** — reduce TAM absolute count or frequency (e.g., CSF1R antagonism → tissue macrophage ablation).
2. **Inhibition** — block a TAM suppressive function without necessarily reducing count (e.g., PI3Kγ inhibition, "don't eat me" checkpoint blockade).
3. **Repolarization** — shift M2-like → M1-like phenotype (CD163/CD206 down, MHC-II / CD80 / CD86 up) without count change. Can co-occur with count shifts.

The schema uses two orthogonal fields (deviation D5 from the seed):
- `intervention_class` — **intent** of the agent (mechanistic class).
- `change_mechanism` — **observed** effect in the paper being extracted.

## Approved deviations from the treg-depletion precedent (D1–D9)

- **D1.** Blood monocytes (PBMC CD14+ / CD14+CD16+) are in-scope **only** when the paper explicitly pre-specifies them as a TAM surrogate. Incidental monocyte counts in trials that did not pre-specify them → exclude.
- **D2.** Checkpoint-inhibitor (CPI) monotherapy is **explicitly excluded** even if TAM counts are reported. CPI is fine as a combo partner (e.g., CSF1Ri + anti-PD1).
- **D3.** Healthy-volunteer PD is **excluded entirely** (unlike treg-depletion, which allowed it).
- **D4.** `IPI-549` / eganelisib gets its own `intervention_class: pi3kg-inhibitor` — not bundled with depletion.
- **D5.** The three modes (deplete / inhibit / repolarize) are captured via orthogonal `intervention_class` (intent) and `change_mechanism` (observed). See enum list.
- **D6.** `scRNA-cluster-shift` is a first-class `readout_type` value (single-cell transcriptomic macrophage-cluster shift is distinct from flow frequency).
- **D7.** `mIF-multiplex` and `CyTOF` are first-class `gating_quality` values, not lumped under "mixed".
- **D8.** Carry `durability_days` over from treg-depletion.
- **D9.** Per-run cap is **30** kept items (deviation from the 50 on treg-depletion).

## Topic

- **Target biology:** tumor-associated macrophages (CD68+, CD163+, CD206+ ± MHC-II, ± CD86); myeloid-derived suppressive populations adjacent to the TAM compartment when the paper ties them to TAM phenotype (monocytic-MDSCs when explicitly framed as TAM precursors).
- **Population:** cancer patients (any indication, any age, any geography). **Healthy volunteers excluded.**
- **Interventions of interest (12 families):**
  1. **CSF1 / CSF1R inhibitors** — pexidartinib, cabiralizumab, axatilimab, AMG 820, emactuzumab, vimseltinib, edicotinib, ARRY-382, BLZ945, lacnotuzumab, IMC-CS4 / LY3022855, PLX7486, "anti-CSF1R", "CSF1R inhibitor"
  2. **PI3Kγ inhibitors** — eganelisib / IPI-549
  3. **CCR2 / CCR5 inhibitors** — PF-04136309, BMS-813160, cenicriviroc, maraviroc (TAM-context only; HIV trials OUT), plozalizumab
  4. **Bisphosphonates** — zoledronic acid, clodronate liposomes (TAM-endpoint filtered)
  5. **Trabectedin / lurbinectedin** — TAM-endpoint filtered
  6. **Anti-CD47 / anti-SIRPα** — magrolimab / Hu5F9-G4, letaplimab / IBI188, lemzoparlimab / TJC4, AO-176, SRF231, TTI-622, TTI-621, evorpacept / ALX148, CC-95251, BI 765063, FSI-189
  7. **Anti-CD24** — IMM47, SWA11 derivatives
  8. **CD40 agonists** — selicrelumab / RO7009789 / CP-870,893, sotigalimab / APX005M, mitazalimab, CDX-1140, 2141-V11, SEA-CD40, ABBV-428
  9. **TLR agonists (TAM-reporting)** — poly-ICLC / Hiltonol, motolimod / VTX-2337, SD-101, tilsotolimod / IMO-2125, lefitolimod / MGN1703, BO-112, vidutolimod / CMP-001, G100 / GLA-SE, imiquimod / resiquimod
  10. **STING agonists** — ADU-S100 / MIW815, MK-1454, SB11285, BMS-986301, E7766, TAK-676, dazostinag
  11. **CLEVER-1 / Stabilin-1 / MARCO** — bexmarilimab / FP-1305
  12. **LILRB / TREM2** — IO-108, JTX-8064, MK-0482, BND-22, PY314, JTX-5
- **Explicit class-level exclusions:**
  - **Checkpoint-inhibitor monotherapy** (D2).
  - **Adoptive-cell-therapy lymphodepletion** where macrophage changes are incidental.
  - **Healthy-volunteer PD studies** (D3).

## Tissue compartments (in scope)

- Tumor (intratumoral biopsy, resection, FNA) — primary target compartment
- PBMC — **only** when paper pre-specifies monocytes/subsets as TAM surrogate (D1)
- TDLN — when reported
- Bone marrow, ascites, pleural effusion — when reported (ovarian, mesothelioma, MM)
- Skin — for topical TLR agonists (imiquimod, resiquimod) reporting local macrophage PD
- **One row per (study × tissue × timepoint-cluster × dose-cohort).** A tumor + TDLN + ascites paper yields up to three rows per timepoint cluster.

## Filters

- **Date range:** 2010-01-01 → 2026-04-23
- **Language:** English only
- **Phases:** Phase 1, 1/2, 2, 2/3, 3, window-of-opportunity, translational substudies, case series (flagged in `design_type`)
- **Geography:** any
- **Study type allowed:** primary-research clinical reports with TAM PD data on ≥3 treated patients with TAM measurement.
- **Study type excluded from main table:** narrative reviews, editorials, commentaries, letters without primary data, preclinical-only reports, in vitro-only studies.
- **Side-list:** systematic reviews and meta-analyses → `reviews.jsonl`.

## Screening — inclusion criteria

Include if ALL hold:

1. Human subjects, N ≥ 3 treated patients with at least one TAM PD measurement.
2. Intervention is on the in-scope 12-family list OR pre-specifies TAM modulation (depletion / inhibition / repolarization) as an endpoint.
3. Reports at least one TAM PD readout in at least one in-scope tissue compartment — count, frequency, ratio (M1:M2 or similar), polarization-marker shift, phagocytosis function, or scRNA macrophage-cluster shift.
4. Primary research (not review / editorial / commentary / letter without primary data).
5. English, 2010–present.
6. **Intent-to-modulate gate:** study either (a) uses an intervention with a TAM-targeting mechanism, or (b) explicitly measures TAM as a pre-specified PD endpoint. Incidental TAM counts without intent are EXCLUDED.
7. **Null / failed attempts are INCLUDED** — failing to modulate is a valuable result.

## Screening — exclusion criteria

Exclude if ANY hold:

- No TAM measurement, or measurement in < 3 treated subjects.
- Checkpoint-inhibitor monotherapy without a TAM-targeting co-intervention (D2).
- Preclinical / animal / in vitro only.
- Review, editorial, commentary, letter without primary data. Systematic reviews and meta-analyses go to the side-list.
- Non-English.
- Healthy-volunteer PD (D3).
- Blood monocyte counts only, without pre-specification as TAM surrogate (D1).
- PK-only without PD readout.
- Study did not aim to modulate TAMs AND did not pre-specify TAM as a measured endpoint.

## Outcome definition — "modulation"

- **Absolute reduction** (classical depletion, e.g., CSF1Ri tumor CD68+ count down): `change_mechanism = absolute-reduction`.
- **Ratio / fraction shift** (e.g., M1:M2 favorable shift with stable total macrophage count): `change_mechanism = ratio-shift`.
- **Repolarization** (CD163/CD206 down, MHC-II / CD80 / CD86 up; multi-marker): `change_mechanism = repolarization`. Requires **multi-marker** evidence — single-marker IHC is not sufficient for `depletion_success: succeeded` on a repolarization row.
- **Expansion-with-repolarization** (rare; macrophages expand absolutely but skew M1): `change_mechanism = expansion-with-repolarization`.
- **Functional-impairment-only** (phagocytosis assay pre/post, or suppression assay): `change_mechanism = functional-impairment-only`. Requires assay-level evidence.
- **Null** (intervention aimed to modulate, did not): `change_mechanism = null-result`.
- Accept paired pre/post and treated-vs-untreated designs.
- Report dose-cohort-level rows when multiple cohorts reported.

## Sources (priority order, NCBI-first)

1. **PubMed** (esearch / esummary / efetch) — primary discovery
2. **PMC** (efetch db=pmc) — full text when PMCID available
3. **ClinicalTrials.gov** (v2 API) — cross-reference NCT IDs, design, results postings
4. **Europe PMC** — fallback for full text when PMC has no record
5. **WebSearch** — only for grey-literature / conference-abstract leads (not proactive)

Include `tool=trialist_screener&email=benjamin.g.vincent@gmail.com` on E-utilities calls. Stay under 3 req/sec.

## Per-run cap

- **Cap:** 30 kept items per run (D9).
- Row count may exceed 30 due to row-grain (multi-tissue / multi-timepoint / multi-cohort papers).

## Query strategy — 12 family queries

Each family is ANDed with a macrophage-relevance clause and filtered by `2010:3000[dp] AND english[la]`.

**Macrophage relevance clause (applied to all families):**

```
("tumor-associated macrophage"[tiab] OR "tumour-associated macrophage"[tiab] OR "TAM"[tiab]
 OR "macrophage"[tiab] OR "CD163"[tiab] OR "CD68"[tiab] OR "CD206"[tiab] OR "myeloid"[tiab])
```

### Family 1 — CSF1 / CSF1R

```
(pexidartinib[tiab] OR cabiralizumab[tiab] OR axatilimab[tiab] OR "AMG 820"[tiab]
 OR emactuzumab[tiab] OR vimseltinib[tiab] OR edicotinib[tiab] OR "ARRY-382"[tiab]
 OR BLZ945[tiab] OR lacnotuzumab[tiab] OR "IMC-CS4"[tiab] OR "LY3022855"[tiab]
 OR "PLX7486"[tiab] OR "anti-CSF1R"[tiab] OR "CSF1R inhibitor"[tiab] OR "CSF-1R"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 2 — PI3Kγ (eganelisib)

```
(eganelisib[tiab] OR "IPI-549"[tiab] OR "PI3K gamma"[tiab] OR "PI3Kgamma"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 3 — CCR2 / CCR5

```
("PF-04136309"[tiab] OR "BMS-813160"[tiab] OR cenicriviroc[tiab] OR maraviroc[tiab]
 OR plozalizumab[tiab] OR "anti-CCR2"[tiab] OR "CCR2 inhibitor"[tiab] OR "CCR5 inhibitor"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 4 — Bisphosphonates (TAM-endpoint)

```
("zoledronic acid"[tiab] OR zoledronate[tiab] OR "clodronate liposomes"[tiab] OR bisphosphonate[tiab])
AND ("tumor-associated macrophage"[tiab] OR "tumour-associated macrophage"[tiab] OR "TAM"[tiab]
     OR CD163[tiab] OR CD68[tiab] OR CD206[tiab])
AND (2010:3000[dp]) AND english[la]
```

### Family 5 — Trabectedin / lurbinectedin (TAM-endpoint)

```
(trabectedin[tiab] OR lurbinectedin[tiab] OR "PM01183"[tiab] OR "ET-743"[tiab])
AND ("tumor-associated macrophage"[tiab] OR "tumour-associated macrophage"[tiab] OR "TAM"[tiab]
     OR CD163[tiab] OR CD68[tiab] OR macrophage[tiab])
AND (2010:3000[dp]) AND english[la]
```

### Family 6 — Anti-CD47 / anti-SIRPα

```
(magrolimab[tiab] OR "Hu5F9-G4"[tiab] OR letaplimab[tiab] OR "IBI188"[tiab] OR lemzoparlimab[tiab]
 OR "TJC4"[tiab] OR "AO-176"[tiab] OR "SRF231"[tiab] OR "TTI-622"[tiab] OR "TTI-621"[tiab]
 OR evorpacept[tiab] OR "ALX148"[tiab] OR "CC-95251"[tiab] OR "BI 765063"[tiab] OR "FSI-189"[tiab]
 OR "anti-CD47"[tiab] OR "anti-SIRP"[tiab] OR "CD47-SIRPalpha"[tiab] OR "CD47 blockade"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 7 — Anti-CD24

```
("anti-CD24"[tiab] OR "CD24 blockade"[tiab] OR "IMM47"[tiab] OR "SWA11"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 8 — CD40 agonists

```
(selicrelumab[tiab] OR "RO7009789"[tiab] OR "CP-870,893"[tiab] OR "CP-870893"[tiab]
 OR sotigalimab[tiab] OR "APX005M"[tiab] OR mitazalimab[tiab] OR "CDX-1140"[tiab]
 OR "2141-V11"[tiab] OR "SEA-CD40"[tiab] OR "ABBV-428"[tiab] OR "CD40 agonist"[tiab]
 OR "anti-CD40"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 9 — TLR agonists (TAM-reporting)

```
("poly-ICLC"[tiab] OR Hiltonol[tiab] OR motolimod[tiab] OR "VTX-2337"[tiab]
 OR "SD-101"[tiab] OR tilsotolimod[tiab] OR "IMO-2125"[tiab] OR lefitolimod[tiab]
 OR "MGN1703"[tiab] OR "BO-112"[tiab] OR vidutolimod[tiab] OR "CMP-001"[tiab]
 OR "G100"[tiab] OR "GLA-SE"[tiab] OR imiquimod[tiab] OR resiquimod[tiab]
 OR "TLR7 agonist"[tiab] OR "TLR8 agonist"[tiab] OR "TLR9 agonist"[tiab])
AND ("tumor-associated macrophage"[tiab] OR "TAM"[tiab] OR CD163[tiab] OR CD68[tiab]
     OR CD206[tiab] OR "macrophage polarization"[tiab] OR "M1 macrophage"[tiab]
     OR "M2 macrophage"[tiab])
AND (2010:3000[dp]) AND english[la]
```

### Family 10 — STING agonists

```
("ADU-S100"[tiab] OR "MIW815"[tiab] OR "MK-1454"[tiab] OR "SB11285"[tiab]
 OR "BMS-986301"[tiab] OR "E7766"[tiab] OR "TAK-676"[tiab] OR dazostinag[tiab]
 OR "STING agonist"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 11 — CLEVER-1 / Stabilin-1 / MARCO

```
(bexmarilimab[tiab] OR "FP-1305"[tiab] OR "CLEVER-1"[tiab] OR "Stabilin-1"[tiab]
 OR "STAB1"[tiab] OR MARCO[tiab] OR "anti-MARCO"[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

### Family 12 — LILRB / TREM2

```
("IO-108"[tiab] OR "JTX-8064"[tiab] OR "MK-0482"[tiab] OR "BND-22"[tiab] OR "PY314"[tiab]
 OR "JTX-5"[tiab] OR LILRB2[tiab] OR LILRB4[tiab] OR "anti-LILRB2"[tiab] OR "anti-TREM2"[tiab]
 OR TREM2[tiab])
AND <macrophage clause>
AND (2010:3000[dp]) AND english[la]
```

Merge all family results; dedupe by NCT > DOI > PMID > normalized title; cap kept items at 30.

## Known watch-outs

- **CSF1R family** — pexidartinib in tenosynovial giant-cell tumor (TGCT) is a non-cancer TAM indication, but the target biology is macrophage CSF1R. Include if TAM PD reported; flag indication.
- **Maraviroc / cenicriviroc** — primarily HIV drugs; only include oncology trials reporting TAM PD.
- **Bisphosphonates** — long history in breast-cancer bone-met prevention; exclude those without TAM PD endpoint.
- **Anti-CD47 magrolimab** — program halted / restructured multiple times (sepsis/anemia signals in AML); retain published PD data regardless of program status.
- **Imiquimod / resiquimod (topical)** — many skin-cancer papers report local macrophage infiltration; include when pre-specified, flag as `tissue: skin`.
- **scRNA papers** — macrophage cluster shifts often reported only in one treatment arm of a platform; capture arm-specific rows per row-grain rule.
- **CD40 agonist "abscopal" framing** — some report no local change but systemic immune activation; for TAM scope, require an intratumoral readout (not just peripheral cytokine).
- **CLEVER-1 / bexmarilimab** — MATINS trial publishes iteratively; retain multiple papers per trial if reporting different PD endpoints.
- **Full text gaps** — many TAM PD papers are in Clin Cancer Res, J Immunother Cancer (open), Lancet Oncol, Nat Cancer — mix of PMC-open and paywalled; expect ~60-70% full-text accessibility.
