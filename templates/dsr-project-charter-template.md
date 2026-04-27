<!-- SPDX-License-Identifier: CC0-1.0 -->
---
template_id: dsr_project_charter_template
selection_id: template_project_charter
target_path: templates/dsr-project-charter-template.md
item_type: template
portion_type: template
output_format: markdown
title: DSR Project Charter Template
purpose: >
  Provide a human-facing charter template for initiating, classifying, scoping,
  planning, and reviewing a Design Science Research project before detailed
  problem, objective, artifact, demonstration, evaluation, contribution, and
  package records are completed.
status: draft
version: "0.1.0"
conformance_target: l2_reviewable
owner: dsr_framework_maintainers
responsible_roles:
  - framework_author
  - dsr_project_lead
  - artifact_steward
  - reviewer
source_basis:
  - source_id: user_current_request
    role: immediate_task_definition
    evidence_status: mapped
  - source_id: dsr_framework_generation_spec
    role: governing_generation_specification
    evidence_status: mapped
  - source_id: dsr_framework_generation_prompt
    role: generation_procedure
    evidence_status: mapped
  - source_id: dsr_lifecycle_model
    role: lifecycle_dependency
    evidence_status: mapped_from_existing_framework_file
  - source_id: dsr_extraction_corpus
    role: scholarly_and_methodological_evidence_base
    evidence_status: not_yet_mapped
related_items:
  upstream_dependencies:
    - id: model_lifecycle
      path: models/dsr-lifecycle-model.yaml
      relationship: supplies_stage_structure_and_lifecycle_decision_logic
    - id: spec_dsr_lifecycle_contribution
      path: specs/product-dsr-lifecycle-and-contribution-model.yaml
      relationship: governs_lifecycle_and_contribution_concepts
    - id: spec_templates_checklists
      path: specs/product-dsr-templates-and-checklists.yaml
      relationship: governs_template_operating_material
  downstream_outputs:
    - id: template_problem_objectives
      path: templates/problem-and-objectives-template.md
      relationship: elaborates_problem_objectives_requirements_and_success_criteria
    - id: template_solution_space
      path: templates/solution-space-record-template.yaml
      relationship: elaborates_solution_space_grounding
    - id: template_design_rationale
      path: templates/design-rationale-template.md
      relationship: elaborates_design_decisions_alternatives_and_tradeoffs
    - id: template_artifact_specification
      path: templates/artifact-specification-template.md
      relationship: elaborates_artifact_components_boundary_and_use_logic
    - id: template_demonstration_record
      path: templates/demonstration-record-template.yaml
      relationship: records_artifact_demonstration_context_and_use_scenario
    - id: template_evaluation_plan
      path: templates/evaluation-plan-template.yaml
      relationship: plans_artifact_quality_utility_and_contribution_evaluation
    - id: template_contribution_claim
      path: templates/contribution-claim-template.yaml
      relationship: formalizes_contribution_claims
    - id: template_transparency_crosswalk
      path: templates/dsr-transparency-crosswalk-template.yaml
      relationship: maps_project_evidence_to_transparency_dimensions
change_history:
  - version: "0.1.0"
    date: "2026-04-27"
    change: Initial L2 reviewable Markdown charter template.
    responsible_party: GPT-5.5 Thinking
---

# DSR Project Charter

> **Use this template when starting or re-scoping a Design Science Research project.** Replace every `TODO:` item with project-specific content. If a section is not applicable, write `Not applicable` and give the rationale. Do not delete required review sections unless a tailoring decision is recorded.

## 0. Template Use and Review Status

| Field | Entry |
|---|---|
| Project title | TODO: Enter the working project title. |
| Project short name or slug | TODO: Enter a lower-kebab-case or lower_snake_case short identifier. |
| Charter version | TODO: Enter version, e.g., `0.1.0`. |
| Charter status | TODO: `draft`, `in_review`, `approved`, `superseded`, or `archived`. |
| Date opened | TODO: YYYY-MM-DD. |
| Date last revised | TODO: YYYY-MM-DD. |
| DSR project lead | TODO: Name or role. |
| Artifact steward | TODO: Name or role responsible for artifact versioning and stewardship. |
| Primary reviewer | TODO: Name or role. |
| Target conformance level | TODO: Usually `l2_reviewable` for an initial charter. |
| Repository or package location | TODO: Path or URL if known. |
| Related package inventory entry | TODO: Package inventory item ID or `not_yet_registered`. |

