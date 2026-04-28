<!-- SPDX-License-Identifier: CC0-1.0 -->

---
template:
  id: template_design_rationale
  item_id: template_design_rationale
  item_type: specification
  title: Design Rationale Template
  target_path: templates/design-rationale-template.md
  output_format: markdown
  status: draft
  version: "0.1.0"
  conformance_target: l2_reviewable
  owner: project_specific_placeholder: responsible_role_or_project_owner
  purpose: >
    Provide a reusable Markdown template for documenting DSR design decisions,
    alternatives, tradeoffs, justificatory knowledge, stakeholder considerations,
    and rationale traceability.
  intended_users:
    - dsr_researcher
    - artifact_designer
    - reviewer
    - maintainer
  source_basis:
    - id: dsr_framework_generation_spec
      evidence_status: mapped
      use: Governs repository conventions, template expectations, reviewability, and DSR distinctions.
    - id: dsr_generation_prompt
      evidence_status: mapped
      use: Governs generation procedure, metadata, traceability, and final review expectations.
    - id: hevner_et_al_2024_transparency_in_design_science_research
      evidence_status: mapped
      use: Supports process, build, evaluation, and contribution transparency fields.
      citation_anchor_ids:
        - CA06
        - CA09
        - CA10
        - CA11
        - CA16
    - id: weigand_johannesson_andersson_2021_artifact_ontology_for_dsr
      evidence_status: mapped
      use: Supports make-plan, use-plan, artifact-boundary, capacity, and stakeholder-conversation fields.
      citation_anchor_ids:
        - A10
        - A15
        - A16
        - A17
    - id: design_rationale_schema
      evidence_status: accepted_v1_limitation
      use: Expected validation dependency for structured design-rationale records.
  related_items:
    upstream_dependencies:
      - templates/problem-and-objectives-template.md
      - templates/solution-space-record-template.yaml
      - schemas/design-rationale.schema.json
    downstream_uses:
      - templates/artifact-specification-template.md
      - templates/build-transparency-record-template.yaml
      - records/design-decisions/
      - records/reviews/
  change_history:
    - version: "0.1.0"
      date: "2026-04-27"
      change: Initial reviewable Markdown template generated for template_design_rationale.
      responsible_party: GPT-5.5 Thinking
---

# Design Rationale Record

Use this template to document why a Design Science Research artifact, component, method, model, protocol, or package decision was made. The record should make the design reasoning inspectable without requiring reviewers to infer hidden assumptions.

Replace every `project_specific_placeholder:` value with project-specific content. Keep sections marked `Not applicable` only when the rationale is explicit.

## 1. Record Control

| Field | Value |
|---|---|
| Design rationale ID | project_specific_placeholder: `design_rationale_<project_or_artifact_slug>_<sequence>` |
| Decision title | project_specific_placeholder: concise decision title |
| Project or artifact | project_specific_placeholder: project/artifact name |
| Artifact version affected | project_specific_placeholder: version, release, branch, or package state |
| Decision status | project_specific_placeholder: proposed / accepted / rejected / superseded / deprecated |
| Decision date | project_specific_placeholder: YYYY-MM-DD |
| Responsible party | project_specific_placeholder: name or role |
| Reviewers or contributors | project_specific_placeholder: names or roles |
| Related decision records | project_specific_placeholder: links or IDs; write `none` if no related records exist |
| Related requirements | project_specific_placeholder: links or IDs from problem-and-objectives record |
| Related solution-space records | project_specific_placeholder: links or IDs from solution-space grounding record |
| Retention rule | Retain with artifact package records while the affected artifact version remains citable, reviewable, or reusable. |

## 2. Decision Summary

### 2.1 Decision Statement

project_specific_placeholder: State the selected design decision in one to three sentences.

Example pattern:

> We decided to [selected design action] for [artifact/component/process] because [primary rationale], while accepting [main tradeoff or residual risk].

### 2.2 Decision Type

Select all that apply.

- [ ] Artifact boundary or scope decision
- [ ] Artifact type or abstraction-level decision
- [ ] Architecture or component decision
- [ ] Data, metadata, or schema decision
- [ ] Interface or user-interaction decision
- [ ] Workflow or process decision
- [ ] Evaluation design decision
- [ ] Evidence, repository, or transparency decision
- [ ] Publication, release, or packaging decision
- [ ] Responsible design, privacy, security, accessibility, or ethics decision
- [ ] Other: project_specific_placeholder

