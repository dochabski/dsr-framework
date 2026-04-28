<!--
SPDX-License-Identifier: CC0-1.0
item_id: root_readme
item_type: description
selection_id: root_readme
status: 0.1.0_public_draft
version: 0.1.0
conformance_target: l2_reviewable_qualified_public_draft
-->

# Design Science Research Framework

The **Design Science Research (DSR) Framework** is a protocol-governed artifact package for planning, documenting, evaluating, reviewing, and publishing Design Science Research artifacts. It is intended to help researchers and reviewers make DSR work more explicit, reusable, reviewable, and citable without collapsing DSR into ordinary consulting, routine software delivery, or purely explanatory research.

This repository treats DSR as a research tradition centered on purposeful artifact development, build-and-evaluate reasoning, relevance to real-world problem contexts, grounding in rigorous knowledge bases, and contribution to reusable design knowledge. The framework also foregrounds DSR-specific concerns that often require more operational support: artifact ontology, contribution positioning, transparency, validity, reliability, replication, projectability, responsible design, and publication readiness.

## Repository status

| Field | Value |
|---|---|
| Package status | `0.1.0_public_draft` -- usable, citable, but still under active validation. |
| Current package version | `0.1.0` |
| Default root README conformance | `L1 documented` |
| Current organization state | Canonical directory structure populated from the product catalog |
| Current validation state | Qualified `L2 reviewable` public-draft evidence: YAML/JSON/CFF parsing passes; schema/template and schema/record validation pairs pass; all 71 repaired corpus sources are multi-file substantively grounded |
| Intended package trajectory | `1.0.0-rc.N` toward `1.0.0_stable` with an `L4 reusable` target; `L5 archival/publication-ready` is reserved for a later release with independent review, preservation, registry, and metadata-freeze evidence |
| Primary audience | DSR researchers, doctoral supervisors, methods instructors, reviewers, editors, and artifact-package maintainers |
| Primary use | Establish a public entry point for a reusable DSR documentation and review framework |

## Release progression

This repository uses a controlled status progression: `0.1.0_public_draft`, `1.0.0-rc.N`, and `1.0.0_stable`. The current release is published and citable as a public draft with qualified L2 reviewability evidence. It is not a stable 1.0 framework, not L3 exercisable, not L4 reuse-validated, and not L5 archival/publication-ready.

The selected v1 target is `l4_reusable_stable`. L5 archival/publication-ready status requires a separate release decision with completed preservation, metadata-freeze, registry, independent-review, and release-approval records.

## What this framework provides

The framework is organized as a compound DSR artifact package. Its intended products include:

1. **Specifications** for repository architecture, artifact packages, lifecycle and contribution modeling, quality review, publication readiness, and validation.
2. **Models** for the DSR lifecycle, artifact ontology, contribution positioning, evaluation alignment, transparency, reliability, replication, and projectability.
3. **Vocabularies** for artifact types, contribution types, knowledge goals, knowledge scopes, lifecycle stages, evaluation families, validity types, reliability types, replication types, transparency dimensions, genre types, responsible-design values, and aesthetics dimensions.
4. **Schemas** for validating structured project records, artifact profiles, evaluation plans, evaluation reports, contribution claims, package inventories, and transparency crosswalks.
5. **Templates and checklists** for researchers who need operational DSR documentation artifacts rather than only prose guidance.
6. **Records** that retain evidence of source basis, decisions, contribution positioning, transparency, evaluation, review, release, and preservation events.
7. **Human-facing documentation** that explains the controlled YAML, JSON Schema, and record files in a form usable by researchers and reviewers.

## Repository map

The organized framework package uses the following top-level structure.

