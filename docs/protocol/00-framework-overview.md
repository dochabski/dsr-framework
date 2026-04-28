<!--
SPDX-License-Identifier: CC0-1.0
item_id: docs_protocol_00_framework_overview
item_type: description
selection_id: docs_overview
status: draft
version: 0.1.0
conformance_target: l2_reviewable
target_path: docs/protocol/00-framework-overview.md
-->

# DSR Framework Overview

## Controlled source links

- [manifest.yaml](../../manifest.yaml)
- [metadata.yaml](../../metadata.yaml)
- [artifact-profile.yaml](../../artifact-profile.yaml)
- [package-inventory.yaml](../../package-inventory.yaml)
- [conformance-declaration.yaml](../../conformance-declaration.yaml)
- [specs/product-catalog.yaml](../../specs/product-catalog.yaml)

## Document status

| Field | Value |
|---|---|
| Selection ID | `docs_overview` |
| Repository path | `docs/protocol/00-framework-overview.md` |
| Item type | `description` |
| Output format | Markdown |
| Status | Draft |
| Version | `0.1.0` |
| Conformance target | `L2 reviewable` |
| Primary audience | DSR researchers, reviewers, editors, maintainers, doctoral supervisors, methods instructors, and artifact-package users |
| Source-of-truth role | Human-facing overview; controlled requirements remain in YAML, JSON Schema, records, and checklists |

## Purpose

The **Design Science Research (DSR) Framework** is a protocol-governed artifact package for planning, documenting, evaluating, reviewing, publishing, and preserving Design Science Research artifacts. It is intended to help users make DSR work more explicit, reviewable, reusable, citable, and publication-prepared without treating the framework itself as a substitute for expert methodological judgment or peer review.

This overview explains the framework at a human-facing level. It orients users to the package structure, the major DSR distinctions preserved by the framework, the expected workflow, the conformance model, and the relationship between narrative documentation and controlled source files.

## Controlled files that this page explains

This page is a guide, not the controlled source of truth. The following repository files provide the authoritative structured content that this page renders or summarizes.

| Controlled or related file | Role in the framework |
|---|---|
| `README.md` | Public repository entry point and high-level orientation. |
| `manifest.yaml` | Canonical package identity and repository manifest. |
| `metadata.yaml` | Structured project, authorship, license, citation, and provenance metadata. |
| `artifact-profile.yaml` | Artifact identity, type, scope, claims, conformance, and reuse constraints. |
| `package-inventory.yaml` | Inventory of expected package files, validation responsibilities, and review status. |
| `conformance-declaration.yaml` | Declared conformance level, tailoring decisions, and package obligations. |
| `specs/product-catalog.yaml` | Product registry and dependency map for the framework. |
| `specs/product-protocol-foundation.yaml` | Protocol-level scope, conformance, and tailoring foundation. |
| `specs/product-dsr-framework-foundation.yaml` | Framework identity, scope, users, assumptions, boundaries, and non-goals. |
| `specs/product-dsr-lifecycle-and-contribution-model.yaml` | Lifecycle, artifact taxonomy, contribution model, transparency, and evaluation alignment. |
| `specs/product-dsr-information-item-architecture.yaml` | DSR-specific information items and records. |
| `specs/product-dsr-repository-architecture.yaml` | Repository tree, naming rules, and file responsibilities. |
| `specs/product-dsr-artifact-package-specification.yaml` | Required package contents, evidence, examples, records, and conformance obligations. |
| `specs/product-dsr-quality-conformance-and-review-model.yaml` | Quality dimensions, maturity, gates, review workflow, and acceptance criteria. |
| `specs/product-dsr-templates-and-checklists.yaml` | Operating specification for reusable templates and checklists. |
| `models/` | Conceptual and operational DSR models. |
| `vocabularies/` | Controlled terms used across schemas, templates, checklists, records, and docs. |
| `schemas/` | JSON Schema files for structured validation. |
| `templates/` | Reusable DSR information-item templates. |
| `checklists/` | Review and readiness checklists. |
| `records/` | Retained evidence of source basis, decisions, transparency, evaluation, review, release, and preservation. |

## What the framework is

The DSR Framework is a **compound DSR artifact package**. It combines several artifact forms:

| Artifact form | Framework expression |
|---|---|
| Method or protocol artifact | Rules for documenting, reviewing, validating, and publishing DSR artifact packages. |
| Model or taxonomy artifact | Lifecycle, artifact ontology, contribution, evaluation, transparency, reliability, and projectability models. |
| Data or information artifact | Controlled YAML records, inventories, metadata, vocabularies, and source-basis mappings. |
| Documentation artifact | Human-facing Markdown guidance under `docs/protocol/`. |
| Quality artifact | Checklists, acceptance criteria, quality gates, review records, and conformance declarations. |

The framework is designed for repository-native use. It favors structured files where validation, traceability, and reuse matter, while using Markdown for explanation, orientation, and guidance.

## What problem it addresses

DSR projects often combine artifact creation, problem relevance, solution grounding, iterative building, demonstration, evaluation, contribution claims, and publication materials. These elements are frequently documented in fragmented ways. As a result, reviewers and later users may struggle to determine:

- what the artifact is;
- what problem class it addresses;
- what contribution is being claimed;
- what evidence supports utility, quality, validity, reliability, or projectability;
- what was demonstrated versus what was evaluated;
- what can be reused or adapted;
- what limitations, boundary conditions, and non-goals constrain the claims.

The DSR Framework addresses this by giving users a reusable package architecture, controlled information items, models, vocabularies, schemas, templates, checklists, records, and human-facing documentation.

## Intended users

| User role | Primary need |
|---|---|
| Researcher or author | Plan, document, evaluate, and publish a DSR artifact package. |
| Reviewer or editor | Inspect DSR identity, artifact claims, evidence, limitations, and conformance. |
| Practitioner or adopter | Understand artifact use conditions, reuse constraints, and adaptation limits. |
| Maintainer or curator | Version, validate, review, release, and preserve the framework package. |
| Instructor, supervisor, or methods coach | Teach DSR documentation, contribution positioning, and evaluation alignment. |
| Repository or research-support team | Integrate package records, schemas, quality gates, and publication metadata into a controlled repository workflow. |

## Scope

### In scope

The framework covers:

- DSR artifact package structure;
- DSR identity and minimum viability checks;
- artifact ontology and boundary documentation;
- problem-space and solution-space documentation;
- artifact build-process transparency;
- demonstration and evaluation records;
- contribution positioning and knowledge-claim documentation;
- validity, reliability, replication, and projectability guidance;
- responsible design and transparency considerations;
- quality gates, review workflows, conformance levels, and readiness checklists;
- repository, release, citation, and preservation scaffolding.

### Out of scope

The framework does **not**:

- replace peer review, ethics review, legal review, security review, or domain expert judgment;
- guarantee that a DSR artifact is effective, valid, generalizable, reusable, or publishable;
- prescribe domain-specific metrics for every possible artifact type or research setting;
- require unsafe disclosure of proprietary, private, security-sensitive, or ethically restricted material;
- treat all DSR artifacts as software;
- treat every demonstration as evaluation evidence;
- claim archival publication readiness unless release, review, preservation, and citation records support that claim.

## Core DSR distinctions preserved by the framework

| Distinction | Operational meaning |
|---|---|
| Artifact utility vs. artifact quality vs. contribution to knowledge | A locally useful artifact, a well-built artifact, and a publishable design-knowledge contribution are related but not identical claims. |
| Demonstration vs. evaluation | Demonstration shows that an artifact can be used in a scenario; evaluation assesses the artifact against explicit criteria and evidence. |
| Artifact instance vs. artifact type | A concrete implementation may instantiate a more general construct, model, method, framework, protocol, design principle, or design theory. |
| Problem space vs. solution space | Problem-space work establishes relevance and boundaries; solution-space work establishes grounding in existing knowledge and alternatives. |
| Build transparency vs. evaluation transparency | Build transparency documents design activity, reasoning, decisions, and construction; evaluation transparency documents criteria, methods, data, findings, and limitations. |
| Idiographic vs. nomothetic or projectable scope | Some claims are local and contextual; others are intended to transfer, generalize, or project across a problem class. |
| Replication vs. projectability | Exact replication may be inappropriate for situated DSR, but transparent context and boundary conditions can support adaptation and cumulative knowledge. |
| Consulting or implementation vs. DSR | DSR requires a contribution to design knowledge, not only delivery of a local solution. |

## Repository architecture

The framework expects a repository layout that separates controlled source files, human-facing guidance, reusable templates, review checklists, retained records, examples, and crosswalks.

