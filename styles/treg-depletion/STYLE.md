# STYLE — treg-depletion shieldbreak table

**Rendering stack:** MkDocs Material (same config as `io-shieldbreak` root `mkdocs.yml`).
Table lives in `docs/shieldbreaks/treg-depletion/index.md`, rendered as standard
Markdown tables with custom CSS injected via `extra_css`.

**CSS file to create:** `docs/stylesheets/treg-depletion.css`
**Register in mkdocs.yml:** add `- stylesheets/treg-depletion.css` under `extra_css`.

---

## 1. Inherited visual rules

These are taken verbatim from the sibling `io-resistance-genie` repo's pill/badge system
(`docs/stylesheets/tiers.css`) and the citation-link pattern used in `docs/papers.md`.
The table builder must not reinvent these — use the same class names and conventions.

### 1.1 Pill/badge base class

```css
/* shared with io-resistance-genie tiers.css — copy or @import */
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
```

All categorical chips and badges in this table derive from `.pill`. The sibling repo
calls the same shape `.tier` / `.sp`; here the canonical name is `.pill` to avoid
class-name collision if both stylesheets are ever co-loaded.

### 1.2 Citation links

Format: one or more inline links, space-separated, after all other cell content.
Use bare anchor tags with the `cite-link` class.

Pattern (from `io-resistance-genie/docs/papers.md`):

```
[PMID](https://pubmed.ncbi.nlm.nih.gov/<pmid>/)
[PMCID](https://europepmc.org/article/PMC/<pmcid>)
[DOI](https://doi.org/<doi>)
[NCT](https://clinicaltrials.gov/study/<nct_id>)
```

Render order within a cell: PMID → PMCID → DOI → NCT. Omit any that are null.
All four may be present; show whichever are non-null. Never fabricate a link.

CSS for the link group:

```css
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
```

The table builder should wrap all four ID links in a `<span class="cite-links">` so
the font shrink applies together without styling each `<a>` individually.

### 1.3 Booktabs aesthetic

- Horizontal rules only: `border-top` on `<thead>` rows and a single `border-bottom`
  under the last `<thead>` row; `border-bottom` on the last `<tbody>` row.
- No vertical borders anywhere.
- No row-zebra striping on the base table — row grouping (section 4.4) provides
  the only background differentiation.

```css
.pd-table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.88em;
}
.pd-table thead tr:first-child th { border-top: 2px solid var(--md-default-fg-color); }
.pd-table thead tr:last-child  th { border-bottom: 1.5px solid var(--md-default-fg-color); }
.pd-table tbody tr:last-child  td { border-bottom: 2px solid var(--md-default-fg-color); }
.pd-table th, .pd-table td { border: none; padding: 0.35em 0.6em; }
.pd-table th { text-align: left; font-weight: 600; }
```

MkDocs Material's own table CSS adds `border-bottom` to every `<td>` by default.
Override by adding `.pd-table td { border-bottom: none !important; }` in the
custom stylesheet — only the group-separator rule (section 4.4) and the final-row
rule re-introduce a bottom line.

### 1.4 Sortable columns

MkDocs Material's `content.tables.sortable` feature (already in `mkdocs.yml`) adds
click-to-sort to every Markdown table automatically. No additional CSS needed.
Column sort state is reflected by Material's built-in `aria-sort` indicators.

Do not add custom sort icons — they conflict with Material's native ones.

### 1.5 Responsive truncation

Long free-text cells truncate to two lines with a `title` tooltip (set `title` to
the full value in the generated HTML). CSS:

```css
.pd-table td.truncate {
  max-width: 18ch;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
/* on hover expand truncated cells */
.pd-table td.truncate:hover {
  white-space: normal;
  overflow: visible;
  position: relative;
  z-index: 10;
  background: var(--md-default-bg-color);
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
```

Apply `.truncate` to: `intervention_detail`, `treg_definition`, `selectivity_note`,
`notes`, `durability`. Do NOT truncate numeric or enum columns — they are already
compact.

---

## 2. Palette

Inherits MkDocs Material `primary: indigo` / `accent: amber` from `mkdocs.yml`.
The token names below map to Material's CSS custom properties.

### 2.1 Base tokens (do not redefine — use as-is from Material)

| Token | Light value | Dark (slate) | Role |
|---|---|---|---|
| `--md-default-fg-color` | `#1a1a2e` approx. | near-white | body text, table borders |
| `--md-default-bg-color` | `#ffffff` | `#1e1e2e` approx. | table background |
| `--md-primary-fg-color` | indigo `#3f51b5` | indigo lighter | cite links, sort indicators |
| `--md-typeset-color` | inherited | inherited | running text |