### Charter Control Notes

- **Purpose of this charter:** TODO: State why the project is being initiated and what decision this charter should support.
- **Decision requested from reviewer or sponsor:** TODO: Example: approve DSR-candidate status, approve problem framing, request revision, reject as non-DSR, or defer.
- **Known tailoring decisions:** TODO: List any sections intentionally omitted, simplified, or expanded.

---

## 1. DSR Identity Statement

### 1.1 Candidate DSR Classification

| Classification Question | Response |
|---|---|
| Is this work intended to create, adapt, configure, or specify an artifact? | TODO: Yes/No/Unclear, with rationale. |
| What artifact or artifact type is expected? | TODO: Construct, model, method, instantiation, framework, taxonomy, ontology, protocol, template set, software object, dataset, package, or other. |
| What practical problem or opportunity motivates artifact development? | TODO: Describe the problem or opportunity in one or two paragraphs. |
| Why is an artifact-based intervention appropriate? | TODO: Explain why documentation, explanation, analysis, or routine process improvement alone is insufficient. |
| What design knowledge may be produced? | TODO: State expected reusable knowledge, such as a method, model, guideline, pattern, ontology, evaluation logic, or artifact package structure. |
| What would make the work non-DSR? | TODO: Identify exclusion risks, such as routine implementation, consulting-only work, purely explanatory research, or no artifact contribution. |

### 1.2 DSR Boundary Statement

**Working boundary:** TODO: State what is inside the DSR project boundary.

**Outside scope:** TODO: State what is explicitly outside the project boundary.

**Routine design risk:** TODO: Explain whether the work risks being only routine design, and how the project will avoid overclaiming.

**Artifact instance versus artifact type:** TODO: Explain whether the project will produce a local instance, a reusable artifact type, or both.

---

## 2. Problem Space

### 2.1 Problem Class and Local Problem Instance

| Field | Entry |
|---|---|
| Problem class | TODO: Name the broader class of problems to which this project belongs. |
| Local problem instance | TODO: Describe the immediate setting, organization, domain, or use case. |
| Problem severity or importance | TODO: Explain why the problem matters. |
| Current unsatisfactory state | TODO: Describe what is missing, inefficient, risky, ambiguous, invalid, unreliable, inaccessible, or otherwise deficient. |
| Desired improvement | TODO: Describe the intended improvement in practical, operational, or knowledge terms. |
| Timeframe or urgency | TODO: Identify relevant deadlines, review cycles, release cycles, or historical constraints. |

### 2.2 Context and Boundary Conditions

| Context Dimension | Description |
|---|---|
| Domain or discipline | TODO |
| Organizational setting | TODO |
| Technical setting | TODO |
| Data, documentation, or evidence setting | TODO |
| Regulatory, policy, or governance setting | TODO |
| Social, cultural, ethical, or accessibility context | TODO |
| Known boundary conditions | TODO |
| Known assumptions | TODO |
| Known constraints | TODO |

### 2.3 Stakeholders and Audiences

| Stakeholder or Audience | Role in Project | Needs or Concerns | Involvement Stage | Evidence Needed |
|---|---|---|---|---|
| TODO: Project sponsor | TODO | TODO | TODO | TODO |
| TODO: Intended artifact user | TODO | TODO | TODO | TODO |
| TODO: Affected stakeholder | TODO | TODO | TODO | TODO |
| TODO: Reviewer or evaluator | TODO | TODO | TODO | TODO |
| TODO: Artifact steward or maintainer | TODO | TODO | TODO | TODO |

---

## 3. Objectives, Requirements, and Success Criteria

### 3.1 Objective Summary

| Objective ID | Objective Statement | Objective Type | Source Problem or Stakeholder Need | Success Criterion | Evidence or Review Method |
|---|---|---|---|---|---|
| OBJ-001 | TODO | functional / quality / documentation / evaluation / contribution / responsible-design | TODO | TODO | TODO |
| OBJ-002 | TODO | TODO | TODO | TODO | TODO |
| OBJ-003 | TODO | TODO | TODO | TODO | TODO |

### 3.2 Requirement Summary