### 2.3 Decision Priority

| Priority dimension | Rating | Rationale |
|---|---:|---|
| Critical to artifact utility | project_specific_placeholder: low / medium / high | project_specific_placeholder |
| Critical to artifact quality | project_specific_placeholder: low / medium / high | project_specific_placeholder |
| Critical to knowledge contribution | project_specific_placeholder: low / medium / high | project_specific_placeholder |
| Critical to reviewability | project_specific_placeholder: low / medium / high | project_specific_placeholder |
| Critical to reuse or projectability | project_specific_placeholder: low / medium / high | project_specific_placeholder |

## 3. Context and Trigger

### 3.1 Triggering Issue

project_specific_placeholder: Describe the uncertainty, conflict, constraint, opportunity, review finding, stakeholder need, or design fork that required a decision.

### 3.2 Design Context

| Context element | Description |
|---|---|
| DSR lifecycle stage | project_specific_placeholder: problem identification / objectives / solution grounding / design-build / demonstration / evaluation / contribution / packaging / release |
| Artifact or component affected | project_specific_placeholder |
| Intended use context | project_specific_placeholder |
| Primary users or stakeholders | project_specific_placeholder |
| Constraints | project_specific_placeholder: technical, organizational, resource, timing, ethical, legal, publication, or maintenance constraints |
| Prior state | project_specific_placeholder: describe the current or previous design state |
| Desired future state | project_specific_placeholder: describe the state the decision is expected to enable |

## 4. Problem-Space Trace

Use this section to show how the decision responds to the documented problem context, objectives, requirements, and success criteria.

| Problem-space element | Source or ID | Relevance to decision |
|---|---|---|
| Problem class | project_specific_placeholder | project_specific_placeholder |
| Local problem instance | project_specific_placeholder | project_specific_placeholder |
| Stakeholder need | project_specific_placeholder | project_specific_placeholder |
| Objective | project_specific_placeholder | project_specific_placeholder |
| Functional requirement | project_specific_placeholder | project_specific_placeholder |
| Nonfunctional requirement | project_specific_placeholder | project_specific_placeholder |
| Success criterion | project_specific_placeholder | project_specific_placeholder |
| Boundary condition | project_specific_placeholder | project_specific_placeholder |

## 5. Solution-Space Trace

Use this section to show how prior knowledge, existing artifacts, technologies, methods, standards, or DSR literature informed the decision.

| Solution-space source | Source type | Relevant finding or principle | Confidence | Use in rationale |
|---|---|---|---|---|
| project_specific_placeholder | project_specific_placeholder: theory / prior artifact / design principle / empirical evidence / standard / stakeholder input / technical constraint | project_specific_placeholder | project_specific_placeholder: low / medium / high | project_specific_placeholder |
| project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 5.1 Evidence Gaps

| Gap ID | Missing evidence | Why it matters | Interim handling |
|---|---|---|---|
| project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder: assumption / review action / evaluation item / backlog item |

## 6. Alternatives Considered

Include the selected alternative as well as rejected alternatives. Do not omit plausible options merely because they were rejected early.

| Alternative ID | Alternative | Description | Expected benefits | Expected costs or risks | Rejection or selection rationale |
|---|---|---|---|---|---|
| ALT-01 | project_specific_placeholder: selected alternative | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder: selected because... |
| ALT-02 | project_specific_placeholder: rejected alternative | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder: rejected because... |
| ALT-03 | project_specific_placeholder: rejected alternative | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder: rejected because... |

## 7. Evaluation Criteria and Tradeoff Analysis

### 7.1 Criteria

Use criteria that fit the decision. Add weights only when the team intentionally used weighted scoring.

| Criterion ID | Criterion | Weight or priority | Measurement or assessment basis | Minimum acceptable condition |
|---|---|---:|---|---|
| C-01 | Artifact utility | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-02 | Artifact quality | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-03 | Contribution to knowledge | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-04 | Feasibility | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-05 | Maintainability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-06 | Validity support | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-07 | Reliability support | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-08 | Replication or projectability support | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-09 | Transparency and reviewability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| C-10 | Responsible design considerations | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 7.2 Tradeoff Matrix

| Alternative ID | Criteria satisfied | Criteria weakened | Tradeoff summary | Residual risk |
|---|---|---|---|---|
| ALT-01 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| ALT-02 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| ALT-03 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

