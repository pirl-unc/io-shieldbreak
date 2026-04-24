*Scope summary for tumor-associated macrophage depletion, inhibition, or repolarization. Last updated 2026-04-23 from 37 trial rows (35 unique PMIDs; skeptic-critiqued: 35/35, 100%). Evidence-synthesis aid for research planning — not clinical guidance.*

## Target effect

The shieldbreak's target effect is **durable human tumor-compartment TAM modulation**, captured orthogonally via intent (`intervention_class`) and observation (`change_mechanism` — absolute reduction, ratio shift, repolarization, or functional impairment). Success is agent-specific: count reduction for CSF1R-style depleters; multi-marker M1-direction shift for repolarizing agents; assay-level functional change for "don't-eat-me" blockers. CPI monotherapy and healthy-volunteer PD are out-of-scope.

## Cross-cutting caveat (read first)

**No TAM-targeting intervention class in this evidence base is free of a structural counter-productive concern.** The skeptic's appraisal across 35 papers returned zero at Low CP severity (distribution: 6 High / 25 Moderate / 4 Unknown / 0 Low). Three findings motivate this framing: (1) the single largest and most rigorously-critiqued trial in the whole set — **Gomez-Roca 2022 (PMID 35577503, n=221)** — paper-internally reports that depth of TAM depletion is *inversely* associated with CD8 infiltration and clinical benefit; (2) CCR2/CCR5 development has effectively program-failed, with Noel 2020 terminated for pulmonary toxicity and Grierson 2025's discussion openly conceding underperformance; (3) CD47/SIRPα's solid-tumor TAM-modulation evidence is absent — the 4 included papers are all hematologic and all `functional-impairment-only` inferred from receptor occupancy, not ex-vivo phagocytosis. Rankings below are calibrated to this.

## Intervention grouping

- **CSF1R pathway (mAb + TKI)** — 13 unique PMIDs, 14 rows: Cassier 2020 (33161240), Gomez-Roca 2022 (35577503), Kitko 2023 (36459673, cGVHD), Papadopoulos 2017 (28655795), Autio 2020 (32847933), Dowlati 2021 (33624233), Falchook 2021 (33852104), Razak 2020 (33046621), Wesolowski 2019 (31258629), Manji 2021 (34321280), Machiels 2020 (33097612), Weiss 2021 (34140403), Boal 2020 (32943455).
- **CD40 agonism** — 3 PMIDs, 3 rows: Byrne 2021 (34112709, selicrelumab neoadjuvant PDAC), Soto 2024 (38181044, sotigalimab neoadj EAC), Coveler 2023 (37385724, SEA-CD40).
- **CD47 / SIRPα blockade** — 4 PMIDs, 4 rows: Advani 2018 (30380386, NEJM DLBCL/FL), Sallman 2023 (36888930, MDS), Daver 2025 (40198272, AML), Strati 2025 (40729376, evorpacept B-NHL).
- **CCR2 / CCR5 blockade** — 3 PMIDs, 3 rows: Nywening 2016 (27055731), Noel 2020 (31297636, terminated), Grierson 2025 (40125795, BMS-813160).
- **CLEVER-1 blockade (bexmarilimab)** — 3 PMIDs, 3 rows: Virtakoivu 2021 (34078651, MATINS-1), Rannikko 2023 (38056464, MATINS-2), Kontro 2025 (40449509, BEXMAB).
- **LILRB2 / TREM2 blockade** — 3 PMIDs, 4 rows: Taylor 2024 (39567210, IO-108), Yeku 2025 (40081941, PY314 + PY159 split arms), Beckermann 2024 (38372949, PY314 + pembro).
- **PI3Kγ inhibition (eganelisib)** — 2 PMIDs, 2 rows: Hong 2023 (37000164, MARIO-1), O'Connell 2024 (39214650, MARIO-3).
- **Trabectedin / lurbinectedin** — 2 PMIDs, 2 rows: Germano 2013 (23410977), Sun 2024 (38374062, TARMIC — primary endpoint missed).
- **STING agonism (ADU-S100)** — 1 PMID, 1 row: Meric-Bernstam 2022 (34716197).
- **TLR4 agonism (G100)** — 1 PMID, 1 row: Bhatia 2019 (30093453).

