---
template_id: template_problem_objectives
item_id: problem_and_objectives_template
item_type: template
title: Problem and Objectives Template
purpose: >
  Provide a reusable Markdown template for documenting DSR problem context,
  problem-space transparency, solution objectives, requirements, constraints,
  success criteria, and traceability from problem evidence to evaluation.
status: draft
version: "0.1.0"
owner: dsr_framework_maintainers
intended_repository_path: templates/problem-and-objectives-template.md
output_format: markdown
conformance_target: l2_reviewable
related_items:
  upstream_dependencies:
    - problem-space schema
    - DSR lifecycle model
    - DSR transparency model
    - evaluation alignment model
  downstream_items:
    - templates/solution-space-record-template.yaml
    - templates/design-rationale-template.md
    - templates/artifact-specification-template.md
    - templates/evaluation-plan-template.yaml
    - templates/contribution-claim-template.yaml
source_basis:
  - source_id: dsr_framework_generation_spec
    evidence_status: mapped
    relevance: Repository conventions, metadata expectations, quality gates, and L2 reviewability.
  - source_id: dsr_framework_generation_prompt
    evidence_status: mapped
    relevance: Selected-portion procedure, template usability, traceability, and completion-report expectations.
  - source_id: dsr_extraction_corpus
    evidence_status: partially_mapped
    relevance: DSR problem-space, objective-identification, build/evaluate, and transparency concepts.
change_history:
  - version: "0.1.0"
    date: 2026-04-27
    change: Initial draft generated for template_problem_objectives.
    responsible_party: GPT-5.5 Thinking
license: CC0-1.0
---

<!-- SPDX-License-Identifier: CC0-1.0 -->

# Problem and Objectives Template

> Use this template to document the problem context, design objectives, requirements, constraints, success criteria, and evaluation implications for a Design Science Research project. Replace all `TODO:` prompts with project-specific content. Retain sections that support reviewability, even when the answer is `not applicable`.

## 1. Document Control

| Field | Value |
|---|---|
| Project ID | TODO: stable project identifier |
| Project title | TODO: project title |
| Prepared by | TODO: name or role |
| Date prepared | TODO: YYYY-MM-DD |
| Version | TODO: 0.1.0 |
| Status | draft |
| Intended conformance level | L2 reviewable |
| Related artifact/profile | TODO: artifact-profile.yaml or artifact ID |
| Related charter | TODO: dsr-project-charter-template.md output, if available |

## 2. Purpose and Scope of This Record

### 2.1 Purpose

TODO: State why this problem-and-objectives record is being created. Include how it will support artifact design, requirements definition, evaluation planning, and contribution positioning.

Example structure:

> This record defines the focal DSR problem, the stakeholders and context affected by the problem, the design objectives derived from the problem, and the success criteria that will later be used to evaluate artifact utility, artifact quality, and contribution to design knowledge.

### 2.2 Scope

| Scope Element | Description |
|---|---|
| In scope | TODO: what this problem-and-objectives record covers |
| Out of scope | TODO: what it intentionally does not cover |
| Unit of analysis | TODO: artifact, process, organization, learner, system, role, community, etc. |
| Application context | TODO: local setting, domain, organization type, or use environment |
| Time boundary | TODO: period covered by problem evidence and expected intervention/evaluation |
| Geographic/regulatory boundary | TODO: jurisdiction, policy environment, accreditation/regulatory constraints, or N/A |

## 3. Focal Problem Statement

### 3.1 Concise Problem Statement

TODO: Write one concise statement of the focal problem.

Recommended pattern:

> In [context], [stakeholders/users] experience [problem or unsatisfactory state], because [known or hypothesized causes], resulting in [consequences], which matters because [practical, theoretical, ethical, compliance, or organizational significance].

### 3.2 Problem Classification

