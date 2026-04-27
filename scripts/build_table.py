#!/usr/bin/env python3
"""
Build the per-shieldbreak trial-table Markdown page from trials.jsonl.

Usage:
    python scripts/build_table.py <slug>

For the `treg-depletion` shieldbreak this renders according to
styles/treg-depletion/STYLE.md:
- Booktabs-style table with `.pd-table` class
- `.pill` badges for success_flag, tissue, assay, change_mechanism
- Signed change colors for pct_change with unicode arrow
- Row grouping by study_id with left-edge stripe (cycle of 6)
- Two-tier column visibility (primary + expanded behind toggle)
- Tissue filter chip row with inline JS
- Side-list for reviews.jsonl rendered as trailing section

Pure-Python; no LLM calls, no external deps.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from html import escape
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "shieldbreaks"
DOCS_DIR = REPO_ROOT / "docs" / "shieldbreaks"
STYLE_DIR = REPO_ROOT / "styles"


# ---------- collapsible-section wrapper ----------


_H2_RE = re.compile(r"^## (?!#)")


def wrap_sections_in_details(
    markdown_text: str,
    skip_headings: frozenset[str] = frozenset(),
) -> str:
    """Wrap each `##` section's body in a collapsed `<details>` block.

    The `##` heading stays visible above the collapsed body (so the
    right-hand TOC and in-page anchors keep working); a single
    Show/hide summary button below each heading toggles visibility of
    that section's content. Content before the first `##` (title,
    backlink, last-updated line) is left untouched.

    Sections whose heading text (after `## `) is in `skip_headings`
    are left bare — no `<details>` wrapper, no toggle button.
    """
    lines = markdown_text.split("\n")
    out: list[str] = []
    in_fence = False
    section_buf: list[str] = []
    in_section = False  # False, or True (wrap), or "skip" (passthrough)

    def flush() -> None:
        nonlocal section_buf, in_section
        if in_section is False:
            return
        while section_buf and section_buf[-1].strip() == "":
            section_buf.pop()
        if in_section == "skip":
            out.extend(section_buf)
            out.append("")
        else:
            out.append('<details class="sb-section" open markdown="1">')
            out.append("<summary>Show / hide</summary>")
            out.append("")
            out.extend(section_buf)
            out.append("")
            out.append("</details>")
            out.append("")
        section_buf = []
        in_section = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence

        is_h2 = not in_fence and bool(_H2_RE.match(line))

        if is_h2:
            flush()
            out.append(line)
            out.append("")
            heading_text = line[3:].strip()
            in_section = "skip" if heading_text in skip_headings else True
        elif in_section is not False:
            section_buf.append(line)
        else:
            out.append(line)

    flush()
    return "\n".join(out)


# ---------- helpers ----------


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def safe(v, default: str = "—") -> str:
    if v is None or v == "":
        return default
    return str(v)


def classify_success(row: dict) -> tuple[str, str]:
    """Map (depletion_success, change_direction, change_mechanism) -> (sf-class, label)."""
    sig = (row.get("change_significance") or "").lower()
    ds = (row.get("depletion_success") or "").lower()
    cd = (row.get("change_direction") or "").lower()
    cm = (row.get("change_mechanism") or "").lower()

    # For repolarization / expansion-with-repolarization, an "increase" in M1
    # markers is the intended outcome, not an adverse signal — don't mis-label.
    repol_mechs = {"repolarization", "expansion-with-repolarization"}
    if cd == "increase" and cm not in ({"expansion-with-ratio-shift"} | repol_mechs):
        return ("sf-increase", "increase")
    if ds == "succeeded" and (
        "p=" in sig or "significant" in sig or "p<" in sig or "reported" in sig
    ):
        if cm in repol_mechs:
            return ("sf-sig-reduction", "repolarized")
        return ("sf-sig-reduction", "significant reduction")
    if ds == "partial" or "inconsistent" in sig or "trend" in sig:
        return ("sf-nonsig-trend", "nonsignificant trend")
    if ds == "failed" or cm == "null-result":
        return ("sf-null-result", "null result")
    if ds == "not-assessed":
        return ("sf-nonsig-trend", "ratio-shift only")
    return ("sf-null-result", "—")


def mech_chip(change_mechanism: str | None) -> str:
    if not change_mechanism:
        return ""
    cm = change_mechanism.lower()
    mapping = {
        # treg-depletion mechanisms
        "absolute-reduction": ("mech-depletion", "depletion"),
        "ratio-shift": ("mech-ratio-only", "ratio only"),
        "expansion-with-ratio-shift": ("mech-frac-shift", "fraction shift"),
        "functional-impairment-only": ("mech-frac-shift", "functional only"),
        "null-result": ("mech-null", "null"),
        # tam-depletion additions
        "repolarization": ("mech-neutral", "repolarization"),
        "expansion-with-repolarization": ("mech-neutral", "expansion + repol"),
    }
    cls, label = mapping.get(cm, ("mech-neutral", cm))
    return f'<span class="pill {cls}">{escape(label)}</span>'


def tissue_chip(tissue: str | None) -> str:
    if not tissue:
        return "—"
    t = tissue.lower()
    cls_map = {
        "pbmc": "tis-pbmc",
        "tumor": "tis-tumor",
        "tdln": "tis-tdln",
        "bone-marrow": "tis-bm",
        "ascites": "tis-ascites",
        "pleural-effusion": "tis-ascites",
        "csf": "tis-other",
        "skin": "tis-skin",
        "other": "tis-other",
    }
    cls = cls_map.get(t, "tis-other")
    return f'<span class="pill {cls}">{escape(tissue)}</span>'


def assay_chip(gating_quality: str | None, readout_type: str | None) -> str:
    """STYLE.md defines assay chips; our schema stores gating_quality.
    treg-depletion values (FOXP3-confirmed, functional-assay, surface-only, mixed, unclear)
    and tam-depletion values (CD68-CD163-based, CD68-CD206-based, CD14-CD16-based,
    CD68-MHCII-based, scRNA-macrophage-cluster, mIF-multiplex, CyTOF, single-marker-only,
    mixed-or-unclear) are all accepted.
    """
    gq = (gating_quality or "").strip()
    rt = (readout_type or "").strip()

    # readout-type wins when present (both shieldbreaks)
    if rt == "suppressive-function":
        return f'<span class="pill assay-flow">{escape("suppress")}</span>'
    if rt == "phagocytosis-function":
        return f'<span class="pill assay-flow">{escape("phago")}</span>'
    if rt == "scRNA-cluster-shift":
        return f'<span class="pill assay-scrna">{escape("scRNA")}</span>'

    # gating-quality driven
    gq_map = {
        # treg-depletion
        "FOXP3-confirmed": ("assay-flow", "flow"),
        "surface-only": ("assay-flow", "flow"),
        "functional-assay": ("assay-flow", "flow+fn"),
        "mixed": ("assay-flow", "flow"),
        "unclear": ("assay-flow", "flow"),
        # tam-depletion
        "CD68-CD163-based": ("assay-ihc", "IHC"),
        "CD68-CD206-based": ("assay-ihc", "IHC"),
        "CD68-MHCII-based": ("assay-ihc", "IHC"),
        "CD14-CD16-based": ("assay-flow", "flow"),
        "scRNA-macrophage-cluster": ("assay-scrna", "scRNA"),
        "mIF-multiplex": ("assay-mif", "mIF"),
        "CyTOF": ("assay-cytof", "CyTOF"),
        "single-marker-only": ("assay-ihc", "IHC"),
        "mixed-or-unclear": ("assay-flow", "mixed"),
    }
    cls, label = gq_map.get(gq, ("assay-flow", "flow"))
    return f'<span class="pill {cls}">{escape(label)}</span>'


def _format_pct(v: float) -> str:
    """Trim trailing zeros so 61.0 → "61", 56.3 → "56.3"."""
    return f"{v:.1f}".rstrip("0").rstrip(".")


def render_change_cell(row: dict) -> tuple[str, str]:
    """Render the Treg change cell. Prefers typed pct_change; falls back to
    directional labeling from change_direction + change_significance.
    Returns (rendered_html, sort_key)."""
    pct = row.get("pct_change")
    if pct is not None:
        v = float(pct)
        cls = "change-neg" if v < 0 else "change-pos"
        arrow = "↓" if v < 0 else "↑"
        sign = "−" if v < 0 else "+"
        return (
            f'<span class="{cls}">{arrow} {sign}{_format_pct(abs(v))}%</span>',
            f"{v:+09.2f}",
        )

    direction = (row.get("change_direction") or "").lower()
    sig = (row.get("change_significance") or "").lower()
    is_significant = (
        any(tok in sig for tok in ("p<", "p=", "significant"))
        and "n.s." not in sig
        and "not tested" not in sig
    )

    if direction == "decrease":
        label = "↓ sig." if is_significant else "↓ qual."
        return (f'<span class="change-neg-qual">{label}</span>', "-0.5")
    if direction == "increase":
        label = "↑ sig." if is_significant else "↑ qual."
        return (f'<span class="change-pos-qual">{label}</span>', "+0.5")
    if direction == "no-change":
        return ('<span class="change-null">≈ n.s.</span>', "0.0")
    if direction == "mixed":
        return ('<span class="change-null">mixed</span>', "0.1")
    return ("—", "")


# bias tags that represent structural confounds / methodological red flags (amber).
# everything else renders as a neutral caveat.
_BIAS_CONFOUND_TAGS = {
    "cd25-gating-confound",
    "surface-marker-gating",
    "foxp3-ihc-single-marker",
    "spin-abstract-vs-results",
    "baseline-imbalance",
    "mechanism-endpoint-not-measured",
    "underpowered",
    "responder-subset-reporting",
}

_BIAS_TAG_TOOLTIPS = {
    "cd25-gating-confound": "CD25-based Treg gating during CD25-targeting therapy (structural confound)",
    "surface-marker-gating": "Treg defined by surface markers only (no FoxP3 confirmation)",
    "foxp3-ihc-single-marker": "Single-marker FOXP3 IHC (can't distinguish Tregs from activated effectors)",
    "open-label": "Unblinded trial",
    "single-arm-no-control": "No concurrent control arm",
    "small-n": "N < 10 evaluable for Treg readout",
    "very-small-n": "N < 5 evaluable for Treg readout",
    "underpowered": "No power calculation for Treg endpoint or clearly underpowered",
    "figure-only-data": "Key numeric lives in a figure panel, no text quantification",
    "abstract-only": "Full text not accessed; critique is from abstract + registry",
    "responder-subset-reporting": "Headline magnitude reported only in responder subset",
    "no-multiplicity-correction": "Multiple endpoints, no Bonferroni/FDR/pre-specified hierarchy",
    "exploratory-endpoint": "Treg readout is exploratory/incidental, not pre-specified",
    "retrospective-analysis": "Retrospective analysis on archival cohort",
    "pbmc-only-generalized": "Tumor-compartment inferences from PBMC-only data",
    "compartment-dissociation": "Opposite-direction results across compartments",
    "industry-sponsored": "Study funded by sponsor of investigational agent",
    "author-coi-sponsor": "≥1 author has financial relationship with sponsor",
    "baseline-imbalance": "Randomization did not balance a prognostic feature",
    "schedule-dependent": "Efficacy reported as schedule-dependent",
    "dose-mixed-analysis": "Results pooled across doses with heterogeneity flagged",
    "short-follow-up": "Follow-up too short to assess durability",
    "spin-abstract-vs-results": "Abstract framing diverges from what results support",
    "mechanism-endpoint-not-measured": "Presumed mechanism affects function but paper only measures counts (or vice versa)",
    "case-report-n-of-few": "Case report or small case series with no trial-level analysis",
}


def _confidence_pill(conf: str | None) -> str:
    if not conf:
        return "—"
    slug = conf.lower().replace(" ", "-")  # "Very low" -> "very-low"
    return f'<span class="pill conf-{escape(slug)}">{escape(conf)}</span>'


def _rob_pill(rating: str | None, tool: str | None) -> str:
    if not rating:
        return ""
    slug = rating.lower().replace(" ", "-").replace("—", "").strip()
    if slug.startswith("not-amenable"):
        slug = "na"
    tooltip = f"Risk of bias ({tool or 'RoB'})" if tool else "Risk of bias"
    return f'<span class="pill rob-{escape(slug)}" title="{escape(tooltip)}">{escape(rating)}</span>'


def _bias_flag_pills(flags: list[str] | None, limit: int = 4) -> str:
    if not flags:
        return ""
    parts: list[str] = []
    shown = flags[:limit]
    extra = len(flags) - len(shown)
    for tag in shown:
        cls = "bias-confound" if tag in _BIAS_CONFOUND_TAGS else "bias-caveat"
        tooltip = _BIAS_TAG_TOOLTIPS.get(tag, tag)
        parts.append(
            f'<span class="pill bias-flag {cls}" title="{escape(tooltip)}">{escape(tag)}</span>'
        )
    if extra > 0:
        parts.append(f'<span class="pill bias-flag bias-caveat" title="{extra} more">+{extra}</span>')
    return '<div class="bias-flags">' + "".join(parts) + "</div>"


def build_confidence_cell(critique: dict | None) -> str:
    if not critique:
        return "—"
    return _confidence_pill(critique.get("per_trial_confidence"))


def build_bias_cell(critique: dict | None) -> str:
    if not critique:
        return "—"
    rob = _rob_pill(critique.get("rob_rating"), critique.get("rob_tool"))
    flags = _bias_flag_pills(critique.get("bias_flags"))
    if not rob and not flags:
        return "—"
    return (rob + flags) or "—"


def cite_links(row: dict, critique_pmids: set[str] | None = None) -> str:
    links: list[str] = []
    if row.get("pmid"):
        links.append(
            f'<a href="https://pubmed.ncbi.nlm.nih.gov/{escape(row["pmid"])}/">PMID</a>'
        )
    if row.get("pmcid"):
        links.append(
            f'<a href="https://europepmc.org/article/PMC/{escape(row["pmcid"].replace("PMC",""))}">PMCID</a>'
        )
    if row.get("doi"):
        links.append(f'<a href="https://doi.org/{escape(row["doi"])}">DOI</a>')
    if row.get("nct_id"):
        links.append(
            f'<a href="https://clinicaltrials.gov/study/{escape(row["nct_id"])}">NCT</a>'
        )
    if critique_pmids and row.get("pmid") and row["pmid"] in critique_pmids:
        links.append(
            f'<a class="critique-link" href="critiques/{escape(row["pmid"])}.md">critique</a>'
        )
    if not links:
        return "—"
    return '<span class="cite-links">' + " ".join(links) + "</span>"


def report_cell(row: dict) -> str:
    """Compact authorship + venue + year block."""
    first = row.get("first_author") or ""
    last = row.get("last_author") or ""
    if first and last and first != last:
        authors = f"{escape(first)} &middot;&middot;&middot; {escape(last)}"
    elif first:
        authors = escape(first)
    else:
        authors = "—"
    journal = row.get("journal") or ""
    year = row.get("year")
    year_str = str(year) if year else ""
    venue_parts = [p for p in (escape(journal) if journal else "", year_str) if p]
    venue = ", ".join(venue_parts)
    return (
        f'<div class="report-cell">'
        f'<div class="report-authors">{authors}</div>'
        + (f'<div class="report-venue">{venue}</div>' if venue else "")
        + "</div>"
    )


def intervention_cell(row: dict) -> str:
    primary = safe(row.get("intervention"))
    combo = row.get("combo_partners")
    if combo and combo.strip() and combo.lower() != "null":
        return f'{escape(primary)}<span class="combo">{escape(combo)}</span>'
    return escape(primary)


def build_row_html(
    row: dict,
    group_idx: int,
    critique_pmids: set[str] | None = None,
    critiques_by_pmid: dict[str, dict] | None = None,
) -> str:
    pct_html, _ = render_change_cell(row)
    sf_cls, sf_label = classify_success(row)
    sf_badge = f'<span class="pill {sf_cls}">{escape(sf_label)}</span>'
    mech_html = mech_chip(row.get("change_mechanism"))

    tissue = row.get("tissue") or "other"

    # Primary cells
    primary_cells = [
        ("", intervention_cell(row)),
        ("", escape(safe(row.get("indication")))),
        ('style="text-align:right"', escape(str(
            row.get("n_treated_with_treg_measurement")
            or row.get("n_treated_with_tam_measurement")
            or ""
        ))),
        ('class="col-report"', report_cell(row)),
        ("", tissue_chip(tissue)),
        ("", assay_chip(row.get("gating_quality"), row.get("readout_type"))),
        ('style="text-align:right"', pct_html),
        ("", sf_badge + (f'<br>{mech_html}' if mech_html else "")),
        ("", build_confidence_cell((critiques_by_pmid or {}).get(row.get("pmid") or ""))),
        ('class="col-bias"', build_bias_cell((critiques_by_pmid or {}).get(row.get("pmid") or ""))),
        ("", cite_links(row, critique_pmids)),
    ]

    # Expanded cells
    expanded_cells = [
        ("col-expanded", escape(safe(row.get("pmid")))),
        ("col-expanded", escape(safe(row.get("design_type")))),
        ('col-expanded truncate', escape(safe(row.get("dose")))),
        ("col-expanded mono truncate", escape(safe(row.get("treg_definition")))),
        ("col-expanded", escape(safe(row.get("readout_type")))),
        ("col-expanded", escape(safe(row.get("timepoint_cluster")))),
        ("col-expanded mono truncate", escape(safe(row.get("timepoint_detail")))),
        ("col-expanded truncate", escape(safe(row.get("baseline_value")))),
        ("col-expanded truncate", escape(safe(row.get("post_value")))),
        ("col-expanded truncate", escape(safe(row.get("change_magnitude")))),
        ("col-expanded", escape(safe(row.get("change_significance")))),
        ("col-expanded col-durability", escape(safe(row.get("durability_described")))),
        ("col-expanded", escape(safe(row.get("intent_to_deplete")))),
        ("col-expanded", escape(safe(row.get("source_type")))),
        ("col-expanded col-notes truncate", escape(safe(row.get("notes")))),
    ]

    td_parts = []
    for attr, content in primary_cells:
        td_parts.append(f"<td {attr}>{content}</td>")
    for cls, content in expanded_cells:
        td_parts.append(f'<td class="{cls}" title="{escape(str(content))}">{content}</td>')

    tr = (
        f'<tr class="group-{group_idx % 6}" data-tissue="{escape(tissue)}" '
        f'data-study="{escape(safe(row.get("pmid"), ""))}">'
        + "".join(td_parts)
        + "</tr>"
    )
    return tr


def build_table_html(
    rows: list[dict],
    critique_pmids: set[str] | None = None,
    critiques_by_pmid: dict[str, dict] | None = None,
) -> str:
    # Sort: pmid, tissue, timepoint_cluster so multi-row studies group contiguously
    tp_order = {
        "baseline": 0,
        "early-on-treatment": 1,
        "mid": 2,
        "late": 3,
        "post-progression": 4,
        "off-treatment-recovery": 5,
    }
    rows_sorted = sorted(
        rows,
        key=lambda r: (
            r.get("pmid") or "zzz",
            r.get("tissue") or "zzz",
            tp_order.get(r.get("timepoint_cluster") or "", 9),
        ),
    )

    # Assign group indices by order of first appearance of pmid
    first_seen: dict[str, int] = {}
    for r in rows_sorted:
        pid = r.get("pmid") or r.get("row_id")
        if pid not in first_seen:
            first_seen[pid] = len(first_seen)

    body_rows = []
    for r in rows_sorted:
        pid = r.get("pmid") or r.get("row_id")
        body_rows.append(build_row_html(r, first_seen[pid], critique_pmids, critiques_by_pmid))

    # Thead: primary + expanded headers
    primary_headers = ["Intervention", "Disease", "N", "Report", "Tissue", "Assay", "Treg change", "Result", "Confidence", "Bias & confounding", "Source"]
    expanded_headers = [
        "PMID", "Design", "Dose/schedule", "Treg defn", "Readout",
        "Timepoint", "Timing detail", "Baseline", "Post", "Magnitude",
        "Significance", "Durability", "Intent", "Data source", "Notes",
    ]

    thead_cells = [f"<th>{h}</th>" for h in primary_headers]
    thead_cells += [f'<th class="th-expanded">{h}</th>' for h in expanded_headers]

    filter_chips_html = """