### 7.3 Decisive Tradeoff

project_specific_placeholder: State the tradeoff that most strongly determined the decision. Distinguish the artifact-performance reason from the knowledge-contribution or reporting reason.

## 8. Rationale Argument

### 8.1 Structured Rationale

Complete the argument structure.

- **Claim:** project_specific_placeholder: the selected decision is justified for this artifact and context.
- **Grounds:** project_specific_placeholder: evidence, requirements, constraints, stakeholder needs, and prior knowledge supporting the decision.
- **Warrant:** project_specific_placeholder: why those grounds support the claim.
- **Backing:** project_specific_placeholder: DSR literature, design principles, evaluation evidence, standards, or domain evidence.
- **Qualifier:** project_specific_placeholder: degree of confidence or conditions under which the rationale holds.
- **Rebuttals or exceptions:** project_specific_placeholder: conditions that could defeat or weaken the rationale.

### 8.2 Design Mechanism

project_specific_placeholder: Explain the expected mechanism by which the decision improves the artifact, implementation, evaluation, reviewability, or contribution.

Example pattern:

> This decision is expected to improve [outcome] by enabling [mechanism] under [conditions], provided that [assumption] holds.

## 9. Impact on DSR Artifact Claims

Distinguish local usefulness from quality evidence and contribution claims.

| Claim category | Impact of decision | Evidence available | Evidence still needed |
|---|---|---|---|
| Artifact utility | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Artifact quality | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Design knowledge contribution | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Practical contribution | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Methodological or theoretical contribution | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Reviewability or transparency | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

## 10. Demonstration and Evaluation Implications

Demonstration shows use; evaluation judges performance, quality, fitness, or contribution. Record both explicitly when relevant.

| Implication type | Required action | Evidence to collect | Responsible party | Timing |
|---|---|---|---|---|
| Demonstration | project_specific_placeholder: show how the artifact/component can be used | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Formative evaluation | project_specific_placeholder: test during build or iteration | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Summative evaluation | project_specific_placeholder: evaluate final or release candidate artifact | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Reviewer assessment | project_specific_placeholder: what a reviewer should inspect | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Post-release monitoring | project_specific_placeholder: what to observe after release, if applicable | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

## 11. Validity, Reliability, Replication, and Projectability

| Quality construct | Implication of decision | Threat introduced or reduced | Mitigation or evidence requirement |
|---|---|---|---|
| Construct validity | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Internal or causal validity | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| External validity or transferability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Evaluation validity | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Process reliability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Artifact reliability | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Measurement reliability | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Replication support | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| Projectability or adaptation support | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

## 12. Responsible Design and Stakeholder Considerations

| Consideration | Impact | Stakeholders affected | Mitigation or design response |
|---|---|---|---|
| Privacy | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Security | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Accessibility | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Equity or inclusion | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Transparency burden | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Intellectual property or proprietary information | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Maintenance burden | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Practitioner usability | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |
| Aesthetic or communicative fit | project_specific_placeholder or Not applicable | project_specific_placeholder | project_specific_placeholder |

## 13. Implementation Notes

| Implementation element | Description |
|---|---|
| Required changes | project_specific_placeholder |
| Files or components affected | project_specific_placeholder |
| Data or schema impacts | project_specific_placeholder |
| Migration or compatibility concerns | project_specific_placeholder |
| Documentation updates required | project_specific_placeholder |
| Review or approval gates | project_specific_placeholder |
| Rollback or revision path | project_specific_placeholder |

## 14. Boundary Conditions and Non-Goals

### 14.1 Boundary Conditions

- project_specific_placeholder: Condition under which the decision is valid.
- project_specific_placeholder: Context where the decision may not transfer.
- project_specific_placeholder: Dependency that must remain true for the rationale to hold.

### 14.2 Non-Goals

- project_specific_placeholder: What this decision does not attempt to solve.
- project_specific_placeholder: What evidence or claim should not be inferred from this decision.

## 15. Risks, Costs, and Mitigations

| Risk ID | Risk or cost | Likelihood | Severity | Mitigation | Owner |
|---|---|---|---|---|---|
| R-01 | project_specific_placeholder | project_specific_placeholder: low / medium / high | project_specific_placeholder: low / medium / high | project_specific_placeholder | project_specific_placeholder |
| R-02 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |
| R-03 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder |

## 16. Revision Triggers

