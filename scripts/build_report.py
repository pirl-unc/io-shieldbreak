#!/usr/bin/env python3
"""
Compose a shieldbreak's PDF report from the scope summary + executive summary.

Usage:
    python3 scripts/build_report.py <slug>

Reads:
    data/shieldbreaks/<slug>/executive_summary.md   (owned by shieldbreak_reporter)
    docs/shieldbreaks/<slug>/scope_summary.md       (owned by trialist_prescriber)
    data/shieldbreaks/<slug>/schema.json            (display title, research question)

Writes:
    docs/shieldbreaks/<slug>/<slug>-shieldbreak-report.pdf

The PDF is structured as:
    Cover page → Executive summary → Target effect → Cross-cutting caveat
        → Top interventions (verbatim, including per-trial detail tables)
        → Ranked prioritization → Caveats → Sources

Pure Python; depends on `markdown` and `weasyprint` (pip-installable).
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "shieldbreaks"
DOCS_DIR = REPO_ROOT / "docs" / "shieldbreaks"


# Sections from scope_summary.md to include in the PDF body, in order.
# Anything else (Intervention grouping, Classes examined but not ranked) is
# dropped — the reviewer audience cares about the ranked synthesis.
INCLUDED_SECTIONS = [
    "Target effect",
    "Cross-cutting caveat",  # may have suffix "(read first)"
    "Top interventions",
    "Ranked prioritization",
    "Caveats",
    "Sources",
]


def _read_meta(slug: str) -> dict:
    p = DATA_DIR / slug / "schema.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError:
        return {}


def _split_sections(markdown_text: str) -> list[tuple[str, str]]:
    """Split a markdown doc into (heading_text, section_body) pairs at `## ` boundaries.

    Anything before the first `## ` is returned with heading_text == "".
    """
    sections: list[tuple[str, str]] = []
    current_heading = ""
    current_body: list[str] = []
    in_fence = False
    h2 = re.compile(r"^## (?!#)(.*)$")
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
        m = None if in_fence else h2.match(line)
        if m:
            if current_heading or current_body:
                sections.append((current_heading, "\n".join(current_body).strip("\n")))
            current_heading = m.group(1).strip()
            current_body = []
        else:
            current_body.append(line)
    if current_heading or current_body:
        sections.append((current_heading, "\n".join(current_body).strip("\n")))
    return sections


def _select_sections(sections: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Pick the sections we want, in INCLUDED_SECTIONS order. Match by prefix
    so 'Cross-cutting caveat (read first)' matches 'Cross-cutting caveat'."""
    out: list[tuple[str, str]] = []
    for wanted in INCLUDED_SECTIONS:
        for heading, body in sections:
            if heading.startswith(wanted):
                out.append((heading, body))
                break
    return out


def _strip_disclaimer(body: str) -> str:
    """Remove the trailing disclaimer paragraph from the Sources section.
    The disclaimer reappears on the cover; no need to repeat at the end."""
    return re.sub(
        r"(\n+\*This summary is an evidence-synthesis aid.*?patient care\.\*)",
        "",
        body,
        flags=re.S,
    ).rstrip()


def _compose_markdown(slug: str, meta: dict, exec_md: str, scope_md: str) -> str:
    """Build the full markdown document for the report."""
    title = meta.get("display_title") or slug.replace("-", " ").title()
    research_q = meta.get("research_question") or ""
    today = datetime.now(timezone.utc).date().isoformat()

    cover = (
        '<div class="cover">\n'
        '<div class="cover-eyebrow">Shieldbreak report</div>\n'
        f'<h1 class="cover-title">{title}</h1>\n'
        + (f'<div class="cover-question">{research_q}</div>\n' if research_q else "")
        + f'<div class="cover-meta">Generated {today} · pirl-unc/io-shieldbreak</div>\n'
        '<div class="cover-disclaimer">This report is an evidence-synthesis aid for research planning. '
        'It does not constitute clinical advice and must not be used to guide patient care.</div>\n'
        "</div>\n\n"
    )

    sections = _split_sections(scope_md)
    selected = _select_sections(sections)
    if not selected:
        raise SystemExit(
            f"build_report: scope_summary.md for {slug} has no recognized "
            f"sections (looking for: {INCLUDED_SECTIONS})"
        )

    body_parts: list[str] = [cover]
    body_parts.append('<div class="section page-break">\n')
    body_parts.append(exec_md.strip() + "\n")
    body_parts.append("</div>\n")

    for heading, body in selected:
        if heading.startswith("Sources"):
            body = _strip_disclaimer(body)
        body_parts.append(f'<div class="section">\n\n## {heading}\n\n{body}\n\n</div>\n')

    return "\n".join(body_parts)


