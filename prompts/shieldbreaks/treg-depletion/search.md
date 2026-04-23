# Treg depletion and/or inhibition — search & screening spec

**Shieldbreak slug:** `treg-depletion` (path frozen for URL stability; display title is "Treg Depletion and/or Inhibition")
**Schema version:** 2 (scope expansion 2026-04-23)

**Research question:** Which clinical interventions reduce regulatory T cells (Tregs) — in absolute number, frequency, functional dominance, or suppressive capacity — in humans, and how durable / context-dependent is that effect?

## Scope expansion (2026-04-23)

Previously: "interventions that REDUCE the number or frequency of Tregs" (depletion-only framing).

Now: **depletion OR functional inhibition OR destabilization of Tregs.** Specifically, we want to capture interventions that:

1. Reduce Treg absolute count (classical depletion).
2. Reduce Treg frequency (% of CD4+, % of lymphocytes), even without absolute count change.
3. Shift Treg : Teff or Treg : CD8 ratios in favor of effectors without reducing Tregs.
4. **Impair Treg suppressive function** (suppression-assay readout) without changing counts — this is the new signal.
5. **Destabilize the Treg phenotype** (FoxP3 loss, Treg → effector conversion, Helios/IKZF2 loss, epigenetic decay of FoxP3 locus).

For any row where 4 or 5 apply without 1/2/3, use `change_mechanism: functional-impairment-only` and `readout_type: suppressive-function`. Claiming `depletion_success: succeeded` under this mechanism requires **assay-level evidence of impaired suppressive capacity** (in vitro suppression assay pre vs post, or an unambiguous FoxP3-stability / methylation readout), not just frequency changes.

## Topic

- **Target biology:** regulatory T cells (CD4+FOXP3+, CD4+CD25hiFOXP3+, CD4+CD25hiCD127lo, CCR4+, CCR8+, TNFR2+, Helios/IKZF2+, etc.). Includes effector/tissue-Treg subsets and FoxP3-stability readouts.
- **Population:** any human subjects — cancer patients, autoimmune/transplant patients, healthy volunteers in PD studies, infectious disease cohorts. No age/sex/geography restriction.
- **Interventions of interest (expanded list):**
  - **Anti-CCR4** — mogamulizumab
  - **Anti-CD25** — daclizumab, basiliximab, camidanlumab tesirine (ADCT-301), RG6292 / vopikitug, other IL-2Rα-targeted agents
  - **Fc-enhanced anti-CTLA-4** — botensilimab (AGEN1181), quavonlimab, ONC-392 / gotistobart (pH-sensitive), BMS-986218, others designed for FcγR-mediated Treg depletion in TME
  - **Standard anti-CTLA-4** — ipilimumab, tremelimumab (ADCC-mediated intratumoral Treg depletion reported)
  - **Low-dose cyclophosphamide** — metronomic or single pre-treatment dose as Treg-depleting strategy
  - **Denileukin diftitox** (ONTAK / E7777 / I/ONTAK)
  - **IL-2 variants / "non-α" IL-2** — nemvaleukin alfa (ALKS 4230), bempegaldesleukin (NKTR-214) — bempeg INCLUDED via ratio / fraction-shift pathway (it expands Tregs; captured with `change_mechanism = ratio_shift`)
  - **Adenosine-axis** — anti-CD39, anti-CD73, A2AR antagonists — when Treg is a pre-specified or reported PD endpoint
  - **Anti-CCR8** — BMS-986340, LY3475070, S-531011, FPA157, GS-1811
  - **Anti-GITR** — TRX518, MK-4166, MK-1248, BMS-986156, GWN323
  - **Anti-OX40** — PF-04518600, MEDI6469, MEDI0562, MOXR0916, BMS-986178 — when Treg PD measured (esp. functional-suppression assay)
  - **Anti-TNFR2** (NEW) — BAT2506, HFB200301 / HFB-2, antagonists intended to destabilize Tregs and impair suppression; first-in-human PD readouts
  - **Anti-TIGIT** (NEW — *inhibition-pathway inclusion*) — tiragolumab, vibostolimab, domvanalimab, ociperlimab, EOS-448 — INCLUDED when Treg function / destabilization / frequency is measured (not merely incidental lymphocyte profiling)
  - **EP4 antagonists** (NEW) — grapiprant (and combos), ONO-4578, palupiprant — when human Treg PD readouts reported
  - **EZH2 inhibitors** — tazemetostat, valemetostat — Treg function / FoxP3-stability readouts
  - **PI3Kδ inhibitors** — idelalisib, copanlisib, umbralisib, duvelisib, parsaclisib — Treg function (not just count) readouts
  - **DNMT inhibitors / HMAs** (NEW emphasis) — azacitidine, decitabine, guadecitabine — FoxP3-stability / Treg-destabilization readouts in MDS/AML/solid tumor
  - **HDAC inhibitors** (NEW emphasis) — romidepsin, vorinostat, panobinostat, entinostat, mocetinostat — Treg function / FoxP3 acetylation / suppressive-capacity readouts
  - **Helios / IKZF2 / cereblon-based degraders** (NEW) — mezigdomide (CC-92480), iberdomide (CC-220), CELMoDs in MM with Treg PD; any IKZF2-selective degrader in humans
  - **IL-1β / IL-6 / TNF pathway blockers** (NEW) — canakinumab, tocilizumab, infliximab, adalimumab, etanercept — ONLY when PD readouts include Treg function (not just count) and the study pre-specified Treg modulation
  - **NRP1 blockade** (NEW) — any human primary data
  - **CAR-T or bispecifics targeting Tregs** (NEW) — CCR8-CAR-T, mesothelin-BiTE-like that deplete Tregs, any Treg-selective cellular therapy
  - **JAK inhibitors, radiation therapy** — when Treg is an explicitly measured endpoint
  - **Chemo beyond cyclophosphamide** — INCLUDED only when Treg reduction is a pre-specified endpoint