| Requirement ID | Requirement Statement | Requirement Type | Priority | Verification, Demonstration, or Evaluation Path | Related Objective |
|---|---|---|---|---|---|
| REQ-001 | TODO | functional | must / should / may | TODO | OBJ-001 |
| REQ-002 | TODO | quality | must / should / may | TODO | TODO |
| REQ-003 | TODO | documentation | must / should / may | TODO | TODO |
| REQ-004 | TODO | evaluation | must / should / may | TODO | TODO |

### 3.3 Success-Criteria Distinctions

| Claim Type | Initial Success Criterion | Evidence Needed | Limitation if Evidence Is Missing |
|---|---|---|---|
| Artifact quality | TODO: Criterion for internal quality, completeness, correctness, usability, maintainability, or fitness. | TODO | TODO |
| Artifact utility | TODO: Criterion for usefulness in the local problem instance or scenario. | TODO | TODO |
| Contribution to knowledge | TODO: Criterion for reusable, projectable, or publishable design knowledge. | TODO | TODO |
| Package reviewability | TODO: Criterion for reviewer navigation, traceability, conformance, and evidence availability. | TODO | TODO |

---

## 4. Solution Space and Prior Knowledge

### 4.1 Initial Knowledge-Base Scan

| Source or Knowledge Family | Relevance to Problem | Relevance to Artifact | Status | Notes |
|---|---|---|---|---|
| TODO: DSR lifecycle or methodology source | TODO | TODO | mapped / not_yet_mapped / pending_review | TODO |
| TODO: Domain literature or standard | TODO | TODO | TODO | TODO |
| TODO: Existing artifact, method, or tool | TODO | TODO | TODO | TODO |
| TODO: Prior internal framework file | TODO | TODO | TODO | TODO |

### 4.2 Solution Alternatives

| Alternative ID | Alternative Description | Adopt / Adapt / Reject / Defer | Rationale | Tradeoffs or Risks |
|---|---|---|---|---|
| ALT-001 | TODO | TODO | TODO | TODO |
| ALT-002 | TODO | TODO | TODO | TODO |
| ALT-003 | TODO | TODO | TODO | TODO |

### 4.3 Novelty and Reuse Positioning

- **What appears reused:** TODO
- **What appears adapted:** TODO
- **What appears new or non-routine:** TODO
- **What appears routine and should not be overclaimed:** TODO
- **Evidence still needed to support novelty:** TODO

---

## 5. Artifact Concept

### 5.1 Artifact Identity

| Field | Entry |
|---|---|
| Artifact working name | TODO |
| Artifact type | TODO: Construct, model, method, instantiation, framework, taxonomy, ontology, protocol, template, checklist, schema, software, dataset, package, or other. |
| Artifact materiality | TODO: conceptual_only, textual_or_documentary, software, data, socio_technical, mixed, or other. |
| Artifact abstraction level | TODO: local instance, reusable type, method, model, framework, theory-oriented, package-level artifact. |
| Artifact boundary | TODO: What counts as part of the artifact? What does not? |
| Intended users | TODO |
| Intended use context | TODO |
| Expected outputs | TODO |

### 5.2 Make/Build Logic and Use Logic

| Logic Type | Charter-Level Description | Later Record or Template |
|---|---|---|
| Make or build logic | TODO: How will the artifact be created, authored, configured, compiled, modeled, or packaged? | `templates/artifact-specification-template.md`; `templates/build-transparency-record-template.yaml` |
| Use logic | TODO: How should intended users apply or operate the artifact? | `templates/artifact-specification-template.md`; `templates/demonstration-record-template.yaml` |
| Capacity or function claims | TODO: What should the artifact enable, improve, validate, structure, or communicate? | `templates/evaluation-plan-template.yaml` |
| Maintenance or stewardship logic | TODO: How will changes, defects, versions, and deprecations be handled? | Release and preservation records |

### 5.3 Component Sketch

| Component ID | Component Name | Component Function | Required for Minimum Viable Artifact? | Evidence or Review Need |
|---|---|---|---|---|
| CMP-001 | TODO | TODO | yes / no / conditional | TODO |
| CMP-002 | TODO | TODO | TODO | TODO |
| CMP-003 | TODO | TODO | TODO | TODO |

---

## 6. Lifecycle Plan

Use this table to document the initial lifecycle status. A stage may be marked `not_started`, `active`, `blocked`, `ready_for_review`, `accepted`, `requires_iteration`, `deferred`, or `not_applicable_with_rationale`.

