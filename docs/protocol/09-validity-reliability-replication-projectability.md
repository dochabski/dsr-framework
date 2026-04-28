<!-- SPDX-License-Identifier: CC0-1.0 -->

# Validity, Reliability, Replication, and Projectability in DSR

## Controlled source links

- [models/dsr-reliability-model.yaml](../../models/dsr-reliability-model.yaml)
- [models/dsr-projectability-model.yaml](../../models/dsr-projectability-model.yaml)
- [vocabularies/validity-types.yaml](../../vocabularies/validity-types.yaml)
- [vocabularies/reliability-types.yaml](../../vocabularies/reliability-types.yaml)
- [vocabularies/replication-types.yaml](../../vocabularies/replication-types.yaml)
- [vocabularies/projectability-types.yaml](../../vocabularies/projectability-types.yaml)

```yaml
item_id: docs_validity_reliability
item_type: description
title: Validity, Reliability, Replication, and Projectability in Design Science Research
status: draft
version: "0.1.0"
owner: DSR Framework maintainers
source_basis:
  - dsr_framework_generation_spec
  - dsr_framework_generation_prompt
  - dsr_extraction_corpus
  - model_reliability
  - model_projectability
related_items:
  upstream:
    - models/dsr-reliability-model.yaml
    - models/dsr-projectability-model.yaml
    - models/dsr-evaluation-alignment-model.yaml
    - specs/product-dsr-quality-conformance-and-review-model.yaml
    - specs/product-dsr-lifecycle-and-contribution-model.yaml
  vocabularies:
    - vocabularies/validity-types.yaml
    - vocabularies/reliability-types.yaml
    - vocabularies/replication-types.yaml
    - vocabularies/projectability-types.yaml
    - vocabularies/evaluation-method-families.yaml
  operating_materials:
    - templates/evaluation-plan-template.yaml
    - templates/evaluation-report-template.yaml
    - templates/review-record-template.yaml
    - checklists/evaluation-readiness-checklist.yaml
    - checklists/reliability-checklist.yaml
    - checklists/replication-projectability-checklist.yaml
    - checklists/publication-readiness-checklist.yaml
change_history:
  - version: "0.1.0"
    date: "2026-04-27"
    change: Initial L2 reviewable documentation page generated for docs_validity_reliability.
```

## 1. Purpose

This page gives human-facing guidance for assessing and documenting **validity**, **reliability**, **replication**, and **projectability** in Design Science Research (DSR) artifact packages. It explains how these concepts work together in the DSR Framework and how they should be represented in plans, reports, reviews, checklists, and retained records.

This page is not the controlled vocabulary or executable validation source. It explains and renders the intended use of the controlled files listed above. Where there is a conflict, the structured model, vocabulary, schema, checklist, or conformance declaration is authoritative.

## 2. Scope and non-goals

This guide applies to DSR projects that create, adapt, evaluate, or report artifacts and design knowledge. It is intended for researchers, reviewers, maintainers, and practitioners who need to judge whether a DSR claim is adequately supported.

This guide does not require every project to prove universal generalization, exact reproducibility, or publication readiness. Many DSR artifacts are situated, emergent, socio-technical, and context-dependent. The goal is to make claims explicit, bounded, evidenced, and reviewable.

## 3. Core distinctions

| Construct | Operational question | Primary object of judgment | Typical evidence | Common failure mode |
|---|---|---|---|---|
| Validity | Is the claim warranted? | Artifact, design process, evaluation, inference, contribution, or context claim | Traceable requirements, design rationale, evaluation evidence, claim-evidence alignment, boundary conditions | Claims exceed evidence or ignore context |
| Reliability | Would the relevant result, method, measure, artifact behavior, or design knowledge be dependable under the stated conditions? | Artifact, method, measure, evaluator judgment, implementation, or design knowledge | Repeatable procedures, consistent measures, multiple observations, stable implementation behavior, diachronic evidence | Single observation is treated as stable evidence |
| Replication | Can the work be repeated, re-instantiated, re-evaluated, or conceptually re-tested? | Study procedure, artifact instance, artifact type, evaluation design, or design knowledge | Protocols, artifact specifications, datasets, code, environment notes, use conditions, comparison logic | Replication is reduced to copying an artifact without context |
| Projectability | Can the design knowledge be responsibly carried forward to a problem class, future case, adapted implementation, or cumulative research path? | Design principle, artifact universal, problem class, use plan, evaluation logic, contribution claim | Boundary conditions, transfer rationale, adaptation rules, problem-class definition, reusable design knowledge | A local success is reported as generalizable without qualification |