- **Explicit exclusions (intervention class):**
  - **Fludarabine** (and fludarabine-containing lymphodepletion regimens in CAR-T/ACT) — OUT; sweeps in every adoptive-cell-therapy paper and Treg reduction is an expected pan-lymphocyte effect.
  - **Bempegaldesleukin as a Treg-reducer** — OUT for depletion; IN for ratio-shift.
- **Comparators:** any (single-arm, paired pre/post, treated-vs-untreated all acceptable; flagged in `design_type`).
- **Outcomes of interest:** any reported Treg PD readout — absolute count, frequency, Treg:Teff ratio, **in vitro suppression assay**, **FoxP3-stability / IKZF2 / Helios / TSDR methylation readout**, tumor/blood/tissue compartment levels. Durability captured separately.

## Tissue compartments (in scope)

- Peripheral blood (PBMC)
- Tumor (intratumoral, including biopsy/resection/FNA)
- Tumor-draining lymph node (TDLN)
- Bone marrow, ascites, pleural effusion, CSF — when reported
- Skin (e.g., mogamulizumab PD in CTCL; autoimmune skin biopsies)
- **One row per (study × tissue × timepoint-cluster × dose-cohort).** A PBMC + tumor + TDLN paper yields up to three rows.

## Filters

- **Date range:** 2000-01-01 → present (2026-04-23)
- **Language:** English only
- **Phases:** Phase 1, 1/2, 2, 3, window-of-opportunity, translational substudies, healthy-volunteer PD, case series (flagged in `design_type`)
- **Geography:** any
- **Study type allowed:** primary-research clinical reports with Treg PD data on ≥3 treated humans with Treg measurement.
- **Study type excluded from main table:** narrative reviews, editorials, commentaries, letters without primary data, preclinical-only reports, in vitro-only studies.
- **Side-list:** systematic reviews and meta-analyses — captured in a separate side-list (`reviews.jsonl`) for PI follow-up.

## Screening — inclusion criteria

Include if ALL of the following hold:

1. Human subjects, N ≥ 3 treated patients (or volunteers) with at least one Treg measurement.
2. Intervention is on the expanded in-scope list OR targets Treg modulation (depletion, inhibition, destabilization) as a pre-specified or reported endpoint.
3. Reports at least one Treg PD readout in at least one in-scope tissue compartment — count, frequency, ratio, or **suppressive-function / FoxP3-stability** readout.
4. Primary research (not review/editorial/commentary).
5. English, 2000–present.
6. **Intent-to-modulate gate:** study either (a) uses an intervention with a Treg-targeting mechanism, or (b) explicitly measures Treg as a pre-specified PD endpoint. Incidental Treg counts without intent are EXCLUDED.
7. **Failed / null attempts are INCLUDED** — failing to deplete is a valuable result.

## Screening — exclusion criteria

Exclude if ANY of the following hold:

- No Treg measurement, or measurement in < 3 treated subjects.
- Intervention is fludarabine-containing lymphodepletion without Treg-specific intent.
- Preclinical / animal / in vitro only.
- Review, editorial, commentary, letter without primary data. Systematic reviews and meta-analyses go to the side-list.
- Non-English.
- Study did not aim to modulate Tregs AND did not pre-specify Treg as a measured endpoint.

## Outcome definition — "reduction"

- **Absolute reduction** (classical depletion): `change_mechanism = absolute-reduction`.
- **Ratio / fraction shift** (e.g., CD8:Treg ratio up with stable Tregs): `change_mechanism = ratio-shift`.
- **Expansion-as-reduction** (bempeg-style; Tregs expand absolutely but Teff expand more): `change_mechanism = expansion-with-ratio-shift`.
- **Functional impairment only** (NEW emphasis): Treg counts unchanged but suppressive capacity reduced in vitro, or FoxP3/TSDR/Helios destabilization. `change_mechanism = functional-impairment-only`. Requires assay-level evidence.
- **Null** (intervention aimed to modulate but did not): `change_mechanism = null-result`.
- Accept paired pre/post and treated-vs-untreated designs.
- Report dose-cohort-level rows when multiple cohorts reported.

## Sources (priority order, NCBI-first)

1. **PubMed** (esearch / esummary / efetch) — primary discovery
2. **PMC** (efetch db=pmc) — full-text when PMCID available
3. **ClinicalTrials.gov** (v2 API) — cross-reference NCT IDs, design, results postings
4. **Europe PMC** — fallback full text
5. **WebSearch** — only for grey-literature / conference-abstract leads (not proactive)

Include `tool=trialist_screener&email=benjamin.g.vincent@gmail.com` on E-utilities calls. Stay under 3 req/sec.

## Per-run cap

- **Cap:** 50 kept items per run.
- **Screening ratio target:** ≥5× the cap.

## Query strategy — expanded families

Run per-family queries and merge. The expanded scope adds these term families:

**Function / destabilization tokens (add to every family):**

```
("Treg function"[tiab] OR "Treg suppressive function"[tiab] OR "Treg suppressive capacity"[tiab]
 OR "regulatory T cell function"[tiab] OR "Treg dysfunction"[tiab] OR "Treg destabilization"[tiab]
 OR "FOXP3 loss"[tiab] OR "FOXP3 instability"[tiab] OR "FoxP3 stability"[tiab]
 OR "TSDR methylation"[tiab] OR "Helios"[tiab] OR "IKZF2"[tiab]
 OR "Treg fragility"[tiab] OR "Treg conversion"[tiab])
```

**Anti-TNFR2 family:**

```
("anti-TNFR2"[tiab] OR "TNFR2 antagonist"[tiab] OR "TNFR2 antibody"[tiab]
 OR "BAT2506"[tiab] OR "HFB200301"[tiab] OR "HFB-2"[tiab] OR "tumor necrosis factor receptor 2"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab])
```

**Anti-TIGIT (inhibition-pathway) family:**

```
("tiragolumab"[tiab] OR "vibostolimab"[tiab] OR "domvanalimab"[tiab]
 OR "ociperlimab"[tiab] OR "EOS-448"[tiab] OR "anti-TIGIT"[tiab] OR "TIGIT antibody"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab] OR "suppressive function"[tiab])
```

**EP4 antagonist family:**

```
("grapiprant"[tiab] OR "ONO-4578"[tiab] OR "palupiprant"[tiab] OR "EP4 antagonist"[tiab]
 OR "prostaglandin E2 receptor 4"[tiab] OR "PTGER4 antagonist"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab])
```

