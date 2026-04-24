#!/usr/bin/env python3
"""
One-shot backfill for the treg-depletion shieldbreak:
add `counter_productive_mechanisms`, `counter_productive_tags`,
and `counter_productive_severity` fields to every existing critique
by appending superseding rows.

Invoke once; pure-Python; no LLM calls, no external deps.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SLUG = "treg-depletion"
CRIT_PATH = REPO_ROOT / "data" / "shieldbreaks" / SLUG / "critiques.jsonl"
RUN_DATE = datetime.now(timezone.utc).date().isoformat().replace("-", "")

# Reason string, recorded once per superseding row.
REASON = (
    "Schema extension 2026-04-23: backfill counter_productive_mechanisms, "
    "counter_productive_tags, and counter_productive_severity fields. "
    "All other narrative, RoB, and confidence fields preserved verbatim from the prior row."
)


# ---------- per-paper backfill content ----------
# Keyed by PMID. Each entry carries:
#   text: 3-6 sentence narrative mixing paper-internal evidence (where cited)
#         and external biological/clinical evidence (explicitly flagged "[external]")
#   tags: list of short machine-readable tags (0-4)
#   severity: "Low" | "Moderate" | "High" | "Unknown"

CPM: dict[str, dict] = {
    # ---------- Fc-enhanced anti-CTLA-4 ----------
    "41759531": {  # Ager 2026 NeoRED-P BMS-986218
        "text": (
            "Fc-enhanced anti-CTLA-4 (BMS-986218, afucosylated ipilimumab) augments ADCC/ADCP on CTLA-4-high "
            "cells; the paper itself argues (Figure 4I–O) that CTLA-4 protein expression was 'exquisitely "
            "confined' to the Treg compartment, bounding the collateral depletion concern for other "
            "effectors in the tumor. However, the same paper documents a compartment dissociation that is "
            "counter-productive in kind: Tregs INCREASE in tumor-draining lymph nodes (p<0.0001) in the "
            "ADT+NF arm, a known class effect the authors acknowledge [paper Results, Figure 4]. The tdLN "
            "is the compartment where anti-tumor CD8 priming happens, so tdLN Treg expansion plausibly "
            "offsets the tumor-Treg reduction the drug accomplishes. Fc-engineering also risks depleting "
            "CTLA-4-upregulating activated CD8 effectors in some tumor contexts [external: Arce Vargas "
            "2018, Cancer Cell]. Severity is moderate — the tumor-side mechanism is clean but the tdLN "
            "signal is measured and unaddressed by the intervention."
        ),
        "tags": ["compartment-dissociation", "tdln-treg-expansion", "adcc-activated-effector-collateral"],
        "severity": "Moderate",
    },

    # ---------- CELMoD iberdomide ----------
    "38776914": {  # Amatangelo 2024 iberdomide MM
        "text": (
            "Iberdomide is a cereblon modulator that degrades Ikaros (IKZF1) and Aiolos (IKZF3) but spares "
            "Helios (IKZF2) and Eos (IKZF4), preserving Treg-lineage TFs. The paper's own PD data "
            "demonstrate that iberdomide INCREASES Tregs alongside effectors in R/R myeloma, the opposite "
            "direction from a Treg-depletion hypothesis. The counter-productive mechanism here is the "
            "mechanism itself for this shieldbreak's goal: the drug is net-suppressive of the "
            "Treg-depletion endpoint. Clinically the CELMoD net effect in MM is driven by direct myeloma "
            "cytotoxicity and effector activation, not Treg reduction — which is why the drug is a useful "
            "therapeutic despite opposing the shieldbreak's proximal mechanism. Severity is high for the "
            "shieldbreak question, regardless of its clinical utility in MM."
        ),
        "tags": ["opposite-direction-mechanism", "treg-induction-by-design"],
        "severity": "High",
    },

    # ---------- Denileukin diftitox (DD / anti-CD25 IL-2 fusion) ----------
    "20664355": {  # Atchison 2010 DD + HD IL-2 RCC
        "text": (
            "Denileukin diftitox targets CD25-high cells via a diphtheria toxin fusion. The "
            "counter-productive concern is twofold: (i) activated CD8 effector T cells transiently express "
            "CD25 and can be co-depleted [external: Baur et al. 2013, FDA ONTAK label]; (ii) co-administered "
            "high-dose IL-2 is known to expand Tregs as well as effectors [external: Ahmadzadeh & Rosenberg "
            "2006, Blood]. The paper reports high-grade lymphopenia and does not distinguish the cell "
            "populations affected beyond a CD25-gated Treg readout, which structurally confounds both the "
            "depletion claim and any off-target assessment. Severity is moderate — the CD25-gating confound "
            "is a measurement problem rather than a clear counter-productive mechanism, but transient "
            "depletion of CD25+ activated effectors is plausible for the dosing schedule used."
        ),
        "tags": ["cd25-effector-collateral", "il2-treg-expansion-confound"],
        "severity": "Moderate",
    },
    "16224276": {  # Attia 2005 DD melanoma
        "text": (
            "Same class concerns as other denileukin diftitox studies: DD depletes CD25-high cells, which "
            "include transiently activated CD25+ CD8 and CD4 effector T cells as well as Tregs "
            "[external: FDA ONTAK label]. This paper is methodologically unusual in using FoxP3 mRNA as "
            "the primary readout, which sidesteps the CD25-gating confound but still cannot distinguish "
            "depletion of Tregs from failure to deplete them when the denominator of CD4 T cells itself "
            "changes. The Attia 2005 negative result is consistent with the class mechanism of DD being "
            "insufficiently Treg-selective to produce a frequency reduction detectable by a FoxP3 readout. "
            "Severity is moderate for the shieldbreak question."
        ),
        "tags": ["cd25-effector-collateral"],
        "severity": "Moderate",
    },
    "16308572": {  # Dannull 2005 DD + RCC DC vaccine
        "text": (
            "Denileukin diftitox given before a tumor-RNA DC vaccine in RCC. The counter-productive concern "
            "is acute: the vaccine's effect depends on CD25-upregulating newly primed effector CD8 T cells, "
            "and DD has a window of anti-CD25 activity that overlaps the priming phase. If DD is "
            "administered close to vaccination, it may deplete the very effectors the vaccine is generating "
            "[external: Rech et al. 2012 PLoS ONE; Sci Transl Med 2009]. The paper's CD25-gated Treg "
            "readout also structurally cannot measure this off-target effect. The Morse 2008 daclizumab "
            "paper explicitly addresses this timing question for daclizumab; Dannull 2005 does not. "
            "Severity is moderate-to-high for the vaccine-combination context."
        ),
        "tags": ["cd25-effector-collateral", "vaccine-priming-window"],
        "severity": "Moderate",
    },
    "27330808": {  # Luke 2016 single-dose DD + gp100 vaccine
        "text": (
            "Single-dose denileukin diftitox immediately before a gp100 peptide vaccine in advanced "
            "melanoma. The class-level concern that DD can deplete CD25+ activated effector T cells is "
            "acutely relevant here because the assay is vaccine-induced gp100-specific CD8 response — the "
            "very population DD might ablate if given after priming. The authors use pre-vaccine DD timing "
            "to minimize this, consistent with the Baur 2013 mechanistic argument that the DD depletion "
            "window is short and confined to pre-priming. Severity is moderate: the timing mitigation is "
            "biologically sound but the paper does not measure CD25-expressing effector subsets directly."
        ),
        "tags": ["cd25-effector-collateral", "vaccine-priming-window"],
        "severity": "Moderate",
    },
    "29204699": {  # Geskin 2018 DD CTCL
        "text": (
            "In CTCL the tumor cells themselves are often CD25+ or CD4+CD25-intermediate, so DD's "
            "anti-tumor activity and its anti-Treg activity are not separable in this disease — a "
            "well-evidenced class distinction from the solid-tumor indications [external: FDA ONTAK label]. "
            "The counter-productive concern for the shieldbreak question is that the 'Treg depletion' "
            "readout in CTCL is contaminated by depletion of CD25+ malignant cells and by depletion of "
            "CD25+ non-malignant T cells that participate in anti-tumor immunity. Severity is moderate — "
            "the drug clearly works in CTCL but not in a way that cleanly isolates a Treg-depletion "
            "mechanism for generalization to other indications."
        ),
        "tags": ["cd25-effector-collateral", "cd25-tumor-target-confound"],
        "severity": "Moderate",
    },
    "33771857": {  # Thibodeaux 2021 DD + IFNα ovarian
        "text": (
            "Phase II failure of DD + IFNα in advanced ovarian cancer. The class-level CD25+ effector "
            "collateral concern applies, and is relevant here because IFNα upregulates CD25 on activated "
            "T cells [external: Petricoin et al. 1997, Nature]. DD + IFNα could therefore make activated "
            "effector T cells MORE susceptible to DD depletion — the combination may have a worse "
            "effector-collateral profile than DD alone. The paper reports clinical failure without "
            "mechanistic dissection of this specific interaction. Severity is moderate-to-high for the "
            "specific combination studied."
        ),
        "tags": ["cd25-effector-collateral", "ifna-cd25-upregulation-interaction"],
        "severity": "Moderate",
    },
    "39362046": {  # Liao 2024 intraperitoneal DD ovarian
        "text": (
            "Intraperitoneal DD in recurrent ovarian cancer. IP administration bounds the systemic exposure "
            "and therefore bounds the systemic CD25+ effector-collateral concern relative to IV DD, which "
            "is a design-level mitigation of the class counter-productive mechanism. Local peritoneal "
            "CD25+ effector depletion remains possible, but the paper reports dose-dependent Treg "
            "reduction without clear evidence of off-target CD8 depletion. Severity is low-to-moderate — "
            "IP route makes this the least-exposed-to-the-class-concern DD application in the set."
        ),
        "tags": ["cd25-effector-collateral", "route-mitigation-ip"],
        "severity": "Low",
    },
    "40006664": {  # Gwin 2025 DD advanced breast
        "text": (
            "DD in treatment-refractory stage IV breast cancer. Class-level CD25+ effector collateral "
            "concern applies (see Atchison 2010 entry). The paper is in a late-line heavily-pretreated "
            "population where lymphoid compartment is already depleted from prior cytotoxic therapy, so "
            "additional DD-mediated CD25+ effector depletion compounds pre-existing lymphopenia in a "
            "counter-productive direction. Severity is moderate."
        ),
        "tags": ["cd25-effector-collateral", "lymphopenia-collateral"],
        "severity": "Moderate",
    },

    # ---------- Anti-CD25 daclizumab ----------
    "17315189": {  # Mahnke 2007 daclizumab melanoma
        "text": (
            "Daclizumab blocks the IL-2Rα (CD25) chain, preventing high-affinity IL-2 signaling on Tregs "
            "but ALSO on activated effector CD8 T cells and CD4 Th1 cells, both of which upregulate CD25 "
            "during priming and proliferation [external: Rech & Vonderheide 2009, Ann NY Acad Sci; Jacobs "
            "et al. 2010, Cancer Res]. This is the textbook counter-productive mechanism: the drug blocks "
            "the same IL-2 signal that anti-tumor effectors need to expand. The paper's claim of a "
            "'prolonged decrease in Tregs in circulation' is CD25-gated and therefore cannot distinguish "
            "Treg depletion from Treg CD25-epitope masking, and cannot measure effector-CD25 signaling "
            "blockade at all. Severity is high for the shieldbreak question."
        ),
        "tags": ["il2-receptor-blockade-collateral", "cd25-gating-confound"],
        "severity": "High",
    },
    "18519811": {  # Morse 2008 daclizumab + CEA vaccine
        "text": (
            "Same class concern as Mahnke 2007: daclizumab blocks IL-2Rα on both Tregs and CD25-upregulating "
            "activated effectors [external: Rech & Vonderheide 2009; Jacobs 2010]. The study adds a vaccine "
            "component, making the counter-productive mechanism particularly salient — vaccine-induced CEA-"
            "specific CD8 responses depend on IL-2Rα signaling that daclizumab blocks. The authors address "
            "this with an explicit pharmacokinetic argument (daclizumab CD25 saturation decays before "
            "effector priming peaks) but do not directly measure effector IL-2 signaling. Severity is high "
            "for the shieldbreak question and for the vaccine-combination context specifically."
        ),
        "tags": ["il2-receptor-blockade-collateral", "vaccine-priming-window", "cd25-gating-confound"],
        "severity": "High",
    },

    # ---------- Standard (non-Fc-enhanced) anti-CTLA-4 ----------
    "21558401": {  # Huang 2011 tremelimumab melanoma
        "text": (
            "Tremelimumab is an IgG2 anti-CTLA-4 that does not deplete intratumoral Tregs in humans despite "
            "the preclinical mouse-ADCC hypothesis. The paper documents an INCREASE in tumor Tregs "
            "(4.75×, p=0.0029), consistent with the class finding. Counter-productive concerns: (a) "
            "anti-CTLA-4 monotherapy is known to induce compensatory upregulation of alternative T-cell "
            "checkpoints including PD-1 and LAG-3 [external: Huang 2017, PNAS; Woo et al. 2012]; (b) the "
            "IgG2 isotype's failure to deplete Tregs means the drug releases CTLA-4-mediated inhibition on "
            "both effectors AND Tregs, a net-equivocal immunomodulation. Severity is low-to-moderate "
            "because the proximal mechanism doesn't operate as intended — limiting off-target concerns."
        ),
        "tags": ["alt-checkpoint-upregulation", "non-depleting-isotype"],
        "severity": "Low",
    },
    "22123319": {  # Hamid 2011 ipilimumab melanoma
        "text": (
            "Ipilimumab (IgG1) does not deplete intratumoral Tregs in humans. Class counter-productive "
            "concerns: (a) PD-1 and LAG-3 compensatory upregulation on T cells after CTLA-4 blockade "
            "[external: Huang 2017, PNAS]; (b) ipilimumab-mediated T-cell activation can drive "
            "immune-related adverse events (colitis, hypophysitis) that reflect paradoxical autoimmunity "
            "in non-tumor tissues — consuming immune capacity away from tumor response. Severity is "
            "low-to-moderate since the proximal Treg-depletion endpoint is not met in humans."
        ),
        "tags": ["alt-checkpoint-upregulation", "paradoxical-autoimmunity"],
        "severity": "Low",
    },
    "18452610": {  # Comin-Anduix 2008 tremelimumab melanoma
        "text": (
            "Same class concerns as Huang 2011 and Ribas 2009: tremelimumab does not deplete intratumoral "
            "Tregs in humans, and CTLA-4 blockade induces compensatory alt-checkpoint upregulation "
            "[external: Huang 2017, PNAS; Woo et al. 2012]. The paper adds the observation that "
            "tremelimumab increases activated effector markers on both Treg and Teff compartments — "
            "consistent with the class interpretation that anti-CTLA-4 is a general T-cell co-stimulation "
            "release rather than a Treg-selective depletion agent. Severity is low for the Treg-depletion "
            "question."
        ),
        "tags": ["alt-checkpoint-upregulation", "non-depleting-isotype"],
        "severity": "Low",
    },
    "19118070": {  # Ribas 2009 ipi/trem retrospective melanoma
        "text": (
            "Retrospective post-hoc analysis of ipilimumab or tremelimumab. Same class counter-productive "
            "findings apply: no intratumoral Treg depletion, expected compensatory alt-checkpoint "
            "upregulation [external: Huang 2017, PNAS]. Severity is low for the shieldbreak question; the "
            "retrospective design also limits the ability to pin mechanism-level observations on the drug."
        ),
        "tags": ["alt-checkpoint-upregulation", "non-depleting-isotype"],
        "severity": "Low",
    },
    "22069060": {  # Nancey 2012 ipilimumab-induced enterocolitis
        "text": (
            "Case report of ipilimumab-induced severe enterocolitis — a paradoxical autoimmune event "
            "driven by the same CTLA-4 blockade that is intended to enhance anti-tumor immunity. The "
            "counter-productive mechanism here is direct and paper-internal: T-cell activation capacity "
            "is consumed by gut immunopathology [external: Beck et al. 2006, JCO for the class "
            "epidemiology]. Severity is moderate at the individual-patient level, low at the population "
            "level — the colitis affects a subset but when it happens it's clearly counter-productive to "
            "the tumor target."
        ),
        "tags": ["paradoxical-autoimmunity"],
        "severity": "Moderate",
    },
    "30054281": {  # Sharma 2019 ipi/trem 3-cancer
        "text": (
            "Well-designed Sharma 2019 paper is the cleanest negative intratumoral Treg data for "
            "standard anti-CTLA-4. Class counter-productive concerns: alt-checkpoint upregulation "
            "[external: Huang 2017, PNAS], failure to deplete means release of CTLA-4 inhibition on both "
            "Treg and Teff compartments equivalently. The paper's finding that prior 'Treg reduction' "
            "claims were frequency-denominator artifacts (Treg % dropped because total T cells rose) adds "
            "to the concern that framing anti-CTLA-4 as a Treg-depletor misallocates mechanistic attention. "
            "Severity is low for the shieldbreak question (the drug doesn't do the proximal thing, so "
            "collateral effects on Tregs-vs-effectors are moot at that mechanism)."
        ),
        "tags": ["alt-checkpoint-upregulation", "non-depleting-isotype"],
        "severity": "Low",
    },
    "28951518": {  # Yi 2017 chemo+ipi NSCLC neoadjuvant
        "text": (
            "Neoadjuvant chemotherapy + ipilimumab in early-stage NSCLC. Ipilimumab counter-productive "
            "concerns apply (alt-checkpoint upregulation, paradoxical autoimmunity) [external: Huang 2017, "
            "PNAS]. The chemotherapy component adds a lymphopenia-collateral dimension: the chemo regimen "
            "itself depletes lymphoid compartment non-selectively, potentially reducing the effector "
            "population that ipilimumab activation would otherwise recruit. Severity is low-to-moderate: "
            "the combination's counter-productive exposure comes more from chemo than from ipilimumab at "
            "the mechanism level."
        ),
        "tags": ["alt-checkpoint-upregulation", "lymphopenia-collateral"],
        "severity": "Low",
    },

    # ---------- Fc-enhanced anti-CTLA-4 (botensilimab) ----------
    "39083809": {  # Chand 2024 botensilimab + balstilimab
        "text": (
            "Botensilimab is an Fc-enhanced (Fc-optimized IgG1) anti-CTLA-4 engineered to increase FcγR "
            "engagement and ADCC/ADCP on CTLA-4-high Tregs. The counter-productive concerns: (a) "
            "Fc-enhancement can deplete activated effector T cells that transiently upregulate CTLA-4 "
            "[external: Simpson et al. 2013, J Exp Med; Arce Vargas et al. 2018, Cancer Cell]; (b) the "
            "combination with anti-PD-1 (balstilimab) compounds autoimmune-toxicity risk — the paper "
            "documents high-grade irAEs consistent with the class expectation. Unlike Ager 2026, this "
            "study does not report compartment-specific Treg data for tumor vs tdLN. Severity is moderate."
        ),
        "tags": ["adcc-activated-effector-collateral", "paradoxical-autoimmunity"],
        "severity": "Moderate",
    },

    # ---------- Non-α IL-2 variants ----------
    "30988166": {  # Bentebibel 2019 bempeg first-in-human
        "text": (
            "Bempegaldesleukin is a PEGylated IL-2 engineered to bias toward IL-2Rβγ (effector/NK) over "
            "IL-2Rαβγ (Treg) signaling. The counter-productive mechanism for this shieldbreak is now "
            "well-evidenced: despite the 'preferential' effector signaling framing, bempeg ABSOLUTELY "
            "expands Tregs 8-10× in humans [external: Gogas 2024 same PIVOT-02 cohort]; the class claim "
            "of 'without Treg enhancement' is a frequency-denominator artifact. The clinical consequence "
            "is visible in the phase 3 PIVOT-IO-001 failure (2022) [external: Diab et al. 2023, JCO]. "
            "Bentebibel 2019's first-in-human report predates this evidence but the mechanism concern was "
            "knowable from the IL-2 biology. Severity is high."
        ),
        "tags": ["treg-expansion-by-design", "denominator-artifact-framing"],
        "severity": "High",
    },
    "32439653": {  # Diab 2020 bempeg + nivo PIVOT-02
        "text": (
            "Same class concerns as Bentebibel 2019: bempeg + nivo in PIVOT-02. The original abstract framed "
            "the drug as effector-selective; the subsequent Gogas 2024 reanalysis of the same cohort "
            "documented 8-10× absolute Treg expansion, and the PIVOT-IO-001 phase 3 failed its primary "
            "endpoints [external: Diab et al. 2023, JCO]. The counter-productive mechanism is the drug's "
            "actual MoA: it expands Tregs, just expands effectors slightly more by frequency. Severity is "
            "high; this is arguably the cleanest negative-clinical-result evidence in the entire set that "
            "the 'favorable ratio' framing is counter-productive to the shieldbreak's goal."
        ),
        "tags": ["treg-expansion-by-design", "denominator-artifact-framing"],
        "severity": "High",
    },
    "39025948": {  # Gogas 2024 PIVOT-02 MoA reanalysis
        "text": (
            "Gogas 2024 is the reanalysis that quantified what Bentebibel 2019 and Diab 2020 framed away: "
            "bempeg absolutely expands Tregs 8-10× and the 'favorable ratio' was a denominator artifact. "
            "The counter-productive mechanism is paper-internal and well-documented here: the drug "
            "expands the population it was designed to spare, and the PIVOT-IO-001 phase 3 clinical "
            "failure is the clinical corollary [external: Diab et al. 2023, JCO]. Severity is high, and "
            "this paper is methodologically the most valuable for understanding WHY the class "
            "counter-productive mechanism matters."
        ),
        "tags": ["treg-expansion-by-design", "denominator-artifact-framing"],
        "severity": "High",
    },
    "40759440": {  # Calvo 2025 nemvaleukin mono
        "text": (
            "Nemvaleukin alfa is an engineered IL-2 fusion designed for IL-2Rβγ preference. Same "
            "counter-productive concern as bempeg: absolute Treg expansion can outpace the 'favorable "
            "ratio' [external: Dennis et al. 2022, Lancet Oncol; ARTISTRY-7 phase 3 failed in ovarian "
            "cancer, 2023]. Nemvaleukin's clinical failures in large phase 3 programs argue the mechanism "
            "shares bempeg's core problem at the clinical level. Severity is moderate-to-high; the "
            "absolute-Treg-expansion signal is smaller than bempeg but in the same direction."
        ),
        "tags": ["treg-expansion-by-design", "denominator-artifact-framing"],
        "severity": "High",
    },
    "39567211": {  # Vaishampayan 2024 nemvaleukin ARTISTRY-1
        "text": (
            "Same class concerns as Calvo 2025. ARTISTRY-1 nemvaleukin mono shows absolute Treg "
            "expansion with claimed effector-biased ratio. The subsequent phase 3 ARTISTRY-7 failure in "
            "ovarian cancer [external: Mylavaram et al. 2023, ASCO] is the clinical evidence the ratio-"
            "shift mechanism does not translate. Severity is high."
        ),
        "tags": ["treg-expansion-by-design", "denominator-artifact-framing"],
        "severity": "High",
    },
    "40990800": {  # Piha-Paul 2025 nemvaleukin less-frequent
        "text": (
            "Less-frequent nemvaleukin dosing in advanced solid tumors. Same class counter-productive "
            "mechanism applies: absolute Treg expansion, denominator-artifact framing. Lower dosing "
            "intensity could theoretically improve the effector/Treg ratio but the paper's PD data "
            "still document absolute Treg expansion. Severity is high."
        ),
        "tags": ["treg-expansion-by-design", "denominator-artifact-framing"],
        "severity": "High",
    },

    # ---------- Cyclophosphamide ----------
    "17956583": {  # Audia 2007 single IV cyclo + BCG
        "text": (
            "Single IV cyclophosphamide is cytotoxic-dose chemotherapy, non-selective for Tregs vs "
            "effectors at that dose [external: Lutsiak et al. 2005, Blood]. The paper's null Treg result "
            "is consistent with this — at cytotoxic dose cyclo depletes lymphoid compartment broadly, "
            "including effector T cells needed for the BCG-induced anti-tumor response. Counter-productive "
            "concern: the dose regimen chosen depletes the effectors the BCG is trying to activate. "
            "Severity is moderate."
        ),
        "tags": ["lymphopenia-collateral"],
        "severity": "Moderate",
    },
    "16960692": {  # Ghiringhelli 2007 metronomic cyclo
        "text": (
            "Metronomic (low-dose oral) cyclophosphamide is reported to be preferentially Treg-depleting "
            "because Tregs have lower ATP reserves and are more sensitive to low-dose alkylation [external: "
            "Lutsiak et al. 2005, Blood; Ghiringhelli et al. 2004, Cancer Immunol Immunother]. The "
            "counter-productive concern is bounded by the dosing: at metronomic dose, collateral effector "
            "depletion is real but modest, and effector function is reportedly preserved. Severity is low "
            "— this is arguably the cleanest dose-selective Treg-depletion mechanism in the set, but it is "
            "not effector-free."
        ),
        "tags": ["lymphopenia-collateral"],
        "severity": "Low",
    },

    # ---------- HDACi ----------
    "29468194": {  # Brinkmann 2018 panobinostat HIV cART
        "text": (
            "Panobinostat is a pan-HDAC inhibitor used here for HIV reservoir reactivation. Paper reports "
            "a 40% INCREASE in Tregs (opposite direction to the shieldbreak hypothesis). "
            "Counter-productive concerns: (a) pan-HDAC inhibition can reduce effector CD8 T-cell function "
            "and destabilize anti-tumor memory [external: Kroesen et al. 2014, Oncotarget]; (b) the "
            "context (HIV cART, not tumor) makes generalization tentative. For the shieldbreak question, "
            "the drug's net direction is counter-productive (Tregs UP), placing severity at high; for its "
            "actual HIV indication this is a separate question."
        ),
        "tags": ["opposite-direction-mechanism", "effector-function-suppression"],
        "severity": "High",
    },
    "24297862": {  # Govindaraj 2014 aza + pano AML
        "text": (
            "Azacitidine + panobinostat in AML. The counter-productive concern is compound: (a) DNMTi "
            "(azacitidine) can demethylate the FOXP3 TSDR and stabilize/induce Tregs [external: Moon et "
            "al. 2016, Clin Cancer Res]; (b) pan-HDACi can reduce effector T-cell function [external: "
            "Kroesen 2014, Oncotarget]. The paper reports a REDUCTION in a TNFR2+ Treg subset only, not "
            "total Tregs; this partial signal does not resolve the class-level counter-productive "
            "exposure. Severity is moderate-to-high."
        ),
        "tags": ["effector-function-suppression", "treg-induction-by-dnmti"],
        "severity": "Moderate",
    },
    "28939740": {  # Pili 2017 entinostat + HD IL-2 RCC
        "text": (
            "Entinostat is class-I-selective HDACi with preferential Treg effects; the paper reports "
            "decreased tumor Tregs combined with HD IL-2. Counter-productive concerns: (a) HD IL-2 "
            "expands Tregs as well as effectors [external: Ahmadzadeh & Rosenberg 2006, Blood], partially "
            "offsetting entinostat's effect; (b) class-I HDACi has been associated with preferentially "
            "enhancing CD8 T-cell function in some settings, which is counter-productive-neutral "
            "[external: McCaw et al. 2021, Cancer Med]. Severity is low for entinostat specifically — the "
            "preclinical class-I-selectivity evidence and paper-internal direction are consistent with "
            "bounded collateral."
        ),
        "tags": ["il2-treg-expansion-confound"],
        "severity": "Low",
    },
    "32681091": {  # Terranova-Barberio 2020 vorinostat + tamox + pembro
        "text": (
            "Vorinostat (broad HDACi, not class-I-selective) in breast cancer. Counter-productive "
            "concerns: (a) vorinostat's broader HDAC target spectrum includes class-II HDACs linked to "
            "effector function [external: Kroesen et al. 2014, Oncotarget]; (b) tamoxifen-pembro adds "
            "modulators with their own off-target profiles. The paper reports tumor Treg decrease with "
            "PBMC Treg stability, a compartment dissociation the class-I-selective preclinical evidence "
            "does not cleanly predict for pan-HDAC vorinostat. Severity is moderate."
        ),
        "tags": ["effector-function-suppression"],
        "severity": "Moderate",
    },
    "34135021": {  # Roussos Torres 2021 entinostat + nivo ± ipi
        "text": (
            "Entinostat + nivo ± ipi combination. Same class-I-HDACi class concerns as Pili 2017 (bounded, "
            "class-I-selective). The nivo/ipi combination adds the alt-checkpoint-upregulation concern for "
            "anti-CTLA-4 [external: Huang 2017, PNAS] and paradoxical autoimmunity risk. Severity is low-"
            "to-moderate."
        ),
        "tags": ["alt-checkpoint-upregulation"],
        "severity": "Low",
    },

    # ---------- DNMTi ----------
    "33876188": {  # Han 2021 decitabine ITP
        "text": (
            "Low-dose decitabine in immune thrombocytopenia (ITP, autoimmune). The 'counter-productive' "
            "framing here is flipped: in ITP, INCREASING Tregs IS the therapeutic goal, so the DNMTi's "
            "well-known Treg-inducing effect via TSDR demethylation [external: Moon et al. 2016, Clin "
            "Cancer Res; Lal & Bromberg 2009, Blood] is the intended mechanism. For the shieldbreak "
            "question (Treg depletion), this paper is a counterexample: DNMTi monotherapy is "
            "DIRECTIONALLY OPPOSITE to Treg depletion. Severity is high for the shieldbreak question "
            "(opposite-direction mechanism by design)."
        ),
        "tags": ["opposite-direction-mechanism", "treg-induction-by-dnmti"],
        "severity": "High",
    },
    "36706355": {  # Penter 2023 decitabine + ipi AML post-HCT
        "text": (
            "Decitabine + ipilimumab in AML/MDS post-allo-HCT. Counter-productive concern is directly "
            "observed: decitabine EXPANDS marrow Tregs via TSDR demethylation [external: Moon 2016], and "
            "the paper documents this marrow Treg expansion as a resistance mechanism to ipilimumab. The "
            "ipilimumab half of the combination adds alt-checkpoint-upregulation concern. Severity is "
            "high — the paper's own finding is that decitabine counter-productively expands the cells ipi "
            "is trying to remove."
        ),
        "tags": ["opposite-direction-mechanism", "treg-induction-by-dnmti"],
        "severity": "High",
    },

    # ---------- Anti-CCR4 mogamulizumab ----------
    "37729184": {  # Fujikawa 2023 moga CCR4-negative solid tumors
        "text": (
            "Mogamulizumab anti-CCR4. The paper itself documents the canonical class counter-productive "
            "mechanism: 'unexpected decrease in central memory CD8+ T cells, which also express CCR4 and "
            "have anti-tumor immunity' [paper Discussion], citing Kurose et al. 2015 and the Nature "
            "Communications 2021 preclinical work [external: Tanaka et al. 2021]. The paper argues "
            "'KW-0761 may concurrently deplete eTregs and central memory CD8+ T cells, and this dual "
            "depletion may cancel anti-tumor immune responses.' The paper also documents high-grade "
            "lymphopenia (25%). Severity is HIGH — this is paper-internal, quantitative, and the authors "
            "explicitly argue it explains the 'minimal clinical benefit' seen in the trial."
        ),
        "tags": ["depletes-beneficial-effectors", "lymphopenia-collateral"],
        "severity": "High",
    },
    "40180420": {  # Jinushi 2025 moga + nivo neoadjuvant
        "text": (
            "Mogamulizumab + nivolumab neoadjuvant in operable solid tumors. Class counter-productive "
            "mechanism from Fujikawa 2023 and the preclinical Tanaka 2021 Nature Communications paper "
            "applies directly [external]: CCR4 is expressed on central memory CD8 T cells and Th1 "
            "effectors, so anti-CCR4 ADCC depletes beneficial effectors alongside Tregs. The paper reports "
            "high-grade lymphopenia consistent with this. Severity is high — the mechanism is "
            "well-evidenced across the anti-CCR4 class and is not mitigated by the neoadjuvant setting."
        ),
        "tags": ["depletes-beneficial-effectors", "lymphopenia-collateral"],
        "severity": "High",
    },
    "35041763": {  # Roelens 2022 moga Sézary
        "text": (
            "Mogamulizumab in Sézary syndrome (CTCL). In CTCL, the malignant cells are CCR4+, so "
            "anti-CCR4 has dual anti-tumor activity — this partially resolves the class counter-productive "
            "concern for CTCL specifically (CCR4+ CD8 depletion still occurs but anti-tumor activity is "
            "also enhanced by depleting CCR4+ malignant cells) [external: Tanaka 2021, Nat Commun]. For "
            "the shieldbreak question (generalizable Treg-depletion mechanism), the class concern "
            "remains. Severity is moderate — in CTCL bounded by dual anti-tumor activity, but the "
            "mechanism-level effector collateral is real and intrinsic to the drug."
        ),
        "tags": ["depletes-beneficial-effectors", "cd25-tumor-target-confound"],
        "severity": "Moderate",
    },
    "40546724": {  # Gordon 2025 moga + rhIL-15
        "text": (
            "Mogamulizumab + rhIL-15 in R/R T-cell malignancies. Class counter-productive concern applies: "
            "CCR4+ CD8 central memory collateral [external: Tanaka 2021, Nat Commun; Fujikawa 2023 paper]. "
            "The rhIL-15 combination partially addresses this by expanding memory CD8 and NK populations "
            "post-depletion, which could rescue the effector compartment — but the paper does not "
            "directly measure whether rescue is effective for the depleted subset. Severity is moderate."
        ),
        "tags": ["depletes-beneficial-effectors", "lymphopenia-collateral"],
        "severity": "Moderate",
    },

    # ---------- Anti-GITR ----------
    "35499569": {  # Davar 2022 TRX518 anti-GITR
        "text": (
            "TRX518 is an afucosylated anti-GITR aimed at Treg depletion via ADCC. Counter-productive "
            "concerns: (a) GITR is expressed on activated CD8 effector T cells as well as Tregs, so "
            "afucosylated anti-GITR can deplete activated effectors [external: Pastor-Fernandez et al. "
            "2023, Front Immunol]; (b) the anti-GITR clinical program did not advance despite modest PD "
            "signals, consistent with the collateral concern not being bounded by drug design. Severity is "
            "moderate."
        ),
        "tags": ["adcc-activated-effector-collateral", "depletes-beneficial-effectors"],
        "severity": "Moderate",
    },
    "34389618": {  # Piha-Paul 2021 GWN323 anti-GITR
        "text": (
            "Same class concerns as Davar 2022. GWN323 is an anti-GITR with Fc-enhanced ADCC; the "
            "counter-productive mechanism is GITR expression on activated effector CD8 T cells "
            "[external: Pastor-Fernandez 2023]. Severity is moderate."
        ),
        "tags": ["adcc-activated-effector-collateral", "depletes-beneficial-effectors"],
        "severity": "Moderate",
    },

    # ---------- Anti-TIGIT ----------
    "38418879": {  # Guan 2024 tiragolumab + atezo NSCLC
        "text": (
            "Tiragolumab is anti-TIGIT Fc-active IgG1. Counter-productive concerns: (a) TIGIT is "
            "expressed on activated effector CD8 T cells (especially exhausted CD8s in TME) so anti-TIGIT "
            "Fc-active mechanism can deplete tumor-infiltrating effectors [external: Chauvin & Zarour "
            "2020, JITC]; (b) the broader anti-TIGIT clinical program has produced mixed phase 3 results "
            "(SKYSCRAPER-01 in PD-L1-high NSCLC missed PFS) [external: Cho et al. 2022, ESMO], "
            "consistent with the collateral concern materializing at clinical scale. Severity is moderate."
        ),
        "tags": ["adcc-activated-effector-collateral", "depletes-beneficial-effectors"],
        "severity": "Moderate",
    },

    # ---------- PI3Kδ-i ----------
    "35170759": {  # Gadi 2022 idelalisib CLL
        "text": (
            "Idelalisib is a PI3Kδ inhibitor. PI3Kδ signaling is required for Treg proliferation and "
            "function but ALSO for effector CD8 T-cell activation and germinal center formation "
            "[external: Okkenhaug et al. 2014, Cancer Discov; Ahmad et al. 2017, Clin Cancer Res]. "
            "Counter-productive concerns: (a) idelalisib has a characteristic toxicity profile of "
            "hepatitis, colitis, pneumonitis that reflects off-target effector disruption; (b) the "
            "drug's label includes black-box warnings for these immune-mediated AEs. Severity is "
            "moderate-to-high for the shieldbreak question; idelalisib is approved in CLL despite these "
            "concerns because the disease-specific efficacy dominates."
        ),
        "tags": ["effector-function-suppression", "paradoxical-autoimmunity"],
        "severity": "Moderate",
    },

    # ---------- Iberdomide / CELMoD (in lupus) ----------
    "35477518": {  # Lipsky 2022 iberdomide SLE
        "text": (
            "Iberdomide in active SLE. The setting is autoimmunity, where INCREASING Tregs is the "
            "therapeutic goal — and the paper reports +104.9% Tregs at 0.45 mg (p<0.001), mechanistically "
            "coherent with Ikaros/Aiolos degradation sparing Helios/IKZF2. For the shieldbreak question "
            "(Treg depletion in cancer), this paper is a counterexample: CELMoD is directionally "
            "opposite. Severity is high for the shieldbreak question (opposite-direction mechanism by "
            "design)."
        ),
        "tags": ["opposite-direction-mechanism", "treg-induction-by-design"],
        "severity": "High",
    },
}


def load_existing() -> list[dict]:
    rows = []
    with CRIT_PATH.open() as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def build_superseding(prior: dict) -> dict | None:
    pmid = prior.get("pmid")
    content = CPM.get(pmid)
    if content is None:
        return None

    new = dict(prior)  # shallow copy; preserves every prior field verbatim
    # Update versioning metadata
    prior_id = prior.get("critique_id") or ""
    # Append -v2 suffix (or bump if -v2 already exists, but for this one-shot there's no v2 yet)
    new_id = f"{prior_id}-v2"
    new["critique_id"] = new_id
    new["supersedes"] = prior_id
    new["supersedes_reason"] = REASON
    new["fetched_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    # Inject the three new fields
    new["counter_productive_mechanisms"] = content["text"]
    new["counter_productive_tags"] = content["tags"]
    new["counter_productive_severity"] = content["severity"]
    return new


def main() -> int:
    priors = load_existing()
    new_rows = []
    missing = []
    for p in priors:
        s = build_superseding(p)
        if s is None:
            missing.append(p.get("pmid"))
        else:
            new_rows.append(s)

    if missing:
        print(f"ERROR — missing CPM content for PMIDs: {missing}")
        return 1

    # Append new rows to critiques.jsonl (preserves old rows; per append-only spec)
    with CRIT_PATH.open("a") as fh:
        for r in new_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"appended {len(new_rows)} superseding rows to {CRIT_PATH}")

    # Severity distribution summary
    sev_count: dict[str, int] = {}
    for r in new_rows:
        s = r["counter_productive_severity"]
        sev_count[s] = sev_count.get(s, 0) + 1
    print("severity distribution:", sev_count)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
