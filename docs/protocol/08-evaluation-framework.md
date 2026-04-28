<!-- SPDX-License-Identifier: CC0-1.0 -->

# Evaluation Framework

## Controlled source links

- [models/dsr-evaluation-alignment-model.yaml](../../models/dsr-evaluation-alignment-model.yaml)
- [vocabularies/evaluation-method-families.yaml](../../vocabularies/evaluation-method-families.yaml)
- [templates/evaluation-plan-template.yaml](../../templates/evaluation-plan-template.yaml)
- [templates/evaluation-report-template.yaml](../../templates/evaluation-report-template.yaml)
- [checklists/evaluation-readiness-checklist.yaml](../../checklists/evaluation-readiness-checklist.yaml)

```yaml
item_id: docs_evaluation
selection_id: docs_evaluation
item_type: description
title: Evaluation Framework
target_path: docs/protocol/08-evaluation-framework.md
status: draft
version: "0.1.0"
owner: dsr_framework_maintainers
conformance_target: l2_reviewable
source_model: models/dsr-evaluation-alignment-model.yaml
related_items:
  upstream:
    - models/dsr-evaluation-alignment-model.yaml
    - vocabularies/evaluation-method-families.yaml
    - vocabularies/validity-types.yaml
    - vocabularies/reliability-types.yaml
    - vocabularies/projectability-types.yaml
  downstream:
    - templates/evaluation-plan-template.yaml
    - templates/evaluation-report-template.yaml
    - schemas/dsr-evaluation-plan.schema.json
    - schemas/dsr-evaluation-report.schema.json
    - checklists/evaluation-readiness-checklist.yaml
    - records/evaluations/record-evaluation-plan-0001.yaml
source_basis:
  - dsr_framework_generation_spec
  - dsr_evaluation_alignment_model
  - dsr_extraction_corpus
change_history:
  - version: "0.1.0"
    date: "2026-04-27"
    change: Initial human-facing evaluation framework guide generated for L2 review.
```

## 1. Purpose

This page explains how to plan, document, and review evaluation in the DSR Framework. It is the human-facing guide for the controlled evaluation alignment model. The controlled source of truth is `models/dsr-evaluation-alignment-model.yaml`; this page renders the model into practical instructions for authors, reviewers, and maintainers.

The evaluation framework exists to prevent unsupported DSR claims. Every important claim about an artifact, method, model, template, schema, contribution, or framework package should be traceable to evaluation questions, criteria, methods, evidence, results, limitations, and review decisions.

## 2. Evaluation in DSR

In this framework, evaluation is the disciplined assessment of an evaluation subject against explicit claims and criteria. It is broader than testing a software artifact and narrower than general research justification.

Evaluation may address:

- artifact existence: whether the artifact exists, is identifiable, and has a stable version or state;
- artifact boundary: whether the artifact components, exclusions, dependencies, and intended use are clear;
- problem-solution fit: whether artifact features respond to the stated problem, objectives, and requirements;
- artifact quality: whether the artifact has relevant properties such as correctness, completeness, reliability, usability, security, maintainability, or interoperability;
- artifact utility: whether the artifact helps intended users perform intended tasks in intended contexts;
- contribution to knowledge: whether the work contributes projectable design knowledge beyond routine local construction;
- contribution significance: whether the contribution is non-trivial relative to prior artifacts, methods, theories, or practices;
- validity, reliability, and projectability: whether the evaluation and the resulting claims are credible, consistent, and appropriately bounded;
- responsible design: whether relevant ethical, social, privacy, security, accessibility, and stakeholder-value obligations are addressed.

Evaluation is claim-relative. A small demonstration may be sufficient for a feasibility claim, but not for a broad naturalistic utility claim. A literature-based argument may support contribution positioning, but not actual field effectiveness unless paired with appropriate use evidence.

## 3. Core distinctions

### 3.1 Demonstration versus evaluation

A demonstration shows that an artifact can be used or can produce an illustrative output. Evaluation judges a defined claim against explicit criteria using a declared method and interpretable evidence.