<div class="filter-row">
  <span class="filter-chip active" data-tissue="all">All</span>
  <span class="filter-chip pill tis-pbmc" data-tissue="PBMC">PBMC</span>
  <span class="filter-chip pill tis-tumor" data-tissue="tumor">tumor</span>
  <span class="filter-chip pill tis-tdln" data-tissue="TDLN">TDLN</span>
  <span class="filter-chip pill tis-bm" data-tissue="bone-marrow">bone marrow</span>
  <span class="filter-chip pill tis-ascites" data-tissue="ascites">ascites</span>
  <span class="filter-chip pill tis-skin" data-tissue="skin">skin</span>
  <span class="filter-chip pill tis-other" data-tissue="other">other</span>
</div>
""".strip()

    toggle_html = """
<label class="expand-toggle">
  <input type="checkbox" id="expand-cols"> Show all columns (dose, treg defn, baseline/post values, durability, notes)
</label>
""".strip()

    table_html = (
        f'<div class="pd-table-wrapper" markdown="0">\n'
        f"{filter_chips_html}\n"
        f"{toggle_html}\n"
        f'<table class="pd-table">\n'
        f"<thead><tr>{''.join(thead_cells)}</tr></thead>\n"
        f"<tbody>\n" + "\n".join(body_rows) + "\n</tbody>\n"
        f"</table>\n"
        f'</div>\n'
        + FILTER_SCRIPT
        + EXPAND_SCRIPT
    )
    return table_html


FILTER_SCRIPT = """
<script>
(function(){
  var chips = document.querySelectorAll('.filter-chip');
  chips.forEach(function(chip){
    chip.addEventListener('click', function(){
      var t = chip.dataset.tissue;
      chips.forEach(function(c){ c.classList.remove('active'); });
      chip.classList.add('active');
      document.querySelectorAll('.pd-table tbody tr').forEach(function(row){
        row.style.display = (t === 'all' || row.dataset.tissue === t) ? '' : 'none';
      });
    });
  });
})();
</script>
""".strip()

EXPAND_SCRIPT = """
<script>
(function(){
  var cb = document.getElementById('expand-cols');
  if (!cb) return;
  cb.addEventListener('change', function(){
    var t = document.querySelector('.pd-table');
    if (t) t.classList.toggle('show-all', cb.checked);
  });
})();
</script>
""".strip()


def build_reviews_section(reviews: list[dict]) -> str:
    if not reviews:
        return ""
    parts = ["\n## Side-list: systematic reviews and meta-analyses\n"]
    parts.append(
        "These are excluded from the primary table but retained as follow-up leads.\n"
    )
    parts.append("| First author | Year | Journal | Title | Type | Links |")
    parts.append("|---|---|---|---|---|---|")
    for r in reviews:
        links = []
        if r.get("pmid"):
            links.append(f'[PMID](https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/)')
        if r.get("doi"):
            links.append(f'[DOI](https://doi.org/{r["doi"]})')
        parts.append(
            f"| {safe(r.get('first_author'))} | {safe(r.get('year'))} | "
            f"{safe(r.get('journal'))} | {safe(r.get('title'))} | "
            f"{safe(r.get('review_type'))} | {' '.join(links) or '—'} |"
        )
    return "\n".join(parts) + "\n"


# ---------- page ----------


_STANDALONE_HTML_BASE_CSS = """
/* Standalone-page chrome for the Pharmacodynamic results trial table.
   Renders alongside the per-shieldbreak stylesheet so all pill / chip
   / filter / table styles are inherited. */