## 4. Relationship among the constructs

The DSR Framework treats validity, reliability, replication, and projectability as linked but non-identical review dimensions.

1. **Validity** asks whether a claim is supported.
2. **Reliability** asks whether the relevant artifact behavior, research method, evaluation measure, or design knowledge is dependable enough for that claim.
3. **Replication** asks whether another actor can repeat, reinstantiate, retest, or conceptually re-evaluate the work.
4. **Projectability** asks whether the knowledge can be carried beyond the original case in a bounded, documented, and useful way.

Reliability often strengthens validity, and both strengthen projectability. Replication may strengthen all three, but exact replication is not always the relevant target in DSR. In many DSR studies, the more appropriate target is **differentiated replication**, **artifact replication**, or **conceptual replication** that preserves the design logic while making context differences explicit.

## 5. Validity guidance

Validity should be specified at the level of the claim being made. A DSR package should not report validity as a single undifferentiated property of the whole project. It should indicate which kind of validity is being claimed and what evidence supports it.

| Validity focus | Use when | Evidence to document | Reviewer check |
|---|---|---|---|
| Problem-space validity | The project claims to address a real, important, bounded problem | Stakeholder evidence, problem class, context description, improvement goals, constraints | Is the problem real, bounded, and suitable for DSR? |
| Construct or semantic validity | The project defines constructs, artifact components, variables, roles, or evaluation concepts | Definitions, controlled vocabulary, literature grounding, concept maps, coding rules | Are terms stable and distinguishable from neighboring concepts? |
| Artifact validity | The artifact is claimed to perform a function or satisfy requirements | Artifact specification, requirements traceability, conformance tests, demonstration and evaluation records | Does the artifact satisfy its stated functional and quality requirements? |
| Design-specification validity | The project claims reusable design knowledge, not only a local build | Make plan, use plan, design principles, design rationale, artifact boundary, capacity or mechanism claims | Is the reusable design specification clear enough to instantiate or adapt? |
| Procedural validity | The project claims the process was rigorous or methodologically sound | Lifecycle records, decision logs, design rationale, evaluation plan, deviations and mitigations | Is the research process visible and justified? |
| Evaluation validity | The project claims the evaluation supports utility, quality, efficacy, or contribution | Evaluation questions, criteria, methods, data, analysis logic, limitations | Does the method fit the evaluation question and claim? |
| Context or ecological validity | The project claims applicability in real or realistic settings | User roles, setting, implementation conditions, constraints, environmental assumptions | Are real-use conditions represented or clearly bounded? |
| External validity or projectability validity | The project claims relevance beyond the immediate case | Problem-class definition, boundary conditions, adaptation logic, cross-case evidence | Is transfer bounded and supported rather than asserted? |
| Contribution validity | The project claims a scholarly or practical contribution | Contribution positioning record, novelty rationale, relation to prior work, audience-specific value | Is the contribution distinct, useful, and traceable to evidence? |

### Minimum validity documentation

At L2 reviewable conformance, a DSR package should document:

- the claim being made;
- the unit of analysis or artifact object to which the claim applies;
- the evidence supporting the claim;
- the context in which the claim holds;
- the limitations, threats, and unresolved questions;
- the connection between validity evidence and evaluation criteria.

A claim should be weakened, scoped, or deferred when evidence is illustrative, conceptual, single-case, incomplete, or not yet independently reviewed.

## 6. Reliability guidance

Reliability in DSR is broader than measurement consistency. It can apply to artifacts, methods, measures, evaluators, implementations, and design knowledge. The DSR Framework distinguishes reliability targets and reliability time horizons.

### 6.1 Reliability targets

