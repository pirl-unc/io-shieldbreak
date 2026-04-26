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

Pure Python; depends on `markdown` and `fpdf2` (both pip-installable, no
system libs needed). fpdf2 was chosen over weasyprint specifically to
avoid the Pango/Cairo system-dependency chain that's brittle on older
macOS / Xcode setups.
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
# The PDF is for external review — "Target effect" and "Cross-cutting
# caveat" stay on the website but are intentionally omitted here so the
# report goes straight from the executive summary into the ranked
# interventions. Reviewers who want context browse the live page.
INCLUDED_SECTIONS = [
    "Top interventions",
    "Ranked prioritization",
    "Caveats",
    "Sources",
]


# Substitutions to scrub references to the internal agent pipeline so
# external reviewers see findings + interpretation, not the toolchain.
# Order matters: longest / most specific patterns first.
_AGENT_SCRUBS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\bskeptic-critiqued\b"),   "critically appraised"),
    (re.compile(r"\bskeptic-High-confidence\b"), "High-confidence"),
    (re.compile(r"\bskeptic-High\b"),        "High"),
    (re.compile(r"\bskeptic-Moderate\b"),    "Moderate"),
    (re.compile(r"\bskeptic-Low\b"),         "Low"),
    (re.compile(r"\bskeptic-assessed\b"),    "appraised"),
    (re.compile(r"\bskeptic-weighted\b"),    "confidence-weighted"),
    (re.compile(r"\bSkeptic\s+confidences?\b"),  "Confidence"),
    (re.compile(r"\bskeptic\s+confidences?\b"),  "confidence"),
    (re.compile(r"\bSkeptic\s+CP-severity\b"), "CP severity"),
    (re.compile(r"\bskeptic\s+CP-severity\b"), "CP severity"),
    (re.compile(r"flagged by the skeptic"),  "flagged in critical appraisal"),
    (re.compile(r"the skeptic flagged"),     "critical appraisal flagged"),
    (re.compile(r"the skeptic identified"),  "critical appraisal identified"),
    (re.compile(r"the skeptic rated"),       "critical appraisal rated"),
    (re.compile(r"the skeptic called out"),  "critical appraisal called out"),
    (re.compile(r"forcing the skeptic to cap"), "forcing a cap of"),
    (re.compile(r"the skeptic'?s appraisal"), "the critical appraisal"),
    (re.compile(r"the skeptic'?s narrative"), "the critique narrative"),
    (re.compile(r"the skeptic'?s"),          "the critical appraisal's"),
    (re.compile(r"in skeptic narrative"),    "in critique narrative"),
    (re.compile(r"\bskeptic notes\b"),       "critique notes"),
    (re.compile(r"\bThe skeptic\b"),         "Critical appraisal"),
    (re.compile(r"\bthe skeptic\b"),         "critical appraisal"),
    (re.compile(r"\bskeptic\b"),             "critique"),
    # Screener / prescriber appear less often
    (re.compile(r"\btrialist_screener\b"),   "search"),
    (re.compile(r"\btrialist_skeptic\b"),    "critical appraisal"),
    (re.compile(r"\btrialist_prescriber\b"), "synthesis"),
    (re.compile(r"\bscreener pass\b"),       "extraction pass"),
    (re.compile(r"\bThe screener\b"),        "The literature search"),
    (re.compile(r"\bthe screener\b"),        "the literature search"),
    (re.compile(r"\bscreener\b"),            "search"),
    (re.compile(r"\bThe prescriber\b"),      "This synthesis"),
    (re.compile(r"\bthe prescriber\b"),      "this synthesis"),
    (re.compile(r"\bprescriber\b"),          "synthesis"),
]


def _scrub_agent_names(text: str) -> str:
    for pat, repl in _AGENT_SCRUBS:
        text = pat.sub(repl, text)
    return text


# ---------- markdown parsing ----------


def _read_meta(slug: str) -> dict:
    p = DATA_DIR / slug / "schema.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError:
        return {}


