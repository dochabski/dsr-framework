<!-- SPDX-License-Identifier: CC0-1.0 -->

# Publication and Review Guidance

## Controlled source links

- [models/dsr-publication-readiness-model.yaml](../../models/dsr-publication-readiness-model.yaml)
- [specs/product-dsr-publication-and-registry-model.yaml](../../specs/product-dsr-publication-and-registry-model.yaml)
- [checklists/publication-readiness-checklist.yaml](../../checklists/publication-readiness-checklist.yaml)
- [templates/review-record-template.yaml](../../templates/review-record-template.yaml)
- [records/releases/record-release-0001-v0-1-0.yaml](../../records/releases/record-release-0001-v0-1-0.yaml)

| Field | Value |
|---|---|
| item_id | `docs_publication_review` |
| item_type | `description` |
| title | Publication and Review Guidance |
| target_path | `docs/protocol/14-publication-and-review-guidance.md` |
| status | `draft` |
| version | `0.1.0` |
| owner | DSR Framework maintainers |
| conformance_target | `l4_reusable` |
| primary_controlled_model | `models/dsr-publication-readiness-model.yaml` |
| related_specs | `specs/product-dsr-publication-and-registry-model.yaml`; `specs/product-dsr-quality-conformance-and-review-model.yaml`; `specs/product-dsr-artifact-package-specification.yaml`; `specs/product-dsr-metadata-and-identifier-profile.yaml` |
| related_checklists | `checklists/publication-readiness-checklist.yaml`; `checklists/artifact-package-readiness-checklist.yaml`; `checklists/contribution-positioning-checklist.yaml`; `checklists/evaluation-readiness-checklist.yaml`; `checklists/dsr-transparency-crosswalk-checklist.yaml` |
| related_records | `records/releases/`; `records/reviews/`; `records/preservation/`; `records/contributions/`; `records/source-basis/` |
| source_basis | DSR Framework Generation Specification; DSR extraction corpus; Documentation Protocol repository model |
| evidence_status | `partially_mapped` |

## 1. Purpose

This guide explains how to prepare, review, release, and cite a Design Science Research (DSR) Framework artifact package when the goal is public reuse, scholarly review, or archival publication. It translates the publication-readiness model into human-facing guidance for authors, maintainers, reviewers, editors, and external users.

The guide is intended to help a project team decide whether a DSR artifact package is ready to be:

1. shared for internal review;
2. reused by another researcher or practitioner;
3. released as a citable repository artifact;
4. registered or archived through a DOI-bearing service; or
5. submitted as supporting material for a scholarly manuscript.

Publication readiness does not mean that the artifact, theory, evaluation, or claims are final. It means the package is documented well enough that a competent reviewer can identify what the artifact is, what it claims, what evidence supports those claims, what is not yet known, and how the package may be reused or extended.

## 2. Scope

This page applies to DSR artifact packages that include one or more of the following outputs:

- conceptual artifacts, such as frameworks, vocabularies, models, ontologies, or taxonomies;
- procedural artifacts, such as methods, protocols, workflows, templates, checklists, and review procedures;
- technical artifacts, such as software, schemas, validation tools, databases, or automation scripts;
- evidence packages, such as evaluation plans, evaluation reports, source-basis records, review records, release records, and preservation records;
- human-facing documentation, such as protocol guides, README files, examples, and contributor instructions.

This page does not replace journal-specific author instructions, institutional repository rules, funder requirements, export-control review, human-subjects review, intellectual-property review, or legal review. It provides a DSR-specific readiness layer that should be used before or alongside those external requirements.

## 3. Publication-readiness principle

A DSR artifact package is publication-ready when it is sufficiently identified, bounded, evidenced, reviewed, and preserved for its intended reuse context.

Publication readiness therefore depends on five linked judgments:

| Readiness question | Required judgment | Primary evidence |
|---|---|---|
| What is being published? | Artifact identity and boundary are clear. | `artifact-profile.yaml`; `manifest.yaml`; `package-inventory.yaml` |
| Why does it matter? | Practical problem, design objective, and contribution claim are explicit. | problem/objectives template; contribution claim; contribution positioning record |
| What supports the claim? | Demonstration, evaluation, review, and traceability records are sufficient for the asserted claim level. | evaluation plan/report; review record; source-basis record; transparency crosswalk |
| Can others inspect or reuse it? | Repository structure, metadata, license, versioning, and usage guidance are complete enough for reuse. | README; metadata; license; CITATION; templates; examples |
| What remains limited or unsettled? | Limitations, non-goals, risks, and open questions are not hidden. | limitations sections; open questions; release notes; review findings |