| Path | Role |
|---|---|
| `README.md` | Public repository entry point and orientation file. |
| `LICENSE` | Repository licensing notice. |
| `CITATION.cff` | Draft citation metadata for repository users. |
| `CHANGELOG.md` | Human-readable change history. |
| `CONTRIBUTING.md` | Contribution workflow and expectations. |
| `GOVERNANCE.md` | Governance, maintainership, and decision authority. |
| `SECURITY.md` | Security and vulnerability reporting expectations. |
| `CODE_OF_CONDUCT.md` | Community conduct expectations. |
| `.zenodo.json` | Zenodo archival and DOI metadata. |
| `manifest.yaml` | Canonical package manifest and repository identity. |
| `REUSE.toml` | Machine-readable repository license annotations. |
| `codemeta.json` | CodeMeta-compatible citation and repository metadata. |
| `metadata.yaml` | Structured project metadata. |
| `artifact-profile.yaml` | Controlled artifact identity, scope, claims, conformance, and reuse constraints. |
| `package-inventory.yaml` | Controlled inventory of package files, expected validation responsibilities, and review status. |
| `conformance-declaration.yaml` | Declared conformance level, tailoring decisions, and package obligations. |
| `specs/` | Controlled product specifications. |
| `models/` | Conceptual and operational DSR models. |
| `vocabularies/` | Controlled vocabularies used by templates, schemas, records, and checklists. |
| `schemas/` | JSON Schema files for structured validation. |
| `templates/` | Reusable project, artifact, evaluation, contribution, and transparency templates. |
| `checklists/` | Quality, readiness, transparency, evaluation, contribution, reliability, and projectability checklists. |
| `docs/protocol/` | Human-facing protocol documentation. |
| `records/` | Retained evidence of decisions, source basis, tailoring, reviews, evaluations, releases, and preservation. |
| `crosswalks/` | Mappings among source traditions, framework products, protocol concepts, and DSR constructs. |
| `examples/` | Demonstration packages and worked examples, separated from required package-control files. |

## How to use the framework

### For a researcher planning a DSR study

Start with the artifact and problem definition materials:

1. Define the problem context, stakeholders, objectives, requirements, and success criteria.
2. Identify the artifact type and artifact boundary.
3. Clarify whether the contribution is primarily a new artifact, a method extension, a design theory contribution, a framework, a taxonomy, an evaluation contribution, or a reusable package contribution.
4. Plan demonstration separately from evaluation.
5. Map expected evidence to artifact utility, artifact quality, and contribution-to-knowledge claims.
6. Record transparency evidence across process, problem space, solution space, build, evaluation, and contribution.

### For a reviewer evaluating a DSR submission

Use the checklists and records to examine whether the work:

1. Has a clear DSR identity rather than only a local implementation or retrospective framing.
2. Defines the artifact and its boundary with enough precision to support review.
3. Connects problem relevance to a grounded solution space.
4. Separates demonstration, evaluation, and contribution claims.
5. Provides sufficient evidence for claimed utility, quality, validity, reliability, and projectability.
6. States limitations, non-goals, and boundary conditions without overclaiming generalization or replication.

### For a maintainer preparing a public release

Use the package-control files:

1. Confirm that `artifact-profile.yaml` describes the artifact package identity and claims.
2. Confirm that `package-inventory.yaml` lists required files, validation responsibilities, and review status.
3. Confirm that `conformance-declaration.yaml` declares the current conformance level and tailoring decisions.
4. Confirm that records exist for source basis, review, evaluation, release, and preservation.
5. Validate structured YAML and JSON-compatible files against their schemas where schemas are available.
6. Prepare citation and archival metadata before release.

## Conformance levels

The framework uses staged conformance so the package can mature without overclaiming readiness.

| Level | Label | Meaning |
|---|---|---|
| `L0` | Draft | Content exists but is not yet complete or internally checked. |
| `L1` | Documented | Purpose, scope, file role, and basic dependencies are documented. |
| `L2` | Reviewable | Content has explicit acceptance criteria, traceability, and review logic. |
| `L3` | Exercisable | Templates, schemas, examples, or validation procedures can be exercised by users. |
| `L4` | Reusable | The package is sufficiently coherent and documented for adaptation by others. |
| `L5` | Archival / publication-ready | The package is release-ready, citable, preserved, and supported by final review records. |

This `README.md` is maintained at `L1 documented` conformance. It orients the repository and identifies dependencies. Package-level validation evidence is retained in `manifest.yaml`, `package-inventory.yaml`, schemas, and review records; this README does not certify publication readiness.

## Core DSR distinctions preserved by the framework

The framework is designed to preserve distinctions that are frequently blurred in DSR documentation.