def _split_sections(md_text: str) -> list[tuple[str, str]]:
    """Split markdown at `## ` boundaries → list of (heading_text, body)."""
    sections: list[tuple[str, str]] = []
    current_heading = ""
    current_body: list[str] = []
    in_fence = False
    h2 = re.compile(r"^## (?!#)(.*)$")
    for line in md_text.splitlines():
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
    out: list[tuple[str, str]] = []
    for wanted in INCLUDED_SECTIONS:
        for heading, body in sections:
            if heading.startswith(wanted):
                out.append((heading, body))
                break
    return out


def _strip_disclaimer(body: str) -> str:
    return re.sub(
        r"(\n+\*This summary is an evidence-synthesis aid.*?patient care\.\*)",
        "",
        body,
        flags=re.S,
    ).rstrip()


# ---------- PDF rendering ----------


# Color palette (RGB tuples)
INK = (26, 26, 38)
INK_MUTED = (107, 107, 127)
INK_FAINT = (164, 164, 178)
ACCENT = (91, 58, 135)
RULE = (180, 180, 196)
RULE_FAINT = (220, 220, 228)
ROW_ALT = (250, 250, 253)
HEADER_BG = (236, 237, 246)
COVER_BG = (244, 240, 251)


_FONT_FAMILY = "Helvetica"  # mutated by _register_unicode_font()


# Common candidate paths for a Unicode-capable font, by style.
# First-match-wins; missing files are skipped.
_FONT_CANDIDATES = {
    "": [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ],
    "B": [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ],
    "I": [
        "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Oblique.ttf",
    ],
    "BI": [
        "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-BoldOblique.ttf",
    ],
}


# ASCII substitutions for when we fall back to Helvetica (Latin-1 only).
# Greek letters and arrows aren't in Latin-1 → spell them out.
_ASCII_SUBS = {
    "•": "*", "—": "--", "–": "-", "−": "-", "…": "...",
    "↑": "^", "↓": "v", "→": "->", "←": "<-", "↔": "<->",
    "≥": ">=", "≤": "<=", "≠": "!=", "≈": "~=", "±": "+/-",
    "“": '"', "”": '"', "‘": "'", "’": "'", "·": "-", "×": "x",
    "™": "(TM)", "®": "(R)", "©": "(C)", "°": " deg",
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
    "ε": "epsilon", "ζ": "zeta", "η": "eta", "θ": "theta",
    "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu", "µ": "mu",
    "ν": "nu", "ξ": "xi", "π": "pi", "ρ": "rho", "σ": "sigma",
    "τ": "tau", "υ": "upsilon", "φ": "phi", "χ": "chi",
    "ψ": "psi", "ω": "omega",
    "Α": "Alpha", "Β": "Beta", "Γ": "Gamma", "Δ": "Delta",
    "Ε": "Epsilon", "Λ": "Lambda", "Μ": "Mu", "Π": "Pi",
    "Σ": "Sigma", "Φ": "Phi",
}


def _register_unicode_font(pdf) -> str:
    """Try to register a Unicode TTF as 'sb-body'. Return font family name in use."""
    global _FONT_FAMILY
    found_any = False
    for style, paths in _FONT_CANDIDATES.items():
        for p in paths:
            if Path(p).exists():
                pdf.add_font("sb-body", style=style, fname=p)
                found_any = True
                break
    if found_any:
        _FONT_FAMILY = "sb-body"
    else:
        _FONT_FAMILY = "Helvetica"
    return _FONT_FAMILY


def _ascii_fallback(text: str) -> str:
    """Replace non-Latin-1 chars with ASCII substitutes (for Helvetica fallback)."""
    if _FONT_FAMILY != "Helvetica":
        return text
    out_chars: list[str] = []
    for ch in text:
        if ch in _ASCII_SUBS:
            out_chars.append(_ASCII_SUBS[ch])
        elif ord(ch) <= 0xFF:
            out_chars.append(ch)
        else:
            out_chars.append("?")
    return "".join(out_chars)


