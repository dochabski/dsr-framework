# DSR Framework v1.4.0

DSR Framework v1.4.0 adds a minimal viable L1/L2 documentation pathway for users who need documented or reviewable DSR artifact records without adopting the full L4 package structure.

## Conformance claim

This release preserves `l4_reusable_stable` package conformance for the DSR Framework host package.

The new minimal pathway supports downstream `l1_documented` and `l2_reviewable` documentation. It does not certify downstream artifacts as L3, L4, or L5.

This release does not claim `l5_archival_publication_ready` status.

## DOI

Zenodo DOI: [10.5281/zenodo.20241016](https://doi.org/10.5281/zenodo.20241016)

Zenodo record: [https://zenodo.org/records/20241016](https://zenodo.org/records/20241016)

## Highlights

- Added `docs/protocol/l1-l2-minimal-documentation-pathway.md`.
- Added minimal L1 and L2 YAML templates.
- Added a minimal L1/L2 README template.
- Added a minimal L1/L2 checklist and JSON Schema.
- Added `examples/minimal-l1-l2-package/` as a small L2 example.
- Added `scripts/validate-minimal-l1-l2.py` for lightweight local validation.
- Added retained v1.4.0 metadata-freeze, release, and approval records.

## Validation

The release commit passed:

```bash
python scripts/validate-minimal-l1-l2.py examples/minimal-l1-l2-package --level l2
python scripts/validate-package.py --write-summary
python scripts/validate-package.py --release-candidate --write-summary
git diff --check
```

## Known limitations

- L5 archival/publication-ready status is not claimed.
- External empirical reuse validation is not claimed.
- The minimal pathway is a lightweight documentation lane, not a replacement for the full L4 reusable-stable package structure.
- Source PDFs are not redistributed in this repository.
