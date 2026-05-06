---
SPDX-License-Identifier: CC0-1.0
item_id: wicked_problem_resolution_workflow
item_type: process_artifact
title: Wicked Problem Resolution Workflow
status: 1.2.0_stable
version: 1.2.0
artifact_type: process_artifact
file_conformance: l1_documented
package_conformance: l4_reusable_stable
l5_claimed: false
intended_repository_location: docs/wicked-problem-resolution-workflow.md
related_framework: Design Science Research operationalization
license: CC0-1.0
---

# Wicked Problem Resolution Workflow

## Purpose

This workflow is a repository-ready process artifact for approaching wicked problems through a Design Science Research (DSR)-oriented logic. It is designed to help a researcher, practitioner, or project team move from a messy, contested, situated problem to a traceable intervention, evaluated artifact, and reusable design knowledge.

The workflow treats wicked problem solving as an iterative process of problem framing, stakeholder/context modeling, causal diagnosis, requirements derivation, artifact design, safe-to-fail experimentation, evaluation, and knowledge codification.

## Operating principle

Do not treat a wicked problem as something to solve once. Treat it as something to progressively tame, evaluate, reframe, and learn from.

Working rule:

> Produce progressively better problem framings, interventions, evaluations, and reusable design knowledge while documenting what is known, assumed, contested, bounded, and learned.

## Intended users

- DSR researchers designing or evaluating artifact-centered interventions.
- Quality assurance, compliance, institutional effectiveness, or process improvement teams.
- Project teams working on ambiguous socio-technical or organizational problems.
- Repository maintainers who need traceable problem-to-artifact documentation.

## When to use this workflow

Use this workflow when the problem has one or more of the following properties:

- The problem definition is contested.
- Stakeholders disagree about causes, priorities, or success criteria.
- Prior fixes have failed, produced side effects, or shifted the burden elsewhere.
- The situation has technical, organizational, ethical, governance, or cultural dimensions.
- There is no obvious stopping rule.
- The intervention must be evaluated under boundary conditions.
- The team needs to produce reusable design knowledge, not merely a local fix.

## Repository outputs

A complete cycle should produce the following files or records:

| Output | Suggested path | Purpose |
|---|---|---|
| Problem situation note | `artifacts/problem-situation-note.md` | Raw description of the problematic situation |
| Wickedness profile | `artifacts/wickedness-profile.yaml` | Structured diagnosis of why the problem is wicked |
| Problem instance/class record | `artifacts/problem-abstraction.yaml` | Link between local problem and broader problem class |
| Stakeholder/context register | `artifacts/context-and-stakeholders.yaml` | Stakeholder roles, claims, incentives, constraints, and boundaries |
| Causal/leverage map | `artifacts/causal-leverage-map.md` | Causal factors and intervention leverage points |
| Requirement trace matrix | `artifacts/problem-requirement-trace.yaml` | Problem-to-objective-to-requirement trace |
| Solution option matrix | `artifacts/solution-option-matrix.md` | Candidate intervention comparison |
| Artifact specification | `artifacts/artifact-specification.yaml` | Artifact/design entity, make plan, use plan, capacity specification, and claims |
| Evaluation protocol | `artifacts/evaluation-protocol.yaml` | Criteria, methods, timing, evidence, and decision rules |
| Claim-evidence matrix | `artifacts/claim-evidence-matrix.yaml` | Evidence linked to make, use, and effect claims |
| Design knowledge record | `artifacts/design-knowledge-record.yaml` | Reusable design principle, design proposition, or negative design knowledge |
| Scale/reframe decision | `artifacts/scale-reframe-decision.md` | Final decision for the cycle |

## Workflow overview

| Phase | Key question | Required output |
|---|---|---|
| 1. Situation capture | What is happening? | Problem situation note |
| 2. Problem abstraction | What local problem and broader problem class are involved? | Problem instance/class record |
| 3. Stakeholder and context mapping | Who is affected, who decides, and what constrains action? | Stakeholder/context register |
| 4. Causal modeling | Why does the problem persist? | Causal/leverage map |
| 5. Objectives and requirements | What must improve, and how will success be recognized? | Requirement trace matrix |
| 6. Solution-space search | What existing knowledge can ground intervention? | Input-knowledge inventory and solution option matrix |
| 7. Artifact design | What intervention artifact will be designed? | Artifact specification |
| 8. Safe-to-fail pilot | What small test can generate evidence? | Pilot and evaluation protocol |
| 9. Evaluation | Which claims are supported by which evidence? | Claim-evidence matrix |
| 10. Knowledge codification | What reusable design knowledge emerged? | Design knowledge record |
| 11. Institutionalization or reframing | Should the intervention scale, revise, stop, or reframe? | Scale/reframe decision |