| Field | Selected Value or Description |
|---|---|
| Problem type | TODO: technical_problem, socio_technical_problem, methodological_problem, wicked_problem, educational_problem, compliance_problem, other |
| Problem class | TODO: broader reusable class of problems |
| Local problem instance | TODO: specific manifestation in this project context |
| Problem maturity | TODO: emergent, partially understood, well understood, contested, changing |
| Problem structure | TODO: well_structured, semi_structured, ill_structured, wicked, unknown |
| DSR relevance | TODO: why artifact creation/evaluation is appropriate rather than only explanation, policy, training, or consulting |

### 3.3 Current Unsatisfactory State

TODO: Describe the current condition that motivates the DSR project. Include observed limitations, pain points, gaps, risks, inefficiencies, errors, missing capabilities, or unmet stakeholder needs.

| Current-State Element | Evidence or Description | Source/Reference | Evidence Strength |
|---|---|---|---|
| TODO: issue 1 | TODO | TODO | TODO: low/moderate/high |
| TODO: issue 2 | TODO | TODO | TODO: low/moderate/high |
| TODO: issue 3 | TODO | TODO | TODO: low/moderate/high |

### 3.4 Consequences and Significance

| Consequence | Affected Stakeholder/System | Severity | Evidence | Notes |
|---|---|---|---|---|
| TODO | TODO | TODO: low/moderate/high/critical | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |

## 4. Problem-Space Transparency

### 4.1 Context Description

| Context Dimension | Description |
|---|---|
| Domain | TODO |
| Organizational setting | TODO |
| Technological setting | TODO |
| Social/cultural setting | TODO |
| Governance/compliance setting | TODO |
| Resource setting | TODO: budget, staffing, tools, data, access, time |
| Prior artifact/network setting | TODO: existing systems, processes, templates, policies, datasets, models, or tools |

### 4.2 Stakeholders and Needs

| Stakeholder ID | Stakeholder Role | Stakeholder Description | Problem Experience | Need or Interest | Involvement Stage |
|---|---|---|---|---|---|
| STK-001 | TODO | TODO | TODO | TODO | problem_identification |
| STK-002 | TODO | TODO | TODO | TODO | requirements |
| STK-003 | TODO | TODO | TODO | TODO | evaluation |

### 4.3 Boundary Conditions

| Boundary ID | Boundary Condition | Type | Implication for Design or Evaluation |
|---|---|---|---|
| BND-001 | TODO | TODO: contextual/technical/social/regulatory/data/resource/time | TODO |
| BND-002 | TODO | TODO | TODO |
| BND-003 | TODO | TODO | TODO |

### 4.4 Assumptions

| Assumption ID | Assumption | Rationale | Risk if False | How It Will Be Checked |
|---|---|---|---|---|
| ASM-001 | TODO | TODO | TODO | TODO |
| ASM-002 | TODO | TODO | TODO | TODO |

## 5. Evidence Basis for the Problem

### 5.1 Evidence Register

Use this section to distinguish documented evidence from inference. Do not overclaim the strength of problem evidence.

| Evidence ID | Evidence Type | Source/Reference | What It Supports | Strength | Limitations |
|---|---|---|---|---|---|
| EV-PROB-001 | TODO: literature/practice data/interview/observation/system log/document review/policy requirement | TODO | TODO | TODO: low/moderate/high | TODO |
| EV-PROB-002 | TODO | TODO | TODO | TODO | TODO |
| EV-PROB-003 | TODO | TODO | TODO | TODO | TODO |

### 5.2 Knowledge Gap or Practical Gap

TODO: Explain the gap between the current state and the desired state. Distinguish at least one of the following:

- **Practical capability gap:** TODO
- **Process or workflow gap:** TODO
- **Artifact or technology gap:** TODO
- **Knowledge or design-theory gap:** TODO
- **Evaluation or measurement gap:** TODO
- **Compliance, transparency, or governance gap:** TODO

## 6. Desired Improvement State

### 6.1 Improvement Goals

| Improvement Goal ID | Improvement Goal | Stakeholder Value | Problem Element Addressed | Priority |
|---|---|---|---|---|
| GOAL-001 | TODO | TODO | TODO | TODO: must/should/could |
| GOAL-002 | TODO | TODO | TODO | TODO |
| GOAL-003 | TODO | TODO | TODO | TODO |

