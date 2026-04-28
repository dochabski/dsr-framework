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
    evidence_status: accepted_v1_limitation
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

> **Use this template when starting or re-scoping a Design Science Research project.** Replace every `project_specific_placeholder:` item with project-specific content. If a section is not applicable, write `Not applicable` and give the rationale. Do not delete required review sections unless a tailoring decision is recorded.

## 0. Template Use and Review Status

| Field | Entry |
|---|---|
| Project title | project_specific_placeholder: Enter the working project title. |
| Project short name or slug | project_specific_placeholder: Enter a lower-kebab-case or lower_snake_case short identifier. |
| Charter version | project_specific_placeholder: Enter version, e.g., `0.1.0`. |
| Charter status | project_specific_placeholder: `draft`, `in_review`, `approved`, `superseded`, or `archived`. |
| Date opened | project_specific_placeholder: YYYY-MM-DD. |
| Date last revised | project_specific_placeholder: YYYY-MM-DD. |
| DSR project lead | project_specific_placeholder: Name or role. |
| Artifact steward | project_specific_placeholder: Name or role responsible for artifact versioning and stewardship. |
| Primary reviewer | project_specific_placeholder: Name or role. |
| Target conformance level | project_specific_placeholder: Usually `l2_reviewable` for an initial charter. |
| Repository or package location | project_specific_placeholder: Path or URL if known. |
| Related package inventory entry | project_specific_placeholder: Package inventory item ID or `not_yet_registered`. |

### Charter Control Notes

- **Purpose of this charter:** project_specific_placeholder: State why the project is being initiated and what decision this charter should support.
- **Decision requested from reviewer or sponsor:** project_specific_placeholder: Example: approve DSR-candidate status, approve problem framing, request revision, reject as non-DSR, or defer.
- **Known tailoring decisions:** project_specific_placeholder: List any sections intentionally omitted, simplified, or expanded.

---

## 1. DSR Identity Statement

### 1.1 Candidate DSR Classification

| Classification Question | Response |
|---|---|
| Is this work intended to create, adapt, configure, or specify an artifact? | project_specific_placeholder: Yes/No/Unclear, with rationale. |
| What artifact or artifact type is expected? | project_specific_placeholder: Construct, model, method, instantiation, framework, taxonomy, ontology, protocol, template set, software object, dataset, package, or other. |
| What practical problem or opportunity motivates artifact development? | project_specific_placeholder: Describe the problem or opportunity in one or two paragraphs. |
| Why is an artifact-based intervention appropriate? | project_specific_placeholder: Explain why documentation, explanation, analysis, or routine process improvement alone is insufficient. |
| What design knowledge may be produced? | project_specific_placeholder: State expected reusable knowledge, such as a method, model, guideline, pattern, ontology, evaluation logic, or artifact package structure. |
| What would make the work non-DSR? | project_specific_placeholder: Identify exclusion risks, such as routine implementation, consulting-only work, purely explanatory research, or no artifact contribution. |

### 1.2 DSR Boundary Statement

**Working boundary:** project_specific_placeholder: State what is inside the DSR project boundary.

**Outside scope:** project_specific_placeholder: State what is explicitly outside the project boundary.

**Routine design risk:** project_specific_placeholder: Explain whether the work risks being only routine design, and how the project will avoid overclaiming.

**Artifact instance versus artifact type:** project_specific_placeholder: Explain whether the project will produce a local instance, a reusable artifact type, or both.

---

## 2. Problem Space

### 2.1 Problem Class and Local Problem Instance

| Field | Entry |
|---|---|
| Problem class | project_specific_placeholder: Name the broader class of problems to which this project belongs. |
| Local problem instance | project_specific_placeholder: Describe the immediate setting, organization, domain, or use case. |
| Problem severity or importance | project_specific_placeholder: Explain why the problem matters. |
| Current unsatisfactory state | project_specific_placeholder: Describe what is missing, inefficient, risky, ambiguous, invalid, unreliable, inaccessible, or otherwise deficient. |
| Desired improvement | project_specific_placeholder: Describe the intended improvement in practical, operational, or knowledge terms. |
| Timeframe or urgency | project_specific_placeholder: Identify relevant deadlines, review cycles, release cycles, or historical constraints. |

### 2.2 Context and Boundary Conditions

