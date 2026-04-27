<!-- SPDX-License-Identifier: CC0-1.0 -->
---
doc_id: docs_protocol_dsr_lifecycle_and_contribution_model
selection_id: docs_lifecycle_contribution
title: DSR Lifecycle and Contribution Model
status: draft
version: "0.1.0"
conformance_target: l2_reviewable
owner_role: dsr_framework_maintainer
target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
source_yaml:
  - specs/product-dsr-lifecycle-and-contribution-model.yaml
related_items:
  - models/dsr-lifecycle-model.yaml
  - models/dsr-contribution-model.yaml
  - models/dsr-artifact-ontology.yaml
  - models/dsr-evaluation-alignment-model.yaml
  - models/dsr-transparency-model.yaml
  - vocabularies/lifecycle-stages.yaml
  - vocabularies/artifact-types.yaml
  - vocabularies/contribution-types.yaml
  - vocabularies/knowledge-goals.yaml
  - vocabularies/knowledge-scopes.yaml
  - templates/dsr-project-charter-template.md
  - templates/problem-and-objectives-template.md
  - templates/artifact-specification-template.md
  - templates/contribution-claim-template.yaml
source_basis:
  - dsr_framework_generation_spec
  - dsr_framework_generation_prompt
  - dsr_extraction_corpus
  - documentation_protocol_repository_model
change_history:
  - version: "0.1.0"
    date: "2026-04-27"
    change: Initial L2 reviewable human-facing documentation page.
---

# DSR Lifecycle and Contribution Model

This page explains how the DSR Framework treats a Design Science Research project as both a **lifecycle of work** and a **contribution-producing argument**. It is a human-facing guide to the controlled lifecycle and contribution materials. The controlled source of truth should remain the related YAML specifications, models, vocabularies, templates, checklists, and records listed in the front matter.

## 1. Purpose

Use this guide to plan, document, review, and communicate a DSR project without collapsing it into ordinary consulting, implementation work, or behavioral explanation alone. A DSR project must show all three of the following:

1. a relevant problem or opportunity in a real or plausible use context;
2. an intentionally designed artifact, artifact type, method, model, framework, ontology, pattern, template, protocol, or instantiation; and
3. a contribution to reusable or projectable knowledge, supported by demonstration, evaluation, rationale, and transparent boundary conditions.

The lifecycle model gives the project an operating sequence. The contribution model explains why the work matters beyond the local build.

## 2. Relationship to controlled files

| Controlled file | Role in this page | Use when |
|---|---|---|
| `specs/product-dsr-lifecycle-and-contribution-model.yaml` | Governing source specification for lifecycle and contribution rules. | Maintaining or revising the controlled framework product. |
| `models/dsr-lifecycle-model.yaml` | Structured lifecycle stages, dependencies, outputs, and iteration rules. | Validating stage coverage or workflow completeness. |
| `models/dsr-contribution-model.yaml` | Controlled contribution-positioning structure. | Classifying what kind of knowledge claim the project makes. |
| `models/dsr-artifact-ontology.yaml` | Boundary model for artifacts, artifact instances, artifact universals, make plans, use plans, capacities, and contexts. | Distinguishing an artifact from a local system, implementation, theory, or intervention alone. |
| `models/dsr-evaluation-alignment-model.yaml` | Alignment among objectives, artifact claims, demonstration, evaluation, and contribution claims. | Checking whether evidence supports claims. |
| `models/dsr-transparency-model.yaml` | Six transparency dimensions applied across the lifecycle. | Checking whether the project is reviewable and reusable. |
| `vocabularies/lifecycle-stages.yaml` | Controlled lifecycle stage names and definitions. | Normalizing repository records and templates. |
| `vocabularies/contribution-types.yaml` | Controlled contribution-type vocabulary. | Positioning novelty and significance. |
| `vocabularies/knowledge-goals.yaml` | Knowledge-goal vocabulary. | Distinguishing definitional, descriptive, explanatory, predictive, prescriptive, methodological, evaluative, or normative claims. |
| `vocabularies/knowledge-scopes.yaml` | Knowledge-scope vocabulary. | Distinguishing local, idiographic, projectable, mixed, or nomothetic claims. |
| `templates/contribution-claim-template.yaml` | Reusable contribution claim record structure. | Recording the final contribution argument. |

This Markdown page may summarize and explain these materials, but it should not replace them.

## 3. Core lifecycle logic

