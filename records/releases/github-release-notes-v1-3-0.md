# DSR Framework v1.3.0

DSR Framework v1.3.0 adds a controlled DSR assessment rubric collection while preserving the existing L4 reusable-stable package posture.

## Conformance claim

This release continues to claim `l4_reusable_stable` package conformance.

It does not claim `l5_archival_publication_ready` status. L5 archival/publication-ready work remains post-v1 work requiring separate preservation, registry, metadata, independent-review, and approval evidence.

## Highlights

- Adds 15 individual DSR assessment rubric YAML files under `rubrics/`.
- Adds `rubrics/dsr_assessment_rubrics_unified.yaml` as a generated single-document collection for review, search, AI ingestion, and distribution convenience.
- Keeps individual rubric YAML files as the canonical editable source records.
- Adds `scripts/build-rubric-collection.py` for deterministic collection regeneration.
- Adds `rubrics/README.md` explaining source-of-truth and regeneration policy.
- Updates package inventory, repository map, release metadata, and retained release records.

## Validation

The release commit passes:

```bash
python scripts/build-rubric-collection.py --date 2026-05-16
python scripts/validate-package.py --write-summary
python scripts/validate-package.py --release-candidate --write-summary
git diff --check
```

## Archival record

Zenodo DOI: [10.5281/zenodo.20238033](https://doi.org/10.5281/zenodo.20238033)

Zenodo record: [https://zenodo.org/records/20238033](https://zenodo.org/records/20238033)

## Known limitations

- L5 archival/publication-ready status is not claimed.
- External empirical reuse validation is not claimed.
- Rubrics guide assessment and review but do not replace reviewer judgment.
- The unified collection reports missing dependency references rather than fabricating absent rubrics.
- Source PDFs and copyrighted source documents are not redistributed in this repository.
