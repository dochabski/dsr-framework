<!-- SPDX-License-Identifier: CC0-1.0 -->

# Transparency and Reporting

## Controlled source links

- [models/dsr-transparency-model.yaml](../../models/dsr-transparency-model.yaml)
- [vocabularies/transparency-dimensions.yaml](../../vocabularies/transparency-dimensions.yaml)
- [templates/dsr-transparency-crosswalk-template.yaml](../../templates/dsr-transparency-crosswalk-template.yaml)
- [schemas/dsr-transparency-crosswalk.schema.json](../../schemas/dsr-transparency-crosswalk.schema.json)
- [records/dsr-transparency/record-dsr-transparency-crosswalk-0001.yaml](../../records/dsr-transparency/record-dsr-transparency-crosswalk-0001.yaml)

## Document control

| Field | Value |
|---|---|
| item_id | `docs_transparency` |
| item_type | `description` |
| target_path | `docs/protocol/10-transparency-and-reporting.md` |
| title | Transparency and Reporting |
| purpose | Provide human-facing guidance for documenting, reporting, reviewing, and tailoring Design Science Research transparency evidence. |
| status | draft |
| version | `0.1.0` |
| owner | DSR Framework maintainer |
| conformance_target | `l2_reviewable` |
| primary_source_file_explained | `models/dsr-transparency-model.yaml` |
| related_controlled_files | `vocabularies/transparency-dimensions.yaml`; `templates/dsr-transparency-crosswalk-template.yaml`; `schemas/dsr-transparency-crosswalk.schema.json`; `checklists/dsr-transparency-crosswalk-checklist.yaml`; `records/dsr-transparency/record-dsr-transparency-crosswalk-0001.yaml` |
| related_docs | `docs/protocol/02-dsr-lifecycle-and-contribution-model.md`; `docs/protocol/08-evaluation-framework.md`; `docs/protocol/09-validity-reliability-replication-projectability.md`; `docs/protocol/14-publication-and-review-guidance.md` |
| source_basis | `dsr_framework_generation_spec`; `dsr_framework_generation_prompt`; `hevner_et_al_2024_transparency_in_design_science_research`; `akoka_et_al_2023`; `weigand_johannesson_andersson_2021` |
| change_history | `0.1.0`: Initial L2 reviewable draft. |

## 1. Purpose of this guide

This guide explains how the DSR Framework treats transparency and reporting for Design Science Research (DSR) artifact packages. It is a human-facing rendering of the transparency model and its related operating materials. The controlled source of truth remains in the model, vocabulary, schema, template, checklist, and record files listed above.

Use this page when planning, documenting, reviewing, or publishing a DSR project package. The goal is not maximum disclosure of everything. The goal is proportionate, reviewable transparency that allows readers, reviewers, practitioners, and future researchers to understand what was done, why it was done, what evidence supports the claims, and what boundaries limit reuse or projection.

Transparency in this framework has six dimensions:

1. process transparency
2. problem-space transparency
3. solution-space transparency
4. build transparency
5. evaluation transparency
6. contribution transparency

These dimensions are adapted from the DSR Transparency Framework in Hevner et al. (2024), which identifies process, problem space, solution space, build, evaluation, and contribution as the central transparency forms for DSR.

## 2. Operating definition

For this framework, DSR transparency means:

> The disciplined documentation and communication of the project context, design reasoning, artifact construction, evaluation evidence, contribution logic, limitations, and reuse boundaries needed for a reviewer or future user to assess, adapt, challenge, or extend a DSR artifact package.

Transparency is not equivalent to open access to every artifact, dataset, internal decision, codebase, meeting note, stakeholder communication, or proprietary asset. Some materials may be withheld, summarized, redacted, embargoed, or represented by metadata when disclosure would create privacy, security, legal, intellectual-property, or excessive-maintenance risks.

## 3. What transparency is for

Transparency supports several review and reuse purposes.