The readiness judgment must be proportional. A conceptual framework does not need the same executable reproducibility evidence as a software tool, but it still needs clear definitions, traceable sources, contribution positioning, review criteria, and limitations.

## 4. DSR-specific publication concerns

DSR publication review differs from generic documentation review because DSR artifacts combine problem relevance, design construction, evaluation, and knowledge contribution. The reviewer should not ask only whether the repository is tidy. The reviewer should also ask whether the package makes the design claim reviewable.

### 4.1 Contribution clarity

A DSR package should distinguish at least four claim layers:

| Claim layer | Review question | Evidence expected |
|---|---|---|
| Artifact identity | What kind of artifact is this? | artifact profile; artifact ontology alignment; package inventory |
| Artifact utility | What problem, task, or use context does it support? | problem/objectives record; demonstration record; use scenarios |
| Artifact quality | How well does it satisfy relevant criteria? | evaluation plan/report; validation checks; review record |
| Knowledge contribution | What reusable design knowledge does it add? | contribution claim; contribution positioning; source-basis record |

A package should not imply that local usefulness automatically establishes a scholarly contribution. Conversely, a package should not present abstract contribution language without enough artifact, context, and evaluation detail to let a reviewer inspect the basis of the claim.

### 4.2 Demonstration is not evaluation

A demonstration shows that an artifact can be used in a context, example, scenario, or walkthrough. An evaluation tests claims against explicit criteria.

For publication review, the package should keep these records separate:

| Record type | Function | Publication role |
|---|---|---|
| Demonstration record | Shows artifact use in a scenario or context. | Supports understandability and use plausibility. |
| Evaluation plan | States what will be evaluated, by what method, and against which criteria. | Supports pre-claim review and evaluation alignment. |
| Evaluation report | Reports results, limitations, and claim implications. | Supports artifact-quality and contribution claims. |
| Review record | Captures independent or self-review findings. | Supports conformance and release decisions. |

When an artifact has only been demonstrated, the release notes should state that the artifact has demonstration evidence but not yet full evaluation evidence.

### 4.3 Genre-appropriate review

DSR artifacts may belong to different genres: design theory, artifact construction, method development, action design research, explanatory design theory, ontology, vocabulary, checklist, or protocol. A reviewer should evaluate the artifact against its declared genre rather than indiscriminately applying every possible DSR criterion.

A genre-appropriate review should check:

1. whether the artifact type is declared correctly;
2. whether the claimed contribution type fits the artifact type;
3. whether the evaluation method fits the claim;
4. whether the package distinguishes local evidence from projectable knowledge;
5. whether the communication format fits both scholarly and practitioner audiences.

### 4.4 Transparency without unnecessary burden

Publication readiness requires transparency, but transparency should be proportionate. A DSR package should document the process, problem space, solution space, build work, evaluation, and contribution, while also respecting privacy, security, intellectual property, and author workload.

For each transparency dimension, the reviewer should ask for enough evidence to assess the claim, not every possible internal artifact.

| Transparency dimension | Minimum publication evidence | Examples of stronger evidence |
|---|---|---|
| Process transparency | Lifecycle stage, major decisions, change history. | Design decision records; activity logs; release notes. |
| Problem-space transparency | Problem class, stakeholders, goals, constraints, boundaries. | Requirements trace; context analysis; stakeholder review. |
| Solution-space transparency | Prior knowledge, alternative approaches, source basis. | Search strategy; source-basis record; crosswalks. |
| Build transparency | Artifact components, design rationale, construction choices. | Design rationale records; architecture diagrams; code comments. |
| Evaluation transparency | Evaluation criteria, methods, findings, limitations. | Full evaluation report; validation outputs; reviewer response. |
| Contribution transparency | Contribution type, knowledge scope, claim boundary. | Contribution positioning record; publication narrative; registry entry. |

## 5. Readiness levels

The framework uses conformance levels to avoid overclaiming. For publication and review, the most relevant levels are L2 through L5.

| Level | Label | Meaning for publication and review | Typical release decision |
|---|---|---|---|
| L2 | Reviewable | The package can be reviewed against explicit criteria. | Internal review or draft release. |
| L3 | Exercisable | The package can be used, run, validated, or walked through. | Pilot reuse or technical review. |
| L4 | Reusable | The package has enough metadata, guidance, review evidence, and boundaries for external reuse. | Public repository release. |
| L5 | Archival publication-ready | The package is ready for formal citation, DOI registration, preservation, and publication linkage. | DOI/archive release and manuscript support. |

This file targets L4. It supports reusable public release, but it does not by itself certify L5 archival publication readiness. L5 requires stronger preservation, citation, release, and registry evidence.