| Evidence activity | Primary question | Typical output | Claim strength supported |
|---|---|---|---|
| Demonstration | Can the artifact operate or illustrate the idea? | Example use case, walkthrough, prototype output | feasibility, plausibility, operability |
| Formative evaluation | What should be improved while the artifact is being designed? | defects, design feedback, revised requirements | design refinement, quality improvement |
| Summative evaluation | Are the stated claims supported by evidence? | findings, criteria judgments, limitations | bounded utility, quality, contribution, or readiness |
| Naturalistic evaluation | Does the artifact work in intended or representative use conditions? | real-use evidence, stakeholder feedback, field results | stronger utility and projectability claims |

Do not report a demonstration as a full evaluation unless it includes criteria, method, evidence, interpretation, and limitations. When only demonstration evidence exists, qualify the supported claim accordingly.

### 3.2 Artifact utility versus artifact quality versus knowledge contribution

These three concepts are related but not interchangeable.

| Claim object | Question | Evidence examples | Common failure mode |
|---|---|---|---|
| Artifact utility | Does the artifact help intended users or contexts achieve intended ends? | task success, stakeholder feedback, before/after indicators, field-use evidence | declaring usefulness without a use case or user context |
| Artifact quality | Does the artifact have required internal or external properties? | validation checks, formal analysis, test results, inspection findings, usability review | naming a quality attribute without operationalizing it |
| Contribution to knowledge | Does the work produce reusable, projectable, or publishable design knowledge? | prior-work positioning, design principles, problem-class framing, contribution typology mapping | treating local delivery as general knowledge without abstraction |

A strong DSR report should make clear which of these are being claimed and what evidence supports each claim.

### 3.3 Ex ante, formative, summative, ex post, and longitudinal evaluation

Evaluation timing should match the artifact state and claim type.

| Timing | Use when | Typical evidence |
|---|---|---|
| Ex ante | The artifact is not fully built or deployed, but design choices require assessment. | expert review, formal analysis, simulation, design rationale, literature-based argument |
| Formative | Design is still changing and feedback is needed. | prototype testing, review findings, log analysis, stakeholder feedback, defect lists |
| Summative | The artifact is sufficiently stable for judgment. | controlled test results, field evidence, usability results, quality review, contribution review |
| Ex post | The artifact has been implemented, used, released, or published. | adoption data, use records, retrospective review, field outcomes, citation or reuse evidence |
| Longitudinal | Persistence, adaptation, evolution, reuse, or sustained utility matters. | repeated observations, maintenance records, version comparisons, reuse cases |

### 3.4 Artificial and naturalistic settings

Artificial evaluation settings are controlled, analytical, simulated, or illustrative. Naturalistic settings involve real or representative users, environments, tasks, and inputs. Artificial settings are often appropriate for early-stage or technical claims; naturalistic settings are usually stronger for field-utility, stakeholder-acceptance, and projectability claims.

## 4. Minimum L2 evaluation alignment chain

For L2 reviewable conformance, every substantive claim should have an explicit trace chain or a documented reason for deferral.

```text
claim
  -> evaluation question
  -> evaluation criterion
  -> indicator or reasoning rule
  -> evaluation method
  -> evidence item or evidence status
  -> evaluation result or planned result
  -> limitation or threat
  -> acceptance decision or review status
```

The chain may be simple for low-risk claims. For example, an artifact existence claim may be evaluated through repository inspection and package inventory review. A broad utility claim requires stronger alignment: intended user, use case, criteria, method, evidence, and limitations.

## 5. Evaluation workflow

### 5.1 Scope the evaluation

Identify what is being evaluated and why.

Required outputs:

- evaluation subject;
- artifact or component boundary;
- version or state;
- lifecycle stage;
- claim inventory;
- conformance target;
- evaluation assumptions and constraints.

Review questions:

- Is the evaluation subject specific enough to judge?
- Is the artifact state clear?
- Are local, reusable, and publication-oriented claims separated?

### 5.2 Translate claims into questions

Turn each claim into one or more evaluation questions.

Examples:

