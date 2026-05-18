# DSR Framework White Paper v1.0.1

This patch release republishes *From Design Science Research Theory to Repository-Native Operationalization: A White Paper for the DSR Framework* with corrected PDF layout.

Zenodo DOI: https://doi.org/10.5281/zenodo.20271949

## Changes

- Fixes long display content that could run past the PDF page boundary.
- Adds visible row separation to generated PDF tables.
- Adds a repeatable PDF build script that injects row rules into Pandoc/LaTeX longtable output.
- Adds build checks that fail on overlong fenced-code lines, overfull hbox warnings, or missing table row-rule insertion.
- Rebuilds the unified Markdown, HTML, and PDF outputs.

## Included artifacts

- Unified Markdown manuscript: `artifacts/dsr-framework-white-paper/whitepaper/whitepaper_unified.md`
- HTML build: `artifacts/dsr-framework-white-paper/build/dsr-framework-whitepaper.html`
- PDF build: `artifacts/dsr-framework-white-paper/build/dsr-framework-whitepaper.pdf`
- BibTeX references: `artifacts/dsr-framework-white-paper/whitepaper/references.bib`
- Publication strategy and service-integration metadata
- Metadata freeze, release, approval, citation/build audit, and final read/edit records

## License and rights

Original project-authored white paper text, metadata, and package materials are dedicated under `CC0-1.0` to maximize reuse, indexing, adaptation, translation, redistribution, and AI/human legibility.

Executable tooling follows the repository code-license policy. Third-party sources, cited works, source PDFs, trademarks, and source-derived quotations are not relicensed by this release.

## Non-claims

This white paper release does not claim:

- L5 archival/publication-ready conformance for the DSR Framework package;
- independent external scholarly peer review;
- empirical validation of DSR Framework effectiveness;
- certification of downstream artifacts;
- redistribution rights over third-party source PDFs or cited works.

## Validation

The release preparation commit passed:

```bash
python artifacts/dsr-framework-white-paper/scripts/check_whitepaper_build.py
python scripts/validate-package.py --write-summary
python scripts/validate-package.py --release-candidate --write-summary
git diff --check
```