:root {
  /* Mirror the Material light-theme tokens used in the per-shieldbreak CSS. */
  --md-default-bg-color: #ffffff;
  --md-default-fg-color: #1a1a26;
  --md-default-fg-color--light: #4a4a5c;
  --md-default-fg-color--lighter: rgba(0, 0, 0, 0.14);
  --md-default-fg-color--lightest: rgba(0, 0, 0, 0.045);
  --md-primary-fg-color: #5b3a87;
  --md-primary-fg-color--lightest: rgba(91, 58, 135, 0.06);
  --md-code-font: ui-monospace, "SFMono-Regular", "Consolas", monospace;
}

@media (prefers-color-scheme: dark) {
  :root {
    --md-default-bg-color: #1a1a26;
    --md-default-fg-color: #f1f1f5;
    --md-default-fg-color--light: #c8c8d2;
    --md-default-fg-color--lighter: rgba(255, 255, 255, 0.18);
    --md-default-fg-color--lightest: rgba(255, 255, 255, 0.05);
    --md-primary-fg-color: #b89cd6;
    --md-primary-fg-color--lightest: rgba(184, 156, 214, 0.10);
  }
  /* Trigger the slate-mode CSS rules in the per-shieldbreak stylesheet. */
  html { color-scheme: dark; }
  body { background: var(--md-default-bg-color); color: var(--md-default-fg-color); }
}

