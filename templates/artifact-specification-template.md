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
  evidence_status: not_yet_mapped
  change_history:
    - version: "0.1.0"
      date: "YYYY-MM-DD"
      change: Initial reusable template.
      changed_by: TODO: name_or_role
```

## How to Use This Template

Use this file to describe a DSR artifact before demonstration, evaluation, reuse, or publication. Replace all `TODO:` entries with project-specific information. Delete guidance notes only after the section has been completed or intentionally marked not applicable.

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
| Artifact name | TODO: artifact_name |
| Artifact short name or acronym | TODO: short_name |
| Artifact identifier | TODO: stable_artifact_id |
| Specification identifier | TODO: artifact_specification_id |
| Specification version | TODO: semantic_version |
| Specification status | draft |
| Responsible author or role | TODO: owner_or_responsible_role |
| Date created | TODO: YYYY-MM-DD |
| Last updated | TODO: YYYY-MM-DD |
| Repository path or location | TODO: path_or_url |
| Related project | TODO: project_id_or_title |
| Intended conformance level | l2_reviewable |

### 1.1 Plain-Language Summary

TODO: In 3-6 sentences, explain what the artifact is, who it is for, what problem it addresses, and what kind of DSR contribution it is expected to support.

### 1.2 Technical Summary

TODO: Provide a concise technical description of the artifact, including its artifact type, structure, operating logic, dependencies, and expected use context.

---

## 2. Artifact Type and Ontological Position

### 2.1 Artifact Classification

| Classification dimension | Selected value | Rationale |
|---|---|---|
| Primary artifact type | TODO: construct / model / method / framework / taxonomy / ontology / instantiation / software / dataset / protocol / other | TODO |
| Secondary artifact types | TODO | TODO |
| Artifact materiality | TODO: conceptual_only / textual_or_documentary / software / data / physical / socio_technical / mixed | TODO |
| Abstraction level | TODO: highly_abstract / moderately_abstract / implementation_specific / mixed | TODO |
| Scope of artifact claim | TODO: local_case / projectable_problem_class / general_method / other | TODO |
| Artifact instance status | TODO: no_instance_yet / prototype / pilot_instance / deployed_instance / archived_instance | TODO |

### 2.2 Artifact Universal Versus Instance

Use this section to clarify whether the DSR contribution is the reusable artifact design, one specific implementation, or both.

| Question | Response |
|---|---|
| What is the reusable artifact universal, type, or design? | TODO |
| What specific instances, prototypes, or deployments exist? | TODO |
| Which claims apply to the reusable artifact type? | TODO |
| Which claims apply only to one instance or implementation context? | TODO |
| What evidence supports moving from instance-level observation to reusable design knowledge? | TODO |

### 2.3 Artifact Boundary Statement

TODO: State what is inside the artifact boundary and what is outside it. Include conceptual, technical, organizational, data, user, and evaluation boundaries as relevant.

**Inside the artifact boundary:**

- TODO: included component, rule, model, procedure, code module, dataset, role, interface, or documentation item.

**Outside the artifact boundary:**

- TODO: excluded system, external service, implementation dependency, organizational process, policy environment, or context factor.

**Boundary rationale:**

TODO: Explain why the boundary is drawn this way and how the boundary affects evaluation, reuse, maintenance, or contribution claims.

---

## 3. Problem, Context, and Intended Users

### 3.1 Problem Context

| Field | Entry |
|---|---|
| Problem class | TODO |
| Local problem instance | TODO |
| Current unsatisfactory state | TODO |
| Stakeholders affected | TODO |
| Context constraints | TODO |
| Opportunity or design gap | TODO |

### 3.2 Intended Users and Roles

| User or role | Relationship to artifact | Use context | Required knowledge or access | Success concern |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

### 3.3 Use Environment

| Environment dimension | Description | Boundary or constraint |
|---|---|---|
| Organizational setting | TODO | TODO |
| Technical infrastructure | TODO | TODO |
| Data environment | TODO | TODO |
| Governance or policy context | TODO | TODO |
| Social or cultural context | TODO | TODO |
| Resource constraints | TODO | TODO |

---

## 4. Artifact Purpose, Objectives, and Requirements

### 4.1 Purpose Statement

TODO: State the artifact purpose in a single paragraph. A strong purpose statement names the problem, the intended transformation, the primary users, and the expected DSR knowledge contribution.

### 4.2 Objectives

| Objective ID | Objective | Objective type | Stakeholder or source | Success criterion |
|---|---|---|---|---|
| OBJ-001 | TODO | functional / quality / usability / evaluation / transparency / governance / ethical | TODO | TODO |

### 4.3 Requirements

| Requirement ID | Requirement statement | Requirement type | Priority | Verification method | Trace to objective |
|---|---|---|---|---|---|
| REQ-001 | TODO | functional / nonfunctional / data / interface / evidence / documentation / ethical | must / should / may | TODO | OBJ-001 |

### 4.4 Non-Goals

| Non-goal ID | Non-goal statement | Rationale | Risk if misunderstood |
|---|---|---|---|
| NG-001 | TODO | TODO | TODO |

---

## 5. Artifact Components and Structure

### 5.1 Component Inventory

| Component ID | Component name | Component type | Function | Required? | Owner or maintainer | Version |
|---|---|---|---|---|---|---|
| CMP-001 | TODO | construct / model / method / module / interface / data / document / procedure / rule / service | TODO | yes / no | TODO | TODO |

### 5.2 Component Descriptions

#### CMP-001: TODO: Component Name

- **Purpose:** TODO
- **Inputs:** TODO
- **Outputs:** TODO
- **Internal logic:** TODO
- **Dependencies:** TODO
- **Failure modes:** TODO
- **Validation evidence:** TODO
- **Boundary notes:** TODO

### 5.3 Structural or Architectural View

TODO: Provide a concise structural description. Include a diagram, table, pseudocode, UML/PlantUML reference, schema reference, repository tree, or component map as appropriate.

```text
TODO: Insert architecture sketch, component tree, PlantUML source, or repository layout.
```

### 5.4 Interfaces and Integration Points

| Interface ID | Interface name | Connects | Data or interaction exchanged | Constraint | Evidence needed |
|---|---|---|---|---|---|
| INT-001 | TODO | TODO | TODO | TODO | TODO |

---

## 6. Make Plan: Build and Configuration Logic

The make plan explains how the artifact is created, assembled, configured, or instantiated.

### 6.1 Build Inputs

| Input ID | Input name | Input type | Source | Required quality | Traceability |
|---|---|---|---|---|---|
| IN-001 | TODO | requirement / theory / dataset / code / component / stakeholder input / design decision | TODO | TODO | TODO |

### 6.2 Build Procedure

| Step ID | Build step | Actor or role | Input | Action | Output | Evidence retained |
|---|---|---|---|---|---|---|
| MAKE-001 | TODO | TODO | TODO | TODO | TODO | TODO |

### 6.3 Design Decisions and Rationale

| Decision ID | Decision | Alternatives considered | Rationale | Tradeoff | Related requirement | Evidence status |
|---|---|---|---|---|---|---|
| DDR-001 | TODO | TODO | TODO | TODO | REQ-001 | not_yet_mapped |

### 6.4 Capacity Specification

| Capacity ID | Capacity or capability | Artifact component | Make condition | Test or inspection method | Expected result |
|---|---|---|---|---|---|
| CAP-001 | TODO | CMP-001 | TODO | TODO | TODO |

### 6.5 Build Constraints and Assumptions

| ID | Constraint or assumption | Impact | Mitigation or review action |
|---|---|---|---|
| ASM-001 | TODO | TODO | TODO |

---

## 7. Use Plan: Use Logic and Expected Effects

The use plan explains how intended users apply the artifact under specified use conditions to produce intended effects.

### 7.1 Use Case Summary

| Use Case ID | Use case | User or role | Trigger | Preconditions | Intended effect |
|---|---|---|---|---|---|
| UC-001 | TODO | TODO | TODO | TODO | TODO |

### 7.2 Use Procedure

| Step ID | Use step | Actor | Artifact component used | Action | Output or effect | Evidence captured |
|---|---|---|---|---|---|---|
| USE-001 | TODO | TODO | CMP-001 | TODO | TODO | TODO |

### 7.3 Use Conditions

| Condition ID | Condition | Required for | Risk if absent | Boundary note |
|---|---|---|---|---|
| COND-001 | TODO | TODO | TODO | TODO |

### 7.4 Effects and Attribution

Distinguish direct use effects from broader usage effects that depend on people, practice, organization, or environment.

| Effect ID | Effect type | Description | Attribution basis | Evidence required | Boundary condition |
|---|---|---|---|---|---|
| EFF-001 | use_effect | TODO | Artifact-mediated effect expected when use plan is followed. | TODO | TODO |
| EFF-002 | usage_effect | TODO | Broader practice effect influenced by artifact plus context. | TODO | TODO |

---

## 8. Artifact Network and Dependencies

### 8.1 Artifact Network Position

TODO: Describe how this artifact is embedded in a broader artifact network: adjacent tools, methods, data sources, institutional procedures, standards, repositories, users, or infrastructures.

### 8.2 Dependency Inventory

| Dependency ID | Dependency | Dependency type | Required? | Version or source | Risk | Mitigation |
|---|---|---|---|---|---|---|
| DEP-001 | TODO | theory / method / software / dataset / policy / standard / repository / human role / infrastructure | yes / no | TODO | TODO | TODO |

### 8.3 Compatibility and Interoperability

| Compatibility concern | Current status | Evidence | Required action |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

---

## 9. Version, Lifecycle, and Maintenance

### 9.1 Version Record

| Version | Date | Status | Summary of change | Compatibility impact | Evidence |
|---|---|---|---|---|---|
| 0.1.0 | TODO: YYYY-MM-DD | draft | Initial specification. | Not yet established. | TODO |

### 9.2 Lifecycle State

| Lifecycle dimension | Current state | Notes |
|---|---|---|
| Concept maturity | TODO: idea / draft / prototype / pilot / evaluated / released / archived | TODO |
| Build maturity | TODO | TODO |
| Use maturity | TODO | TODO |
| Evaluation maturity | TODO | TODO |
| Maintenance status | TODO | TODO |
| Reuse readiness | TODO | TODO |

### 9.3 Maintenance Plan

| Maintenance item | Frequency or trigger | Responsible role | Evidence retained |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

### 9.4 Deprecation or Retirement Conditions

TODO: State when the artifact, a component, or an instance should be superseded, deprecated, archived, or retired.

---

## 10. Demonstration and Evaluation Traceability

### 10.1 Demonstration Plan or Evidence

Demonstration shows that the artifact can be used in an illustrative or relevant context. It is not the same as evaluation unless evaluation criteria and evidence are explicitly applied.

| Demonstration ID | Context | User or actor | Task | Artifact version | Output | Evidence location |
|---|---|---|---|---|---|---|
| DEMO-001 | TODO | TODO | TODO | TODO | TODO | TODO |

### 10.2 Evaluation Plan or Evidence

Evaluation judges artifact utility, quality, or contribution claims against criteria.

| Evaluation ID | Claim evaluated | Evaluation method | Criterion | Metric or indicator | Data source | Status |
|---|---|---|---|---|---|---|
| EVAL-001 | TODO | TODO | TODO | TODO | TODO | planned / complete / not_applicable |

### 10.3 Claim-to-Evidence Traceability

| Claim ID | Claim | Claim type | Evidence required | Evidence status | Related artifact component | Related evaluation |
|---|---|---|---|---|---|---|
| CLM-001 | TODO | utility / quality / contribution / reuse / validity / reliability / projectability | TODO | not_yet_mapped | CMP-001 | EVAL-001 |

---

## 11. Contribution and Knowledge Positioning

### 11.1 Contribution Summary

| Contribution dimension | Statement | Evidence status |
|---|---|---|
| Contribution to practice | TODO | not_yet_mapped |
| Contribution to DSR methodology | TODO | not_yet_mapped |
| Contribution to artifact ontology or artifact design knowledge | TODO | not_yet_mapped |
| Contribution to evaluation knowledge | TODO | not_yet_mapped |
| Contribution to reporting, transparency, or reuse | TODO | not_yet_mapped |

### 11.2 Knowledge Goal and Scope

| Dimension | Selected value | Rationale |
|---|---|---|
| Primary knowledge goal | TODO: definitional / descriptive / explanatory / predictive / explanatory_predictive / prescriptive / evaluative / methodological | TODO |
| Knowledge scope | TODO: idiographic / nomothetic / analytical_generalization / projectable_to_problem_class / mixed | TODO |
| Contribution type | TODO: improvement / exaptation / invention / method_extension / theory_building / evaluation_extension / other | TODO |

### 11.3 Reuse and Projectability

| Reuse condition | Description | Evidence needed |
|---|---|---|
| Problem-class fit | TODO | TODO |
| Context fit | TODO | TODO |
| Technical fit | TODO | TODO |
| User-capability fit | TODO | TODO |
| Adaptation requirements | TODO | TODO |

---

## 12. Transparency, Responsible Design, and Risk

### 12.1 DSR Transparency Mapping

| Transparency dimension | How this specification addresses it | Remaining gap |
|---|---|---|
| Process transparency | TODO | TODO |
| Problem-space transparency | TODO | TODO |
| Solution-space transparency | TODO | TODO |
| Build transparency | TODO | TODO |
| Evaluation transparency | TODO | TODO |
| Contribution transparency | TODO | TODO |

### 12.2 Responsible Design Review

| Value or concern | Relevance | Risk | Mitigation | Evidence |
|---|---|---|---|---|
| Privacy | TODO | TODO | TODO | TODO |
| Security | TODO | TODO | TODO | TODO |
| Accessibility | TODO | TODO | TODO | TODO |
| Equity or stakeholder fairness | TODO | TODO | TODO | TODO |
| Sustainability or maintenance burden | TODO | TODO | TODO | TODO |
| Intellectual property or proprietary constraints | TODO | TODO | TODO | TODO |

### 12.3 Failure Modes

| Failure Mode ID | Failure mode | Cause | Consequence | Detection method | Mitigation |
|---|---|---|---|---|---|
| FM-001 | TODO | TODO | TODO | TODO | TODO |

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
| Consistency | TODO: pass / partial / fail | TODO |
| Coherence | TODO: pass / partial / fail | TODO |
| Cogency | TODO: pass / partial / fail | TODO |
| Correspondence | TODO: pass / partial / fail | TODO |
| DSR transparency | TODO: pass / partial / fail | TODO |
| Reviewability | TODO: pass / partial / fail | TODO |

---

## 14. Limitations, Assumptions, and Open Questions

### 14.1 Limitations

| Limitation ID | Limitation | Impact on artifact claim | Mitigation or next step |
|---|---|---|---|
| LIM-001 | TODO | TODO | TODO |

### 14.2 Assumptions

| Assumption ID | Assumption | Basis | Review trigger |
|---|---|---|---|
| ASM-001 | TODO | TODO | TODO |

### 14.3 Open Questions

| Question ID | Open question | Decision needed | Responsible role | Target date |
|---|---|---|---|---|
| OQ-001 | TODO | TODO | TODO | TODO |

---

## 15. Source Basis and Traceability

### 15.1 Source Basis

| Source ID | Source type | Use in this specification | Evidence status |
|---|---|---|---|
| dsr_framework_generation_spec | protocol specification | Governs file conventions, metadata, quality gates, and conformance target. | mapped |
| dsr_framework_generation_prompt | generation procedure | Governs template usability, traceability, and completion reporting. | mapped |
| weigand_johannesson_andersson_2021_artifact_ontology_for_dsr | DSR corpus source | Supports artifact universal, make plan, use plan, capacity, artifact network, and use-effect distinctions. | mapped |
| hevner_et_al_2024_transparency_in_design_science_research | DSR corpus source | Supports process, problem-space, solution-space, build, evaluation, and contribution transparency mapping. | mapped |
| TODO: project_specific_source | TODO | TODO | not_yet_mapped |

### 15.2 Trace Links

| Trace ID | From | To | Relationship | Evidence status |
|---|---|---|---|---|
| TR-001 | OBJ-001 | REQ-001 | objective_to_requirement | not_yet_mapped |
| TR-002 | REQ-001 | CMP-001 | requirement_to_component | not_yet_mapped |
| TR-003 | CMP-001 | CAP-001 | component_to_capacity | not_yet_mapped |
| TR-004 | CAP-001 | EVAL-001 | capacity_to_evaluation | not_yet_mapped |
| TR-005 | CLM-001 | EVAL-001 | claim_to_evidence | not_yet_mapped |

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
    - Project-specific evidence will be supplied by the artifact author and should be marked TODO until available.
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