| Context Dimension | Description |
|---|---|
| Domain or discipline | project_specific_placeholder |
| Organizational setting | project_specific_placeholder |
| Technical setting | project_specific_placeholder |
| Data, documentation, or evidence setting | project_specific_placeholder |
| Regulatory, policy, or governance setting | project_specific_placeholder |
| Social, cultural, ethical, or accessibility context | project_specific_placeholder |
| Known boundary conditions | project_specific_placeholder |
| Known assumptions | project_specific_placeholder |
| Known constraints | project_specific_placeholder |

### 2.3 Stakeholders and Audiences

| Stakeholder or Audience | Role in Project | Needs or Concerns | Involvement Stage | Evidence Needed |
|---|---|---|---|---|
| project_specific_placeholder: Project sponsor | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| project_specific_placeholder: Intended artifact user | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| project_specific_placeholder: Affected stakeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| project_specific_placeholder: Reviewer or evaluator | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| project_specific_placeholder: Artifact steward or maintainer | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 3. Objectives, Requirements, and Success Criteria

### 3.1 Objective Summary

| Objective ID | Objective Statement | Objective Type | Source Problem or Stakeholder Need | Success Criterion | Evidence or Review Method |
|---|---|---|---|---|---|
| OBJ-001 | project_specific_placeholder | functional / quality / documentation / evaluation / contribution / responsible-design | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| OBJ-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| OBJ-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 3.2 Requirement Summary

| Requirement ID | Requirement Statement | Requirement Type | Priority | Verification, Demonstration, or Evaluation Path | Related Objective |
|---|---|---|---|---|---|
| REQ-001 | project_specific_placeholder | functional | must / should / may | project_specific_placeholder | OBJ-001 |
| REQ-002 | project_specific_placeholder | quality | must / should / may | project_specific_placeholder | project_specific_placeholder |
| REQ-003 | project_specific_placeholder | documentation | must / should / may | project_specific_placeholder | project_specific_placeholder |
| REQ-004 | project_specific_placeholder | evaluation | must / should / may | project_specific_placeholder | project_specific_placeholder |

### 3.3 Success-Criteria Distinctions

| Claim Type | Initial Success Criterion | Evidence Needed | Limitation if Evidence Is Missing |
|---|---|---|---|
| Artifact quality | project_specific_placeholder: Criterion for internal quality, completeness, correctness, usability, maintainability, or fitness. | project_specific_placeholder | project_specific_placeholder |
| Artifact utility | project_specific_placeholder: Criterion for usefulness in the local problem instance or scenario. | project_specific_placeholder | project_specific_placeholder |
| Contribution to knowledge | project_specific_placeholder: Criterion for reusable, projectable, or publishable design knowledge. | project_specific_placeholder | project_specific_placeholder |
| Package reviewability | project_specific_placeholder: Criterion for reviewer navigation, traceability, conformance, and evidence availability. | project_specific_placeholder | project_specific_placeholder |

---

## 4. Solution Space and Prior Knowledge

### 4.1 Initial Knowledge-Base Scan

| Source or Knowledge Family | Relevance to Problem | Relevance to Artifact | Status | Notes |
|---|---|---|---|---|
| project_specific_placeholder: DSR lifecycle or methodology source | project_specific_placeholder | project_specific_placeholder | mapped / accepted_v1_limitation / pending_review | project_specific_placeholder |
| project_specific_placeholder: Domain literature or standard | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| project_specific_placeholder: Existing artifact, method, or tool | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| project_specific_placeholder: Prior internal framework file | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 4.2 Solution Alternatives

| Alternative ID | Alternative Description | Adopt / Adapt / Reject / Defer | Rationale | Tradeoffs or Risks |
|---|---|---|---|---|
| ALT-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| ALT-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| ALT-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 4.3 Novelty and Reuse Positioning

- **What appears reused:** project_specific_placeholder
- **What appears adapted:** project_specific_placeholder
- **What appears new or non-routine:** project_specific_placeholder
- **What appears routine and should not be overclaimed:** project_specific_placeholder
- **Evidence still needed to support novelty:** project_specific_placeholder

---

## 5. Artifact Concept

### 5.1 Artifact Identity