| Directory or file | Purpose |
|---|---|
| Root package files | Identify the package, license, citation metadata, governance, inventory, conformance, and public orientation. |
| `specs/` | Controlled product specifications and dependency logic. |
| `models/` | Conceptual and operational models used by templates, schemas, records, and checklists. |
| `vocabularies/` | Controlled terms for consistent classification and validation. |
| `schemas/` | JSON Schema validation resources. |
| `templates/` | Reusable records and working templates for researchers. |
| `checklists/` | Review, quality, transparency, evaluation, reliability, projectability, package, and publication readiness checks. |
| `docs/protocol/` | Human-facing documentation pages that explain the structured files. |
| `records/` | Retained evidence of source basis, decisions, tailoring, review, evaluation, release, and preservation. |
| `crosswalks/` | Mappings among source traditions, protocol elements, and DSR constructs. |
| `examples/` | Demonstration packages or worked examples, not required package-control files. |

## Product architecture

The framework is built as a dependency-linked set of products.

| Product family | Examples |
|---|---|
| Root and package control | `README.md`, `manifest.yaml`, `metadata.yaml`, `artifact-profile.yaml`, `package-inventory.yaml`, `conformance-declaration.yaml` |
| Product specifications | Protocol foundation, DSR foundation, lifecycle and contribution, information-item architecture, repository architecture, metadata profile, artifact package, quality review, publication, templates/checklists, automation/validation |
| Models | Canonical model, lifecycle model, artifact ontology, contribution model, evaluation alignment, transparency, reliability, projectability, publication readiness, decision flow |
| Vocabularies | Artifact types, contribution types, knowledge goals, knowledge scopes, lifecycle stages, evaluation methods, validity, reliability, replication, projectability, transparency, genre, responsible design, aesthetics |
| Schemas | Artifact profile, package inventory, conformance declaration, project, artifact, evaluation plan/report, contribution claim, transparency crosswalk |
| Templates | Project charter, problem and objectives, solution space, design rationale, artifact specification, build transparency, demonstration record, evaluation plan/report, contribution claim, review record |
| Checklists | Minimum DSR identity, package readiness, transparency, evaluation readiness, contribution positioning, reliability, projectability, publication readiness |
| Records | Source basis, contribution positioning, transparency crosswalk, evaluation plan, self-review, release |

## How to use the framework

### 1. Establish DSR identity

Begin by confirming that the work is being framed as DSR rather than only local implementation, consulting, software delivery, or explanatory research. Use the minimum DSR checklist and artifact-profile materials to verify that the work has:

- a problem context;
- an artifact or artifact class;
- a build or design process;
- demonstration or use context;
- evaluation logic appropriate to the claims;
- a contribution claim;
- limitations and boundary conditions.

### 2. Define the artifact package

Use the root package files and artifact package specification to define:

- package identity;
- artifact identity and type;
- repository structure;
- file responsibilities;
- license and citation metadata;
- package inventory;
- conformance level;
- tailoring decisions.

### 3. Describe the DSR project and artifact

Use the project, problem, solution-space, design-rationale, and artifact-specification templates to describe:

- problem context, stakeholders, goals, and constraints;
- solution-space grounding and alternatives;
- artifact components, make logic, use logic, and boundaries;
- design decisions, rejected alternatives, and tradeoffs;
- assumptions, limitations, and non-goals.

### 4. Plan demonstration and evaluation separately

Use demonstration and evaluation templates to avoid overclaiming. Demonstration records should show how the artifact is used or instantiated. Evaluation plans and reports should state explicit criteria, methods, evidence, findings, limitations, and claim implications.

### 5. Position the contribution

Use contribution vocabularies and records to identify whether the contribution is primarily an artifact, method, model, framework, taxonomy, design principle, design theory, evaluation contribution, exaptation, improvement, or package contribution. Also state the intended knowledge goal and scope.

### 6. Record transparency evidence

Use transparency models, crosswalks, and records to document the six DSR transparency dimensions:

| Dimension | Evidence focus |
|---|---|
| Process transparency | Activities, sequencing, decisions, emergence, iteration, and rationale. |
| Problem-space transparency | Context, stakeholders, problem class, goals, constraints, and boundary conditions. |
| Solution-space transparency | Prior knowledge, alternatives, candidate solutions, design theories, technologies, and justification. |
| Build transparency | Design search, construction, artifact components, make logic, collaboration, and design decisions. |
| Evaluation transparency | Criteria, methods, data, participants or units, results, validity threats, and limitations. |
| Contribution transparency | Claimed design knowledge, practice impact, scientific impact, scope, and reuse implications. |

### 7. Review quality and conformance

Apply quality gates and readiness checklists before claiming higher conformance. Review should test consistency, coherence, cogency, correspondence, transparency, and reviewability.

