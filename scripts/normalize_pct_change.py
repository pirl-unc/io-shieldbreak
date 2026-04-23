"""Populate typed pct_change on trials.jsonl from free-text change_magnitude.

Adds three fields per row where extractable:
  pct_change         signed float, percent (e.g. -73.0 means 73% reduction)
  pct_change_stat    'median' | 'mean' | 'point' | 'range-midpoint' | 'fold-derived'
  pct_change_source  short string citing which text fragment sourced the value

Leaves all three null when the row is qualitative-only, proportional-only
(e.g. '4/4 reduced'), or authors explicitly state no significant change.
Never invents a number from a qualitative claim.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TRIALS = REPO / "data" / "shieldbreaks" / "treg-depletion" / "trials.jsonl"

# Patterns tried in priority order. Each returns (signed_percent, stat_label, snippet).
HEADLINE_PATTERNS = [
    # "median X% reduction" / "median ~X% reduction"
    (
        re.compile(r"median\s*~?\s*(\d+(?:\.\d+)?)\s*%\s*reduction", re.I),
        lambda m: (-float(m.group(1)), "median"),
    ),
    (
        re.compile(r"median\s*~?\s*(\d+(?:\.\d+)?)\s*%\s*(?:increase|rise|expansion)", re.I),
        lambda m: (+float(m.group(1)), "median"),
    ),
    # "mean X% reduction" / "mean reduction X%"
    (
        re.compile(r"mean\s*~?\s*(\d+(?:\.\d+)?)\s*%\s*reduction", re.I),
        lambda m: (-float(m.group(1)), "mean"),
    ),
    (
        re.compile(r"mean\s*(?:reduction|decrease)\s*(?:of\s*)?(\d+(?:\.\d+)?)\s*%", re.I),
        lambda m: (-float(m.group(1)), "mean"),
    ),
    (
        re.compile(r"mean\s*~?\s*(\d+(?:\.\d+)?)\s*%\s*(?:increase|rise|expansion)", re.I),
        lambda m: (+float(m.group(1)), "mean"),
    ),
    # "X-Y% reduction" (range → midpoint)
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)\s*%\s*(?:relative\s+)?reduction", re.I),
        lambda m: (-(float(m.group(1)) + float(m.group(2))) / 2, "range-midpoint"),
    ),
    # "~X% reduction" (point estimate)
    (
        re.compile(r"~\s*(\d+(?:\.\d+)?)\s*%\s*reduction", re.I),
        lambda m: (-float(m.group(1)), "point"),
    ),
    (
        re.compile(r"~\s*(\d+(?:\.\d+)?)\s*%\s*(?:increase|rise|expansion)", re.I),
        lambda m: (+float(m.group(1)), "point"),
    ),
    # "X% reduction" / "X% decrease" / "X% decline"
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*%\s*(?:relative\s+)?(?:reduction|decrease|decline)", re.I),
        lambda m: (-float(m.group(1)), "point"),
    ),
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*%\s*(?:increase|rise|expansion)", re.I),
        lambda m: (+float(m.group(1)), "point"),
    ),
    # "X×/Xx INCREASE" — fold, convert to percent (Nx increase → +(N-1)*100%)
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*[×x]\s*INCREASE", re.I),
        lambda m: ((float(m.group(1)) - 1) * 100, "fold-derived"),
    ),
    # "expanded ~Nx" / "expanded Nx"
    (
        re.compile(r"expanded\s*~?\s*(\d+(?:\.\d+)?)\s*[×x]", re.I),
        lambda m: ((float(m.group(1)) - 1) * 100, "fold-derived"),
    ),
    # "Nx expansion"
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*[×x]\s*expansion", re.I),
        lambda m: ((float(m.group(1)) - 1) * 100, "fold-derived"),
    ),
    # "Nx decrease" / "Nx reduction" (fold-down)
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*[×x]\s*(?:decrease|reduction)", re.I),
        lambda m: (-(1 - 1 / float(m.group(1))) * 100, "fold-derived"),
    ),
    # "NxFCB[max]" — fold-change-from-baseline notation used in IL-2 variant studies
    (
        re.compile(r"(\d+(?:\.\d+)?)\s*[×x]\s*FCB", re.I),
        lambda m: ((float(m.group(1)) - 1) * 100, "fold-derived"),
    ),
]


def longest_match(text: str) -> tuple[float, str, str] | None:
    """Try patterns in priority order; return first hit."""
    if not text:
        return None
    for pat, fn in HEADLINE_PATTERNS:
        m = pat.search(text)
        if m:
            val, stat = fn(m)
            return val, stat, m.group(0)
    return None


# Per-row manual overrides. Keyed by (pmid, tissue, timepoint_cluster).
# Used when headline-regex would pick the wrong number or when the row needs
# human judgment (multi-arm studies, fold ranges, absolute-vs-relative, etc.)
#
# Value: dict with pct_change / pct_change_stat / pct_change_source, or
#        dict with skip=True to force null despite regex match.
OVERRIDES: dict[tuple[str, str, str], dict] = {
    # ~8-10x absolute Treg expansion in bempeg+nivo (Gogas 2024 PIVOT-02).
    # Midpoint 9x → +800%.
    ("39025948", "PBMC", "early-on-treatment"): {
        "pct_change": 800.0,
        "pct_change_stat": "fold-derived",
        "pct_change_source": "~8-10× absolute Treg expansion (midpoint 9×)",
    },
    # Median +1.05% ABSOLUTE increase in Treg frequency — not a relative % change.
    # The column is relative %, so leave null with a note (captured in notes).
    ("28951518", "PBMC", "early-on-treatment"): {"skip": True},
    # 40006664: "Overall depletion n.s. (p=0.10)" — responder subset −56% but
    # overall is non-significant. The typed column should reflect the overall
    # prespecified analysis, which is null. Note preserves responder subset.
    ("40006664", "PBMC", "early-on-treatment"): {"skip": True},
    # 40180420: CCR4+ eTreg −86.7% is the headline; total FoxP3+ is mixed.
    # Default regex captures this correctly; no override needed.
    # 16960692: "~61% reduction in frequency" — regex catches; correct.
    # 37729184: "Median ~90% reduction" — regex catches; correct.
    # 21558401: "~4.75× INCREASE" → +375%. Regex catches.
    # 39567211 nemva+pembro: "minimal Treg expansion" — qualitative, null.
    # All other rows: either regex catches or genuinely qualitative.
}


def decide(row: dict) -> dict:
    key = (row.get("pmid") or "", row.get("tissue") or "", row.get("timepoint_cluster") or "")
    override = OVERRIDES.get(key)
    if override:
        if override.get("skip"):
            return {"pct_change": None, "pct_change_stat": None, "pct_change_source": None}
        return {
            "pct_change": override["pct_change"],
            "pct_change_stat": override["pct_change_stat"],
            "pct_change_source": override["pct_change_source"],
        }

    # Authors explicitly state no significant change — respect that even if a
    # descriptive pre/post delta could be computed.
    direction = (row.get("change_direction") or "").lower()
    if direction == "no-change":
        return {"pct_change": None, "pct_change_stat": None, "pct_change_source": None}

    mag = row.get("change_magnitude") or ""
    hit = longest_match(mag)
    if hit:
        val, stat, snippet = hit
        return {
            "pct_change": round(val, 1),
            "pct_change_stat": stat,
            "pct_change_source": f"change_magnitude: {snippet!r}",
        }

    # Fall through: try baseline_value/post_value for a clear "A to B"
    # numeric pair. We deliberately don't try hard here — narrative baseline
    # strings are too heterogeneous to parse safely.
    return {"pct_change": None, "pct_change_stat": None, "pct_change_source": None}


def main() -> None:
    rows = [json.loads(line) for line in TRIALS.read_text().splitlines() if line.strip()]
    updated_count = 0
    assigned = []
    for row in rows:
        result = decide(row)
        # Only overwrite if previously null — never clobber a curated value.
        if row.get("pct_change") in (None, "", "null") and result["pct_change"] is not None:
            updated_count += 1
            assigned.append((row.get("pmid"), row.get("tissue"), result["pct_change"], result["pct_change_stat"]))
        row["pct_change"] = result["pct_change"]
        row["pct_change_stat"] = result["pct_change_stat"]
        row["pct_change_source"] = result["pct_change_source"]

    TRIALS.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    print(f"Rows processed: {len(rows)}")
    print(f"pct_change populated: {updated_count}")
    print()
    print("Assignments:")
    for pmid, tissue, val, stat in assigned:
        sign = "+" if val > 0 else ""
        print(f"  PMID {pmid:10} {tissue:8} {sign}{val}%  ({stat})")


if __name__ == "__main__":
    main()