REPORT_CSS = """
@page {
  size: Letter;
  margin: 0.85in 0.75in 0.95in 0.75in;
  @bottom-center {
    content: counter(page) " of " counter(pages);
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 9pt;
    color: #6b6b7f;
  }
  @bottom-right {
    content: "io-shieldbreak";
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 9pt;
    color: #6b6b7f;
  }
}
@page :first {
  margin: 0;
  @bottom-center { content: ""; }
  @bottom-right { content: ""; }
}

html, body {
  font-family: 'Charter', 'Georgia', 'Times New Roman', serif;
  font-size: 10pt;
  line-height: 1.45;
  color: #1a1a26;
}

/* ---- Cover page ---- */
.cover {
  page: cover;
  width: 100%;
  height: 100vh;
  padding: 1.5in 1in 1in 1in;
  background: linear-gradient(135deg, #f6f4fb 0%, #ecedf6 100%);
  page-break-after: always;
  display: block;
}
.cover-eyebrow {
  font-family: 'Helvetica', 'Arial', sans-serif;
  font-size: 10pt;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #5b3a87;
  margin-bottom: 0.3in;
}
.cover-title {
  font-family: 'Charter', 'Georgia', serif;
  font-size: 28pt;
  font-weight: 700;
  line-height: 1.15;
  color: #1a1a26;
  margin: 0 0 0.4in 0;
}
.cover-question {
  font-family: 'Charter', 'Georgia', serif;
  font-size: 12pt;
  font-style: italic;
  line-height: 1.45;
  color: #3f3f5c;
  margin: 0 0 0.5in 0;
  max-width: 5.5in;
}
.cover-meta {
  font-family: 'Helvetica', 'Arial', sans-serif;
  font-size: 10pt;
  color: #6b6b7f;
  margin-bottom: 0.3in;
}
.cover-disclaimer {
  font-family: 'Helvetica', 'Arial', sans-serif;
  font-size: 8.5pt;
  font-style: italic;
  color: #6b6b7f;
  border-top: 1px solid #b4b4c4;
  padding-top: 0.18in;
  margin-top: 1.2in;
  max-width: 5.5in;
}

/* ---- Sections ---- */
.section { display: block; }
.section.page-break { page-break-before: always; }

h1 {
  font-family: 'Charter', 'Georgia', serif;
  font-size: 18pt;
  font-weight: 700;
  margin: 0 0 0.18in 0;
  color: #1a1a26;
  border-bottom: 2px solid #1a1a26;
  padding-bottom: 0.06in;
}
h2 {
  font-family: 'Charter', 'Georgia', serif;
  font-size: 14pt;
  font-weight: 700;
  margin: 0.32in 0 0.12in 0;
  color: #1a1a26;
  border-bottom: 1px solid #b4b4c4;
  padding-bottom: 0.04in;
  page-break-after: avoid;
}
h3 {
  font-family: 'Charter', 'Georgia', serif;
  font-size: 12pt;
  font-weight: 700;
  margin: 0.22in 0 0.08in 0;
  color: #2a2a38;
  page-break-after: avoid;
}
p { margin: 0.06in 0 0.10in 0; }
strong { font-weight: 700; }
em { font-style: italic; }

/* ---- Lists ---- */
ul, ol { margin: 0.06in 0 0.12in 0.18in; padding-left: 0.10in; }
li { margin: 0.03in 0; }

/* ---- Links ---- */
a {
  color: #2a4d8a;
  text-decoration: none;
}
a:hover { text-decoration: underline; }

/* ---- Tables ---- */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.10in 0 0.18in 0;
  font-size: 8.5pt;
  page-break-inside: auto;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th {
  font-family: 'Helvetica', 'Arial', sans-serif;
  font-size: 8pt;
  font-weight: 700;
  text-align: left;
  background: #ecedf6;
  color: #1a1a26;
  padding: 0.05in 0.07in;
  border-top: 1.5px solid #1a1a26;
  border-bottom: 1px solid #1a1a26;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
td {
  padding: 0.05in 0.07in;
  border-bottom: 0.5px solid #d6d6dc;
  vertical-align: top;
  line-height: 1.35;
}
tbody tr:last-child td { border-bottom: 1.5px solid #1a1a26; }
tbody tr:nth-child(even) td { background: #fafafd; }

/* Subtle highlight for "Unknown - non-OA" cells so reviewers spot access gaps */
td:has-text("Unknown - non-OA") { color: #6b6b7f; }

/* ---- Code & monospace ---- */
code {
  font-family: 'Menlo', 'Consolas', monospace;
  font-size: 9pt;
  background: #f5f5f9;
  padding: 0 0.05in;
  border-radius: 2px;
}

/* ---- Horizontal rule ---- */
hr {
  border: none;
  border-top: 1px solid #d6d6dc;
  margin: 0.18in 0;
}

/* ---- Closing italic disclaimer paragraph in exec summary ---- */
em:only-child { color: #6b6b7f; font-size: 9pt; }
"""