| Reliability target | Operational meaning | Evidence examples |
|---|---|---|
| Artifact reliability | The artifact performs dependably under stated use conditions | Repeated tests, robustness checks, error logs, performance stability, fault handling, environmental constraints |
| Method reliability | The research or design method can be followed consistently enough to support trustworthy outputs | Step definitions, procedure records, decision logs, reviewer replication of method application, method tailoring rationale |
| Measure reliability | The evaluation measures produce stable or consistent observations | Instrument definitions, coding protocols, calibration, multiple observations, inter-rater checks, test-retest evidence |
| Evaluator reliability | Multiple reviewers, coders, or evaluators can make compatible judgments | Rubrics, scoring guidance, adjudication records, agreement summaries, reviewer training notes |
| Implementation reliability | The artifact can be deployed, configured, operated, or maintained consistently enough for the intended context | Installation steps, dependencies, configuration files, operating constraints, known failure modes, maintenance notes |
| Design-knowledge reliability | The design principle, pattern, model, or specification remains useful under stated future or cross-context conditions | Problem-class boundaries, adaptation rules, cross-case evaluation, longitudinal evidence, successful re-instantiation |

### 6.2 Reliability time horizons

| Time horizon | Meaning | Appropriate evidence |
|---|---|---|
| Synchronic reliability | Dependability at one point in time or within the same evaluation moment | Multiple observers, triangulation, repeated trials in the same setting, consistent scoring, internal robustness checks |
| Diachronic reliability | Dependability across time, versions, settings, or knowledge moments | Longitudinal evaluation, versioned records, maintenance logs, retesting after change, cross-context re-use evidence |

A project may be synchronically reliable but not yet diachronically reliable. For example, an artifact may perform consistently during one controlled evaluation but lack evidence across versions, environments, or real-use cycles.

### 6.3 Reliability documentation requirements

At L2 reviewable conformance, reliability documentation should answer:

1. What must be reliable for the claim to hold?
2. Under what conditions is reliability being asserted?
3. Is reliability synchronic, diachronic, or both?
4. What evidence supports reliability?
5. What reliability threats remain?
6. How does reliability evidence support validity, replication, or projectability?

## 7. Replication guidance

Replication in DSR should be tied to the nature of the artifact and the knowledge claim. Exact duplication of a socio-technical intervention may be impossible or uninformative when the intervention changes the environment. The package should therefore specify the intended replication mode.

| Replication mode | Use when | Required documentation |
|---|---|---|
| Procedural replication | Another researcher should be able to follow the same research or evaluation procedure | Protocol steps, inputs, outputs, tailoring decisions, analysis rules, review records |
| Artifact replication | Another actor should be able to rebuild, reinstantiate, configure, or deploy the artifact | Artifact specification, dependencies, installation steps, make plan, test data, environment notes |
| Evaluation replication | Another evaluator should be able to repeat or approximate the evaluation logic | Evaluation plan, metrics, instruments, data handling, criteria, baselines, limitations |
| Conceptual replication | Another project should test the same design principle, mechanism, or contribution claim in a new setting | Design principle statement, problem-class definition, mechanism rationale, boundary conditions |
| Differentiated replication | Another study should preserve the design logic while explicitly varying context, implementation, users, or conditions | Variation rationale, invariant design elements, changed conditions, expected impact of differences |
| No replication claim | The project does not yet claim replicability | Explanation of limitation, what is missing, future evidence needed |

Replication claims should not be treated as binary. They should be scoped by artifact maturity, disclosure constraints, context specificity, data availability, and maintenance burden.

## 8. Projectability guidance

Projectability is the capacity of a DSR output to inform future work beyond the immediate local instance. It includes but is not limited to generalization. A projectable contribution may support adaptation, reuse, transfer, cumulative research, reviewer comparison, teaching, or practitioner implementation.

### 8.1 Projectability objects

| Projectability object | Description | Example evidence |
|---|---|---|
| Problem class | The class of problems to which the design knowledge may apply | Problem-class definition, inclusion and exclusion boundaries, stakeholder classes |
| Artifact type or universal | The reusable artifact specification beyond one artifact instance | Make plan, use plan, capacity specification, components, variation points |
| Design principle | A prescriptive statement linking context, intervention, mechanism, and expected outcome | Design principle table, rationale, evaluation evidence, boundary conditions |
| Method or process model | A reusable way of conducting, evaluating, or documenting DSR | Procedure, roles, inputs, outputs, tailoring rules, quality gates |
| Evaluation logic | A reusable approach for judging artifact utility, quality, or contribution | Criteria, metrics, evidence standards, validity threats, reviewer guidance |
| Repository package | A reusable set of files enabling inspection, adaptation, citation, or extension | Manifest, metadata, templates, schemas, records, examples, license |

### 8.2 Projectability levels