| Stage ID | Stage Label | Charter-Level Status | Required or Expected Output | Owner | Exit Evidence or Acceptance Criterion |
|---|---|---|---|---|---|
| lc01 | Initiate and classify DSR effort | TODO | Project charter; initial DSR identity statement | TODO | DSR rationale or exclusion rationale is documented. |
| lc02 | Define problem space | TODO | Problem and objectives record | TODO | Problem class, local problem instance, stakeholders, and boundaries are explicit. |
| lc03 | Define objectives, requirements, and success criteria | TODO | Objectives, requirements, and acceptance criteria | TODO | Objectives are reviewable and linked to evaluation paths. |
| lc04 | Ground solution space | TODO | Solution-space record; alternatives log | TODO | Major design choices are grounded or marked not_yet_mapped. |
| lc05 | Specify artifact and design rationale | TODO | Artifact specification; design rationale | TODO | Artifact boundary, components, make/use logic, and rationale are explicit. |
| lc06 | Build or configure artifact | TODO | Build transparency record; artifact version | TODO | Reviewable artifact snapshot exists with known limitations. |
| lc07 | Demonstrate artifact use | TODO | Demonstration record; example or walkthrough | TODO | Demonstration context, inputs, outputs, and limitations are recorded. |
| lc08 | Plan and execute evaluation | TODO | Evaluation plan; evaluation report | TODO | Evaluation evidence is linked to objectives and claims. |
| lc09 | Position contribution | TODO | Contribution claim; contribution positioning record | TODO | Claims have evidence, scope, boundaries, and limitations. |
| lc10 | Communicate and package | TODO | Metadata, inventory, conformance, transparency crosswalk | TODO | Package is navigable, traceable, and reviewable. |
| lc11 | Review, release, and steward | TODO | Review record; release or preservation record | TODO | Release or non-release decision is recorded. |

### 6.1 Initial Lifecycle Entry Point

Select the best entry point and explain the rationale.

- [ ] Problem-centered entry: the project begins from a clearly experienced problem, organizational need, or research gap.
- [ ] Objective-centered entry: the project begins from a stated objective but still needs problem validation.
- [ ] Design-and-development-centered entry: a candidate artifact already exists but needs DSR grounding, evaluation, and contribution positioning.
- [ ] Evaluation-centered entry: an artifact exists and the project centers on evaluation and knowledge contribution.
- [ ] Communication-and-packaging entry: a body of work exists and needs packaging, traceability, and reviewability.

**Entry-point rationale:** TODO

### 6.2 Decision Gates

| Gate ID | Decision Point | Evidence Required | Possible Decisions | Current Disposition |
|---|---|---|---|---|
| GATE-01 | DSR identity gate | Charter, problem statement, artifact role, contribution expectation | accept / revise / reject_non_dsr / defer | TODO |
| GATE-02 | Problem-objective alignment gate | Problem-space record, objectives, requirements, success criteria | accept / revise / narrow_scope / defer | TODO |
| GATE-03 | Artifact specification gate | Solution grounding, artifact specification, design rationale | accept / revise / split_artifact / defer | TODO |
| GATE-04 | Demonstration readiness gate | Artifact snapshot, use scenario, demonstration plan | accept / revise / return_to_build / defer | TODO |
| GATE-05 | Evaluation readiness gate | Evaluation plan, criteria, evidence sources, limitations | accept / revise / narrow_claims / defer | TODO |
| GATE-06 | Contribution and package review gate | Contribution claim, evaluation report, transparency crosswalk, inventory | accept / revise / lower_conformance / defer | TODO |

---

## 7. Demonstration and Evaluation Intent

### 7.1 Demonstration Intent

| Field | Entry |
|---|---|
| Demonstration type | TODO: illustrative, simulated, example package, pilot, field use, walkthrough, expert scenario, or other. |
| Demonstration context | TODO |
| Demonstration user or role | TODO |
| Demonstration task | TODO |
| Demonstration outputs | TODO |
| What the demonstration can show | TODO |
| What the demonstration cannot prove | TODO |

### 7.2 Evaluation Intent

| Evaluation Question ID | Evaluation Question | Claim Type | Timing | Method Family | Evidence Needed | Decision Use |
|---|---|---|---|---|---|---|
| EQ-001 | TODO | artifact_quality / artifact_utility / contribution / package_quality | formative / summative / both | TODO | TODO | accept / revise / reject / narrow_claim |
| EQ-002 | TODO | TODO | TODO | TODO | TODO | TODO |
| EQ-003 | TODO | TODO | TODO | TODO | TODO | TODO |

