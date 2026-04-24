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

**Practical considerations.** Both agents are investigational
(botensilimab AGEN1181 and BMS-986218 are in active clinical development
as of 2026). Industry-controlled supply; academic access primarily
through sponsored trials. Combinable with anti-PD-1 and ADT as
demonstrated.

**Why this rank.** The strongest mechanism-rescue story in the dataset
and the most rigorous intratumoral randomized comparison (Ager 2026),
but total n across the class is small and single-vendor; one more
replication outside the sponsors would shift this to Rank 1 territory.

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

| Rank | Intervention | Likelihood of effect | Toxicity burden | Overall |
|---:|---|---|---|---|
| 1 | Anti-CCR4 (mogamulizumab) | High in CCR4+ eTreg subset (Fujikawa, Jinushi, Roelens concordant) | Moderate (cutaneous, infusion, post-allo-HSCT signal) | **Strongest, most-replicated depletion with direct tumor evidence** |
| 2 | Fc-enhanced anti-CTLA-4 | Moderate (Ager randomized control; Chand consistent) | Moderate-to-high (class-level irAE + FcγR-engagement signal) | **Mechanism-rescue; thin but directionally clean; watch for independent replication** |
| 3 | Low-dose metronomic cyclophosphamide | Moderate (schedule-dependent; p<0.0001 in Ghiringhelli, null in Audia) | Low-to-moderate (generic, well-characterized) | **Cheap, accessible, schedule-sensitive — good combination backbone** |
| 4 | Denileukin diftitox | Low-to-moderate after CD25-gating discount | Moderate (capillary-leak, supply instability) | **Large literature but structurally confounded; FoxP3-mRNA readouts needed** |
| 5 | Class-I HDAC inhibitors | Moderate in oncology, unfavorable in HIV/cART (context-dependent) | Moderate (cytopenias; QT for panobinostat) | **Plausible; context-sensitive; no single-agent replication yet** |
| 6 | Standard anti-CTLA-4 | Very low for the Treg-depletion endpoint specifically | Moderate-to-high (standard irAE profile) | **Foundational negative result; motivates Rank 2; not the tool for this endpoint** |

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