The lifecycle is intentionally iterative. Stages are ordered enough to support review and traceability, but a DSR project may move backward when problem understanding, artifact design, demonstration, evaluation, or contribution positioning changes.

| Stage | Primary question | Minimum output | Review focus |
|---|---|---|---|
| 1. Problem-space initiation | What real-world or scholarly problem class motivates the work? | Problem context, stakeholders, scope, improvement goal, constraints, and initial success criteria. | Relevance, boundedness, stakeholder grounding, and distinction from a merely local task. |
| 2. Objectives and requirements | What must a better artifact or design response accomplish? | Objectives, meta-requirements, acceptance criteria, design constraints, and trace links to the problem. | Whether objectives are specific enough to guide design and evaluation. |
| 3. Solution-space grounding | What existing knowledge, artifacts, technologies, or theories inform the design? | Literature, existing artifacts, design theories, standards, technical constraints, and gap analysis. | Rigor, non-duplication, grounding, and awareness of alternatives. |
| 4. Contribution positioning | What kind of contribution is anticipated? | Initial contribution type, knowledge goal, knowledge scope, artifact type, and novelty rationale. | Whether the project has a plausible research contribution, not only a delivery goal. |
| 5. Artifact design and specification | What is being designed, and what is its intended form and function? | Artifact specification, make plan, use plan, components, design rationale, and boundary conditions. | Internal coherence among problem, requirements, artifact form, and intended use. |
| 6. Build or instantiation | How is the artifact made, represented, configured, or operationalized? | Prototype, model, method, framework, ontology, template, protocol, software, implementation record, or other instantiation evidence. | Build transparency, versioning, reproducibility of construction logic, and design-decision traceability. |
| 7. Demonstration | Can the artifact be used or applied to a relevant case or scenario? | Demonstration record, use scenario, walkthrough, proof of concept, example package, or application evidence. | Feasibility, intelligibility, and fit between artifact and intended use context. |
| 8. Evaluation | How well does the artifact satisfy its objectives and claims? | Evaluation plan, evaluation report, criteria, data or observations, analysis, results, and limitations. | Alignment among evaluation criteria, artifact claims, context, methods, and evidence strength. |
| 9. Contribution synthesis | What knowledge claim is justified after design, demonstration, and evaluation? | Contribution claim, limitations, boundary conditions, comparison to prior work, and projectability statement. | Whether the claim is proportionate to evidence and properly scoped. |
| 10. Communication and packaging | How will the artifact and knowledge be communicated, reused, and reviewed? | Documentation package, metadata, inventory, transparency crosswalk, review records, and release materials. | Repository completeness, reviewability, reuse support, and scholarly/practitioner communication. |
| 11. Iteration and accumulation | What should be refined, replicated, adapted, or extended? | Open questions, backlog, version plan, replication/projectability notes, and successor records. | Whether the project supports cumulative design knowledge rather than a one-off result. |

## 4. Iteration rules

Iteration should be explicit rather than hidden. A project should record a return to an earlier stage when any of the following occurs:

| Iteration trigger | Return to | Record evidence |
|---|---|---|
| The problem is too broad, too narrow, or insufficiently grounded. | Problem-space initiation. | Problem revision note, stakeholder/context evidence, scope change. |
| Objectives do not operationalize the problem or are not evaluable. | Objectives and requirements. | Revised requirements, acceptance criteria, rationale. |
| Existing knowledge or artifacts already solve the problem or change the design space. | Solution-space grounding. | Literature update, prior-art comparison, design alternative record. |
| The expected contribution is routine, unsupported, or misclassified. | Contribution positioning. | Contribution-positioning update and novelty assessment. |
| The artifact design no longer fits requirements, constraints, or use context. | Artifact design and specification. | Design decision record and updated artifact specification. |
| The build reveals infeasibility, hidden assumptions, or implementation drift. | Build or artifact design. | Build transparency record, issue log, design change. |
| Demonstration shows the artifact cannot be meaningfully applied. | Artifact design, requirements, or problem-space stage. | Demonstration record, failure analysis, revised use scenario. |
| Evaluation evidence does not support the claim. | Evaluation plan, artifact design, objectives, or contribution positioning. | Evaluation report, claim revision, limitation statement. |
| Communication exposes missing documentation, unclear audience, or reuse barriers. | Communication and packaging. | Review record, package inventory update, documentation backlog. |