| Claim | Evaluation question |
|---|---|
| The template is reusable across DSR projects. | What evidence shows that the template can be adapted across a bounded class of DSR projects? |
| The schema improves reviewability. | Which review tasks become more checkable because of the schema? |
| The artifact contributes design knowledge. | What abstracted principle, model, method, vocabulary, or rule is produced beyond a local instance? |
| The artifact is useful for practitioners. | Which practitioner task, setting, and success criterion does the artifact improve? |

### 5.3 Operationalize criteria

Define how each question will be judged. Criteria should include pass conditions, fail conditions, and interpretation logic.

Good criteria are:

- tied to a claim;
- observable, inspectable, or argumentatively assessable;
- specific to artifact state and conformance level;
- bounded by context and assumptions;
- explicit about what counts as insufficient evidence.

### 5.4 Select methods

Choose methods that fit the claim and artifact state.

| Method family | Strong for | Weak for | Required qualifier |
|---|---|---|---|
| Analytical or conceptual evaluation | coherence, design rationale, boundary, literature alignment | broad field utility | empirical claims remain tentative without use evidence |
| Formal or mathematical evaluation | correctness, consistency, formal properties | stakeholder acceptance, field utility | assumptions and model scope must be stated |
| Prototype demonstration | operability, feasibility, example use | summative utility, projectability | do not overstate beyond demonstration scope |
| Expert review | plausibility, completeness, contribution significance | actual field effectiveness | reviewer expertise and criteria must be declared |
| Controlled user or task evaluation | usability, task success, controlled comparison | naturalistic projectability | artificial conditions must be reported |
| Naturalistic field evaluation | real-use utility, stakeholder value, problem-solution fit | precise causal attribution without comparison | context and boundary conditions must be documented |
| Longitudinal evaluation | sustained utility, evolution, reuse, maintenance | initial feasibility only | time period and version changes must be reported |
| Literature-based or repository evaluation | contribution positioning, accumulated design knowledge, projectability | direct usefulness without use evidence | search scope and selection basis must be documented |
| Mixed methods evaluation | multi-claim evaluation, triangulation | under-specified claims | integration logic must be explicit |

### 5.5 Collect, map, or retain evidence

Evidence may be empirical, formal, documentary, analytical, or review-based. The framework does not require all evidence to be public, but it does require evidence status to be explicit.

Recommended evidence fields:

- evidence identifier;
- evidence type;
- source or location;
- linked method;
- linked claim;
- availability status;
- retention rule;
- limitation notes;
- confidentiality or non-shareability rationale where applicable.

Use `evidence_status: accepted_v1_limitation` when evidence exists in the project but has not yet been linked to the claim. Use `evidence_status: deferred` when the evaluation is intentionally postponed.

### 5.6 Analyze and interpret

Evaluation results should answer evaluation questions, not merely list activities.

Each result should state:

- finding summary;
- evidence summary;
- support status;
- affected claims;
- limitations;
- remaining uncertainty;
- whether the claim should be accepted, qualified, revised, rejected, or deferred.

Allowed claim-support statuses include:

- `supported`;
- `partially_supported`;
- `unsupported`;
- `contradicted`;
- `inconclusive`;
- `not_evaluated`;
- `deferred`.

### 5.7 Decide and report

An evaluation should end in a bounded decision, not a vague positive statement.

Decision examples:

| Decision | Meaning |
|---|---|
| accept_claim | Evidence is sufficient for the stated claim and scope. |
| accept_with_qualification | Evidence supports a narrower or conditional version of the claim. |
| revise_claim | The claim should be rewritten to match the evidence. |
| reject_claim | Evidence does not support the claim. |
| defer_claim | Evaluation is intentionally postponed. |
| require_additional_evidence | The claim remains plausible but lacks sufficient evidence. |

## 6. Claim-to-evidence guidance

### 6.1 Artifact existence claim

Minimum L2 evidence:

- artifact name and identifier;
- artifact type;
- version or state;
- location or reference;
- boundary statement.

Typical methods:

- document inspection;
- repository inventory review.

Insufficient evidence:

- artifact is named but not located;
- artifact type is ambiguous;
- artifact exists only as an idea with no defined boundary.

### 6.2 Artifact boundary claim

