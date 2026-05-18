# DSR Framework White Paper Package

This package contains the v1.0.1 DSR Framework white paper and release-preparation scaffold for turning the DSR theory synthesis materials into a citable, repository-native white paper.

Canonical DOI: https://doi.org/10.5281/zenodo.20271949

## Decision

Use a **repository-native methodological white paper with an open artifact package**. The canonical release path should be:

1. GitHub repository package as living source of truth.
2. Zenodo archive of a versioned GitHub release for DOI citation.
3. OSF project as discovery hub and MetaArXiv/OSF Preprints submission after the GitHub release and Zenodo DOI are available.
4. Octopus modular record after stable sections can be mapped to research-process publication types.
5. Mendeley Data or Dryad only for data packages, not for the white paper itself.
6. ResearchGate, Academia.edu, LinkedIn, Substack, ORCID, and personal pages as dissemination links, not canonical sources.

## Key files

| File | Role |
|---|---|
| `whitepaper/chapters/` | Separate Markdown chapters for editing. |
| `whitepaper/whitepaper_unified.md` | Single Markdown manuscript for compilation and upload. |
| `whitepaper/references.bib` | BibTeX source used by Pandoc citeproc for the main reference list. |
| `whitepaper/appendices/parsed-source-bibliography.md` | Supplemental parsed-source bibliography retained outside the main reference list. |
| `publication_strategy.md` | Human-facing platform strategy. |
| `codex_handoff.md` | Token-efficient Codex prompt and execution plan. |
| `manual_checklist.md` | Actions that require manual platform access or judgment. |
| `metadata/` | Citation, Zenodo, CodeMeta, service-profile, and release metadata templates. |
| `repo_integration/repo-update-checklist.md` | DSR Framework repository update checklist. |
| `sources/` | Source reviews and supporting structured materials copied from the working context. |
| `scripts/build_whitepaper_pdf.py` | PDF build path that wraps long display content and injects visible row rules into generated LaTeX tables. |
| `scripts/check_whitepaper_build.py` | Regression check for title-page metadata, heading numbering, citation setup, and PDF text defects. |
| `llms.txt` | AI-legible summary and file map. |

## License and rights

Original project-authored white paper text, metadata, and package materials are intended to follow the repository's maximally open non-code policy: CC0-1.0. Citation is appreciated for scholarly traceability but is not a license condition. Executable tooling follows the repository code-license policy, currently Apache-2.0 unless otherwise marked.

Third-party sources, cited works, trademarks, source PDFs, and source-derived quotations are not relicensed by this package. Before public deposit, review source-derived text and remove or rewrite anything that is too close to copyrighted source material.

## Build

```bash
python scripts/assemble_whitepaper.py
make html
make pdf
python scripts/check_whitepaper_build.py
```

If `make` is unavailable, run `python scripts/build_whitepaper_pdf.py --pdf-engine <path-to-tectonic-or-other-engine>` for the PDF path so table row rules and overflow checks remain active. If Pandoc or LaTeX is unavailable, the canonical source remains `whitepaper/whitepaper_unified.md`.
