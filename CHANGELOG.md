<!-- SPDX-License-Identifier: CC0-1.0 -->

# Changelog

## Unreleased

- Recorded Zenodo DOI `10.5281/zenodo.20241016` and publication verification for v1.4.0.
- Added draft DSR Framework white paper package under `artifacts/dsr-framework-white-paper/`.
- Added white paper Markdown chapters, unified Markdown, HTML/PDF builds, metadata templates, source map, publication strategy, and manual platform checklist.
- Fixed draft white paper Pandoc metadata, heading numbering, citeproc references, and build regression checks.
- Clarified maximally open CC0-1.0 rights posture for original white paper package content and metadata.
- Prepared DSR Framework white paper v1.0.0 release records, final read/edit record, metadata freeze, release approval, and GitHub release notes.
- Recorded Zenodo DOI `10.5281/zenodo.20264299` and publication verification for the DSR Framework white paper v1.0.0 release.
- Recorded public OSF project `https://osf.io/wytgc/` and ORCID DOI work dissemination for the DSR Framework white paper v1.0.0 release.
- Recorded MetaArXiv preprint submission `https://osf.io/preprints/metaarxiv/ebf8m_v1` for the DSR Framework white paper v1.0.0 release as pending OSF Preprints moderation.
- Fixed white paper PDF layout by wrapping long display content, adding visible table row separation, and making the PDF build check fail on overlong fenced lines or overfull hbox warnings.
- Prepared white paper v1.0.1 patch release metadata for corrected GitHub, Zenodo, OSF, and MetaArXiv publication.
- Recorded white paper v1.0.1 publication verification for GitHub release `whitepaper-v1.0.1`, Zenodo DOI `10.5281/zenodo.20271949`, OSF project file updates, MetaArXiv metadata update, and ORCID work update.
- Fixed white paper PDF table headers by adding a systemic longtable header styling patch and build regression check.
- Prepared white paper v1.0.2 patch release metadata for corrected GitHub, Zenodo, OSF, MetaArXiv, and ORCID publication.
- Recorded white paper v1.0.2 publication verification for GitHub release `whitepaper-v1.0.2`, Zenodo DOI `10.5281/zenodo.20272519`, MetaArXiv metadata update, and OSF/ORCID follow-up status.

## [1.4.0] - 2026-05-16

### Added

- Added `docs/protocol/l1-l2-minimal-documentation-pathway.md` for users who need L1 documented or L2 reviewable DSR records without adopting the full L4 package structure.
- Added minimal L1 and L2 YAML templates, a minimal pathway README template, checklist, JSON Schema, example package, and lightweight validator.
- Added retained v1.4.0 metadata-freeze, release, release-approval, and GitHub release-note records.
- Recorded Zenodo DOI `10.5281/zenodo.20238033` and publication verification for v1.3.0.
- Added JSON sidecar for the unified DSR assessment rubric collection.
- Added rubric-generation process/provenance files under `rubrics/process/`.

### Changed

- Updated release-facing metadata for the v1.4.0 minor release while preserving `l4_reusable_stable` conformance and `l5_claimed: false`.
- Updated package inventory and rubric documentation while preserving individual rubric YAML files as canonical.

### Validation

- Minimal L2 example validation passes with `python scripts/validate-minimal-l1-l2.py examples/minimal-l1-l2-package --level l2`.
- Public validation passes with controlled inventory alignment.
- Release-candidate validation passes for the v1 L4 reusable-stable gate.
- v1.4.0 does not claim external empirical reuse validation, downstream artifact validation, or L5 archival/publication-ready status.

## [1.3.0] - 2026-05-16

### Added

- Added `rubrics/` with 15 canonical individual DSR assessment rubric YAML files.
- Added `rubrics/dsr_assessment_rubrics_unified.yaml` as a generated single-document collection for review, search, AI ingestion, and distribution convenience.
- Added `rubrics/README.md` and `scripts/build-rubric-collection.py` for rubric source-of-truth policy and deterministic collection regeneration.
- Added retained v1.3.0 metadata-freeze, release, release-approval, and GitHub release-note records.

### Changed

- Updated release-facing metadata for the v1.3.0 minor release while preserving `l4_reusable_stable` conformance and `l5_claimed: false`.
- Updated repository inventory and validation summary to `210/210` controlled files after rubric and release records are added.

### Validation

- Public validation passes with controlled inventory alignment.
- Release-candidate validation passes for the v1 L4 reusable-stable gate.
- v1.3.0 does not claim external empirical reuse validation, downstream artifact validation, or L5 archival/publication-ready status.

## [1.2.0] - 2026-05-06

### Added

- Added `docs/wicked-problem-resolution-workflow.md` as a controlled DSR-oriented process artifact for moving from wicked problem framing to artifact intervention, evaluation, and design-knowledge capture.
- Added retained v1.2.0 metadata-freeze, release, release-approval, and GitHub release-note records.

### Changed

- Updated release-facing metadata for the v1.2.0 minor release while preserving `l4_reusable_stable` conformance and `l5_claimed: false`.
- Updated repository inventory and validation summary to `188/188` controlled files after release records are added.

### Validation

- Public validation passes with controlled inventory alignment.
- Release-candidate validation passes for the v1 L4 reusable-stable gate.
- v1.2.0 does not claim external empirical reuse validation, downstream artifact validation, or L5 archival/publication-ready status.

## [1.1.0] - 2026-05-05

### Added

- Added the nested DSR theory operational kernel artifact package under `artifacts/dsr-theory-operational-kernel/`.
- Added retained self-application validation records comparing `documentation-protocol` and `dsr-framework` against the DSR theory operational kernel.
- Added crosswalks from the theory kernel to both repository layers and per-target validation records.

### Changed

- Updated release-facing metadata for the v1.1.0 minor release while preserving `l4_reusable_stable` conformance and `l5_claimed: false`.
- Updated repository inventory and validation summary to `183/183` controlled files after release records are added.

### Validation

- Public validation passes with controlled inventory alignment.
- Release-candidate validation passes for the v1 L4 reusable-stable gate.
- v1.1.0 does not claim external empirical reuse validation, downstream artifact validation, standalone kernel stable release, or L5 archival/publication-ready status.

## [1.0.2] - 2026-05-02

### Changed

- Reconciled release-facing conformance language across README, artifact profile, conformance declaration, manifest, and package inventory with the current v1 L4 reusable-stable claim.
- Hardened validation so stale pre-v1/public-draft contradiction phrases fail when the package is in L4 reusable-stable state.
- Updated release metadata for the v1.0.2 patch release while preserving `l4_reusable_stable` conformance and `l5_claimed: false`.

### Validation

- Public validation passes with controlled inventory alignment.
- Release-candidate validation passes for the v1 L4 reusable-stable gate.
- v1.0.2 does not claim external empirical reuse validation or L5 archival/publication-ready status.

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