CSF1R-in-combo papers are rolled up into the CSF1R group rather than left in a generic `combo` class because pharmacology is what matters for research-planning ranking.

## Top interventions

### 1. CSF1R pathway (mAb and small-molecule inhibitors) — largest and most reproducible depletion signal; but with a paper-internal counter-productive finding that tempers the rank

**Evidence base.** 13 unique trials (phase 1–1b; mono and combo; total n treated with TAM readout ≈ 748). Agents: emactuzumab, cabiralizumab, AMG 820, LY3022855/IMC-CS4, axatilimab, pexidartinib. Absolute-reduction is the dominant observed mechanism (10/13 trials report `absolute-reduction` or `succeeded` depletion). Skeptic confidence distribution: 1 High, 6 Moderate, 6 Low; RoB 11 Moderate / 2 Serious; CP-severity 11 Moderate / 2 High. Tumor-compartment evidence is strongest for emactuzumab — Cassier 2020 (PMID 33161240) documents durable CSF1R+/CD163+ depletion with 71% ORR in dTGCT (a macrophage-driven tumor), and Gomez-Roca 2022 (PMID 35577503, n=221) reports median −80% CSF1R+ and −63% CD163+ in paired tumor biopsies. Axatilimab (Kitko 2023, PMID 36459673) is an FDA-approved proof-of-mechanism, but in cGVHD, not cancer.

**Likelihood of desired effect.** High for the PD endpoint itself — multiple independently-sponsored trials in different indications reproduce tumor and PBMC macrophage depletion on treatment. Much lower for clinical benefit outside macrophage-driven tumors: among the solid-tumor combo trials (Autio 2020, Dowlati 2021, Papadopoulos 2017, Razak 2020, Falchook 2021), objective responses are uncommon and Razak 2020 was specifically called "insufficient for further evaluation." Gomez-Roca 2022 reports the critical disconnect paper-internally: **deeper CSF1R+/CD163+ reduction was associated with progressive disease, and persistence of a TAM subpopulation tracked with CD8 infiltration and benefit.** This is the single most consequential finding for ranking in the whole evidence base.

**Toxicity profile.** Class signature is on-target tissue-macrophage collateral: periorbital edema (Langerhans-cell depletion), transaminitis (Kupffer-cell depletion), CK/LDH elevations (myocyte-associated macrophage involvement), and a compensatory serum CSF1 rise documented across essentially every trial (Cassier 2020, Autio 2020, Papadopoulos 2017, Gomez-Roca 2022). Pexidartinib adds a hepatic black-box warning and a broader kinase footprint (KIT, FLT3-ITD). Long-term osteoclast depletion carries fracture risk; in pediatric dosing (Boal 2020, PMID 32943455), growth-plate concerns are acknowledged but not directly measured. Sources: trial-internal AE tables; FDA axatilimab label (Niktimvo, Aug 2024); pexidartinib label (Turalio, 2019).

**Counter-productive mechanisms.** CP severity aggregate: **High**, replicated across the set. Three concerns drive the rating. (i) **Depletion depth is inversely correlated with clinical benefit** — Gomez-Roca 2022 paper-internally shows that in their n=221 dataset, patients with deeper CSF1R+/CD163+ reduction had *worse* outcomes, and persistence of a residual TAM subpopulation tracked with CD8 infiltration. The skeptic rated this paper High confidence — it is the most-rigorously-evidenced paper in the set and the finding directly contradicts depletion-as-goal. (ii) **Tissue-macrophage collateral is on-mechanism, not idiosyncratic** — osteoclasts, Kupffer cells, Langerhans cells, and splenic red-pulp macrophages all depend on CSF1R signaling; their depletion is the cause of the class AE signature, not a side-effect. (iii) **IL-34-driven escape** — CSF1R has two ligands (CSF1 and IL-34); receptor blockade alone cannot address IL-34-dominant suppressive TAM subsets, which may survive or expand during treatment. Partial depletion with a specific subset target appears to be a better PD endpoint than maximal depletion.

