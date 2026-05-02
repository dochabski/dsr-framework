<!--
SPDX-License-Identifier: CC0-1.0
item_id: root_readme
item_type: description
selection_id: root_readme
status: 1.0.1_stable
version: 1.0.1
file_conformance: l1_documented
package_conformance: l4_reusable_stable
l5_claimed: false
-->

# Design Science Research Framework

The **Design Science Research (DSR) Framework** is a protocol-governed artifact package for planning, documenting, evaluating, reviewing, and publishing Design Science Research artifacts. It is intended to help researchers and reviewers make DSR work more explicit, reusable, reviewable, and citable without collapsing DSR into ordinary consulting, routine software delivery, or purely explanatory research.

This repository treats DSR as a research tradition centered on purposeful artifact development, build-and-evaluate reasoning, relevance to real-world problem contexts, grounding in rigorous knowledge bases, and contribution to reusable design knowledge. The framework also foregrounds DSR-specific concerns that often require more operational support: artifact ontology, contribution positioning, transparency, validity, reliability, replication, projectability, responsible design, and publication readiness.

## Repository status

| Field | Value |
|---|---|
| Package status | `1.0.1_stable` -- reusable stable package, not L5 archival/publication-ready. |
| Current package version | `1.0.1` |
| Default root README conformance | `L1 documented` |
| Current organization state | Canonical directory structure populated from the product catalog |
| Current validation state | `L4 reusable stable` release evidence: YAML/JSON/CFF parsing passes; schema/template, schema/record, and canonical-example validation pairs pass; claim-level traceability, retained review records, metadata freeze, and release record are present |
| Intended package trajectory | `1.0.x_stable`; `L5 archival/publication-ready` is reserved for a later release with independent external review, preservation closure, registry publication, and L5 release approval |
| Primary audience | DSR researchers, doctoral supervisors, methods instructors, reviewers, editors, and artifact-package maintainers |
| Primary use | Establish a public entry point for a reusable DSR documentation and review framework |

## Release progression

This repository uses a controlled status progression: `0.1.0_public_draft`, `1.0.0-rc.N`, and `1.0.x_stable`. The current release is prepared as the stable v1.0.1 framework with L4 reusable-stable package conformance.

L5 archival/publication-ready status is not claimed for v1.0.1. L5 requires a separate release decision with completed preservation closure, registry publication, independent external review, archival fixity evidence, and L5 release approval.

## What this framework provides

The framework is organized as a compound DSR artifact package. Its intended products include:

1. **Specifications** for repository architecture, artifact packages, lifecycle and contribution modeling, quality review, publication readiness, and validation.
2. **Models** for the DSR lifecycle, artifact ontology, contribution positioning, evaluation alignment, transparency, reliability, replication, and projectability.
3. **Vocabularies** for artifact types, contribution types, knowledge goals, knowledge scopes, lifecycle stages, evaluation families, validity types, reliability types, replication types, transparency dimensions, genre types, responsible-design values, and aesthetics dimensions.
4. **Schemas** for validating structured project records, artifact profiles, evaluation plans, evaluation reports, contribution claims, package inventories, and transparency crosswalks.
5. **Templates and checklists** for researchers who need operational DSR documentation artifacts rather than only prose guidance.
6. **Records** that retain evidence of source basis, decisions, contribution positioning, transparency, evaluation, review, release, and preservation events.
7. **Human-facing documentation** that explains the controlled YAML, JSON Schema, and record files in a form usable by researchers and reviewers.

## Scope boundary

The purpose of this repository is to operationalize the canonical Design Science Research (DSR) paradigm as a GitHub-native artifact package.

The repository is not intended to be an exhaustive theory of DSR, a replacement for DSR literature, a universal disciplinary standard, or a guarantee that any downstream artifact has been empirically validated. Its narrower purpose is to make DSR work more explicit, structured, reviewable, reusable, citable, and release-ready.

The framework therefore treats GitHub not merely as a file host or software platform, but as a research artifact stewardship environment. Repository structure, version control, metadata, schemas, templates, checklists, records, crosswalks, examples, and releases are used to make DSR artifacts inspectable across their problem framing, solution grounding, design/build process, demonstration, evaluation, contribution claims, limitations, and reuse conditions.

The core framework includes the materials needed to support this operationalization: DSR models, controlled vocabularies, templates, schemas, checklists, records, crosswalks, examples, documentation, metadata, and release controls.

Companion guides, teaching materials, extended workbooks, discipline-specific adaptations, and advanced modules are supporting or extension materials. They may help users understand or apply the framework, but they are not themselves required for the core framework claim.

## Core, support, and extension layers

| Layer | Role | Examples |
|---|---|---|
| Core framework | Required to operationalize DSR as a reviewable GitHub artifact package | Models, vocabularies, schemas, templates, checklists, records, crosswalks, package metadata, release controls |
| Support layer | Helps users understand, teach, or apply the framework | Companion guide, worked examples, role-based pathways, explanatory documentation |
| Extension layer | Useful for future growth but not required for the v1 core claim | Discipline-specific adaptations, advanced responsible-design modules, expanded pedagogy, automation beyond validation basics |

This distinction prevents the repository from being interpreted as an attempt to exhaustively formalize all of DSR. The v1 package claim is narrower: the repository operationalizes DSR documentation, evaluation, review, reuse, and citation in a structured GitHub-native form.

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

This `README.md` is maintained at `L1 documented` conformance. It orients the repository and identifies dependencies. Package-level L4 validation evidence is retained in `manifest.yaml`, `package-inventory.yaml`, schemas, examples, crosswalks, review records, and release records; this README does not claim L5 archival/publication-ready status.

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

This repository is a stable v1 DSR artifact package, but it remains a bounded framework rather than a finished disciplinary standard.

Known limitations for the current release:

- The root README provides orientation, not the complete controlled specification.
- L4 reusable-stable package conformance is claimed for the current v1 line, but L5 archival/publication-ready status is not claimed.
- The framework has retained source-level and claim-level traceability for major v1 claims, but it does not claim full literature saturation or universal disciplinary consensus.
- The canonical example and validation records support exercisability and reuse-readiness; they do not prove empirical improvement of DSR outcomes or validate downstream artifacts automatically.
- Source PDFs and copyrighted source documents are not redistributed in this repository.
- Independent external review, archival fixity closure, registry publication closure, and any L5 release approval remain post-v1 work.

## Recommended next work

Recommended next work should preserve the current L4-not-L5 boundary:

1. Reconcile any remaining stale public-draft or qualified-L2 wording in controlled records against the current v1 L4 claim.
2. Add an explicit policy for any future `artifacts/` or `packages/` directory so substantive artifact packages are distinguished from examples and core framework materials.
3. Add a bounded DSR theory operationalization artifact package only after the directory policy is retained.
4. Add a self-application validation record comparing `documentation-protocol` and `dsr-framework` against the DSR theory operational model.
5. Keep L5 archival/publication-ready work separate until preservation closure, registry evidence, independent external review, and L5 release approval are retained.

## Citation and reuse

Use the repository citation metadata in `CITATION.cff`, the repository license notice in `LICENSE`, and the archived-release metadata in `.zenodo.json`. The current v1.0.1 release is the reusable-stable package release. It is not an L5 archival/publication-ready release and it does not certify downstream artifacts merely because they use the framework.

## Maintainer note

This file is a human-facing repository entry point. Controlled source-of-truth content should live in structured files such as `manifest.yaml`, `metadata.yaml`, `artifact-profile.yaml`, `package-inventory.yaml`, `conformance-declaration.yaml`, and product specifications under `specs/`.