def _make_pdf(slug: str, meta: dict, exec_md: str, scope_md: str, out_path: Path) -> None:
    try:
        from fpdf import FPDF
        from fpdf.enums import XPos, YPos
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `fpdf2`.\n  pip install fpdf2 markdown"
        ) from e

    title = meta.get("display_title") or slug.replace("-", " ").title()
    research_q = meta.get("research_question") or ""
    today = datetime.now(timezone.utc).date().isoformat()

    sections = _select_sections(_split_sections(scope_md))
    if not sections:
        raise SystemExit(
            f"build_report: scope_summary.md for {slug} has no recognized sections "
            f"(looking for: {INCLUDED_SECTIONS})"
        )

    class ReportPDF(FPDF):
        def footer(self):
            if self.page_no() <= 1:
                return  # cover page: no footer
            self.set_y(-12)
            self.set_font(_FONT_FAMILY, "I", 8)
            self.set_text_color(*INK_MUTED)
            self.cell(
                0,
                6,
                f"{self.page_no()} of {{nb}}    ·    io-shieldbreak    ·    {slug}",
                align="C",
            )

    pdf = ReportPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    _register_unicode_font(pdf)

    _render_cover(pdf, title, research_q, today)
    _render_exec_summary(pdf, _scrub_agent_names(exec_md))

    for heading, body in sections:
        if heading.startswith("Sources"):
            body = _strip_disclaimer(body)
        _render_section(pdf, heading, _scrub_agent_names(body))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


# ---------- cover ----------


def _render_cover(pdf, title: str, research_q: str, today: str) -> None:
    pdf.add_page()
    # Background tint
    pdf.set_fill_color(*COVER_BG)
    pdf.rect(0, 0, pdf.w, pdf.h, style="F")

    pdf.set_y(40)
    pdf.set_x(20)
    pdf.set_text_color(*ACCENT)
    pdf.set_font(_FONT_FAMILY, "B", 10)
    pdf.cell(0, 6, "SHIELDBREAK REPORT")

    pdf.set_y(58)
    pdf.set_x(20)
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "B", 26)
    pdf.multi_cell(w=pdf.w - 40, h=11, text=title, align="L")

    if research_q:
        pdf.ln(6)
        pdf.set_x(20)
        pdf.set_font(_FONT_FAMILY, "I", 12)
        pdf.set_text_color(63, 63, 92)
        pdf.multi_cell(w=pdf.w - 40, h=6, text=research_q, align="L")

    # Meta line
    pdf.set_y(pdf.h - 50)
    pdf.set_x(20)
    pdf.set_text_color(*INK_MUTED)
    pdf.set_font(_FONT_FAMILY, "", 10)
    pdf.cell(0, 5, f"Generated {today}    ·    pirl-unc/io-shieldbreak")

    # Disclaimer
    pdf.set_y(pdf.h - 32)
    pdf.set_x(20)
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.2)
    pdf.line(20, pdf.h - 33, pdf.w - 20, pdf.h - 33)
    pdf.ln(2)
    pdf.set_x(20)
    pdf.set_text_color(*INK_MUTED)
    pdf.set_font(_FONT_FAMILY, "I", 8)
    pdf.multi_cell(
        w=pdf.w - 40,
        h=4,
        text=(
            "This report is an evidence-synthesis aid for research planning. It does "
            "not constitute clinical advice and must not be used to guide patient care."
        ),
    )


# ---------- body sections ----------


def _render_exec_summary(pdf, exec_md: str) -> None:
    pdf.add_page()
    _render_markdown_block(pdf, exec_md, top_h1=True)


def _render_section(pdf, heading: str, body: str) -> None:
    # Page break before each top-level section
    pdf.add_page()
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "B", 16)
    pdf.cell(0, 8, heading, new_x=XPos_LMARGIN(), new_y=YPos_NEXT())
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.5)
    pdf.line(pdf.l_margin, pdf.get_y() + 0.5, pdf.w - pdf.r_margin, pdf.get_y() + 0.5)
    pdf.ln(4)
    _render_markdown_block(pdf, body, top_h1=False)


# fpdf2 enum helpers (rebound at module load to avoid repeated imports)
def XPos_LMARGIN():
    from fpdf.enums import XPos
    return XPos.LMARGIN


def YPos_NEXT():
    from fpdf.enums import YPos
    return YPos.NEXT


