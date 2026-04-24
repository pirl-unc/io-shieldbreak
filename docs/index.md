# io-shieldbreak

A curated collection of clinical-trial tables and critical reviews of manuscripts on strategies to **overcome resistance to cancer immunotherapies** — combinations and modalities aimed at restoring response in tumors that resist immune checkpoint inhibitors, adoptive cell therapies (CAR-T, TIL), cancer vaccines, cytokine therapies, bispecifics, oncolytic viruses, and other immuno-oncology agents.

The site is organized by **shieldbreak** — each shieldbreak is one research question (one resistance axis, one class of intervention) with its own search parameters, extraction schema, sortable trial table, and manuscript critique.

## What's here

- **[Shieldbreaks](shieldbreaks/index.md)** — directory of all project queries, each with a trial table and a critique report
- **[Methods](methods.md)** — search sources, screening defaults, extraction conventions, critique conventions

## How it's maintained

Each shieldbreak passes through three Claude Code subagents in sequence. The `trialist_screener` searches the medical literature (NCBI-first), screens hits against PI-defined criteria, and extracts structured trial data. The `trialist_skeptic` then reads the ingested manuscripts in full, verifies that extracted values match the source, and publishes a structured methodological critique — including an assessment, for every paper, of **counter-productive mechanisms** by which the intervention's MoA may undermine the shieldbreak's broader target effect even when the proximal endpoint is met. Finally, the `trialist_prescriber` synthesizes the two prior outputs into a short top-level narrative: it groups trials by intervention or intervention class under PI-confirmed granularity, selects 3–7 interventions to rank, and for each writes a section covering evidence base, likelihood of the desired effect, toxicity profile, counter-productive mechanisms, practical considerations, and a ranked-position rationale — capped with a Ranked prioritization table weighing Likelihood × Toxicity × Counter-productive MoA into an Overall column. Raw search responses are archived per run, data files are append-only, and corrections supersede prior rows rather than overwriting them.
