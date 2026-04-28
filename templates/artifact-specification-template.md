<!-- SPDX-License-Identifier: CC0-1.0 -->

# DSR Artifact Specification Template

```yaml
template_metadata:
  template_id: template_artifact_specification
  template_path: templates/artifact-specification-template.md
  title: DSR Artifact Specification Template
  item_type: specification_template
  output_format: markdown
  status: draft
  version: "0.1.0"
  conformance_target: l2_reviewable
  owner_role: artifact_author
  purpose: >
    Provide a reusable Markdown template for specifying a Design Science Research
    artifact, including its components, make logic, use logic, boundary, version,
    artifact-network dependencies, evaluation traceability, and contribution claims.
  source_basis:
    - dsr_framework_generation_spec
    - dsr_framework_generation_prompt
    - artifact_ontology
    - dsr_corpus:weigand_johannesson_andersson_2021_artifact_ontology_for_dsr
    - dsr_corpus:hevner_et_al_2024_transparency_in_design_science_research
  related_items:
    upstream_dependencies:
      - models/dsr-artifact-ontology.yaml
      - vocabularies/artifact-types.yaml
      - schemas/dsr-artifact.schema.json
      - templates/design-rationale-template.md
      - templates/build-transparency-record-template.yaml
    downstream_uses:
      - artifact-profile.yaml
      - records/dsr-transparency/record-dsr-transparency-crosswalk-0001.yaml
      - records/evaluations/record-evaluation-plan-0001.yaml
      - docs/protocol/05-artifact-ontology.md
  evidence_status: accepted_v1_limitation
  change_history:
    - version: "0.1.0"
      date: "YYYY-MM-DD"
      change: Initial reusable template.
      changed_by: project_specific_placeholder: name_or_role
```

## How to Use This Template

Use this file to describe a DSR artifact before demonstration, evaluation, reuse, or publication. Replace all `project_specific_placeholder:` entries with project-specific information. Delete guidance notes only after the section has been completed or intentionally marked not applicable.

The specification should distinguish:

- the artifact as a reusable type, design, or artifact universal;
- any artifact instance, implementation, prototype, or deployment;
- the make plan used to create or configure the artifact;
- the use plan that explains how the artifact is applied to produce intended effects;
- capacities, constraints, and boundary conditions;
- artifact utility, artifact quality, and contribution to knowledge;
- demonstration evidence versus evaluation evidence.

---

## 1. Artifact Identity

| Field | Entry |
|---|---|
| Artifact name | project_specific_placeholder: artifact_name |
| Artifact short name or acronym | project_specific_placeholder: short_name |
| Artifact identifier | project_specific_placeholder: stable_artifact_id |
| Specification identifier | project_specific_placeholder: artifact_specification_id |
| Specification version | project_specific_placeholder: semantic_version |
| Specification status | draft |
| Responsible author or role | project_specific_placeholder: owner_or_responsible_role |
| Date created | project_specific_placeholder: YYYY-MM-DD |
| Last updated | project_specific_placeholder: YYYY-MM-DD |
| Repository path or location | project_specific_placeholder: path_or_url |
| Related project | project_specific_placeholder: project_id_or_title |
| Intended conformance level | l2_reviewable |

### 1.1 Plain-Language Summary

project_specific_placeholder: In 3-6 sentences, explain what the artifact is, who it is for, what problem it addresses, and what kind of DSR contribution it is expected to support.

### 1.2 Technical Summary

project_specific_placeholder: Provide a concise technical description of the artifact, including its artifact type, structure, operating logic, dependencies, and expected use context.

---

## 2. Artifact Type and Ontological Position

### 2.1 Artifact Classification