Iteration is not a weakness. It becomes a weakness only when it is invisible, unrecorded, or used to retrofit a research narrative after the fact.

## 5. Contribution model

A DSR contribution is a justified claim that the work adds useful, reviewable, and appropriately scoped knowledge. The contribution may be practical, methodological, theoretical, evaluative, or some combination of these, but it must be connected to the artifact and to evidence.

### 5.1 Contribution claim anatomy

A complete contribution claim should identify:

| Element | Guiding question | Typical evidence |
|---|---|---|
| Problem class | What type of problem or opportunity does the work address? | Problem record, stakeholder evidence, context description, literature gap. |
| Artifact or design object | What artifact type, design specification, method, model, framework, ontology, template, pattern, protocol, or instantiation is contributed? | Artifact specification, build record, repository files, design rationale. |
| Knowledge goal | What kind of knowledge is being claimed? | Controlled value from `vocabularies/knowledge-goals.yaml`. |
| Knowledge scope | How broadly may the knowledge apply? | Controlled value from `vocabularies/knowledge-scopes.yaml`; boundary conditions. |
| Novelty and significance | What is new or meaningfully improved? | Prior-art comparison, solution-space record, contribution-positioning record. |
| Mechanism or rationale | Why should the artifact work? | Design principles, kernel theory, causal or functional rationale, design theory. |
| Demonstration evidence | Can the artifact be applied or used? | Demonstration record, scenario, example, prototype walkthrough. |
| Evaluation evidence | How well does it work against criteria? | Evaluation plan and report, measures, observations, analysis, limitations. |
| Projectability | What can others reuse, adapt, replicate, or test? | Package inventory, reuse instructions, boundary conditions, replication/projectability notes. |

### 5.2 Knowledge goals

A contribution should not be labeled simply as "new knowledge." It should be classified by the type of knowledge it offers.

| Knowledge goal | Use when the project primarily contributes | Boundary note |
|---|---|---|
| Definitional | A clearer construct, class, term, ontology element, or conceptual distinction. | Do not use when the main contribution is only a named local artifact. |
| Descriptive | A documented account of a design situation, artifact behavior, process, or pattern. | Descriptive claims alone may not be sufficient for DSR unless connected to artifact design or use. |
| Explanatory | A rationale for why an artifact, mechanism, design choice, or context produces an effect. | Requires more than observed performance. |
| Predictive | A claim about expected artifact behavior or outcome under specified conditions. | Requires clear conditions and evaluable expectations. |
| Prescriptive | A design principle, method, guideline, template, pattern, protocol, or rule for action. | Must specify context and intended outcome. |
| Methodological | A contribution to how DSR is conducted, documented, evaluated, reviewed, or reused. | Should be distinguished from a domain artifact. |
| Evaluative | Evidence about artifact quality, utility, validity, reliability, or fit for use. | Should be tied to explicit criteria and claims. |
| Normative | A value-bearing or governance-oriented claim about what DSR should require or prioritize. | Should identify the value basis and limits. |

### 5.3 Knowledge scope

The scope of a DSR claim should be no broader than its evidence permits.

| Scope | Meaning | Acceptable claim form |
|---|---|---|
| Idiographic/local | Applies to one case, site, organization, project, or artifact instance. | "In this context, the artifact supported..." |
| Projectable to problem class | Applies plausibly to a bounded class of similar problems or contexts. | "For this type of problem, the artifact design suggests..." |
| Mixed | Combines local evidence with partially generalized design knowledge. | "This case supports a design principle that may transfer when..." |
| Nomothetic/general | Intended to apply broadly across a class of cases. | "Across this defined class, the model proposes..." |
| Not yet established | Evidence is insufficient to define scope. | "Scope is pending further demonstration or evaluation." |

## 6. Artifact and contribution distinctions

The lifecycle and contribution model requires several distinctions that should remain visible in records and documentation.

| Distinction | Meaning | Why it matters |
|---|---|---|
| Artifact instance vs. artifact type | A built prototype or implementation is not the same as the reusable design knowledge or artifact universal it instantiates. | Prevents overclaiming from one implementation. |
| Demonstration vs. evaluation | Demonstration shows that use is possible; evaluation judges performance, quality, utility, or effect against criteria. | Prevents proof-of-concept evidence from being overstated as full evaluation. |
| Artifact utility vs. artifact quality | Utility concerns problem-solving value; quality concerns properties such as correctness, usability, maintainability, validity, reliability, or transparency. | Supports claim-specific evidence. |
| Build process vs. design rationale | The build process records what was done; the rationale records why design decisions were made. | Supports transparency and reviewability. |
| Contribution to practice vs. contribution to knowledge | Practice impact concerns use; knowledge contribution concerns reusable or projectable understanding. | Prevents implementation success from being treated automatically as scholarly contribution. |
| Local relevance vs. projectability | A local problem can motivate DSR, but the resulting claim must define what can transfer or accumulate. | Supports reuse, replication, adaptation, and publication review. |