### 6.2 Utility, Quality, and Knowledge Distinctions

| Distinction | Project-Specific Meaning |
|---|---|
| Artifact utility | TODO: what practical usefulness would mean in this context |
| Artifact quality | TODO: what internal/external quality attributes would mean |
| Contribution to knowledge | TODO: what reusable design knowledge, method knowledge, or theory contribution may result |
| Demonstration | TODO: how artifact use will be shown without treating demonstration as evaluation |
| Evaluation | TODO: how artifact performance, utility, quality, or contribution will be assessed |

## 7. Solution Objectives

### 7.1 Objective Register

Objectives should mediate between the problem definition and the later build/evaluate activities. Each objective should be traceable to evidence, stakeholder needs, and evaluation criteria.

| Objective ID | Objective Statement | Objective Type | Derives From | Priority | Evaluation Implication |
|---|---|---|---|---|---|
| OBJ-001 | TODO: The artifact shall... / The project shall... | TODO: functional_requirement | TODO: problem/evidence/stakeholder IDs | must | TODO |
| OBJ-002 | TODO | TODO: nonfunctional_requirement | TODO | should | TODO |
| OBJ-003 | TODO | TODO: quality_attribute | TODO | must | TODO |
| OBJ-004 | TODO | TODO: evaluation_requirement | TODO | must | TODO |
| OBJ-005 | TODO | TODO: ethical_or_normative_requirement | TODO | should | TODO |
| OBJ-006 | TODO | TODO: contribution_objective | TODO | could | TODO |

Allowed objective types:

- `functional_requirement`: capability or behavior the artifact must provide.
- `nonfunctional_requirement`: performance, accessibility, security, usability, maintainability, or operational constraint.
- `quality_attribute`: desired property of the artifact, method, model, dataset, or design knowledge.
- `evaluation_requirement`: objective that defines what must be evaluated and how confidence will be established.
- `ethical_or_normative_requirement`: objective tied to responsible design, privacy, fairness, safety, accessibility, compliance, or stakeholder protection.
- `constraint`: condition that limits the solution space.
- `contribution_objective`: objective tied to reusable DSR knowledge, publication, projectability, or methodological contribution.

### 7.2 Objective Rationale

| Objective ID | Rationale | Alternative Considered | Why This Objective Is Appropriate |
|---|---|---|---|
| OBJ-001 | TODO | TODO | TODO |
| OBJ-002 | TODO | TODO | TODO |
| OBJ-003 | TODO | TODO | TODO |

### 7.3 Objective Completeness Check

| Check | Response |
|---|---|
| Do objectives cover the focal problem statement? | TODO: yes/no/partial + explanation |
| Do objectives address all must-have stakeholder needs? | TODO |
| Do objectives distinguish utility, quality, and contribution? | TODO |
| Do objectives avoid prescribing a premature solution? | TODO |
| Do objectives provide a basis for evaluation planning? | TODO |

## 8. Requirements and Constraints

### 8.1 Requirements Register

| Requirement ID | Requirement Statement | Requirement Type | Source Objective | Verification/Evaluation Method | Priority |
|---|---|---|---|---|---|
| REQ-001 | TODO | TODO: functional/nonfunctional/data/interface/process/documentation/governance | OBJ-001 | TODO | must |
| REQ-002 | TODO | TODO | OBJ-002 | TODO | must |
| REQ-003 | TODO | TODO | OBJ-003 | TODO | should |
| REQ-004 | TODO | TODO | OBJ-004 | TODO | should |

### 8.2 Meta-Requirements

Meta-requirements express generalized requirements that may support reusable design knowledge beyond the local artifact instance.

| Meta-Requirement ID | Meta-Requirement | Problem Class Addressed | Local Instantiation | Reuse/Projectability Note |
|---|---|---|---|---|
| MR-001 | TODO | TODO | TODO | TODO |
| MR-002 | TODO | TODO | TODO | TODO |