| Classification dimension | Selected value | Rationale |
|---|---|---|
| Primary artifact type | project_specific_placeholder: construct / model / method / framework / taxonomy / ontology / instantiation / software / dataset / protocol / other | project_specific_placeholder |
| Secondary artifact types | project_specific_placeholder | project_specific_placeholder |
| Artifact materiality | project_specific_placeholder: conceptual_only / textual_or_documentary / software / data / physical / socio_technical / mixed | project_specific_placeholder |
| Abstraction level | project_specific_placeholder: highly_abstract / moderately_abstract / implementation_specific / mixed | project_specific_placeholder |
| Scope of artifact claim | project_specific_placeholder: local_case / projectable_problem_class / general_method / other | project_specific_placeholder |
| Artifact instance status | project_specific_placeholder: no_instance_yet / prototype / pilot_instance / deployed_instance / archived_instance | project_specific_placeholder |

### 2.2 Artifact Universal Versus Instance

Use this section to clarify whether the DSR contribution is the reusable artifact design, one specific implementation, or both.

| Question | Response |
|---|---|
| What is the reusable artifact universal, type, or design? | project_specific_placeholder |
| What specific instances, prototypes, or deployments exist? | project_specific_placeholder |
| Which claims apply to the reusable artifact type? | project_specific_placeholder |
| Which claims apply only to one instance or implementation context? | project_specific_placeholder |
| What evidence supports moving from instance-level observation to reusable design knowledge? | project_specific_placeholder |

### 2.3 Artifact Boundary Statement

project_specific_placeholder: State what is inside the artifact boundary and what is outside it. Include conceptual, technical, organizational, data, user, and evaluation boundaries as relevant.

**Inside the artifact boundary:**

- project_specific_placeholder: included component, rule, model, procedure, code module, dataset, role, interface, or documentation item.

**Outside the artifact boundary:**

- project_specific_placeholder: excluded system, external service, implementation dependency, organizational process, policy environment, or context factor.

**Boundary rationale:**

project_specific_placeholder: Explain why the boundary is drawn this way and how the boundary affects evaluation, reuse, maintenance, or contribution claims.

---

## 3. Problem, Context, and Intended Users

### 3.1 Problem Context

| Field | Entry |
|---|---|
| Problem class | project_specific_placeholder |
| Local problem instance | project_specific_placeholder |
| Current unsatisfactory state | project_specific_placeholder |
| Stakeholders affected | project_specific_placeholder |
| Context constraints | project_specific_placeholder |
| Opportunity or design gap | project_specific_placeholder |

### 3.2 Intended Users and Roles

| User or role | Relationship to artifact | Use context | Required knowledge or access | Success concern |
|---|---|---|---|---|
| project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 3.3 Use Environment

| Environment dimension | Description | Boundary or constraint |
|---|---|---|
| Organizational setting | project_specific_placeholder | project_specific_placeholder |
| Technical infrastructure | project_specific_placeholder | project_specific_placeholder |
| Data environment | project_specific_placeholder | project_specific_placeholder |
| Governance or policy context | project_specific_placeholder | project_specific_placeholder |
| Social or cultural context | project_specific_placeholder | project_specific_placeholder |
| Resource constraints | project_specific_placeholder | project_specific_placeholder |

---

## 4. Artifact Purpose, Objectives, and Requirements

### 4.1 Purpose Statement

project_specific_placeholder: State the artifact purpose in a single paragraph. A strong purpose statement names the problem, the intended transformation, the primary users, and the expected DSR knowledge contribution.

### 4.2 Objectives

| Objective ID | Objective | Objective type | Stakeholder or source | Success criterion |
|---|---|---|---|---|
| OBJ-001 | project_specific_placeholder | functional / quality / usability / evaluation / transparency / governance / ethical | project_specific_placeholder | project_specific_placeholder |

### 4.3 Requirements

| Requirement ID | Requirement statement | Requirement type | Priority | Verification method | Trace to objective |
|---|---|---|---|---|---|
| REQ-001 | project_specific_placeholder | functional / nonfunctional / data / interface / evidence / documentation / ethical | must / should / may | project_specific_placeholder | OBJ-001 |

### 4.4 Non-Goals

| Non-goal ID | Non-goal statement | Rationale | Risk if misunderstood |
|---|---|---|---|
| NG-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 5. Artifact Components and Structure

### 5.1 Component Inventory