### 2.2 Semantic color tokens (define in `treg-depletion.css`)

These extend the palette for PD-specific semantics. They follow the same
light/dark pair pattern as `tiers.css`.

**Success flag — the primary emphasis badge:**

| Class suffix | Meaning | Light bg | Light fg | Light border | Dark bg | Dark fg | Dark border |
|---|---|---|---|---|---|---|---|
| `sig-reduction` | significant-reduction | `#d9f2e5` | `#1d6b4a` | `#9fd4b7` | `#1d4a36` | `#9fd4b7` | `#4a7a62` |
| `nonsig-trend` | nonsignificant-trend | `#fbeacb` | `#8a5510` | `#e0b87c` | `#4a3616` | `#e0b87c` | `#7a5c2e` |
| `null-result` | null-result | `#ececf2` | `#3f3f5c` | `#b4b4c4` | `#2a2a38` | `#b4b4c4` | `#4e4e64` |
| `increase` | increase (Tregs went up) | `#fde4d3` | `#8c4a1f` | `#e8b896` | `#4a2a14` | `#e8b896` | `#7a4a2a` |

Rationale: `sig-reduction` reuses the `tier-est` green from `tiers.css` because a
significant Treg reduction is the confirmed positive outcome, same semantic weight as
an established mechanism. `nonsig-trend` reuses `tier-cont` amber. `null-result` reuses
`sp-invitro` grey. `increase` reuses `sp-human` salmon/orange as a caution color —
distinctly warm without being a hard error red (which is reserved for data quality
flags, not biological outcomes).

**Signed change values (pct_change, fold_change):**

| Class | Meaning | Light | Dark |
|---|---|---|---|
| `.change-neg` | value < 0, Treg reduction (good) | `color: #1d6b4a` | `color: #9fd4b7` |
| `.change-pos` | value > 0, Treg increase (bad) | `color: #8c4a1f` | `color: #e8b896` |
| `.change-zero` | value = 0 or not-significant | `color: var(--md-default-fg-color)` | same |

No background fill on signed change cells — color alone is sufficient signal.
A unicode arrow prefix is added by the table builder: `↓` (U+2193) for negative,
`↑` (U+2191) for positive, nothing for zero. Arrow and number share the same color
class so they read as one unit.

Example rendered cell: `<span class="change-neg">↓ −38%</span>`

**Tissue filter chips:**

| Class | Tissue | Light bg | Light fg | Light border |
|---|---|---|---|---|
| `.tis-pbmc` | PBMC | `#dce6f7` | `#234f8c` | `#7ea5d4` |
| `.tis-tumor` | tumor | `#e7dcf3` | `#5b3a87` | `#a995c8` |
| `.tis-tdln` | TDLN | `#d4ecec` | `#1d5c5c` | `#8fc4c4` |
| `.tis-bm` | BM | `#e8ebc7` | `#5a6a1d` | `#bac28a` |
| `.tis-ascites` | ascites | `#fbeacb` | `#8a5510` | `#e0b87c` |
| `.tis-skin` | skin | `#fde4d3` | `#8c4a1f` | `#e8b896` |
| `.tis-other` | other | `#ececf2` | `#3f3f5c` | `#b4b4c4` |

Dark-mode pairs: follow the same inversion pattern as `tiers.css` (darken the
background by ~60–65%, lighten the text to the border color of the light variant).

**Assay chips:**

| Class | Assay | Light bg | Light fg | Light border |
|---|---|---|---|---|
| `.assay-flow` | flow | `#dce6f7` | `#234f8c` | `#7ea5d4` |
| `.assay-cytof` | CyTOF | `#e7dcf3` | `#5b3a87` | `#a995c8` |
| `.assay-ihc` | IHC | `#d4ecec` | `#1d5c5c` | `#8fc4c4` |
| `.assay-mif` | mIF | `#fbeacb` | `#8a5510` | `#e0b87c` |
| `.assay-bulk-rna` | bulk-RNA | `#e8ebc7` | `#5a6a1d` | `#bac28a` |
| `.assay-scrna` | scRNA | `#d9f2e5` | `#1d6b4a` | `#9fd4b7` |
| `.assay-qpcr` | qPCR | `#ececf2` | `#3f3f5c` | `#b4b4c4` |