| Purpose | What transparency should enable | Typical audience |
|---|---|---|
| Trust in the research account | Readers can see how claims follow from documented design and evaluation activity. | Reviewers, editors, researchers |
| Application and adaptation | Practitioners can judge whether the artifact or design knowledge is usable in a new context. | Practitioners, managers, implementers |
| Replication and projectability | Future researchers can compare contexts, adapt the artifact, and accumulate design knowledge. | Researchers, methodologists |
| Pedagogy and training | Instructors and learners can inspect examples of DSR reasoning, reporting, and evidence. | Students, instructors, supervisors |
| Innovation and generativity | Other researchers can extend the artifact type, design theory, method, model, or instantiation. | Researchers, designers, developers |
| Accountability | Stakeholders can assess whether responsible, ethical, social, or governance concerns were considered. | Stakeholders, publics, reviewers |

A transparent DSR package should make it possible to distinguish the delivered artifact, the evidence of artifact utility, the evidence of artifact quality, and the asserted contribution to knowledge.

## 4. The six transparency dimensions

### 4.1 Process transparency

Process transparency documents the actual sequence of DSR activity, including planned actions, emergent changes, design decisions, reasons, and contextual events.

Minimum reporting content:

- lifecycle stage sequence followed by the project
- major deviations from the original plan
- decision points and rationale
- roles involved in design, review, evaluation, and governance
- design iterations and build-evaluate cycles
- date or version references for important changes
- links to retained decision records where available

Evidence examples:

- project charter
- design decision records
- activity logs
- meeting notes or summarized decision memos
- issue tracker exports or change logs
- iteration summaries
- review records

Do not represent a project as if it followed a clean linear method when the actual project was emergent or iterative. If the project was retrospectively framed as DSR, disclose that history and explain what evidence supports the DSR identity. Retrospective overcoating of ordinary practice as DSR is a specific transparency risk.

### 4.2 Problem-space transparency

Problem-space transparency documents the application context, problem class, stakeholders, goals, requirements, constraints, timeframe, and boundary conditions that make the project relevant.

Minimum reporting content:

- problem statement and problem class
- local problem instance
- affected stakeholders and users
- improvement goals
- functional, quality, governance, and evidence requirements
- scope exclusions and non-goals
- constraints, resources, risks, and dependencies
- timeframe and context-change assumptions
- boundary conditions for reuse or transfer

Evidence examples:

- problem-and-objectives template
- requirements table
- stakeholder map
- context description
- risk register
- governance constraints
- acceptance criteria

Problem-space transparency is especially important because DSR artifacts are situated in social, organizational, technical, and temporal contexts. Reporting should show why the artifact is relevant to the problem and how changes in context may affect use, evaluation, or transfer.

### 4.3 Solution-space transparency

Solution-space transparency documents how the project was grounded in prior knowledge, existing artifacts, design theories, technologies, methods, and alternative solutions.

Minimum reporting content:

- literature basis and search boundaries
- relevant descriptive and prescriptive knowledge
- related artifacts, technologies, methods, models, and design theories
- alternatives considered and rejected
- reuse of prior components or design principles
- assumptions imported from the knowledge base
- gaps that justified the new or adapted artifact

Evidence examples:

- solution-space record
- literature-search notes
- source-basis record
- alternative-analysis table
- prior artifact comparison
- design theory mapping
- dependency inventory

Solution-space transparency is the link between rigor and artifact design. A DSR project should not only state that prior literature exists; it should explain how prior knowledge shaped requirements, architecture, design decisions, evaluation criteria, and contribution claims.

### 4.4 Build transparency

Build transparency documents how the artifact was designed, constructed, configured, adapted, or instantiated.

Minimum reporting content:

- artifact type and artifact boundary
- artifact components and relationships
- design specification, make logic, and use logic
- design rationale and tradeoffs
- iteration history
- design constraints and implementation choices
- relevant stakeholder inputs
- version and configuration information
- known limitations, defects, and unresolved issues