# ---------- markdown block renderer ----------


_TABLE_LINE = re.compile(r"^\s*\|.*\|\s*$")
_TABLE_SEP = re.compile(r"^\s*\|?[\s|:\-]+\|?\s*$")
_INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
_INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
_INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_INLINE_CODE = re.compile(r"`([^`]+)`")


def _render_markdown_block(pdf, md: str, top_h1: bool) -> None:
    """Render a markdown block (no top-level # if top_h1=False).

    Recognizes: ###, paragraphs, bullet lists, ordered lists, GFM tables,
    bold / italic / link / inline-code spans, horizontal rules.
    """
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # Blank line → small vertical gap
        if not s:
            pdf.ln(2)
            i += 1
            continue

        # H1
        if s.startswith("# ") and top_h1:
            pdf.set_text_color(*INK)
            pdf.set_font(_FONT_FAMILY, "B", 18)
            pdf.cell(0, 9, s[2:].strip(), new_x=XPos_LMARGIN(), new_y=YPos_NEXT())
            pdf.set_draw_color(*INK)
            pdf.set_line_width(0.6)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)
            i += 1
            continue

        # H3 — the numbered intervention descriptors. These are the
        # primary navigation anchors of the report (one per ranked
        # intervention) so they're rendered larger than the parent
        # ## section header to read as the dominant content tier.
        if s.startswith("### "):
            pdf.ln(5)
            pdf.set_text_color(*INK)
            _multiline_text(pdf, s[4:].strip(), line_h=10, size=20)
            pdf.ln(2)
            i += 1
            continue

        # H4 (rarely used in this report — but support it)
        if s.startswith("#### "):
            pdf.set_text_color(*INK)
            _multiline_text(pdf, s[5:].strip(), line_h=5.5, size=11)
            i += 1
            continue

        # Horizontal rule
        if s in ("---", "***", "___"):
            pdf.ln(2)
            pdf.set_draw_color(*RULE_FAINT)
            pdf.set_line_width(0.2)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)
            i += 1
            continue

        # Table — collect contiguous table lines
        if _TABLE_LINE.match(line) and i + 1 < len(lines) and _TABLE_SEP.match(lines[i + 1]):
            j = i
            while j < len(lines) and (_TABLE_LINE.match(lines[j]) or _TABLE_SEP.match(lines[j])):
                j += 1
            _render_table(pdf, lines[i:j])
            i = j
            continue

        # Bullet list — collect contiguous list lines
        if re.match(r"^\s*[-*+]\s+", line):
            j = i
            while j < len(lines) and (
                re.match(r"^\s*[-*+]\s+", lines[j])
                or (lines[j].startswith("  ") and lines[j].strip())
            ):
                j += 1
            _render_bullets(pdf, lines[i:j])
            i = j
            continue

        # Ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            j = i
            while j < len(lines) and (
                re.match(r"^\s*\d+\.\s+", lines[j])
                or (lines[j].startswith("  ") and lines[j].strip())
            ):
                j += 1
            _render_ordered(pdf, lines[i:j])
            i = j
            continue

        # Block quote (single-line common case)
        if s.startswith("> "):
            _render_blockquote(pdf, s[2:])
            i += 1
            continue

        # Plain paragraph — collect until blank line
        para_lines = [line]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not _is_block_start(lines[j], lines, j):
            para_lines.append(lines[j])
            j += 1
        _render_paragraph(pdf, " ".join(p.strip() for p in para_lines))
        i = j


def _is_block_start(line: str, lines: list[str], idx: int) -> bool:
    s = line.strip()
    if s.startswith(("# ", "## ", "### ", "#### ", "- ", "* ", "+ ", "> ")):
        return True
    if re.match(r"^\s*\d+\.\s+", line):
        return True
    if s in ("---", "***", "___"):
        return True
    if (
        _TABLE_LINE.match(line)
        and idx + 1 < len(lines)
        and _TABLE_SEP.match(lines[idx + 1])
    ):
        return True
    return False


def _render_paragraph(pdf, text: str) -> None:
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "", 10)
    _emit_inline_runs(pdf, text, line_height=5)
    pdf.ln(2)