| Component ID | Component name | Component type | Function | Required? | Owner or maintainer | Version |
|---|---|---|---|---|---|---|
| CMP-001 | project_specific_placeholder | construct / model / method / module / interface / data / document / procedure / rule / service | project_specific_placeholder | yes / no | project_specific_placeholder | project_specific_placeholder |

### 5.2 Component Descriptions

#### CMP-001: project_specific_placeholder: Component Name

- **Purpose:** project_specific_placeholder
- **Inputs:** project_specific_placeholder
- **Outputs:** project_specific_placeholder
- **Internal logic:** project_specific_placeholder
- **Dependencies:** project_specific_placeholder
- **Failure modes:** project_specific_placeholder
- **Validation evidence:** project_specific_placeholder
- **Boundary notes:** project_specific_placeholder

### 5.3 Structural or Architectural View

project_specific_placeholder: Provide a concise structural description. Include a diagram, table, pseudocode, UML/PlantUML reference, schema reference, repository tree, or component map as appropriate.

```text
project_specific_placeholder: Insert architecture sketch, component tree, PlantUML source, or repository layout.
```

### 5.4 Interfaces and Integration Points

| Interface ID | Interface name | Connects | Data or interaction exchanged | Constraint | Evidence needed |
|---|---|---|---|---|---|
| INT-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 6. Make Plan: Build and Configuration Logic

The make plan explains how the artifact is created, assembled, configured, or instantiated.

### 6.1 Build Inputs

| Input ID | Input name | Input type | Source | Required quality | Traceability |
|---|---|---|---|---|---|
| IN-001 | project_specific_placeholder | requirement / theory / dataset / code / component / stakeholder input / design decision | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 6.2 Build Procedure

| Step ID | Build step | Actor or role | Input | Action | Output | Evidence retained |
|---|---|---|---|---|---|---|
| MAKE-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 6.3 Design Decisions and Rationale

| Decision ID | Decision | Alternatives considered | Rationale | Tradeoff | Related requirement | Evidence status |
|---|---|---|---|---|---|---|
| DDR-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | REQ-001 | accepted_v1_limitation |

### 6.4 Capacity Specification

| Capacity ID | Capacity or capability | Artifact component | Make condition | Test or inspection method | Expected result |
|---|---|---|---|---|---|
| CAP-001 | project_specific_placeholder | CMP-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 6.5 Build Constraints and Assumptions

| ID | Constraint or assumption | Impact | Mitigation or review action |
|---|---|---|---|
| ASM-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 7. Use Plan: Use Logic and Expected Effects

The use plan explains how intended users apply the artifact under specified use conditions to produce intended effects.

### 7.1 Use Case Summary

| Use Case ID | Use case | User or role | Trigger | Preconditions | Intended effect |
|---|---|---|---|---|---|
| UC-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 7.2 Use Procedure

| Step ID | Use step | Actor | Artifact component used | Action | Output or effect | Evidence captured |
|---|---|---|---|---|---|---|
| USE-001 | project_specific_placeholder | project_specific_placeholder | CMP-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 7.3 Use Conditions

| Condition ID | Condition | Required for | Risk if absent | Boundary note |
|---|---|---|---|---|
| COND-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 7.4 Effects and Attribution

Distinguish direct use effects from broader usage effects that depend on people, practice, organization, or environment.

| Effect ID | Effect type | Description | Attribution basis | Evidence required | Boundary condition |
|---|---|---|---|---|---|
| EFF-001 | use_effect | project_specific_placeholder | Artifact-mediated effect expected when use plan is followed. | project_specific_placeholder | project_specific_placeholder |
| EFF-002 | usage_effect | project_specific_placeholder | Broader practice effect influenced by artifact plus context. | project_specific_placeholder | project_specific_placeholder |

---

## 8. Artifact Network and Dependencies

### 8.1 Artifact Network Position

project_specific_placeholder: Describe how this artifact is embedded in a broader artifact network: adjacent tools, methods, data sources, institutional procedures, standards, repositories, users, or infrastructures.

### 8.2 Dependency Inventory