Evidence examples:

- artifact specification
- design rationale record
- build transparency record
- architecture diagram
- pseudocode or code reference
- configuration record
- screenshots, wireframes, process maps, or model diagrams
- change log

Build transparency does not always require publication of executable source code or full implementation materials. Where code, data, or operational details cannot be shared, provide an appropriate substitute: pseudocode, design specification, API summary, configuration description, screenshots, controlled-access location, redacted sample, or rationale for nondisclosure.

### 4.5 Evaluation transparency

Evaluation transparency documents how the artifact was assessed, what criteria were used, what evidence was collected, and how evaluation findings support or limit claims.

Minimum reporting content:

- evaluation purpose and timing
- formative and summative evaluation distinction
- evaluation setting
- evaluation method family
- evaluation criteria
- data, observations, measures, or artifacts inspected
- stakeholder role in evaluation
- claims supported by each evidence source
- threats to validity, reliability, and interpretation
- findings, limitations, and residual uncertainty

Evidence examples:

- evaluation plan
- evaluation report
- demonstration record
- test results
- expert review results
- usability findings
- simulation results
- field observation notes
- quality review record

Evaluation transparency must preserve the distinction between demonstration and evaluation. A demonstration shows that an artifact can be used or illustrated in a scenario. An evaluation provides evidence about utility, quality, performance, acceptance, fitness for use, or contribution-relevant effects under stated criteria.

### 4.6 Contribution transparency

Contribution transparency documents how the project contributes to practice, artifact knowledge, design knowledge, methodology, theory, evaluation, or reporting.

Minimum reporting content:

- contribution claim
- contribution type
- knowledge goal
- knowledge scope
- artifact utility claim
- artifact quality claim
- design knowledge claim
- practice impact claim
- scientific or methodological contribution claim
- novelty and significance rationale
- limitations and non-claims
- projectability or transfer boundary

Evidence examples:

- contribution claim template
- contribution positioning record
- evaluation report
- publication readiness record
- artifact profile
- source-basis record
- limitations section

Contribution transparency requires separating what was built from what was learned. A working artifact may support practice utility, but the DSR contribution depends on the design knowledge, evaluative knowledge, artifact ontology, method extension, theory refinement, or transferable pattern that the project makes available.

## 5. Minimum transparency crosswalk

Every DSR package should include or link to a transparency crosswalk. The crosswalk may be implemented as a retained record, a section in the artifact profile, or a stand-alone file using `templates/dsr-transparency-crosswalk-template.yaml`.

| Dimension | Required question | Minimum evidence | Pass condition |
|---|---|---|---|
| Process | Can a reviewer reconstruct the major DSR activities and decisions? | Lifecycle sequence, decision records, iteration notes | Major activities, reasons, changes, and outputs are visible. |
| Problem space | Can a reviewer understand the application context and improvement target? | Problem statement, stakeholders, goals, requirements, constraints | Scope, goals, users, constraints, and boundaries are explicit. |
| Solution space | Can a reviewer see how prior knowledge shaped the artifact? | Literature basis, alternatives, prior artifacts, design principles | Design choices are grounded rather than arbitrary. |
| Build | Can a reviewer understand what was built and how it works at the relevant level of abstraction? | Artifact specification, design rationale, version/configuration information | Artifact boundary, components, make/use logic, and limitations are documented. |
| Evaluation | Can a reviewer assess the fit between claims and evidence? | Evaluation plan/report, criteria, results, threats | Evaluation methods and evidence align to stated claims. |
| Contribution | Can a reviewer identify what knowledge contribution is claimed and bounded? | Contribution claim, contribution type, knowledge goal/scope, limitations | Practice and knowledge contributions are distinguished and justified. |

## 6. Reporting workflow

Use the following workflow when preparing a DSR artifact package.

### Step 1: Identify transparency obligations

Determine which dimensions apply to the selected artifact type, contribution claim, evaluation stage, and conformance target.

Output:

- applicable transparency dimensions
- required records and templates
- known nondisclosure constraints
- preliminary evidence inventory

### Step 2: Populate source records during the project

Record process, problem, solution, build, evaluation, and contribution evidence as the project develops. Do not wait until the final manuscript stage to reconstruct evidence from memory.

Output:

- project charter
- problem-and-objectives record
- solution-space record
- design rationale or build transparency record
- evaluation plan and report
- contribution claim

### Step 3: Create the transparency crosswalk

Map each claim to the evidence that supports it. Mark unavailable evidence explicitly and explain whether the absence is a true limitation, a nondisclosure constraint, or an intentional tailoring decision.

Output:

- `record-dsr-transparency-crosswalk-0001.yaml` or equivalent
- evidence-status values such as `available`, `partial`, `redacted`, `controlled_access`, `not_applicable`, or `accepted_v1_limitation`

### Step 4: Check proportionality and risk

Review whether the requested or included transparency materials create burden, confidentiality risk, security exposure, privacy exposure, intellectual-property risk, or long-term maintenance obligations.

Output:

- redaction decisions
- substituted evidence summaries
- access conditions
- limitations and risk notes

### Step 5: Align reporting to the publication and package structure

Translate controlled records into human-facing reporting. Do not duplicate all controlled data in narrative form. Link to the authoritative files and summarize what a reader needs to understand.

Output:

- manuscript or docs section
- artifact package file links
- repository inventory updates
- publication-readiness notes

### Step 6: Review against quality gates

Apply the transparency checklist and the relevant package, evaluation, contribution, reliability, and projectability checklists.

Output:

- completed checklist
- review record
- remediation actions
- readiness decision

## 7. Evidence-status vocabulary for reporting

Use consistent evidence-status values when building a crosswalk or review record.

| Evidence status | Meaning | Reporting expectation |
|---|---|---|
| `available` | Evidence is included in the package. | Link to the file or section. |
| `partial` | Some evidence is available, but not enough for full reconstruction. | State what is missing and why. |
| `redacted` | Evidence exists but sensitive content has been removed. | State redaction reason and remaining evidence value. |
| `controlled_access` | Evidence exists but is not publicly released. | State access condition or governance reason. |
| `not_applicable` | Dimension or evidence type does not apply. | Explain the tailoring rationale. |
| `accepted_v1_limitation` | Evidence may exist but has not been mapped to the package. | Treat as an open review issue. |
| `unavailable` | Evidence does not exist or cannot be recovered. | State the limitation and claim impact. |

## 8. Balancing transparency with risk

Transparency must be managed, not maximized without judgment.

| Risk | Examples | Acceptable mitigation |
|---|---|---|
| Confidentiality risk | Proprietary requirements, internal process records, partner communications | Redact, summarize, embargo, or use controlled access. |
| Privacy risk | Human participant data, stakeholder identities, evaluation records | De-identify, aggregate, anonymize, or provide IRB/governance statement. |
| Security risk | Vulnerabilities, credentials, exploit paths, sensitive architecture | Remove operational details, provide safe architecture summary, document withheld evidence. |
| Intellectual-property risk | Trade secrets, licensed code, patentable implementation details | Provide design abstraction, component interface, or protected access path. |
| Maintenance burden | Executable artifacts that cannot be sustained publicly | Provide versioned snapshot, archived binary, pseudocode, screenshots, or dependency summary. |
| Information overload | Excessive raw logs or uncurated materials | Provide index, evidence map, summary, and selected appendices. |
| False precision | Overstated reproducibility or generalizability | State boundary conditions, residual uncertainty, and projection limits. |

A transparency limitation is acceptable when it is explicit, justified, and mapped to affected claims. It is not acceptable to hide missing evidence while making strong claims that require that evidence.

## 9. Reporting structure for a DSR transparency section

A DSR report, artifact profile, or repository README should include a concise transparency section. The following structure is recommended.