* { box-sizing: border-box; }
html { color-scheme: light dark; }
body {
  margin: 0;
  padding: 1.5rem clamp(1rem, 4vw, 3rem) 3rem;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue",
               Helvetica, Arial, sans-serif;
  line-height: 1.45;
  font-size: 14px;
}

.sb-meta {
  max-width: 90rem;
  margin: 0 auto 1.5rem auto;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--md-default-fg-color--lighter);
}
.sb-meta-eyebrow {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--md-primary-fg-color);
  margin: 0 0 0.4rem 0;
}
.sb-meta-title {
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0 0 0.4rem 0;
  line-height: 1.25;
}
.sb-meta-stats {
  font-size: 0.85rem;
  color: var(--md-default-fg-color--light);
  margin: 0;
}
.sb-meta-back {
  display: inline-block;
  margin-top: 0.6rem;
  font-size: 0.85rem;
  color: var(--md-primary-fg-color);
  text-decoration: none;
}
.sb-meta-back:hover { text-decoration: underline; }

/* Treat the slate dark-mode prefix used by the per-shieldbreak stylesheet
   as a no-op selector — the @media block above already swapped variables. */
[data-md-color-scheme="slate"] { display: contents; }

main { max-width: 90rem; margin: 0 auto; }

/* Hard-coded substitutes for Material's Markdown-extension classes that
   the inlined stylesheet may reference. */
table { border-collapse: collapse; }
"""


def build_standalone_pd_html(
    slug: str,
    rows: list[dict],
    critique_pmids: set[str] | None,
    critiques_by_pmid: dict[str, dict] | None,
    meta: dict,
) -> str:
    """Compose a self-contained HTML document with the Pharmacodynamic results
    trial table — usable by an external reviewer without MkDocs."""
    n_rows = len(rows)
    n_studies = len({r.get("pmid") for r in rows if r.get("pmid")})
    n_success = sum(1 for r in rows if r.get("depletion_success") == "succeeded")
    n_failed = sum(1 for r in rows if r.get("depletion_success") == "failed")
    n_partial = sum(1 for r in rows if r.get("depletion_success") == "partial")
    n_not_assessed = sum(1 for r in rows if r.get("depletion_success") == "not-assessed")
    title = meta.get("display_title") or slug.replace("-", " ").title()
    today = datetime.now(timezone.utc).date().isoformat()

    table_html = build_table_html(rows, critique_pmids, critiques_by_pmid)
    inlined_css = _STANDALONE_HTML_BASE_CSS + "\n\n" + build_css()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — Pharmacodynamic results</title>
<style>{inlined_css}</style>
</head>
<body>
<header class="sb-meta">
  <p class="sb-meta-eyebrow">Pharmacodynamic results</p>
  <h1 class="sb-meta-title">{escape(title)}</h1>
  <p class="sb-meta-stats"><strong>Last updated:</strong> {today} &nbsp;
    <strong>Rows:</strong> {n_rows} across {n_studies} studies &nbsp;
    <strong>Outcomes:</strong> {n_success} succeeded / {n_partial} partial /
    {n_failed} failed / {n_not_assessed} not-assessed (ratio-shift)</p>
  <p class="sb-meta-stats"><em>Self-contained download from
    pirl-unc.github.io/io-shieldbreak — open in any modern browser.
    Filters and the "Show all columns" toggle work offline.</em></p>
</header>
<main>
{table_html}
</main>
</body>
</html>
"""


def _read_shieldbreak_meta(slug: str) -> dict:
    """Read top-level meta fields from schema.json. Returns empty dict if missing."""
    schema_path = DATA_DIR / slug / "schema.json"
    if not schema_path.exists():
        return {}
    try:
        return json.loads(schema_path.read_text())
    except json.JSONDecodeError:
        return {}


