*Scope summary for Treg Depletion and/or Inhibition. Last updated 2026-04-24
from 51 trial-rows across 44 studies (skeptic-critiqued: 44/44, 100%).
Evidence-synthesis aid for research planning — not clinical guidance.*

## Target effect

Reduce the abundance, frequency, dominance, or suppressive function of
regulatory T cells in humans — via classical absolute depletion, ratio
shift in favor of effectors, or destabilization of the Treg phenotype
(FoxP3 loss, TSDR demethylation reversal, functional-suppression-assay
impairment). Tissue compartments of interest are tumor, tumor-draining
lymph node, peripheral blood, bone marrow, and involved tissue (skin,
ascites, colon). Durability and compartment concordance are tracked
alongside magnitude.

## Cross-cutting caveat (read first)

**The magnitude of Treg depletion is frequently uncoupled from clinical
benefit in this dataset**, and several of the "positive" intervention
classes carry structural confounds that inflate the apparent effect.
Three examples motivate the synthesis: (1) the long-running denileukin
diftitox (DD) literature is pervasively compromised by CD25-gating during
CD25-targeting therapy (Dannull 2005 family; flagged by the skeptic as
`cd25-gating-confound`), (2) the IL-2-variant "favorable-ratio" framing
(bempegaldesleukin, nemvaleukin) did not translate into clinical benefit
in PIVOT-IO (phase 3 failed), (3) standard anti-CTLA-4 reliably fails to
deplete intratumoral Tregs in humans (Sharma 2019, Huang 2011, Penter
2023) despite a coherent preclinical mechanism — the reconciling variable
is Fc engineering, not target engagement. Compartment dissociation is
also pervasive (e.g., Ager 2026: tumor Tregs ↓, tdLN Tregs ↑). Rankings
below are calibrated to this.

## Intervention grouping

- **Anti-CCR4 (mogamulizumab)** — Fujikawa 2023 (PMID 37729184), Jinushi
  2025 (PMID 40180420), Roelens 2022 (PMID 35041763), Gordon 2025
  (+rhIL-15; PMID 40546724).
- **Fc-enhanced anti-CTLA-4** — Ager 2026 BMS-986218+ADT (PMID 41759531),
  Chand 2024 botensilimab+balstilimab (PMID 39083809).
- **Low-dose / metronomic cyclophosphamide** — Ghiringhelli 2007 (PMID
  16960692), Audia 2007 (PMID 17956583).
- **Denileukin diftitox (DD / ONTAK / E7777)** — Dannull 2005 (PMID
  16308572), Attia 2005 (PMID 16224276), Atchison 2010 (PMID 20664355),
  Luke 2016 (PMID 27330808), Thibodeaux 2021 (PMID 33771857), Geskin
  2018 (PMID 29204699), Liao 2024 (PMID 39362046), Gwin 2025 (PMID
  40006664).
- **Class-I HDAC inhibitors** — Brinkmann 2018 panobinostat/HIV (PMID
  29468194), Pili 2017 entinostat+IL-2 (PMID 28939740), Terranova-Barberio
  2020 vorinostat+tamoxifen+pembro (PMID 32681091), Roussos Torres 2021
  entinostat+nivo (PMID 34135021), Govindaraj 2014 aza+panobinostat (PMID
  24297862).
- **Standard anti-CTLA-4** — Huang 2011 tremelimumab (PMID 21558401),
  Hamid 2011 ipilimumab (PMID 22123319), Sharma 2019 ipi/treme (PMID
  30054281), Comin-Anduix 2008 treme (PMID 18452610), Ribas 2009 ipi/treme
  (PMID 19118070), Nancey 2012 ipi (PMID 22069060), Yi 2017 chemo+ipi
  (PMID 28951518), Penter 2023 decitabine+ipi (PMID 36706355).

Combination-regimen rows were rolled into their mechanism-of-interest
bucket (entinostat+nivo → HDACi; decitabine+ipi → standard anti-CTLA-4;
mogamulizumab+IL-15 → anti-CCR4). See *Classes examined but not ranked*
below for counterexamples.

## Top interventions

### 1. Anti-CCR4 (mogamulizumab) — most-replicated, mechanism-coherent Treg depletion across PBMC, tumor, and skin

**Evidence base.** 4 trials (paired pre/post, window-of-opportunity, and
translational substudies; total n with Treg measurement = 97 across the
group). Effect magnitudes: ~90% PBMC CCR4+ effector-Treg depletion in
ATLL/CTCL (Fujikawa 2023, PMID 37729184); median 86.7% intratumoral eTreg
reduction in 16/16 solid-tumor neoadjuvant cases (Jinushi 2025, PMID
40180420); significant PBMC and mixed-direction skin decrease at 4 weeks
in Sézary syndrome (Roelens 2022, PMID 35041763); n=6 +rhIL-15 combo with
Treg PD recorded but not tested (Gordon 2025, PMID 40546724). Skeptic
confidence: 1 High, 2 Moderate, 1 Low.

**Likelihood of desired effect.** Direction, magnitude, and compartment
concordance are all consistent — and the target biology (CCR4 is
selectively enriched on effector Tregs) matches the readout. Jinushi 2025
anchors tumor-compartment depletion where most other classes fail.
Mogamulizumab depletes the CCR4+ eTreg *subset* specifically; total
intratumoral FOXP3+ counts are mixed (8/16 decreased in Jinushi), so
claims should be phrased at the subset level.

**Toxicity profile.** Prescribing experience comes predominantly from
the CTCL/ATLL label. Infusion reactions, skin eruptions (drug rash,
severe cutaneous reactions including SJS/TEN have been reported),
immune-related AEs, and severe/fatal complications after subsequent
allogeneic HSCT are labelled risks (FDA USPI POTELIGEO; see DailyMed).
In the solid-tumor combination setting (Jinushi 2025) the safety profile
was reported as manageable with no new signals, but the population is
small and follow-up is short.

**Counter-productive mechanisms.** CP severity aggregate: **High**
(paper-internal + replicated). The class concern is **depletion of
beneficial effectors**: CCR4 is co-expressed on central-memory CD8
T cells and Th1 effectors, so ADCC against CCR4+ Tregs collaterally
depletes anti-tumor effectors (flagged 4/4 papers; paper-internal in
Fujikawa 2023 and Jinushi 2025, external-evidence-only in Roelens 2022
and Gordon 2025; anchored to Tanaka 2021 *Nat Commun* and Kurose 2015
preclinical). Fujikawa 2023 authors explicitly argue this "dual
depletion may cancel anti-tumor immune responses" and tie it to the
observed minimal clinical benefit, with high-grade lymphopenia in 25%.
Mitigations seen in the set: CTCL indications where CCR4+ malignant
cells are themselves a target (Roelens 2022) and IL-15 rescue of
memory-CD8/NK post-depletion (Gordon 2025, mechanism plausible but not
directly measured).

**Practical considerations.** Mogamulizumab is FDA-approved for CTCL
(2018); off-label use in solid tumors is window-of-opportunity /
investigator-led so far. Combinable with anti-PD-1 (Jinushi 2025) and
with rhIL-15 (Gordon 2025). Flow gating for CCR4 is straightforward;
eTreg quantification (CD45RA−FoxP3^hi, Miyara Fr. II) is recommended given
that total-FoxP3 readouts dilute the effect.

**Why this rank.** Most-replicated positive signal in the shieldbreak,
with direct intratumoral evidence, a mechanism-coherent subset readout,
and two Moderate-or-better skeptic confidences. No other class combines
these three properties.