**Change mechanism chips (secondary visual weight — smaller, less saturated):**

| Class | Value | Light bg | Light fg | Light border |
|---|---|---|---|---|
| `.mech-depletion` | depletion | `#d9f2e5` | `#1d6b4a` | `#9fd4b7` |
| `.mech-frac-shift` | fraction-shift | `#dce6f7` | `#234f8c` | `#7ea5d4` |
| `.mech-ratio-only` | ratio-only | `#fbeacb` | `#8a5510` | `#e0b87c` |
| `.mech-null` | null-result | `#ececf2` | `#3f3f5c` | `#b4b4c4` |

Change mechanism chips use a slightly reduced `font-size: 0.65em` (vs. `0.72em` for
success_flag badges) to visually rank below the success_flag column.

---

## 3. Typography

Inherits the MkDocs Material body font stack. No custom font load required.

| Role | Token / treatment |
|---|---|
| Table body | Material default sans-serif, `0.88em` relative to page body |
| Column headers | `font-weight: 600`, same size as body cells |
| Monospace cells | `font-family: var(--md-code-font)`, `font-size: 0.82em` — same token Material uses for inline code |
| Notes / captions | `font-style: italic; font-size: 0.82em; color: var(--md-default-fg-color--light)` |
| Cite links | `0.75em`, primary color (see section 1.2) |
| Pill/badge text | `0.72em`, `font-weight: 600` (base class) |
| Change-mech chip | `0.65em`, `font-weight: 600` |

**Monospace columns:** `treg_definition` and `treg_teff_ratio_change` use
`class="mono"` on the `<td>`. This makes surface marker strings like
`CD4+CD25hiCD127loFoxP3+` render in fixed-width so readers can visually diff
definitions across rows. Also apply `.mono` to the `timing` column when it contains
structured strings like "C1D1, C1D8, C3D1".

```css
.pd-table td.mono {
  font-family: var(--md-code-font);
  font-size: 0.82em;
}
```

**Durability column** (`col-durability`): plain prose, not monospace. The numerals
embedded in strings like "nadir d8, recovered d28" do not warrant full mono — they
are not being compared positionally across rows. Render as standard table body text
with italic styling so it reads as a qualitative annotation rather than a precise
measurement:

```css
.pd-table td.col-durability { font-style: italic; font-size: 0.83em; }
```

**Baseline stat inline format** (see section 4.1): no special class — the stat
descriptor is rendered as a `<small>` element with `opacity: 0.75` immediately after
the numeric value within the same cell.

---

## 4. PD-specific column rules

### 4.1 Numeric pre/post pairs with mixed stat types

Columns `baseline_treg_freq_pct`, `baseline_treg_abs`, `post_treg_freq_pct`,
`post_treg_abs` each display the value + its stat descriptor inline.

**Format rule:**

| `baseline_stat_type` | Rendered string |
|---|---|
| `mean-sd` | `12.4% (mean ± SD)` |
| `median-iqr` | `8.1% [5.2–11.0]` — IQR in square brackets |
| `range` | `8.1% [3.0–14.2]` — range in square brackets, same bracket style as IQR |
| `point` | `8.1%` — no parenthetical, just the value |

The parenthetical / bracket string is wrapped in `<small style="opacity:0.75">`.
When only the center value is available (SD/IQR/range not extracted), render as
`12.4% (mean)` or `8.1% (median)` per stat_type — never omit the descriptor.

The denominator string (`baseline_treg_freq_denom`, e.g. "of CD4+") is appended
as a second `<small>` on a new line within the same cell:

```
12.4% (mean ± SD)
<small class="denom">of CD4+</small>
```

```css
.pd-table td small.denom {
  display: block;
  font-size: 0.78em;
  opacity: 0.6;
  font-style: italic;
}
```

`baseline_stat_type` is a metadata field — it does not appear as its own column
in any view. It is consumed at render time to format the value cells above.

### 4.2 Signed change values

Columns: `pct_change`, `fold_change`.

Render rule for `pct_change`:
- Negative value → `<span class="change-neg">↓ −{abs(value)}%</span>`
- Positive value → `<span class="change-pos">↑ +{value}%</span>`
- Zero or null  → `—`

Render rule for `fold_change` (same color logic, different format):
- Negative (< 1.0 if fold, or negative if log-fold) → `<span class="change-neg">↓ {value}×</span>`
- Positive → `<span class="change-pos">↑ {value}×</span>`

If both `pct_change` and `fold_change` are present for the same row, show
`pct_change` in the primary view and `fold_change` in the expanded detail only.

