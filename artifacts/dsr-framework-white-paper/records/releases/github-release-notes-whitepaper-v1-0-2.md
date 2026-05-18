# DSR Framework White Paper v1.0.2

This patch release republishes *From Design Science Research Theory to Repository-Native Operationalization: A White Paper for the DSR Framework* with corrected PDF table-header styling.

Zenodo DOI: https://doi.org/10.5281/zenodo.20272519

## Changes

- Fixes generated PDF tables whose header rows were visually indistinguishable from body rows.
- Adds a systemic Pandoc/LaTeX build patch that applies a light header band and bold header text to generated `longtable` headers.
- Preserves the v1.0.1 visible row-separation fix for human-legible table bodies.
- Updates the build regression check so future PDFs must record both table-header styling and row-rule insertion.
- Rebuilds the PDF output from the repeatable white-paper build script.

## Included artifacts

- Unified Markdown manuscript: `artifacts/dsr-framework-white-paper/whitepaper/whitepaper_unified.md`
- HTML build: `artifacts/dsr-framework-white-paper/build/dsr-framework-whitepaper.html`
- PDF build: `artifacts/dsr-framework-white-paper/build/dsr-framework-whitepaper.pdf`
- BibTeX references: `artifacts/dsr-framework-white-paper/whitepaper/references.bib`
- Publication strategy and service-integration metadata
- Metadata freeze, release, approval, citation/build audit, final read/edit, and publication-verification records

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
