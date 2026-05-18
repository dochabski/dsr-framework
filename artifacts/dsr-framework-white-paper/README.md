# DSR Framework White Paper Package

This package contains a draft white paper and release-preparation scaffold for turning the DSR theory synthesis materials into a citable, repository-native white paper.

## Decision

Use a **repository-native methodological white paper with an open artifact package**. The canonical release path should be:

1. GitHub repository package as living source of truth.
2. Zenodo archive of a versioned GitHub release for DOI citation.
3. OSF project/preprint as discovery hub after the GitHub draft is stable.
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
| `scripts/check_whitepaper_build.py` | Regression check for title-page metadata, heading numbering, citation setup, and PDF text defects. |
| `llms.txt` | AI-legible summary and file map. |

## Build

```bash
python scripts/assemble_whitepaper.py
make html
make pdf
python scripts/check_whitepaper_build.py
```

If `make` is unavailable, run the equivalent Pandoc commands directly with `--citeproc`. If Pandoc or LaTeX is unavailable, the canonical source remains `whitepaper/whitepaper_unified.md`.