`p_value` is displayed as-is (e.g. `0.031`) in primary view; if < 0.001, render
`< 0.001`. `statistical_test` appears only in expanded detail.

### 4.3 Success flag badge

Column: `success_flag`. This is the highest-emphasis categorical indicator.

HTML pattern:
```html
<span class="pill sf-sig-reduction">significant reduction</span>
<span class="pill sf-nonsig-trend">nonsignificant trend</span>
<span class="pill sf-null-result">null result</span>
<span class="pill sf-increase">increase</span>
```

CSS class names use prefix `sf-` to namespace from assay and tissue chips.
Colors from palette section 2.2.

The `sf-sig-reduction` badge uses `font-size: 0.78em` (slightly larger than other
pills) to further emphasize that this is the primary result indicator.

### 4.4 Row grouping for multi-row studies

The same `study_id` can appear on multiple consecutive rows (different tissue,
timepoint cluster, or dose cohort). Without visual grouping, these look like
duplicates.

**Rule:** rows sharing the same `study_id` are rendered as a group. The group
receives a left-edge marker — a `3px solid` left border on the first cell (`<td>`)
of every row in the group, using the group's accent color drawn from a fixed cycle
of 6 neutral-to-cool tones. The table builder assigns cycle index by order of first
appearance of each `study_id`.

```css
/* Group accent cycle — 6 left-edge colors, light mode */
.group-0 td:first-child { border-left: 3px solid #7ea5d4; }
.group-1 td:first-child { border-left: 3px solid #9fd4b7; }
.group-2 td:first-child { border-left: 3px solid #e0b87c; }
.group-3 td:first-child { border-left: 3px solid #a995c8; }
.group-4 td:first-child { border-left: 3px solid #bac28a; }
.group-5 td:first-child { border-left: 3px solid #8fc4c4; }
/* cycle repeats: modulo 6 */

/* Dark mode */
[data-md-color-scheme="slate"] .group-0 td:first-child { border-left-color: #3d5e8a; }
[data-md-color-scheme="slate"] .group-1 td:first-child { border-left-color: #4a7a62; }
[data-md-color-scheme="slate"] .group-2 td:first-child { border-left-color: #7a5c2e; }
[data-md-color-scheme="slate"] .group-3 td:first-child { border-left-color: #6a4c90; }
[data-md-color-scheme="slate"] .group-4 td:first-child { border-left-color: #555f25; }
[data-md-color-scheme="slate"] .group-5 td:first-child { border-left-color: #3e6464; }
```

The first `<td>` in the first row of a group also receives a `border-top: 1px solid
var(--md-default-fg-color--light)` group separator to mark the boundary clearly.
No background fill — the left-edge stripe is sufficient. The booktabs rule against
horizontal borders applies within a group, not between groups.

A `study_id` that appears only once still gets a group class (for consistent left
padding), but the left-edge color is `transparent`.

### 4.5 Combination column

Column: `combination`. When non-null, the co-administered agent is rendered as
secondary text directly under the primary intervention name in the same `<td>`,
separated by a `+` prefix in muted color:

```html
<td>
  Ipilimumab<br>
  <span class="combo">+ Nivolumab</span>
</td>
```

```css
.pd-table td .combo {
  display: block;
  font-size: 0.82em;
  opacity: 0.7;
  margin-top: 0.15em;
}
.pd-table td .combo::before { content: "+ "; }
/* table builder must NOT add a second "+" if the value already starts with "+" */
```

This keeps the cell compact while making it unambiguous that the row represents a
combination regimen. "Inline +" is not used because it collapses the primary and
combo agent into a single scan target, harming skimmability.

### 4.6 Change mechanism chip

Column: `change_mechanism`. Secondary visual weight — rendered as a smaller `.pill`
with `font-size: 0.65em`. Place it directly below the `success_flag` badge in the
primary table cell if they share a column in the condensed view; otherwise it is a
separate column in the expanded view only (see section 5).

HTML pattern:
```html
<span class="pill mech-depletion">depletion</span>
<span class="pill mech-frac-shift">fraction shift</span>
<span class="pill mech-ratio-only">ratio only</span>
<span class="pill mech-null">null</span>
```

### 4.7 Assay and tissue chips

Both use the `.pill` base class with the namespaced color classes from section 2.2.

Tissue chips appear in the filter chip row above the table (section 6) AND as
inline chips in the `tissue` column of the table. Both use the same class.