## 6. Publication-readiness workflow

Use the following workflow before releasing or submitting a DSR package.

### Step 1: Confirm package identity

Verify that the root package files identify the artifact package clearly.

Minimum checks:

- `README.md` describes the package purpose and use context.
- `manifest.yaml` identifies package contents and canonical identity.
- `metadata.yaml` provides authorship, version, status, keywords, and citation-relevant metadata.
- `artifact-profile.yaml` identifies artifact type, boundary, intended users, claims, constraints, and conformance level.
- `package-inventory.yaml` lists files, responsibilities, and validation expectations.
- `conformance-declaration.yaml` states conformance level and any tailoring.

### Step 2: Confirm claim structure

Every release should have a bounded contribution claim. The claim should not exceed the evidence.

A publication-ready claim should identify:

- artifact type;
- problem class;
- intended use context;
- contribution type;
- knowledge goal;
- knowledge scope;
- evaluation status;
- projectability boundary;
- limitations and non-goals.

If any of these fields are missing, release may still be possible, but the release must be marked as draft, exploratory, or not yet fully evaluated.

### Step 3: Confirm evidence package

The evidence package should include enough retained records for a reviewer to reconstruct the basis of the release decision.

| Evidence area | Minimum record or file | Review purpose |
|---|---|---|
| Source basis | `records/source-basis/` | Shows intellectual and methodological grounding. |
| Contribution | `records/contributions/` | Shows how the artifact is positioned. |
| Transparency | `records/dsr-transparency/` | Shows what was disclosed and what was limited. |
| Evaluation | `records/evaluations/` | Shows criteria, methods, results, and limitations. |
| Review | `records/reviews/` | Shows self-review or independent review outcomes. |
| Release | `records/releases/` | Shows version, date, status, and release decision. |
| Preservation | `records/preservation/` | Shows archival and long-term access decisions where applicable. |

### Step 4: Run quality-gate review

The release reviewer should assess the package against six gates.

| Gate | Pass condition |
|---|---|
| Consistency | File names, directories, statuses, identifiers, and item types follow repository conventions. |
| Coherence | Related files do not contradict each other. |
| Cogency | Users can understand and apply the package without hidden assumptions. |
| Correspondence | The package content supports the declared DSR artifact package purpose. |
| DSR transparency | Relevant process, problem, solution, build, evaluation, and contribution evidence is present or explicitly limited. |
| Reviewability | A reviewer can judge acceptance criteria, evidence, validation, and unresolved issues. |

A package should not proceed to L4 release with unresolved critical failures in consistency, coherence, correspondence, or reviewability.

### Step 5: Prepare repository release materials

Before public release, prepare the files that make the artifact findable, citable, reusable, and governable.

Minimum expected release materials:

- `LICENSE`
- `CITATION.cff`
- `.zenodo.json` or equivalent archival metadata file
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `GOVERNANCE.md`
- `SECURITY.md` where the package includes technical artifacts or security-relevant materials
- `CODE_OF_CONDUCT.md` where community contribution is expected
- release record in `records/releases/`
- updated `package-inventory.yaml`
- updated `conformance-declaration.yaml`

### Step 6: Make release decision

Use one of the following release decisions.

| Decision | Use when | Required action |
|---|---|---|
| `approve_release` | All critical criteria pass and only non-blocking issues remain. | Create release record and tag/version update. |
| `approve_with_limitations` | Package is useful but has declared evaluation, reuse, or evidence limits. | State limitations in release notes and records. |
| `revise_before_release` | Important evidence, metadata, or coherence issues remain. | Create remediation tasks before release. |
| `do_not_release` | Claims are unsupported, sensitive content is exposed, or core package identity is unclear. | Retain review record and block release. |

## 7. Author guidance

Authors preparing a DSR artifact package for publication should use the following operating rules.

### 7.1 State the artifact before the article

A publication package should make the artifact inspectable before it argues for the artifact's scholarly importance. Start with artifact identity, then move to problem relevance, design rationale, evaluation, contribution, and reuse.

Minimum author statement:

> This package provides [artifact type] for [problem class/use context]. It supports [use or decision task]. It claims [contribution type] at [knowledge scope]. It has been [demonstrated/evaluated/reviewed] using [evidence type]. Its known limits are [limitations].

### 7.2 Match claim level to evidence level

Use cautious claim verbs unless evaluation is complete.

