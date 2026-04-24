#!/usr/bin/env python3
"""
Build the per-shieldbreak critique Markdown page from critiques.jsonl + trials.jsonl.

Usage:
    python scripts/build_critique.py <slug>

Pure-Python; no LLM calls, no external deps.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "shieldbreaks"
DOCS_DIR = REPO_ROOT / "docs" / "shieldbreaks"


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


def build_per_paper_md(crit: dict, trial_rows_for_paper: list[dict]) -> str:
    """Render a single paper's critique block inside the master critique.md."""
    first = crit.get("first_author", "—")
    year = crit.get("year", "—")
    title = crit.get("title", "—")
    pmid = crit.get("pmid")
    doi = crit.get("doi")
    pmcid = crit.get("pmcid")
    nct = trial_rows_for_paper[0].get("nct_id") if trial_rows_for_paper else None

    citation_parts = []
    if pmid:
        citation_parts.append(f"[PMID {pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)")
    if pmcid:
        pmcnum = pmcid.replace("PMC", "")
        citation_parts.append(f"[PMCID {pmcid}](https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/)")
    if doi:
        citation_parts.append(f"[DOI {doi}](https://doi.org/{doi})")
    if nct:
        citation_parts.append(f"[NCT {nct}](https://clinicaltrials.gov/study/{nct})")

    lines = []
    lines.append(f"### {first} {year} — {title}")
    lines.append("")
    lines.append(f"**Citation.** {' · '.join(citation_parts) if citation_parts else '—'}")
    lines.append(f"**Source tier.** {safe(crit.get('source_tier'))}")
    lines.append("")

    lines.append(f"**Key critique.** {safe(crit.get('key_critique'))}")
    lines.append("")

    # Quick-read dimension block
    lines.append(f"**Design.** {safe(crit.get('design_notes'))}")
    lines.append(f"**Sample size & power.** {safe(crit.get('sample_size_notes'))}")
    lines.append(f"**Effect-size calibration.** {safe(crit.get('effect_calibration_notes'))}")
    lines.append(f"**Missing data.** {safe(crit.get('missing_data_notes'))}")
    lines.append(f"**Multiplicity.** {safe(crit.get('multiplicity_notes'))}")
    lines.append(f"**Generalizability.** {safe(crit.get('generalizability_notes'))}")
    gating = (
        crit.get("gating_notes")
        or crit.get("treg_gating_notes")
        or crit.get("tam_gating_notes")
    )
    lines.append(f"**Gating / definition.** {safe(gating)}")
    cpm_sev = crit.get("counter_productive_severity") or "—"
    cpm_tags = crit.get("counter_productive_tags") or []
    cpm_tags_str = f" ({', '.join(f'`{t}`' for t in cpm_tags)})" if cpm_tags else ""
    lines.append(
        f"**Counter-productive mechanisms ({cpm_sev}{cpm_tags_str}).** "
        f"{safe(crit.get('counter_productive_mechanisms'))}"
    )
    lines.append(f"**COI & funding.** {safe(crit.get('coi_funding_notes'))}")
    lines.append(f"**Spin / abstract-to-text consistency.** {safe(crit.get('spin_notes'))}")
    lines.append("")

    # Extraction fidelity
    discrep = crit.get("extraction_discrepancies") or []
    if not discrep:
        lines.append("**Extraction fidelity.** Matches source.")
    else:
        lines.append("**Extraction fidelity.** Discrepancies found:")
        lines.append("")
        for d in discrep:
            lines.append(
                f"- `{d.get('field','?')}` — extracted `{d.get('extracted','?')}`"
                f" vs source `{d.get('source_says','?')}`"
                f" (at {d.get('source_location','?')})"
                + (f": {d['note']}" if d.get("note") else "")
            )
    lines.append("")

    # Retraction status
    retraction = crit.get("retraction_status") or "none"
    if retraction != "none":
        lines.append(f"**⚠ RETRACTION STATUS: {retraction}.** {safe(crit.get('retraction_notes'))}")
        lines.append("")
    else:
        lines.append("**Retraction status.** None found as of review date.")
        lines.append("")

    # Risk of bias + per-trial confidence
    lines.append(
        f"**Risk of bias.** {safe(crit.get('rob_tool'))}: "
        f"**{safe(crit.get('rob_rating'))}** — {safe(crit.get('rob_rationale'))}"
    )
    lines.append(
        f"**Per-trial confidence.** **{safe(crit.get('per_trial_confidence'))}** — "
        f"{safe(crit.get('confidence_rationale'))}"
    )
    lines.append("")
    return "\n".join(lines)