### 7.3 Validity, Reliability, Replication, and Projectability Risks

| Quality Concern | Initial Risk | Planned Mitigation | Evidence Needed |
|---|---|---|---|
| Validity | TODO | TODO | TODO |
| Reliability | TODO | TODO | TODO |
| Replication or repeatability | TODO | TODO | TODO |
| Projectability or transfer | TODO | TODO | TODO |
| Responsible design | TODO | TODO | TODO |

---

## 8. Contribution Positioning

### 8.1 Candidate Contribution Claims

| Claim ID | Candidate Claim | Contribution Type | Knowledge Goal | Knowledge Scope | Evidence Needed | Boundary Conditions |
|---|---|---|---|---|---|---|
| CLAIM-001 | TODO | artifact / method / model / framework / evaluation / reporting / theory / package | definitional / descriptive / explanatory / predictive / prescriptive / methodological / evaluative | idiographic / projectable / nomothetic / mixed | TODO | TODO |
| CLAIM-002 | TODO | TODO | TODO | TODO | TODO | TODO |
| CLAIM-003 | TODO | TODO | TODO | TODO | TODO | TODO |

### 8.2 Contribution Audiences

| Audience | What They Need from the Project | Intended Communication Product |
|---|---|---|
| Scholarly reviewers | TODO | TODO |
| DSR researchers | TODO | TODO |
| Practitioners or implementers | TODO | TODO |
| Maintainers or artifact stewards | TODO | TODO |
| Public or policy audience, if applicable | TODO | TODO |

### 8.3 Overclaiming Controls

- **Claims that should remain local unless more evidence is gathered:** TODO
- **Claims that may become projectable with boundary conditions:** TODO
- **Claims that should not be made in this project:** TODO
- **Evidence that would be required for stronger claims:** TODO

---

## 9. Transparency Plan

| Transparency Dimension | Charter-Level Commitment | Planned Evidence or File | Current Status |
|---|---|---|---|
| Process transparency | TODO: How will decisions, iterations, and deviations be recorded? | TODO | not_started / active / mapped / deferred |
| Problem-space transparency | TODO: How will context, stakeholders, scope, and boundaries be recorded? | TODO | TODO |
| Solution-space transparency | TODO: How will knowledge grounding, alternatives, and prior artifacts be recorded? | TODO | TODO |
| Build transparency | TODO: How will artifact construction, versions, and rationale be recorded? | TODO | TODO |
| Evaluation transparency | TODO: How will criteria, methods, findings, and limitations be recorded? | TODO | TODO |
| Contribution transparency | TODO: How will practical and scholarly claims be documented and bounded? | TODO | TODO |

### 9.1 Evidence and Record Retention

| Evidence or Record | Purpose | Expected Location | Retention Rule | Owner |
|---|---|---|---|---|
| Project charter | Initiate and classify DSR project | `templates/dsr-project-charter-template.md` or project-specific record | Retain while project is active and archive with release package. | TODO |
| Problem and objectives record | Preserve problem-space and success criteria | TODO | TODO | TODO |
| Solution-space record | Preserve grounding and alternatives | TODO | TODO | TODO |
| Design rationale | Preserve design choices and tradeoffs | TODO | TODO | TODO |
| Build transparency record | Preserve artifact construction evidence | TODO | TODO | TODO |
| Demonstration record | Preserve demonstration scenario and limits | TODO | TODO | TODO |
| Evaluation plan and report | Preserve evaluation design and findings | TODO | TODO | TODO |
| Contribution claim | Preserve claim scope and evidence basis | TODO | TODO | TODO |
| Review and release records | Preserve gate decisions and release status | TODO | TODO | TODO |

---

## 10. Risks, Constraints, and Responsible Design

### 10.1 Risk Register

| Risk ID | Risk Description | Risk Type | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| RISK-001 | TODO | technical / evidence / validity / stakeholder / ethical / schedule / maintenance / publication | low / medium / high | low / medium / high | TODO | TODO | open |
| RISK-002 | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| RISK-003 | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

### 10.2 Responsible Design Considerations