```markdown
## Transparency and reporting

### Process transparency
- Lifecycle path:
- Major iterations:
- Key decisions:
- Deviations from plan:
- Evidence links:

### Problem-space transparency
- Problem class:
- Local problem instance:
- Stakeholders:
- Improvement goals:
- Constraints and boundaries:
- Evidence links:

### Solution-space transparency
- Knowledge base searched:
- Prior artifacts or theories used:
- Alternatives considered:
- Reuse or dependency decisions:
- Evidence links:

### Build transparency
- Artifact type and boundary:
- Components:
- Make/use logic:
- Rationale and tradeoffs:
- Version or configuration:
- Evidence links:

### Evaluation transparency
- Evaluation questions:
- Methods and criteria:
- Evidence collected:
- Findings:
- Threats and limitations:
- Evidence links:

### Contribution transparency
- Contribution claim:
- Contribution type:
- Knowledge goal and scope:
- Practice contribution:
- Scientific or methodological contribution:
- Non-claims and boundaries:
- Evidence links:
```

This structure may be shortened for lightweight packages, but L2 reviewable conformance requires enough evidence for independent review.

## 10. Reviewer guidance

A reviewer should assess transparency by asking whether the package supports warranted judgment. The reviewer should not demand every possible source file or raw data item if a proportionate evidence substitute is sufficient.

| Review concern | Reviewer question | Fail signal | Remediation |
|---|---|---|---|
| Process opacity | Can I tell what was actually done? | The project appears artificially linear or reconstructed without evidence. | Add timeline, decision records, iteration summary, and deviation notes. |
| Problem ambiguity | Can I tell what problem the artifact addresses? | The problem is generic, decontextualized, or disconnected from stakeholders. | Add problem class, local instance, stakeholders, requirements, and boundary conditions. |
| Weak grounding | Can I tell how prior knowledge shaped the design? | Literature is cited but not connected to artifact choices. | Add solution-space mapping and alternative rationale. |
| Build opacity | Can I tell what artifact was produced? | Artifact boundary, components, or use logic are unclear. | Add artifact specification, diagrams, version/configuration notes, and rationale. |
| Evaluation mismatch | Can I tell which claims are supported by which evidence? | Evaluation evidence does not align with claims. | Add claim-evidence matrix and evaluation limitations. |
| Contribution overclaim | Can I tell what knowledge contribution is actually warranted? | Practice utility is treated as sufficient proof of general knowledge contribution. | Separate artifact utility, quality, and contribution claims. |
| Unmanaged nondisclosure | Are withheld materials justified? | Evidence is missing without explanation. | Add evidence status, redaction rationale, and claim impact. |

## 11. Acceptance criteria

This page and its related controlled files satisfy L2 reviewable transparency guidance when the package can show the following:

- The six transparency dimensions are defined and operationalized.
- The page identifies controlled source files rather than becoming the only source of truth.
- The framework distinguishes demonstration from evaluation.
- The framework distinguishes artifact utility, artifact quality, and contribution to knowledge.
- The crosswalk supports claim-to-evidence traceability.
- Missing, redacted, controlled-access, or not-applicable evidence can be recorded explicitly.
- Transparency risks and burdens are acknowledged.
- Reviewer questions and remediation paths are provided.
- Limitations and open questions are visible.

## 12. Common failure modes

| Failure mode | Description | Corrective action |
|---|---|---|
| Ex-post DSR-ification | A non-DSR project is retrospectively framed as DSR without transparent process and knowledge-contribution evidence. | Disclose project history, identify actual DSR elements, and limit claims accordingly. |
| Evidence dumping | Raw materials are provided without indexing or claim mapping. | Add an evidence inventory and crosswalk. |
| Abstractness barrier | Reporting uses technical or theoretical language that blocks practitioner understanding. | Add plain-language summaries and concrete use guidance. |
| Replication overclaim | The package implies exact replication where context change makes that inappropriate. | Reframe as differentiated replication, projectability, transfer, or adaptation. |
| Contribution conflation | Artifact success, artifact quality, and knowledge contribution are treated as the same thing. | Separate utility, quality, and contribution claims. |
| Confidentiality silence | Sensitive evidence is omitted without explanation. | Add redaction or controlled-access rationale. |
| Evaluation underreporting | Findings are stated without criteria, method, setting, or threat discussion. | Add evaluation plan/report links and claim-evidence alignment. |