### 8. Prepare for release and preservation

Before publication or archival release, verify metadata, citation, license, package inventory, conformance declaration, release records, preservation records, validation outputs, and known limitations.

## Conformance model

The framework uses staged conformance so draft materials can be useful without overclaiming maturity.

| Level | Label | Meaning |
|---|---|---|
| `L0` | Draft | Content exists but is incomplete or not yet internally checked. |
| `L1` | Documented | Purpose, scope, file role, and basic dependencies are documented. |
| `L2` | Reviewable | Content includes explicit review logic, traceability, acceptance criteria, or quality-gate alignment. |
| `L3` | Exercisable | Users can exercise schemas, templates, examples, validation procedures, or review workflows. |
| `L4` | Reusable | Content is sufficiently coherent and documented for responsible adaptation by others. |
| `L5` | Archival or publication-ready | Release, citation, preservation, final review, and publication-readiness evidence support archival use. |

This overview is generated at **L2 reviewable**. It provides reviewable orientation, traceable file references, explicit scope, assumptions, non-goals, quality gates, and use logic. It does not itself validate the package or certify publication readiness.

## Quality gates for this overview

| Gate | Pass condition |
|---|---|
| Consistency | The file is Markdown, uses the expected path, and follows the documentation-page role. |
| Coherence | The page aligns with root files, specs, models, templates, checklists, and records without replacing them. |
| Cogency | The page explains how a user should navigate and apply the framework. |
| Correspondence | The page supports the DSR Framework as a reviewable and reusable artifact package. |
| DSR transparency | The page identifies how the framework supports process, problem-space, solution-space, build, evaluation, and contribution transparency. |
| Reviewability | The page states scope, assumptions, limitations, non-goals, file dependencies, and quality-gate expectations. |

## Evidence and traceability posture

The framework is grounded in two evidence families:

1. **Documentation protocol and repository architecture evidence**, which governs structured information items, repository layout, controlled records, and validation-oriented package design.
2. **DSR corpus evidence**, which grounds artifact ontology, lifecycle logic, contribution positioning, transparency, evaluation, reliability, validity, replication, projectability, and publication-readiness concepts.

Where detailed evidence has not yet been mapped to a specific claim, controlled files should use `evidence_status: not_yet_mapped` or `evidence_status: partially_mapped` rather than inventing authority.

## Limitations

- This overview summarizes the framework but does not replace controlled YAML, JSON Schema, templates, checklists, or retained records.
- Repository files may mature at different conformance levels; users should check `package-inventory.yaml` and `conformance-declaration.yaml` for current status.
- The framework can support evaluation planning and review, but it cannot itself prove artifact effectiveness or scholarly contribution.
- Some project-specific evidence, such as data, code, restricted materials, ethics records, or proprietary implementation details, may require tailoring, redaction, summaries, or access-controlled storage.
- Publication readiness must be supported by release, review, citation, preservation, and validation records; it should not be inferred from this overview alone.

## Open questions and backlog

| ID | Question | Disposition |
|---|---|---|
| `oq_overview_001` | Which protocol documentation pages should be considered mandatory for the first public release? | Defer to publication and release readiness model. |
| `oq_overview_002` | Which examples should be included to demonstrate framework instantiation without being mistaken for evaluation evidence? | Defer to examples and evaluation records. |
| `oq_overview_003` | Which validation checks should be automated before moving from L2 to L3? | Defer to automation and validation specification. |
| `oq_overview_004` | How much DSR source-to-construct mapping is sufficient for L4 reuse? | Defer to source-basis records and quality review. |

## Recommended reading order

For a first-time user, read the framework in this order:

1. `README.md`
2. `docs/protocol/00-framework-overview.md`
3. `artifact-profile.yaml`
4. `conformance-declaration.yaml`
5. `package-inventory.yaml`
6. `specs/product-dsr-framework-foundation.yaml`
7. `specs/product-dsr-lifecycle-and-contribution-model.yaml`
8. `models/dsr-framework-canonical-model.yaml`
9. `models/dsr-lifecycle-model.yaml`
10. `models/dsr-artifact-ontology.yaml`
11. `models/dsr-evaluation-alignment-model.yaml`
12. `models/dsr-transparency-model.yaml`
13. Relevant templates and checklists for the user's project stage

## Change history

| Version | Date | Change type | Summary |
|---|---|---|---|
| `0.1.0` | 2026-04-27 | Initial creation | Created human-facing framework overview aligned to the generation specification, root README, framework foundation specification, and current package architecture. |