### 8.3 Design Constraints

| Constraint ID | Constraint | Constraint Type | Design Implication | Evaluation Implication |
|---|---|---|---|---|
| CON-001 | TODO | TODO: technical/resource/time/security/regulatory/ethical/organizational | TODO | TODO |
| CON-002 | TODO | TODO | TODO | TODO |

### 8.4 Non-Goals

| Non-Goal ID | Non-Goal | Reason Excluded | Risk of Misinterpretation |
|---|---|---|---|
| NG-001 | TODO | TODO | TODO |
| NG-002 | TODO | TODO | TODO |

## 9. Success Criteria and Acceptance Logic

### 9.1 Success Criteria Register

| Criterion ID | Success Criterion | Linked Objective/Requirement | Measurement or Assessment Method | Threshold or Decision Rule | Evidence Required |
|---|---|---|---|---|---|
| SC-001 | TODO | OBJ-001 / REQ-001 | TODO | TODO | TODO |
| SC-002 | TODO | OBJ-002 / REQ-002 | TODO | TODO | TODO |
| SC-003 | TODO | OBJ-003 / REQ-003 | TODO | TODO | TODO |
| SC-004 | TODO | OBJ-004 / REQ-004 | TODO | TODO | TODO |

### 9.2 Minimum Acceptance Criteria

A project may proceed to solution-space grounding and design rationale only when the following minimum criteria are satisfied or explicitly waived.

| Gate ID | Review Question | Pass Condition | Status | Notes |
|---|---|---|---|---|
| POB-GATE-001 | Is the focal problem stated clearly enough to guide design? | One concise focal problem statement is present and bounded. | TODO: pass/fail/waived | TODO |
| POB-GATE-002 | Are stakeholders and context documented? | Primary stakeholders, context dimensions, and boundaries are identified. | TODO | TODO |
| POB-GATE-003 | Are objectives traceable to the problem? | Each must-have objective links to a problem element, evidence item, or stakeholder need. | TODO | TODO |
| POB-GATE-004 | Are requirements reviewable? | Each requirement has a type, source objective, and verification/evaluation method. | TODO | TODO |
| POB-GATE-005 | Are success criteria evaluable? | Each success criterion defines evidence and a decision rule or threshold. | TODO | TODO |

## 10. Evaluation Implications

### 10.1 Evaluation Planning Notes

TODO: Explain how the problem/objective record shapes the evaluation plan.

| Evaluation Implication ID | Linked Objective or Criterion | Evaluation Focus | Candidate Method | Notes |
|---|---|---|---|---|
| EVAL-IMP-001 | OBJ-001 / SC-001 | TODO: utility/quality/validity/reliability/projectability | TODO | TODO |
| EVAL-IMP-002 | OBJ-002 / SC-002 | TODO | TODO | TODO |

### 10.2 Demonstration vs. Evaluation Boundary

| Question | Response |
|---|---|
| What will demonstrate that the artifact can be used? | TODO |
| What will evaluate whether the artifact works well enough? | TODO |
| What evidence will not count as evaluation by itself? | TODO |
| What claims are evaluation evidence sufficient to support? | TODO |
| What claims are not yet supported? | TODO |

## 11. Traceability Matrix

Use this matrix to preserve a reviewable chain from problem evidence to objectives, requirements, success criteria, and evaluation planning.

| Problem Element ID | Evidence ID | Stakeholder/Context ID | Objective ID | Requirement ID | Success Criterion ID | Evaluation Implication ID |
|---|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |

## 12. Transparency Mapping

| DSR Transparency Dimension | How This Record Addresses It | Evidence Status |
|---|---|---|
| Process transparency | TODO: how the problem/objective framing process was documented | TODO: mapped/not_yet_mapped/not_applicable |
| Problem-space transparency | TODO: problem context, stakeholders, goals, timeframe, boundaries | TODO |
| Solution-space transparency | TODO: links to related solution-space record or literature grounding | TODO |
| Build transparency | TODO: how objectives/requirements will constrain later build choices | TODO |
| Evaluation transparency | TODO: success criteria and evaluation implications | TODO |
| Contribution transparency | TODO: knowledge contribution objective and intended projectability | TODO |

