"""Backfill last_author on trials.jsonl by fetching PubMed metadata.

Uses NCBI E-utilities efetch (rettype=xml). Cached full-text XMLs from
data/shieldbreaks/<slug>/full_text/ are used first where possible; falls
back to live efetch for anything missing.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def last_author_from_pubmed_xml(xml_text: str) -> str | None:
    """Parse a PubMed efetch XML response (pubmed rettype) and return the
    last author's 'Lastname Initials' or None."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None
    # Pubmed XML: PubmedArticle/MedlineCitation/Article/AuthorList/Author
    # PMC XML: article/front/article-meta/contrib-group/contrib[@contrib-type='author']/name
    authors = root.findall(".//AuthorList/Author")
    if authors:
        last = authors[-1]
        ln = last.findtext("LastName")
        init = last.findtext("Initials")
        coll = last.findtext("CollectiveName")
        if ln:
            return f"{ln} {init}".strip() if init else ln
        if coll:
            return coll
        return None
    # PMC JATS fallback
    contribs = root.findall(".//contrib[@contrib-type='author']")
    if contribs:
        last = contribs[-1]
        surname = last.findtext(".//surname")
        given = last.findtext(".//given-names")
        if surname:
            # Shorten given names to initials
            initials = "".join(p[0] for p in (given or "").split() if p)
            return f"{surname} {initials}".strip()
        coll = last.findtext(".//collab")
        if coll is not None and coll.text:
            return coll.text
    return None


def fetch_pubmed_xml(pmid: str) -> str | None:
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        f"?db=pubmed&id={pmid}&rettype=xml"
    )
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  fetch error for PMID {pmid}: {e}", file=sys.stderr)
        return None


def try_cached(slug: str, pmid: str, pmcid: str | None) -> str | None:
    base = REPO / "data" / "shieldbreaks" / slug / "full_text"
    # Prefer PubMed-XML cache (has AuthorList); PMC JATS is secondary.
    candidates = [base / f"pubmed_{pmid}.xml"]
    if pmcid:
        candidates.append(base / f"{pmcid}.xml")
    for p in candidates:
        if p.exists():
            return p.read_text(errors="replace")
    return None


def main(slug: str) -> int:
    trials_path = REPO / "data" / "shieldbreaks" / slug / "trials.jsonl"
    rows = [json.loads(l) for l in trials_path.read_text().splitlines() if l.strip()]

    # Group by pmid so we fetch once per paper.
    pmid_to_author: dict[str, str | None] = {}
    pmids_needed = {r["pmid"] for r in rows if r.get("pmid") and not r.get("last_author")}
    print(f"Unique PMIDs needing last_author: {len(pmids_needed)}")

    for i, pmid in enumerate(sorted(pmids_needed), 1):
        pmcid = next((r.get("pmcid") for r in rows if r.get("pmid") == pmid and r.get("pmcid")), None)
        cached = try_cached(slug, pmid, pmcid)
        author: str | None = None
        if cached:
            author = last_author_from_pubmed_xml(cached)
        if not author:
            xml_text = fetch_pubmed_xml(pmid)
            if xml_text:
                author = last_author_from_pubmed_xml(xml_text)
            time.sleep(0.34)  # respect NCBI 3 req/s without API key
        pmid_to_author[pmid] = author
        marker = "✓" if author else "✗"
        print(f"  [{i:2}/{len(pmids_needed)}] {marker} PMID {pmid}: {author!r}")

    updated = 0
    for r in rows:
        if r.get("pmid") and r.get("pmid") in pmid_to_author and not r.get("last_author"):
            r["last_author"] = pmid_to_author[r["pmid"]]
            if r["last_author"]:
                updated += 1

    trials_path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    print(f"\nRows updated with last_author: {updated}/{len(rows)}")
    missing = [r["pmid"] for r in rows if not r.get("last_author")]
    if missing:
        print(f"Still missing on {len(missing)} rows: {sorted(set(missing))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "treg-depletion"))