---

# Phase 1. Capture the problematic situation

## Goal

Describe the problematic situation before imposing a premature solution frame.

## Actions

1. Write a raw description of the situation.
2. Identify visible symptoms, harms, bottlenecks, conflicts, and unmet needs.
3. Separate facts, interpretations, assumptions, and stakeholder claims.
4. Identify why the situation may be wicked.

## Diagnostic question

> What situation keeps reproducing the unwanted condition, even after reasonable people try to fix it?

## Output: problem situation note

Suggested structure:

```markdown
# Problem Situation Note

## Raw situation description

## Visible symptoms

## Harms and risks

## Affected processes, artifacts, or systems

## Known facts

## Interpretations

## Assumptions

## Stakeholder claims

## Prior attempted fixes

## Initial wickedness indicators
```

## Wickedness profile checklist

Check all that apply:

- [ ] Problem definition is contested.
- [ ] Stakeholders disagree about success.
- [ ] Causes are circular or mutually reinforcing.
- [ ] The system changes while the team studies it.
- [ ] Every intervention has side effects.
- [ ] There is no obvious stopping rule.
- [ ] Evidence is incomplete, ambiguous, or politically charged.
- [ ] The problem crosses organizational or disciplinary boundaries.
- [ ] Stakeholders have unequal power or burden.
- [ ] The problem cannot be isolated from its context.

---

# Phase 2. Define the problem instance and problem class

## Goal

Distinguish the situated problem instance from the abstract problem class so that local problem solving can produce reusable design knowledge.

## Actions

1. Define the local problem instance.
2. Abstract the broader problem class.
3. State the practical and theoretical relevance.
4. Define boundary conditions.

## Template

```text
Problem instance:
In [context], [stakeholders] experience [unwanted condition] because [suspected mechanisms/constraints], resulting in [consequences].

Problem class:
This is an instance of a broader class of problems in which [generalized actors/systems] struggle to [generalized function] under [generalized constraints].

Relevance:
This matters because [severity, frequency, risk, opportunity, stakeholder burden, institutional importance].

Boundary conditions:
This framing applies when [conditions] and may not apply when [conditions].
```

## Output: problem abstraction record

Suggested YAML structure:

```yaml
problem_abstraction:
  problem_instance:
    context: null
    stakeholders: []
    unwanted_condition: null
    suspected_mechanisms: []
    consequences: []
  problem_class:
    generalized_problem_type: null
    generalized_actors_or_systems: []
    generalized_constraints: []
    reusable_problem_statement: null
  relevance:
    practical_relevance: null
    theoretical_or_design_relevance: null
    severity_or_importance: null
  boundary_conditions:
    applies_when: []
    may_not_apply_when: []
  trace:
    source_evidence: []
    assumptions: []
    open_questions: []
```

---

# Phase 3. Map stakeholders and context

## Goal

Represent the socio-technical setting that shapes both the problem and any possible intervention.

## Actions

1. Identify stakeholder groups, not only named individuals.
2. Document stakeholder goals, pains, incentives, authority, constraints, and likely resistance.
3. Map contextual constraints: policy, data, systems, culture, budget, time, compliance, ethics, technology, and governance.
4. Identify affected artifacts, processes, documents, systems, metrics, and decision rights.

## Diagnostic question

> Who benefits from the current structure, who is harmed by it, who can change it, and who must live with the result?

## Stakeholder profile table

| Stakeholder group | Goals | Pains | Incentives | Authority | Constraints | Likely resistance | Evidence source |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Context register

| Context dimension | Current condition | Constraint or affordance | Evidence | Boundary condition |
|---|---|---|---|---|
| Organizational |  |  |  |  |
| Technical |  |  |  |  |
| Social/cultural |  |  |  |  |
| Regulatory/compliance |  |  |  |  |
| Resource |  |  |  |  |
| Temporal |  |  |  |  |
| Data/information |  |  |  |  |
| Governance |  |  |  |  |

---