## 13. Traceability

| trace_id | Source or related item | Role in this page |
|---|---|---|
| `trace_docs_transparency_selection` | `docs_transparency` selection row | Defines target path, output format, purpose, conformance, and dependency. |
| `trace_generation_spec` | `dsr_framework_generation_spec` | Defines repository conventions, docs-page expectations, quality gates, and completion-report requirement. |
| `trace_generation_prompt` | `dsr_framework_generation_prompt` | Defines generation procedure, governed source priority, Markdown documentation rules, and DSR-specific distinctions. |
| `trace_model_transparency` | `models/dsr-transparency-model.yaml` | Primary controlled model explained by this human-facing page. |
| `trace_vocab_transparency` | `vocabularies/transparency-dimensions.yaml` | Controlled vocabulary for the six dimensions. |
| `trace_template_crosswalk` | `templates/dsr-transparency-crosswalk-template.yaml` | Operational template for documenting evidence. |
| `trace_schema_crosswalk` | `schemas/dsr-transparency-crosswalk.schema.json` | Validation target for transparency crosswalk records. |
| `trace_checklist_transparency` | `checklists/dsr-transparency-crosswalk-checklist.yaml` | Review checklist associated with this page. |
| `trace_hevner_2024` | `hevner_et_al_2024_transparency_in_design_science_research` | Primary DSR transparency source; supports six dimensions, risks, audiences, and reporting guidance. |
| `trace_akoka_2023` | `akoka_et_al_2023` | Supports knowledge-contribution transparency, accumulation, and path-based reporting. |
| `trace_weigand_2021` | `weigand_johannesson_andersson_2021` | Supports artifact boundary, make/use logic, artifact universal, and build transparency. |

## 14. Limitations and non-goals

This guide is an L2 reviewable documentation page. It does not by itself validate a transparency crosswalk, prove that a package is publication-ready, or replace the structured files used by the repository.

Non-goals:

- It does not require full open release of code, data, raw logs, or proprietary artifacts.
- It does not define a universal minimum evidence set for every DSR genre.
- It does not assert that exact replication is always possible or desirable in DSR.
- It does not replace evaluation, validity, reliability, projectability, or publication-readiness guidance.
- It does not close future development of more detailed transparency checklists.

Open questions:

- What evidence thresholds should distinguish L2 reviewable, L3 exercisable, L4 reusable, and L5 archival/publication-ready transparency?
- Which transparency materials should be required for specific artifact types such as models, methods, taxonomies, software instantiations, schemas, and socio-technical protocols?
- How should controlled-access evidence be represented in public registries and archival releases?
- What scoring rubric should reviewers use when transparency is partial but proportionately justified?

## 15. Completion report

```yaml
completion_report:
  generated_selection_id: docs_transparency
  generated_path: docs/protocol/10-transparency-and-reporting.md
  item_type: description
  output_format: markdown
  conformance_target: l2_reviewable
  dependencies_used:
    - dsr-framework-generation-prompt.md
    - dsr-framework-generation-spec.yaml
    - dsr-framework-selection-table.md
    - chunked_folder_conversion_extractions_20260427030321_part001.yaml
  assumptions:
    - The controlled files named in this page either exist elsewhere in the framework package or will be generated as selected portions.
    - This page is a human-facing guide and not the sole source of controlled transparency data.
    - External sources were not used because the project instruction and generation specification prioritize internal corpus and protocol sources unless current external facts are required.
  open_questions:
    - Define exact conformance thresholds for transparency at L3, L4, and L5.
    - Finalize validation rules in the transparency crosswalk schema after the controlled model and vocabulary are stabilized.
  quality_gate_status:
    consistency: pass
    coherence: pass
    cogency: pass
    correspondence: pass
    dsr_transparency: pass
    reviewability: pass
  next_recommended_file: docs/protocol/14-publication-and-review-guidance.md
```
<!-- BEGIN GENERATED LITERATURE TRACE ANCHORS -->