| Distinction | Why it matters |
|---|---|
| Artifact utility vs. artifact quality vs. knowledge contribution | A useful local artifact is not automatically a publishable design-knowledge contribution. |
| Demonstration vs. evaluation | Showing an artifact in use is not the same as evaluating its fitness, effects, or contribution claims. |
| Artifact instance vs. artifact type | A concrete implementation may instantiate a more general artifact, method, model, or design principle. |
| Idiographic vs. nomothetic scope | Some claims are local and contextual; others are intended to be projectable across a class of problems. |
| Problem space vs. solution space | Relevance requires explicit problem framing; rigor requires grounding in existing knowledge and candidate solutions. |
| Build transparency vs. evaluation transparency | Artifact construction and artifact assessment need different documentation evidence. |
| Replication vs. projectability | Exact replication may be inappropriate for situated DSR, while transparent context and boundary conditions can support adaptation and cumulative knowledge. |
| Consulting or implementation vs. DSR | DSR requires contribution to design knowledge, not merely delivery of a local artifact. |

## Evidence basis

The framework is grounded in two evidence families:

1. **Documentation Protocol alignment**: repository structure, controlled information items, package metadata, records, validation logic, and release conventions.
2. **DSR extraction corpus**: curated source extractions from scholarly DSR literature covering artifact ontology, design knowledge, lifecycle models, evaluation, transparency, contribution types, validity, reliability, replication, projectability, and publication norms.

The source-to-framework alignment pass maps all 71 repaired DSR corpus sources to substantive non-source-basis framework targets. The retained crosswalk is `crosswalks/source-to-framework-alignment.yaml`; it records evidence anchors, supported constructs, grounding decisions, target paths, and exclusions. The repaired extraction corpus remains outside this public package directory, and original extraction files remain preserved for auditability.

## Quality gates

Generated framework files should be reviewed against six package-level quality gates.

| Gate | Review question |
|---|---|
| Consistency | Does the file follow naming, item-type, status, and repository conventions? |
| Coherence | Does the file align with related products, schemas, templates, records, and documentation? |
| Cogency | Can the intended user understand and apply the file without hidden assumptions? |
| Correspondence | Does the file support the DSR Framework as a reviewable and reusable artifact package? |
| DSR transparency | Does the file support the relevant transparency dimensions, or explain why a dimension is not applicable? |
| Reviewability | Can a reviewer evaluate the file against explicit criteria, evidence, or validation logic? |

## Current limitations

This repository is under active construction. Users should treat the framework as a developing artifact package rather than a finished standard.

Known limitations at this stage:

- The root README provides orientation but not a complete controlled specification.
- Required root files are present, and public repository, creator, maintainer, release, license, and DOI facts are recorded for v0.1.0; stable v1 metadata still needs a separate freeze record.
- Source-to-framework traceability is repaired for all 71 corpus sources; claim-level traceability remains uneven and needs a dedicated v1 mapping pass.
- Schemas validate the current templates and records, but they should be tightened field-by-field after structure and vocabulary decisions stabilize.
- Example packages should not be treated as evaluation evidence unless a corresponding evaluation record exists.
- L4/L5 readiness should not be claimed until validation automation, example use, review, preservation, and release records support those levels.

## Recommended next work

For the repository to move beyond organized draft status, complete these work items next:

1. Finish the v1 readiness audit and keep root metadata, conformance, inventory, release records, and citation files consistent.
2. Tighten schemas from permissive structure validation toward stricter field-level validation.
3. Add a canonical worked example package after templates and validation expectations stabilize.
4. Convert source-level grounding into claim-level traceability.
5. Add retained review, preservation, metadata-freeze, and release-approval records before any stable v1 or L5 claim.

## Citation and reuse

Use the repository citation metadata in `CITATION.cff`, the repository license notice in `LICENSE`, and the archived-release metadata in `.zenodo.json`. This v0.1.0 package is a public draft: citable and reusable, but still under active validation and not yet a stable 1.0 framework.

## Maintainer note

This file is a human-facing repository entry point. Controlled source-of-truth content should live in structured files such as `manifest.yaml`, `metadata.yaml`, `artifact-profile.yaml`, `package-inventory.yaml`, `conformance-declaration.yaml`, and product specifications under `specs/`.
