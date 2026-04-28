<!-- SPDX-License-Identifier: CC0-1.0 -->

# DSR Framework v1.0.0

DSR Framework v1.0.0 is the first stable release of the Design Science Research Framework artifact package.

## Conformance claim

This release claims `l4_reusable_stable` package conformance.

It does not claim `l5_archival_publication_ready` status. L5 archival/publication-ready work remains post-v1 work requiring separate preservation, registry, metadata, independent-review, and approval evidence.

## Highlights

- Stabilized root package controls and release metadata.
- Added v1 claim-level traceability for major framework claims.
- Added canonical minimal worked example.
- Stabilized templates and checklists for reuse.
- Hardened JSON Schema validation.
- Upgraded validation automation for v1 release-candidate checks.
- Added retained completeness, kick-the-tires, full-review, author-response, metadata-freeze, and release records.

## Validation

The release commit must pass:

```bash
python scripts/validate-package.py --write-summary
python scripts/validate-package.py --release-candidate --write-summary
git diff --check
```

## Known limitations

- L5 archival/publication-ready status is not claimed.
- External empirical reuse validation is not claimed.
- The canonical example is synthetic and demonstrative.
- Source PDFs are not redistributed in this repository.

## Citation

Use `CITATION.cff` for citation metadata and the repository license notice for reuse terms.