def build_index_md(slug: str) -> str:
    rows = read_jsonl(DATA_DIR / slug / "trials.jsonl")
    reviews = read_jsonl(DATA_DIR / slug / "reviews.jsonl")
    meta = _read_shieldbreak_meta(slug)
    critiques = read_jsonl(DATA_DIR / slug / "critiques.jsonl")
    critique_pmids = {c["pmid"] for c in critiques if c.get("pmid")}
    critiques_by_pmid = {c["pmid"]: c for c in critiques if c.get("pmid")}
    n_rows = len(rows)
    n_studies = len({r.get("pmid") for r in rows if r.get("pmid")})
    n_success = sum(1 for r in rows if r.get("depletion_success") == "succeeded")
    n_failed = sum(1 for r in rows if r.get("depletion_success") == "failed")
    n_partial = sum(1 for r in rows if r.get("depletion_success") == "partial")
    n_not_assessed = sum(1 for r in rows if r.get("depletion_success") == "not-assessed")

    today = datetime.now(timezone.utc).date().isoformat()
    title = meta.get("display_title") or slug.replace("-", " ").title()
    research_question = meta.get("research_question") or ""

    class_counts: dict[str, int] = {}
    for r in rows:
        c = r.get("intervention_class") or "other"
        class_counts[c] = class_counts.get(c, 0) + 1
    class_summary = ", ".join(
        f"{k} ({v})" for k, v in sorted(class_counts.items(), key=lambda kv: -kv[1])
    )

    tissue_counts: dict[str, int] = {}
    for r in rows:
        t = r.get("tissue") or "other"
        tissue_counts[t] = tissue_counts.get(t, 0) + 1
    tissue_summary = ", ".join(
        f"{k} ({v})" for k, v in sorted(tissue_counts.items(), key=lambda kv: -kv[1])
    )

    # Prescriber-owned narrative synthesis. When present, it replaces the
    # default class/tissue bullets under a single "## Scope summary" heading.
    scope_summary_path = DOCS_DIR / slug / "scope_summary.md"
    if scope_summary_path.exists():
        scope_summary_block = (
            "## Scope summary\n\n"
            + scope_summary_path.read_text().strip()
            + "\n\n"
            + "### Scope inventory\n\n"
            + f"- **Intervention classes:** {class_summary}\n"
            + f"- **Tissue compartments:** {tissue_summary}\n"
            + "- **Design types:** paired pre/post, treated-vs-untreated, single-arm, window-of-opportunity, case series (all flagged per row)\n"
            + "- **Row grain:** one row per (study × tissue × timepoint-cluster × dose-cohort)\n"
            + "- **Primary-research-only;** reviews / meta-analyses live in the "
              "[side-list](#side-list-systematic-reviews-and-meta-analyses) below.\n"
        )
    else:
        scope_summary_block = (
            "## Scope summary\n\n"
            + f"- **Intervention classes:** {class_summary}\n"
            + f"- **Tissue compartments:** {tissue_summary}\n"
            + "- **Design types:** paired pre/post, treated-vs-untreated, single-arm, window-of-opportunity, case series (all flagged per row)\n"
            + "- **Row grain:** one row per (study × tissue × timepoint-cluster × dose-cohort)\n"
            + "- **Primary-research-only;** reviews / meta-analyses live in the "
              "[side-list](#side-list-systematic-reviews-and-meta-analyses) below.\n"
        )

    download_block_parts: list[str] = []
    pdf_path = DOCS_DIR / slug / f"{slug}-shieldbreak-report.pdf"
    if pdf_path.exists():
        size_kb = pdf_path.stat().st_size / 1024
        download_block_parts.append(
            f'<p class="pdf-download"><a href="{slug}-shieldbreak-report.pdf" '
            f'download>📄 Download PDF report</a> '
            f'<span class="pdf-meta">({size_kb:.0f} KB — executive summary + ranked '
            f'interventions + per-trial detail tables)</span></p>'
        )
    critique_pdf_path = DOCS_DIR / slug / f"{slug}-critique.pdf"
    if critique_pdf_path.exists():
        size_kb = critique_pdf_path.stat().st_size / 1024
        download_block_parts.append(
            f'<p class="pdf-download"><a href="{slug}-critique.pdf" '
            f'download>🔍 Download critique PDF</a> '
            f'<span class="pdf-meta">({size_kb:.0f} KB — per-paper appraisal '
            f'+ cross-paper synthesis)</span></p>'
        )
    standalone_html_path = DOCS_DIR / slug / f"{slug}-pharmacodynamic-results.html"
    if standalone_html_path.exists():
        size_kb = standalone_html_path.stat().st_size / 1024
        download_block_parts.append(
            f'<p class="pdf-download"><a href="{slug}-pharmacodynamic-results.html" '
            f'download>📊 Download Pharmacodynamic results (HTML)</a> '
            f'<span class="pdf-meta">({size_kb:.0f} KB — sortable, filterable trial '
            f'table; opens locally in any browser)</span></p>'
        )
    pdf_link_block = "\n".join(download_block_parts) + ("\n\n" if download_block_parts else "")

    header = f"""# {title}

[← back to shieldbreaks]({"../index.md"})

**Last updated:** {today}  **Rows:** {n_rows} across {n_studies} studies  **Outcomes:** {n_success} succeeded / {n_partial} partial / {n_failed} failed / {n_not_assessed} not-assessed (ratio-shift)

{pdf_link_block}## Research question

{research_question}

{scope_summary_block}
See `prompts/shieldbreaks/{slug}/search.md` for the full search specification and
`prompts/shieldbreaks/{slug}/extract.md` for the extraction schema.

## Pharmacodynamic results

"""

    table_html = build_table_html(rows, critique_pmids, critiques_by_pmid)
    reviews_md = build_reviews_section(reviews)

    return wrap_sections_in_details(
        header + table_html + "\n" + reviews_md,
        skip_headings=frozenset({"Pharmacodynamic results"}),
    )