def _render_blockquote(pdf, text: str) -> None:
    x0 = pdf.l_margin
    pdf.set_x(x0 + 3)
    pdf.set_text_color(63, 63, 92)
    pdf.set_font(_FONT_FAMILY, "I", 10)
    _emit_inline_runs(pdf, text, line_height=5, indent=3)
    pdf.set_x(x0)
    # Left border
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.5)
    pdf.ln(1)


def _render_bullets(pdf, lines: list[str]) -> None:
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "", 10)
    indent = 5
    for line in lines:
        m = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        if not m:
            continue
        depth = (len(m.group(1)) // 2)
        bullet_x = pdf.l_margin + depth * 4
        text = m.group(2)
        pdf.set_x(bullet_x)
        pdf.cell(3, 5, "•")
        pdf.set_x(bullet_x + 4)
        _emit_inline_runs(pdf, text, line_height=5, indent=bullet_x + 4 - pdf.l_margin)
    pdf.ln(1)


def _render_ordered(pdf, lines: list[str]) -> None:
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "", 10)
    n = 1
    for line in lines:
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if not m:
            continue
        text = m.group(2)
        pdf.set_x(pdf.l_margin)
        pdf.cell(7, 5, f"{n}.")
        pdf.set_x(pdf.l_margin + 7)
        _emit_inline_runs(pdf, text, line_height=5, indent=7)
        n += 1
    pdf.ln(1)


# ---------- inline-span renderer ----------


def _emit_inline_runs(pdf, text: str, line_height: float, indent: float = 0.0) -> None:
    """Lay out a paragraph honoring **bold**, *italic*, [link](url), `code`."""
    runs = _tokenize_inline(text)
    line_w = pdf.w - pdf.r_margin - pdf.l_margin - indent
    y_start = pdf.get_y()
    x_left = pdf.l_margin + indent
    pdf.set_x(x_left)
    cur_x = x_left
    for run in runs:
        s, style, color, link = run
        # word-wrap: break run on spaces
        words = re.findall(r"\S+\s*", s)
        for word in words:
            pdf.set_font(_FONT_FAMILY, style, 10)
            pdf.set_text_color(*color)
            w = pdf.get_string_width(word)
            if cur_x + w > pdf.l_margin + indent + line_w + 0.01:
                # new line
                pdf.ln(line_height)
                cur_x = x_left
                pdf.set_x(cur_x)
                # strip leading space on wrap
                if word.startswith(" "):
                    word = word.lstrip(" ")
                    w = pdf.get_string_width(word)
            pdf.cell(w, line_height, word, link=link or "")
            cur_x += w
    pdf.ln(line_height)


def _tokenize_inline(text: str) -> list[tuple[str, str, tuple, str]]:
    """Return list of (text, font_style, rgb, link). Order of precedence:
    inline code → links → bold → italic. Ignores nesting depth > 1."""
    # Split on inline code first to protect contents from other rules
    parts: list[tuple[str, bool]] = []  # (text, is_code)
    last = 0
    for m in _INLINE_CODE.finditer(text):
        if m.start() > last:
            parts.append((text[last : m.start()], False))
        parts.append((m.group(1), True))
        last = m.end()
    if last < len(text):
        parts.append((text[last:], False))

    runs: list[tuple[str, str, tuple, str]] = []
    for part_text, is_code in parts:
        if is_code:
            runs.append((part_text, "", INK_MUTED, ""))
            continue
        runs.extend(_tokenize_links(part_text))
    return runs


def _tokenize_links(text: str) -> list[tuple[str, str, tuple, str]]:
    runs: list[tuple[str, str, tuple, str]] = []
    last = 0
    for m in _INLINE_LINK.finditer(text):
        if m.start() > last:
            runs.extend(_tokenize_emph(text[last : m.start()], link=""))
        runs.extend(_tokenize_emph(m.group(1), link=m.group(2), is_link=True))
        last = m.end()
    if last < len(text):
        runs.extend(_tokenize_emph(text[last:], link=""))
    return runs