## 7. Lifecycle-to-transparency crosswalk

Every lifecycle stage should support at least one transparency dimension.

| Lifecycle area | Primary transparency dimension | Documentation expected |
|---|---|---|
| Problem-space initiation | Problem-space transparency | Context, stakeholders, goals, constraints, scope, boundary conditions. |
| Objectives and requirements | Problem-space and contribution transparency | Objectives, requirements, acceptance criteria, traceability to problem and claim. |
| Solution-space grounding | Solution-space transparency | Existing theories, artifacts, technologies, literature, alternatives, gap analysis. |
| Artifact design and build | Build transparency | Design decisions, build records, artifact specification, versions, make/use logic. |
| Demonstration and evaluation | Evaluation transparency | Demonstration scenarios, evaluation methods, criteria, results, limitations. |
| Contribution synthesis | Contribution transparency | Contribution claim, novelty, significance, scope, limitations, projectability. |
| Communication and packaging | Process and contribution transparency | Package inventory, metadata, review records, release notes, reuse guidance. |

## 8. Minimum reviewable evidence for L2

For L2 reviewable conformance, the lifecycle/contribution documentation should be sufficient for a reviewer to understand the project and identify what evidence exists or is missing.

| Evidence object | Required at L2? | Review note |
|---|---:|---|
| Problem and objectives record | Yes | Must define the problem class, stakeholders, scope, objectives, and success criteria. |
| Solution-space grounding record | Yes | Must show relevant prior knowledge and alternatives. |
| Artifact specification | Yes | Must describe the artifact boundary, components, make/use logic, and version. |
| Design rationale | Yes | Must justify major design choices and rejected alternatives. |
| Build transparency record | Yes, if artifact is built or instantiated | Must record how the artifact was made or operationalized. |
| Demonstration record | Yes, unless not yet applicable | Must show whether and how the artifact can be applied. |
| Evaluation plan | Yes | Must define criteria and evidence strategy. |
| Evaluation report | Required when evaluation has occurred | Must distinguish findings from claims and limitations. |
| Contribution claim | Yes | Must position contribution type, knowledge goal, knowledge scope, novelty, and evidence basis. |
| Transparency crosswalk | Yes | Must show coverage across process, problem, solution, build, evaluation, and contribution. |
| Package inventory | Yes | Must identify files, responsibilities, and validation status. |
| Review record | Yes | Must document review outcome and remediation items. |

## 9. Common failure modes

| Failure mode | Symptom | Remediation |
|---|---|---|
| Ex-post DSR framing | A completed implementation is retroactively described as research without prior problem, objectives, design rationale, or evaluation logic. | Reconstruct evidence honestly, label gaps, and avoid unsupported claims. |
| Routine design overclaim | The artifact is useful but not novel, theoretically relevant, methodologically useful, or projectable. | Reposition as a local implementation or identify a narrower contribution claim. |
| Evidence-claim mismatch | Evaluation evidence supports usability but the contribution claims general effectiveness or theory. | Reduce the claim scope or add appropriate evaluation evidence. |
| Demonstration treated as evaluation | A walkthrough, scenario, or prototype run is reported as if it established effectiveness. | Reclassify as demonstration and define a future evaluation plan. |
| Missing artifact boundary | The project describes a system, intervention, or process without specifying the artifact or design object. | Add artifact specification, make/use plan, components, and boundaries. |
| Unclear knowledge scope | The project does not state whether its claim is local, projectable, mixed, or general. | Add knowledge-scope classification and boundary conditions. |
| Hidden iteration | Major changes occur without records or rationale. | Add design decision records, change history, and iteration notes. |
| Practitioner-only communication | The package explains how to use the artifact but not what knowledge it contributes. | Add contribution-positioning and scholarly communication sections. |

## 10. Reviewer checklist for this page

A reviewer should be able to answer these questions after using the lifecycle and contribution model:

1. Can the DSR problem class, local problem instance, stakeholders, and desired improvement be identified?
2. Are objectives and requirements traceable to the problem and to evaluation criteria?
3. Is the solution space sufficiently grounded in prior theory, artifacts, methods, technologies, or standards?
4. Is the artifact type and boundary clear?
5. Are make plans, use plans, build decisions, and design rationales documented at a proportionate level?
6. Is demonstration separated from evaluation?
7. Do evaluation methods and criteria match the artifact claims?
8. Is the contribution type, knowledge goal, and knowledge scope explicitly classified?
9. Are novelty, significance, and projectability claims proportionate to evidence?
10. Are limitations, non-goals, and open questions visible enough for review and reuse?

## 11. Source-basis notes

This page is grounded in the internal DSR extraction corpus and the DSR Framework generation rules. The most directly relevant corpus source families include:

| Source family | Relevance to this page |
|---|---|
| Hevner et al. 2004 and related DSR consensus sources | Artifact creation, relevance/rigor, build/evaluate, and design knowledge. |
| Peffers et al. DSRM tradition | Problem identification, objectives, design/development, demonstration, evaluation, and communication sequence. |
| Gregor and Hevner contribution tradition | Contribution positioning, design knowledge, and communication of research contribution. |
| Weigand, Johannesson, and Andersson artifact ontology | Artifact type/instance distinction, make plan, use plan, capacities, and artifact boundary. |
| Akoka, Comyn-Wattiau, Prat, and Storey knowledge paths | Dynamic knowledge moments, contribution paths, knowledge goals, and knowledge scope. |
| Hevner et al. transparency framework | Process, problem-space, solution-space, build, evaluation, and contribution transparency. |
| Baskerville, Kaul, Pries-Heje, and Storey bounded creativity model | Iteration indicators and stage-specific return logic across the DSR lifecycle. |
| De Sordi DSRM synthesis | Operational six-phase DSRM, demonstration/evaluation distinction, artifact reuse, and communication to practitioner and scholarly audiences. |

## 12. Open questions and backlog

| ID | Open question | Proposed disposition |
|---|---|---|
| oq_lifecycle_stage_vocab_alignment | Should the controlled lifecycle vocabulary use the eleven-stage expanded model in this page or map it to a smaller six-stage DSRM backbone? | Resolve in `vocabularies/lifecycle-stages.yaml` and `models/dsr-lifecycle-model.yaml`. |
| oq_contribution_scope_granularity | Should `projectable_to_problem_class` remain a separate knowledge-scope value or be modeled as a subtype of mixed scope? | Resolve in `vocabularies/knowledge-scopes.yaml`. |
| oq_artifact_universal_language | Should the framework require the term artifact universal, or use a plainer phrase such as reusable artifact type? | Resolve in `models/dsr-artifact-ontology.yaml` and documentation style guidance. |
| oq_demonstration_threshold | What minimum evidence distinguishes a demonstration from a mere description? | Resolve in `models/dsr-evaluation-alignment-model.yaml` and the demonstration record template. |

## 13. Acceptance criteria

This documentation page is acceptable at L2 when:

- it identifies the controlled files it explains;
- it provides a usable lifecycle sequence without treating the sequence as rigidly linear;
- it distinguishes artifact design, build, demonstration, evaluation, and contribution synthesis;
- it classifies contribution by artifact type, contribution type, knowledge goal, and knowledge scope;
- it includes lifecycle-to-transparency mapping;
- it includes reviewable evidence expectations and common failure modes;
- it avoids overclaiming publication readiness, replication, or generalizability; and
- it preserves open questions where controlled vocabulary or model decisions remain unsettled.
<!-- BEGIN GENERATED LITERATURE TRACE ANCHORS -->

## Literature Trace Anchors