**Practical considerations.** Multiple agents are clinically available (pexidartinib, axatilimab approved; emactuzumab, LY3022855, AMG 820 developmental). ADA immunogenicity is a cross-agent concern that the Falchook 2021 / Gomez-Roca 2022 discussions both raise (LY3022855 reported ~3× the ADA rate of emactuzumab). IL-34-driven escape (dual CSF1R-ligand biology) is class-wide and cannot be overcome by receptor blockade alone. For combo design, the Gomez-Roca finding argues for *partial* rather than maximal depletion as the target PD endpoint.

**Why this rank.** Largest reproducible PD signal across the shieldbreak, but the Gomez-Roca inverse-correlation finding — skeptic-High-confidence, n=221, the paper most deserving of weight in the set — reframes maximal depletion as potentially counter-productive and forces a High CP-severity call at the class level. Rank 1 reflects evidence-base size and mechanism clarity, not an endorsement of deeper-is-better.

### 2. CD40 agonism — mechanistically distinct (activation, not depletion); small dataset, consistent repolarization, mixed clinical signal

**Evidence base.** 3 monotherapy/near-mono trials + 2 combinations with CSF1R blockade (Machiels 2020, Weiss 2021, counted under the CSF1R group). Agents: selicrelumab (CP-870,893), sotigalimab (APX005M), SEA-CD40. All 3 standalone trials skeptic-Moderate confidence, CP-Moderate, RoB-Moderate. Total n ≈ 89 across the 3 mono papers. Byrne 2021 (PMID 34112709) — neoadjuvant selicrelumab in resectable PDAC — is the clearest "repolarization without depletion" row in the set. Soto 2024 (PMID 38181044) documents scRNA-seq myeloid-compartment shift in neoadjuvant EAC with a 38% pCR rate.

**Likelihood of desired effect.** Moderate for repolarization (succeeded/partial in all 3 mono trials); low-to-moderate for downstream clinical benefit as monotherapy. The combo evidence is pointedly negative: Weiss 2021 (PMID 34140403) — APX005M + cabiralizumab ± nivolumab — produced 62% PD with 0% ORR, and the critique notes this as a mechanism-coherent concern (CSF1R depletion removing the antigen-presenting macrophage the CD40 agonist is trying to activate). Machiels 2020 produced no objective responses. **Combining CD40 agonism with CSF1R depletion is, in the available evidence, null-efficacy.**

**Toxicity profile.** Cytokine release syndrome, transaminitis, and thromboembolism are reported across every CD40-agonist trial (Byrne 2021, Soto 2024, Coveler 2023, Machiels 2020, Weiss 2021). SEA-CD40's non-fucosylated Fc engineering may increase exhaustion-driver risk per the Coveler 2023 critique. Neoadjuvant positioning makes CRS/transaminitis-driven surgical delays a specific clinical counter-productive signal.

**Counter-productive mechanisms.** CP severity aggregate: **Moderate** (3/3 mono papers). Two patterns flagged: (i) **systemic non-cognate T-cell activation** — CD40 agonists activate T cells broadly, which can drive terminal differentiation and exhaustion rather than productive anti-tumor priming when the timing isn't matched to a tumor-antigen-specific response; (ii) **mechanism conflict with CSF1R combinations** — the CD40+CSF1R combo null-efficacy signal (Weiss 2021 and Machiels 2020, both 0% ORR in unselected solid tumors) is mechanism-coherent: CSF1R inhibition removes the macrophage population CD40 is trying to activate. This is a specific contraindication for research-planning, not just a signal across unrelated trials. SEA-CD40's Fc engineering (Coveler 2023) adds an exhaustion-driver concern at the dose-response level.

