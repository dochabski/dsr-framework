# DSR Framework v1.0.2

DSR Framework v1.0.2 is a patch release for the v1 stable line.

## Conformance Claim

This release preserves `l4_reusable_stable` package conformance.

It does not claim `l5_archival_publication_ready` status. L5 archival/publication-ready work remains post-v1 work requiring separate preservation, registry, metadata, independent-review, and approval evidence.

## Changes

- Reconciled README, artifact profile, conformance declaration, manifest, and package inventory wording with the current L4 reusable-stable claim.
- Clarified that L5 archival/publication-ready status, empirical framework utility, independent external review, and automatic downstream artifact validation are outside the current claim.
- Hardened validation so stale pre-v1/public-draft contradiction phrases fail when the package is in L4 reusable-stable state.

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
- Zenodo publication is not performed by this patch release task.
- The DSR theory operationalization artifact package remains future work.

## Citation

Use `CITATION.cff` for citation metadata and the repository license notice for reuse terms.