```yaml
source_basis:
- source_id: akoka_comyn_wattiau_prat_storey_2023_knowledge_contributions_in_dsr
  short_citation: Akoka et al. (2023)
  evidence_anchor_id: A07
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adopted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Akoka et al. (2023) grounds contribution_positioning.method_extension through extracted anchor A07: A dynamic, graph-based
    representation of DSR knowledge contributions plus seven strategies and four guidelines.'
- source_id: gregor_zwikael_2024_ijpm_102584
  short_citation: Gregor & Zwikael, 2024
  evidence_anchor_id: A28
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Gregor & Zwikael, 2024 grounds contribution_positioning.synthesis through extracted anchor A28: Domain-specific operationalization
    and reporting guidance for applying Design Science Research in project management.'
- source_id: bub_2018_integrated_method_digital_innovation_dsr
  short_citation: Bub (2018)
  evidence_anchor_id: CA-10
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Bub (2018) grounds contribution_positioning.method_extension through extracted anchor CA-10: Operational integration
    of stage-gate digital innovation management with Design Science Research stages in a situational method artifact.'
- source_id: suero_montero_kapinga_2019_dsr_strengthened
  short_citation: Suero Montero & Kapinga (2019)
  evidence_anchor_id: A07
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Suero Montero & Kapinga (2019) grounds contribution_positioning.method_extension through extracted anchor A07: Extension
    of Design Science Research methodology by embedding co-creation and co-design throughout the design cycle for Information
    and Communication Technologies for Development.'
- source_id: baskerville_kaul_priesheje_storey_2019_inducing_creativity
  short_citation: Baskerville et al. 2019
  evidence_anchor_id: A8
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Baskerville et al. 2019 grounds contribution_positioning.method_extension through extracted anchor A8: Provides operational
    iteration indicators for Design Science Research based on bounded creativity and bounded rationality.'
- source_id: baskerville_kaul_priesheje_storey_2019_inducing_creativity_dsr
  short_citation: Baskerville et al. (2019)
  evidence_anchor_id: A10
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Baskerville et al. (2019) grounds contribution_positioning.method_extension through extracted anchor A10: >.'
- source_id: mullarkey_hevner_gill_dutta_2019_citizen_data_scientist
  short_citation: Mullarkey et al. (2019)
  evidence_anchor_id: A16
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Mullarkey et al. (2019) grounds contribution_positioning.method_extension through extracted anchor A16: Operationalizes
    elaborated Action Design Research as a staged, iterative, artifact-centered method for citizen-led data science projects.'
- source_id: maedche_gregor_morana_feine_2019_problem_space_dsr
  short_citation: Maedche et al. (2019)
  evidence_anchor_id: A09
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Maedche et al. (2019) grounds contribution_positioning.method_extension through extracted anchor A09: Refines Design
    Science Research methodology by operationalizing the problem space through stakeholders, needs, goals, and requirements.'
- source_id: van_der_merwe_gerber_smuts_2020_guidelines_conducting_dsr
  short_citation: van der Merwe et al. (2020)
  evidence_anchor_id: CA04
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'van der Merwe et al. (2020) grounds contribution_positioning.synthesis through extracted anchor CA04: Novice-oriented
    synthesis of DSR themes, guidelines, seminal works, process models, evaluation references, and reporting guidance.'
- source_id: vom_brocke_hevner_maedche_2020_design_science_research_cases
  short_citation: vom Brocke, Hevner, and Maedche (2020)
  evidence_anchor_id: A12
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'vom Brocke, Hevner, and Maedche (2020) grounds contribution_positioning.synthesis through extracted anchor A12: Operational
    synthesis of DSR concepts and case documentation structure for planning, conducting, evaluating, and communicating DSR
    projects.'
- source_id: johannesson_perjons_2021_intro_design_science_2e
  short_citation: Johannesson & Perjons (2021)
  evidence_anchor_id: A12
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Johannesson & Perjons (2021) grounds contribution_positioning.synthesis through extracted anchor A12: Operational
    five-activity Design Science Research method framework with artifact, evaluation, reporting, and ethics guidance.'
- source_id: johannesson_perjons_2021_ch11
  short_citation: Johannesson and Perjons 2021
  evidence_anchor_id: A04
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Johannesson and Perjons 2021 grounds contribution_positioning.method_extension through extracted anchor A04: Clarifies
    that DSR framework activities are logically ordered by input-output dependencies rather than temporally ordered like waterfall
    phases.'
- source_id: '9783030821562'
  short_citation: De Sordi 2021
  evidence_anchor_id: A020
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'De Sordi 2021 grounds contribution_positioning.synthesis through extracted anchor A020: Operational synthesis of
    DSR concepts, artifact types, process phases, evaluation criteria, and theory-development logic from artifacts.'
- source_id: purao_2021_dsr_problems_where_do_they_come_from
  short_citation: Purao (2021)
  evidence_anchor_id: A20
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Purao (2021) grounds contribution_positioning.method_extension through extracted anchor A20: A phase-based approach
    for identifying and developing DSR research problems, with emphasis on practice-generated problems, problem-class abstraction,
    research-front positioning....'
- source_id: hevner_storey_2021_externalities_dsr
  short_citation: Hevner & Storey, 2021
  evidence_anchor_id: A18
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Hevner & Storey, 2021 grounds contribution_positioning.method_extension through extracted anchor A18: Adds prerequisite
    space and four externalities to DSR project preparation and governance.'
- source_id: schwartz_yahav_2021_kcd
  short_citation: Schwartz & Yahav (2021)
  evidence_anchor_id: A6
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Schwartz & Yahav (2021) grounds contribution_positioning.method_extension through extracted anchor A6: Introduces
    Knowledge Contribution Diagrams as an extensible graphical technique for representing multiple component-level knowledge
    contributions within complex Design Science Research....'
- source_id: leimeister_dickhaut_janson_2021_design_pattern_bridge_problem_solution
  short_citation: Leimeister, Dickhaut, and Janson (2021)
  evidence_anchor_id: A03
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Leimeister, Dickhaut, and Janson (2021) grounds contribution_positioning.synthesis through extracted anchor A03:
    Positions design patterns as reusable design-knowledge artifacts that bridge problem-space and solution-space by combining
    context, requirements, rationale, consequences, and solution....'
- source_id: src_5a002849d9b3
  short_citation: Drechsler, Gerber, and Hevner 2022
  evidence_anchor_id: A05
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Drechsler, Gerber, and Hevner 2022 grounds contribution_positioning.synthesis through extracted anchor A05: Positions
    DSR as an epistemological and methodological foundation for transdisciplinary research on wicked problems while providing
    a peer-reviewed corpus of artifacts, evaluations....'
- source_id: smuts_winter_gerber_vandermerwe_2022_designing_dsr_taxonomy
  short_citation: Smuts et al. (2022)
  evidence_anchor_id: A11
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Smuts et al. (2022) grounds contribution_positioning.method_extension through extracted anchor A11: Operational taxonomy
    of Design Science Research study-design dimensions and characteristics.'
- source_id: alismail_zhang_chatterjee_2017_dsr_objectives_framework
  short_citation: Alismail, Zhang, and Chatterjee (2017)
  evidence_anchor_id: A06
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Alismail, Zhang, and Chatterjee (2017) grounds contribution_positioning.method_extension through extracted anchor
    A06: Operational framework for identifying DSR objectives that connect problem definition, artifact type, requirements,
    reasoning, build activity, and evaluation.'
- source_id: nagle_sammon_doyle_2017_insights_pdsr
  short_citation: Nagle, Sammon, and Doyle (2017)
  evidence_anchor_id: A1
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Nagle, Sammon, and Doyle (2017) grounds contribution_positioning.method_extension through extracted anchor A1: Practitioner-facing
    operationalization of Design Science Research through a rigor/relevance/iteration canvas.'
- source_id: contell_diaz_venable_2017_dscaffolding
  short_citation: Contell, Díaz, and Venable 2017
  evidence_anchor_id: A08
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Contell, Díaz, and Venable 2017 grounds contribution_positioning.method_extension through extracted anchor A08: Operational
    integration of multiple Design Science Research activities and frameworks into a MindMeister-based scaffolding tool.'
- source_id: 978-3-658-26336-2_3
  short_citation: Siedhoff 2019
  evidence_anchor_id: A06
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Siedhoff 2019 grounds contribution_positioning.synthesis through extracted anchor A06: Operational synthesis of DSRP,
    design thinking, design theory anatomy, case-study research, and action design research for business model innovation.'
- source_id: hunziker_blankenagel_2021_design_science_research_design
  short_citation: Hunziker & Blankenagel (2021)
  evidence_anchor_id: A10
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Hunziker & Blankenagel (2021) grounds contribution_positioning.synthesis through extracted anchor A10: Operational
    guidance for business and management DSR, including artifact typology, process sequence, evaluation criteria, generalization,
    and reporting structure.'
- source_id: brendel_et_al_2021_replication_study_types_dsr
  short_citation: Brendel et al. (2021)
  evidence_anchor_id: A14
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Brendel et al. (2021) grounds contribution_positioning.method_extension through extracted anchor A14: Eight Design
    Science Research replication study types plus a progression framework.'
- source_id: thuan_drechsler_antunes_2019_construction_dsr_questions
  short_citation: Thuan, Drechsler, and Antunes (2019)
  evidence_anchor_id: A21
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Thuan, Drechsler, and Antunes (2019) grounds contribution_positioning.synthesis through extracted anchor A21: Operational
    typology and artifact-specific templates for constructing and formulating Design Science Research questions.'
- source_id: peffers_tuunanen_niehaves_2018_design_science_research_genres
  short_citation: Peffers, Tuunanen, and Niehaves 2018
  evidence_anchor_id: CA-003
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Peffers, Tuunanen, and Niehaves 2018 grounds contribution_positioning.synthesis through extracted anchor CA-003:
    Defines and compares five prototype DSR genres to support genre-sensitive evaluation, reporting, and publication.'
- source_id: baskerville_baiyere_gregor_hevner_rossi_2018_design_science_research_contributions
  short_citation: Baskerville et al. (2018)
  evidence_anchor_id: A3
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Baskerville et al. (2018) grounds contribution_positioning.synthesis through extracted anchor A3: Refines Design
    Science Research contribution logic by balancing artifact sufficiency, design theorizing, process reflection, and impact
    assessment for publication.'
- source_id: tuunanen_winter_vombrocke_2024_edsr_design_echelons
  short_citation: Tuunanen et al. (2024)
  evidence_anchor_id: A08
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Tuunanen et al. (2024) grounds contribution_positioning.method_extension through extracted anchor A08: Adds design
    echelons as a self-contained, validation-linked organizing logic for complex Design Science Research projects.'
- source_id: van_aken_chandrasekaran_halman_2016_jom_dsr
  short_citation: van Aken et al. (2016)
  evidence_anchor_id: A14
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'van Aken et al. (2016) grounds contribution_positioning.method_extension through extracted anchor A14: Operationalizes
    Design Science Research for operations management publication by defining generic design, design proposition, pragmatic
    validity, field testing, generalization, and reviewer....'
- source_id: ijmpb-01-2020-0015
  short_citation: Henriques and O'Neill (2023)
  evidence_anchor_id: A09
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Henriques and O''Neill (2023) grounds contribution_positioning.method_extension through extracted anchor A09: Operational
    process-and-data meta-model integrating DSR stages with focus-group activities and traceability documentation.'
- source_id: trigo_2026_art_nlr
  short_citation: Trigo (2026)
  evidence_anchor_id: A18
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Trigo (2026) grounds contribution_positioning.method_extension through extracted anchor A18: Provides an operational
    method for staged, decision-driven narrative evidence synthesis across Design Science Research activities.'
- source_id: pekkola_2023_reflections_supervising_postgraduate_dsr_thesis
  short_citation: Pekkola 2023
  evidence_anchor_id: not_available
  supports_construct: contribution_positioning.contribution
  evidence_role: process_model
  grounding_decision: scoped
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Pekkola 2023 grounds contribution_positioning.contribution through extracted anchor not_available: Reflections on
    Supervising the Postgraduate Students’ Design Science Research Thesis.'
- source_id: proquest_ebookcentral_docid_5210703_chapter_c_page_119
  short_citation: Applied Design Science Research, chapter C, p. 119
  evidence_anchor_id: CA4
  supports_construct: contribution_positioning.synthesis
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Applied Design Science Research, chapter C, p. 119 grounds contribution_positioning.synthesis through extracted anchor
    CA4: Methodological synthesis into an Iterative Design Science Research framework centered on practitioner cooperation
    and internal/external evaluation.'
- source_id: tqm-01-2023-0017
  short_citation: Antony et al. (2024)
  evidence_anchor_id: A12
  supports_construct: contribution_positioning.method_extension
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Antony et al. (2024) grounds contribution_positioning.method_extension through extracted anchor A12: Extends traditional
    Design Science Research methodology for Operational Excellence-Environmental, Social, and Governance initiatives by adding
    multidimensional evaluation, design thinking....'
- source_id: feine_morana_maedche_2019_machine_executable_descriptive_knowledge
  short_citation: Feine, Morana, and Maedche (2019)
  evidence_anchor_id: A02
  supports_construct: dsr_lifecycle.other
  evidence_role: process_model
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/02-dsr-lifecycle-and-contribution-model.md
  note: 'Feine, Morana, and Maedche (2019) grounds dsr_lifecycle.other through extracted anchor A02: Operational method for
    transforming descriptive X-knowledge into machine-executable prescriptive design knowledge.'
```

<!-- END GENERATED LITERATURE TRACE ANCHORS -->