def build_css() -> str:
    """Emit the treg-depletion.css per STYLE.md. Also includes .pill base class
    (factored out so future shieldbreaks can @import it)."""
    return """/* Generated by scripts/build_table.py — do not hand-edit.
   Source spec: styles/treg-depletion/STYLE.md */

/* ---- PDF download link (above Research question) ---- */
p.pdf-download {
  display: inline-block;
  margin: 0.5em 0 1em 0;
  padding: 0.4em 0.9em;
  border: 1px solid var(--md-primary-fg-color, #5b3a87);
  border-radius: 0.3em;
  background: var(--md-primary-fg-color--lightest, rgba(91, 58, 135, 0.06));
  font-size: 0.92em;
}
p.pdf-download a {
  font-weight: 600;
  text-decoration: none;
  color: var(--md-primary-fg-color, #5b3a87);
}
p.pdf-download a:hover { text-decoration: underline; }
p.pdf-download .pdf-meta {
  margin-left: 0.5em;
  font-size: 0.82em;
  opacity: 0.75;
  font-weight: 400;
}
[data-md-color-scheme="slate"] p.pdf-download {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.18);
}

/* ---- Collapsible subsection wrappers (one toggle per ## section) ---- */
details.sb-section {
  margin: 0.25em 0 1.25em 0;
}
details.sb-section > summary {
  display: inline-block;
  cursor: pointer;
  padding: 0.25em 0.85em;
  background: var(--md-default-fg-color--lightest, rgba(0, 0, 0, 0.045));
  border: 1px solid var(--md-default-fg-color--lighter, rgba(0, 0, 0, 0.14));
  border-radius: 0.3em;
  font-size: 0.82em;
  font-weight: 600;
  user-select: none;
  margin: 0.1em 0 0.9em 0;
  list-style: none;
  transition: background 0.12s;
}
details.sb-section > summary::-webkit-details-marker { display: none; }
details.sb-section > summary::before {
  content: "\\25B8";   /* ▸ */
  display: inline-block;
  margin-right: 0.45em;
  transition: transform 0.12s;
}
details.sb-section[open] > summary::before {
  content: "\\25BE";   /* ▾ */
}
details.sb-section > summary:hover {
  background: var(--md-default-fg-color--lighter, rgba(0, 0, 0, 0.1));
}
[data-md-color-scheme="slate"] details.sb-section > summary {
  background: rgba(255, 255, 255, 0.055);
  border-color: rgba(255, 255, 255, 0.14);
}
[data-md-color-scheme="slate"] details.sb-section > summary:hover {
  background: rgba(255, 255, 255, 0.11);
}

/* ---- .pill base class (factor into pills.css if a second shieldbreak lands) ---- */
.pill {
  display: inline-block;
  padding: 0.05em 0.55em;
  margin-right: 0.35em;
  border-radius: 0.65em;
  font-size: 0.72em;
  font-weight: 600;
  letter-spacing: 0.02em;
  line-height: 1.5;
  vertical-align: 0.12em;
  white-space: nowrap;
  border: 1px solid transparent;
}

/* ---- Citation links ---- */
.cite-links a {
  font-size: 0.75em;
  font-weight: 600;
  letter-spacing: 0.01em;
  color: var(--md-primary-fg-color);
  text-decoration: none;
  margin-right: 0.3em;
  white-space: nowrap;
}
.cite-links a:hover { text-decoration: underline; }
.cite-links a.critique-link {
  color: var(--md-default-fg-color);
  background: var(--md-default-fg-color--lightest, rgba(0,0,0,0.05));
  padding: 0.05em 0.4em;
  border-radius: 0.3em;
  font-style: italic;
}
[data-md-color-scheme="slate"] .cite-links a.critique-link {
  background: rgba(255,255,255,0.08);
}

/* ---- Booktabs-style table ---- */
.pd-table-wrapper { overflow-x: auto; margin: 1em 0; }
.pd-table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.88em;
}
.pd-table thead tr:first-child th { border-top: 2px solid var(--md-default-fg-color); }
.pd-table thead tr:last-child  th { border-bottom: 1.5px solid var(--md-default-fg-color); }
.pd-table tbody tr:last-child  td { border-bottom: 2px solid var(--md-default-fg-color); }
.pd-table th, .pd-table td {
  border: none;
  padding: 0.35em 0.6em;
  vertical-align: top;
}
.pd-table td { border-bottom: none !important; }
.pd-table th { text-align: left; font-weight: 600; }

/* ---- Truncation ---- */
.pd-table td.truncate {
  max-width: 22ch;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.pd-table td.truncate:hover {
  white-space: normal;
  overflow: visible;
  position: relative;
  z-index: 10;
  background: var(--md-default-bg-color);
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

/* ---- Monospace cells ---- */
.pd-table td.mono {
  font-family: var(--md-code-font);
  font-size: 0.82em;
}

/* ---- Durability ---- */
.pd-table td.col-durability { font-style: italic; font-size: 0.83em; }

/* ---- Notes column ---- */
.pd-table td.col-notes {
  font-style: italic;
  font-size: 0.80em;
  opacity: 0.8;
  max-width: 26ch;
}

/* ---- Inline combination secondary text ---- */
.pd-table td .combo {
  display: block;
  font-size: 0.82em;
  opacity: 0.7;
  margin-top: 0.15em;
}
.pd-table td .combo::before { content: "+ "; }

/* ---- Two-tier column visibility ---- */
.pd-table .col-expanded { display: none; }
.pd-table.show-all .col-expanded { display: table-cell; }
.pd-table .th-expanded { display: none; }
.pd-table.show-all .th-expanded { display: table-cell; }

.expand-toggle {
  display: inline-block;
  margin: 0.5em 0;
  font-size: 0.85em;
  cursor: pointer;
  user-select: none;
}
.expand-toggle input { margin-right: 0.4em; }

/* ---- Filter chip row ---- */
.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4em;
  margin-bottom: 0.75em;
  align-items: center;
}
.filter-chip {
  cursor: pointer;
  opacity: 0.65;
  transition: opacity 0.15s;
}
.filter-chip.active { opacity: 1; outline: 2px solid var(--md-primary-fg-color); }
.filter-chip:hover { opacity: 0.9; }

/* ---- Signed change (typed pct_change) ---- */
.change-neg { color: #1d6b4a; font-weight: 600; }
.change-pos { color: #8c4a1f; font-weight: 600; }
[data-md-color-scheme="slate"] .change-neg { color: #9fd4b7; }
[data-md-color-scheme="slate"] .change-pos { color: #e8b896; }

/* ---- Directional change (qualitative fallback, no typed pct_change) ---- */
.change-neg-qual { color: #1d6b4a; font-weight: 500; font-style: italic; opacity: 0.85; }
.change-pos-qual { color: #8c4a1f; font-weight: 500; font-style: italic; opacity: 0.85; }
.change-null { color: var(--md-default-fg-color--light); font-style: italic; }
[data-md-color-scheme="slate"] .change-neg-qual { color: #9fd4b7; }
[data-md-color-scheme="slate"] .change-pos-qual { color: #e8b896; }

/* ---- Success flag badges ---- */
.pill.sf-sig-reduction {
  background: #d9f2e5; color: #1d6b4a; border-color: #9fd4b7;
  font-size: 0.78em;
}
.pill.sf-nonsig-trend {
  background: #fbeacb; color: #8a5510; border-color: #e0b87c;
}
.pill.sf-null-result {
  background: #ececf2; color: #3f3f5c; border-color: #b4b4c4;
}
.pill.sf-increase {
  background: #fde4d3; color: #8c4a1f; border-color: #e8b896;
}
[data-md-color-scheme="slate"] .pill.sf-sig-reduction {
  background: #1d4a36; color: #9fd4b7; border-color: #4a7a62;
}
[data-md-color-scheme="slate"] .pill.sf-nonsig-trend {
  background: #4a3616; color: #e0b87c; border-color: #7a5c2e;
}
[data-md-color-scheme="slate"] .pill.sf-null-result {
  background: #2a2a38; color: #b4b4c4; border-color: #4e4e64;
}
[data-md-color-scheme="slate"] .pill.sf-increase {
  background: #4a2a14; color: #e8b896; border-color: #7a4a2a;
}

/* ---- Tissue chips ---- */
.pill.tis-pbmc    { background:#dce6f7; color:#234f8c; border-color:#7ea5d4; }
.pill.tis-tumor   { background:#e7dcf3; color:#5b3a87; border-color:#a995c8; }
.pill.tis-tdln    { background:#d4ecec; color:#1d5c5c; border-color:#8fc4c4; }
.pill.tis-bm      { background:#e8ebc7; color:#5a6a1d; border-color:#bac28a; }
.pill.tis-ascites { background:#fbeacb; color:#8a5510; border-color:#e0b87c; }
.pill.tis-skin    { background:#fde4d3; color:#8c4a1f; border-color:#e8b896; }
.pill.tis-other   { background:#ececf2; color:#3f3f5c; border-color:#b4b4c4; }

/* ---- Assay chips ---- */
.pill.assay-flow      { background:#dce6f7; color:#234f8c; border-color:#7ea5d4; }
.pill.assay-cytof     { background:#e7dcf3; color:#5b3a87; border-color:#a995c8; }
.pill.assay-ihc       { background:#d4ecec; color:#1d5c5c; border-color:#8fc4c4; }
.pill.assay-mif       { background:#fbeacb; color:#8a5510; border-color:#e0b87c; }
.pill.assay-bulk-rna  { background:#e8ebc7; color:#5a6a1d; border-color:#bac28a; }
.pill.assay-scrna     { background:#d9f2e5; color:#1d6b4a; border-color:#9fd4b7; }
.pill.assay-qpcr      { background:#ececf2; color:#3f3f5c; border-color:#b4b4c4; }

/* ---- Report (authorship + venue) cell ---- */
.pd-table td.col-report { max-width: 18ch; }
.report-cell { line-height: 1.25; }
.report-authors { font-weight: 600; font-size: 0.92em; }
.report-venue { font-size: 0.78em; opacity: 0.75; font-style: italic; margin-top: 0.1em; }

/* ---- Confidence pills ---- */
.pill.conf-high         { background: #d9f2e5; color: #1d6b4a; border-color: #9fd4b7; }
.pill.conf-moderate     { background: #dce6f7; color: #234f8c; border-color: #7ea5d4; }
.pill.conf-low          { background: #fbeacb; color: #8a5510; border-color: #e0b87c; }
.pill.conf-very-low     { background: #fde4d3; color: #8c4a1f; border-color: #e8b896; }
[data-md-color-scheme="slate"] .pill.conf-high      { background:#1d4a36; color:#9fd4b7; border-color:#4a7a62; }
[data-md-color-scheme="slate"] .pill.conf-moderate  { background:#2a3a5a; color:#7ea5d4; border-color:#3d5e8a; }
[data-md-color-scheme="slate"] .pill.conf-low       { background:#4a3616; color:#e0b87c; border-color:#7a5c2e; }
[data-md-color-scheme="slate"] .pill.conf-very-low  { background:#4a2a14; color:#e8b896; border-color:#7a4a2a; }

/* ---- Risk-of-bias pills (smaller, secondary to confidence) ---- */
.pill.rob-low               { background:#d9f2e5; color:#1d6b4a; border-color:#9fd4b7; font-size:0.68em; }
.pill.rob-some-concerns     { background:#fbeacb; color:#8a5510; border-color:#e0b87c; font-size:0.68em; }
.pill.rob-moderate          { background:#ececf2; color:#3f3f5c; border-color:#b4b4c4; font-size:0.68em; }
.pill.rob-serious           { background:#fde4d3; color:#8c4a1f; border-color:#e8b896; font-size:0.68em; }
.pill.rob-na                { background:#ececf2; color:#6b6b7f; border-color:#b4b4c4; font-size:0.68em; font-style:italic; }
[data-md-color-scheme="slate"] .pill.rob-low           { background:#1d4a36; color:#9fd4b7; border-color:#4a7a62; }
[data-md-color-scheme="slate"] .pill.rob-some-concerns { background:#4a3616; color:#e0b87c; border-color:#7a5c2e; }
[data-md-color-scheme="slate"] .pill.rob-moderate      { background:#2a2a38; color:#b4b4c4; border-color:#4e4e64; }
[data-md-color-scheme="slate"] .pill.rob-serious       { background:#4a2a14; color:#e8b896; border-color:#7a4a2a; }
[data-md-color-scheme="slate"] .pill.rob-na            { background:#2a2a38; color:#8a8a9e; border-color:#4e4e64; }

/* ---- Bias / confounding flag pills ---- */
.bias-flags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2em;
  margin-top: 0.25em;
  max-width: 22ch;
}
.pill.bias-flag {
  font-size: 0.62em;
  padding: 0.02em 0.4em;
  white-space: nowrap;
}
.pill.bias-flag.bias-confound { background:#fde4d3; color:#8c4a1f; border-color:#e8b896; }
.pill.bias-flag.bias-caveat   { background:#ececf2; color:#3f3f5c; border-color:#b4b4c4; }
[data-md-color-scheme="slate"] .pill.bias-flag.bias-confound { background:#4a2a14; color:#e8b896; border-color:#7a4a2a; }
[data-md-color-scheme="slate"] .pill.bias-flag.bias-caveat   { background:#2a2a38; color:#b4b4c4; border-color:#4e4e64; }

.pd-table td.col-bias { max-width: 24ch; }

/* ---- Change mechanism chips (smaller) ---- */
.pill.mech-depletion  { background:#d9f2e5; color:#1d6b4a; border-color:#9fd4b7; font-size:0.65em; }
.pill.mech-frac-shift { background:#dce6f7; color:#234f8c; border-color:#7ea5d4; font-size:0.65em; }
.pill.mech-ratio-only { background:#fbeacb; color:#8a5510; border-color:#e0b87c; font-size:0.65em; }
.pill.mech-null       { background:#ececf2; color:#3f3f5c; border-color:#b4b4c4; font-size:0.65em; }
.pill.mech-neutral    { background:#e7dcf3; color:#5b3a87; border-color:#a995c8; font-size:0.65em; }

/* ---- Row grouping (left-edge stripe cycle) ---- */
.pd-table tr.group-0 td:first-child { border-left: 3px solid #7ea5d4; }
.pd-table tr.group-1 td:first-child { border-left: 3px solid #9fd4b7; }
.pd-table tr.group-2 td:first-child { border-left: 3px solid #e0b87c; }
.pd-table tr.group-3 td:first-child { border-left: 3px solid #a995c8; }
.pd-table tr.group-4 td:first-child { border-left: 3px solid #bac28a; }
.pd-table tr.group-5 td:first-child { border-left: 3px solid #8fc4c4; }
[data-md-color-scheme="slate"] .pd-table tr.group-0 td:first-child { border-left-color: #3d5e8a; }
[data-md-color-scheme="slate"] .pd-table tr.group-1 td:first-child { border-left-color: #4a7a62; }
[data-md-color-scheme="slate"] .pd-table tr.group-2 td:first-child { border-left-color: #7a5c2e; }
[data-md-color-scheme="slate"] .pd-table tr.group-3 td:first-child { border-left-color: #6a4c90; }
[data-md-color-scheme="slate"] .pd-table tr.group-4 td:first-child { border-left-color: #555f25; }
[data-md-color-scheme="slate"] .pd-table tr.group-5 td:first-child { border-left-color: #3e6464; }
"""