def build_critique_page(slug: str) -> str:
    trials = read_jsonl(DATA_DIR / slug / "trials.jsonl")
    crits = read_jsonl(DATA_DIR / slug / "critiques.jsonl")

    # Group trials by pmid
    trials_by_pmid: dict[str, list[dict]] = defaultdict(list)
    for r in trials:
        k = r.get("pmid") or r.get("doi") or r.get("title")
        trials_by_pmid[k].append(r)

    # Latest critique per paper (take last; supersedes chain is simple here)
    latest: dict[str, dict] = {}
    for c in crits:
        k = c.get("pmid") or c.get("doi") or c.get("title")
        latest[k] = c

    # Sort by first_author / year
    ordered = sorted(latest.values(), key=lambda c: (c.get("first_author", "") or "", c.get("year", 0) or 0))

    # Schema meta
    meta_path = DATA_DIR / slug / "schema.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    display_title = meta.get("display_title") or slug.replace("-", " ").title()

    today = datetime.now(timezone.utc).date().isoformat()

    n_papers = len(ordered)
    n_discrepancies = sum(len(c.get("extraction_discrepancies") or []) for c in ordered)
    n_retract = sum(1 for c in ordered if (c.get("retraction_status") or "none") != "none")
    rob_dist = defaultdict(int)
    for c in ordered:
        rob_dist[c.get("rob_rating") or "—"] += 1
    conf_dist = defaultdict(int)
    for c in ordered:
        conf_dist[c.get("per_trial_confidence") or "—"] += 1

    # Header
    out = []
    out.append(f"# Trialist critique — {display_title}")
    out.append("")
    out.append(f"_Last updated: {today}. Papers reviewed: {n_papers}._")
    out.append("")
    out.append("[← back to shieldbreak](index.md) · [← back to shieldbreaks](../index.md)")
    out.append("")

    out.append("## Top-line findings")
    out.append("")
    topline = meta.get("critique_topline_override")
    if topline:
        for t in topline:
            out.append(f"- {t}")
    else:
        out.append("_(see synthesis section below for cross-paper findings)_")
    out.append("")

    out.append("## Summary stats")
    out.append("")
    out.append(f"- **Papers critiqued:** {n_papers}")
    out.append(f"- **Extraction-fidelity discrepancies flagged:** {n_discrepancies}")
    out.append(f"- **Retractions / corrections / expressions of concern:** {n_retract}")
    out.append("")
    out.append("### Risk-of-bias distribution")
    out.append("")
    out.append("| Rating | N |")
    out.append("|---|---:|")
    for k, v in sorted(rob_dist.items()):
        out.append(f"| {k} | {v} |")
    out.append("")
    out.append("### Per-trial confidence distribution")
    out.append("")
    out.append("| Confidence | N |")
    out.append("|---|---:|")
    for k, v in sorted(conf_dist.items()):
        out.append(f"| {k} | {v} |")
    out.append("")

    # Counter-productive severity distribution (schema extension 2026-04-23)
    cpm_dist: dict[str, int] = defaultdict(int)
    for c in ordered:
        cpm_dist[c.get("counter_productive_severity") or "—"] += 1
    if any(k != "—" for k in cpm_dist):
        out.append("### Counter-productive-mechanism severity distribution")
        out.append("")
        out.append("| Severity | N |")
        out.append("|---|---:|")
        sev_order = {"High": 0, "Moderate": 1, "Low": 2, "Unknown": 3, "—": 4}
        for k, v in sorted(cpm_dist.items(), key=lambda kv: sev_order.get(kv[0], 99)):
            out.append(f"| {k} | {v} |")
        out.append("")

    # Cross-paper synthesis (if present)
    synthesis = meta.get("critique_synthesis")
    if synthesis:
        out.append("## Cross-paper synthesis")
        out.append("")
        for section, bullets in synthesis.items():
            out.append(f"### {section}")
            out.append("")
            for b in bullets:
                out.append(f"- {b}")
            out.append("")

    out.append("## Per-paper critiques")
    out.append("")
    for c in ordered:
        k = c.get("pmid") or c.get("doi") or c.get("title")
        trials_for_paper = trials_by_pmid.get(k, [])
        out.append(build_per_paper_md(c, trials_for_paper))
        out.append("---")
        out.append("")
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: build_critique.py <slug>", file=sys.stderr)
        return 2
    slug = argv[1]
    sb_data = DATA_DIR / slug
    sb_docs = DOCS_DIR / slug
    if not sb_data.exists():
        print(f"no data dir: {sb_data}", file=sys.stderr)
        return 1
    sb_docs.mkdir(parents=True, exist_ok=True)
    page = build_critique_page(slug)
    (sb_docs / "critique.md").write_text(page)
    n = len(read_jsonl(sb_data / "critiques.jsonl"))
    print(f"built docs/shieldbreaks/{slug}/critique.md — {n} critiques")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
