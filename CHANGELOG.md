<!-- SPDX-License-Identifier: CC0-1.0 -->

# Changelog

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