def update_shieldbreaks_index(slug: str, row_count: int) -> None:
    """Regenerate the cross-shieldbreak directory page from data/shieldbreaks/*/trials.jsonl."""
    # (slug, display_title, row_count, last_updated, has_critique)
    entries: list[tuple[str, str, int, str, bool]] = []
    for sb_dir in DATA_DIR.iterdir():
        if not sb_dir.is_dir():
            continue
        jsonl = sb_dir / "trials.jsonl"
        if not jsonl.exists():
            continue
        rows = read_jsonl(jsonl)
        if not rows:
            continue
        last_upd = datetime.fromtimestamp(jsonl.stat().st_mtime, timezone.utc).date().isoformat()
        meta = _read_shieldbreak_meta(sb_dir.name)
        display_title = meta.get("display_title") or sb_dir.name.replace("-", " ").title()
        has_critique = (DOCS_DIR / sb_dir.name / "critique.md").exists()
        entries.append((sb_dir.name, display_title, len(rows), last_upd, has_critique))

    entries.sort(key=lambda e: e[1].casefold())

    lines = [
        "# Shieldbreaks",
        "",
        'A "shieldbreak" is a single project query — one research question about a mechanism of resistance to a cancer immunotherapy (checkpoint blockade, adoptive cell therapy, vaccine, cytokine, bispecific, oncolytic virus, or other immuno-oncology modality), with its own search parameters, extraction schema, trial table, and manuscript critique. Each lives in its own subdirectory so it can evolve independently of the others.',
        "",
        "## Active shieldbreaks",
        "",
    ]
    if not entries:
        lines.append("_(no shieldbreaks yet — the first will appear here once `trialist_screener` runs)_")
    else:
        lines.append("| Shieldbreak | Rows | Last updated | Critique |")
        lines.append("|---|---|---|---|")
        for name, title, n, upd, has_critique in entries:
            critique_cell = f"[critique]({name}/critique.md)" if has_critique else "—"
            lines.append(f"| [{title}]({name}/index.md) | {n} | {upd} | {critique_cell} |")
    lines += [
        "",
        "## Adding a shieldbreak",
        "",
        "Invoke the `trialist_screener` Claude Code subagent and answer \"new shieldbreak\" when prompted. The agent will:",
        "",
        "1. Ask for a project name and propose a slug (kebab-case)",
        "2. Elicit the search parameters → write to `prompts/shieldbreaks/<slug>/search.md`",
        "3. Elicit the extraction schema → write to `prompts/shieldbreaks/<slug>/extract.md` and `data/shieldbreaks/<slug>/schema.json`",
        "4. Run the search, screen, extract → append to `data/shieldbreaks/<slug>/trials.jsonl`",
        "5. Generate `docs/shieldbreaks/<slug>/index.md` with the trial table",
        "6. Add a row to this index page linking to the new project",
        "",
        "Once a shieldbreak has trial rows, the companion `trialist_skeptic` subagent reads the ingested manuscripts in full, verifies the extracted fields against the source, and publishes `docs/shieldbreaks/<slug>/critique.md` — a per-paper and cross-paper methodological appraisal. The skeptic also assesses, for every paper, **counter-productive mechanisms** by which the intervention's MoA may undermine the shieldbreak's broader target effect (e.g., anti-CCR4 depleting CCR4+ CD8 effector-memory cells alongside Tregs) even when the proximal endpoint is met.",
        "",
        "With the screener and skeptic runs complete, the `trialist_prescriber` subagent then synthesizes a top-level narrative: it reads `trials.jsonl` and `critiques.jsonl`, groups rows into interventions or intervention classes under PI-confirmed granularity, and for each selected intervention (3–7 total) writes a short section covering evidence base, likelihood of the desired effect, toxicity profile, counter-productive mechanisms, practical considerations, and a ranked-position rationale. The output is published as `docs/shieldbreaks/<slug>/scope_summary.md` and inlined at the top of the shieldbreak page under the `## Scope summary` heading; a Ranked prioritization table at the end weighs Likelihood × Toxicity × Counter-productive MoA into an Overall column. Rankings reflect the shieldbreak's Target effect as written; re-scoping it toward a downstream goal shifts the weights.",
    ]
    (DOCS_DIR / "index.md").write_text("\n".join(lines) + "\n")