**DNMTi / HMA family (Treg-focused):**

```
("azacitidine"[tiab] OR "decitabine"[tiab] OR "guadecitabine"[tiab] OR "DNMT inhibitor"[tiab]
 OR "hypomethylating"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab] OR "TSDR"[tiab])
```

**HDACi family:**

```
("romidepsin"[tiab] OR "vorinostat"[tiab] OR "panobinostat"[tiab] OR "entinostat"[tiab]
 OR "mocetinostat"[tiab] OR "HDAC inhibitor"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab] OR "suppressive function"[tiab])
```

**Helios / IKZF2 / cereblon-degrader family:**

```
("mezigdomide"[tiab] OR "iberdomide"[tiab] OR "CC-220"[tiab] OR "CC-92480"[tiab]
 OR "CELMoD"[tiab] OR "cereblon"[tiab] OR "IKZF2"[tiab] OR "Helios"[tiab]
 OR "Ikaros degrader"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab])
```

**PI3Kδ inhibitor family (function-focused):**

```
("idelalisib"[tiab] OR "copanlisib"[tiab] OR "umbralisib"[tiab] OR "duvelisib"[tiab]
 OR "parsaclisib"[tiab] OR "PI3K delta"[tiab] OR "PI3Kdelta"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "suppressive function"[tiab])
```

**Anti-GITR / anti-OX40 (function-focused re-query):**

```
("TRX518"[tiab] OR "MK-4166"[tiab] OR "MK-1248"[tiab] OR "BMS-986156"[tiab] OR "GWN323"[tiab]
 OR "PF-04518600"[tiab] OR "MEDI6469"[tiab] OR "MEDI0562"[tiab] OR "MOXR0916"[tiab] OR "BMS-986178"[tiab]
 OR "anti-GITR"[tiab] OR "anti-OX40"[tiab])
AND ("suppressive function"[tiab] OR "Treg function"[tiab] OR "FOXP3"[tiab] OR "Treg"[tiab])
```

**IL-1β / IL-6 / TNF pathway Treg-PD:**

```
("canakinumab"[tiab] OR "tocilizumab"[tiab] OR "infliximab"[tiab] OR "adalimumab"[tiab]
 OR "etanercept"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab] OR "suppressive function"[tiab])
AND ("pharmacodynamic"[tiab] OR "pre-specified"[tiab] OR "primary endpoint"[tiab] OR "biomarker"[tiab])
```

**NRP1 blockade:**

```
("neuropilin-1"[tiab] OR "NRP1"[tiab] OR "NRP-1"[tiab])
AND ("Treg"[tiab] OR "regulatory T"[tiab] OR "FOXP3"[tiab])
AND ("clinical"[tiab] OR "patient"[tiab] OR "trial"[tiab])
```

**CAR-T / bispecific Treg-selective:**

```
("CCR8 CAR"[tiab] OR "Treg CAR"[tiab] OR "Treg depleting"[tiab] OR "Treg selective bispecific"[tiab])
AND ("clinical"[tiab] OR "patient"[tiab] OR "trial"[tiab])
```

Merge all family results; dedupe by NCT > DOI > PMID > title; cap at 50.

## Known watch-outs

- CAR-T papers will flood via fludarabine — filter aggressively.
- "Regulatory T cell" is used loosely in some papers (no FoxP3 confirmation); flag in `gating_quality`.
- Older ipilimumab/tremelimumab intratumoral Treg depletion papers are contested; both supportive and null reports retained.
- Mogamulizumab in CTCL has rich skin + blood data — expect multiple rows per paper.
- **TNFR2 antagonists and Helios degraders are early-clinical** — expect thin human PD literature, possibly only abstracts/conference reports.
- **Anti-TIGIT literature is enormous** but most papers don't report Treg suppressive-function readouts — filter hard for "suppressive function" / "functional impairment" / "Treg fragility" signal.
- HDACi and DNMTi have a mix of Treg-UP and Treg-DOWN signals depending on dose and context — report both honestly, use `change_mechanism = functional-impairment-only` only when an actual suppression assay is done.