def _render_html(markdown_text: str) -> str:
    try:
        import markdown
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `markdown`. "
            "Install with: pip install markdown weasyprint"
        ) from e
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "attr_list", "md_in_html", "sane_lists"],
        output_format="html5",
    )
    body_html = md.convert(markdown_text)
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        "<title>Shieldbreak report</title>\n"
        f"<style>{REPORT_CSS}</style>\n"
        "</head>\n"
        f"<body>\n{body_html}\n</body>\n"
        "</html>\n"
    )


def _render_pdf(html: str, out_path: Path) -> None:
    try:
        from weasyprint import HTML
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `weasyprint`.\n"
            "  pip install weasyprint markdown\n"
            "  # macOS also needs Pango (Homebrew): brew install pango"
        ) from e
    except OSError as e:
        if "libgobject" in str(e) or "pango" in str(e).lower():
            raise SystemExit(
                "build_report: weasyprint imported but cannot load Pango.\n"
                "  macOS:  brew install pango\n"
                "  Linux:  apt install libpango-1.0-0 libpangoft2-1.0-0\n"
                "See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
            ) from e
        raise
    out_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(REPO_ROOT)).write_pdf(str(out_path))


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: build_report.py <slug>", file=sys.stderr)
        return 2
    slug = argv[1]

    scope_md_path = DOCS_DIR / slug / "scope_summary.md"
    exec_md_path = DATA_DIR / slug / "executive_summary.md"
    if not scope_md_path.exists():
        print(f"build_report: missing {scope_md_path}", file=sys.stderr)
        return 1
    if not exec_md_path.exists():
        print(f"build_report: missing {exec_md_path}", file=sys.stderr)
        return 1

    meta = _read_meta(slug)
    exec_md = exec_md_path.read_text()
    scope_md = scope_md_path.read_text()

    composed_md = _compose_markdown(slug, meta, exec_md, scope_md)
    html = _render_html(composed_md)
    out_path = DOCS_DIR / slug / f"{slug}-shieldbreak-report.pdf"
    _render_pdf(html, out_path)

    size_kb = out_path.stat().st_size / 1024
    print(f"built {out_path.relative_to(REPO_ROOT)} — {size_kb:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
