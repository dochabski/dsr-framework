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
  owner: TODO: responsible_role_or_project_owner
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
      evidence_status: not_yet_mapped
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

Replace every `TODO:` value with project-specific content. Keep sections marked `Not applicable` only when the rationale is explicit.

## 1. Record Control

| Field | Value |
|---|---|
| Design rationale ID | TODO: `design_rationale_<project_or_artifact_slug>_<sequence>` |
| Decision title | TODO: concise decision title |
| Project or artifact | TODO: project/artifact name |
| Artifact version affected | TODO: version, release, branch, or package state |
| Decision status | TODO: proposed / accepted / rejected / superseded / deprecated |
| Decision date | TODO: YYYY-MM-DD |
| Responsible party | TODO: name or role |
| Reviewers or contributors | TODO: names or roles |
| Related decision records | TODO: links or IDs; write `none` if no related records exist |
| Related requirements | TODO: links or IDs from problem-and-objectives record |
| Related solution-space records | TODO: links or IDs from solution-space grounding record |
| Retention rule | Retain with artifact package records while the affected artifact version remains citable, reviewable, or reusable. |

## 2. Decision Summary

### 2.1 Decision Statement

TODO: State the selected design decision in one to three sentences.

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
- [ ] Other: TODO

### 2.3 Decision Priority

| Priority dimension | Rating | Rationale |
|---|---:|---|
| Critical to artifact utility | TODO: low / medium / high | TODO |
| Critical to artifact quality | TODO: low / medium / high | TODO |
| Critical to knowledge contribution | TODO: low / medium / high | TODO |
| Critical to reviewability | TODO: low / medium / high | TODO |
| Critical to reuse or projectability | TODO: low / medium / high | TODO |

## 3. Context and Trigger

### 3.1 Triggering Issue

TODO: Describe the uncertainty, conflict, constraint, opportunity, review finding, stakeholder need, or design fork that required a decision.

### 3.2 Design Context

| Context element | Description |
|---|---|
| DSR lifecycle stage | TODO: problem identification / objectives / solution grounding / design-build / demonstration / evaluation / contribution / packaging / release |
| Artifact or component affected | TODO |
| Intended use context | TODO |
| Primary users or stakeholders | TODO |
| Constraints | TODO: technical, organizational, resource, timing, ethical, legal, publication, or maintenance constraints |
| Prior state | TODO: describe the current or previous design state |
| Desired future state | TODO: describe the state the decision is expected to enable |

## 4. Problem-Space Trace

Use this section to show how the decision responds to the documented problem context, objectives, requirements, and success criteria.

| Problem-space element | Source or ID | Relevance to decision |
|---|---|---|
| Problem class | TODO | TODO |
| Local problem instance | TODO | TODO |
| Stakeholder need | TODO | TODO |
| Objective | TODO | TODO |
| Functional requirement | TODO | TODO |
| Nonfunctional requirement | TODO | TODO |
| Success criterion | TODO | TODO |
| Boundary condition | TODO | TODO |

## 5. Solution-Space Trace

Use this section to show how prior knowledge, existing artifacts, technologies, methods, standards, or DSR literature informed the decision.

| Solution-space source | Source type | Relevant finding or principle | Confidence | Use in rationale |
|---|---|---|---|---|
| TODO | TODO: theory / prior artifact / design principle / empirical evidence / standard / stakeholder input / technical constraint | TODO | TODO: low / medium / high | TODO |
| TODO | TODO | TODO | TODO | TODO |

### 5.1 Evidence Gaps

| Gap ID | Missing evidence | Why it matters | Interim handling |
|---|---|---|---|
| TODO | TODO | TODO | TODO: assumption / review action / evaluation item / backlog item |

## 6. Alternatives Considered

Include the selected alternative as well as rejected alternatives. Do not omit plausible options merely because they were rejected early.

| Alternative ID | Alternative | Description | Expected benefits | Expected costs or risks | Rejection or selection rationale |
|---|---|---|---|---|---|
| ALT-01 | TODO: selected alternative | TODO | TODO | TODO | TODO: selected because... |
| ALT-02 | TODO: rejected alternative | TODO | TODO | TODO | TODO: rejected because... |
| ALT-03 | TODO: rejected alternative | TODO | TODO | TODO | TODO: rejected because... |

## 7. Evaluation Criteria and Tradeoff Analysis

### 7.1 Criteria

Use criteria that fit the decision. Add weights only when the team intentionally used weighted scoring.

| Criterion ID | Criterion | Weight or priority | Measurement or assessment basis | Minimum acceptable condition |
|---|---|---:|---|---|
| C-01 | Artifact utility | TODO | TODO | TODO |
| C-02 | Artifact quality | TODO | TODO | TODO |
| C-03 | Contribution to knowledge | TODO | TODO | TODO |
| C-04 | Feasibility | TODO | TODO | TODO |
| C-05 | Maintainability | TODO | TODO | TODO |
| C-06 | Validity support | TODO | TODO | TODO |
| C-07 | Reliability support | TODO | TODO | TODO |
| C-08 | Replication or projectability support | TODO | TODO | TODO |
| C-09 | Transparency and reviewability | TODO | TODO | TODO |
| C-10 | Responsible design considerations | TODO | TODO | TODO |