Minimum L2 evidence:

- component list;
- included and excluded scope;
- artifact instance or artifact universal distinction;
- dependencies;
- assumptions.

Typical methods:

- artifact specification review;
- ontology alignment review.

Insufficient evidence:

- implementation instance is treated as reusable design knowledge without abstraction;
- theory, model, template, schema, or method is not bounded as an artifact.

### 6.3 Problem-solution fit claim

Minimum L2 evidence:

- problem statement;
- stakeholder or context statement;
- solution objectives;
- requirements or success criteria;
- trace from problem elements to artifact features.

Typical methods:

- requirements traceability review;
- expert review;
- case walkthrough;
- problem-space analysis.

Insufficient evidence:

- features are not mapped to the problem;
- objectives are not operationalized;
- stakeholder value is asserted but not specified.

### 6.4 Artifact utility claim

Minimum L2 evidence:

- intended use case;
- intended user or stakeholder;
- evaluation criterion;
- method and setting;
- evidence or planned evidence;
- limitation statement.

Stronger evidence for higher conformance:

- real or representative use data;
- baseline or comparator;
- stakeholder feedback or performance data;
- naturalistic or mixed setting where the claim scope requires it.

Typical methods:

- prototype demonstration;
- controlled user evaluation;
- field case;
- naturalistic artifact evaluation;
- before/after comparison;
- mixed methods evaluation.

Insufficient evidence:

- declaring usefulness without a use case;
- relying only on author assertion for field utility;
- treating demonstration output as summative evaluation without criteria.

### 6.5 Artifact quality claim

Minimum L2 evidence:

- quality attribute definition;
- artifact part or behavior under review;
- inspection, test, or analysis method;
- result or evidence status.

Typical methods:

- technical test;
- formal analysis;
- schema validation;
- usability inspection;
- security review;
- maintainability review;
- interoperability check.

Insufficient evidence:

- quality attribute is named but not operationalized;
- test scope is not reported;
- quality result is generalized beyond the tested artifact version.

### 6.6 Contribution-to-knowledge claim

Minimum L2 evidence:

- contribution claim text;
- knowledge goal;
- knowledge scope;
- contribution type;
- prior knowledge or alternative baseline;
- evidence that the claim exceeds routine local design.

Typical methods:

- literature positioning;
- contribution typology mapping;
- expert review;
- design principle extraction;
- cross-case or repository analysis.

Insufficient evidence:

- local artifact delivery is claimed as general knowledge without abstraction;
- novelty is claimed without prior-work comparison;
- contribution scope is not stated.

### 6.7 Validity, reliability, and projectability claims

| Claim type | Minimum L2 evidence | Typical methods | Main risk |
|---|---|---|---|
| Validity | validity type, threat, mitigation, residual limitation | validity threat analysis, construct mapping, context boundary review | generic validity language without specific threats |
| Reliability | reliability target, consistency condition, repeatability or agreement basis | inter-rater agreement, repeated execution, audit trail review, procedural replay | claiming repeatability without procedure or conditions |
| Projectability | problem class, transfer scope, boundary conditions, mechanism or design principle | analytical generalization, replication logic, cross-context comparison, repository analysis | broad generalization without problem-class boundaries |

## 7. Evaluation transparency requirements

Evaluation transparency means that readers can understand what was evaluated, how it was evaluated, what evidence was collected, what the evidence supports, and what remains unresolved.

At L2, an evaluation plan or report should disclose:

- evaluation subject and artifact version;
- claim inventory;
- evaluation questions;
- criteria and pass/fail logic;
- method family and method rationale;
- timing and setting;
- evidence status;
- baseline or comparator if used;
- findings or planned findings;
- limitations and threats;
- claim-support decisions;
- repository or retention location for evidence where feasible.

If evidence cannot be shared because of privacy, security, intellectual property, or institutional constraints, document the constraint and provide substitute transparency material such as a summary, redacted extract, pseudocode, screenshots, schema, rubric, or independent review note.

## 8. Evaluation plan structure

An evaluation plan should be created before claims are reported as supported. A minimal L2 plan should include:

```yaml
evaluation_plan:
  plan_id: project_specific_placeholder
  title: project_specific_placeholder
  status: draft
  version: "0.1.0"
  evaluation_subjects: []
  claim_inventory: []
  evaluation_questions: []
  criteria: []
  indicators_or_reasoning_rules: []
  methods: []
  evidence_plan: []
  baselines_or_comparators: []
  limitations_and_threats: []
  decision_rules: []
  traceability_links: []
  retention_and_transparency: []
```

The plan may be short for a low-risk documentation artifact. It should be more detailed when claims involve field utility, stakeholder impact, reuse, publication readiness, safety, security, privacy, or transfer beyond the original context.

## 9. Evaluation report structure

An evaluation report should not merely repeat the plan. It should record what happened, what was found, and what claims are now supportable.

A minimal L2 report should include:

```yaml
evaluation_report:
  report_id: project_specific_placeholder
  linked_plan_id: project_specific_placeholder
  status: draft
  version: "0.1.0"
  evaluation_subjects_reviewed: []
  methods_executed: []
  evidence_collected: []
  results: []
  claim_support_assessments: []
  limitations_and_threats: []
  deviations_from_plan: []
  acceptance_decisions: []
  follow_up_actions: []
  retained_evidence_locations: []
```

## 10. Reviewer checklist

Use these questions when reviewing an evaluation plan or report.

| Check | Review question | Pass condition |
|---|---|---|
| EV-01 | Is every substantive claim inventoried? | Claims are explicit, typed, and scoped. |
| EV-02 | Does every claim translate into evaluation questions? | Each claim has a question or justified deferral. |
| EV-03 | Are criteria operationalized? | Criteria include interpretation logic or pass/fail conditions. |
| EV-04 | Are methods fit-for-claim? | Method timing and setting match claim strength and artifact state. |
| EV-05 | Is demonstration distinguished from evaluation? | Demonstrations are not overstated as summative evidence. |
| EV-06 | Is evidence status explicit? | Evidence is collected, planned, retained, not shareable, deferred, or not yet mapped. |
| EV-07 | Are baselines or comparators handled? | A comparator is used or interpretation without one is justified. |
| EV-08 | Are limitations linked to claims? | Limitations qualify specific findings or decisions. |
| EV-09 | Are decisions bounded? | Acceptance decisions are tied to claim scope and conformance level. |
| EV-10 | Is evaluation transparency adequate? | A reviewer can follow the chain from claim to evidence to decision. |

## 11. Common failure patterns

Avoid the following patterns:

- naming an evaluation method without stating criteria;
- reporting a demonstration as if it were naturalistic evaluation;
- claiming artifact utility without user, task, context, and success condition;
- claiming contribution significance without prior-work positioning;
- claiming projectability without a problem class and boundary conditions;
- treating lack of evidence as positive evidence;
- listing limitations without changing claim strength;
- reporting only favorable findings;
- asserting publication readiness from incomplete or deferred evaluation;
- using a single evidence item to support multiple different claims without explaining the interpretation logic.

## 12. Source-basis notes

This page is grounded in the controlled evaluation alignment model and the DSR corpus. The source basis especially supports the following ideas:

| Source family | Use in this page |
|---|---|
| DSR evaluation alignment model | Defines the claim-to-question-to-criterion-to-method-to-evidence-to-decision chain and the controlled claim categories. |
| DSR transparency literature | Grounds the need to document evaluation methods, criteria, evidence, stakeholder confidence, and limitations. |
| DSR contribution-path literature | Grounds the relationship between evaluation, contribution articulation, knowledge scope, and cumulative design knowledge. |
| DSR naturalistic evaluation and methodology sources | Grounds the demonstration/evaluation boundary and the importance of typical users, environments, and inputs for stronger utility claims. |
| Software-embedded evaluation support literature | Grounds the possibility of embedding evaluation data collection into artifacts while preserving interpretation and context. |
| Integrated DSR evaluation criteria literature | Grounds the idea that criteria should be selected according to knowledge type, artifact type, actor role, and evaluation purpose. |

## 13. Acceptance criteria for this docs page