**Practical considerations.** Sotigalimab's parent PRINCE phase 2 in metastatic PDAC was negative; selicrelumab has no oncology approval. Neoadjuvant windows (Byrne 2021, Soto 2024) are the current highest-signal clinical setting. Avoid stacking with CSF1R depleters.

**Why this rank.** Mechanistically different from all other ranked entries and the only class in the set with reproducible *repolarization-without-depletion* evidence. Ranked 2 despite thin evidence because the mechanism is non-redundant with other classes; the low rank reflects the negative combination signal and small cohorts.

### 3. CD47 / SIRPα blockade — strong hematologic-malignancy efficacy, but TAM biology is inferred and two phase 3 trials failed post-dataset

**Evidence base.** 4 trials: Advani 2018 (NEJM DLBCL/FL), Sallman 2023 (MDS), Daver 2025 (AML), Strati 2025 (evorpacept B-NHL). Total n ≈ 243. All 4 skeptic-Low confidence, all RoB-Moderate, CP-severity 3 Moderate / 1 High. Critically, **every trial in this group reports `change_mechanism: functional-impairment-only` inferred from receptor-occupancy or clinical response, not from an ex-vivo phagocytosis assay** — a uniform extraction flag that the skeptic called out in all 4 critiques.

**Likelihood of desired effect.** Clinically, the efficacy signal in hematologic combos is real (Advani 2018: 50% ORR, 36% CR in rituximab-refractory NHL; Strati 2025: 80% CR with evorpacept + len + rit). Mechanistically, the shieldbreak's target effect — demonstrated TAM modulation — is not well-served by this evidence because phagocytosis is not measured. The post-dataset reality is additionally load-bearing: the magrolimab phase 3 ENHANCE (MDS) and ENHANCE-3 (AML) trials both posted futility/harm signals in 2023–2024, forcing the skeptic to cap Sallman 2023 and Daver 2025 at Low confidence despite large n.

**Toxicity profile.** Uniform on-target anemia (CD47 on RBCs) and thrombocytopenia (CD47 on platelets); priming-dose strategies partially mitigate but do not eliminate these. Evorpacept's engineered reduced-RBC-binding design (Strati 2025) appears to lower but not abolish cytopenia signal. Infection/sepsis signal is prominent in AML combos.

**Counter-productive mechanisms.** CP severity aggregate: **Moderate-to-High** (3 Moderate, 1 High across the set). Three concerns: (i) **on-target anemia/thrombocytopenia** is unavoidable because CD47 is ubiquitously expressed on RBCs and platelets — not a dose-limiting off-target effect but an on-mechanism collateral; (ii) **post-dataset phase 3 failures** (ENHANCE, ENHANCE-3) are external evidence that the mechanism in its tested form does not translate to durable clinical benefit in the hematologic populations where the phase 1b signal was strongest; (iii) **TAM-modulation evidence is absent in solid tumors**, where the shieldbreak's target biology actually resides — all 4 papers are hematologic. If the PI's question is "can CD47/SIRPα blockade modulate solid-tumor TAMs," the literature in this shieldbreak does not answer it.

**Practical considerations.** Magrolimab program restructured after ENHANCE failures; evorpacept is the active CD47-pathway agent. The solid-tumor scope of this shieldbreak is not well-represented in the evidence — all 4 papers are hematologic.

**Why this rank.** Solid clinical-efficacy data in hematologic malignancies but weak direct-TAM evidence, and the post-dataset phase 3 failures cap confidence. Ranked 3 above CCR2/CCR5 because the CD40 comparator is the only one with tumor-compartment PD; CD47 is third because two phase 3 failures plus missing TAM-assay evidence is a research-planning signal worth flagging prominently.

### 4. CCR2 / CCR5 blockade — program-failed at class level; retained because the failure mode is instructive