| Field | Entry |
|---|---|
| Artifact working name | project_specific_placeholder |
| Artifact type | project_specific_placeholder: Construct, model, method, instantiation, framework, taxonomy, ontology, protocol, template, checklist, schema, software, dataset, package, or other. |
| Artifact materiality | project_specific_placeholder: conceptual_only, textual_or_documentary, software, data, socio_technical, mixed, or other. |
| Artifact abstraction level | project_specific_placeholder: local instance, reusable type, method, model, framework, theory-oriented, package-level artifact. |
| Artifact boundary | project_specific_placeholder: What counts as part of the artifact? What does not? |
| Intended users | project_specific_placeholder |
| Intended use context | project_specific_placeholder |
| Expected outputs | project_specific_placeholder |

### 5.2 Make/Build Logic and Use Logic

| Logic Type | Charter-Level Description | Later Record or Template |
|---|---|---|
| Make or build logic | project_specific_placeholder: How will the artifact be created, authored, configured, compiled, modeled, or packaged? | `templates/artifact-specification-template.md`; `templates/build-transparency-record-template.yaml` |
| Use logic | project_specific_placeholder: How should intended users apply or operate the artifact? | `templates/artifact-specification-template.md`; `templates/demonstration-record-template.yaml` |
| Capacity or function claims | project_specific_placeholder: What should the artifact enable, improve, validate, structure, or communicate? | `templates/evaluation-plan-template.yaml` |
| Maintenance or stewardship logic | project_specific_placeholder: How will changes, defects, versions, and deprecations be handled? | Release and preservation records |

### 5.3 Component Sketch

| Component ID | Component Name | Component Function | Required for Minimum Viable Artifact? | Evidence or Review Need |
|---|---|---|---|---|
| CMP-001 | project_specific_placeholder | project_specific_placeholder | yes / no / conditional | project_specific_placeholder |
| CMP-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| CMP-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 6. Lifecycle Plan

Use this table to document the initial lifecycle status. A stage may be marked `not_started`, `active`, `blocked`, `ready_for_review`, `accepted`, `requires_iteration`, `deferred`, or `not_applicable_with_rationale`.

| Stage ID | Stage Label | Charter-Level Status | Required or Expected Output | Owner | Exit Evidence or Acceptance Criterion |
|---|---|---|---|---|---|
| lc01 | Initiate and classify DSR effort | project_specific_placeholder | Project charter; initial DSR identity statement | project_specific_placeholder | DSR rationale or exclusion rationale is documented. |
| lc02 | Define problem space | project_specific_placeholder | Problem and objectives record | project_specific_placeholder | Problem class, local problem instance, stakeholders, and boundaries are explicit. |
| lc03 | Define objectives, requirements, and success criteria | project_specific_placeholder | Objectives, requirements, and acceptance criteria | project_specific_placeholder | Objectives are reviewable and linked to evaluation paths. |
| lc04 | Ground solution space | project_specific_placeholder | Solution-space record; alternatives log | project_specific_placeholder | Major design choices are grounded or marked accepted_v1_limitation. |
| lc05 | Specify artifact and design rationale | project_specific_placeholder | Artifact specification; design rationale | project_specific_placeholder | Artifact boundary, components, make/use logic, and rationale are explicit. |
| lc06 | Build or configure artifact | project_specific_placeholder | Build transparency record; artifact version | project_specific_placeholder | Reviewable artifact snapshot exists with known limitations. |
| lc07 | Demonstrate artifact use | project_specific_placeholder | Demonstration record; example or walkthrough | project_specific_placeholder | Demonstration context, inputs, outputs, and limitations are recorded. |
| lc08 | Plan and execute evaluation | project_specific_placeholder | Evaluation plan; evaluation report | project_specific_placeholder | Evaluation evidence is linked to objectives and claims. |
| lc09 | Position contribution | project_specific_placeholder | Contribution claim; contribution positioning record | project_specific_placeholder | Claims have evidence, scope, boundaries, and limitations. |
| lc10 | Communicate and package | project_specific_placeholder | Metadata, inventory, conformance, transparency crosswalk | project_specific_placeholder | Package is navigable, traceable, and reviewable. |
| lc11 | Review, release, and steward | project_specific_placeholder | Review record; release or preservation record | project_specific_placeholder | Release or non-release decision is recorded. |

### 6.1 Initial Lifecycle Entry Point

Select the best entry point and explain the rationale.

- [ ] Problem-centered entry: the project begins from a clearly experienced problem, organizational need, or research gap.
- [ ] Objective-centered entry: the project begins from a stated objective but still needs problem validation.
- [ ] Design-and-development-centered entry: a candidate artifact already exists but needs DSR grounding, evaluation, and contribution positioning.
- [ ] Evaluation-centered entry: an artifact exists and the project centers on evaluation and knowledge contribution.
- [ ] Communication-and-packaging entry: a body of work exists and needs packaging, traceability, and reviewability.