### 7.2 Tradeoff Matrix

| Alternative ID | Criteria satisfied | Criteria weakened | Tradeoff summary | Residual risk |
|---|---|---|---|---|
| ALT-01 | TODO | TODO | TODO | TODO |
| ALT-02 | TODO | TODO | TODO | TODO |
| ALT-03 | TODO | TODO | TODO | TODO |

### 7.3 Decisive Tradeoff

TODO: State the tradeoff that most strongly determined the decision. Distinguish the artifact-performance reason from the knowledge-contribution or reporting reason.

## 8. Rationale Argument

### 8.1 Structured Rationale

Complete the argument structure.

- **Claim:** TODO: the selected decision is justified for this artifact and context.
- **Grounds:** TODO: evidence, requirements, constraints, stakeholder needs, and prior knowledge supporting the decision.
- **Warrant:** TODO: why those grounds support the claim.
- **Backing:** TODO: DSR literature, design principles, evaluation evidence, standards, or domain evidence.
- **Qualifier:** TODO: degree of confidence or conditions under which the rationale holds.
- **Rebuttals or exceptions:** TODO: conditions that could defeat or weaken the rationale.

### 8.2 Design Mechanism

TODO: Explain the expected mechanism by which the decision improves the artifact, implementation, evaluation, reviewability, or contribution.

Example pattern:

> This decision is expected to improve [outcome] by enabling [mechanism] under [conditions], provided that [assumption] holds.

## 9. Impact on DSR Artifact Claims

Distinguish local usefulness from quality evidence and contribution claims.

| Claim category | Impact of decision | Evidence available | Evidence still needed |
|---|---|---|---|
| Artifact utility | TODO | TODO | TODO |
| Artifact quality | TODO | TODO | TODO |
| Design knowledge contribution | TODO | TODO | TODO |
| Practical contribution | TODO | TODO | TODO |
| Methodological or theoretical contribution | TODO | TODO | TODO |
| Reviewability or transparency | TODO | TODO | TODO |

## 10. Demonstration and Evaluation Implications

Demonstration shows use; evaluation judges performance, quality, fitness, or contribution. Record both explicitly when relevant.

| Implication type | Required action | Evidence to collect | Responsible party | Timing |
|---|---|---|---|---|
| Demonstration | TODO: show how the artifact/component can be used | TODO | TODO | TODO |
| Formative evaluation | TODO: test during build or iteration | TODO | TODO | TODO |
| Summative evaluation | TODO: evaluate final or release candidate artifact | TODO | TODO | TODO |
| Reviewer assessment | TODO: what a reviewer should inspect | TODO | TODO | TODO |
| Post-release monitoring | TODO: what to observe after release, if applicable | TODO | TODO | TODO |

## 11. Validity, Reliability, Replication, and Projectability

| Quality construct | Implication of decision | Threat introduced or reduced | Mitigation or evidence requirement |
|---|---|---|---|
| Construct validity | TODO | TODO | TODO |
| Internal or causal validity | TODO or Not applicable | TODO | TODO |
| External validity or transferability | TODO | TODO | TODO |
| Evaluation validity | TODO | TODO | TODO |
| Process reliability | TODO | TODO | TODO |
| Artifact reliability | TODO | TODO | TODO |
| Measurement reliability | TODO or Not applicable | TODO | TODO |
| Replication support | TODO | TODO | TODO |
| Projectability or adaptation support | TODO | TODO | TODO |

## 12. Responsible Design and Stakeholder Considerations

| Consideration | Impact | Stakeholders affected | Mitigation or design response |
|---|---|---|---|
| Privacy | TODO or Not applicable | TODO | TODO |
| Security | TODO or Not applicable | TODO | TODO |
| Accessibility | TODO or Not applicable | TODO | TODO |
| Equity or inclusion | TODO or Not applicable | TODO | TODO |
| Transparency burden | TODO or Not applicable | TODO | TODO |
| Intellectual property or proprietary information | TODO or Not applicable | TODO | TODO |
| Maintenance burden | TODO or Not applicable | TODO | TODO |
| Practitioner usability | TODO or Not applicable | TODO | TODO |
| Aesthetic or communicative fit | TODO or Not applicable | TODO | TODO |

## 13. Implementation Notes

| Implementation element | Description |
|---|---|
| Required changes | TODO |
| Files or components affected | TODO |
| Data or schema impacts | TODO |
| Migration or compatibility concerns | TODO |
| Documentation updates required | TODO |
| Review or approval gates | TODO |
| Rollback or revision path | TODO |

## 14. Boundary Conditions and Non-Goals