**Evidence base.** 3 trials: Nywening 2016 (PF-04136309 + FOLFIRINOX), Noel 2020 (PF-04136309 + GnP — terminated for pulmonary toxicity), Grierson 2025 (BMS-813160 + nivo + GnP). Total n ≈ 92. Skeptic CP-severity 2 High / 1 Moderate; confidence 2 Moderate / 1 Low; RoB 2 Serious / 1 Moderate. Nywening 2016 is the strongest PD demonstration (mean tumor TAM 9.0% → 2.4%, p=0.008, paired biopsies) with a 49% vs 0% ORR signal. Grierson 2025 reports intratumoral TAM reduction *without* concurrent peripheral-monocyte change — the authors interpret this as peripheral rebound compensating for tumor depletion.

**Likelihood of desired effect.** PD target-engagement is demonstrable but not translating. Noel 2020's early termination for pulmonary toxicity is the defining datapoint. Grierson 2025's discussion section contains a sponsor-written concession that the drug under-delivered and a call for "a more efficacious CCR2-targeted therapeutic." Monocyte rebound on therapy-off is well-characterized.

**Toxicity profile.** Pulmonary toxicity (Noel 2020), and the mechanism-proposed counter-productive signal is monocyte sequestration in pulmonary tissue from blocked egress. Grierson 2025 reports standard GnP-plus-nivo toxicity without a new CCR2/5-specific signal — consistent with the drug not engaging as hoped.

**Counter-productive mechanisms.** CP severity aggregate: **High** (2 High, 1 Moderate). Three concerns: (i) **program-terminating toxicity** — Noel 2020's pulmonary-toxicity early termination is the class-defining safety datapoint; (ii) **monocyte rebound** — on-therapy blockade of CCR2+ monocyte mobilization is reversible on drug washout, and the Grierson 2025 intratumoral-reduction-without-peripheral-change finding is interpreted as compensatory mobilization from the bone-marrow reservoir; (iii) **sponsor-acknowledged underperformance** — Grierson 2025's discussion explicitly calls for "a more efficacious CCR2-targeted therapeutic," which is an unusual public concession in a phase 1b paper and signals the class as currently program-failed.

**Practical considerations.** No approved CCR2/5 oncology agent. Development programs for PF-04136309 and BMS-813160 have not advanced. The class is **effectively program-failed** for the oncology TAM indication as of 2026.

**Why this rank.** Ranked 4 (last) to stay honest about the class-level failure while keeping it in the ranked set because Nywening 2016 remains the cleanest demonstration in the whole shieldbreak of tumor-compartment TAM depletion correlating with objective response — a mechanism-hypothesis worth preserving even if the specific agents failed.

## Classes examined but not ranked (unranked observations)

**CLEVER-1 blockade (bexmarilimab, 3 trials, Virtakoivu 2021 / Rannikko 2023 / Kontro 2025).** Skeptic CP-severity Unknown across all 3 — narrow-target early clinical. Repolarization signal is mechanistically unusual (v-ATPase-mediated endosomal-acidification impairment per Virtakoivu 2021), and MATINS has pivoted to hematologic indications. Too early to rank; the BEXMAB (Kontro 2025) AML/MDS phase 1 is the most watchable next-step datapoint.

**LILRB2 / TREM2 blockade (3 trials, Taylor 2024 / Yeku 2025 / Beckermann 2024).** Genuinely early. IO-108 (Taylor 2024) has a 23% combo-cohort ORR signal worth tracking; PY314 has two papers (Yeku 2025 and Beckermann 2024) with a null-result in ICI-refractory RCC. **TREM2-specific long-term concern: microglial and osteoclast dependence — Nasu-Hakola disease is TREM2 loss-of-function — which short phase 1 trials cannot detect.** Not ranked for lack of evidence.