| Dependency ID | Dependency | Dependency type | Required? | Version or source | Risk | Mitigation |
|---|---|---|---|---|---|---|
| DEP-001 | project_specific_placeholder | theory / method / software / dataset / policy / standard / repository / human role / infrastructure | yes / no | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 8.3 Compatibility and Interoperability

| Compatibility concern | Current status | Evidence | Required action |
|---|---|---|---|
| project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 9. Version, Lifecycle, and Maintenance

### 9.1 Version Record

| Version | Date | Status | Summary of change | Compatibility impact | Evidence |
|---|---|---|---|---|---|
| 0.1.0 | project_specific_placeholder: YYYY-MM-DD | draft | Initial specification. | Not yet established. | project_specific_placeholder |

### 9.2 Lifecycle State

| Lifecycle dimension | Current state | Notes |
|---|---|---|
| Concept maturity | project_specific_placeholder: idea / draft / prototype / pilot / evaluated / released / archived | project_specific_placeholder |
| Build maturity | project_specific_placeholder | project_specific_placeholder |
| Use maturity | project_specific_placeholder | project_specific_placeholder |
| Evaluation maturity | project_specific_placeholder | project_specific_placeholder |
| Maintenance status | project_specific_placeholder | project_specific_placeholder |
| Reuse readiness | project_specific_placeholder | project_specific_placeholder |

### 9.3 Maintenance Plan

| Maintenance item | Frequency or trigger | Responsible role | Evidence retained |
|---|---|---|---|
| project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 9.4 Deprecation or Retirement Conditions

project_specific_placeholder: State when the artifact, a component, or an instance should be superseded, deprecated, archived, or retired.

---

## 10. Demonstration and Evaluation Traceability

### 10.1 Demonstration Plan or Evidence

Demonstration shows that the artifact can be used in an illustrative or relevant context. It is not the same as evaluation unless evaluation criteria and evidence are explicitly applied.

| Demonstration ID | Context | User or actor | Task | Artifact version | Output | Evidence location |
|---|---|---|---|---|---|---|
| DEMO-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 10.2 Evaluation Plan or Evidence

Evaluation judges artifact utility, quality, or contribution claims against criteria.

| Evaluation ID | Claim evaluated | Evaluation method | Criterion | Metric or indicator | Data source | Status |
|---|---|---|---|---|---|---|
| EVAL-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | planned / complete / not_applicable |

### 10.3 Claim-to-Evidence Traceability

| Claim ID | Claim | Claim type | Evidence required | Evidence status | Related artifact component | Related evaluation |
|---|---|---|---|---|---|---|
| CLM-001 | project_specific_placeholder | utility / quality / contribution / reuse / validity / reliability / projectability | project_specific_placeholder | accepted_v1_limitation | CMP-001 | EVAL-001 |

---

## 11. Contribution and Knowledge Positioning

### 11.1 Contribution Summary

| Contribution dimension | Statement | Evidence status |
|---|---|---|
| Contribution to practice | project_specific_placeholder | accepted_v1_limitation |
| Contribution to DSR methodology | project_specific_placeholder | accepted_v1_limitation |
| Contribution to artifact ontology or artifact design knowledge | project_specific_placeholder | accepted_v1_limitation |
| Contribution to evaluation knowledge | project_specific_placeholder | accepted_v1_limitation |
| Contribution to reporting, transparency, or reuse | project_specific_placeholder | accepted_v1_limitation |

### 11.2 Knowledge Goal and Scope

| Dimension | Selected value | Rationale |
|---|---|---|
| Primary knowledge goal | project_specific_placeholder: definitional / descriptive / explanatory / predictive / explanatory_predictive / prescriptive / evaluative / methodological | project_specific_placeholder |
| Knowledge scope | project_specific_placeholder: idiographic / nomothetic / analytical_generalization / projectable_to_problem_class / mixed | project_specific_placeholder |
| Contribution type | project_specific_placeholder: improvement / exaptation / invention / method_extension / theory_building / evaluation_extension / other | project_specific_placeholder |

