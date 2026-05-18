# Appendix C: Codex build plan {.unnumbered}

This package is optimized so Codex can finish the release with minimal token use.

## Files Codex should read first {.unnumbered}

1. `README.md`
2. `codex_handoff.md`
3. `whitepaper/whitepaper_unified.md`
4. `whitepaper/references.bib`
5. `publication_strategy.md`
6. `repo_integration/repo-update-checklist.md`

## Files Codex should avoid reading unless necessary {.unnumbered}

1. `sources/dsr-source-operational-extractions-unified-part001.yaml`
2. `sources/dsr-source-operational-extractions-unified-part002.yaml`
3. Any full extraction YAML unless revising source registry appendices.

## First Codex task {.unnumbered}

Apply the citation/build patch, run the Markdown assembly script, render HTML and PDF if Pandoc/LaTeX are available, and update only the necessary repository index files. Do not tag, create a GitHub release, publish to Zenodo, or publish externally until final human edit and metadata freeze.

## Build commands {.unnumbered}

```bash
python scripts/assemble_whitepaper.py
make html
make pdf
python scripts/check_whitepaper_build.py
```

If LaTeX is not available, skip PDF and produce HTML plus unified Markdown.
