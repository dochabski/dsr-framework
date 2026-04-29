# DSR Framework v1.0.1

DSR Framework v1.0.1 is a patch release for the v1 stable line.

## Conformance claim

This release preserves `l4_reusable_stable` package conformance.

It does not claim `l5_archival_publication_ready` status. L5 archival/publication-ready work remains post-v1 work requiring separate preservation, registry, metadata, independent-review, and approval evidence.

## Changes

- Added a retained core scope-boundary decision record.
- Added a README scope-boundary section explaining that the repository operationalizes canonical DSR as a GitHub-native artifact package.
- Distinguished core framework, support layer, and extension layer materials.
- Clarified that the repository is not an exhaustive theory of DSR, a replacement for DSR literature, a universal disciplinary standard, or a downstream validation guarantee.

## Validation

The release commit passes:

```bash
python scripts/validate-package.py --write-summary
python scripts/validate-package.py --release-candidate --write-summary
git diff --check
```

## Known limitations

- L5 archival/publication-ready status is not claimed.
- External empirical reuse validation is not claimed.
- Zenodo publication is not performed by this patch release task.

## Citation

Use `CITATION.cff` for citation metadata and the repository license notice for reuse terms.