# Phase 4. Build a causal and structural model

## Goal

Model why the problem persists before selecting an intervention.

## Actions

1. Create a causal map of reinforcing loops, bottlenecks, incentives, dependencies, and failure points.
2. Identify root causes, contributing causes, enabling conditions, constraints, and symptoms.
3. Distinguish controllable, influenceable, and uncontrollable factors.
4. Identify leverage points where small changes may produce large improvements.

## Causal factor categories

| Category | Meaning | Example prompt |
|---|---|---|
| Root cause | Necessary underlying driver | What must be true for this problem to recur? |
| Contributing cause | Worsens the problem but is not sufficient alone | What amplifies the problem? |
| Enabling condition | Allows the problem to continue | What permits the issue to persist? |
| Constraint | Limits feasible solutions | What cannot easily be changed? |
| Symptom | Visible manifestation | What people complain about first? |
| Leverage point | High-value intervention point | Where can change produce disproportionate improvement? |

## Control/influence matrix

| Factor | Type | Controllable? | Influenceable? | Uncontrollable? | Evidence | Potential leverage point |
|---|---|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |

---

# Phase 5. Translate the problem into objectives and requirements

## Goal

Convert diagnosis into evaluable design targets.

## Actions

1. Convert the problem into improvement objectives.
2. Convert objectives into requirements.
3. Define acceptance criteria for each requirement.
4. Trace each requirement back to a problem factor or stakeholder need.

## Requirement trace matrix

| Problem factor | Objective | Requirement | Acceptance criterion | Stakeholder source | Evidence source |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Requirement quality checks

Each requirement should be:

- [ ] Traceable to a problem factor or stakeholder need.
- [ ] Testable or inspectable.
- [ ] Bounded by context.
- [ ] Feasible under known constraints.
- [ ] Linked to an evaluation criterion.
- [ ] Clear enough to guide design decisions.

---

# Phase 6. Search the solution space

## Goal

Ground intervention design in existing knowledge instead of inventing from scratch.

## Actions

1. Identify prior solutions, analogous cases, theories, methods, technologies, design patterns, and practitioner knowledge.
2. Identify why previous fixes failed or only partially worked.
3. Generate multiple candidate interventions.
4. Compare options against fit, feasibility, acceptability, reversibility, evaluability, ethical burden, and knowledge value.

## Option evaluation matrix

| Option | Problem fit | Feasibility | Stakeholder acceptability | Reversibility | Evaluability | Ethical burden | Knowledge value | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |  |  |

Scoring suggestion:

- 1 = weak
- 2 = limited
- 3 = adequate
- 4 = strong
- 5 = excellent

## Prior-solution critique prompts

- What did prior fixes assume about the problem?
- Which stakeholder burdens did they ignore?
- Which contextual conditions made them fail?
- Which partial successes should be preserved?
- Which design patterns can be adapted?
- Which alternatives should be rejected and why?

---

# Phase 7. Design the intervention as an artifact

## Goal

Specify the intervention as a DSR artifact or design entity, not just as an activity or local fix.

## Actions

1. Name the artifact or intervention.
2. Classify the artifact type.
3. Define what the artifact is supposed to make possible.
4. Define how it is produced or maintained.
5. Define how users are supposed to use it.
6. State the claims being made about it.

## Artifact types

Examples:

- Construct
- Model
- Method
- Framework
- Taxonomy
- Design principle
- Design pattern
- Process artifact
- Technical instantiation
- Dashboard
- Workflow
- Governance structure
- Policy mechanism
- Training protocol
- Knowledge graph
- Socio-technical intervention

## Artifact specification template

```yaml
artifact:
  name: null
  artifact_type: null
  problem_class_addressed: null
  intended_users: []
  artifact_boundary:
    included: []
    excluded: []
  capacity_specification:
    - capacity: null
      success_indicator: null
  make_plan:
    steps: []
    required_resources: []
    maintenance_needs: []
    conformance_checks: []
  use_plan:
    user_roles: []
    use_context: null
    use_steps: []
    expected_user_behaviors: []
  claims:
    make_claim: null
    use_claim: null
    usage_effect_claim: null
  boundary_conditions: []
  trace:
    requirements_addressed: []
    design_decisions: []
    unresolved_risks: []
```

---

# Phase 8. Run safe-to-fail experiments

## Goal

Test the intervention without committing to a large irreversible reform.

