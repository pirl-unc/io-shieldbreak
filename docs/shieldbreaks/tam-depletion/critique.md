# Trialist critique — Tumor-associated Macrophage Depletion, Inhibition, or Repolarization

_Last updated: 2026-04-24. Papers reviewed: 35._

[← back to shieldbreak](index.md) · [← back to shieldbreaks](../index.md)

## Top-line findings

<details class="sb-section" open markdown="1">
<summary>Show / hide</summary>


_(see synthesis section below for cross-paper findings)_

</details>

## Summary stats

<details class="sb-section" open markdown="1">
<summary>Show / hide</summary>


- **Papers critiqued:** 35
- **Extraction-fidelity discrepancies flagged:** 4
- **Retractions / corrections / expressions of concern:** 0

### Risk-of-bias distribution

| Rating | N |
|---|---:|
| Low | 1 |
| Moderate | 28 |
| Serious | 5 |
| not-amenable-to-standard-rob | 1 |

### Per-trial confidence distribution

| Confidence | N |
|---|---:|
| High | 2 |
| Low | 16 |
| Moderate | 17 |

### Counter-productive-mechanism severity distribution

| Severity | N |
|---|---:|
| High | 6 |
| Moderate | 25 |
| Unknown | 4 |

</details>

## Per-paper critiques

<details class="sb-section" open markdown="1">
<summary>Show / hide</summary>


### Advani R 2018 — CD47 Blockade by Hu5F9-G4 and Rituximab in Non-Hodgkin's Lymphoma

**Citation.** [PMID 30380386](https://pubmed.ncbi.nlm.nih.gov/30380386/) · [PMCID PMC8058634](https://pmc.ncbi.nlm.nih.gov/articles/PMC8058634/) · [DOI 10.1056/NEJMoa1807315](https://doi.org/10.1056/NEJMoa1807315) · [NCT NCT02953509](https://clinicaltrials.gov/study/NCT02953509)
**Source tier.** pmc_full_text

**Key critique.** High-impact NEJM phase 1b paper demonstrating 50% ORR / 36% CR in rituximab-refractory NHL with magrolimab + rituximab. **Critical caveat for this shieldbreak: phagocytosis of tumor cells is not directly measured ex vivo.** The mechanism is *inferred* from (a) ~100% CD47 receptor occupancy on circulating cells and (b) clinical response. The screener's `depletion_success: not-assessed` is correct — and this critique supports capping per-trial confidence on the TAM-biology claim accordingly. The clinical efficacy is the paper's main contribution; the TAM-biology row is supporting-evidence only.

**Design.** Phase 1b, 3+3 dose-escalation, 10/20/30 mg/kg maintenance dosing + 1 mg/kg priming, rituximab 375 mg/m² weekly cycle 1 then monthly cycles 2–6. n=22 (15 DLBCL + 7 FL). CD47-RO by flow; 5F9 tumor penetrance by anti-human IgG4 IHC in one patient. ITT analysis for response (1 patient with DLT-driven discontinuation counted as non-responder).
**Sample size & power.** n=22 total, n=13 in the 30 mg/kg maintenance dose cohort. Phase 1b — not powered for efficacy; ITT inclusion of discontinued patients is the rigorous choice.
**Effect-size calibration.** 50% ORR in rituximab-refractory DLBCL/FL is striking. The ENHANCE trial series and subsequent phase 3 data in MDS eventually showed magrolimab's efficacy was more context-dependent than early phase 1 suggested (ENHANCE-2 / ENHANCE-3 failures in AML). For NHL the follow-up has been attenuated; magrolimab's development has substantially slowed across the program.
**Missing data.** One patient discontinued at ~2 weeks due to ITP; included as non-responder in ITT. Grade 4 neutropenia and grade 3 ITP were the two DLTs in cohort 3 — relevant safety signals.
**Multiplicity.** Primary endpoints (safety, RP2D); efficacy a secondary. No formal efficacy hypothesis test.
**Generalizability.** Heavily pretreated (median 4 prior lines) rituximab-refractory NHL — a high-unmet-need population. Excluded: baseline hemoglobin <9.5 (pre-enriches for healthier patients).
**Gating / definition.** CD47-RO on circulating RBCs and WBCs by flow; anti-IgG4 tumor IHC in one case. No ex-vivo phagocytosis assay, no direct TAM quantification. **This is the crux of the shieldbreak gap.**
**Counter-productive mechanisms (Moderate (`on-target-anemia`, `on-target-thrombocytopenia`, `homeostatic-clearance-disruption`)).** Predictable on-target: CD47 is on RBCs → anemia (grade 1-2 in all patients; mitigated by priming-dose strategy leveraging aging-RBC clearance). Also on platelets: one grade 3 ITP as DLT. Beyond cytopenias: by blocking the 'don't eat me' signal systemically, magrolimab can disrupt homeostatic removal of aged cells and may induce compensatory SIRPα-high macrophage selection. The paper notes no late toxicities at 6-8 month follow-up; long-term CD47-blockade data remain thin.
**COI & funding.** Funded by Forty Seven (later acquired by Gilead) and LLS. Disclosure forms in supplement — company employment for several authors.
**Spin / abstract-to-text consistency.** Measured — 'promising activity' claim tracks the data. The specific phrase 'no clinically significant safety events' understates the two DLTs and the expected anemia; it is a common NEJM editorial convention but is not a faithful summary of the safety table.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Phase 1b single-arm; ITT analysis and independent central review for radiology reduce but do not eliminate selection bias concerns.
**Per-trial confidence.** **Low** — Per the user's instruction and per methodological principle: for the *TAM-biology* claim this row represents, mechanism is inferred not measured, so Low is the appropriate cap. (The clinical-efficacy claim would rate higher — but that is not this shieldbreak's question.)

---

### Autio KA 2020 — Immunomodulatory Activity of a Colony-stimulating Factor-1 Receptor Inhibitor in Patients with Advanced Refractory Breast or Prostate Cancer