This page is acceptable for L2 review when:

- it identifies `models/dsr-evaluation-alignment-model.yaml` as the controlled source file;
- it explains the evaluation workflow in human-usable language;
- it preserves the distinction among demonstration, artifact utility, artifact quality, and contribution to knowledge;
- it includes a minimum traceability chain from claims to decisions;
- it states limitations and common overclaiming risks;
- it links evaluation to downstream plans, reports, schemas, templates, checklists, and records;
- it avoids asserting that all DSR projects require the same evaluation methods.

## 14. Open questions and backlog

- Should L3 and higher conformance define stronger minimum evidence expectations for field utility, stakeholder acceptance, and projectability claims?
- Should evaluation method families be expanded with domain-specific examples for education, healthcare, software engineering, policy, and organizational design?
- Should the framework include a scoring rubric for claim-support strength, or should it remain judgment-based at L2?
- Should evidence-retention rules differ for public open artifacts versus restricted institutional or proprietary artifacts?
- Should evaluation reporting include separate short forms for early-stage conceptual artifacts, schemas, templates, and fully implemented socio-technical systems?
<!-- BEGIN GENERATED LITERATURE TRACE ANCHORS -->

## Literature Trace Anchors

```yaml
source_basis:
- source_id: weber_2018_design_science_research
  short_citation: Weber (2018)
  evidence_anchor_id: A10
  supports_construct: evaluation_alignment.methodological
  evidence_role: evaluation
  grounding_decision: adopted
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Weber (2018) grounds evaluation_alignment.methodological through extracted anchor A10: Refines DSR evaluation by
    separating process-quality criteria from outcome-quality criteria.'
- source_id: akoka_comynwattiau_prat_storey_2017_dsr_knowledge_types
  short_citation: Akoka et al. (2017)
  evidence_anchor_id: A11
  supports_construct: evaluation_alignment.evaluative
  evidence_role: evaluation
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Akoka et al. (2017) grounds evaluation_alignment.evaluative through extracted anchor A11: Knowledge-type-specific
    integrated evaluation criteria for nomothetic DSR knowledge.'
- source_id: sjostrom_kruse_haj_bolouri_flensburg_2018_sees
  short_citation: Sjöström et al. (2018)
  evidence_anchor_id: A08
  supports_construct: evaluation_alignment.methodological
  evidence_role: evaluation
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Sjöström et al. (2018) grounds evaluation_alignment.methodological through extracted anchor A08: A six-category framework
    for embedding evaluation data-collection support into DSR software artifacts.'
- source_id: baskerville_kaul_storey_2018_aesthetics_design_science_research
  short_citation: Baskerville, Kaul, and Storey (2018)
  evidence_anchor_id: CA12
  supports_construct: evaluation_alignment.evaluative
  evidence_role: evaluation
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Baskerville, Kaul, and Storey (2018) grounds evaluation_alignment.evaluative through extracted anchor CA12: Extends
    DSR evaluation and contribution logic by operationalizing aesthetic quality as a possible complement to rigor and utility.'
- source_id: hansen_pries_heje_2020_situational_knowledge_network_nexus
  short_citation: Hansen & Pries-Heje (2020)
  evidence_anchor_id: A026
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Hansen & Pries-Heje (2020) grounds evaluation_alignment.prescriptive through extracted anchor A026: Shows how Design
    Science Research can extend kernel theory while producing situational artifacts for a wicked socio-technical problem.'
- source_id: desrist2020_tremblay_lucapp
  short_citation: Tremblay et al. (2020)
  evidence_anchor_id: A10
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Tremblay et al. (2020) grounds evaluation_alignment.prescriptive through extracted anchor A10: Field-grounded mHealth
    design guidelines derived from a stakeholder-centered design-test-redesign process.'
- source_id: krasikov_legner_eurich_2021_open_data_sourcing
  short_citation: Krasikov, Legner, and Eurich 2021
  evidence_anchor_id: CA-08
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Krasikov, Legner, and Eurich 2021 grounds evaluation_alignment.prescriptive through extracted anchor CA-08: A prescriptive,
    ADR-developed enterprise method for open data sourcing with use case documentation, screening, multilevel assessment,
    semantic documentation, and knowledge-graph-based....'
- source_id: da_silva_berkenbrock_berkenbrock_2017_collabtrack_dsr
  short_citation: da Silva, Berkenbrock, and Berkenbrock 2017
  evidence_anchor_id: A13
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'da Silva, Berkenbrock, and Berkenbrock 2017 grounds evaluation_alignment.prescriptive through extracted anchor A13:
    Applied demonstration of using DSR with User-Centered Design and Participatory Design to build and evaluate image-based
    smartphone communication artifacts for collaborative assistive....'
- source_id: schmid_2022_ch3_design_science_research_methodology
  short_citation: Schmid 2022
  evidence_anchor_id: CA-020
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Schmid 2022 grounds evaluation_alignment.prescriptive through extracted anchor CA-020: Applied operationalization
    of canonical DSR methodology for a gamified electronic negotiation training artifact, including contribution classification
    and evaluation strategy.'
- source_id: 978-3-658-40731-5_5
  short_citation: Garayo Maiztegui 2023, ch. 5
  evidence_anchor_id: CA-01
  supports_construct: evaluation_alignment.evaluative
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Garayo Maiztegui 2023, ch. 5 grounds evaluation_alignment.evaluative through extracted anchor CA-01: Operationalized
    DSR case linking company problem relevance, theory-informed e-learning artifact construction, and objective field-experiment
    evaluation for customized ERP process training.'
- source_id: mohammad_husamaldin_2025_sustainable_project_portfolio_management_dsr
  short_citation: Mohammad & Husamaldin (2025)
  evidence_anchor_id: A09
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Mohammad & Husamaldin (2025) grounds evaluation_alignment.prescriptive through extracted anchor A09: Applies Design
    Science Research artifact logic to create a sustainability-oriented Project Portfolio Management framework integrating
    materiality assessment and fuzzy-logic analytics.'
- source_id: skalli_cherrafi_charkaoui_chiarini_shokri_antony_garza_reyes_foster_2025_lss40_framework
  short_citation: Skalli et al. 2025
  evidence_anchor_id: A14
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Skalli et al. 2025 grounds evaluation_alignment.prescriptive through extracted anchor A14: A full operations-management
    example of DSR artifact development, refinement, and field evaluation for a Lean Six Sigma 4.0 implementation framework.'
- source_id: benfell_2021_modeling_functional_requirements_tacit_knowledge
  short_citation: Benfell (2021)
  evidence_anchor_id: A11
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Benfell (2021) grounds evaluation_alignment.prescriptive through extracted anchor A11: Worked DSRM case showing how
    a theoretically grounded requirements-modeling artifact can capture tacit end-user knowledge and bridge requirements to
    design.'
- source_id: s11846-026-00996-0
  short_citation: Gadola et al. (2026)
  evidence_anchor_id: A23
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Gadola et al. (2026) grounds evaluation_alignment.prescriptive through extracted anchor A23: Demonstrates how Design
    Science Research can create and evaluate an intangible, human-centered organizational process artifact in a management
    context.'
- source_id: cauffman_weggeman_2024_sofap_p
  short_citation: Cauffman & Weggeman, 2024
  evidence_anchor_id: A13
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Cauffman & Weggeman, 2024 grounds evaluation_alignment.prescriptive through extracted anchor A13: A detailed domain
    application showing how Design Science Research can produce, document, and validate a context-sensitive psychological
    intervention protocol using CIMO building blocks and....'
- source_id: beinke_fitte_teuteberg_2019_blockchain_ehr
  short_citation: Beinke et al. (2019)
  evidence_anchor_id: A14
  supports_construct: evaluation_alignment.prescriptive
  evidence_role: evaluation
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/08-evaluation-framework.md
  note: 'Beinke et al. (2019) grounds evaluation_alignment.prescriptive through extracted anchor A14: A requirements-grounded
    five-tier blockchain-based electronic health record architecture developed and evaluated using Design Science Research.'
```

<!-- END GENERATED LITERATURE TRACE ANCHORS -->