## 13. Responsible Design, Risk, and Ethical Considerations

| Consideration ID | Value/Risk/Concern | Affected Stakeholders | Design or Evaluation Response | Status |
|---|---|---|---|---|
| RD-001 | TODO: privacy, security, fairness, accessibility, transparency, safety, burden, exclusion, misuse, compliance | TODO | TODO | TODO |
| RD-002 | TODO | TODO | TODO | TODO |

## 14. Limitations and Open Questions

### 14.1 Limitations

| Limitation ID | Limitation | Implication | Mitigation or Next Step |
|---|---|---|---|
| LIM-001 | TODO | TODO | TODO |
| LIM-002 | TODO | TODO | TODO |

### 14.2 Open Questions

| Question ID | Open Question | Owner | Needed Input | Target Resolution Point |
|---|---|---|---|---|
| OQ-001 | TODO | TODO | TODO | TODO |
| OQ-002 | TODO | TODO | TODO | TODO |

## 15. Reviewer Checklist

| Check ID | Review Question | Evidence Required | Pass Condition | Fail Condition | Remediation Guidance |
|---|---|---|---|---|---|
| POB-CHK-001 | Is the focal problem clear, bounded, and DSR-relevant? | Problem statement, scope, problem classification | Problem can guide artifact design and evaluation. | Problem is too vague, purely descriptive, or not artifact-addressable. | Rewrite problem statement and clarify DSR relevance. |
| POB-CHK-002 | Are stakeholders and context sufficiently documented? | Stakeholder table, context description, boundary conditions | Main affected roles and contextual limits are visible. | Stakeholders or context are missing. | Add stakeholder/context evidence and boundary conditions. |
| POB-CHK-003 | Are objectives derived from the problem and evidence? | Objective register and traceability matrix | Objectives link to problem elements, evidence, or needs. | Objectives appear arbitrary or solution-biased. | Add derivation rationale or revise objectives. |
| POB-CHK-004 | Are requirements specific enough for design work? | Requirements register | Requirements are typed, prioritized, and verifiable. | Requirements are ambiguous or untestable. | Rewrite requirements using measurable or inspectable terms. |
| POB-CHK-005 | Are success criteria evaluable? | Success criteria register | Criteria include methods, evidence, and decision rules. | Criteria lack thresholds, evidence, or evaluation logic. | Add measurement/assessment method and acceptance logic. |
| POB-CHK-006 | Are utility, quality, and contribution distinguished? | Section 6.2 and objective types | The record does not conflate use, artifact quality, and knowledge contribution. | Claims are conflated or overclaimed. | Separate practical utility, artifact quality, and knowledge contribution claims. |
| POB-CHK-007 | Are demonstration and evaluation distinguished? | Section 10.2 | Demonstration evidence and evaluation evidence are explicitly separated. | Demonstration is treated as sufficient evaluation without rationale. | Add evaluation plan implications and claim limits. |
| POB-CHK-008 | Are limitations and open questions explicit? | Sections 14.1 and 14.2 | Uncertainty is visible and assigned to next steps. | The record hides assumptions or unresolved dependencies. | Add limitations, assumptions, and needed inputs. |

## 16. Completion Summary

Complete this section when the problem-and-objectives record is ready for internal review.

| Field | Response |
|---|---|
| Prepared by | TODO |
| Date completed | TODO: YYYY-MM-DD |
| Review status | TODO: draft/in_review/approved |
| Ready for solution-space grounding? | TODO: yes/no/conditional |
| Ready for design rationale? | TODO: yes/no/conditional |
| Ready for evaluation planning? | TODO: yes/no/conditional |
| Major unresolved risks | TODO |
| Next recommended file | templates/solution-space-record-template.yaml |