### 14.1 Boundary Conditions

- TODO: Condition under which the decision is valid.
- TODO: Context where the decision may not transfer.
- TODO: Dependency that must remain true for the rationale to hold.

### 14.2 Non-Goals

- TODO: What this decision does not attempt to solve.
- TODO: What evidence or claim should not be inferred from this decision.

## 15. Risks, Costs, and Mitigations

| Risk ID | Risk or cost | Likelihood | Severity | Mitigation | Owner |
|---|---|---|---|---|---|
| R-01 | TODO | TODO: low / medium / high | TODO: low / medium / high | TODO | TODO |
| R-02 | TODO | TODO | TODO | TODO | TODO |
| R-03 | TODO | TODO | TODO | TODO | TODO |

## 16. Revision Triggers

Revise this rationale if any of the following occur.

- [ ] A key requirement changes.
- [ ] A stakeholder group or use context changes.
- [ ] Evaluation evidence contradicts the expected mechanism.
- [ ] A superior alternative becomes feasible.
- [ ] A privacy, security, accessibility, or maintenance risk becomes material.
- [ ] The artifact boundary, package conformance level, or release target changes.
- [ ] Other: TODO

## 17. Traceability Matrix

| Trace ID | From | To | Trace type | Evidence status |
|---|---|---|---|---|
| TR-01 | TODO: requirement ID | TODO: selected decision | satisfies / constrains / conflicts_with / informs | TODO: mapped / not_yet_mapped |
| TR-02 | TODO: solution-space source ID | TODO: selected decision | informs | TODO |
| TR-03 | TODO: selected decision | TODO: artifact component | implements / modifies / constrains | TODO |
| TR-04 | TODO: selected decision | TODO: evaluation item | requires_evaluation / supports_evaluation | TODO |
| TR-05 | TODO: selected decision | TODO: contribution claim | supports / limits / does_not_support | TODO |

## 18. Reviewer Checklist

| Check ID | Review question | Evidence required | Pass condition | Status |
|---|---|---|---|---|
| DR-C01 | Is the decision stated clearly enough for a reviewer to identify what changed? | Decision statement; affected artifact/component | The selected option and affected scope are unambiguous. | TODO |
| DR-C02 | Are plausible alternatives documented? | Alternatives table | At least one selected and one rejected option are described, unless a sole-source constraint is justified. | TODO |
| DR-C03 | Are tradeoffs explicit rather than implied? | Criteria and tradeoff matrix | Benefits, costs, weakened criteria, and residual risks are visible. | TODO |
| DR-C04 | Is the rationale grounded in problem-space and solution-space evidence? | Trace tables; source basis | Requirements and justificatory knowledge are linked or evidence gaps are marked. | TODO |
| DR-C05 | Are artifact utility, artifact quality, and knowledge contribution distinguished? | Impact table | The record does not overclaim contribution from utility alone. | TODO |
| DR-C06 | Are demonstration and evaluation implications separated? | Demonstration/evaluation table | Use scenarios and evaluation criteria are not conflated. | TODO |
| DR-C07 | Are validity, reliability, replication, and projectability implications addressed? | Quality construct table | Relevant threats and mitigations are recorded or marked not applicable with rationale. | TODO |
| DR-C08 | Are responsible design issues considered proportionately? | Responsible design table | Material privacy, security, accessibility, equity, IP, and maintenance concerns are addressed. | TODO |
| DR-C09 | Are revision triggers and rollback paths defined? | Revision triggers; implementation notes | Future conditions requiring reconsideration are explicit. | TODO |

## 19. Completion Status

| Completion item | Status | Notes |
|---|---|---|
| Required metadata complete | TODO: yes / no / partial | TODO |
| Problem-space trace complete | TODO: yes / no / partial | TODO |
| Solution-space trace complete | TODO: yes / no / partial | TODO |
| Alternatives and tradeoffs complete | TODO: yes / no / partial | TODO |
| Rationale argument complete | TODO: yes / no / partial | TODO |
| Evaluation implications complete | TODO: yes / no / partial | TODO |
| Quality implications complete | TODO: yes / no / partial | TODO |
| Responsible design implications complete | TODO: yes / no / partial | TODO |
| Reviewer checklist complete | TODO: yes / no / partial | TODO |

## 20. Open Questions

| Question ID | Open question | Needed input | Owner | Target resolution date |
|---|---|---|---|---|
| OQ-01 | TODO | TODO | TODO | TODO: YYYY-MM-DD |

## 21. Appendix: Optional Decision Log Entry

Use this compact entry in package inventories, release notes, or design-decision indexes.

```yaml
design_decision_summary:
  decision_id: TODO
  title: TODO
  status: TODO
  date: TODO
  artifact_or_component: TODO
  selected_option: TODO
  primary_rationale: TODO
  primary_tradeoff: TODO
  evidence_status: TODO: mapped / partially_mapped / not_yet_mapped
  related_records:
    - TODO
```