Assay chips appear only in the table body (`assay` column).

### 4.8 Notes column

Column: `notes`. Italic, small, low-opacity. Apply `.col-notes` to the `<td>`.

```css
.pd-table td.col-notes {
  font-style: italic;
  font-size: 0.80em;
  opacity: 0.8;
  max-width: 22ch;
}
```

Notes cells also receive `.truncate` (section 1.5). Tooltip (`title` attribute)
carries the full text.

---

## 5. Column visibility — primary vs. expanded

With 28+ columns, the default view is unreadable on a laptop. The table builder
must implement a two-tier system.

### 5.1 Primary view columns (shown by default, always)

| # | Column | Display header | Width hint |
|---|---|---|---|
| 1 | `intervention` + `combination` | Intervention | `min-width: 10ch` |
| 2 | `disease_context` | Disease | `min-width: 8ch` |
| 3 | `n_treated` | N | `min-width: 3ch; text-align: right` |
| 4 | `tissue` | Tissue | `min-width: 6ch` (chip) |
| 5 | `assay` | Assay | `min-width: 5ch` (chip) |
| 6 | `pct_change` | Treg change | `min-width: 7ch; text-align: right` |
| 7 | `success_flag` | Result | `min-width: 10ch` (badge) |
| 8 | `pmid` / `pmcid` / `doi` / `nct_id` | Source | `min-width: 8ch` (cite links) |

Total: 8 logical columns (cols 1 and 2 may wrap on narrow screens; col 8 is link-only).

### 5.2 Expanded view columns (behind "Show all columns" toggle)

All remaining columns, in this order:

| Columns added | Display header |
|---|---|
| `study_id` | Study ID |
| `study_design` | Design |
| `intervention_detail` | Dose/schedule (truncated) |
| `baseline_treg_freq_pct` | Baseline freq (truncated stat) |
| `baseline_treg_freq_denom` | Denom |
| `baseline_treg_abs` | Baseline abs |
| `post_treg_freq_pct` | Post freq |
| `post_treg_abs` | Post abs |
| `fold_change` | Fold change |
| `p_value` | p |
| `statistical_test` | Test |
| `durability` | Durability |
| `treg_definition` | Treg defn (mono, truncated) |
| `treg_teff_ratio_change` | Treg:Teff ratio |
| `change_mechanism` | Mechanism |
| `selectivity_note` | Selectivity (truncated) |
| `timing` | Timing |
| `source_type` | Data source |
| `notes` | Notes (italic, truncated) |

The "Show all columns" toggle is an `<input type="checkbox" id="expand-cols">` with
a `<label>` placed immediately above the table. When checked, the CSS class
`show-all` is added to the `<table>` element (or its wrapper) via a small inline
`<script>`. Hidden columns use `display: none` by default; toggling removes this.

```css
/* columns hidden in primary view */
.pd-table .col-expanded { display: none; }
.pd-table.show-all .col-expanded { display: table-cell; }
/* also show/hide <th> in <thead> */
.pd-table .th-expanded { display: none; }
.pd-table.show-all .th-expanded { display: table-cell; }
```

The toggle script (inline, no external JS dependency):

```html
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
```

---

## 6. Filter chip row (tissue filter)

A single row of tissue chips placed immediately above the table, inside a
`<div class="filter-row">`. Clicking a chip filters visible rows to those
matching that tissue value. "All" chip is always present and selected by default.

```html
<div class="filter-row">
  <span class="filter-chip active" data-tissue="all">All</span>
  <span class="filter-chip pill tis-pbmc" data-tissue="PBMC">PBMC</span>
  <span class="filter-chip pill tis-tumor" data-tissue="tumor">tumor</span>
  <span class="filter-chip pill tis-tdln" data-tissue="TDLN">TDLN</span>
  <span class="filter-chip pill tis-bm" data-tissue="BM">BM</span>
  <span class="filter-chip pill tis-ascites" data-tissue="ascites">ascites</span>
  <span class="filter-chip pill tis-skin" data-tissue="skin">skin</span>
  <span class="filter-chip pill tis-other" data-tissue="other">other</span>
</div>
```

```css
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
```

Filter script (inline, no external JS dependency). Each `<tr>` in `<tbody>` must
have a `data-tissue` attribute matching the value in its tissue column. The "All"
chip resets to showing every row.

```html
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
```

---

## 7. Full CSS variable reference for `treg-depletion.css`

The table builder should use these variable names consistently. Variables prefixed
`--td-` are local to this stylesheet; `--md-` variables come from Material and must
not be redefined.

