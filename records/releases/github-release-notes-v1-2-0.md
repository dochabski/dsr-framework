# DSR Framework v1.2.0

DSR Framework v1.2.0 is a minor release for the v1 stable line.

## Conformance Claim

This release preserves `l4_reusable_stable` package conformance for the host DSR Framework package.

It does not claim `l5_archival_publication_ready` status. L5 archival/publication-ready work remains post-v1 work requiring separate preservation, registry, metadata, independent-review, and approval evidence.

## Changes

- Added `docs/wicked-problem-resolution-workflow.md` as a controlled process artifact.
- The workflow guides DSR-oriented movement from wicked problem framing to stakeholder/context modeling, causal diagnosis, requirements derivation, artifact intervention design, safe-to-fail evaluation, claim-evidence alignment, and reusable design-knowledge capture.
- Reconciled package inventory, manifest pointers, release metadata, and validation summary.

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
- The workflow is process guidance and does not certify any downstream wicked-problem intervention.
- Source PDFs are not redistributed in this repository.

## Citation

Use `CITATION.cff` for citation metadata and the repository license notice for reuse terms.