**Citation.** [PMID 32847933](https://pubmed.ncbi.nlm.nih.gov/32847933/) · [DOI 10.1158/1078-0432.CCR-20-0855](https://doi.org/10.1158/1078-0432.CCR-20-0855) · [NCT NCT02265536](https://clinicaltrials.gov/study/NCT02265536)
**Source tier.** pubmed_abstract

**Key critique.** Phase 1 of anti-CSF1R mAb LY3022855 in 34 advanced MBC / mCRPC patients across four schedules. PD on blood monocytes is the headline PBMC readout; no tumor macrophage depletion is directly shown in the abstract. Clinical activity is modest (SD as best response).

**Design.** Phase 1 dose-escalation, four schedule cohorts (A-D, 1.0–1.25 mg/kg weekly/biweekly and 100 mg weekly/biweekly). Open-label, single-arm. Efficacy by RECIST and PCWG2. Not powered for efficacy.
**Sample size & power.** n=34 (22 MBC + 12 mCRPC). Schedule comparison is descriptive across small cohorts (≤10 per cohort); cannot resolve dose-schedule differences.
**Effect-size calibration.** Best response SD only (23% in MBC, 25% in mCRPC) — consistent with other CSF1R monotherapy in non-CSF1-driven solid tumors (LY3022855 D2G, AMG 820, emactuzumab monotherapy). This is the 'null effect on tumor' finding that the tam-depletion table should weigh carefully.
**Missing data.** Not inferable from abstract.
**Multiplicity.** Multiple schedule cohorts compared descriptively; no adjustment.
**Generalizability.** Heavily pretreated advanced MBC and mCRPC — a setting where TAMs are only one axis of immune dysfunction. Extrapolation to other TAM-high tumors (PDAC, GBM) is limited.
**Gating / definition.** Proinflammatory CD14^dim CD16^bright monocytes decreased at day 8 in PBMCs — a well-validated CSF1R PD marker in circulation. No tumor macrophage definition verifiable from the abstract.
**Counter-productive mechanisms (Moderate (`csf1-rebound`, `non-classical-monocyte-depletion`, `tissue-macrophage-collateral`)).** CSF1R blockade depletes CD14^dim CD16^bright non-classical monocytes, which include antigen-presenting and patrolling subsets. On-target: compensatory CSF1 ligand rise — the classic CSF1 plasma spike — is present at day 8 per the abstract ('circulating CSF-1 levels increased'), confirming ligand accumulation that can enable IL-34-driven rebound TAM restoration once dosing changes.
**COI & funding.** Eli Lilly funded and employed co-authors (D. Schaer et al.); multiple academic authors report Lilly grants during the study. Consistent with a sponsored phase 1 and appropriately disclosed.
**Spin / abstract-to-text consistency.** Abstract uses 'clinically meaningful stable disease >9 months' for 2 MBC patients — terminology that is defensible but selects favorable outliers. Headline framing ('well tolerated and showed evidence of immune modulation') tracks the data.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Serious** — Single-arm phase 1 with 4-way schedule variation and no tumor PD in abstract; bias in selection of the 'durable SD' patients is unavoidable.
**Per-trial confidence.** **Low** — Abstract-only read; the row concerns PBMC monocyte PD (well-validated), but no tumor TAM depletion is demonstrated in this publication.

---

### Beckermann KE 2024 — A phase 1b open-label study to evaluate the safety, tolerability, pharmacokinetics, and pharmacodynamics of PY314 in combination with pembrolizumab in patients with advanced renal cell carcinoma

**Citation.** [PMID 38372949](https://pubmed.ncbi.nlm.nih.gov/38372949/) · [DOI 10.1007/s10637-024-01419-1](https://doi.org/10.1007/s10637-024-01419-1) · [NCT NCT04691375](https://clinicaltrials.gov/study/NCT04691375)
**Source tier.** pubmed_abstract

**Key critique.** Phase 1b PY314 (anti-TREM2) + pembrolizumab in ICI-refractory RCC. Small cohort; paired tumor biopsies intended. Limited activity in ICI-refractory setting — expected for single TAM-modulator addition.

**Design.** Phase 1b open-label single-arm, NCT05367401. Combination safety and PK/PD primary.
**Sample size & power.** Small (phase 1b).
**Effect-size calibration.** Limited activity in ICI-refractory RCC is class-consistent.
**Missing data.** Not extractable from abstract.
**Multiplicity.** Descriptive.
**Generalizability.** ICI-refractory RCC — highly pre-selected.
**Gating / definition.** Not visible in abstract.
**Counter-productive mechanisms (Moderate (`neurodegeneration-risk`, `osteoclast-depletion`, `irAE-stacking`)).** Same TREM2 class concerns as Yeku 2025. Stacked with pembrolizumab-typical irAE risk.
**COI & funding.** Pionyr / Merck; not in abstract.
**Spin / abstract-to-text consistency.** Cannot fully assess from abstract.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1b.
**Per-trial confidence.** **Low** — Abstract-only.

---

### Bhatia S 2019 — Intratumoral G100, a TLR4 Agonist, Induces Antitumor Immune Responses and Tumor Regression in Patients with Merkel Cell Carcinoma

**Citation.** [PMID 30093453](https://pubmed.ncbi.nlm.nih.gov/30093453/) · [PMCID PMC6368904](https://pmc.ncbi.nlm.nih.gov/articles/PMC6368904/) · [DOI 10.1158/1078-0432.CCR-18-0469](https://doi.org/10.1158/1078-0432.CCR-18-0469)
**Source tier.** pmc_full_text

**Key critique.** Pilot IT TLR4 agonist (G100/GLA-SE) in 10 patients with MCC (3 locoregional + 7 metastatic). CD8 infiltration and pathologic CR in 1 neoadjuvant patient. Very small; the paper is appropriately hedged. The G100 program has not progressed past pilot.

**Design.** Pilot open-label single-arm, two cohorts (neoadjuvant LR and metastatic). Paired biopsies d0 and d22/surgery.
**Sample size & power.** n=10 total. Hypothesis-generating only.
**Effect-size calibration.** 1 pCR in neoadjuvant + 2 durable PRs in metastatic — activity consistent with TLR4-driven local immune activation but very small.
**Missing data.** All 10 completed ≥1 cycle. Reported fully.
**Multiplicity.** Multiple biomarkers; exploratory.
**Generalizability.** MCC is a virally-driven immunogenic tumor — strong prior probability of response to any immune stimulus.
**Gating / definition.** Multispectral IHC with CD4/CD8/CD68/PD-1/PD-L1 and single-marker CD68 for macrophages. Limited TAM-specific quantification.
**Counter-productive mechanisms (Moderate (`pd-l1-induction`, `ido1-induction`, `tolerogenic-dc-activation`, `cytokine-release`)).** TLR4 agonism class risks: (a) activation of tolerogenic / regulatory DCs in certain TMEs; (b) IDO1 and PD-L1 induction as compensatory checkpoints; (c) systemic flu-like cytokine response. In MCC (immunogenic) these risks are likely outweighed by antigen-reveal benefit, but in cold tumors the counter-productive wing could dominate.
**COI & funding.** Immune Design funded / employed co-authors with patent interest in GLA. Academic-industry collaboration transparently disclosed.
**Spin / abstract-to-text consistency.** Paper is appropriately cautious given n=10.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Pilot; small n precludes strong inference.
**Per-trial confidence.** **Low** — Full text; n=10 limits weight regardless of biological plausibility.

---

### Boal LH 2020 — Pediatric PK/PD Phase I Trial of Pexidartinib in Relapsed and Refractory Leukemias and Solid Tumors Including Neurofibromatosis Type I-Related Plexiform Neurofibromas

**Citation.** [PMID 32943455](https://pubmed.ncbi.nlm.nih.gov/32943455/) · [PMCID PMC7909006](https://pmc.ncbi.nlm.nih.gov/articles/PMC7909006/) · [DOI 10.1158/1078-0432.CCR-20-1696](https://doi.org/10.1158/1078-0432.CCR-20-1696)
**Source tier.** pmc_full_text

**Key critique.** Pediatric phase 1 of pexidartinib in relapsed/refractory leukemia (NCT02390752). Row captures PBMC monocyte PD. Pediatric-specific growth/bone concerns for CSF1R inhibition are relevant here but not tested beyond safety. Few responses in a small cohort.

**Design.** Pediatric phase 1, rolling-6 dose escalation, pexidartinib 400–600 mg/m²/day, relapsed/refractory leukemia.
**Sample size & power.** Small pediatric cohort; PD signals class-consistent.
**Effect-size calibration.** Limited clinical activity; expected for pediatric dose-escalation.
**Missing data.** Reported.
**Multiplicity.** Descriptive.
**Generalizability.** Pediatric leukemia — bone marrow macrophage biology differs from solid-tumor TAM biology.
**Gating / definition.** CD14+CD16+ subset flow cytometry; absolute monocyte counts.
**Counter-productive mechanisms (Moderate (`osteoclast-depletion`, `pediatric-growth-risk`, `hepatotoxicity`, `csf1-rebound`)).** Pediatric-specific: osteoclast depletion by CSF1R blockade in growing patients raises long-term bone-development concerns not captured in phase 1 duration. CSF1R class collateral (hepatic, cutaneous) applies. Pexidartinib's KIT/FLT3-ITD activity has specific relevance in leukemia and complicates interpretation of PBMC counts.
**COI & funding.** Plexxikon/Daiichi Sankyo funded; NIH support.
**Spin / abstract-to-text consistency.** Reasonable.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard pediatric phase 1 design.
**Per-trial confidence.** **Low** — Full text read; pediatric-leukemia context limits transferability to the shieldbreak's typical TAM biology.

---

### Byrne KT 2021 — Neoadjuvant Selicrelumab, an Agonist CD40 Antibody, Induces Changes in the Tumor Microenvironment in Patients with Resectable Pancreatic Cancer

**Citation.** [PMID 34112709](https://pubmed.ncbi.nlm.nih.gov/34112709/) · [PMCID PMC8667686](https://pmc.ncbi.nlm.nih.gov/articles/PMC8667686/) · [DOI 10.1158/1078-0432.CCR-21-1047](https://doi.org/10.1158/1078-0432.CCR-21-1047)
**Source tier.** pmc_full_text

**Key critique.** Neoadjuvant selicrelumab (CD40 agonist) ± chemo in resectable PDAC with pre- and post-treatment tumor biopsies. Shows macrophage activation markers (M1 shift) — the rare 'repolarization-without-depletion' pattern. Small n; translational paper. Follow-up combination trials have been disappointing.

**Design.** Neoadjuvant window-of-opportunity study in resectable PDAC, paired pre-post tumor biopsies.
**Sample size & power.** Small (phase 1 neoadjuvant).
**Effect-size calibration.** Macrophage repolarization documented; clinical impact on resection outcomes unclear at this sample size.
**Missing data.** Reported.
**Multiplicity.** Multiple biomarker readouts; exploratory.
**Generalizability.** Resectable PDAC — narrow population.
**Gating / definition.** mIF / scRNA-seq with CD68, CD163, HLA-DR, CD206 panels. Multi-marker repolarization assessment is stronger than single-marker IHC.
**Counter-productive mechanisms (Moderate (`cytokine-release`, `hepatotoxicity`, `thromboembolism`, `premature-t-cell-differentiation`)).** CD40 agonism: cytokine release syndrome (often transient but clinically relevant), transaminitis, thromboembolism. In the context of a planned surgery, CD40-agonist-induced transaminitis or CRS could delay resection — a clinical counter-productive outcome. Systemic T-cell activation without cognate tumor-antigen engagement may drive exhaustion.
**COI & funding.** Roche/Genentech; academic authors (Vonderheide).
**Spin / abstract-to-text consistency.** Measured — translational-biology paper.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Translational neoadjuvant with paired biopsies — well-designed for PD question; small n.
**Per-trial confidence.** **Moderate** — Full text; multi-marker repolarization evidence is stronger than CD163-only single-marker IHC that other rows sometimes rely on.

---

### Cassier PA 2020 — Long-term clinical activity, safety and patient-reported quality of life in patients with tenosynovial giant cell tumour treated with emactuzumab

**Citation.** [PMID 33161240](https://pubmed.ncbi.nlm.nih.gov/33161240/) · [DOI 10.1016/j.ejca.2020.09.038](https://doi.org/10.1016/j.ejca.2020.09.038) · [NCT NCT01494688](https://clinicaltrials.gov/study/NCT01494688)
**Source tier.** pubmed_abstract

**Key critique.** Long-term follow-up of a single-arm phase 1 dTGCT cohort (n=63 enrolled; biopsies in 36). Durable CSF1R+/CD163+ macrophage depletion with on-target skin/face AEs consistent with the drug class. I can only see the abstract — methodological detail (ITT handling, imputation, biopsy timing) is not verifiable without the full text.

**Design.** Open-label phase 1 dose-escalation + expansion (NCT01494688), monotherapy emactuzumab 900–2000 mg q2w escalation with OBD 1000 mg in expansion. Single-arm; no randomization or blinding. Response assessed by central MRI per RECIST 1.1. Abstract reports independently reviewed ORR.
**Sample size & power.** 63 patients enrolled; 36 with biopsy. Not powered — phase 1 descriptive. Large, consistent response rate (71% ORR, durable at 1-2y) mitigates the small-sample concern in this rare indication.
**Effect-size calibration.** ORR and biomarker response consistent with other CSF1R monotherapy in TGCT (pexidartinib ENLIVEN, axatilimab-TGCT extensions). dTGCT is a CSF1-driven disease; a class effect is biologically expected and has been reproduced.
**Missing data.** Cannot assess attrition or imputation from abstract. 27/63 patients without biopsy is substantial missingness in the PD sub-analysis.
**Multiplicity.** Multiple endpoints (ORR, safety, QoL WOMAC, EuroQol) with no pre-specified hierarchy visible in abstract; AE-domain multiplicity not corrected (standard in phase 1).
**Generalizability.** dTGCT is a locally aggressive, CSF1-driven neoplasm — mechanistically a 'best case' for CSF1R blockade. Findings should not be extrapolated to TAM biology in solid tumors without intact CSF1R-independent TAM subsets.
**Gating / definition.** CSF1R+ and CD68/CD163+ IHC in tumor biopsies. Dual-marker macrophage gating is standard but not multiplexed in the abstract; cannot confirm spatial or tumor-compartment quantitation from abstract alone.
**Counter-productive mechanisms (Moderate (`tissue-macrophage-collateral`, `csf1-rebound`, `il34-escape`)).** CSF1R blockade depletes tissue-resident macrophages broadly — osteoclasts (fracture risk in long-term dosing), Kupffer cells (transaminitis / periorbital edema from dermal Langerhans-cell depletion are already seen). For dTGCT specifically these are largely AE considerations, but in an oncology-repurposing frame they matter: compensatory CSF1 plasma rebound and monocyte expansion can re-populate the TAM niche via CSF1R-independent (IL-34-driven) routes once dosing stops.
**COI & funding.** Funding and disclosures not visible in abstract; prior reports (Cassier Lancet Oncol 2015) were Roche-funded with employment/consulting disclosures.
**Spin / abstract-to-text consistency.** Abstract framing is measured — 'pronounced and durable responses…manageable safety profile' is consistent with the reported 71% ORR in this indication.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Single-arm open-label trial in a rare indication with objective central imaging review mitigates detection bias, but confounding and selection bias cannot be ruled out without the full text.
**Per-trial confidence.** **Moderate** — Proof-of-mechanism is strong in dTGCT where CSF1 is the genetic driver; for this table's purposes (TAM depletion in oncology), confidence is capped at Moderate because I only read the abstract.

---

### Coveler AL 2023 — SEA-CD40, a non-fucosylated CD40 agonist: a phase 1 dose-escalation study

**Citation.** [PMID 37385724](https://pubmed.ncbi.nlm.nih.gov/37385724/) · [PMCID PMC10314623](https://pmc.ncbi.nlm.nih.gov/articles/PMC10314623/) · [DOI 10.1136/jitc-2022-005584](https://doi.org/10.1136/jitc-2022-005584) · [NCT NCT02376699](https://clinicaltrials.gov/study/NCT02376699)
**Source tier.** pmc_full_text

**Key critique.** Phase 1 dose-escalation of SEA-CD40 (non-fucosylated CD40 agonist designed for enhanced Fc-γRIIIA binding). PBMC PD readouts; modest clinical activity. Class-typical CRS profile.

**Design.** Phase 1 dose-escalation, solid tumors and lymphoma.
**Sample size & power.** Small phase 1.
**Effect-size calibration.** Modest activity as monotherapy — consistent with CD40-agonist class.
**Missing data.** Reported.
**Multiplicity.** Descriptive.
**Generalizability.** Advanced solid tumors / lymphoma.
**Gating / definition.** PBMC flow; tumor biomarkers secondary.
**Counter-productive mechanisms (Moderate (`cytokine-release`, `thromboembolism`, `premature-t-cell-differentiation`)).** SEA-CD40's enhanced Fc engineering may increase non-cognate T-cell activation and exhaustion driver potential. CRS and thromboembolism are the dominant clinical counter-productive signals.
**COI & funding.** Seagen funded.
**Spin / abstract-to-text consistency.** Measured.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1.
**Per-trial confidence.** **Moderate** — Full text; PBMC PD well-characterized.

---

### Daver N 2025 — Azacitidine, Venetoclax, and Magrolimab in Newly Diagnosed and Relapsed Refractory Acute Myeloid Leukemia

**Citation.** [PMID 40198272](https://pubmed.ncbi.nlm.nih.gov/40198272/) · [PMCID PMC12165814](https://pmc.ncbi.nlm.nih.gov/articles/PMC12165814/) · [DOI 10.1158/1078-0432.CCR-25-0229](https://doi.org/10.1158/1078-0432.CCR-25-0229)
**Source tier.** pmc_full_text

**Key critique.** Triplet magrolimab + aza + venetoclax in newly-diagnosed + R/R AML. Post-ENHANCE futility this paper is essentially the program's 'wind-down' combination-exploration dataset. Responses reported; **TAM biology again inferred, not measured**. Venetoclax adds its own myelosuppression to magrolimab-related anemia.

**Design.** Phase 1/2 (NCT03248479 MDS stream or parallel AML study, details in full text). Triplet with decoupled magrolimab dosing schedules.
**Sample size & power.** AML-specific cohort size in full text.
**Effect-size calibration.** Activity reported in newly-diagnosed AML approximating other aza+ven regimens; the question is whether magrolimab adds value — answered 'no' at the phase 3 level (ENHANCE-3).
**Missing data.** Described in Methods.
**Multiplicity.** Multiple cohorts — descriptive.
**Generalizability.** AML newly-diagnosed (unfit) and R/R — two distinct populations pooled.
**Gating / definition.** Bone marrow response assessment; magrolimab RO in circulating cells. No direct TAM quantification.
**Counter-productive mechanisms (High (`hematologic-stacking`, `on-target-anemia`, `dose-intensity-failure`)).** Three-drug hematologic toxicity stacking: anemia (magrolimab on-target) + thrombocytopenia (venetoclax/magrolimab) + neutropenia (azacitidine/venetoclax). The cytopenia burden can force dose delays that reduce target engagement — a dose-intensity-based counter-productive pathway.
**COI & funding.** Gilead/Forty Seven; extensive industry disclosures.
**Spin / abstract-to-text consistency.** Measured.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1/2 single-arm design.
**Per-trial confidence.** **Low** — TAM mechanism inferred; phase 3 failure in the same mechanism/context caps the weight this paper should carry.

---

### Dowlati A 2021 — LY3022855, an anti-colony stimulating factor-1 receptor (CSF-1R) monoclonal antibody, in patients with advanced solid tumors

**Citation.** [PMID 33624233](https://pubmed.ncbi.nlm.nih.gov/33624233/) · [DOI 10.1007/s10637-021-01084-8](https://doi.org/10.1007/s10637-021-01084-8) · [NCT NCT01346358](https://clinicaltrials.gov/study/NCT01346358)
**Source tier.** pubmed_abstract

**Key critique.** Phase 1 dose-escalation of LY3022855 in refractory solid tumors with weight-based (part A) and flat-dose (part B) cohorts. PBMC monocyte PD reported; limited clinical efficacy. Abstract-only.

**Design.** Phase 1 dose-escalation, two parts (weight-based and non-weight-based), multiple dose levels from 0.3 mg/kg Q2W up to flat 200 mg Q2W range. Open-label, single-arm.
**Sample size & power.** Sample size not pulled into abstract tail; appears multiple-dozen patients across cohorts.
**Effect-size calibration.** Consistent with other CSF1R monotherapy in all-comer solid tumors: limited objective response; PBMC PD present. Class-consistent.
**Missing data.** Not extractable.
**Multiplicity.** Multiple cohorts; descriptive reporting.
**Generalizability.** Heavily pretreated all-comer cohort.
**Gating / definition.** Abstract mentions PD readouts on circulating monocyte subsets; no tumor TAM gating detail extractable.
**Counter-productive mechanisms (Moderate (`csf1-rebound`, `tissue-macrophage-collateral`, `ada-blunted-target-engagement`)).** Same class profile as other CSF1R mAbs: CSF1 ligand rise, tissue macrophage depletion, IL-34-driven escape. Immunogenicity (ADAs at 3× emactuzumab's rate per Falchook 2021 discussion) may blunt sustained target engagement — a potential counter-productive-via-pharmacokinetic failure.
**COI & funding.** Eli Lilly sponsored; disclosures not in abstract.
**Spin / abstract-to-text consistency.** Cannot assess from abstract.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 design; bias profile unremarkable.
**Per-trial confidence.** **Low** — Abstract-only; PBMC PD is well-replicated but tumor TAM depletion not demonstrated here.

---

### Falchook GS 2021 — A phase 1a/1b trial of CSF-1R inhibitor LY3022855 in combination with durvalumab or tremelimumab in patients with advanced solid tumors

**Citation.** [PMID 33852104](https://pubmed.ncbi.nlm.nih.gov/33852104/) · [DOI 10.1007/s10637-021-01088-4](https://doi.org/10.1007/s10637-021-01088-4) · [NCT NCT02718911](https://clinicaltrials.gov/study/NCT02718911)
**Source tier.** pubmed_abstract

**Key critique.** Phase 1a/1b of LY3022855 combined with durvalumab or tremelimumab in advanced solid tumors. Row captures PBMC PD. Clinical benefit limited; ADAs reportedly higher than for emactuzumab (cross-study note from Gomez-Roca 2022 discussion). Abstract-only.

**Design.** Dose-escalation and expansion, NSCLC and ovarian cohorts at RP2D, open-label single-arm. Two ICI partners (anti-PD-L1 vs anti-CTLA-4) in separate arms — no head-to-head comparison.
**Sample size & power.** Modest cohort sizes per expansion arm.
**Effect-size calibration.** Gomez-Roca 2022 discussion notes 'LY3022855 combined with durvalumab lacked objective responses in 19 NSCLC patients.' That cross-study comparison is consistent with this abstract's tenor.
**Missing data.** Not extractable.
**Multiplicity.** Multiple dose cohorts × two ICI partners × two tumor types — descriptive only.
**Generalizability.** Advanced refractory all-comer then NSCLC/OC expansions.
**Gating / definition.** Monocyte PD in blood; full gating not visible.
**Counter-productive mechanisms (Moderate (`ada-blunted-target-engagement`, `csf1-rebound`, `tissue-macrophage-collateral`)).** ADA-driven loss of exposure is an explicit concern the Gomez-Roca paper raises in comparing this drug to emactuzumab. PD loss at later cycles could actively select for counter-productive outcomes if TAM recovery occurs in the presence of continuing ICI pressure. Standard CSF1R class collateral applies.
**COI & funding.** Eli Lilly and AstraZeneca sponsors; not in abstract.
**Spin / abstract-to-text consistency.** Cannot assess.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1; open-label dose-escalation limits inference.
**Per-trial confidence.** **Low** — Abstract-only plus apparent lack of objective response in a key expansion cohort caps the weight this row should carry.

---

### Germano G 2013 — Role of macrophage targeting in the antitumor activity of trabectedin

**Citation.** [PMID 23410977](https://pubmed.ncbi.nlm.nih.gov/23410977/) · [DOI 10.1016/j.ccr.2013.01.008](https://doi.org/10.1016/j.ccr.2013.01.008)
**Source tier.** pubmed_abstract

**Key critique.** Landmark mechanistic paper (Cancer Cell 2013, Allavena/Mantovani lab) demonstrating trabectedin's monocyte/macrophage selectivity in mouse tumor models AND a small human monocyte-depletion observation. Primarily preclinical with translational confirmation. The row represents the human monocyte-depletion observation — a small n from a preclinically-dominant paper.

**Design.** Mostly preclinical (4 mouse tumor models with caspase-8-dependent monocyte apoptosis); translational human component is a small observation in treated patients.
**Sample size & power.** Human cohort size small (not specified in abstract but low double-digits).
**Effect-size calibration.** The mouse data anchor the mechanistic hypothesis; the human component is confirmatory not powered.
**Missing data.** N/A for a mostly-preclinical paper.
**Multiplicity.** Multiple mouse models tested.
**Generalizability.** Mouse findings validated in trabectedin-approved indications (sarcoma, ovarian).
**Gating / definition.** Blood monocyte depletion measured — standard flow cytometry; details not in abstract.
**Counter-productive mechanisms (Moderate (`systemic-cytotoxicity`, `compensatory-myelopoiesis`, `steroid-premedication-immunosuppression`)).** Trabectedin depletes pro-inflammatory monocytes and TAMs via caspase-8-dependent apoptosis — the selectivity for mononuclear phagocytes over neutrophils and lymphocytes is mechanistically attractive but imperfect (clinical use shows cytopenias). In long-term use: compensatory myelopoiesis, steroid premedication-induced immunosuppression.
**COI & funding.** Italian and EU funding; Pharmamar connection.
**Spin / abstract-to-text consistency.** Measured translational claim.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** none: **not-amenable-to-standard-rob** — Predominantly preclinical paper with a small translational component; RoB tools don't apply.
**Per-trial confidence.** **Low** — Abstract-only + small human cohort; the paper's translational value is in its mechanism hypothesis, not in patient-level TAM quantification.

---

### Gomez-Roca C 2022 — Anti-CSF-1R emactuzumab in combination with anti-PD-L1 atezolizumab in advanced solid tumor patients naive or experienced for immune checkpoint blockade

**Citation.** [PMID 35577503](https://pubmed.ncbi.nlm.nih.gov/35577503/) · [PMCID PMC9114963](https://pmc.ncbi.nlm.nih.gov/articles/PMC9114963/) · [DOI 10.1136/jitc-2021-004076](https://doi.org/10.1136/jitc-2021-004076) · [NCT NCT02323191](https://clinicaltrials.gov/study/NCT02323191)
**Source tier.** pmc_full_text

**Key critique.** Large phase 1b (N=221) with the most complete TAM PD dataset in the set. Marked reduction of CSF1R+ and CD163+ TAMs in paired tumor biopsies (median −80% CSF1R+, −63% CD163+ in non-PD patients; CSF1R+ −72% / CD163+ −28% in non-PD — the paper itself notes the counterintuitive direction: less TAM reduction was associated with clinical benefit). Clinical activity is modest (ORR 9.8% UBC-naïve, 12.5% NSCLC ICB-experienced). The authors' own finding that TAM persistence tracked with CD8 expansion is an important negative-for-the-hypothesis result worth flagging.

**Design.** Phase 1b, open-label, non-randomized, multicenter (NCT02323191) with 3+3 dose escalation up to OBD 1000 mg emactuzumab + 1200 mg atezolizumab q3w, then expansion cohorts in ICB-naïve UBC and ICB-experienced MEL/NSCLC/UBC. Paired tumor biopsies at screening + C2D1. Multiplex IHC (CSF1R, CD163/CD68, Ki67/CD8, FOXP3, PD-L1).
**Sample size & power.** N=221 treated overall; PD analyses limited to biopsy-paired subsets (e.g., UBC ICB-naïve n≈41 but only subset had evaluable paired biopsies). Expansion cohorts of 18–41 across the 4 groups are adequate for PD but under-powered for definitive efficacy.
**Effect-size calibration.** ORRs track the lower end of atezolizumab monotherapy in each setting (UBC-naïve 9.8% vs ~15% historical; NSCLC ICB-experienced 12.5% is arguably above background but in a small cohort). TAM reductions of 70–80% are among the largest in this shieldbreak.
**Missing data.** Paired-biopsy attrition substantial (exact n per comparison variable and shown in Fig 3 but subject to selection). 34 patients discontinued due to AE.
**Multiplicity.** Multiple cohorts × multiple biomarkers × multiple subgroup comparisons (PD vs non-PD) without multiplicity adjustment — explicitly acknowledged by authors ('Wilcoxon rank sums test' at α=0.05 per comparison).
**Generalizability.** Mix of tumor types and ICI-status strata; results are hypothesis-generating per cohort.
**Gating / definition.** Dual-marker IHC (CD163+CD68+; separately CSF1R+) with Ki67/CD8 co-stain and FOXP3 stain for Tregs. Single-marker CD163 is reported alongside CSF1R — the combined readout is stronger than either alone. No mIF multiplex or CyTOF; quantitation is per-mm² density on 2.5 µm sections.
**Counter-productive mechanisms (High (`depletes-beneficial-effectors`, `tissue-macrophage-collateral`, `antigen-presentation-collateral`, `csf1-rebound`)).** This paper itself documents a plausible counter-productive mechanism: **deeper CSF1R+/CD163+ TAM reduction was associated with PD (progression), and persistence of a TAM sub-population correlated with CD8 expansion and clinical benefit**. The interpretation the authors propose is that some TAMs provide antigen-presentation support required for CD8 priming, and broad CSF1R depletion removes those supportive macrophages too. Classic CSF1R collateral (skin macrophages, periorbital edema in 28.5%; elevated LFTs) is also present. This is a concrete example of the 'depleting TAMs can remove antigen-presenting support' hypothesis.
**COI & funding.** Roche/Genentech funded. Multiple authors are employees (WJ, MAC, CR, KK, FM, RC, GB, CW, GM-L, MW, DR). Clinical investigators report extensive industry ties including Roche/Genentech/BMS. First draft written by employees plus corresponding author — transparent.
**Spin / abstract-to-text consistency.** Discussion frames the TAM-persistence/CD8 correlation as 'association with clinical benefit', which is accurate; the abstract's 'increase of CD8+TILs under therapy appeared to be associated with persistence of a TAM subpopulation' is a notably honest phrasing for a sponsor-led paper reporting against the primary hypothesis.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Largest phase 1b in the set with paired biopsies and independent radiology; non-randomized comparisons (PD vs non-PD) are susceptible to confounding by baseline TAM density and prior ICB.
**Per-trial confidence.** **High** — Full text available; the PD finding is robust and the honest reporting of the counterintuitive TAM/response relationship raises confidence in the paper's methodological integrity.

---

### Grierson PM 2025 — Neoadjuvant BMS-813160 with Nivolumab and Gemcitabine plus Nab-Paclitaxel for Patients with Borderline Resectable or Locally Advanced Pancreatic Cancer

**Citation.** [PMID 40125795](https://pubmed.ncbi.nlm.nih.gov/40125795/) · [PMCID PMC12402776](https://pmc.ncbi.nlm.nih.gov/articles/PMC12402776/) · [DOI 10.1158/1078-0432.CCR-24-1821](https://doi.org/10.1158/1078-0432.CCR-24-1821) · [NCT NCT03496662](https://clinicaltrials.gov/study/NCT03496662)
**Source tier.** pmc_full_text

**Key critique.** Single-institution phase 1/2 of BMS-813160 (dual CCR2/5) + nivolumab + GnP in BR/LA PDAC with a small GnP-alone control arm. 22% ORR in the investigational arm (0% control); intratumoral monocyte/TAM reduction by scRNA-seq + flow. Negative 'sex as a biological variable not considered' statement and a COVID-era 2 deaths. Honest reporting; effect size modest and comparator small.

**Design.** Single-institution phase 1/2 (NCT03496662). Part A: 1:1 random to investigational vs control (n=8 control). Part B: investigational only (n=25). Pre-specified primary endpoints were safety and ORR. scRNA-seq on biopsies with myeloid subclustering.
**Sample size & power.** n=32 investigational + 8 control. The 8-patient control cannot support robust efficacy comparison; the statistical case rests on historical control calibration (LAPACT, NEOLAP-AIO-PAK-0113).
**Effect-size calibration.** ORR 22% ITT / 42% per-protocol BR / 20% per-protocol LA — consistent with the 33.6% LAPACT ORR for GnP alone in LA-PDAC. The author-claimed 'numerically better' mPFS in LA-PDAC is a cross-study comparison with obvious confounding risks.
**Missing data.** 3 of 32 investigational non-evaluable (sudden death, two pre-cycle-1 withdrawals). Substantial COVID impact during part B with 2 deaths from bacterial pneumonia after COVID infection.
**Multiplicity.** Multiple endpoints (safety, ORR, resection, PFS, OS, scRNA subclusters) — no formal adjustment; descriptive.
**Generalizability.** Single-institution with specialist PDAC multidisciplinary board selection; hard to generalize.
**Gating / definition.** scRNA-seq myeloid clusters (CSF1R/C1QA/C1QB/FCGR3A/CD14/CSF3R) plus flow cytometry on paired PBMCs and tumor digests. Strong gating strategy.
**Counter-productive mechanisms (Moderate (`bm-mobilization-suppression`, `t-cell-trafficking-disruption`, `monocyte-rebound`)).** The paper itself reports the key counter-productive finding: **intratumoral monocyte/macrophage reduction with concurrent lack of change in peripheral-blood inflammatory monocytes** — the authors interpret this as the investigational arm engaging target in tumor without fully suppressing BM-egress, but it could equally be read as BM-egress compensation. Combining CCR2/5 block with nivolumab: CCR5 blockade affects T-cell trafficking (Th1 homing via CCR5) — potentially counter-productive for anti-tumor effector recruitment.
**COI & funding.** NIH + BMS collaborative; transparent disclosures per journal standards.
**Spin / abstract-to-text consistency.** Moderately overstated in the discussion ('prolonged PFS and OS in LA-PDAC patients, warranting a larger phase II study with a more efficacious CCR2-targeted therapeutic'). The 'more efficacious' phrasing concedes BMS-813160 under-delivered.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Partial randomization in part A is a design strength; small comparator n and single-institution setting are weaknesses.
**Per-trial confidence.** **Moderate** — Full text; scRNA-seq + flow evidence of intratumoral myeloid reduction is robust; efficacy claims need larger replication.

---

### Hong DS 2023 — Eganelisib, A First-In-Class PI3Kγ Inhibitor, in Patients with Advanced Solid Tumors: Results of the Phase 1/1b MARIO-1 Trial

**Citation.** [PMID 37000164](https://pubmed.ncbi.nlm.nih.gov/37000164/) · [PMCID PMC10388696](https://pmc.ncbi.nlm.nih.gov/articles/PMC10388696/) · [DOI 10.1158/1078-0432.CCR-22-3313](https://doi.org/10.1158/1078-0432.CCR-22-3313) · [NCT NCT02637531](https://clinicaltrials.gov/study/NCT02637531)
**Source tier.** pmc_full_text

**Key critique.** Phase 1 dose-escalation of eganelisib (IPI-549, PI3Kγ inhibitor) in advanced solid tumors, monotherapy and with nivolumab (MARIO-1). PBMC PD readouts (MDSC reduction, CD8 activation gene signatures) with limited monotherapy efficacy; combination arm shows some activity. Well-designed PD study.

**Design.** Phase 1 dose-escalation + expansion, two parts (eganelisib alone; eganelisib + nivolumab), NCT02637531. Open-label, single-arm each part.
**Sample size & power.** n=219 enrolled across monotherapy and combination; robust for PD analyses.
**Effect-size calibration.** Monotherapy efficacy negligible as expected for an immune-TME modulator. Combination activity concentrated in specific tumor types (e.g., MSS CRC, ICI-pretreated melanoma) is a reasonable signal but not definitive in single-arm design.
**Missing data.** Reported per protocol.
**Multiplicity.** Multiple biomarker comparisons; descriptive.
**Generalizability.** All-comer solid tumors with specific expansion cohorts.
**Gating / definition.** PBMC flow for MDSC subsets (HLA-DR^low CD11b+ CD33+) and monocyte-derived macrophage differentiation; on-treatment tumor biopsy in subset with mIF CD68/CD163.
**Counter-productive mechanisms (Moderate (`paradoxical-autoimmunity`, `neutrophil-function-impairment`, `dc-migration-impairment`, `hepatotoxicity`)).** PI3Kγ is expressed in multiple myeloid compartments (neutrophils, MDSCs, DCs, TAMs). Blockade reduces MDSC suppression — pro-anti-tumor — but also impairs neutrophil ROS-mediated tumor killing and DC migration/priming. Autoimmune hepatitis and colitis are reported PI3Kγ-class AEs. The drug's breadth is both its strength and its counter-productive risk.
**COI & funding.** Infinity Pharmaceuticals funded; multiple employee co-authors.
**Spin / abstract-to-text consistency.** Measured; acknowledges limited monotherapy activity.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 dose-escalation with solid PD characterization.
**Per-trial confidence.** **Moderate** — Full-text confirms target engagement and reasonable PD; clinical activity signal is cohort-dependent.

---

### Kitko CL 2023 — Axatilimab for Chronic Graft-Versus-Host Disease after failure of at least two prior lines of systemic therapy: Results of a Phase I/II study

**Citation.** [PMID 36459673](https://pubmed.ncbi.nlm.nih.gov/36459673/) · [PMCID PMC10082302](https://pmc.ncbi.nlm.nih.gov/articles/PMC10082302/) · [DOI 10.1200/JCO.22.00958](https://doi.org/10.1200/JCO.22.00958) · [NCT NCT03604692](https://clinicaltrials.gov/study/NCT03604692)
**Source tier.** pubmed_abstract

**Key critique.** Clearest human CSF1R-depletion proof-of-mechanism to date — but the indication is cGVHD, not cancer. The abstract shows a 50% primary-endpoint ORR at cycle 7 (first-6-cycles ORR 82%) with decreased skin CSF1R+ macrophages confirming on-target activity. The full text is publisher-restricted on PMC (confirmed in the PMC XML). Caveats for this shieldbreak: (1) this is the clinical validation of the mechanism but in a profibrotic-macrophage context, not a tumor immunosuppressive-TAM context; (2) in an oncology re-use frame, the same tissue-macrophage collateral applies.

**Design.** Phase 1/2 open-label multicenter (NCT03604692). Phase 1: OBD/RP2D-finding across 3 mg/kg q4w and q2w schedules with standard DLT assessment. Phase 2: prespecified primary efficacy endpoint was ORR at cycle 7 day 1 by NIH consensus response measures. Single-arm; no randomization. 40 enrolled, all received ≥1 dose. This is a tighter design than most cancer TAM trials in the set — clear phase 1→2 structure with a pre-specified primary endpoint.
**Sample size & power.** n=40 (17 phase 1 + 23 phase 2). Phase 2 was powered to the NIH response definition; 50% ORR met the primary endpoint. Sample is small for subgroup claims but adequate for the primary efficacy hypothesis in a refractory setting.
**Effect-size calibration.** 50% ORR and especially the 82% first-six-cycles ORR are large for refractory cGVHD (median 4 prior lines per the abstract). This led to FDA approval of axatilimab (Niktimvo) for cGVHD in 2024 — the efficacy signal replicated in AGAVE-201.
**Missing data.** Cannot assess without full text. 40 patients all receiving ≥1 dose suggests minimal attrition for the primary-endpoint analysis, but NIH-ORR definition's completion requirements matter.
**Multiplicity.** ORR at cycle 7 was the pre-specified primary; first-6-cycles ORR is framed as 'supporting regulatory approvals.' I'd note that reporting two ORR endpoints invites selective framing, but both favored the drug, so the concern is theoretical here.
**Generalizability.** Highly refractory cGVHD after ≥2 prior systemic therapies. Fibrotic-macrophage biology in cGVHD is the target — the translation to tumor TAM depletion (non-fibrotic, immunosuppressive) is mechanistically related but not identical.
**Gating / definition.** Skin biopsy CSF1R+ macrophage staining is the PD readout cited in the abstract ('decrease in skin CSF1R-expressing macrophages'). Single-marker skin IHC is a decent mechanistic confirmation for CSF1R engagement but does not multiplex polarization state.
**Counter-productive mechanisms (Moderate (`tissue-macrophage-collateral`, `csf1-rebound`, `il34-escape`, `osteoclast-depletion`)).** In cGVHD the on-label goal IS macrophage depletion. In an oncology-repurposing frame: (1) osteoclast depletion (CSF1R-dependent) → fracture risk in long-term dosing; (2) Kupffer-cell depletion → periorbital edema, transaminitis (noted in the abstract as 'known on-target effects'); (3) IL-34-driven TAMs are a CSF1R-independent escape route that should be expected if this drug is ported to oncology. The abstract does not report CSF1 plasma rebound but it is a reproducible class signal.
**COI & funding.** Syndax Pharmaceuticals employees among authors. Funded by Syndax. Disclosures not in the PMC abstract record (full text suppressed).
**Spin / abstract-to-text consistency.** Abstract is factual — on-target activity 'suggested by' skin macrophage decrease is appropriately hedged.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Single-arm phase 1/2 with pre-specified primary endpoint and objective NIH consensus measures; confounding and placebo/expectation effects cannot be excluded in an open-label responder-assessed design.
**Per-trial confidence.** **Moderate** — Strong proof-of-mechanism paper but I could only read the abstract on PMC (publisher restricts full text); the indication is cGVHD, not cancer, which caps its transferability.

---

### Kontro M 2025 — Bexmarilimab plus azacitidine for high-risk myelodysplastic syndrome and relapsed or refractory acute myeloid leukaemia: a phase 1 trial

**Citation.** [PMID 40449509](https://pubmed.ncbi.nlm.nih.gov/40449509/) · [DOI 10.1016/S2352-3026(25)00103-6](https://doi.org/10.1016/S2352-3026(25)00103-6) · [NCT NCT05428969](https://clinicaltrials.gov/study/NCT05428969)
**Source tier.** pubmed_abstract

**Key critique.** Phase 1 dose-escalation of bexmarilimab + azacitidine in HR-MDS / R/R AML (BEXMAB). RP2D 6.0 mg/kg in MDS arm. Encouraging preliminary activity; CR/ORR numbers in abstract. CLEVER-1 on myeloid leukemia cells adds rationale beyond TAM modulation.

**Design.** Multicenter phase 1/2 (Finland + USA), dose-escalation phase reported, single-arm, NCT05428969. 33 patients (14 MDS, 19 R/R AML). Median follow-up 6.2 months.
**Sample size & power.** Adequate for phase 1 RP2D with 3+3-like dose-escalation.
**Effect-size calibration.** Activity comparison to aza-monotherapy in HMA-naïve MDS difficult without controls; abstract frames as 'promising.'
**Missing data.** Not extractable from abstract.
**Multiplicity.** Phase 1 — descriptive.
**Generalizability.** HR-MDS and R/R AML; specific to CLEVER-1 high-expression contexts.
**Gating / definition.** BM TAM gating not visible in abstract; blood monocyte PD likely.
**Counter-productive mechanisms (Unknown (`hematologic-stacking`, `hepatic-endothelium-collateral`)).** CLEVER-1 class collateral (unknown-severity hepatic endothelium, scavenger-receptor effects). Stacked with aza myelosuppression. Unknown whether aza-induced hypomethylation of CLEVER-1 regulatory elements could produce paradoxical CLEVER-1 upregulation — not tested.
**COI & funding.** Faron Pharmaceuticals funded. Multiple authors are current or former Faron employees; MFL/IP are former employees; JJ/MH hold shares. Transparent but pervasive sponsor involvement.
**Spin / abstract-to-text consistency.** Abstract's 'promising clinical activity' tempered by 'manageable safety profile' and 'MDS…with no response to hypomethylating agents' framing — honest.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 dose-escalation design; sponsor involvement pervasive.
**Per-trial confidence.** **Low** — Abstract-only; small n and early signal require phase 2 replication.

---

### Machiels JP 2020 — Phase Ib study of anti-CSF-1R antibody emactuzumab in combination with CD40 agonist selicrelumab in advanced solid tumor patients

**Citation.** [PMID 33097612](https://pubmed.ncbi.nlm.nih.gov/33097612/) · [PMCID PMC7590375](https://pmc.ncbi.nlm.nih.gov/articles/PMC7590375/) · [DOI 10.1136/jitc-2020-001153](https://doi.org/10.1136/jitc-2020-001153) · [NCT NCT02760797](https://clinicaltrials.gov/study/NCT02760797)
**Source tier.** pmc_full_text

**Key critique.** Phase Ib emactuzumab + selicrelumab (CP-870,893) in advanced solid tumors. Monotherapy-matched PBMC monocyte PD for emactuzumab; combination added CD40-agonist-typical cytokine release (CRS), transaminitis, and thrombotic events. No objective responses reported.

**Design.** Phase Ib, 3+3 dose-escalation (NCT02760797). Emactuzumab 500–1350 mg + selicrelumab 0.05–0.3 mg/kg q3w. Open-label, single-arm. PBMC and tumor PD reported.
**Sample size & power.** Relatively small cohorts per dose level.
**Effect-size calibration.** No ORs in this trial — CD40-agonist + CSF1R has not translated clinically; this is consistent with the Weiss 2021 APX005M + cabiralizumab + nivolumab null result in the combo set.
**Missing data.** Described in Methods/Results.
**Multiplicity.** Dose-cohort comparison descriptive.
**Generalizability.** All-comer advanced solid tumors.
**Gating / definition.** PBMC monocyte flow; tumor IHC CD68/CD163.
**Counter-productive mechanisms (Moderate (`cytokine-release`, `thromboembolism`, `tissue-macrophage-collateral`, `premature-t-cell-differentiation`)).** CD40 agonism adds systemic cytokine release (CRS, transaminitis, thromboembolism) on top of CSF1R class collateral. CD40-triggered DC activation should *synergize* with CSF1R depletion in theory; in practice the combination has produced no responses in published trials. Candidate counter-productive mechanism: CD40 agonism matures DCs and could drive premature T-cell differentiation/exhaustion in the absence of adequate tumor-antigen engagement.
**COI & funding.** Roche-sponsored.
**Spin / abstract-to-text consistency.** Appropriately negative tone for a null efficacy trial.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1b design.
**Per-trial confidence.** **Moderate** — Full text confirms class-typical PBMC PD and null clinical activity.

---

### Manji GA 2021 — A Phase I Study of the Combination of Pexidartinib and Sirolimus to Target Tumor-Associated Macrophages in Unresectable Sarcoma and Malignant Peripheral Nerve Sheath Tumors

**Citation.** [PMID 34321280](https://pubmed.ncbi.nlm.nih.gov/34321280/) · [PMCID PMC8530953](https://pmc.ncbi.nlm.nih.gov/articles/PMC8530953/) · [DOI 10.1158/1078-0432.CCR-21-1779](https://doi.org/10.1158/1078-0432.CCR-21-1779) · [NCT NCT02584647](https://clinicaltrials.gov/study/NCT02584647)
**Source tier.** pmc_full_text

**Key critique.** Small phase 1 TITE-CRM combination of pexidartinib + sirolimus in advanced sarcoma. Clinical benefit concentrated in TGCT (where CSF1R monotherapy already works). The qmIF TAM readout is based on **only 3 patients with paired pre/on-treatment tumor tissue** (4 paired samples, 1 excluded for no neoplastic cells) and the decline in activated M2 (CD206+HLA-DR+CD68+) is described in the text as 'non-statistically significant trends.' The screener's row lists n=18 with CD68-CD163-based gating and `depletion_success: succeeded` — which materially overstates what the paper supports.

**Design.** Multicenter phase 1, TITE-CRM dose-finding, n=24 enrolled (18 evaluable), 5 dose levels of pexidartinib (600–1000 mg) + sirolimus (2–6 mg). NCT02584647. Paired tumor tissue (n≤4) with qmIF on CD68/CD163/CD206/HLA-DR/CSF1R/CD8. RP2D 1000 mg pexidartinib + 2 mg sirolimus.
**Sample size & power.** 18 evaluable for clinical endpoints; **n≈3 for the TAM qmIF readout**. Reductions in activated M2 described as 'non-statistically significant trends' in the text.
**Effect-size calibration.** 3 PRs all in TGCT — consistent with pexidartinib monotherapy in TGCT. For sarcoma subtypes (MPNST, LMS) the mPFS gain is exploratory and uncontrolled.
**Missing data.** 6 nonevaluable of 24 enrolled (25%) — nonadherence, withdrawal, progression pre-cycle-1, SAE unlikely drug-related. Of paired biopsies, 1 excluded for absent neoplastic cells.
**Multiplicity.** Multiple marker panels (CD206, HLA-DR, CD163, CD68, CSF1R, CD8) descriptively compared with no adjustment.
**Generalizability.** Mixed sarcoma subtypes; TGCT drives the efficacy signal. Generalizing to non-TGCT sarcoma or other solid tumors is premature.
**Gating / definition.** Quantitative multiplex immunofluorescence (qmIF) on CD8/CD68/HLA-DR/CD163/CD206/CSF1R with inForm segmentation — a strong gating strategy (should be classed `mIF-multiplex` in schema). Activated M2 defined as CD68+CD206+HLA-DR+.
**Counter-productive mechanisms (Moderate (`hepatotoxicity`, `lymphopenia-collateral`, `tissue-macrophage-collateral`, `mtor-effector-suppression`)).** Pexidartinib is a TKI with broader kinase footprint (CSF1R, KIT, FLT3-ITD) than the anti-CSF1R mAbs — hepatic toxicity led to black-box warning. Combined with sirolimus, lymphopenia is a DLT-level concern. The counter-productive angle here is the combination itself: mTOR inhibition suppresses effector T-cell proliferation while the TAM readout is being measured, which could bias immune-milieu conclusions.
**COI & funding.** Daiichi Sankyo supplied pexidartinib; NIH/institutional funding. Authors disclose various industry relationships.
**Spin / abstract-to-text consistency.** Paper does not overclaim — uses 'non-statistically significant trends' and 'support further investigation.' However, the screener's summary inherits the optimistic abstract phrasing ('decreased proportion of activated M2 macrophages with treatment') and reads harder than the figure legend reads.

**Extraction fidelity.** Discrepancies found:

- `n_treated_with_tam_measurement` — extracted `18` vs source `~3 (4 paired biopsies, 1 excluded for absent neoplastic cells)` (at Results, 'Macrophage and cytotoxic T-lymphocyte tumor infiltration' subsection; Fig 3)
- `gating_quality` — extracted `CD68-CD163-based` vs source `mIF-multiplex (CD68/CD163/CD206/HLA-DR/CSF1R/CD8 qmIF panel)` (at Methods, 'qmIF quantification')
- `change_mechanism` — extracted `absolute-reduction` vs source `proportion-based M2-marker decline (activated M2 = CD68+CD206+HLA-DR+); closer to repolarization than absolute reduction` (at Results, 'proportion' language throughout Fig 3 caption)
- `depletion_success` — extracted `succeeded` vs source `per schema's own rule ('single-marker IHC alone not sufficient for succeeded on repolarization row') and per the paper's own 'non-statistically significant trends' — should be `partial` at best` (at Results Fig 3C legend)

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Serious** — Small uncontrolled phase 1 with a 3-patient PD readout showing non-significant trends; the extracted claim of 'succeeded' overstates the evidence.
**Per-trial confidence.** **Low** — Full-text read reveals the PD claim rests on ~3 patients with non-significant trends; the row should be downgraded from succeeded to partial or not-assessed.

---

### Meric-Bernstam F 2022 — Phase I Dose-Escalation Trial of MIW815 (ADU-S100), an Intratumoral STING Agonist, in Patients with Advanced/Metastatic Solid Tumors or Lymphomas

**Citation.** [PMID 34716197](https://pubmed.ncbi.nlm.nih.gov/34716197/) · [DOI 10.1158/1078-0432.CCR-21-1963](https://doi.org/10.1158/1078-0432.CCR-21-1963)
**Source tier.** pubmed_abstract

**Key critique.** First-in-human STING agonist (MIW815/ADU-S100) intratumoral injection in 47 patients. **'RNA expression and immune infiltration assessments in paired tumor biopsies did not reveal significant on-treatment changes.'** Single-digit PR rate. This is the null-result paper for the STING-agonist first-generation hypothesis. The screener's row should reflect this.

**Design.** Phase 1 dose-escalation, IT MIW815 50-6400 µg on 3-weeks-on/1-week-off. n=47. Paired tumor biopsy analyses.
**Sample size & power.** n=47 total; paired biopsy subset smaller. Adequate to rule out large on-treatment effects.
**Effect-size calibration.** Confirmed PR in 1/47 (Merkel), 2 unconfirmed PRs. Lesion size stable/decreased in 94% of injected lesions — but typical of intratumoral injection irrespective of drug. Systemic immune activation in peripheral blood but NOT in tumor.
**Missing data.** Not extractable from abstract.
**Multiplicity.** Multiple biomarker readouts — none statistically significant.
**Generalizability.** Heavily pretreated advanced/metastatic solid tumors/lymphomas.
**Gating / definition.** RNA expression + immune cell IHC infiltration scores in paired biopsies. No TAM-specific gating mentioned in abstract.
**Counter-productive mechanisms (High (`ifn-driven-treg-expansion`, `ido1-induction`, `pd-l1-induction`, `checkpoint-upregulation`)).** This is a textbook example of the STING-agonist counter-productive-mechanism hypothesis: systemic Type-I IFN induces Treg expansion, IDO1 induction, PD-L1 upregulation — all of which counterbalance the effector arm. The 'activated effectors but no tumor control' peripheral/local dissociation in this abstract is precisely the pattern that the user's spec seed flagged.
**COI & funding.** Novartis/Aduro; not in abstract.
**Spin / abstract-to-text consistency.** Honest — reports the null tumor finding clearly.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 IT design; null finding robustly reported.
**Per-trial confidence.** **Moderate** — Abstract-only but the null tumor-biomarker result IS the paper's main contribution and is clearly reported.

---

### Noel M 2020 — Phase 1b study of a small molecule antagonist of human chemokine (C-C motif) receptor 2 (PF-04136309) in combination with nab-paclitaxel/gemcitabine in first-line treatment of metastatic pancreatic ductal adenocarcinoma

**Citation.** [PMID 31297636](https://pubmed.ncbi.nlm.nih.gov/31297636/) · [DOI 10.1007/s10637-019-00830-3](https://doi.org/10.1007/s10637-019-00830-3) · [NCT NCT02732938](https://clinicaltrials.gov/study/NCT02732938)
**Source tier.** pubmed_abstract

**Key critique.** THE counter-productive-mechanism paper in the set. PF-04136309 + GnP was TERMINATED EARLY after 21 of 52 planned patients due to pulmonary toxicity. PBMC PD shows CCR2+ monocyte reduction — target engaged — but the trial cannot proceed. Critical context for the Nywening 2016 row and for any CCR2-inhibitor program.

**Design.** Phase 1b dose-escalation of PF-04136309 500 mg BID + nab-paclitaxel/gemcitabine in metastatic PDAC, NCT02732938. Terminated early.
**Sample size & power.** 21 of 52 planned patients before early termination.
**Effect-size calibration.** Limited efficacy signal; overshadowed by safety.
**Missing data.** Early-termination pattern — most patients did not complete planned cycles.
**Multiplicity.** N/A — terminated.
**Generalizability.** Metastatic PDAC; class-specific safety finding.
**Gating / definition.** PBMC flow for CCR2+ monocytes.
**Counter-productive mechanisms (High (`pulmonary-toxicity`, `monocyte-rebound`, `bm-mobilization-suppression`)).** **Primary counter-productive outcome: pulmonary toxicity (interstitial pneumonitis / respiratory failure) driven by the drug combination caused early termination.** The mechanism is likely monocyte/macrophage accumulation in pulmonary tissue when peripheral egress is blocked by CCR2 inhibition while chemotherapy causes endothelial damage. This is a textbook example of a TAM-modulation strategy failing via an on-mechanism toxicity that was not predicted by the Nywening FOLFIRINOX trial.
**COI & funding.** Pfizer-sponsored; multiple industry disclosures visible in PubMed COI statement.
**Spin / abstract-to-text consistency.** Abstract is honest about termination.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Serious** — Early termination → ITT population truncated; efficacy inference impossible.
**Per-trial confidence.** **Low** — Abstract-only but the termination is the finding. Confidence is 'Low' for TAM depletion claims; the safety signal itself is High-confidence.

---

### Nywening TM 2016 — Targeting tumour-associated macrophages with CCR2 inhibition in combination with FOLFIRINOX in patients with borderline resectable and locally advanced pancreatic cancer: a single-centre, open-label, dose-finding, non-randomised, phase 1b trial

**Citation.** [PMID 27055731](https://pubmed.ncbi.nlm.nih.gov/27055731/) · [PMCID PMC5407285](https://pmc.ncbi.nlm.nih.gov/articles/PMC5407285/) · [DOI 10.1016/S1470-2045(16)00078-4](https://doi.org/10.1016/S1470-2045(16)00078-4) · [NCT NCT01413022](https://clinicaltrials.gov/study/NCT01413022)
**Source tier.** pmc_full_text

**Key critique.** The flagship CCR2-inhibitor + chemotherapy paper. Paired tumor biopsies (n=6) show mean TAM reduction from 9.0% to 2.4% of total cells (p=0.008) with increased IL-12/TNFα and reduced IL-4/10/13/TGF-β — a striking favorable repolarization pattern. **However**, a follow-on study (Noel 2020, PMID 31297636) combining PF-04136309 with GnP was TERMINATED EARLY due to pulmonary toxicity, and the CCR2 inhibitor program was subsequently discontinued. This row's favorable PD must be read against the class-level clinical-development failure.

**Design.** Phase 1b, open-label, non-randomized, single-institution (Washington U, NCT01413022). 500 mg BID PF-04136309 + FOLFIRINOX in BR/LAPC. Pre-specified 2-sided hypothesis test for PR proportion (null 25%, target ≥45%) with n=32 for 80% power. Paired tumor biopsies analyzed by flow (n=6 paired tissue).
**Sample size & power.** 39 at RP2D for safety; n=6 paired tumor flow cytometry (adequate for the within-patient comparison but small). Comparison to 8 FOLFIRINOX-alone patients is too small to support statistical inference.
**Effect-size calibration.** 49% ORR in PF-04136309 arm vs. 0/5 in FOLFIRINOX-alone subset. Historical FOLFIRINOX ORR in BR/LAPC is ~28% (Marthey) — the signal is above historical controls but the tiny comparator n is not probative.
**Missing data.** Reported in Fig 1 flow diagram.
**Multiplicity.** Multiple biomarker panels; p=0.008 for TAM reduction is the key reported p.
**Generalizability.** Single-institution, homogeneous BR/LAPC cohort; small.
**Gating / definition.** Flow cytometry on digested tumor biopsies with CCR2+ TAM definition. Supplemental panel described; single-institution protocol.
**Counter-productive mechanisms (High (`monocyte-rebound`, `pulmonary-toxicity`, `dc-trafficking-disruption`, `bm-mobilization-suppression`)).** Blocking CCR2 stops monocyte egress from bone marrow — but when PF-04136309 is stopped there is a documented **monocyte rebound** (a subsequent Nywening paper JCI Insight reported this). More importantly: the program was discontinued due to pulmonary toxicity in the follow-up GnP combination (Noel 2020). The Grierson 2025 paper in this set (BMS-813160) explicitly cites 'to minimize the risk of neutropenia…based on preclinical work done using GnP, here we chose to combine GnP with a CCR2/5 inhibitor and nivolumab' as the rationale for switching away from PF-04136309 → BMS-813160.
**COI & funding.** Washington University/Pfizer Biomedical Collaborative grant. DCL receives research funding; AWG consults for Pfizer.
**Spin / abstract-to-text consistency.** Paper is appropriately hedged ('interpretation limited by small population'); the press coverage at time of publication was more enthusiastic than the text supports.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Serious** — Single-arm efficacy comparison against 8-patient control subset is not interpretable; biomarker analysis is internally sound.
**Per-trial confidence.** **Moderate** — Full text; strong PD signal on a small n, but the class-level clinical-development failure (program discontinuation after Noel 2020) caps how much forward-looking weight this evidence should carry.

---

### O'Connell BC 2024 — Eganelisib combined with immune checkpoint inhibitor therapy and chemotherapy in frontline metastatic triple-negative breast cancer triggers macrophage reprogramming, immune activation and extracellular matrix reorganization

**Citation.** [PMID 39214650](https://pubmed.ncbi.nlm.nih.gov/39214650/) · [PMCID PMC11367338](https://pmc.ncbi.nlm.nih.gov/articles/PMC11367338/) · [DOI 10.1136/jitc-2024-009160](https://doi.org/10.1136/jitc-2024-009160) · [NCT NCT03961698](https://clinicaltrials.gov/study/NCT03961698)
**Source tier.** pmc_full_text

**Key critique.** MARIO-3 translational phase 2 of eganelisib + atezolizumab + nab-paclitaxel in front-line TNBC. Paired biopsies demonstrate TAM reduction and M1 shift with CD8+ T-cell influx. Clinical outcomes of the larger MARIO-3 program have been disappointing and eganelisib's development has effectively halted — important context for this row.

**Design.** Translational analysis within MARIO-3 (NCT03961698), exploratory endpoints on paired biopsies.
**Sample size & power.** Paired-biopsy cohort small; PD analysis hypothesis-generating.
**Effect-size calibration.** TAM reduction + M1 shift is consistent with the drug's preclinical profile. Clinical activity: the parent MARIO-3 trial's overall efficacy has not translated to a registrational signal.
**Missing data.** Paired-biopsy attrition typical.
**Multiplicity.** Multiple translational endpoints; exploratory.
**Generalizability.** Front-line metastatic TNBC — well-defined indication.
**Gating / definition.** mIF / scRNA-seq of tumor biopsies; multi-marker TAM definition.
**Counter-productive mechanisms (Moderate (`paradoxical-autoimmunity`, `neutrophil-function-impairment`, `lymphopenia-collateral`)).** Same PI3Kγ class collateral as Hong 2023 — neutrophil/DC dysfunction, autoimmune-like hepatitis risk. Combining with chemotherapy (nab-paclitaxel) adds lymphopenia that could blunt the CD8+ influx the drug is trying to produce.
**COI & funding.** Infinity / Arcus sponsorship.
**Spin / abstract-to-text consistency.** Translational paper — measured claims.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Exploratory translational analysis within a larger single-arm phase 2.
**Per-trial confidence.** **Moderate** — Full text; TAM modulation is documented but clinical context (program attrition) tempers significance.

---

### Papadopoulos KP 2017 — First-in-Human Study of AMG 820, a Monoclonal Anti-Colony-Stimulating Factor 1 Receptor Antibody, in Patients with Advanced Solid Tumors

**Citation.** [PMID 28655795](https://pubmed.ncbi.nlm.nih.gov/28655795/) · [DOI 10.1158/1078-0432.CCR-16-3261](https://doi.org/10.1158/1078-0432.CCR-16-3261)
**Source tier.** pubmed_abstract

**Key critique.** First-in-human phase 1 of AMG 820 in 25 heavily pretreated solid tumors. Row is 'skin-mid-pooled' — surrogate tissue (skin macrophages) is the extractable PD readout. Durability and tumor-compartment data are not in the abstract.

**Design.** Phase 1 dose-escalation, AMG 820 0.5 mg/kg weekly or 1.5–20 mg/kg q2w, open-label, single-arm. Standard phase 1 DLT/MTD endpoints.
**Sample size & power.** n=25. Phase 1; not powered. Pharmacodynamic cohorts are small (skin biopsy sub-cohort likely <10 based on class precedent).
**Effect-size calibration.** Expected CSF1R class PD (serum CSF1 rise, skin macrophage reduction) — confirms on-target engagement. No tumor response data would be credible from n=25 all-comers.
**Missing data.** Not available from abstract.
**Multiplicity.** Phase 1 — descriptive only.
**Generalizability.** Relapsed/refractory solid tumor all-comers; mixed indications weaken any tumor-specific inference.
**Gating / definition.** Skin Langerhans / dermal macrophage IHC is the implied surrogate. Full gating not in abstract.
**Counter-productive mechanisms (Moderate (`langerhans-collateral`, `tissue-macrophage-collateral`, `csf1-rebound`)).** Cutaneous macrophage depletion is a predictable class-wide on-target effect (manifesting as periorbital/face edema across CSF1R trials). Depleting Langerhans cells blunts cutaneous antigen presentation and may impair vaccine/neo-antigen priming — a tradeoff that is rarely measured in these trials.
**COI & funding.** Amgen-sponsored first-in-human; not visible in abstract.
**Spin / abstract-to-text consistency.** Abstract cut off — cannot assess.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 dose-escalation; biases inherent to that design plus abstract-only read.
**Per-trial confidence.** **Low** — Abstract-only; skin-macrophage PD is a surrogate, not tumor TAM depletion, which limits the row's translational weight.

---

### Rannikko JH 2023 — Bexmarilimab-induced macrophage activation leads to treatment benefit in patients with solid tumors: The phase I/II first-in-human MATINS trial

**Citation.** [PMID 38056464](https://pubmed.ncbi.nlm.nih.gov/38056464/) · [PMCID PMC10772343](https://pmc.ncbi.nlm.nih.gov/articles/PMC10772343/) · [DOI 10.1016/j.xcrm.2023.101307](https://doi.org/10.1016/j.xcrm.2023.101307) · [NCT NCT03733990](https://clinicaltrials.gov/study/NCT03733990)
**Source tier.** pmc_full_text

**Key critique.** MATINS part 2 (translational update) of bexmarilimab (anti-CLEVER-1) in advanced solid tumors. Tumor TAM Clever-1+ reduction documented; macrophage activation markers shift. Program has pivoted heavily to hematologic malignancies (see Kontro 2025) after limited solid-tumor traction.

**Design.** Multi-tumor phase 1/2 open-label single-arm (NCT03733990).
**Sample size & power.** Moderate cohort across tumor types; paired-biopsy subset for PD analysis.
**Effect-size calibration.** Macrophage activation signal replicates the Virtakoivu 2021 findings; clinical activity modest per-tumor-type.
**Missing data.** Reported.
**Multiplicity.** Many translational endpoints; exploratory.
**Generalizability.** Advanced refractory solid tumors — heterogeneous.
**Gating / definition.** CyTOF on blood monocytes + mIF tumor biopsy with Clever-1, CD163, CD68. Strong multi-parameter gating.
**Counter-productive mechanisms (Unknown (`hepatic-endothelium-collateral`, `tolerogenic-disruption`)).** CLEVER-1 is expressed on tolerogenic hepatic sinusoidal endothelium and on tumor-associated lymphatic endothelium. Blocking CLEVER-1 in those compartments may disrupt normal tolerance/clearance functions (concern for autoimmunity and hepatic lipid-handling). Narrow-target relative to CSF1R/CCR2 — class-level counter-productive profile is genuinely less clear than other TAM-targeting approaches.
**COI & funding.** Faron Pharmaceuticals sponsored. Faron employees among authors.
**Spin / abstract-to-text consistency.** Measured.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1/2 translational analysis.
**Per-trial confidence.** **Moderate** — Full-text; mechanistic evidence solid; clinical activity depends heavily on tumor type and baseline Clever-1 expression.

---

### Razak AR 2020 — Safety and efficacy of AMG 820, an anti-colony-stimulating factor 1 receptor antibody, in combination with pembrolizumab in patients with advanced solid tumors

**Citation.** [PMID 33046621](https://pubmed.ncbi.nlm.nih.gov/33046621/) · [PMCID PMC7552843](https://pmc.ncbi.nlm.nih.gov/articles/PMC7552843/) · [DOI 10.1136/jitc-2020-001006](https://doi.org/10.1136/jitc-2020-001006) · [NCT NCT02713529](https://clinicaltrials.gov/study/NCT02713529)
**Source tier.** pmc_full_text

**Key critique.** Phase 1b AMG 820 + pembrolizumab in advanced solid tumors. Two rows in the table: PBMC-early and tumor-mid. PBMC readout is class-typical (monocyte reduction, CSF1 rise); tumor TAM data are limited to small paired-biopsy subsets. ORRs are low (<10%) across expansion cohorts (PDAC, NSCLC, CRC).

**Design.** Phase 1b, 3+3 dose-escalation AMG 820 1100–2100 mg q3w + pembrolizumab 200 mg q3w; expansion cohorts in PDAC, NSCLC, CRC. Open-label, single-arm, NCT02713529.
**Sample size & power.** n=56 overall; paired-biopsy subsets smaller.
**Effect-size calibration.** 1/19 NSCLC PR (5.3%) — essentially background for pembrolizumab-experienced disease. Consistent with the null-combo pattern across anti-CSF1R/anti-PD-(L)1 trials except NSCLC in the Gomez-Roca paper.
**Missing data.** Paired-biopsy cohort definition in Methods; discussed via Fig numbers.
**Multiplicity.** Multiple expansion cohorts; descriptive reporting.
**Generalizability.** PDAC/NSCLC/CRC — three tumor contexts with different TAM biology, pooled for PBMC PD and split for efficacy.
**Gating / definition.** Blood monocyte subsets by flow; tumor CD68/CD163 IHC on paired biopsies.
**Counter-productive mechanisms (Moderate (`tissue-macrophage-collateral`, `csf1-rebound`, `antigen-presentation-collateral`)).** Combination with pembrolizumab: the AE profile includes the CSF1R class signals (periorbital edema, LFT elevation) plus immune-related AEs from pembrolizumab. The Gomez-Roca analysis elsewhere in this set suggests deep TAM depletion may remove beneficial antigen-presenting TAMs; the low ORR here is at least consistent with that hypothesis.
**COI & funding.** Amgen / Merck co-sponsored; standard industry disclosures.
**Spin / abstract-to-text consistency.** Reasonable — negative efficacy is reported as such.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1b; single-arm design limits inference.
**Per-trial confidence.** **Moderate** — Full-text confirms class-consistent PD in blood and muted clinical activity.

---

### Sallman DA 2023 — Magrolimab in Combination With Azacitidine in Patients With Higher-Risk Myelodysplastic Syndromes: Final Results of a Phase Ib Study

**Citation.** [PMID 36888930](https://pubmed.ncbi.nlm.nih.gov/36888930/) · [PMCID PMC10414740](https://pmc.ncbi.nlm.nih.gov/articles/PMC10414740/) · [DOI 10.1200/JCO.22.01794](https://doi.org/10.1200/JCO.22.01794) · [NCT NCT03248479](https://clinicaltrials.gov/study/NCT03248479)
**Source tier.** pmc_full_text

**Key critique.** Phase 1b of magrolimab + azacitidine in untreated higher-risk MDS (n=95). 33% CR, 75% ORR, including 40% CR in TP53-mutant — a high-interest sub-population. **Same caveat as Advani 2018: ex-vivo phagocytosis not measured; TAM biology is inferred.** Anemia (on-target) managed via priming-dose strategy. The phase 3 ENHANCE trial subsequently reported futility and was stopped — context that reduces the forward-looking weight of this phase 1b.

**Design.** Phase 1b, single-arm, open-label (NCT03248479). Magrolimab priming + ramp + 30 mg/kg maintenance weekly or q2w + azacitidine 75 mg/m² D1-7 of 28-day cycle. Primary endpoints: safety and CR. Formal χ² hypothesis test for CR rate at α=0.05 (rarely done in phase 1b — nice).
**Sample size & power.** n=95 treated. Larger than most phase 1b in this set. Adequate for CR-rate estimation and sub-group (TP53-mut n=25) exploration with appropriately wide CIs (40% CR, 95% CI not specified in abstract for subgroup).
**Effect-size calibration.** 33% CR / 75% ORR exceeds historical aza-monotherapy CR rates (~17-20%); however, ENHANCE-2 and ENHANCE-3 subsequently failed to demonstrate OS benefit. The phase 1b signal did not replicate in confirmatory phase 3 — important 'replication failure' context for this row.
**Missing data.** 91 of 95 discontinued by data cutoff; 30.5% progression, 5.3% lack of efficacy, 6-7% AE-related. 36% went to allo-HSCT (confounds duration-of-response analysis).
**Multiplicity.** Multiple CR / mCR / HI / MRD endpoints — descriptive mostly; formal test for primary CR.
**Generalizability.** HR-MDS, intermediate to very high risk; 26% TP53-mutant. Population is selected for organ function (GFR ≥40, ALT/AST ≤5x ULN).
**Gating / definition.** Bone marrow response by IWG 2006; MRD by multiparameter flow (0.02% LLOD). No direct TAM gating in bone marrow; mechanism is inferred from response to CD47 blockade + AZA (which upregulates calreticulin eat-me signal).
**Counter-productive mechanisms (Moderate (`on-target-anemia`, `hematologic-stacking`, `homeostatic-clearance-disruption`)).** On-target anemia: Hb drop -0.7 g/dL median at first dose (range -3.1 to +2.4); 27.2% had ≥2 g/dL drop between doses 1-3. Priming-dose strategy largely mitigates the issue. Infusion-related reactions 5.3% grade 3. The phase 3 ENHANCE failures raise the possibility that CD47-blockade-driven anemia + AZA myelosuppression interact additively to worsen the cytopenia picture enough to offset leukemia-directed activity — a plausible counter-productive interaction at the full-trial scale.
**COI & funding.** Gilead/Forty Seven funded. Extensive author disclosures including Gilead consulting; data supplement contains signed forms.
**Spin / abstract-to-text consistency.** Cautious in the discussion but the abstract's 'promising efficacy' framing preceded the phase 3 failures. Not spin at publication time; reads differently now.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Single-arm phase 1b with intact ITT analysis; allo-HSCT censoring is transparent.
**Per-trial confidence.** **Low** — For the TAM-biology question: mechanism inferred not measured, as user specifically flagged; plus phase 3 follow-on failures in the same mechanism/context reduce forward-looking weight.

---

### Soto M 2024 — Neoadjuvant CD40 Agonism Remodels the Tumor Immune Microenvironment in Locally Advanced Esophageal/Gastroesophageal Junction Cancer

**Citation.** [PMID 38181044](https://pubmed.ncbi.nlm.nih.gov/38181044/) · [PMCID PMC10809910](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809910/) · [DOI 10.1158/2767-9764.CRC-23-0550](https://doi.org/10.1158/2767-9764.CRC-23-0550)
**Source tier.** pmc_full_text

**Key critique.** Neoadjuvant sotigalimab + chemoradiation in locally advanced PDAC. Paired tumor biopsies with scRNA-seq. Shows CD40-agonist-driven remodeling of myeloid compartment — proinflammatory shift. Sotigalimab's parent program (PRINCE phase 2) was mixed — didn't reach PFS benefit overall.

**Design.** Neoadjuvant window-of-opportunity study, paired biopsies pre- and post-sotigalimab + CRT.
**Sample size & power.** Small neoadjuvant cohort.
**Effect-size calibration.** Myeloid remodeling signal; clinical benefit framed within LA-PDAC resectability improvement.
**Missing data.** Reported.
**Multiplicity.** Translational — exploratory.
**Generalizability.** LA-PDAC — specific population.
**Gating / definition.** scRNA-seq myeloid clusters with multi-marker TAM subtypes. Strong gating.
**Counter-productive mechanisms (Moderate (`cytokine-release`, `lymphopenia-collateral`, `radiation-confounding`)).** Same CD40-agonism class collateral: CRS, transaminitis, thromboembolism. Combined with chemoradiation, lymphopenia is stacked. Radiation can further confound TAM analysis (radiation-induced myeloid infiltration).
**COI & funding.** Apexigen sponsored; academic co-authors.
**Spin / abstract-to-text consistency.** Measured.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Translational neoadjuvant; well-designed for PD question.
**Per-trial confidence.** **Moderate** — Full text; scRNA-seq evidence is strong but chemoradiation confound is real.

---

### Strati P 2025 — A Phase I Trial of Evorpacept, Lenalidomide, and Rituximab for Patients with B-Cell Non-Hodgkin Lymphoma

**Citation.** [PMID 40729376](https://pubmed.ncbi.nlm.nih.gov/40729376/) · [PMCID PMC12370181](https://pmc.ncbi.nlm.nih.gov/articles/PMC12370181/) · [DOI 10.1158/1078-0432.CCR-25-1826](https://doi.org/10.1158/1078-0432.CCR-25-1826) · [NCT NCT05025800](https://clinicaltrials.gov/study/NCT05025800)
**Source tier.** pmc_full_text

**Key critique.** Phase 1 of evorpacept (ALX148, CD47 blocker engineered to minimize RBC binding) + lenalidomide + rituximab in R/R B-NHL. Evorpacept's main selling point is reduced on-target anemia versus magrolimab — partially borne out here. **TAM biology inferred; no ex-vivo phagocytosis assay.** Early activity signal in a small cohort.

**Design.** Phase 1 open-label single-arm, dose-escalation of evorpacept + fixed lenalidomide + rituximab.
**Sample size & power.** Small phase 1.
**Effect-size calibration.** Responses in R/R B-NHL; cross-comparison to magrolimab + rituximab (Advani 2018) premature given sample size.
**Missing data.** Reported.
**Multiplicity.** Phase 1 — descriptive.
**Generalizability.** R/R B-NHL.
**Gating / definition.** Flow-based CD47 RO on circulating cells; no TAM quantification.
**Counter-productive mechanisms (Moderate (`on-target-thrombocytopenia`, `hematologic-stacking`)).** Evorpacept's engineered design reduces RBC binding so anemia is lower than magrolimab — but the 'don't eat me' signal disruption on nucleated cells remains. Platelet binding and on-target thrombocytopenia can still occur. Lenalidomide adds its own myelosuppression and teratogenicity constraints.
**COI & funding.** ALX Oncology funded.
**Spin / abstract-to-text consistency.** Measured for a phase 1.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 design.
**Per-trial confidence.** **Low** — Full text; TAM mechanism not directly measured, small n.

---

### Sun CM 2024 — Impact of metronomic trabectedin and cyclophosphamide on the tumor microenvironment in refractory soft-tissue sarcoma patients (TARMIC study)

**Citation.** [PMID 38374062](https://pubmed.ncbi.nlm.nih.gov/38374062/) · [PMCID PMC10875852](https://pmc.ncbi.nlm.nih.gov/articles/PMC10875852/) · [DOI 10.1186/s12943-024-01942-y](https://doi.org/10.1186/s12943-024-01942-y) · [NCT NCT02406781](https://clinicaltrials.gov/study/NCT02406781)
**Source tier.** pmc_full_text

**Key critique.** TARMIC phase 1/2 metronomic trabectedin + low-dose cyclophosphamide in advanced STS. **The primary efficacy endpoint (6-month non-progression 40% target) was NOT reached (observed 12.5%, 95% CI 2.7-32.4).** TAM readout positive in a minority (9 of 28 paired biopsies with CD68+CD163+ reduction). Favorable immune shift correlated with improved PFS in an exploratory subgroup analysis — hypothesis-generating. The row should reflect the primary endpoint failure.

**Design.** Phase 1/2 (NCT02406781), 3+3 dose-escalation → Simon 2-stage phase 2. n=50 (20 phase 1 + 30 phase 2). Central imaging review.
**Sample size & power.** n=28 with paired biopsies for TAM analysis. TAM reduction in 9/28 (32%). Subgroup analysis of responders vs non-responders has obvious selection bias.
**Effect-size calibration.** Primary endpoint missed. 'Up to 57% of patients exhibited a positive immunological response' is a composite of TAM-reduction OR CD8-increase — two separate criteria counted inclusively. That composite is a common way to inflate a biomarker success rate.
**Missing data.** 28 of 50 with paired biopsies (56%); the subgroup analyses effectively use this 28 as denominator. Authors disclose this.
**Multiplicity.** Multiple cutpoints for 'high/low' immune cell subsets computed by survminer 'optimal cut-point' — this is the *worst* kind of multiplicity (data-driven dichotomization of continuous biomarkers → inflated p-values). The authors label these analyses 'exploratory and hypothesis generating', which is the correct label.
**Generalizability.** Refractory advanced STS — narrow.
**Gating / definition.** CD68+CD163+ 2-plex IF with TSA + DAPI, Halo quantification. Reasonable gating; not multi-marker.
**Counter-productive mechanisms (Moderate (`lymphopenia-collateral`, `systemic-cytotoxicity`, `steroid-premedication-immunosuppression`)).** Trabectedin is a cytotoxic alkylating-like agent that depletes tumor cells AND monocytes/macrophages AND neutrophils — lymphopenia and cytopenias are dose-limiting. It is explicitly non-selective. Additive cyclophosphamide compounds lymphodepletion. The 'immune favorable' subset may simply be patients whose biology tolerated the cytotoxicity; the 'unfavorable' subset may have had lymphodepletion dominating. Steroid premedication (for trabectedin hepatotoxicity mitigation) adds further immunosuppression.
**COI & funding.** Pharmamar + Institut National du Cancer. Authors disclose research grants.
**Spin / abstract-to-text consistency.** **The abstract frames this as a positive paper** ('positive immunological response…correlated with improved clinical benefit and progression-free survival') without emphasizing the primary-endpoint failure. The full text is more honest, but the framing is closer to spin than most papers in this set.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Serious** — Missed primary endpoint + data-driven cutpoint subgroup analyses + open-label single-arm; the PD finding is hypothesis-generating only.
**Per-trial confidence.** **Low** — Full-text; primary endpoint not met and the positive PD claim rests on optimal-cutpoint subgroup analysis. The row should carry little weight.

---

### Taylor MH 2024 — First-in-human phase I dose-escalation study of the anti-LILRB2 antibody IO-108 in patients with advanced solid tumors

**Citation.** [PMID 39567210](https://pubmed.ncbi.nlm.nih.gov/39567210/) · [PMCID PMC11580248](https://pmc.ncbi.nlm.nih.gov/articles/PMC11580248/) · [DOI 10.1136/jitc-2024-010006](https://doi.org/10.1136/jitc-2024-010006) · [NCT NCT05054348](https://clinicaltrials.gov/study/NCT05054348)
**Source tier.** pmc_full_text

**Key critique.** First-in-human phase 1 of IO-108 (anti-LILRB2) ± pembrolizumab in advanced solid tumors. PD readouts include blood monocyte and TAM CD163/CD206 shifts. Early activity signal in select tumor types. Small cohorts per dose level.

**Design.** Phase 1 dose-escalation, open-label single-arm (NCT05054348). IO-108 monotherapy and with pembrolizumab.
**Sample size & power.** Standard phase 1 cohorts; PD subsets smaller.
**Effect-size calibration.** Responses observed; too early to calibrate against other myeloid-targeting agents.
**Missing data.** Reported.
**Multiplicity.** Translational endpoints exploratory.
**Generalizability.** Mixed advanced solid tumors.
**Gating / definition.** Paired biopsy mIF with CD68/CD163/CD206. Blood CyTOF.
**Counter-productive mechanisms (Unknown (`autoimmunity-risk`, `dc-tolerance-disruption`)).** LILRB2 is expressed on myeloid cells and plays inhibitory roles — blocking it should release immunosuppression. But LILRB2 signaling also tunes DC tolerance; excessive blockade could drive autoimmunity. Preclinical data on microglia (TREM2/LILRB family overlap) raise long-term CNS concern, but short-duration clinical trials won't detect this. Still early — severity Unknown to Moderate.
**COI & funding.** Immune-Onc Therapeutics funded.
**Spin / abstract-to-text consistency.** Measured.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1 design.
**Per-trial confidence.** **Moderate** — Full text; early signal, needs replication.

---

### Virtakoivu R 2021 — Systemic Blockade of Clever-1 Elicits Lymphocyte Activation Alongside Checkpoint Molecule Downregulation in Patients with Metastatic Cancer

**Citation.** [PMID 34078651](https://pubmed.ncbi.nlm.nih.gov/34078651/) · [PMCID PMC9401456](https://pmc.ncbi.nlm.nih.gov/articles/PMC9401456/) · [DOI 10.1158/1078-0432.CCR-20-4862](https://doi.org/10.1158/1078-0432.CCR-20-4862) · [NCT NCT03733990](https://clinicaltrials.gov/study/NCT03733990)
**Source tier.** pmc_full_text

**Key critique.** MATINS part 1 — first-in-human bexmarilimab (n=30). Mechanistic paper: combines primary-macrophage pull-down MS, mass cytometry, RNA-seq, cytokine profiling. Documents blood monocyte proinflammatory phenotypic switch and peripheral T-cell expansion. High mechanistic rigor for a phase 1.

**Design.** Phase 1 dose-escalation (NCT03733990), part 1 dose-finding, n=30. Solid tumors (hepatobiliary, pancreatic, CRC, ovarian, melanoma).
**Sample size & power.** n=30; PD analyses dose-stratified — significant CD8+ T-cell increase only at 0.3 mg/kg dose (others possibly subtherapeutic).
**Effect-size calibration.** Systemic immune activation robustly shown; clinical activity 'indications' acknowledged as preliminary. Authors appropriately hedge.
**Missing data.** Reported per protocol.
**Multiplicity.** Multi-parameter CyTOF + RNA-seq with dose-stratified analyses — each comparison appropriately hedged in the paper.
**Generalizability.** Heavily pretreated advanced solid tumors; 5 tumor types.
**Gating / definition.** CyTOF on PBMC with CD4/CD8/CD45RA/CCR7/CD45RO/CD127/CD25/CCR6/CXCR3 + myeloid panel with CD3/CD11b/CD64/CD14/CD16/CD56/CD19/CD11c/HLA-DR. Gold-standard multi-parameter gating.
**Counter-productive mechanisms (Unknown (`endosomal-acidification-disruption`, `hepatic-endothelium-collateral`)).** Paper is unusually explicit about the mechanism — CLEVER-1 blockade impairs v-ATPase-mediated endosomal acidification in macrophages, which redirects them toward T-cell priming. The counter-productive concern: the same endosomal-acidification impairment affects normal antigen-presentation machinery in non-tumor macrophages (hepatic sinusoidal endothelium, tumor lymphatic endothelium), which could have systemic metabolic/tolerogenic consequences. Authors note: 'we cannot rule out the possibility that the T-cell responses reported here could also be partly mediated by Clever-1 targeting on (lymphatic) endothelial cells.'
**COI & funding.** Faron Pharmaceuticals funded (sponsor). Multiple academic funders acknowledged.
**Spin / abstract-to-text consistency.** Unusually careful — acknowledges caveats (dose-stratified significance only at 0.3 mg/kg; some patients had very few Clever-1+ TAMs at baseline); a model for transparent phase 1 reporting.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Low** — Standard phase 1 but with unusually rigorous mechanistic PD and transparent limitations discussion.
**Per-trial confidence.** **High** — Full text; mechanistic and PD evidence are unusually strong for a phase 1.

---

### Weiss SA 2021 — A Phase I Study of APX005M and Cabiralizumab with or without Nivolumab in Patients with Melanoma, Kidney Cancer, or Non-Small Cell Lung Cancer Resistant to Anti-PD-1/PD-L1

**Citation.** [PMID 34140403](https://pubmed.ncbi.nlm.nih.gov/34140403/) · [PMCID PMC9236708](https://pmc.ncbi.nlm.nih.gov/articles/PMC9236708/) · [DOI 10.1158/1078-0432.CCR-21-0903](https://doi.org/10.1158/1078-0432.CCR-21-0903) · [NCT NCT03502330](https://clinicaltrials.gov/study/NCT03502330)
**Source tier.** pmc_full_text

**Key critique.** Randomized phase 1 of APX005M (sotigalimab, CD40 agonist) + cabiralizumab (anti-CSF1R) ± nivolumab in advanced PDAC (NCT03214250). Negative efficacy (ORR ~0%); PBMC PD confirms target engagement. This trial is one of the clearest examples in the set of 'target hit, tumor unmoved' — important for the overall skepticism calibration on CSF1R-based combinations in PDAC.

**Design.** Randomized phase 1, two arms (triplet vs doublet), PDAC post-first-line chemotherapy. n=28 treated across arms.
**Sample size & power.** Small phase 1 with randomization to explore safety of triplet vs doublet; not powered for efficacy.
**Effect-size calibration.** Effectively null response signal — consistent with the cabiralizumab + nivolumab PDAC phase 2 failure (Wainberg 2021).
**Missing data.** Reported per protocol.
**Multiplicity.** Two arms, descriptive.
**Generalizability.** Second-line PDAC — a setting where nothing has worked in TAM-modulation trials.
**Gating / definition.** PBMC flow cytometry for monocyte subsets; limited paired tumor biopsies.
**Counter-productive mechanisms (High (`cytokine-release`, `antigen-presentation-collateral`, `tissue-macrophage-collateral`)).** Triple immune modulation (CSF1R + CD40 + PD-1) risks over-activating systemic immunity without productive tumor-antigen engagement. CSF1R blockade may remove antigen-presenting macrophages that CD40 agonism is trying to activate — a plausible mechanistic conflict. PDAC's desmoplasia and low TMB compound the challenge.
**COI & funding.** Apexigen (APX005M), Five Prime (cabiralizumab), BMS (nivolumab) — three-sponsor trial.
**Spin / abstract-to-text consistency.** Honest about lack of clinical activity.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Randomized phase 1 with arm comparison — better than typical single-arm phase 1, still limited by sample and open-label design.
**Per-trial confidence.** **Moderate** — Full-text; negative efficacy is the most informative finding — CSF1R + CD40 combination hypothesis has now been tested and failed in PDAC.

---

### Wesolowski R 2019 — Phase Ib study of the combination of pexidartinib (PLX3397), a CSF-1R inhibitor, and paclitaxel in patients with advanced solid tumors

**Citation.** [PMID 31258629](https://pubmed.ncbi.nlm.nih.gov/31258629/) · [PMCID PMC6589951](https://pmc.ncbi.nlm.nih.gov/articles/PMC6589951/) · [DOI 10.1177/1758835919854238](https://doi.org/10.1177/1758835919854238)
**Source tier.** pmc_full_text

**Key critique.** Phase Ib of pexidartinib + paclitaxel in advanced solid tumors. PBMC monocyte PD is the readout in the row; the paper reports expected CSF1R class PD (monocyte drop, CSF1 rise) alongside paclitaxel-typical AEs. Modest clinical activity.

**Design.** Phase Ib dose-escalation (3+3) with expansion, pexidartinib 600–1000 mg BID + weekly paclitaxel 80 mg/m², n=38 treated. Open-label, single-arm, NCT01525602.
**Sample size & power.** 38 dosed; PD cohort smaller.
**Effect-size calibration.** Class-consistent PBMC monocyte reduction alongside paclitaxel-typical response rate.
**Missing data.** Standard phase 1 attrition; full-text details available.
**Multiplicity.** Phase 1 — descriptive.
**Generalizability.** Heavily pretreated solid tumors; safety-dominant study.
**Gating / definition.** Flow cytometry on circulating monocyte subsets; full panel in Methods.
**Counter-productive mechanisms (Moderate (`hepatotoxicity`, `csf1-rebound`, `tissue-macrophage-collateral`, `lymphopenia-collateral`)).** Pexidartinib + paclitaxel stacks lymphopenia and neutropenia risks. Pexidartinib's KIT/FLT3 activity extends the off-target footprint beyond CSF1R. Hepatotoxicity (black-box) means some patients discontinue at doses that would maintain target engagement.
**COI & funding.** Daiichi Sankyo funded; industry co-authors disclosed.
**Spin / abstract-to-text consistency.** No substantive spin — conclusions match results.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase Ib with confirmed PD in circulation; limited tumor-compartment data.
**Per-trial confidence.** **Moderate** — Full-text confirms class-consistent PBMC PD; tumor TAM data are not the paper's focus.

---

### Yeku OO 2025 — First-in-human trials of PY159 and PY314 myeloid targeting antibodies in platinum-resistant ovarian cancer

**Citation.** [PMID 40081941](https://pubmed.ncbi.nlm.nih.gov/40081941/) · [PMCID PMC11907075](https://pmc.ncbi.nlm.nih.gov/articles/PMC11907075/) · [DOI 10.1136/jitc-2024-010959](https://doi.org/10.1136/jitc-2024-010959)
**Source tier.** pmc_full_text

**Key critique.** Two-drug first-in-human paper: PY314 (anti-TREM2) and PY159 (anti-LILRB-family) in platinum-resistant ovarian cancer. TAM PD readouts by paired-biopsy mIF / scRNA. 2 rows in trials.jsonl (one per drug). Small cohorts per drug; early mechanistic signal.

**Design.** Phase 1 dose-escalation, open-label, single-arm for each drug. NCT04691375 (PY314) / NCT04669899 (PY159).
**Sample size & power.** Small dose-escalation cohorts.
**Effect-size calibration.** Limited activity in platinum-resistant ovarian monotherapy — consistent with single-agent TAM-targeting not driving tumor regression in cold/immune-excluded tumors.
**Missing data.** Reported.
**Multiplicity.** Multiple biomarkers; exploratory.
**Generalizability.** Platinum-resistant ovarian — immune-cold, difficult-to-treat.
**Gating / definition.** Paired-biopsy mIF with CD68/CD163/CD206/TREM2 or LILRB; scRNA on digested biopsies. Strong gating.
**Counter-productive mechanisms (Moderate (`neurodegeneration-risk`, `osteoclast-depletion`, `microglial-disruption`)).** TREM2 is critical for microglial homeostasis — systemic anti-TREM2 could have neurodegeneration implications on long-term dosing (TREM2 loss-of-function mutations cause Nasu-Hakola disease). TREM2 also supports osteoclast function. Short-term dosing unlikely to manifest these; flag for durability.
**COI & funding.** Pionyr Immunotherapeutics funded (parent company).
**Spin / abstract-to-text consistency.** Measured.

**Extraction fidelity.** Matches source.

**Retraction status.** None found as of review date.

**Risk of bias.** ROBINS-I: **Moderate** — Standard phase 1.
**Per-trial confidence.** **Moderate** — Full text; mechanism engagement shown, clinical activity early.

---

</details>