# ---------- per-paper critique pages ----------


DIMENSION_SECTIONS = [
    ("Design", "design_notes"),
    ("Sample size", "sample_size_notes"),
    ("Effect magnitude calibration", "effect_calibration_notes"),
    ("Missing data", "missing_data_notes"),
    ("Multiplicity", "multiplicity_notes"),
    ("Generalizability", "generalizability_notes"),
    ("Gating / definition", "gating_notes"),
    ("Counter-productive mechanisms", "counter_productive_mechanisms"),
    ("Conflict of interest & funding", "coi_funding_notes"),
    ("Spin / framing", "spin_notes"),
]


def build_critique_page(slug: str, critique: dict) -> str:
    """Render a single per-paper critique as standalone markdown."""
    pmid = critique.get("pmid") or ""
    author = critique.get("first_author") or "Unknown"
    year = critique.get("year") or ""
    title = critique.get("title") or ""

    header_ids = []
    if pmid:
        header_ids.append(f'**PMID:** [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)')
    if critique.get("pmcid"):
        pmcid = critique["pmcid"]
        header_ids.append(
            f'**PMCID:** [{pmcid}](https://europepmc.org/article/PMC/{pmcid.replace("PMC", "")})'
        )
    if critique.get("doi"):
        doi = critique["doi"]
        header_ids.append(f'**DOI:** [{doi}](https://doi.org/{doi})')

    lines: list[str] = [
        f"# {author} {year} — critique",
        "",
        f"> {title}",
        "",
        f"[← back to critique report](../critique.md) · [← back to shieldbreak](../index.md)",
        "",
    ]
    if header_ids:
        lines += [" · ".join(header_ids), ""]

    cpm_sev = critique.get("counter_productive_severity") or "—"
    cpm_tags = critique.get("counter_productive_tags") or []
    cpm_tags_str = ", ".join(f"`{t}`" for t in cpm_tags) if cpm_tags else ""
    lines += [
        f"**Risk of bias ({critique.get('rob_tool', '—')}):** {critique.get('rob_rating', '—')}  ",
        f"**Per-trial confidence:** {critique.get('per_trial_confidence', '—')}  ",
        f"**Counter-productive MoA:** {cpm_sev}"
        + (f" ({cpm_tags_str})" if cpm_tags_str else "")
        + "  ",
        f"**Source tier:** {critique.get('source_tier', '—')}",
        "",
        "## Key critique",
        "",
        critique.get("key_critique") or "_(not recorded)_",
        "",
        "## Per-dimension findings",
        "",
    ]

    for label, field in DIMENSION_SECTIONS:
        val = critique.get(field)
        # Legacy fallback: gating_notes may be stored under shieldbreak-specific keys
        # on older critiques (e.g., treg_gating_notes before the 2026-04-23 rename).
        if not val and field == "gating_notes":
            val = critique.get("treg_gating_notes") or critique.get("tam_gating_notes")
        val = val or "_(not assessed)_"
        lines += [f"### {label}", "", val, ""]

    discrepancies = critique.get("extraction_discrepancies") or []
    lines += ["## Extraction fidelity", ""]
    if not discrepancies:
        lines += ["No discrepancies noted — the screener's extracted values match the source.", ""]
    else:
        for d in discrepancies:
            if isinstance(d, dict):
                field = d.get("field", "—")
                expected = d.get("source_value", d.get("expected", "—"))
                extracted = d.get("extracted_value", d.get("extracted", "—"))
                note = d.get("note", "")
                lines += [f"- **{field}**: source says `{expected}`; extraction has `{extracted}`. {note}"]
            else:
                lines += [f"- {d}"]
        lines.append("")

    lines += ["## Risk of bias — rationale", "", critique.get("rob_rationale") or "_(not recorded)_", ""]
    lines += ["## Confidence — rationale", "", critique.get("confidence_rationale") or "_(not recorded)_", ""]

    status = critique.get("retraction_status") or "none"
    retract_notes = critique.get("retraction_notes") or ""
    lines += ["## Retraction status", "", f"**{status}**"]
    if retract_notes:
        lines += ["", retract_notes]
    lines.append("")

    return wrap_sections_in_details("\n".join(lines) + "\n")


def build_per_paper_critique_pages(slug: str) -> int:
    """Split critiques.jsonl into docs/shieldbreaks/<slug>/critiques/<pmid>.md. Returns count written."""
    critiques = read_jsonl(DATA_DIR / slug / "critiques.jsonl")
    if not critiques:
        return 0
    out_dir = DOCS_DIR / slug / "critiques"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for c in critiques:
        pmid = c.get("pmid")
        if not pmid:
            continue
        (out_dir / f"{pmid}.md").write_text(build_critique_page(slug, c))
        written += 1
    return written


# ---------- main ----------


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: build_table.py <slug>", file=sys.stderr)
        return 2
    slug = argv[1]
    sb_data = DATA_DIR / slug
    sb_docs = DOCS_DIR / slug
    if not sb_data.exists():
        print(f"no data dir: {sb_data}", file=sys.stderr)
        return 1
    sb_docs.mkdir(parents=True, exist_ok=True)

    # CSS first — the standalone HTML inlines it.
    css_dir = REPO_ROOT / "docs" / "stylesheets"
    css_dir.mkdir(parents=True, exist_ok=True)
    (css_dir / f"{slug}.css").write_text(build_css())

    # Standalone Pharmacodynamic-results HTML — must exist before
    # build_index_md runs so the download-link block can detect it.
    rows_for_html = read_jsonl(sb_data / "trials.jsonl")
    critiques_for_html = read_jsonl(sb_data / "critiques.jsonl")
    standalone_html = build_standalone_pd_html(
        slug,
        rows_for_html,
        {c["pmid"] for c in critiques_for_html if c.get("pmid")},
        {c["pmid"]: c for c in critiques_for_html if c.get("pmid")},
        _read_shieldbreak_meta(slug),
    )
    (sb_docs / f"{slug}-pharmacodynamic-results.html").write_text(standalone_html)

    page = build_index_md(slug)
    (sb_docs / "index.md").write_text(page)

    # Per-paper critique pages (skipped if critiques.jsonl doesn't exist)
    n_critiques = build_per_paper_critique_pages(slug)

    # Rewrite the skeptic-owned critique.md with the same collapsible
    # wrapping so the whole shieldbreak site is consistent. If it's
    # already wrapped, just normalize the `<details>` opening tag
    # (keeps the file consistent with any config change here, e.g.
    # default-open vs default-closed) without re-nesting.
    critique_md = sb_docs / "critique.md"
    if critique_md.exists():
        existing = critique_md.read_text()
        if 'class="sb-section"' in existing:
            existing = re.sub(
                r'<details class="sb-section"[^>]*>',
                '<details class="sb-section" open markdown="1">',
                existing,
            )
            critique_md.write_text(existing)
        else:
            critique_md.write_text(wrap_sections_in_details(existing))

    # Update cross-shieldbreak index
    rows = read_jsonl(sb_data / "trials.jsonl")
    update_shieldbreaks_index(slug, len(rows))

    print(f"built docs/shieldbreaks/{slug}/index.md — {len(rows)} rows")
    print(f"built docs/stylesheets/{slug}.css")
    if n_critiques:
        print(f"built docs/shieldbreaks/{slug}/critiques/ — {n_critiques} per-paper pages")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