**Entry-point rationale:** project_specific_placeholder

### 6.2 Decision Gates

| Gate ID | Decision Point | Evidence Required | Possible Decisions | Current Disposition |
|---|---|---|---|---|
| GATE-01 | DSR identity gate | Charter, problem statement, artifact role, contribution expectation | accept / revise / reject_non_dsr / defer | project_specific_placeholder |
| GATE-02 | Problem-objective alignment gate | Problem-space record, objectives, requirements, success criteria | accept / revise / narrow_scope / defer | project_specific_placeholder |
| GATE-03 | Artifact specification gate | Solution grounding, artifact specification, design rationale | accept / revise / split_artifact / defer | project_specific_placeholder |
| GATE-04 | Demonstration readiness gate | Artifact snapshot, use scenario, demonstration plan | accept / revise / return_to_build / defer | project_specific_placeholder |
| GATE-05 | Evaluation readiness gate | Evaluation plan, criteria, evidence sources, limitations | accept / revise / narrow_claims / defer | project_specific_placeholder |
| GATE-06 | Contribution and package review gate | Contribution claim, evaluation report, transparency crosswalk, inventory | accept / revise / lower_conformance / defer | project_specific_placeholder |

---

## 7. Demonstration and Evaluation Intent

### 7.1 Demonstration Intent

| Field | Entry |
|---|---|
| Demonstration type | project_specific_placeholder: illustrative, simulated, example package, pilot, field use, walkthrough, expert scenario, or other. |
| Demonstration context | project_specific_placeholder |
| Demonstration user or role | project_specific_placeholder |
| Demonstration task | project_specific_placeholder |
| Demonstration outputs | project_specific_placeholder |
| What the demonstration can show | project_specific_placeholder |
| What the demonstration cannot prove | project_specific_placeholder |

### 7.2 Evaluation Intent

| Evaluation Question ID | Evaluation Question | Claim Type | Timing | Method Family | Evidence Needed | Decision Use |
|---|---|---|---|---|---|---|
| EQ-001 | project_specific_placeholder | artifact_quality / artifact_utility / contribution / package_quality | formative / summative / both | project_specific_placeholder | project_specific_placeholder | accept / revise / reject / narrow_claim |
| EQ-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| EQ-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 7.3 Validity, Reliability, Replication, and Projectability Risks

| Quality Concern | Initial Risk | Planned Mitigation | Evidence Needed |
|---|---|---|---|
| Validity | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Reliability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Replication or repeatability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Projectability or transfer | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Responsible design | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 8. Contribution Positioning

### 8.1 Candidate Contribution Claims

| Claim ID | Candidate Claim | Contribution Type | Knowledge Goal | Knowledge Scope | Evidence Needed | Boundary Conditions |
|---|---|---|---|---|---|---|
| CLAIM-001 | project_specific_placeholder | artifact / method / model / framework / evaluation / reporting / theory / package | definitional / descriptive / explanatory / predictive / prescriptive / methodological / evaluative | idiographic / projectable / nomothetic / mixed | project_specific_placeholder | project_specific_placeholder |
| CLAIM-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| CLAIM-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 8.2 Contribution Audiences

| Audience | What They Need from the Project | Intended Communication Product |
|---|---|---|
| Scholarly reviewers | project_specific_placeholder | project_specific_placeholder |
| DSR researchers | project_specific_placeholder | project_specific_placeholder |
| Practitioners or implementers | project_specific_placeholder | project_specific_placeholder |
| Maintainers or artifact stewards | project_specific_placeholder | project_specific_placeholder |
| Public or policy audience, if applicable | project_specific_placeholder | project_specific_placeholder |

### 8.3 Overclaiming Controls

- **Claims that should remain local unless more evidence is gathered:** project_specific_placeholder
- **Claims that may become projectable with boundary conditions:** project_specific_placeholder
- **Claims that should not be made in this project:** project_specific_placeholder
- **Evidence that would be required for stronger claims:** project_specific_placeholder

---

## 9. Transparency Plan