## Literature Trace Anchors

```yaml
source_basis:
- source_id: hevner_et_al_2024_transparency_in_design_science_research
  short_citation: Hevner et al. (2024)
  evidence_anchor_id: CA01
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'Hevner et al. (2024) grounds transparency_reporting.reporting_guidance through extracted anchor CA01: A six-feature
    framework and reporting-guidance structure for transparent Design Science Research.'
- source_id: zur_heiden_2020_considering_context_dsr
  short_citation: zur Heiden (2020)
  evidence_anchor_id: A10
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'zur Heiden (2020) grounds transparency_reporting.reporting_guidance through extracted anchor A10: Refines DSR reporting
    and projectability by operationalizing context specification and context-to-design traceability.'
- source_id: opdenakker_talmar_2021_slr_examples_dsr
  short_citation: Opdenakker and Talmar (2021)
  evidence_anchor_id: A09
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'Opdenakker and Talmar (2021) grounds transparency_reporting.reporting_guidance through extracted anchor A09: Operational
    guidance for using systematic literature reviews to synthesize causal and prescriptive design knowledge through Context-Intervention-Mechanism-Outcome
    or related structures.'
- source_id: vom_brocke_gau_maedche_2021_journaling_dsr_process
  short_citation: vom Brocke, Gau, and Mädche 2021
  evidence_anchor_id: A06
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'vom Brocke, Gau, and Mädche 2021 grounds transparency_reporting.reporting_guidance through extracted anchor A06:
    Introduces concurrent journaling of the Design Science Research process as a transparency and documentation protocol for
    making design knowledge production more visible.'
- source_id: vom_brocke_weber_grisold_2021_dsr_practical_relevance
  short_citation: vom Brocke, Weber, and Grisold (2021)
  evidence_anchor_id: A09
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'vom Brocke, Weber, and Grisold (2021) grounds transparency_reporting.reporting_guidance through extracted anchor
    A09: A collaboration-centered framework and reporting criteria for increasing practical relevance and societal value in
    Design Science Research.'
- source_id: dickhaut_janson_leimeister_2022_design_knowledge_representation
  short_citation: Dickhaut, Janson, and Leimeister (2022)
  evidence_anchor_id: A10
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'Dickhaut, Janson, and Leimeister (2022) grounds transparency_reporting.reporting_guidance through extracted anchor
    A10: Five codification recommendations for reusable and applicable DSR design knowledge.'
- source_id: van_aken_chandrasekaran_halman_2016_jom_design_science_research
  short_citation: van Aken et al. (2016)
  evidence_anchor_id: A18
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'van Aken et al. (2016) grounds transparency_reporting.reporting_guidance through extracted anchor A18: Operationalizes
    DSR for operations management publication through generic designs, design propositions, pragmatic validity, field testing,
    generalization, and reviewer criteria.'
- source_id: vom_brocke_maedche_2019_dsr_grid
  short_citation: vom Brocke & Maedche, 2019
  evidence_anchor_id: A03
  supports_construct: transparency_reporting.reporting_guidance
  evidence_role: transparency
  grounding_decision: adapted
  evidence_status: substantive
  target_path: docs/protocol/10-transparency-and-reporting.md
  note: 'vom Brocke & Maedche, 2019 grounds transparency_reporting.reporting_guidance through extracted anchor A03: Six-dimension
    framework for planning, communicating, reviewing, and accumulating DSR project knowledge.'
```

<!-- END GENERATED LITERATURE TRACE ANCHORS -->
