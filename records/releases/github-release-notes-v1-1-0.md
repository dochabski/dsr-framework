# DSR Framework v1.1.0

DSR Framework v1.1.0 is a minor release for the v1 stable line.

## Conformance Claim

This release preserves `l4_reusable_stable` package conformance for the host DSR Framework package.

It does not claim `l5_archival_publication_ready` status. L5 archival/publication-ready work remains post-v1 work requiring separate preservation, registry, metadata, independent-review, and approval evidence.

## Changes

- Added a nested DSR theory operational kernel artifact package under `artifacts/dsr-theory-operational-kernel/`.
- Added retained self-application validation comparing `documentation-protocol` and `dsr-framework` against the theory kernel.
- Added per-target validation records and crosswalks for the two-repository architecture.
- Reconciled nested artifact inventory, root package inventory, manifest pointers, and validation summary.

## Validation

The release commit passes:

```bash
python scripts/validate-package.py --write-summary
python scripts/validate-package.py --release-candidate --write-summary
git diff --check
```

## Known Limitations

- L5 archival/publication-ready status is not claimed.
- External empirical reuse validation is not claimed.
- The nested DSR theory operational kernel remains draft L2 reviewable evidence, not a standalone stable release.
- Source PDFs are not redistributed in this repository.
- Zenodo publication is not performed by this release-preparation task.

## Citation

Use `CITATION.cff` for citation metadata and the repository license notice for reuse terms.