### 11.3 Reuse and Projectability

| Reuse condition | Description | Evidence needed |
|---|---|---|
| Problem-class fit | project_specific_placeholder | project_specific_placeholder |
| Context fit | project_specific_placeholder | project_specific_placeholder |
| Technical fit | project_specific_placeholder | project_specific_placeholder |
| User-capability fit | project_specific_placeholder | project_specific_placeholder |
| Adaptation requirements | project_specific_placeholder | project_specific_placeholder |

---

## 12. Transparency, Responsible Design, and Risk

### 12.1 DSR Transparency Mapping

| Transparency dimension | How this specification addresses it | Remaining gap |
|---|---|---|
| Process transparency | project_specific_placeholder | project_specific_placeholder |
| Problem-space transparency | project_specific_placeholder | project_specific_placeholder |
| Solution-space transparency | project_specific_placeholder | project_specific_placeholder |
| Build transparency | project_specific_placeholder | project_specific_placeholder |
| Evaluation transparency | project_specific_placeholder | project_specific_placeholder |
| Contribution transparency | project_specific_placeholder | project_specific_placeholder |

### 12.2 Responsible Design Review

| Value or concern | Relevance | Risk | Mitigation | Evidence |
|---|---|---|---|---|
| Privacy | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Security | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Accessibility | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Equity or stakeholder fairness | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Sustainability or maintenance burden | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Intellectual property or proprietary constraints | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 12.3 Failure Modes

| Failure Mode ID | Failure mode | Cause | Consequence | Detection method | Mitigation |
|---|---|---|---|---|---|
| FM-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 13. Acceptance Criteria and Review Checklist

### 13.1 Acceptance Criteria

| Criterion ID | Acceptance criterion | Evidence required | Pass condition | Fail condition |
|---|---|---|---|---|
| AC-001 | Artifact identity and boundary are explicit. | Completed Sections 1-2. | Reviewer can distinguish artifact type, instance, and boundary. | Artifact is ambiguously described or conflates artifact, system, theory, and implementation. |
| AC-002 | Components and structure are specified. | Completed Section 5. | Each core component has a function, dependency, and boundary note. | Components are missing or described only narratively. |
| AC-003 | Make plan is traceable. | Completed Section 6. | Build inputs, steps, decisions, capacities, and assumptions are documented. | Build logic cannot be reconstructed. |
| AC-004 | Use plan is traceable. | Completed Section 7. | Use cases, use conditions, use steps, and effects are documented. | Artifact utility claims lack a use scenario. |
| AC-005 | Version and lifecycle are controlled. | Completed Section 9. | Current version, lifecycle state, and maintenance responsibilities are specified. | Version or maintenance state is absent. |
| AC-006 | Demonstration and evaluation are distinguished. | Completed Section 10. | Demonstration evidence is not overclaimed as evaluation evidence. | Demonstration, evaluation, and contribution claims are conflated. |
| AC-007 | Claims are traceable to evidence needs. | Completed Section 10.3. | Each major claim has evidence status and required evidence. | Claims are unsupported or unverifiable. |
| AC-008 | Transparency and risk are addressed. | Completed Section 12. | Relevant transparency dimensions and responsible design risks are reviewed. | Risks or transparency gaps are omitted without rationale. |

### 13.2 Quality Gate Status

| Quality gate | Status | Reviewer notes |
|---|---|---|
| Consistency | project_specific_placeholder: pass / partial / fail | project_specific_placeholder |
| Coherence | project_specific_placeholder: pass / partial / fail | project_specific_placeholder |
| Cogency | project_specific_placeholder: pass / partial / fail | project_specific_placeholder |
| Correspondence | project_specific_placeholder: pass / partial / fail | project_specific_placeholder |
| DSR transparency | project_specific_placeholder: pass / partial / fail | project_specific_placeholder |
| Reviewability | project_specific_placeholder: pass / partial / fail | project_specific_placeholder |

---

## 14. Limitations, Assumptions, and Open Questions

### 14.1 Limitations