```
/* Success flag */
--td-sf-sig-bg         #d9f2e5   / dark: #1d4a36
--td-sf-sig-fg         #1d6b4a   / dark: #9fd4b7
--td-sf-sig-border     #9fd4b7   / dark: #4a7a62

--td-sf-nonsig-bg      #fbeacb   / dark: #4a3616
--td-sf-nonsig-fg      #8a5510   / dark: #e0b87c
--td-sf-nonsig-border  #e0b87c   / dark: #7a5c2e

--td-sf-null-bg        #ececf2   / dark: #2a2a38
--td-sf-null-fg        #3f3f5c   / dark: #b4b4c4
--td-sf-null-border    #b4b4c4   / dark: #4e4e64

--td-sf-increase-bg    #fde4d3   / dark: #4a2a14
--td-sf-increase-fg    #8c4a1f   / dark: #e8b896
--td-sf-increase-border #e8b896  / dark: #7a4a2a

/* Signed change */
--td-change-neg        #1d6b4a   / dark: #9fd4b7
--td-change-pos        #8c4a1f   / dark: #e8b896
```

---

## 8. Usage instructions for table builder

1. Add `- stylesheets/treg-depletion.css` to `extra_css` in `mkdocs.yml`.
2. Write `docs/stylesheets/treg-depletion.css` containing all rules in this spec.
   The file must also `@import` (or copy inline) the `.pill` base class from
   `io-resistance-genie`'s `tiers.css` — or, if this repo has its own copy, from
   `docs/stylesheets/pills.css`. Do not duplicate between shieldbreaks; factor a
   shared `pills.css` if a second shieldbreak is added.
3. Build the table from `data/shieldbreaks/treg-depletion/trials.jsonl` using
   `scripts/build_table.py treg-depletion`. The script must:
   - Sort rows by `study_id` first, then `tissue`, then `timing` — so groups are
     contiguous before the user applies any column sort.
   - Assign `.group-{n % 6}` classes to rows per `study_id` (section 4.4).
   - Emit the filter chip row (section 6) and inline scripts before the `<table>`.
   - Wrap the table in `<div class="pd-table-wrapper">` with `overflow-x: auto` for
     mobile.
4. Confirm `mkdocs build --strict` passes before committing.

---

## 9. What the source STYLE.md would have provided vs. what was built from scratch

The referenced source file
`/Users/benjaminvincent/turtle/pirl-unc/pfo/conductor/styles/trial-table/STYLE.md`
does not exist on disk. The following was inferred from first-principles examination
of the live rendering stack:

**Directly inherited (from `io-resistance-genie` as the closest live sibling):**
- `.pill` base class geometry (padding, border-radius, font-size, font-weight) —
  taken verbatim from `tiers.css`.
- Semantic color hexes for all four outcome-states mapped to the `tier-est` /
  `tier-cont` / `sp-invitro` / `sp-human` colors in `tiers.css`.
- Citation link pattern (PMID → PMCID → DOI → NCT) — from `papers.md` column
  pattern.
- MkDocs Material feature flags (sortable tables, dark mode tokens) — from
  `mkdocs.yml` in this repo.

**Extended / newly specified (no prior source to inherit from):**
- Booktabs CSS rules (horizontal-only borders, overrides for Material's default
  border-bottom-on-every-td).
- `pct_change` / `fold_change` signed color + arrow convention.
- `success_flag` badge with `sf-` namespace.
- Tissue and assay chip color assignments.
- `change_mechanism` chip at reduced font-size.
- Row grouping via `.group-{n}` left-edge cycle.
- `combination` inline secondary-text pattern.
- Baseline stat inline format (`mean ± SD`, `[IQR]`).
- Monospace treatment for `treg_definition`.
- Two-tier column visibility (primary / expanded).
- Tissue filter chip row + scripts.
- `treg-depletion.css` variable naming convention.

**Gaps to address in the shared style if `pfo/conductor/styles/trial-table/STYLE.md`
is ever written:**
- The `.pill` base class should be factored into a repo-level
  `docs/stylesheets/pills.css` so both `treg-depletion` and any future shieldbreak
  can `@import` it without duplicating geometry rules.
- A shared citation-link CSS block (`.cite-links`) should live in a
  `docs/stylesheets/base-table.css`, not be re-specified per shieldbreak.
- Booktabs override rules are generic enough to belong in a shared base as well.
  Currently each shieldbreak would need to redeclare them.