| Level | Description | Appropriate wording |
|---|---|---|
| Local utility | Evidence supports usefulness in the studied context only | "Supported in this case under these conditions" |
| Bounded transferability | Evidence and rationale support use in similar contexts | "May transfer to contexts sharing these boundary conditions" |
| Problem-class projectability | Evidence supports a class of related problems | "Projectable to this problem class, with adaptation" |
| Design-knowledge accumulation | Evidence contributes to a reusable body of DSR knowledge | "Extends, refines, or challenges existing design knowledge" |
| Broad generalization | Evidence supports broad use across diverse contexts | Use only with strong cross-context evidence |

## 9. Evidence alignment workflow

Use this workflow when planning or reviewing a DSR package.

1. **Identify the claim.** Write the artifact, evaluation, reliability, replication, or projectability claim in one sentence.
2. **Classify the claim.** Determine whether the claim concerns utility, quality, validity, reliability, replication, projectability, or contribution.
3. **Identify the claim object.** Specify whether the object is an artifact instance, artifact type, method, measure, design principle, problem class, evaluation result, or contribution claim.
4. **Select evidence.** Link the claim to the evaluation plan, evaluation report, artifact specification, design rationale, transparency record, or review record.
5. **Assess reliability.** Determine whether artifact, method, measure, evaluator, implementation, or design-knowledge reliability is needed.
6. **Assess validity.** Determine whether the evidence warrants the claim and whether limitations are explicit.
7. **Assess replication.** State which replication mode is supported or not supported.
8. **Assess projectability.** State the level of transfer, adaptation, or accumulation justified by the evidence.
9. **Record limitations.** Preserve unresolved threats, failed checks, and future evidence needs.
10. **Update the package.** Revise related templates, checklists, records, or package inventory entries if evidence changes.

## 10. Claim-evidence matrix

A DSR evaluation report should include or link to a matrix like the following.

| Claim ID | Claim text | Claim object | Validity focus | Reliability target | Replication mode | Projectability level | Evidence record | Status |
|---|---|---|---|---|---|---|---|---|
| TODO: claim_id | TODO: claim text | TODO: artifact/method/measure/design knowledge | TODO | TODO | TODO | TODO | TODO: record path | draft |

## 11. Threats and mitigations

| Threat | Why it matters in DSR | Mitigation |
|---|---|---|
| Local success overclaimed as general design knowledge | DSR often begins with a situated artifact or intervention | State problem-class boundaries and distinguish local utility from projectability |
| Demonstration treated as evaluation | A working example does not necessarily test utility, quality, or contribution | Label demonstration and evaluation separately and document evaluation criteria |
| Artifact instance confused with artifact type | A deployed system may not itself be reusable design knowledge | Document artifact universal/type, make plan, use plan, and variation points |
| Measures treated as reliable without evidence | Unstable instruments weaken validity claims | Provide calibration, repeated measurement, inter-rater checks, or limitations |
| Artificial evaluation overextended to naturalistic contexts | Controlled settings may omit users, constraints, and organizational dynamics | Use ecological validity checks or scope claims to artificial evaluation |
| Context differences ignored in replication | Reuse may fail when environment, stakeholders, technology, or governance differs | Document context, boundary conditions, and differentiated replication logic |
| Diachronic drift ignored | Artifacts, problem spaces, users, and technologies change over time | Version artifacts, preserve change history, and re-evaluate after material changes |
| Proprietary or sensitive materials withheld without substitute evidence | Reviewers may be unable to assess claims | Provide redacted evidence, pseudocode, screenshots, summarized logs, or access-controlled records |

## 12. Review checklist for this guide

Use these checks when reviewing a DSR package against this guidance.

| Check ID | Question | Pass condition | If failed |
|---|---|---|---|
| vrp_01 | Are validity claims separated by claim type and evidence object? | Each major claim has a validity focus and linked evidence | Split broad claims and add claim-evidence records |
| vrp_02 | Are reliability targets identified where needed? | Artifact, method, measure, evaluator, implementation, or design-knowledge reliability is specified | Add reliability target mapping |
| vrp_03 | Are synchronic and diachronic reliability distinguished? | Time horizon is explicit or not applicable with rationale | Add time-horizon note and evidence |
| vrp_04 | Is replication mode specified? | Procedural, artifact, evaluation, conceptual, differentiated, or no replication claim is declared | Add replication classification |
| vrp_05 | Is projectability bounded? | Transfer or generalization claims identify problem class and boundary conditions | Narrow the claim or add evidence |
| vrp_06 | Are demonstration and evaluation distinct? | Demonstration records do not substitute for evaluation reports unless justified | Add evaluation plan/report or relabel claim |
| vrp_07 | Are limitations visible? | Threats, constraints, and missing evidence are documented | Add limitations and future evidence needs |
| vrp_08 | Are package records traceable? | Claims link to templates, reports, reviews, or records | Add traceability links |

