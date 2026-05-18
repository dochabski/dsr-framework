# Appendix C. Codex Build Plan

This package is optimized so Codex can finish the release with minimal token use.

## Files Codex should read first

1. `README.md`
2. `codex_handoff.md`
3. `whitepaper/whitepaper_unified.md`
4. `publication_strategy.md`
5. `repo_integration/repo-update-checklist.md`

## Files Codex should avoid reading unless necessary

1. `sources/dsr-source-operational-extractions-unified-part001.yaml`
2. `sources/dsr-source-operational-extractions-unified-part002.yaml`
3. Any full extraction YAML unless revising source registry appendices.

## First Codex task

Create a branch in the DSR Framework repo, add this package under `artifacts/dsr-framework-white-paper/`, run the Markdown assembly script, render HTML and PDF if Pandoc/LaTeX are available, and update only the necessary repository index files.

## Build commands

```bash
python scripts/assemble_whitepaper.py
make html
make pdf
```

If LaTeX is not available, skip PDF and produce HTML plus unified Markdown.