## Actions

1. Select a small pilot context.
2. Define success, partial success, failure, and harmful side effects.
3. Implement the smallest useful version of the artifact.
4. Collect evidence from multiple angles: performance, user experience, stakeholder acceptance, unintended consequences, cost, and sustainability.
5. Decide whether to preserve, revise, scale, combine, or abandon the intervention.

## Pilot scope record

```yaml
pilot:
  pilot_name: null
  scope: null
  participating_stakeholders: []
  intervention_version: null
  duration: null
  assumptions_being_tested: []
  success_thresholds: []
  partial_success_thresholds: []
  failure_thresholds: []
  harm_or_burden_thresholds: []
  rollback_plan: null
```

## Evaluation matrix

| Claim | Evidence needed | Method | Timing | Stakeholder | Decision rule |
|---|---|---|---|---|---|
| The artifact can be built reliably | Build/conformance evidence | Inspection, walkthrough, test | Ex ante or formative | Implementer | Revise if core capacity is absent |
| Users can use it as intended | Use evidence | Pilot, observation, usability test | Ex post or formative | Users | Revise if workarounds dominate |
| It improves the target condition | Effect evidence | Metrics, comparison, case evidence | Ex post or summative | Beneficiaries/sponsors | Scale only if benefit exceeds burden |

---

# Phase 9. Evaluate claim-evidence alignment

## Goal

Determine which claims are supported, unsupported, overclaimed, or context-dependent.

## Actions

1. Link every evaluation result to a specific claim.
2. Identify unsupported claims.
3. Identify context-dependent findings.
4. Identify unintended consequences and stakeholder burdens.
5. Decide whether the intervention is effective, promising, inconclusive, harmful, or overclaimed.

## Claim-evidence matrix

```yaml
claim_evidence_matrix:
  claims:
    - claim_id: null
      claim_type: null # make_claim | use_claim | usage_effect_claim | contribution_claim
      claim_text: null
      evidence:
        - evidence_id: null
          evidence_type: null
          method: null
          result_summary: null
          supports_claim: null # yes | partially | no | unclear
          limitations: []
      boundary_conditions: []
      judgment: null # effective | promising | inconclusive | harmful | overclaimed
```

## Judgment categories

| Category | Meaning |
|---|---|
| Effective | Evidence supports use under stated conditions |
| Promising | Some evidence supports continued iteration |
| Inconclusive | Evidence is insufficient or mixed |
| Harmful | Intervention worsens key outcomes or burdens stakeholders |
| Overclaimed | Evidence supports a narrower claim than originally stated |

---

# Phase 10. Codify design knowledge

## Goal

Convert local intervention learning into reusable design knowledge.

## Actions

1. State what was learned about the problem class.
2. State what was learned about the artifact or intervention.
3. State what worked, for whom, why, and under what conditions.
4. State what did not work and why.
5. Package the reusable knowledge for future projects.

## Design principle template

```text
For [problem class] in [context/boundary conditions],
use/design [artifact or intervention feature],
because it enables [mechanism/capacity],
which tends to produce [intended outcome],
provided that [conditions/constraints] hold.
```

## Design knowledge record

```yaml
design_knowledge_record:
  knowledge_id: null
  knowledge_type: null # design_principle | design_pattern | design_theory_element | negative_design_knowledge | evaluation_finding
  problem_class: null
  context_or_boundary_conditions: []
  artifact_or_intervention_feature: null
  mechanism_or_rationale: null
  intended_outcome: null
  evidence_basis: []
  limitations: []
  transferability_notes: null
  related_artifacts: []
  contribution_claim: null
```

---

# Phase 11. Institutionalize, scale, or reframe

## Goal

Decide what to do with the intervention and what cycle should follow.

## Actions

1. Decide whether to scale, modify, pause, or abandon.
2. Define governance and maintenance responsibilities.
3. Update policies, templates, training, systems, or documentation.
4. Monitor whether the problem mutates.
5. Re-enter the workflow if the problem changes.

## Scale/reframe decision record

```yaml
scale_reframe_decision:
  decision: null # scale | revise | pause | abandon | reframe | combine_with_other_intervention
  decision_rationale: null
  evidence_basis: []
  stakeholder_implications: []
  maintenance_owner: null
  governance_changes_needed: []
  documentation_updates_needed: []
  monitoring_plan: null
  next_cycle_trigger: null
```