## 13. Acceptance criteria

This documentation page is acceptable for L2 reviewable conformance when:

- it identifies the controlled files it explains;
- it distinguishes validity, reliability, replication, and projectability;
- it provides operational review questions and evidence expectations;
- it supports the DSR distinctions between artifact instance, artifact type, design knowledge, demonstration, and evaluation;
- it avoids unsupported claims of full reproducibility, universal generalization, or archival publication readiness;
- it includes limitations and review checks that allow another reviewer to evaluate the page.

## 14. Limitations and open questions

This page is an explanatory guide. The structured reliability model, projectability model, vocabularies, checklists, and schemas remain the proper source for controlled validation. Open issues for future versions include:

- harmonizing validity vocabulary with the final quality and conformance model;
- aligning replication modes with repository packaging and automation checks;
- adding examples from completed DSR Framework example packages;
- defining scoring levels for reviewer use without turning projectability into an overgeneralization metric;
- determining whether publication-ready L4 or L5 conformance should require stronger diachronic evidence.
<!-- BEGIN GENERATED LITERATURE TRACE ANCHORS -->

## Literature Trace Anchors

```yaml
source_basis:
- source_id: reining_ahlemann_mueller_thakurta_2022_knowledge_accumulation_dsr
  short_citation: Reining et al. (2022)
  evidence_anchor_id: A10
  supports_construct: validity_reliability.critique_or_gap_analysis
  evidence_role: validity
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/09-validity-reliability-replication-projectability.md
  note: 'Reining et al. (2022) grounds validity_reliability.critique_or_gap_analysis through extracted anchor A10: Four quality
    criteria for cumulative Design Science Research mapped to an evolutionary scientific-progress process model: relevance,
    balancing novelty and reuse, testability, and usefulness.'
- source_id: siponen_klaavuniemi_2021_primary_scientific_contribution
  short_citation: Siponen & Klaavuniemi (2021)
  evidence_anchor_id: A14
  supports_construct: validity_reliability.critique_or_gap_analysis
  evidence_role: validity
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/09-validity-reliability-replication-projectability.md
  note: 'Siponen & Klaavuniemi (2021) grounds validity_reliability.critique_or_gap_analysis through extracted anchor A14:
    Challenges the consensus-like expectation that Design Science Research''s primary scientific contribution should be new
    theory.'
- source_id: storey_baskerville_2021_digital_science_field_dsr
  short_citation: Storey & Baskerville, 2021
  evidence_anchor_id: CA10
  supports_construct: validity_reliability.critique_or_gap_analysis
  evidence_role: validity
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/09-validity-reliability-replication-projectability.md
  note: 'Storey & Baskerville, 2021 grounds validity_reliability.critique_or_gap_analysis through extracted anchor CA10: Extends
    the DSR consensus paradigm into digital science by arguing that scientific digital artifact production should be treated
    as theory-driven, verifiable design science.'
- source_id: iivari_2020_critical_look_theories_dsr
  short_citation: Iivari (2020)
  evidence_anchor_id: A8
  supports_construct: validity_reliability.critique_or_gap_analysis
  evidence_role: validity
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/09-validity-reliability-replication-projectability.md
  note: 'Iivari (2020) grounds validity_reliability.critique_or_gap_analysis through extracted anchor A8: Clarifies and critiques
    design theory, kernel theory, and substantive technological theory in DSRIS.'
- source_id: storey_baskerville_kaul_2025_reliability_in_design_science_research
  short_citation: Storey et al. (2025)
  evidence_anchor_id: A011
  supports_construct: validity_reliability.reliability_framework
  evidence_role: validity
  grounding_decision: adopted
  evidence_status: substantive
  target_path: docs/protocol/09-validity-reliability-replication-projectability.md
  note: 'Storey et al. (2025) grounds validity_reliability.reliability_framework through extracted anchor A011: A multidimensional
    framework for assessing reliability in DSR across artifact, method, measures, and design knowledge using synchronic and
    diachronic timing.'
```

<!-- END GENERATED LITERATURE TRACE ANCHORS -->