def _tokenize_emph(
    text: str, link: str = "", is_link: bool = False
) -> list[tuple[str, str, tuple, str]]:
    color = ACCENT if is_link else INK
    runs: list[tuple[str, str, tuple, str]] = []

    # bold first
    last = 0
    for m in _INLINE_BOLD.finditer(text):
        if m.start() > last:
            runs.extend(_tokenize_italic(text[last : m.start()], color, link))
        runs.append((m.group(1), "B", color, link))
        last = m.end()
    if last < len(text):
        runs.extend(_tokenize_italic(text[last:], color, link))

    return runs


def _tokenize_italic(text: str, color: tuple, link: str) -> list[tuple[str, str, tuple, str]]:
    runs: list[tuple[str, str, tuple, str]] = []
    last = 0
    for m in _INLINE_ITALIC.finditer(text):
        if m.start() > last:
            runs.append((text[last : m.start()], "", color, link))
        runs.append((m.group(1), "I", color, link))
        last = m.end()
    if last < len(text):
        runs.append((text[last:], "", color, link))
    return runs


# ---------- table renderer ----------


def _render_table(pdf, lines: list[str]) -> None:
    rows: list[list[str]] = []
    for line in lines:
        s = line.strip().strip("|")
        if _TABLE_SEP.match(line):
            continue
        cells = [c.strip() for c in re.split(r"\s*\|\s*", s)]
        rows.append(cells)
    if not rows:
        return

    n_cols = len(rows[0])
    page_w = pdf.w - pdf.l_margin - pdf.r_margin

    # Column widths: heuristic — last column gets more if it looks like
    # "Reference" (it's narrower in chars), middle Efficacy / Toxicity get more.
    headers = [h.lower() for h in rows[0]]
    widths = _column_widths(headers, page_w)

    # Render header row
    pdf.ln(2)
    pdf.set_fill_color(*HEADER_BG)
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.4)
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "B", 8)
    _render_table_row(pdf, rows[0], widths, fill=True, header=True)

    # Body rows
    pdf.set_font(_FONT_FAMILY, "", 8)
    pdf.set_text_color(*INK)
    for ri, row in enumerate(rows[1:]):
        if len(row) < n_cols:
            row = row + [""] * (n_cols - len(row))
        elif len(row) > n_cols:
            row = row[:n_cols]
        zebra = ri % 2 == 1
        _render_table_row(pdf, row, widths, fill=zebra, header=False)
    pdf.ln(2)


def _column_widths(headers: list[str], page_w: float) -> list[float]:
    n = len(headers)
    if n == 4 and "reference" in headers[-1]:
        # Therapeutic agent / Efficacy / Toxicity / Reference layout
        ratios = [0.20, 0.32, 0.32, 0.16]
    elif n == 5 or n == 6:
        # Ranked-prioritization-style table
        if n == 5:
            ratios = [0.05, 0.22, 0.21, 0.21, 0.31]
        else:
            ratios = [0.04, 0.18, 0.18, 0.16, 0.18, 0.26]
    else:
        ratios = [1.0 / n] * n
    return [page_w * r for r in ratios]


def _render_table_row(pdf, cells: list[str], widths: list[float], fill: bool, header: bool) -> None:
    from fpdf.enums import XPos, YPos

    # Pre-compute wrapped lines per cell to figure out the row height
    # We use multi_cell with a temporary write to measure, but fpdf2 makes
    # this awkward. Instead, estimate by character count vs col width.
    line_h = 4.2 if not header else 4.6
    pad_v = 1.2
    cell_lines: list[list[str]] = []
    for cell, w in zip(cells, widths):
        # Strip markdown links/bold for measurement; we'll re-emit during draw
        plain = _strip_inline_md(cell)
        wrapped = _word_wrap(plain, w - 2.4, pdf, font_style="B" if header else "")
        cell_lines.append(wrapped)
    n_lines = max(1, max(len(c) for c in cell_lines))
    row_h = max(line_h * n_lines + pad_v * 2, 6)

    # Page-break check
    if pdf.get_y() + row_h > pdf.h - pdf.b_margin:
        pdf.add_page()

    x0 = pdf.l_margin
    y0 = pdf.get_y()
    if fill:
        bg = HEADER_BG if header else ROW_ALT
        pdf.set_fill_color(*bg)
        pdf.rect(x0, y0, sum(widths), row_h, style="F")

    # Draw bottom rule
    pdf.set_draw_color(*RULE_FAINT if not header else INK)
    pdf.set_line_width(0.5 if header else 0.2)
    pdf.line(x0, y0 + row_h, x0 + sum(widths), y0 + row_h)
    if header:
        # Top rule above header
        pdf.set_line_width(0.5)
        pdf.line(x0, y0, x0 + sum(widths), y0)

    # Render cells
    cx = x0
    for cell, w, lines in zip(cells, widths, cell_lines):
        cy = y0 + pad_v
        for ln in lines:
            pdf.set_xy(cx + 1.2, cy)
            _emit_table_cell_line(pdf, ln, w - 2.4, header)
            cy += line_h
        cx += w

    pdf.set_xy(x0, y0 + row_h)