| Consideration | Charter-Level Assessment | Action Needed |
|---|---|---|
| Stakeholder inclusion | TODO | TODO |
| Accessibility and usability | TODO | TODO |
| Privacy, confidentiality, or security | TODO | TODO |
| Equity or unintended harms | TODO | TODO |
| Maintenance burden | TODO | TODO |
| Transparency burden or overload | TODO | TODO |
| Intellectual property or licensing | TODO | TODO |

---

## 11. Minimum Reviewability Checklist

Mark each item before moving the charter from `draft` to `in_review`.

- [ ] The project has a working title, owner, steward, and reviewer.
- [ ] The charter states why the project is a DSR candidate.
- [ ] The intended artifact or artifact uncertainty is explicit.
- [ ] The local problem instance is distinguished from the broader problem class.
- [ ] Stakeholders and intended users are identified.
- [ ] Objectives, requirements, and success criteria are separated.
- [ ] Artifact quality, artifact utility, and contribution-to-knowledge claims are not conflated.
- [ ] Demonstration intent is distinguished from evaluation intent.
- [ ] Initial contribution claims include knowledge goal, knowledge scope, evidence needs, and boundary conditions.
- [ ] The lifecycle stage plan identifies current status and expected outputs.
- [ ] Transparency obligations are mapped to planned evidence or records.
- [ ] Known risks, limitations, assumptions, and open questions are recorded.
- [ ] The charter identifies downstream templates or records that must be completed next.

---

## 12. Assumptions, Limitations, and Open Questions

### 12.1 Assumptions

| Assumption ID | Assumption | Basis | Validation or Review Plan |
|---|---|---|---|
| ASM-001 | TODO | TODO | TODO |
| ASM-002 | TODO | TODO | TODO |
| ASM-003 | TODO | TODO | TODO |

### 12.2 Limitations

| Limitation ID | Limitation | Consequence | Mitigation or Disclosure Plan |
|---|---|---|---|
| LIM-001 | TODO | TODO | TODO |
| LIM-002 | TODO | TODO | TODO |
| LIM-003 | TODO | TODO | TODO |

### 12.3 Open Questions

| Question ID | Open Question | Responsible Role | Needed Input | Target Disposition |
|---|---|---|---|---|
| OQ-001 | TODO | TODO | TODO | resolve / defer / record_as_limitation |
| OQ-002 | TODO | TODO | TODO | TODO |
| OQ-003 | TODO | TODO | TODO | TODO |

---

## 13. Charter Approval and Disposition

| Role | Name or Role Holder | Decision | Date | Notes |
|---|---|---|---|---|
| DSR project lead | TODO | approve / request_revision / reject / defer | TODO | TODO |
| Artifact steward | TODO | approve / request_revision / reject / defer | TODO | TODO |
| Reviewer | TODO | approve / request_revision / reject / defer | TODO | TODO |
| Sponsor or owner, if applicable | TODO | approve / request_revision / reject / defer | TODO | TODO |

### 13.1 Disposition Statement

**Disposition:** TODO: `approved_for_problem_objectives_work`, `approved_for_solution_grounding`, `requires_revision`, `rejected_as_non_dsr`, `deferred`, or other controlled disposition.

**Rationale:** TODO

**Next required file or record:** TODO: Example: `templates/problem-and-objectives-template.md`, `templates/solution-space-record-template.yaml`, or `records/design-decisions/record-dsr-identity-decision.yaml`.

---

## 14. Embedded Template Quality Gate Mapping

| Quality Gate | How This Charter Supports the Gate | Reviewer Evidence |
|---|---|---|
| Consistency | Uses the target path, template naming convention, status values, lifecycle stage IDs, and related-item links. | File metadata, lifecycle table, related items. |
| Coherence | Connects DSR identity, problem space, objectives, artifact concept, lifecycle plan, evaluation intent, contribution positioning, and transparency. | Completed sections 1-9. |
| Cogency | Orders information from initiation through review disposition and separates claims from evidence. | Completed objectives, requirements, lifecycle, and risk tables. |
| Correspondence | Frames the project as part of a reviewable DSR artifact package rather than an isolated narrative. | Related outputs and conformance fields. |
| DSR transparency | Includes process, problem-space, solution-space, build, evaluation, and contribution transparency planning. | Section 9 transparency table. |
| Reviewability | Includes review checklist, decision gates, acceptance criteria, assumptions, limitations, open questions, and disposition. | Sections 6, 11, 12, and 13. |