| Evidence status | Acceptable claim language | Avoid |
|---|---|---|
| Conceptual grounding only | proposes, structures, clarifies, organizes | proves, validates, demonstrates effectiveness |
| Demonstration evidence | demonstrates use, illustrates feasibility, shows applicability in example | establishes effectiveness, generalizes |
| Formative evaluation | improves, refines, detects issues, supports usability or feasibility | confirms final utility |
| Summative evaluation | supports claim that, provides evidence for, meets stated criteria | guarantees, universally applies |
| Independent reuse evidence | has been reused/adapted in specified contexts | is generally valid without boundary conditions |

### 7.3 Preserve review traceability

Do not delete review findings merely because they are inconvenient. Publication-ready packages should preserve adverse findings, limitations, and remediations. A strong package is not one with no weaknesses; it is one whose weaknesses are visible, bounded, and addressed proportionately.

### 7.4 Communicate to more than one audience

A DSR package should usually support at least two audiences:

- scholarly reviewers who need traceability, contribution positioning, and evidence;
- practical users who need purpose, installation or use instructions, examples, constraints, and limitations.

Where possible, include both technical and plain-language descriptions.

## 8. Reviewer guidance

Reviewers should evaluate publication readiness using both package-level criteria and DSR-specific criteria.

### 8.1 Package-level review questions

1. Is the package identity clear?
2. Is the repository structure consistent with the declared protocol?
3. Are required files present and named correctly?
4. Are versions, statuses, and licenses clear?
5. Are citation and archival metadata present where needed?
6. Can a user find the source-of-truth files?
7. Can a reviewer reconstruct what changed between versions?

### 8.2 DSR-specific review questions

1. Is the artifact type declared and defensible?
2. Is the problem class explicit?
3. Is the solution-space grounding visible?
4. Is the design rationale documented?
5. Is the distinction between demonstration and evaluation preserved?
6. Are evaluation criteria aligned with the artifact claims?
7. Is the contribution type clear?
8. Is the knowledge scope bounded?
9. Are limitations and non-goals explicit?
10. Is the package reusable without implying unsupported generalization?

### 8.3 Reviewer decision matrix

| Finding | Severity | Recommended reviewer action |
|---|---|---|
| Missing package identity | Critical | Block release until root metadata and artifact profile are corrected. |
| Unsupported contribution claim | Critical | Require claim narrowing or additional evidence. |
| Demonstration presented as evaluation | Major | Require separation of demonstration and evaluation records. |
| Missing limitations | Major | Require limitations and boundary conditions. |
| Incomplete citation metadata | Major for L5, minor for L4 | Require `CITATION.cff`, metadata, or archival record depending on target level. |
| Missing examples | Minor to major | Require at least one example if reuse depends on usage interpretation. |
| Inconsistent terminology | Major | Align vocabularies, models, and docs. |
| Sensitive or proprietary material exposed | Critical | Block release pending security, privacy, or IP review. |
| No preservation plan | Major for L5 | Add preservation record before archival release. |

## 9. Publication package contents

For an L4 reusable release, the package should contain the following categories of content.

| Category | Required for L4? | Function |
|---|---:|---|
| Root description and metadata | Yes | Makes the package understandable and citable. |
| Artifact profile | Yes | Identifies artifact type, purpose, scope, and claims. |
| Package inventory | Yes | Identifies what is included and what each file does. |
| Conformance declaration | Yes | States declared conformance level and tailoring. |
| Controlled models/specs/vocabularies | As applicable | Provide source-of-truth definitions. |
| Templates/checklists | As applicable | Support reuse and review. |
| Human-facing docs | Yes | Explain how to use the controlled files. |
| Evidence records | Yes | Preserve source basis, review, evaluation, release, and transparency evidence. |
| Examples | Strongly recommended | Show how the artifact can be used. |
| Schemas/validation | Required when structured files are intended to be validated | Support consistency and automation. |
| Archival metadata | Required for L5, recommended for L4 | Supports citation and preservation. |

## 10. Release notes guidance

Each release should include a release record and public release notes.

Release notes should include:

- release identifier;
- release date;
- release status;
- conformance level;
- summary of major changes;
- files added, changed, deprecated, or removed;
- evaluation status;
- review status;
- known limitations;
- reuse guidance;
- citation guidance;
- next planned work.

Use direct, bounded language. Do not use release notes to hide unresolved quality issues.

## 11. Citation and registry guidance

A DSR package should be made citable when the intended audience includes external researchers, reviewers, or practitioners who may depend on stable references.

Minimum citation-readiness checks:

- package has a stable title;
- creators and contributors are identified;
- version is declared;
- release date is declared;
- license is declared;
- repository URL is stable;
- preferred citation is present;
- DOI or archival identifier is present for L5, or planned for a future release;
- related manuscript, documentation, and source-basis records are cross-linked.