Revise this rationale if any of the following occur.

- [ ] A key requirement changes.
- [ ] A stakeholder group or use context changes.
- [ ] Evaluation evidence contradicts the expected mechanism.
- [ ] A superior alternative becomes feasible.
- [ ] A privacy, security, accessibility, or maintenance risk becomes material.
- [ ] The artifact boundary, package conformance level, or release target changes.
- [ ] Other: project_specific_placeholder

## 17. Traceability Matrix

| Trace ID | From | To | Trace type | Evidence status |
|---|---|---|---|---|
| TR-01 | project_specific_placeholder: requirement ID | project_specific_placeholder: selected decision | satisfies / constrains / conflicts_with / informs | project_specific_placeholder: mapped / accepted_v1_limitation |
| TR-02 | project_specific_placeholder: solution-space source ID | project_specific_placeholder: selected decision | informs | project_specific_placeholder |
| TR-03 | project_specific_placeholder: selected decision | project_specific_placeholder: artifact component | implements / modifies / constrains | project_specific_placeholder |
| TR-04 | project_specific_placeholder: selected decision | project_specific_placeholder: evaluation item | requires_evaluation / supports_evaluation | project_specific_placeholder |
| TR-05 | project_specific_placeholder: selected decision | project_specific_placeholder: contribution claim | supports / limits / does_not_support | project_specific_placeholder |

## 18. Reviewer Checklist

| Check ID | Review question | Evidence required | Pass condition | Status |
|---|---|---|---|---|
| DR-C01 | Is the decision stated clearly enough for a reviewer to identify what changed? | Decision statement; affected artifact/component | The selected option and affected scope are unambiguous. | project_specific_placeholder |
| DR-C02 | Are plausible alternatives documented? | Alternatives table | At least one selected and one rejected option are described, unless a sole-source constraint is justified. | project_specific_placeholder |
| DR-C03 | Are tradeoffs explicit rather than implied? | Criteria and tradeoff matrix | Benefits, costs, weakened criteria, and residual risks are visible. | project_specific_placeholder |
| DR-C04 | Is the rationale grounded in problem-space and solution-space evidence? | Trace tables; source basis | Requirements and justificatory knowledge are linked or evidence gaps are marked. | project_specific_placeholder |
| DR-C05 | Are artifact utility, artifact quality, and knowledge contribution distinguished? | Impact table | The record does not overclaim contribution from utility alone. | project_specific_placeholder |
| DR-C06 | Are demonstration and evaluation implications separated? | Demonstration/evaluation table | Use scenarios and evaluation criteria are not conflated. | project_specific_placeholder |
| DR-C07 | Are validity, reliability, replication, and projectability implications addressed? | Quality construct table | Relevant threats and mitigations are recorded or marked not applicable with rationale. | project_specific_placeholder |
| DR-C08 | Are responsible design issues considered proportionately? | Responsible design table | Material privacy, security, accessibility, equity, IP, and maintenance concerns are addressed. | project_specific_placeholder |
| DR-C09 | Are revision triggers and rollback paths defined? | Revision triggers; implementation notes | Future conditions requiring reconsideration are explicit. | project_specific_placeholder |

## 19. Completion Status

| Completion item | Status | Notes |
|---|---|---|
| Required metadata complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Problem-space trace complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Solution-space trace complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Alternatives and tradeoffs complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Rationale argument complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Evaluation implications complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Quality implications complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Responsible design implications complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |
| Reviewer checklist complete | project_specific_placeholder: yes / no / partial | project_specific_placeholder |

## 20. Open Questions

| Question ID | Open question | Needed input | Owner | Target resolution date |
|---|---|---|---|---|
| OQ-01 | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder | project_specific_placeholder: YYYY-MM-DD |

## 21. Appendix: Optional Decision Log Entry

Use this compact entry in package inventories, release notes, or design-decision indexes.

```yaml
design_decision_summary:
  decision_id: project_specific_placeholder
  title: project_specific_placeholder
  status: project_specific_placeholder
  date: project_specific_placeholder
  artifact_or_component: project_specific_placeholder
  selected_option: project_specific_placeholder
  primary_rationale: project_specific_placeholder
  primary_tradeoff: project_specific_placeholder
  evidence_status: project_specific_placeholder: mapped / partially_mapped / accepted_v1_limitation
  related_records:
    - project_specific_placeholder
```
