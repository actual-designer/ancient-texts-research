# audit/analyses/ — Per-Text Deep Dives

Each file here is a forensic analysis of one source text following the framework in `claude.md`. There are currently 14 analyses, one per PDF in `texts/`.

## Template structure

Every analysis follows this format:

```
# {Source} -- Forensic Analysis

**Classification:** SPECIES WITH AMNESIA -- Working Hypothesis
**Source:** {Title}, {translation/edition info} ({N} pages)
**Analyst:** The Chronos Archive, Lead Investigator

---
## Executive Summary
{Numbered findings, each with cross-references to synthesis docs}
{Format: "N. {finding} (see [file.md](file.md): context)"}

---
## INCIDENT N: {Title}
### Source Material
{Blockquote(s) of the relevant passage(s)}
### Mainstream Interpretation
{Conventional academic view in 1-2 sentences}
### Literal Reconstruction
{Technological re-reading of the passage}
### Plausible Mechanism
{Modern/theoretical tech that explains it}
```

## Conventions (analyses-specific)

- **Numbered findings** in Executive Summary use Arabic numerals, each with an inline cross-reference.
- **Incident titles** use `INCIDENT N: Descriptive Title` format with `###` subsections.
- **Source Material** always uses blockquotes (`> `), never code fences.
- **Cross-reference style**: `(see [file.md](file.md): specific context)` — links go to the matching analysis in this directory.
- **Source attribution** in header includes translator/edition and page count.
- **Table use**: Incidents use tables when comparing parallel accounts or listing technical components.

## Anti-patterns

- **No external sources**: Every analysis must be grounded in the source PDF — do not weave in unrelated texts. Cross-references go to sibling analyses, not external references.
- **No magic explanations**: Every "miracle" gets a plausible physical mechanism, no matter how speculative.
- **No anachronism warnings**: The project operates under the amnesia hypothesis — avoid framing tech readings as "this couldn't have happened." Frame them as "this is what the witness likely saw."