**Per-trial detail.**

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Mogamulizumab (KW-0761) monotherapy, CCR4-negative solid tumors | PBMC eTreg median 2.1% → 0.20% of CD4+ at 4 weeks (~90% reduction, dose-independent across 0.1–1.0 mg/kg, n=37 evaluable). 1 PR + 9 SD of 49 (modest monotherapy activity despite profound PD) | N=49; treatment-related AEs in 93.9%; grade 3–4 in 21 (42.9%). Dominant categories skin disorders (n=34) and lymphopenia (n=34, with 15 grade 3–4 lymphopenia events ≈30%). No grade 3–4 skin disorders; no drug-related deaths | [Fujikawa 2023](https://pubmed.ncbi.nlm.nih.gov/37729184/) |
| Mogamulizumab + nivolumab (neoadjuvant, renal/lung/esophageal/oral) | Tumor CCR4+ FoxP3+ eTreg median −86.7% (range −94.8% to −52.7%), 16/16 patients depleted; total FoxP3+ median −11.1% (decreased in 8/16). 1 pCR + 3 PRs / 16; trend toward improved PFS/OS with lymphocyte infiltration | N=16; grade 3–4 TRAEs in 6/16 (38%): lymphopenia 25%, maculopapular rash 13% most frequent. 1 grade 5 interstitial pneumonia (cause of death adjudicated as disease progression). Cohort 2 (higher dose) skin AEs led to early closure without proceeding to cohort 3 | [Jinushi 2025](https://pubmed.ncbi.nlm.nih.gov/40180420/) |
| Mogamulizumab (Sézary syndrome, long-term PD) | Drastic decrease in activated PBMC Tregs within first 4 weeks (numeric values not reported — abstract-only, paper not OA); long-term skin immune restoration qualitative; 17/26 with early complete blood response correlated with higher baseline CCR4 | N=26; abstract-only; AE quantitative data not extractable. Mogamulizumab on-label cutaneous and infusion-reaction risks per FDA POTELIGEO USPI apply | [Roelens 2022](https://pubmed.ncbi.nlm.nih.gov/35041763/) |
| Mogamulizumab + rhIL-15 (R/R T-cell malignancies) | Treg PD not measured in this trial — PD focus is NK expansion and ADCC. Treg row retained as mechanism-targeted regimen (uncritiqued for Treg-specific contribution); 1 PR (ATLL) | N=6; most common AEs rash, infection, fever (67% each); grade 4 AKI in 33%; grade 3+ anemia in 25% of cycles; 2 DLTs at dose level 2 (grade 4 acidosis/capillary leak/AKI; grade 4 myositis); MTD = dose level 1 | [Gordon 2025](https://pubmed.ncbi.nlm.nih.gov/40546724/) |

### 2. Fc-enhanced anti-CTLA-4 — mechanism-rescue for the anti-CTLA-4 failure mode, with thin but directionally clean human evidence

**Evidence base.** 2 trials (n with Treg measurement = 36 total;
randomized phase I and paired pre/post phase I). Ager 2026 BMS-986218 +
ADT reduced intratumoral Tregs relative to ADT alone (p=0.031) in
high-risk localized prostate cancer (PMID 41759531). Chand 2024
botensilimab + balstilimab reported significant intratumoral FOXP3+
reduction by IHC in MSS mCRC (PMID 39083809). Skeptic confidence: both
Moderate; Ager RoB Some concerns, Chand RoB Moderate.

**Likelihood of desired effect.** Pharmacologically distinct from
standard anti-CTLA-4: Fc engineering for increased FcγR affinity is the
variable that reconciles the preclinical ADCC-on-Treg model with the
null human result for ipilimumab/tremelimumab (see Rank 6). Ager 2026 is
the most rigorous intratumoral-Treg PD readout in the shieldbreak — it
pairs a randomized control (ADT alone) with a mechanism-specific
comparator, and the contrast is significant. Chand 2024 is single-arm
IHC, industry-sponsored; the direction is consistent but the evidentiary
weight is lower. Compartment dissociation is on display — Ager also
observed *expansion* of tdLN Tregs while tumor Tregs contracted.

**Toxicity profile.** Botensilimab has reported immune-related AEs
including colitis, hepatitis, pneumonitis and infusion reactions at
rates roughly comparable to or slightly exceeding ipilimumab at
equivalent doses in the Chand 2024 combination (PMID 39083809, per the
published safety section). Class-level FcγR-engagement predicts potential
for heightened irAE burden relative to non-Fc-enhanced anti-CTLA-4, but
head-to-head data are not available in this dataset. BMS-986218 safety
in Ager 2026 was reported as manageable at the neoadjuvant dose tested.

**Counter-productive mechanisms.** CP severity aggregate: **Moderate**
(2/2 papers). Two flagged patterns: (i) **compartment dissociation /
tdLN Treg expansion** — Ager 2026 directly documents tumor-Treg
contraction alongside tdLN Treg expansion (p<0.0001), a paper-internal
finding in the priming compartment; (ii) **ADCC on activated effectors**
— Fc-engineering increases FcγR engagement on any CTLA-4-high cell,
which transiently includes activated CD8 effectors (external: Simpson
2013, Arce Vargas 2018). Ager 2026 partially bounds (ii) by showing
CTLA-4 protein was largely confined to the Treg compartment in that
tumor. Chand 2024 does not report compartment-specific data and adds
anti-PD-1 combination autoimmune-toxicity compounding
(paradoxical-autoimmunity tag).

**Practical considerations.** Both agents are investigational
(botensilimab AGEN1181 and BMS-986218 are in active clinical development
as of 2026). Industry-controlled supply; academic access primarily
through sponsored trials. Combinable with anti-PD-1 and ADT as
demonstrated.

**Why this rank.** The strongest mechanism-rescue story in the dataset
and the most rigorous intratumoral randomized comparison (Ager 2026),
but total n across the class is small and single-vendor; one more
replication outside the sponsors would shift this to Rank 1 territory.

**Per-trial detail.**

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| BMS-986218 (Fc-enhanced anti-CTLA-4 / afucosylated ipilimumab) + ADT, neoadjuvant high-risk localized prostate | Tumor TI-Treg frequency reduced in ADT+BMS-986218 vs ADT alone (p=0.031, n=14 vs n=10); ADT-only arm INCREASED TI-Tregs vs untreated (p=0.002); tdLN Tregs simultaneously expanded (p<0.0001). Densities figure-only, not text-quantified. Depth of Treg reduction associated with improved clinical outcomes; CD16a+ macrophage correlation p=0.033 supports ADCC | N=24 randomized; any-grade TRAEs 80% (ADT-only) vs 71% (ADT+NF), mostly attributed to ADT and injection-site reactions. Grade ≥3 TRAEs rare — 1 patient had grade 3 asymptomatic lipase elevation that resolved without intervention; 3 grade 1–2 GI events on anti-CTLA4-NF arm. No interim safety boundary crossings; no unexpected surgical complications | [Ager 2026](https://pubmed.ncbi.nlm.nih.gov/41759531/) |
| Botensilimab (AGEN1181, Fc-enhanced anti-CTLA-4) + balstilimab (anti-PD-1), MSS mCRC | Significant intratumoral FOXP3+ reduction by IHC and RNA-seq signature in n=12 paired biopsies (fold-change and p not text-stated; figure-only, Fig 5H). PBMC/serum Tregs unchanged (tumor-selective). Activity in ICI-resistant tumor type | N≈65 phase 1 enrolled; most common grade ≥3 TRAE was diarrhea/colitis (combined preferred terms diarrhea/colitis/enteritis; per-AE frequencies in Supplementary Table S9 not in extracted text). Notably absent: hypophysitis (consistent with V11L/L30L Fc point mutations abrogating C1q binding) | [Chand 2024](https://pubmed.ncbi.nlm.nih.gov/39083809/) |

### 3. Low-dose / metronomic cyclophosphamide — schedule-dependent; the positive report is small but statistically strong

**Evidence base.** 2 trials (n with Treg measurement = 58). Ghiringhelli
2007 reported a 61% Treg frequency reduction and 78% absolute count
reduction (p<0.0001 for both) in n=9 end-stage solid-cancer patients on
metronomic oral cyclophosphamide, with restored NK/T-cell function (PMID
16960692). Audia 2007 reported no Treg reduction in n=49 with a single
IV cyclophosphamide dose prior to intratumoral BCG (PMID 17956583).
Skeptic confidence: Moderate (Ghiringhelli), Low (Audia).

**Likelihood of desired effect.** Dose-schedule-dependent. The
metronomic oral schedule (Ghiringhelli) depleted; the single IV dose
(Audia) did not. This is a real biological distinction, not a
discrepancy to explain away — both critiques converge on schedule as
the reconciling variable. The positive report is small (n=9) but the
effect size and significance are unambiguous.

**Toxicity profile.** Metronomic cyclophosphamide has a
well-characterized safety profile: myelosuppression, hemorrhagic
cystitis (rare at metronomic doses), infections, and gonadotoxicity are
the load-bearing labelled risks (cyclophosphamide USPI; FDA DailyMed).
At the 50 mg/day oral metronomic dose used by Ghiringhelli, cumulative
exposure is lower than standard chemotherapy but long-term bladder and
fertility monitoring is standard.

**Counter-productive mechanisms.** CP severity aggregate: **Low** for
the metronomic regimen (Ghiringhelli 2007), **Moderate** for single-IV
dosing (Audia 2007). The mechanism-level concern is **non-selective
lymphopenia** at cytotoxic doses; metronomic oral dosing exploits the
lower ATP reserves of Tregs for preferential depletion (Lutsiak 2005
*Blood*; Ghiringhelli 2004) and the paper-internal evidence is that
effector function is preserved/restored. This is arguably the cleanest
dose-selective Treg-depletion mechanism in the shieldbreak — but it is
not effector-free, and the single-IV Audia 2007 null is
mechanism-consistent with non-selective depletion eliminating the
BCG-responding effectors.

**Practical considerations.** Generic, inexpensive, orally available,
globally accessible. Combinable with checkpoint blockade and vaccines;
used widely as a Treg-depleting pretreatment in adoptive-cell-therapy
and vaccine trials outside this dataset. Schedule must be metronomic —
single-IV dosing is a likely null.

**Why this rank.** High replication floor for schedule biology and a
strong statistical result in the positive report, but the total evidence
base is 2 trials and the positive n is 9. Ranked above DD despite the
smaller n because the CD25-gating confound makes much of the DD
literature hard to interpret.

**Per-trial detail.**

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Metronomic oral cyclophosphamide 50 mg/day (advanced end-stage solid cancer) | PBMC CD4+CD25high frequency 7.9 ± 1.5% → 3.1 ± 1.8% (−61%, p<0.0001); absolute count 28.7 ± 9.4 → 6.4 ± 5.4 cells/mm³ (−78%, p<0.0001) at 1 month. T-cell proliferation and NK cytotoxicity restored to healthy-volunteer levels | N=9; AE frequencies not reported in this PD-focused paper. Cyclophosphamide class risks (myelosuppression, hemorrhagic cystitis, infections, gonadotoxicity) per generic USPI apply; metronomic 50 mg/day cumulative exposure substantially below standard chemotherapy dosing | [Ghiringhelli 2007](https://pubmed.ncbi.nlm.nih.gov/16960692/) |
| Single IV cyclophosphamide + intratumoral BCG (metastatic mixed solid cancer) | PBMC Treg baseline 9.2% (vs 7.1% healthy); no significant modulation of Treg numbers or function post-cyclophosphamide. Authors explicitly state cyclophosphamide may not represent optimal Treg-elimination therapy | N=49; abstract-only (paper not in PMC OA); detailed AE frequencies not extractable. Standard single-dose cyclophosphamide toxicity expected | [Audia 2007](https://pubmed.ncbi.nlm.nih.gov/17956583/) |

### 4. Denileukin diftitox (DD / ONTAK / E7777) — large body of work, but the CD25-gating confound and the Attia-vs-Dannull split make this ambiguous

**Evidence base.** 8 trials (n with Treg measurement = 153 across the
group; designs span paired pre/post, randomized phase 2, single-arm
phase 1/2, and case series). Positive signals: Dannull 2005 (~51% PBMC
reduction in RCC; PMID 16308572), Atchison 2010 (56.3% with DD+HD IL-2;
PMID 20664355), Thibodeaux 2021 (n=2 DD+IFNα "worked" before drug
shortage; PMID 33771857), Geskin 2018 (29% in CTCL, p=0.03 — responder-
dependent; PMID 29204699), Liao 2024 (73% PBMC p=0.0275, 67% ascites
p=0.27 n.s.; PMID 39362046), Gwin 2025 (p=0.10 overall n.s., partial;
PMID 40006664). Negative signals: Attia 2005 (null by FoxP3 mRNA with
retained ≥50% suppressive function, n=13 melanoma; PMID 16224276), Luke
2016 (phase 2 n=60 with peptide vaccine, no depletion; PMID 27330808).
Skeptic confidence: 1 Moderate (Attia), 2 Moderate (Liao, Geskin), 5 Low;
RoB distribution includes 2 Serious.

**Likelihood of desired effect.** Genuinely uncertain. The Attia 2005
vs Dannull 2005 split is the foundational conflict in this class, and
the skeptic identified a pervasive structural confound:
**CD25-gating during CD25-targeting therapy** means many of the
"positive" reports are measuring surviving CD25^lo cells rather than
genuine Treg depletion. The two reports that sidestep the confound with
FoxP3-mRNA readouts go in opposite directions (Liao 2024 positive in
PBMC; Attia 2005 negative in melanoma). The response-stratified finding
in Geskin 2018 (responders deplete, non-responders expand) is
intriguing but post-hoc. Directional consistency within CD25-gated
studies is not strong evidence when the gating is the confound.

**Toxicity profile.** DD's labelled risks include capillary-leak
syndrome, visual/vascular events, infusion reactions, and
hepatotoxicity (ONTAK/E7777 USPI, FDA DailyMed). The product has had
multiple manufacturing/supply interruptions, including the shortage
that halted Thibodeaux 2021 enrollment — a non-trivial practical
toxicity for research planning.

**Counter-productive mechanisms.** CP severity aggregate: **Moderate**
(7/8 Moderate, 1/8 Low). Dominant flag: **CD25+ activated-effector
collateral** — DD depletes CD25-high cells indiscriminately, including
transiently activated CD8 and CD4 effectors (external: FDA ONTAK label,
Baur 2013). Paper-internal concerns sharpen this in two specific
contexts: (a) **vaccine-priming window** (Dannull 2005, Luke 2016) — if
DD exposure overlaps priming, it may ablate the very effectors the
vaccine generates; (b) **IFNα-CD25 interaction** (Thibodeaux 2021) —
IFNα upregulates CD25 on activated T cells, plausibly making the
DD+IFNα combination worse for effector collateral than DD alone. Liao
2024's intraperitoneal route bounds systemic exposure and is the
Low-severity case. In CTCL (Geskin 2018) the CD25+ malignant-cell
confound operates in both directions and the Treg-depletion mechanism
is not cleanly isolable.

**Practical considerations.** E7777 (now also referred to as I/ONTAK)
received FDA approval for CTCL (2023); supply has historically been
inconsistent. Academic access outside CTCL requires sponsored or
investigator-led trials. Any future Treg-PD endpoint should use FoxP3
mRNA or TSDR methylation to sidestep the CD25 confound — surface-only
CD25-based gating should be treated as uninformative here.

**Why this rank.** Largest evidence base in the shieldbreak after
standard anti-CTLA-4, but the skeptic-weighted magnitude shrinks
substantially once the CD25 confound is applied and the Attia-vs-Dannull
split is taken seriously. Ranked here rather than lower because Liao
2024 and Geskin 2018 provide at least some confound-resistant positive
signal.

**Per-trial detail.**

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Denileukin diftitox (DAB389IL-2, single 18 µg/kg dose) prior to RCC RNA-DC vaccine | PBMC CD4+CD25high Tregs reduced 26–76% relative (median −51%) at day 4 in 7/7 treated; FoxP3 mRNA −30 to −80%; in vitro suppressive activity abrogated; nadir d4, ~75% recovery by 2 months. Enhanced vaccine-induced T-cell responses | N=7 treated + 4 vaccine-only controls; AE quantification not in extractable text — abstract describes Treg depletion "without inducing toxicity on other cellular subsets". DD class risks (capillary leak, infusion reactions, hepatotoxicity, visual events) per ONTAK USPI apply | [Dannull 2005](https://pubmed.ncbi.nlm.nih.gov/16308572/) |
| Denileukin diftitox 9 or 18 µg/kg/day × 5 (metastatic melanoma, two cohorts) | PBMC FoxP3 mRNA cycle-1 change: 9 µg/kg cohort −1.27±2.57 (p=0.656, n=4); 18 µg/kg cohort −2.01±0.618 (p=0.031, n=5); pooled p=0.167. After ≥4 cycles −3.30±3.21 (p=0.380). In vitro Treg suppression retained at ≥50% in 5/5 patients tested. 0/13 objective responses | N=13; detailed AE frequencies not extractable from PMC text. Generally tolerated at studied doses (single grade ≥3 hypersensitivity reaction was DLT-defining in protocol) | [Attia 2005](https://pubmed.ncbi.nlm.nih.gov/16224276/) |
| Denileukin diftitox + high-dose IL-2 (metastatic RCC) | PBMC Tregs median −56.3% pre-DD to post-DD (p=0.013, pooled cohorts B+C n=15). 33% RR (not distinguishable from HD IL-2 monotherapy historical benchmark) | N=18; abstract-only (J Immunother not OA); detailed AE frequencies not extractable. HD IL-2 toxicity (capillary leak, hypotension, organ dysfunction) is the dominant burden in this combination | [Atchison 2010](https://pubmed.ncbi.nlm.nih.gov/20664355/) |
| Single-dose denileukin diftitox + gp100 peptide vaccine (advanced melanoma, RCT) | PBMC Tregs not significantly altered (no quantification, Fig 2 unquantified); 1/1 paired tumor biopsy showed INCREASED intratumoral FoxP3 post-DD. No improvement in vaccine-induced T-cell responses vs vaccine alone. 1 PR + 8 SD across 17 treated (4 DD: 5 vaccine-only) | N=17 treated; no drug-related grade 3–4 adverse events reported. DLTs defined as ≥grade 3 or grade 2+ autoimmunity / visual impairment per protocol | [Luke 2016](https://pubmed.ncbi.nlm.nih.gov/27330808/) |
| Denileukin diftitox + IFNα (advanced ovarian) | DD monotherapy phase II "failed"; DD + IFNα2a phase II 2/2 patients responded before DD shortage halted enrollment (numerics not extractable from abstract). Qualitative claim of Treg depletion + IFNα-augmented anti-tumor immunity | N=2 (DD+IFNα completed); abstract-only (Clin Cancer Res not OA); AE quantitative data not extractable. DD class risks apply | [Thibodeaux 2021](https://pubmed.ncbi.nlm.nih.gov/33771857/) |
| Denileukin diftitox 18 µg/kg/day × 5 (CTCL: MF and Sézary) | PBMC CD4+FoxP3+ median relative change −29% (94% CI −83% to −20%) post one DD cycle, p=0.03; clinical responders (9/12 long-term) achieved 20–45% absolute Treg reductions; non-responders 2/3 EXPANDED Tregs | N=77; abstract-only AE detail in extracted text. DD-typical infusion reactions, capillary-leak risk per ONTAK USPI; in CTCL cohort the CD25+ malignant-cell substrate confounds attribution | [Geskin 2018](https://pubmed.ncbi.nlm.nih.gov/29204699/) |
| Intraperitoneal denileukin diftitox (ONTAK), recurrent ovarian | PBMC FoxP3 mRNA pooled −73% (mean 0.1726±0.0442 → 0.0374±0.0101, p=0.0275; 15 µg/kg subset p=0.0374); ascites mean −67% (0.1855±0.0945 → 0.0597±0.0304) but p=0.2737 n.s. (n=3). 5/9 met ≥25% Treg reduction efficacy criterion; 3 had CA-125 decreases, no PRs | N=10 across 3 dose levels; majority of AEs transient grades 1–2; 1 DLT in 6-patient 15 µg/kg expansion. 1 grade 4 cytokine storm at 25 µg/kg requiring prolonged hospitalization closed that arm. MTD = 15 µg/kg | [Liao 2024](https://pubmed.ncbi.nlm.nih.gov/39362046/) |
| Denileukin diftitox (E7777 / I/ONTAK) 18 µg/kg/day × 5 + pDC-targeted vaccine (stage IV breast) | Overall PBMC Treg change p=0.10 (n.s.); 6/15 (40%) achieved ≥25% reduction (responder subset 56.0% ± 10.96%); anti-DT IgG response in 100% by week 6 likely limited efficacy. 0 CR/PR; 4 SD (27%) | N=15; 11 (73%) had at least one grade 3–4 AE; 2 (13%) discontinued for toxicity, 9 (60%) for progressive disease; per-AE category frequencies not extracted | [Gwin 2025](https://pubmed.ncbi.nlm.nih.gov/40006664/) |

### 5. Class-I HDAC inhibitors (entinostat / vorinostat / panobinostat) — context-dependent direction; oncology signals plausibly favorable, HIV/cART signal opposite

**Evidence base.** 5 trials (n with Treg measurement = 76 across the
group). Oncology context — directionally favorable: Pili 2017
entinostat+HD IL-2 RCC (lower Treg associated with response, p=0.03;
PMID 28939740), Terranova-Barberio 2020 vorinostat+tamoxifen+pembro in
ER+ breast (tumor Tregs 11.8%→2.9% overall, p=0.0067; PMID 32681091),
Roussos Torres 2021 entinostat+nivo (CD8:FoxP3 ratio 4.11→9.03,
p=0.002; PMID 34135021), Govindaraj 2014 aza+panobinostat in AML
(TNFR2+ Treg subset reduction in PBMC and BM with associated benefit;
PMID 24297862). HIV/cART context — opposite: Brinkmann 2018 panobinostat
HIV cART cohort (+40% Tregs at day 4, p=0.003; PMID 29468194). Skeptic
confidence: all 5 Moderate; 2 Some concerns RoB, 3 Moderate.

**Likelihood of desired effect.** Plausibly favorable in oncology,
clearly unfavorable in HIV/cART reactivation — a context-dependent
class. Terranova-Barberio 2020 is the strongest single intratumoral
result in this group (large magnitude, p<0.01, in tumor). Roussos
Torres 2021 is properly a ratio-shift rather than Treg-only reduction
(the +119.7% `pct_change` field reflects the CD8:FoxP3 *ratio* shift,
not a Treg expansion — a data-quality note for downstream readers).
Govindaraj 2014 targets a minority subset (TNFR2+ Tregs), not total
Tregs, and panobinostat is the in-vitro driver.

**Toxicity profile.** Class-I HDACi labelled toxicities include
thrombocytopenia, neutropenia, fatigue, GI (nausea/diarrhea),
QT-interval prolongation (panobinostat more than entinostat/vorinostat),
and a black-box diarrhea/cardiac warning for panobinostat in myeloma
(FARYDAK USPI, FDA DailyMed). Vorinostat (ZOLINZA USPI) and entinostat
(investigational) carry broadly similar hematologic toxicity at
oncology doses. IL-2 combination (Pili 2017) and pembrolizumab
combination (Terranova-Barberio 2020) add the respective partner
toxicity profiles.

**Counter-productive mechanisms.** CP severity aggregate: **Moderate**
(spread: 2 Low, 2 Moderate, 1 High context-outlier). Flagged patterns:
(i) **effector-function suppression** — pan-HDAC inhibitors
(vorinostat, panobinostat) can reduce effector CD8 function (external:
Kroesen 2014); bounded for class-I-selective entinostat (Pili 2017,
Roussos Torres 2021, both Low). (ii) **Opposite-direction mechanism in
the wrong context** — Brinkmann 2018 panobinostat in HIV/cART increases
Tregs 40%, a High-severity outlier that is context-discordant
(HIV-latency reactivation, not oncology) and footnoted accordingly.
(iii) **DNMTi confounder** in Govindaraj 2014 — the azacitidine partner
demethylates the FOXP3 TSDR and can induce Tregs, operating against the
HDACi direction. The selectivity/breadth axis (class-I vs pan-HDAC) is
the reconciling variable the data point at.

**Practical considerations.** Vorinostat and panobinostat are
FDA-approved (CTCL and multiple myeloma respectively); entinostat is
investigational as of 2026. Orally available, broadly combinable. The
HIV-reservoir use case motivated Brinkmann 2018 and is *not* a
Treg-depletion indication — inclusion of that data point here is as a
counterexample that pins down context-dependence.

**Why this rank.** Directionally favorable signal in oncology with
multiple Moderate-confidence results and one strong intratumoral
magnitude, but context-dependence and the single-positive-per-agent
pattern prevent a higher ranking. Mechanism is plausible but not
precisely specified (FoxP3 stability, TSDR methylation, TNFR2+ subset
biology — each HDACi study invokes a different rationale).

**Per-trial detail.**

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Panobinostat (pan-HDAC) in HIV+cART (reservoir reactivation, context-discordant) | PBMC Treg frequency +40% at day 4 (p=0.003), sustained at day 28 (p=0.004); CTLA-4 MFI on Tregs +25% (p=0.007); CD39 MFI +12% (p=0.02). Tregs ACTIVATED rather than depleted; returned to baseline by week 24 | N≈14–15 evaluable; HIV/cART context — paper notes oncology-dose HDACi toxicities have impeded development as immunomodulators in non-cancer; quantitative AE table not extracted | [Brinkmann 2018](https://pubmed.ncbi.nlm.nih.gov/29468194/) |
| Entinostat + high-dose IL-2 (metastatic ccRCC) | PBMC Tregs lower in responders (n=5) than progressors (n=7) at C1D1 (p=0.0273); lower Treg overall associated with response (p=0.03). Tumor (n=3 paired): entinostat priming prevented HD IL-2-induced Treg expansion (not statistically tested). ORR 37%; mPFS 13.8 mo; mOS 65.3 mo | N=47; most common grade 3–4 TRAEs hypophosphatemia 16%, decreased lymphocytes 15%, hypocalcemia 7% — all transient. 1 RA flare; 1 death during treatment deemed unrelated (cardiac tamponade from undiagnosed lung primary). HD IL-2 hypotension 3.2%, capillary-leak signal expected | [Pili 2017](https://pubmed.ncbi.nlm.nih.gov/28939740/) |
| Vorinostat + tamoxifen + pembrolizumab (ER+ metastatic breast, ≥5 prior regimens) | Tumor CD4+FoxP3+CTLA-4+ Tregs 11.8% → 2.9% overall (−75.4%, p=0.0067); responders 20.3% → 4.2% (p=0.031); non-responders 10.4% → 2.5% (p=0.034). PBMC Tregs unchanged. Treg depletion in BOTH responders and non-responders. ORR 4%; CBR 19%. Trial stopped early for futility | N=34; grade 3–4 toxicities included transaminitis 9% (incl immune hepatitis with discontinuation), fatigue 6%, hyponatremia 6%, thrombocytopenia 6%, anorexia 3%; 1 disabling stroke (relatedness unclear) requiring discontinuation. Grade 2 irAEs included pneumonitis, hypothyroidism, colitis, fatigue | [Terranova-Barberio 2020](https://pubmed.ncbi.nlm.nih.gov/32681091/) |
| Entinostat + nivolumab ± ipilimumab (advanced HER2-negative breast / solid tumors) | Tumor CD8/FoxP3 ratio median 4.11 → 9.03 (T0 → T2; +119.7% RATIO, p=0.002, Wilcoxon, n=14 paired); ratio shift required ICI addition (T1 post-entinostat-only median 3.56). Not a Treg-absolute reduction. ORR 16% (incl. CR in TNBC); 4 responders trended toward greater shift (n.s.) | N=33 across 4 dose levels. Treatment-related AEs: fatigue 65%, nausea 41%, anemia 38%, diarrhea 26%, anorexia 26%. Grade 3–4: fatigue 21%, anemia 27%, neutropenia 12%. RP2D entinostat 3 mg weekly + nivolumab 3 mg/kg q2w + ipilimumab 1 mg/kg q6w (max 4) | [Roussos Torres 2021](https://pubmed.ncbi.nlm.nih.gov/34135021/) |
| Azacitidine + panobinostat (AML, BM + PBMC) | TNFR2+ Treg subset (minority of total Tregs) decreased in PBMC and BM after 28-day cycles; associated with increased BM effector IFN-γ and IL-2 and clinical benefit in subset. Numerics not reported (abstract-only). Total FoxP3+ Tregs not the readout | N=14; abstract-only (paper not in PMC). Class panobinostat AEs (cytopenias, GI, QT prolongation per FARYDAK USPI) and azacitidine toxicities expected | [Govindaraj 2014](https://pubmed.ncbi.nlm.nih.gov/24297862/) |

### 6. Standard anti-CTLA-4 (ipilimumab / tremelimumab) — foundational negative result for the Treg-depletion endpoint; motivates Rank 2

**Evidence base.** 8 trials (n with Treg measurement = 233 across the
group; includes foundational papers Huang 2011, Sharma 2019, and
Comin-Anduix 2008). Ipilimumab and tremelimumab do not deplete
intratumoral Tregs in humans: Huang 2011 tumor FOXP3+ density
35→167 cells/mm² (p=0.0029, an *increase*; PMID 21558401), Sharma 2019
across melanoma/prostate/bladder paired biopsies — FoxP3+ increase in
all cohorts (PMID 30054281), Comin-Anduix 2008 PBMC n.s. (PMID 18452610),
Ribas 2009 n.s. tumor (PMID 19118070), Yi 2017 PBMC increase with
chemo+ipi, p=0.012 (PMID 28951518), Penter 2023 marrow Treg expansion
on decitabine+ipi in AML/MDS (PMID 36706355). Hamid 2011 measured
baseline-only biomarker (PMID 22123319); Nancey 2012 is an n=1
enterocolitis case report overclaiming depletion (PMID 22069060).
Skeptic confidence: 1 High (Sharma), 3 Moderate, 3 Low, 1 Very low.

**Likelihood of desired effect.** Low — converging evidence across the
most methodologically rigorous reports in the shieldbreak (Sharma 2019
High confidence; Huang 2011 Moderate) indicates that non-Fc-enhanced
anti-CTLA-4 does not deplete intratumoral Tregs in humans and in
several contexts actively *expands* them. This is the foundational
negative result that motivates the Fc-enhancement program (Rank 2).

**Toxicity profile.** Ipilimumab's irAE profile (colitis, hepatitis,
hypophysitis, pneumonitis, dermatitis, endocrinopathies) is
well-characterized (YERVOY USPI, FDA DailyMed). Tremelimumab's profile
is similar (IMJUDO USPI). Standard-dose irAEs are clinically significant
and rate-limiting.

**Counter-productive mechanisms.** CP severity aggregate: **Low** (6/8
Low, 1 Moderate case-report, 1 High is the decitabine-co-drug confound
in Penter 2023). The aggregate understates the real story because the
*proximal* Treg-depletion mechanism fails in humans — so CP severity is
technically Low (you can't have collateral from a mechanism that isn't
engaging). The flagged class concerns are: (i) **alt-checkpoint
upregulation** — CTLA-4 blockade induces PD-1 and LAG-3 compensatory
expression (external: Huang 2017 *PNAS*; Woo 2012); (ii) **paradoxical
autoimmunity** — irAEs (colitis, hypophysitis) consume immune capacity
in non-tumor tissue (Nancey 2012 case report). Penter 2023's High
severity is a co-drug effect: decitabine expands marrow Tregs via TSDR
demethylation, a finding the authors document directly as an ipilimumab
resistance mechanism — a warning for any DNMTi + anti-CTLA-4
combination rather than a standalone ipi/treme concern.

**Practical considerations.** Both agents are FDA-approved in multiple
indications (ipi 2011, tremelimumab 2022). Widely available, combinable
with anti-PD-1 and platinum chemotherapy. For Treg-depletion PD
endpoints specifically, standard anti-CTLA-4 should not be the tool of
choice — use Fc-enhanced variants (Rank 2) or move to a different class.

**Why this rank.** Foundational, but negative. Included in the ranked
list because the negative result is load-bearing for the rest of the
synthesis — it is the reason Rank 2 exists as a distinct class and the
reason this shieldbreak treats Fc engineering as the reconciling
variable.

**Per-trial detail.**

| Therapeutic agent | Efficacy | Toxicity | Reference |
|---|---|---|---|
| Tremelimumab 15 mg/kg q3mo (metastatic melanoma, paired biopsies) | Tumor FOXP3+ density 35.20 ± 30.06 → 167.35 ± 162.37 cells/mm² post-dose (+375%, p=0.0029 paired, n=19). FOXP3 INCREASED, not depleted; CD8+ TIL increase independent of clinical response. Caveat: paper applied unpaired Mann-Whitney label to paired biopsy data | N=32 enrolled, 19 paired-biopsy. Tremelimumab + ipilimumab class irAEs (grade ≥3) ~20% in pivotal phase 2; per-AE breakdown not in extracted text for this translational paper. DLT-defined events: grade 4 TRAE, grade ≥3 hypersensitivity, grade ≥2 colitis, autoimmune events in critical organs | [Huang 2011](https://pubmed.ncbi.nlm.nih.gov/21558401/) |
| Ipilimumab (advanced melanoma, predictive-biomarker study) | Baseline (NOT longitudinal) FOXP3 quantification only: detected in 75.0% of clinical-benefit pretreatment biopsies vs 36.0% of non-benefit (p=0.014). Not a depletion endpoint — incidental Treg readout | N=82 evaluable across two ipilimumab doses (10 mg/kg vs 3 mg/kg). Drug-related any-grade 82.5% vs 76.2%; grade 3–4 15.0% vs 31.0%. irAE any-grade 55.0% vs 66.7%; grade 3–4 7.5% vs 19.0%. GI most common irAE category. 5 (12.5%) vs 11 (26.2%) discontinued for AE | [Hamid 2011](https://pubmed.ncbi.nlm.nih.gov/22123319/) |
| Ipilimumab or tremelimumab (foundational paired tumor analysis: melanoma, prostate, bladder) | Tumor FOXP3+ INCREASED in all cohorts: ipilimumab melanoma (n=16 post vs 19 untreated, p<0.05), tremelimumab paired melanoma (n=18, p<0.05), no reduction in bladder (n=9) or prostate (n=16). CyTOF orthogonal validation in n=5 paired melanoma. Densities figure-only | N=45 across cohorts; this is a translational tumor-IHC paper without primary AE reporting. Standard ipilimumab/tremelimumab irAE profiles per YERVOY and IMJUDO USPIs apply | [Sharma 2019](https://pubmed.ncbi.nlm.nih.gov/30054281/) |
| Tremelimumab (melanoma, PBMC PD with detailed flow) | PBMC FoxP3 mRNA showed no statistically significant change pre vs post-dose (n=8 evaluable of 13); Treg functional assay not performed (insufficient cells from 40 mL draws) | N=29 reported on this trial cohort; documented G2/G3 toxicities included diarrhea G2, hepatitis G3, acne rosacea G2, colitis G3, panhypopituitarism (2 cases, hypophysitis), uveitis, leukocytoclastic vasculitis. Per-patient case-list rather than aggregated rates | [Comin-Anduix 2008](https://pubmed.ncbi.nlm.nih.gov/18452610/) |
| Ipilimumab or tremelimumab (retrospective biopsy analysis, melanoma) | n=15 biopsies from 7 patients; no consistent FoxP3 reduction; slight FoxP3+ increase in 2/3 paired responders; IDO associated with non-response. Numerics not extractable (paper not in PMC OA) | N=7; abstract-only AE detail. Standard anti-CTLA-4 irAEs apply | [Ribas 2009](https://pubmed.ncbi.nlm.nih.gov/19118070/) |
| Ipilimumab (case series of patients with severe enterocolitis) | Lamina-propria FoxP3+ Treg "profound long-lasting depletion" reported qualitatively in n=4; numeric density values not extractable (paper not in PMC OA). Title overclaims for case-report-level evidence | N=4 case series — all by definition had severe (grade ≥3) ipilimumab-induced enterocolitis, which is the inclusion criterion. Not informative for class-level toxicity rates | [Nancey 2012](https://pubmed.ncbi.nlm.nih.gov/22069060/) |
| Neoadjuvant chemotherapy + ipilimumab (early-stage NSCLC) | PBMC: median Treg frequency INCREASED slightly by +1.05% (V1 chemo-alone → V3 post-ipi), p=0.012 — significant but tiny magnitude and opposite direction from depletion. Tumor: no pre-treatment biopsy, change not assessable | N=24; treatment-related grade 1–2 AEs in 54%, grade 3–4 in 46%, no treatment-related deaths. Most AEs attributable to carboplatin/paclitaxel. Ipilimumab-attributed irAEs: grade 2 pneumonitis 4%, grade 3 adrenal insufficiency 17%, diarrhea/colitis grade 1–2 25% + grade 3 13% | [Yi 2017](https://pubmed.ncbi.nlm.nih.gov/28951518/) |
| Decitabine + ipilimumab (R/R AML/MDS, BM scRNA-seq + mIF) | Bone-marrow CD3+FOXP3+ density INCREASED post-ipilimumab (qualitative; baseline not numerically reported, no p-value cited); authors interpret BM Treg expansion as ipilimumab-resistance mechanism and explicitly suggest combining with Treg-depleting strategies | N=18; AE quantitative data not in extracted PMC text. Decitabine + ipilimumab combination toxicity (cytopenias, irAEs) per parent ETCTN/CTEP 10026 trial | [Penter 2023](https://pubmed.ncbi.nlm.nih.gov/36706355/) |

## Classes examined but not ranked (counterexamples and thin-evidence classes)

Seven additional classes were surveyed and deliberately omitted from the
ranked list:

- **Non-α IL-2 variants (nemvaleukin, bempegaldesleukin)** — 6 trials
  (Bentebibel 2019 PMID 30988166; Diab 2020 PMID 32439653; Vaishampayan
  2024 PMID 39567211; Gogas 2024 PMID 39025948; Calvo 2025 PMID
  40759440; Piha-Paul 2025 PMID 40990800). These *expand* Tregs
  absolutely, with a "favorable-ratio" framing that did not hold up:
  Gogas 2024 PIVOT-02 showed ~8–10× absolute Treg expansion with
  bempegaldesleukin (+800%) and the PIVOT-IO phase 3 failed. Mechanism
  does not fit the shieldbreak's target effect.

- **Anti-CD25 daclizumab** — 2 trials (Mahnke 2007 PMID 17315189; Morse
  2008 PMID 18519811). Reported reductions are confounded by
  **CD25-based gating during CD25-targeting therapy** (same structural
  issue as DD). Not enough confound-resistant data to rank.

- **Iberdomide / CELMoDs** — 2 studies (Lipsky 2022 PMID 35477518; Amatangelo
  2024 PMID 38776914). Iberdomide/mezigdomide degrade Ikaros/Aiolos
  rather than Helios/IKZF2, and therefore *expand* Tregs (e.g., +104.9%
  at 0.45 mg in Lipsky 2022, p<0.001). Wrong direction.

- **DNMT inhibitors / HMAs as monotherapy** — Han 2021 low-dose
  decitabine in ITP (PMID 33876188) and Penter 2023 decitabine+ipi (PMID
  36706355, rolled into anti-CTLA-4 above) both show DNMTi *increases*
  Treg quantity/function. Counterexample direction in isolation;
  Govindaraj 2014 aza+panobinostat is the exception only because the
  HDACi partner drives the direction.

- **Anti-GITR** — 2 trials (Piha-Paul 2021 GWN323 PMID 34389618; Davar
  2022 TRX518 PMID 35499569). Both Low confidence, programs
  deprioritized by sponsors; insufficient evidence to rank.

- **Anti-TIGIT** — 1 trial with Treg readout (Guan 2024 tiragolumab PMID
  38418879). Single translational substudy, PBMC-only, Low confidence;
  not enough to rank.

- **PI3Kδ inhibitors** — 1 trial (Gadi 2022 idelalisib in CLL, n=9 PBMC;
  PMID 35170759). Very-small-n, Low confidence.

## Ranked prioritization

| Rank | Intervention | Likelihood of effect | Toxicity burden | Counter-productive MoA | Overall |
|---:|---|---|---|---|---|
| 1 | Anti-CCR4 (mogamulizumab) | High in CCR4+ eTreg subset (Fujikawa, Jinushi, Roelens concordant) | Moderate (cutaneous, infusion, post-allo-HSCT signal) | **High** (CCR4+ CD8 effector-memory collateral; 2/4 paper-internal, 4/4 replicated) | **Strongest, most-replicated depletion with direct tumor evidence — but pair with effector rescue if the goal is anti-tumor benefit** |
| 2 | Fc-enhanced anti-CTLA-4 | Moderate (Ager randomized control; Chand consistent) | Moderate-to-high (class-level irAE + FcγR-engagement signal) | **Moderate** (tdLN Treg expansion, ADCC on activated CTLA-4-high effectors; 2/2) | **Mechanism-rescue; thin but directionally clean; CP profile narrows but does not close the Rank-1 gap** |
| 3 | Low-dose metronomic cyclophosphamide | Moderate (schedule-dependent; p<0.0001 in Ghiringhelli, null in Audia) | Low-to-moderate (generic, well-characterized) | **Low** (metronomic regimen is the cleanest dose-selective mechanism in the set; single-IV is Moderate) | **Cheap, accessible, schedule-sensitive, low collateral — strong combination backbone** |
| 4 | Denileukin diftitox | Low-to-moderate after CD25-gating discount | Moderate (capillary-leak, supply instability) | **Moderate** (CD25+ activated-effector collateral; vaccine-priming window and IFNα-CD25 interaction elevate specific combinations) | **Large literature but structurally confounded; FoxP3-mRNA readouts needed; avoid priming-overlap scheduling** |
| 5 | Class-I HDAC inhibitors | Moderate in oncology, unfavorable in HIV/cART (context-dependent) | Moderate (cytopenias; QT for panobinostat) | **Moderate** (class-I-selective entinostat bounded Low; pan-HDAC and DNMTi-partner cases Moderate-High) | **Plausible; context- and selectivity-sensitive; entinostat is the cleanest CP profile in class** |
| 6 | Standard anti-CTLA-4 | Very low for the Treg-depletion endpoint specifically | Moderate-to-high (standard irAE profile) | **Low** (proximal mechanism fails so collateral is moot; Penter 2023 decitabine-co-drug is the High outlier and a combination-specific warning) | **Foundational negative result; motivates Rank 2; not the tool for this endpoint** |

The **Counter-productive MoA** column summarizes the skeptic-assessed
severity of mechanism-level risks that the intervention may undermine
the shieldbreak's target effect even when its proximal endpoint is
met. It is distinct from Toxicity burden (which is about patient-level
AEs). A severe counter-productive MoA pulls the Overall rating down
even when Likelihood of effect is high. Severity aggregates per-group
as the modal paper-level severity, bumped up one step when a
paper-internal High is replicated across ≥2 papers or documents a
wrong-direction mechanism in the intended context. Wrong-direction
context-outliers (e.g., Brinkmann panobinostat in HIV; Penter
decitabine co-drug) are footnoted rather than allowed to move the
aggregate.

## Caveats

- **Total-n is small for several ranked groups.** Fc-enhanced
  anti-CTLA-4 has n=36 across 2 trials; cyclophosphamide positive
  report is n=9; mogamulizumab solid-tumor tumor data is n=16
  (Jinushi 2025). Rankings reflect magnitude × confidence, not
  magnitude alone.
- **CD25-gating confound is pervasive** across the DD and anti-CD25
  literature. Any future Treg-PD endpoint in a CD25-targeting program
  should use FoxP3 mRNA, TSDR methylation, or Helios/IKZF2 readouts.
- **Compartment dissociation is pervasive.** Tumor-Treg depletion
  often coexists with tdLN-Treg expansion (Ager 2026) or with skin
  expansion (Roelens 2022 mixed). PBMC-only data should not be
  extrapolated to tumor.
- **Industry sponsorship** is flagged by the skeptic for Chand 2024
  (botensilimab) and several IL-2-variant trials; this is a caveat,
  not a disqualifier.
- **One extraction-fidelity discrepancy** carried over from the
  screener pass: Huang 2011 applied a Mann-Whitney test label to
  paired pre/post biopsy data. The skeptic flagged it; the directional
  conclusion is unaffected.
- **Data-quality note for Roussos Torres 2021:** the `pct_change` of
  +119.7% reflects a CD8:FoxP3 *ratio* shift, not a Treg-specific
  change — read the underlying biology, not the field value.
- **What would change the ranking.**
  - An independent (non-sponsor) replication of Fc-enhanced
    anti-CTLA-4 intratumoral depletion would plausibly move Rank 2
    above Rank 1.
  - A second confound-resistant (FoxP3 mRNA / TSDR) DD study with
    concordant positive direction would move Rank 4 up.
  - A randomized HDACi ± ICI study with a pre-specified intratumoral
    Treg endpoint would sharpen Rank 5 considerably.
  - A head-to-head of metronomic oral vs low-dose IV cyclophosphamide
    with matched Treg PD would resolve the schedule question at Rank 3.
- **Shared CP pattern — CD25+ effector collateral** spans Rank 4
  (denileukin diftitox) and the non-ranked anti-CD25 daclizumab class.
  Any CD25-targeting Treg-depletion program should assume the readout
  is structurally confounded *and* that activated effectors are being
  co-depleted in the priming window. Use FoxP3 mRNA / TSDR and schedule
  around (not over) effector priming.
- **Shared CP pattern — beneficial-effector collateral via
  surface-marker promiscuity** is the dominant concern for the two
  highest-likelihood classes: anti-CCR4 (CCR4+ CD8 central-memory) and
  Fc-enhanced anti-CTLA-4 (CTLA-4-upregulating activated effectors). If
  the target effect is re-scoped from "proximal Treg depletion" toward
  "restored anti-tumor immunity," this shared pattern is load-bearing
  against both top ranks and favors Rank 3 (metronomic
  cyclophosphamide) as a combination backbone.
- **CP aggregation rule used here:** modal per-group severity, bumped
  up one step when a paper-internal High is replicated across ≥2
  papers or documents a clearly wrong-direction mechanism in the
  intended context. Wrong-direction outliers in a discordant context
  (Brinkmann panobinostat in HIV; Penter decitabine-co-drug) are
  footnoted rather than allowed to move the aggregate.
- **Rankings reflect Target-effect-as-written** ("reduce Treg
  abundance/frequency/dominance/suppressive function"). If the Target
  effect is re-scoped toward anti-tumor benefit, CP severity should
  weigh more heavily and Rank 1 narrows substantially against Rank 2
  and Rank 3.

## Sources

- Trial data and critiques: `data/shieldbreaks/treg-depletion/trials.jsonl`
  and `data/shieldbreaks/treg-depletion/critiques.jsonl`; per-trial
  citations below are also linked from the main table.
- Ager CR et al. 2026 (BMS-986218+ADT, prostate) —
  [PMID 41759531](https://pubmed.ncbi.nlm.nih.gov/41759531/)
- Atchison E et al. 2010 (DD + HD IL-2, RCC) —
  [PMID 20664355](https://pubmed.ncbi.nlm.nih.gov/20664355/)
- Attia P et al. 2005 (DD, melanoma, null) —
  [PMID 16224276](https://pubmed.ncbi.nlm.nih.gov/16224276/)
- Audia S et al. 2007 (single-IV cyclophosphamide + BCG, null) —
  [PMID 17956583](https://pubmed.ncbi.nlm.nih.gov/17956583/)
- Amatangelo M et al. 2024 (iberdomide + dex, myeloma) —
  [PMID 38776914](https://pubmed.ncbi.nlm.nih.gov/38776914/)
- Bentebibel SE et al. 2019 (bempegaldesleukin, PD) —
  [PMID 30988166](https://pubmed.ncbi.nlm.nih.gov/30988166/)
- Brinkmann CR et al. 2018 (panobinostat, HIV/cART) —
  [PMID 29468194](https://pubmed.ncbi.nlm.nih.gov/29468194/)
- Calvo E et al. 2025 (nemvaleukin monotherapy) —
  [PMID 40759440](https://pubmed.ncbi.nlm.nih.gov/40759440/)
- Chand D et al. 2024 (botensilimab+balstilimab, MSS mCRC) —
  [PMID 39083809](https://pubmed.ncbi.nlm.nih.gov/39083809/)
- Comin-Anduix B et al. 2008 (tremelimumab) —
  [PMID 18452610](https://pubmed.ncbi.nlm.nih.gov/18452610/)
- Dannull J et al. 2005 (DD + DC vaccine, RCC) —
  [PMID 16308572](https://pubmed.ncbi.nlm.nih.gov/16308572/)
- Davar D et al. 2022 (TRX518 anti-GITR) —
  [PMID 35499569](https://pubmed.ncbi.nlm.nih.gov/35499569/)
- Diab A et al. 2020 (bempegaldesleukin + nivolumab) —
  [PMID 32439653](https://pubmed.ncbi.nlm.nih.gov/32439653/)
- Fujikawa K et al. 2023 (mogamulizumab, PBMC) —
  [PMID 37729184](https://pubmed.ncbi.nlm.nih.gov/37729184/)
- Gadi D et al. 2022 (idelalisib, CLL) —
  [PMID 35170759](https://pubmed.ncbi.nlm.nih.gov/35170759/)
- Geskin LJ et al. 2018 (DD, CTCL) —
  [PMID 29204699](https://pubmed.ncbi.nlm.nih.gov/29204699/)
- Ghiringhelli F et al. 2007 (metronomic cyclophosphamide) —
  [PMID 16960692](https://pubmed.ncbi.nlm.nih.gov/16960692/)
- Gogas H et al. 2024 (bempegaldesleukin + nivolumab, PIVOT-02) —
  [PMID 39025948](https://pubmed.ncbi.nlm.nih.gov/39025948/)
- Gordon MJ et al. 2025 (mogamulizumab + rhIL-15) —
  [PMID 40546724](https://pubmed.ncbi.nlm.nih.gov/40546724/)
- Govindaraj C et al. 2014 (azacitidine + panobinostat, AML) —
  [PMID 24297862](https://pubmed.ncbi.nlm.nih.gov/24297862/)
- Guan X et al. 2024 (tiragolumab+atezolizumab, anti-TIGIT) —
  [PMID 38418879](https://pubmed.ncbi.nlm.nih.gov/38418879/)
- Gwin WR et al. 2025 (DD / E7777 combo, breast) —
  [PMID 40006664](https://pubmed.ncbi.nlm.nih.gov/40006664/)
- Hamid O et al. 2011 (ipilimumab baseline biomarker) —
  [PMID 22123319](https://pubmed.ncbi.nlm.nih.gov/22123319/)
- Han P et al. 2021 (low-dose decitabine, ITP) —
  [PMID 33876188](https://pubmed.ncbi.nlm.nih.gov/33876188/)
- Huang RR et al. 2011 (tremelimumab, melanoma) —
  [PMID 21558401](https://pubmed.ncbi.nlm.nih.gov/21558401/)
- Jinushi K et al. 2025 (mogamulizumab+nivo, neoadjuvant) —
  [PMID 40180420](https://pubmed.ncbi.nlm.nih.gov/40180420/)
- Liao JB et al. 2024 (intraperitoneal DD, ovarian) —
  [PMID 39362046](https://pubmed.ncbi.nlm.nih.gov/39362046/)
- Lipsky PE et al. 2022 (iberdomide, SLE) —
  [PMID 35477518](https://pubmed.ncbi.nlm.nih.gov/35477518/)
- Luke JJ et al. 2016 (DD + gp100 vaccine, melanoma) —
  [PMID 27330808](https://pubmed.ncbi.nlm.nih.gov/27330808/)
- Mahnke K et al. 2007 (daclizumab) —
  [PMID 17315189](https://pubmed.ncbi.nlm.nih.gov/17315189/)
- Morse MA et al. 2008 (daclizumab + CEA vaccine) —
  [PMID 18519811](https://pubmed.ncbi.nlm.nih.gov/18519811/)
- Nancey S et al. 2012 (ipi + enterocolitis, case report) —
  [PMID 22069060](https://pubmed.ncbi.nlm.nih.gov/22069060/)
- Penter L et al. 2023 (decitabine+ipilimumab, AML/MDS) —
  [PMID 36706355](https://pubmed.ncbi.nlm.nih.gov/36706355/)
- Piha-Paul SA et al. 2021 (GWN323 anti-GITR ± spartalizumab) —
  [PMID 34389618](https://pubmed.ncbi.nlm.nih.gov/34389618/)
- Piha-Paul SA et al. 2025 (nemvaleukin, less-frequent IV) —
  [PMID 40990800](https://pubmed.ncbi.nlm.nih.gov/40990800/)
- Pili R et al. 2017 (entinostat + HD IL-2, RCC) —
  [PMID 28939740](https://pubmed.ncbi.nlm.nih.gov/28939740/)
- Ribas A et al. 2009 (ipi/treme retrospective, melanoma) —
  [PMID 19118070](https://pubmed.ncbi.nlm.nih.gov/19118070/)
- Roelens M et al. 2022 (mogamulizumab, Sézary) —
  [PMID 35041763](https://pubmed.ncbi.nlm.nih.gov/35041763/)
- Roussos Torres ET et al. 2021 (entinostat+nivo) —
  [PMID 34135021](https://pubmed.ncbi.nlm.nih.gov/34135021/)
- Sharma A et al. 2019 (ipi/treme tumor FOXP3, foundational) —
  [PMID 30054281](https://pubmed.ncbi.nlm.nih.gov/30054281/)
- Terranova-Barberio M et al. 2020 (vorinostat+tamoxifen+pembro) —
  [PMID 32681091](https://pubmed.ncbi.nlm.nih.gov/32681091/)
- Thibodeaux SR et al. 2021 (DD + IFNα, ovarian) —
  [PMID 33771857](https://pubmed.ncbi.nlm.nih.gov/33771857/)
- Vaishampayan UN et al. 2024 (nemvaleukin monotherapy) —
  [PMID 39567211](https://pubmed.ncbi.nlm.nih.gov/39567211/)
- Yi JS et al. 2017 (chemo+ipilimumab, NSCLC) —
  [PMID 28951518](https://pubmed.ncbi.nlm.nih.gov/28951518/)
- FDA prescribing information — POTELIGEO (mogamulizumab), YERVOY
  (ipilimumab), IMJUDO (tremelimumab), ONTAK / E7777 / I-ONTAK
  (denileukin diftitox), ZOLINZA (vorinostat), FARYDAK (panobinostat),
  cyclophosphamide generic USPI — all via
  [DailyMed](https://dailymed.nlm.nih.gov/dailymed/).

---
*This summary is an evidence-synthesis aid for research planning. It
does not constitute clinical advice and must not be used to guide
patient care.*