**PI3Kγ inhibition (eganelisib, Hong 2023 / O'Connell 2024).** MARIO-1 showed MDSC reduction; MARIO-3 showed TAM repolarization correlating with PFS in front-line TNBC. Program has attenuated. Class collateral includes paradoxical autoimmunity from neutrophil ROS impairment and DC migration defects. Not ranked because n is small and program momentum has visibly slowed.

**Trabectedin / lurbinectedin (Germano 2013 / Sun 2024).** Monocyte-selective cytotoxicity is mechanistically distinctive (caspase-8-dependent), but **the TARMIC phase 1/2 (Sun 2024) missed its primary 6-month non-progression endpoint — observed 12.5% vs 40% target.** Germano 2013 remains the mechanistic foundation. Not ranked because the clinical evidence does not support a forward research call in this shieldbreak frame.

**STING agonism (ADU-S100, Meric-Bernstam 2022).** Textbook counter-productive-mechanism case: intratumoral injection with n=47 and the paper explicitly reports that "RNA expression and immune infiltration assessments in paired tumor biopsies did not reveal significant on-treatment changes." Program halted. Skeptic CP-severity High. Not ranked; retained in this section as the clearest negative exemplar in the set.

## Ranked prioritization

| Rank | Intervention | Likelihood of desired effect | Toxicity burden | Counter-productive MoA | Overall |
|---:|---|---|---|---|---|
| 1 | CSF1R pathway (mAb + TKI) | High for PD; Low-Moderate for clinical benefit outside macrophage-driven tumors | Moderate (on-target tissue-macrophage collateral; hepatic for TKI) | **High** (Gomez-Roca paper-internal inverse correlation between depletion depth and CD8 benefit; IL-34 escape) | Highest-evidence class but temper depletion-depth as the PD goal |
| 2 | CD40 agonism | Moderate for repolarization; Low-Moderate for monotherapy clinical benefit; Null in CSF1R combo | Moderate (CRS, transaminitis, thromboembolism class-wide) | **Moderate** (mechanism conflict with CSF1R depleters; exhaustion drivers with engineered Fc) | Non-redundant mechanism; avoid CSF1R combos |
| 3 | CD47 / SIRPα blockade | Low for the shieldbreak's TAM-modulation target (phagocytosis inferred, not measured); Moderate-High for hematologic clinical benefit | Moderate-High (uniform anemia, thrombocytopenia; sepsis in AML combos) | **Moderate-High** (post-dataset ENHANCE phase 3 failures; solid-tumor evidence absent) | Active clinical program only at evorpacept; solid-tumor gap |
| 4 | CCR2 / CCR5 blockade | Moderate for PD; Low for clinical translation | Serious for PF-04136309 + GnP (program-terminated for pulmonary toxicity) | **High** (terminated trial; rebound kinetics; sponsor-acknowledged underperformance) | Class effectively program-failed; retained for mechanism-hypothesis value |

The **Counter-productive MoA** column summarizes the skeptic-assessed severity of mechanism-level risks that the intervention may undermine the shieldbreak's target effect even when its proximal endpoint is met. It is distinct from Toxicity burden (which is about patient-level AEs). A severe counter-productive MoA pulls the Overall rating down even when Likelihood of effect is high. Severity aggregates per-group as the modal paper-level severity, bumped up one step when a paper-internal High is replicated across ≥2 papers or documents a wrong-direction mechanism in the intended context. Wrong-direction context-outliers are footnoted rather than allowed to move the aggregate.

## Caveats

- **Zero Low-CP-severity trials in this shieldbreak.** No ranked intervention is free of a structural counter-productive concern; rankings are relative, not absolute endorsements.
- **Sample-size heterogeneity.** CSF1R has n ≈ 748 across 13 trials; CCR2/CCR5 has n ≈ 92 across 3. The ranking weights reproducibility alongside magnitude.
- **Hematologic vs solid-tumor split.** CD47/SIRPα evidence is entirely hematologic; CCR2/5 is entirely pancreatic; CSF1R and CD40 span indications.
- **Combination antagonism signal.** The CD40+CSF1R combo null-efficacy (Machiels 2020, Weiss 2021) is a specific research-planning call: do not stack these mechanisms without a preclinical rationale addressing the antigen-presentation conflict.
- **Phagocytosis-assay gap.** No CD47 paper in this set reports ex-vivo phagocytosis quantification. A phase 2 that measures this endpoint directly would be highly informative.
- **CP aggregation rule used here:** modal per-group severity, bumped up one step when a paper-internal High is replicated across ≥2 papers or documents a clearly wrong-direction mechanism in the intended context. Wrong-direction outliers in a discordant context (e.g., Kitko 2023 axatilimab in cGVHD vs oncology repurposing) are footnoted rather than allowed to move the aggregate.
- **Rankings reflect Target-effect-as-written** ("durable human tumor-compartment TAM modulation"). If the Target effect is re-scoped toward anti-tumor clinical benefit, CP severity should weigh more heavily and Rank 1 narrows substantially against Rank 2 — CSF1R's Gomez-Roca inverse-correlation finding becomes near-disqualifying and CD40 agonism's non-redundant mechanism becomes a more attractive research-planning choice.
- **What would change the ranking.** (a) A CSF1R trial that demonstrates *partial* depletion as a pre-specified PD endpoint with correlated clinical benefit would strengthen rank 1. (b) A CD40 monotherapy phase 2 with tumor scRNA-seq would elevate rank 2. (c) An evorpacept solid-tumor phase 1b with paired biopsies would reposition CD47/SIRPα. (d) CLEVER-1 or LILRB2 phase 2 data could introduce a new ranked entry.

## Sources

- Advani R 2018, NEJM — PMID 30380386
- Autio KA 2020, Cancer — PMID 32847933
- Beckermann KE 2024 — PMID 38372949
- Bhatia S 2019, Cancer Immunol Res — PMID 30093453
- Boal LH 2020 — PMID 32943455
- Byrne KT 2021, Cancer Immunol Res — PMID 34112709
- Cassier PA 2020, Lancet Oncol — PMID 33161240
- Coveler AL 2023 — PMID 37385724
- Daver N 2025 — PMID 40198272
- Dowlati A 2021 — PMID 33624233
- Falchook GS 2021 — PMID 33852104
- Germano G 2013, Cancer Cell — PMID 23410977
- Gomez-Roca C 2022, Ann Oncol — PMID 35577503
- Grierson PM 2025 — PMID 40125795
- Hong DS 2023 (MARIO-1) — PMID 37000164
- Kitko CL 2023 — PMID 36459673
- Kontro M 2025 (BEXMAB) — PMID 40449509
- Machiels JP 2020 — PMID 33097612
- Manji GA 2021 — PMID 34321280
- Meric-Bernstam F 2022 (ADU-S100) — PMID 34716197
- Noel M 2020 (terminated) — PMID 31297636
- Nywening TM 2016, Lancet Oncol — PMID 27055731
- O'Connell BC 2024 (MARIO-3) — PMID 39214650
- Papadopoulos KP 2017 — PMID 28655795
- Rannikko JH 2023 (MATINS part 2) — PMID 38056464
- Razak AR 2020 — PMID 33046621
- Sallman DA 2023 (MDS) — PMID 36888930
- Soto M 2024 — PMID 38181044
- Strati P 2025 (evorpacept) — PMID 40729376
- Sun CM 2024 (TARMIC — primary endpoint missed) — PMID 38374062
- Taylor MH 2024 (IO-108) — PMID 39567210
- Virtakoivu R 2021 (MATINS part 1) — PMID 34078651
- Weiss SA 2021 — PMID 34140403
- Wesolowski R 2019 — PMID 31258629
- Yeku OO 2025 (PY314 + PY159) — PMID 40081941

External labels/cited: Niktimvo (axatilimab) FDA label, Aug 2024; Turalio (pexidartinib) FDA label, 2019.

---
*This summary is an evidence-synthesis aid for research planning. It does not constitute clinical advice and must not be used to guide patient care.*