| Transparency Dimension | Charter-Level Commitment | Planned Evidence or File | Current Status |
|---|---|---|---|
| Process transparency | project_specific_placeholder: How will decisions, iterations, and deviations be recorded? | project_specific_placeholder | not_started / active / mapped / deferred |
| Problem-space transparency | project_specific_placeholder: How will context, stakeholders, scope, and boundaries be recorded? | project_specific_placeholder | project_specific_placeholder |
| Solution-space transparency | project_specific_placeholder: How will knowledge grounding, alternatives, and prior artifacts be recorded? | project_specific_placeholder | project_specific_placeholder |
| Build transparency | project_specific_placeholder: How will artifact construction, versions, and rationale be recorded? | project_specific_placeholder | project_specific_placeholder |
| Evaluation transparency | project_specific_placeholder: How will criteria, methods, findings, and limitations be recorded? | project_specific_placeholder | project_specific_placeholder |
| Contribution transparency | project_specific_placeholder: How will practical and scholarly claims be documented and bounded? | project_specific_placeholder | project_specific_placeholder |

### 9.1 Evidence and Record Retention

| Evidence or Record | Purpose | Expected Location | Retention Rule | Owner |
|---|---|---|---|---|
| Project charter | Initiate and classify DSR project | `templates/dsr-project-charter-template.md` or project-specific record | Retain while project is active and archive with release package. | project_specific_placeholder |
| Problem and objectives record | Preserve problem-space and success criteria | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Solution-space record | Preserve grounding and alternatives | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Design rationale | Preserve design choices and tradeoffs | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Build transparency record | Preserve artifact construction evidence | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Demonstration record | Preserve demonstration scenario and limits | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Evaluation plan and report | Preserve evaluation design and findings | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Contribution claim | Preserve claim scope and evidence basis | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Review and release records | Preserve gate decisions and release status | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 10. Risks, Constraints, and Responsible Design

### 10.1 Risk Register

| Risk ID | Risk Description | Risk Type | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| RISK-001 | project_specific_placeholder | technical / evidence / validity / stakeholder / ethical / schedule / maintenance / publication | low / medium / high | low / medium / high | project_specific_placeholder | project_specific_placeholder | open |
| RISK-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| RISK-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 10.2 Responsible Design Considerations

| Consideration | Charter-Level Assessment | Action Needed |
|---|---|---|
| Stakeholder inclusion | project_specific_placeholder | project_specific_placeholder |
| Accessibility and usability | project_specific_placeholder | project_specific_placeholder |
| Privacy, confidentiality, or security | project_specific_placeholder | project_specific_placeholder |
| Equity or unintended harms | project_specific_placeholder | project_specific_placeholder |
| Maintenance burden | project_specific_placeholder | project_specific_placeholder |
| Transparency burden or overload | project_specific_placeholder | project_specific_placeholder |
| Intellectual property or licensing | project_specific_placeholder | project_specific_placeholder |

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
| ASM-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| ASM-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| ASM-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 12.2 Limitations

| Limitation ID | Limitation | Consequence | Mitigation or Disclosure Plan |
|---|---|---|---|
| LIM-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| LIM-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| LIM-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 12.3 Open Questions

| Question ID | Open Question | Responsible Role | Needed Input | Target Disposition |
|---|---|---|---|---|
| OQ-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | resolve / defer / record_as_limitation |
| OQ-002 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| OQ-003 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 13. Charter Approval and Disposition

| Role | Name or Role Holder | Decision | Date | Notes |
|---|---|---|---|---|
| DSR project lead | project_specific_placeholder | approve / request_revision / reject / defer | project_specific_placeholder | project_specific_placeholder |
| Artifact steward | project_specific_placeholder | approve / request_revision / reject / defer | project_specific_placeholder | project_specific_placeholder |
| Reviewer | project_specific_placeholder | approve / request_revision / reject / defer | project_specific_placeholder | project_specific_placeholder |
| Sponsor or owner, if applicable | project_specific_placeholder | approve / request_revision / reject / defer | project_specific_placeholder | project_specific_placeholder |

### 13.1 Disposition Statement

**Disposition:** project_specific_placeholder: `approved_for_problem_objectives_work`, `approved_for_solution_grounding`, `requires_revision`, `rejected_as_non_dsr`, `deferred`, or other controlled disposition.

**Rationale:** project_specific_placeholder

**Next required file or record:** project_specific_placeholder: Example: `templates/problem-and-objectives-template.md`, `templates/solution-space-record-template.yaml`, or `records/design-decisions/record-dsr-identity-decision.yaml`.

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