## Stopping rule

Stop the current cycle when the intervention is good enough to preserve, scale, revise, or abandon under explicit evidence and boundary conditions. Do not stop merely because the wicked problem appears temporarily quiet.

---

# Weekly cadence

| Week | Focus | Main artifact |
|---|---|---|
| Week 1 | Situation, stakeholders, context | Problem/context brief |
| Week 2 | Problem instance/class and causal model | Problem-class and causal map |
| Week 3 | Objectives, requirements, solution search | Requirement and solution matrix |
| Week 4 | Artifact/intervention design | Artifact specification |
| Week 5 | Pilot/evaluation setup | Evaluation protocol |
| Week 6 | Safe-to-fail implementation | Pilot evidence |
| Week 7 | Evaluation and learning | Claim-evidence matrix |
| Week 8 | Codification and next decision | Design knowledge record and scale/reframe decision |

After Week 8, either scale, revise, abandon, or reframe and begin another cycle.

---

# Anti-pattern checks

| Anti-pattern | Diagnostic question | Corrective action |
|---|---|---|
| Premature solutioning | Did the team choose a solution before modeling the problem? | Return to causal modeling and requirements derivation. |
| Stakeholder flattening | Did the team treat stakeholders as one group with one interest? | Split stakeholders by role, burden, authority, and incentives. |
| Localism | Is the team only fixing a local symptom without abstracting the problem class? | Write the problem instance/class distinction explicitly. |
| Overabstraction | Is the problem class too broad to guide action? | Add boundary conditions and concrete examples. |
| Artifact black box | Has the team specified how the intervention works? | Add make plan, use plan, capacity specification, and design rationale. |
| Evaluation mismatch | Does the evidence actually test the claim? | Rebuild the claim-evidence matrix. |
| Success theater | Is the team collecting favorable evidence while ignoring burden or side effects? | Add unintended-consequence and stakeholder-burden tracking. |
| Missing boundary conditions | Is the team implying generality without specifying where findings apply? | Add contextual and transferability limits. |
| No knowledge capture | Did the team solve locally without producing reusable design knowledge? | Create a design knowledge record. |
| Transparency overload | Is documentation too large to use? | Separate minimum required trace from optional supporting evidence. |

---

# Minimal GitHub issue template

Use this when opening an issue for a wicked problem cycle.

```markdown
## Problem situation

## Why this may be wicked

- [ ] Contested definition
- [ ] Stakeholder conflict
- [ ] Circular causality
- [ ] No obvious stopping rule
- [ ] High side-effect risk
- [ ] Context-dependent success criteria

## Problem instance

## Candidate problem class

## Stakeholders affected

## Known constraints

## Candidate leverage points

## Proposed next artifact

## Evidence needed

## Boundary conditions

## Open questions
```

---

# Minimum pull request checklist

Before merging a wicked-problem workflow artifact, confirm:

- [ ] The problem instance is stated.
- [ ] The problem class is stated.
- [ ] Stakeholders and context are documented.
- [ ] Requirements trace back to problem factors or stakeholder needs.
- [ ] The intervention is specified as an artifact or design entity.
- [ ] Make plan, use plan, and capacity specification are included when applicable.
- [ ] Evaluation criteria are linked to claims.
- [ ] Boundary conditions are explicit.
- [ ] Design knowledge or negative design knowledge is captured.
- [ ] The next decision is scale, revise, pause, abandon, or reframe.

---

# Suggested repository placement

Recommended default location:

```text
docs/wicked-problem-resolution-workflow.md
```

If this is treated as a reusable DSR artifact rather than only documentation, place a copy or companion record under:

```text
artifacts/process/wicked-problem-resolution-workflow.md
```

Suggested companion files:

```text
artifacts/templates/problem-abstraction.yaml
artifacts/templates/artifact-specification.yaml
artifacts/templates/evaluation-protocol.yaml
artifacts/templates/design-knowledge-record.yaml
.github/ISSUE_TEMPLATE/wicked_problem_cycle.md
.github/pull_request_template.md
```

---

# Maintenance notes

- Keep this file stable as a process artifact.
- Put project-specific applications in separate artifact records.
- Treat each application as a new cycle with its own evidence and boundary conditions.
- Revise this workflow only when repeated cycles show that a phase, template, or checklist is missing, misleading, or too burdensome.