def _emit_table_cell_line(pdf, text: str, w: float, header: bool) -> None:
    """Emit one line of cell content with inline formatting (bold / link)."""
    # Highlight 'Unknown - non-OA' in muted color
    if "Unknown - non-OA" in text:
        pdf.set_text_color(*INK_MUTED)
    else:
        pdf.set_text_color(*INK)

    # Re-tokenize for inline (links + bold) but keep on a single line
    # Strip code backticks, emphasize bold text
    runs = _tokenize_inline(text)
    cur_x = pdf.get_x()
    y = pdf.get_y()
    for run_text, style, color, link in runs:
        pdf.set_font(_FONT_FAMILY, style if not header else "B", 8)
        run_color = color if not header else INK
        pdf.set_text_color(*run_color)
        pdf.set_xy(cur_x, y)
        # truncate if exceeds cell width
        ww = pdf.get_string_width(run_text)
        if cur_x + ww > pdf.get_x() + w + 0.01:
            # already at limit; bail (line wrapping handled at split-time)
            break
        pdf.cell(ww, 4.2, run_text, link=link or "")
        cur_x += ww


def _strip_inline_md(text: str) -> str:
    """Remove markdown formatting markers for plain-text measurement."""
    text = _INLINE_LINK.sub(r"\1", text)
    text = _INLINE_BOLD.sub(r"\1", text)
    text = _INLINE_ITALIC.sub(r"\1", text)
    text = _INLINE_CODE.sub(r"\1", text)
    return text


def _word_wrap(text: str, width: float, pdf, font_style: str = "", size: int = 8) -> list[str]:
    """Break `text` into lines that each fit in `width` mm at the given font size.

    Default size 8 is for table cells. Heading paths pass their own size so
    measurement uses the same metrics as final rendering — otherwise wrapping
    is wrong AND the rendering picks up size 8 (which previously caused
    `### N.` headings to silently downgrade to 8pt regardless of what the
    caller asked for).
    """
    pdf.set_font(_FONT_FAMILY, font_style, size)
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for w in words[1:]:
        candidate = current + " " + w
        if pdf.get_string_width(candidate) <= width:
            current = candidate
        else:
            lines.append(current)
            current = w
    lines.append(current)
    return lines


def _multiline_text(pdf, text: str, line_h: float, size: int = 16) -> None:
    """Render a heading text with manual word wrap (so we don't lose page layout)."""
    width = pdf.w - pdf.r_margin - pdf.l_margin
    lines = _word_wrap(text, width, pdf, font_style="B", size=size)
    pdf.set_font(_FONT_FAMILY, "B", size)
    for ln in lines:
        pdf.cell(0, line_h, ln, new_x=XPos_LMARGIN(), new_y=YPos_NEXT())


# ---------- main ----------


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

    out_path = DOCS_DIR / slug / f"{slug}-shieldbreak-report.pdf"
    _make_pdf(slug, meta, exec_md, scope_md, out_path)

    size_kb = out_path.stat().st_size / 1024
    print(f"built {out_path.relative_to(REPO_ROOT)} — {size_kb:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