| Limitation ID | Limitation | Impact on artifact claim | Mitigation or next step |
|---|---|---|---|
| LIM-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 14.2 Assumptions

| Assumption ID | Assumption | Basis | Review trigger |
|---|---|---|---|
| ASM-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 14.3 Open Questions

| Question ID | Open question | Decision needed | Responsible role | Target date |
|---|---|---|---|---|
| OQ-001 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

---

## 15. Source Basis and Traceability

### 15.1 Source Basis

| Source ID | Source type | Use in this specification | Evidence status |
|---|---|---|---|
| dsr_framework_generation_spec | protocol specification | Governs file conventions, metadata, quality gates, and conformance target. | mapped |
| dsr_framework_generation_prompt | generation procedure | Governs template usability, traceability, and completion reporting. | mapped |
| weigand_johannesson_andersson_2021_artifact_ontology_for_dsr | DSR corpus source | Supports artifact universal, make plan, use plan, capacity, artifact network, and use-effect distinctions. | mapped |
| hevner_et_al_2024_transparency_in_design_science_research | DSR corpus source | Supports process, problem-space, solution-space, build, evaluation, and contribution transparency mapping. | mapped |
| project_specific_placeholder: project_specific_source | project_specific_placeholder | project_specific_placeholder | accepted_v1_limitation |

### 15.2 Trace Links

| Trace ID | From | To | Relationship | Evidence status |
|---|---|---|---|---|
| TR-001 | OBJ-001 | REQ-001 | objective_to_requirement | accepted_v1_limitation |
| TR-002 | REQ-001 | CMP-001 | requirement_to_component | accepted_v1_limitation |
| TR-003 | CMP-001 | CAP-001 | component_to_capacity | accepted_v1_limitation |
| TR-004 | CAP-001 | EVAL-001 | capacity_to_evaluation | accepted_v1_limitation |
| TR-005 | CLM-001 | EVAL-001 | claim_to_evidence | accepted_v1_limitation |

---

## 16. Appendix: Minimal Completion Checklist

Before submitting this specification for review, verify that:

- [ ] Artifact identity, type, and boundary are explicit.
- [ ] Artifact universal/type is distinguished from instance/prototype/deployment.
- [ ] Components, interfaces, and dependencies are listed.
- [ ] Make plan and build decisions are documented.
- [ ] Use plan, use conditions, and intended effects are documented.
- [ ] Capacities and expected effects are stated as testable or reviewable claims.
- [ ] Version, lifecycle state, and maintenance plan are documented.
- [ ] Demonstration and evaluation evidence are separated.
- [ ] Utility, quality, contribution, reuse, and projectability claims are traceable.
- [ ] Transparency dimensions are mapped.
- [ ] Responsible design risks are reviewed.
- [ ] Limitations, assumptions, and open questions are documented.

---

## Completion Report Template

```yaml
completion_report:
  generated_selection_id: template_artifact_specification
  generated_path: templates/artifact-specification-template.md
  item_type: specification_template
  output_format: markdown
  conformance_target: l2_reviewable
  dependencies_used:
    - dsr-framework-generation-prompt.md
    - dsr-framework-generation-spec.yaml
    - dsr-framework-selection-table.md
    - chunked_folder_conversion_extractions_20260427030321_part001.yaml
  assumptions:
    - The template is intended as a researcher-facing Markdown specification template rather than a JSON/YAML validation schema.
    - Project-specific evidence will be supplied by the artifact author and should be marked project_specific_placeholder until available.
    - The artifact ontology dependency is operationalized through artifact universal, make plan, use plan, capacity, artifact network, and use/usage effect distinctions.
  open_questions:
    - Whether a future companion JSON Schema should validate a structured YAML version of this template.
    - Whether artifact-type enumerations should be synchronized directly with vocabularies/artifact-types.yaml once finalized.
  quality_gate_status:
    consistency: pass
    coherence: pass
    cogency: pass
    correspondence: pass
    dsr_transparency: pass
    reviewability: pass
  next_recommended_file: template_build_transparency
```
