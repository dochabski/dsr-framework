<!-- SPDX-License-Identifier: CC0-1.0 -->

# Changelog

## Unreleased

### Added

- Added v1 readiness audit and conformance-target decision records.
- Added package validation script and GitHub Actions workflow for public-draft validation.
- Added retained machine-readable validation summary under `records/validation/`.
- Added optional release-candidate validation mode and workflow dispatch input.

### Changed

- Normalized v0.1.0 status as a citable public draft with qualified L2 reviewability evidence.
- Set the v1.0.0 stable target to L4 reusable and deferred L5 archival/publication-ready claims until preservation, registry, metadata-freeze, and independent-review gates pass.
- Updated package inventory to include validation automation and to mark empty public-draft areas as planned rather than silently complete.
- Cleaned v0.1.0 release-record facts so confirmed GitHub/Zenodo details are separated from future v1/L5 follow-up.
- Separated file-level and package-level conformance fields in root-facing metadata.
- Hardened validation for release-record contradictions, conformance-scope ambiguity, Unicode control characters, documentation link coverage, and release-candidate gates.

## [0.1.0] - 2026-04-27

### Added

- Initial public draft DSR Framework package for planning, documenting, evaluating, reviewing, and publishing Design Science Research artifacts and artifact packages.
- Root metadata, manifest, artifact profile, package inventory, conformance declaration, citation metadata, Zenodo metadata, CodeMeta metadata, REUSE metadata, and open license files.
- Product specifications, models, vocabularies, schemas, templates, checklists, protocol documentation, and retained records.
- `crosswalks/source-to-framework-alignment.yaml` mapping all 71 repaired DSR corpus sources to framework constructs, evidence anchors, grounding decisions, target paths, exclusions, and evidence status.

### Changed

- Updated crosswalk summary counts after source-traceability remediation: 0 source-basis-only sources, 0 single-file substantive sources, 71 multi-file substantive sources, and 142 substantive trace objects.
- Updated root metadata and citation files to use `dochabski/dsr-framework`, `v0.1.0`, CC0-1.0, and reserved Zenodo DOI `10.5281/zenodo.19835424`.
- Excluded `FRAMEWORK_AUDIT_2026-04-27.md` and `_unmapped/` generated staging archives from the mapped public package.

### Validation

- YAML, JSON, and CFF parse checks pass.
- JSON Schema meta-validation and known schema/template/record validation pairs pass.
- Source traceability validation passes for all 71 repaired corpus sources.

### Known Limitations

- This is a public draft release under active validation, not a stable 1.0 framework.
- External utility evaluation and independent reuse evidence remain future work.
- The Zenodo DOI is published at https://zenodo.org/records/19835424.
