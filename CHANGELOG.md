<!-- SPDX-License-Identifier: CC0-1.0 -->

# Changelog

## Unreleased

- No unreleased changes.

## [1.0.1] - 2026-04-29

### Added

- Added retained scope-boundary decision record clarifying the core framework, support layer, and extension layer.

### Changed

- Clarified that the repository operationalizes canonical DSR as a GitHub-native artifact package, not as an exhaustive DSR theory, replacement for DSR literature, universal disciplinary standard, or downstream validation guarantee.
- Updated release-facing metadata for the v1.0.1 patch release while preserving `l4_reusable_stable` conformance and `l5_claimed: false`.

### Validation

- Public validation passes with controlled inventory alignment.
- Release-candidate validation passes for the v1 L4 reusable-stable gate.
- v1.0.1 does not claim external empirical reuse validation or L5 archival/publication-ready status.

## [1.0.0] - 2026-04-28

### Added

- Added v1 claim-level traceability for major framework claims.
- Added canonical minimal DSR worked example package.
- Added retained completeness, kick-the-tires, full-review, author-response, metadata-freeze, and v1 release records.
- Added package validation automation for public-draft and v1 L4 release-candidate validation.
- Added structured GitHub issue templates, public-draft decision/tailoring records, and LF normalization policy.

### Changed

- Promoted current package status to `1.0.0_stable` and package conformance to `l4_reusable_stable`.
- Preserved `l5_claimed: false`; L5 archival/publication-ready work remains post-v1.
- Hardened schemas and added canonical example schema-instance validation fixtures.
- Stabilized templates and checklists against the canonical example.
- Reconciled manifest, metadata, artifact profile, conformance declaration, package inventory, citation metadata, CodeMeta, and Zenodo metadata for v1.0.0.

### Validation

- Public validation passes with controlled inventory alignment.
- Release-candidate validation is expected to pass after the release approval record is added.
- v1.0.0 does not claim external empirical reuse validation or L5 archival/publication-ready status.

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