For L5, the release record should identify the archival service, DOI or persistent identifier, preservation scope, and any files excluded from archival deposit.

## 12. Responsible publication review

Before releasing a package, review potential harms and constraints.

| Risk | Review question | Possible mitigation |
|---|---|---|
| Privacy risk | Does the package expose personal, participant, student, employee, or stakeholder data? | Remove, aggregate, anonymize, or restrict. |
| Security risk | Does the package disclose vulnerabilities, credentials, attack paths, or unsafe procedures? | Redact, restrict, or coordinate disclosure. |
| Proprietary risk | Does the package disclose restricted IP, vendor materials, client data, or confidential implementation details? | Replace with abstracted examples or obtain permission. |
| Misuse risk | Could the artifact be applied outside its valid boundary in a harmful way? | Add boundary conditions and misuse warnings. |
| Overclaiming risk | Does the package imply stronger evidence than it has? | Narrow claims and mark evaluation status. |
| Maintenance risk | Does release imply support that maintainers cannot provide? | State maintenance level and support policy. |

A release should be blocked if it exposes sensitive material or creates a foreseeable misuse risk that cannot be mitigated through documentation, redaction, or access control.

## 13. Acceptance criteria

This page satisfies its L4 purpose when it meets the following criteria.

| Criterion | Pass condition |
|---|---|
| Identity | The page identifies its item ID, path, status, version, source basis, and controlled model dependency. |
| Scope | The page distinguishes publication review, artifact-package review, scholarly review, release review, and archival readiness. |
| Operational guidance | The page provides a usable workflow for author preparation, reviewer assessment, release decision, and citation readiness. |
| DSR alignment | The page distinguishes artifact utility, artifact quality, knowledge contribution, demonstration, evaluation, projectability, and transparency. |
| L4 restraint | The page supports reusable release without claiming that all L5 archival requirements are satisfied. |
| Reviewability | The page includes review questions, decision states, evidence expectations, failure modes, and remediation logic. |
| Traceability | The page names related specs, models, checklists, records, and corpus evidence anchors. |

## 14. Traceability

| trace_id | Supports | Source or dependency | Evidence status |
|---|---|---|---|
| `trace_publication_review_selection` | Selected target path and conformance | `dsr-framework-selection-table.md` / `docs_publication_review` | mapped |
| `trace_generation_rules` | Markdown docs page rules and quality gates | `dsr-framework-generation-spec.yaml`; `dsr-framework-generation-prompt.md` | mapped |
| `trace_publication_model` | Publication and release readiness | `models/dsr-publication-readiness-model.yaml` | not_yet_mapped |
| `trace_quality_review` | Review gates and acceptance criteria | `specs/product-dsr-quality-conformance-and-review-model.yaml`; `checklists/publication-readiness-checklist.yaml` | partially_mapped |
| `trace_transparency_publication` | Process, problem, solution, build, evaluation, and contribution transparency | Hevner et al. 2024, anchors CA01, CA14, CA15, CA16, CA17, CA18 | mapped_from_corpus |
| `trace_contribution_publication` | Contribution-positioning and communication | Akoka et al. 2023, anchors A10, A13, A14, A15, A16 | mapped_from_corpus |
| `trace_genre_review` | Genre-sensitive review expectations | DSR genre source, anchors CA-003 and CA-010 | mapped_from_corpus |
| `trace_grid_communication` | Communication with editors and reviewers | DSR Grid source, anchors A09 and A10 | mapped_from_corpus |

## 15. Limitations

- This page is a human-facing guide, not the source-of-truth publication-readiness model.
- The controlled model `models/dsr-publication-readiness-model.yaml` should be treated as the normative source once generated or approved.
- The guide does not provide journal-specific manuscript formatting requirements.
- The guide does not replace legal, security, privacy, institutional review, or intellectual-property review.
- The guide assumes the repository architecture and package-control files defined elsewhere in the DSR Framework.
- Some evidence mappings remain at `partially_mapped` status until the publication-readiness model and release records are generated.

## 16. Open questions

1. Should L4 require at least one independent reviewer, or is a documented self-review sufficient for early releases?
2. Should L5 require DOI registration through Zenodo, or should the model allow alternative archival registries?
3. Should publication readiness include a minimum number of example packages for reusable protocols?
4. Should review severity levels be standardized across all checklists and review records?
5. Should journal-submission readiness be modeled separately from repository-release readiness?

## 17. Change history

| version | date | change | responsible_party |
|---|---|---|---|
| 0.1.0 | 2026-04-27 | Initial draft of publication and review guidance for L4 reusable package release. | GPT-5.5 Thinking |
