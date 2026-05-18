---
title: "From Design Science Research Theory to Repository-Native Operationalization"
subtitle: "A White Paper for the DSR Framework"
author:
  - name: "David Ochabski"
    orcid: "0009-0000-9117-0651"
date: "2026-05-17"
version: "0.1.0-draft"
status: "working white paper draft"
repository: "https://github.com/dochabski/dsr-framework"
related_repository: "https://github.com/dochabski/documentation-protocol"
canonical_source_policy: "GitHub source of truth plus Zenodo DOI release for archival citation"
license_note: "Verify final license, third-party quotation status, and platform compatibility before public deposit."
---

# From Design Science Research Theory to Repository-Native Operationalization

## Version note

This draft is prepared as an open artifact white paper. It is designed to be readable as a normal human-facing paper and also structured enough for repository automation, AI ingestion, archival deposit, and future validation work.

The paper should not claim independent external validation, semantic consensus, or L5 archival/publication-ready status until those events are explicitly recorded in the DSR Framework repository.

## Abstract

Design Science Research (DSR) is an artifact-centered research tradition in which researchers identify a relevant problem, design and instantiate an artifact or design entity, evaluate that artifact against explicit objectives and criteria, and communicate reusable or projectable design knowledge. The challenge addressed by this white paper is operational: DSR theory provides rich guidance, but DSR work is often documented in prose that obscures artifact boundaries, problem-to-requirement traces, evaluation alignment, contribution claims, and reuse conditions. This paper synthesizes the DSR theory base and explains how the DSR Framework repository operationalizes it as a GitHub-native artifact package. The framework treats DSR documentation as a structured, traceable, validation-ready system that includes models, vocabularies, schemas, templates, checklists, records, crosswalks, rubrics, examples, and nested artifacts. The paper positions the repository as a compound DSR artifact: a framework for producing, reviewing, releasing, citing, and reusing DSR artifact packages. It also proposes a publication and dissemination strategy that preserves a single canonical source of truth while increasing human and machine discoverability through GitHub, Zenodo, OSF, Octopus, and selected profile/dissemination channels.

## Keywords

Design Science Research; design knowledge; artifact ontology; DSR evaluation; DSR transparency; repository-native research; research artifact packaging; GitHub; Zenodo; Open Science Framework; Octopus; FAIR; AI-legible documentation.

## Recommended citation placeholder

Ochabski, D. (2026). *From Design Science Research Theory to Repository-Native Operationalization: A White Paper for the DSR Framework* (Version 0.1.0-draft). DSR Framework. DOI pending.

---

# Executive Summary

This white paper should be framed as a **repository-native methodological white paper with an open artifact package**. It is not mainly a policy brief, a promotional white paper, a dataset descriptor, or a conventional literature review. Its contribution is partly conceptual, partly methodological, and partly infrastructural: it explains what DSR is, how DSR can be operationalized, and how the DSR Framework repository is operationalizing it.

The central thesis is:

> Design Science Research becomes more reviewable, reusable, citable, and AI-legible when its core commitments are represented as structured repository artifacts: problem and context records, artifact specifications, requirements traces, design-rationale records, evaluation plans and reports, contribution claims, controlled vocabularies, schemas, validation shapes, rubrics, examples, release records, and preservation metadata.

The paper makes three linked arguments.

First, DSR is not merely "building something." It is artifact-centered inquiry that connects a practically significant problem, a designed artifact or design entity, rigorous grounding in prior knowledge, demonstration and evaluation, and reusable design knowledge.

Second, DSR needs operational structure. A complete DSR record should capture the problem instance, problem class, context, stakeholders, input knowledge, objectives, requirements, artifact/design entity, build trace, demonstration/use trace, evaluation evidence, contribution claim, design knowledge, boundary conditions, and transparency trace.

Third, the DSR Framework repository is a credible attempt to implement that structure. Its strongest contribution is traceability discipline: it treats GitHub not simply as a host but as a research artifact stewardship environment where files, versions, metadata, validation records, release records, and crosswalks carry methodological evidence.

The recommended publication architecture is intentionally conservative: use GitHub as the canonical living source, Zenodo as the DOI-bearing archival release, OSF as a project/discovery hub or optional preprint layer, and Octopus as an optional research-process record once the paper has stable modular sections. Use ResearchGate, Academia.edu, LinkedIn, Substack, and similar services for dissemination only. Use Mendeley Data or Dryad only for genuine data packages, not as the canonical home for the white paper itself.

---

# 1. Introduction

Design Science Research has an operational problem beneath its theoretical richness. The field gives researchers a strong paradigm: identify relevant problems, design artifacts, evaluate them, and contribute design knowledge. Yet many DSR outputs remain hard to inspect because their most important relations are buried in narrative. A reader may see an artifact but not the problem class it addresses, an evaluation but not the claim it supports, or a contribution statement but not the boundary conditions that make the claim reusable rather than overgeneralized.

This paper treats DSR documentation as a design problem in its own right. If DSR is artifact-centered inquiry, then a framework for documenting DSR artifacts can itself be designed, evaluated, reviewed, released, and improved as a DSR artifact. The DSR Framework repository follows that logic. It attempts to translate DSR theory into structured repository products: models, vocabularies, schemas, templates, rubrics, records, checklists, examples, and crosswalks.

The paper distinguishes two layers that should not be conflated.

1. **DSR theory**: the scholarly and professional literature on artifact-centered research, problem relevance, rigorous grounding, build/evaluate logic, contribution, evaluation, transparency, reliability, replication, projectability, and publication.
2. **Repository operationalization**: the specific implementation of those ideas in the DSR Framework repository and its related Documentation Protocol repository.

The purpose is not to replace the DSR literature with a single repository template. The purpose is narrower and more practical: to show how DSR commitments can be represented in a source-grounded, reviewable, reusable, citable, and machine-actionable artifact package.

## Audience

The primary audiences are DSR researchers, doctoral supervisors, methodology instructors, reviewers, editors, repository maintainers, and AI-assisted research infrastructure builders. Practitioners may also use the framework where DSR artifacts must be documented for reuse, review, audit, or publication.

## White paper type

The recommended genre is a repository-native methodological white paper with an open artifact package. A conventional review article would understate the designed artifact package. A dataset deposit would overemphasize the source extractions. A policy brief would be too thin. A software paper would be too narrow. The right genre is a white paper that explains the theory, states the operational model, and points to a versioned repository artifact.

---

# 2. What Design Science Research Is

Design Science Research is an artifact-centered research paradigm. Its central operation is not observation alone and not implementation alone, but the disciplined transformation of a relevant problem into an evaluated artifact and codified design knowledge. A DSR study therefore needs a problem, context, input knowledge, objectives, artifact, instantiation or demonstration, evaluation evidence, contribution claim, and transparency trace.

A compact formalization is useful:

```text
DSR = <P, C, Rq, K_in, O, A, I, E, DK, K_out, T>
```

where `P` is the problem, `C` the context, `Rq` the research question, `K_in` the input knowledge, `O` the objectives and requirements, `A` the artifact or design entity, `I` the instantiation or use case, `E` the evaluation evidence, `DK` the generated design knowledge, `K_out` the output knowledge, and `T` the transparency trace.

The field's consensus commitments can be summarized as follows.

| Commitment | Operational meaning | Failure avoided |
|---|---|---|
| Artifact centrality | A designed artifact or design entity is the object of inquiry. | Pure explanation or critique without design contribution. |
| Practical problem relevance | The artifact is justified by a meaningful problem in context. | Abstract artifact construction without stakeholder or problem grounding. |
| Rigor through knowledge base | The design and evaluation draw from prior theory, artifacts, methods, patterns, and evidence. | Unjustified invention. |
| Build/evaluate logic | Design and evaluation are coupled and often iterative. | Undemonstrated or unevaluated artifact claims. |
| Design knowledge contribution | The study contributes reusable or projectable knowledge, not just local delivery. | Routine implementation overclaim. |
| Evaluation validity | Evaluation fits the artifact, maturity, context, criteria, and claim type. | Method-claim mismatch. |
| Communication | The study communicates problem, artifact, method, evaluation, contribution, and applicability. | Artifact delivery without research communication. |
| Accumulation | Knowledge is codified so later researchers can reuse, adapt, replicate, or challenge it. | Isolated one-off artifact reports. |
| Genre plurality | DSR allows multiple artifact and contribution genres. | False requirement that all DSR must look like one paper template. |

This interpretation sets the boundary between DSR and ordinary consulting or software delivery. A local implementation may be useful, but a DSR contribution requires explicit design knowledge, evaluation evidence, and boundary conditions.

---

# 3. How DSR Can Be Operationalized

The operational problem is to convert DSR commitments into a record architecture that can be reviewed, validated, reused, and cited. This paper proposes a minimum DSR record architecture with twelve required modules.

| Module | Purpose | Minimum contents |
|---|---|---|
| Source and project identity | Establish provenance and reviewability. | title, authors, version, source role, DSR genre, extraction confidence |
| Problem space | Prevent weak problem grounding. | problem instance, problem class, severity, relevance, solvability |
| Context | Bound validity and projectability. | organization, domain, stakeholders, constraints, artifact network, boundary conditions |
| Input knowledge / solution space | Establish rigor grounding. | kernel theories, prior artifacts, methods, design patterns, practitioner knowledge |
| Objectives and requirements | Translate the problem into evaluable design targets. | objectives, meta-requirements, design requirements, acceptance criteria |
| Artifact/design entity | Define the designed object of inquiry. | artifact type, artifact universal, instantiation, specification, make plan, use plan, capacity specification |
| Build and design rationale | Avoid artifact black boxing. | design decisions, alternatives, rationale, build trace, iteration trace |
| Demonstration and use | Show feasibility and situated use. | scenario, prototype, pilot, use case, implementation context, user role |
| Evaluation | Support utility and claim validity. | evaluation object, criteria, timing, setting, evidence mode, stakeholders, findings, limitations |
| Design knowledge and contribution | Distinguish research from routine design. | contribution object, knowledge goal, scope, novelty, evidence basis, boundary conditions |
| Reliability, replication, accumulation | Support cumulative DSR. | reliability target, replication type, reuse conditions, projectability statement |
| Transparency and responsible disclosure | Support trust without overload. | process, problem-space, solution-space, build, evaluation, and contribution transparency |

This architecture turns DSR into a linked system rather than a linear narrative. The key spaces are problem space, context space, solution space, design space, artifact space, evaluation space, knowledge space, and communication/transparency space. The most important edges are:

```text
problem -> objective -> requirement -> design decision -> artifact -> demonstration -> evaluation -> contribution claim -> design knowledge -> reuse boundary
```

Operationalization should not over-formalize every judgment. Some checks can be automated, such as whether a study has a problem class, artifact, evaluation plan, and contribution claim. Other checks require human review, such as whether the problem is important, whether the artifact is novel enough, whether the evidence adequately supports the claim, and whether boundary conditions are credible.

## Evaluation alignment

A DSR evaluation record should distinguish timing, function, setting, object, evidence mode, criterion, stakeholder, and claim supported. Demonstration is not evaluation unless criteria, evidence, and claims are defined. Evaluation evidence should be represented separately from contribution claims: evaluation says whether and under what conditions the artifact works; contribution explains what reusable knowledge has been added.

## Contribution alignment

A strong design-knowledge claim links context, intervention, mechanism or rationale, outcome, and boundary condition. This makes the contribution portable enough to be useful while still bounded enough to avoid overgeneralization.

---

# 4. Repository-Native Operationalization

The DSR Framework repository operationalizes DSR by making methodological evidence structural. Instead of asking authors only to write a narrative, it gives them repository locations and controlled information items for the claims a DSR study needs to support.

The repository-native model has five design principles.

| Design principle | Repository expression |
|---|---|
| Source of truth discipline | Controlled YAML and metadata files capture the authoritative structured record. |
| Human legibility | Markdown documentation explains the structured files for researchers, reviewers, and maintainers. |
| AI legibility | Stable identifiers, schemas, controlled vocabularies, and file maps support machine ingestion and automated review. |
| Non-overclaiming | Conformance levels and release records distinguish draft, documented, reviewable, exercisable, reusable, and archival/publication-ready status. |
| Traceability | Crosswalks and records connect source basis, problem framing, design choices, evaluation evidence, contribution claims, and release decisions. |

The repository is therefore not just a static guide. It is a compound artifact package containing specifications, models, vocabularies, schemas, templates, checklists, rubrics, records, crosswalks, examples, documentation, metadata, release controls, and nested artifacts.

## The role of GitHub

GitHub is useful here because the artifact is file-based and versioned. A repository can retain commits, releases, tags, issue discussions, pull requests, review records, validation scripts, package inventories, and citation metadata. That does not make GitHub an archive by itself. It makes GitHub the living source-of-truth environment that should be paired with an archival DOI-bearing release repository.

## The role of the Documentation Protocol

The Documentation Protocol supplies the meta-protocol: source-of-truth separation, package conformance, review records, release controls, preservation logic, citation metadata, licensing, and service integration. The DSR Framework applies that meta-protocol to the DSR domain. This relationship should be stated explicitly so readers understand why the framework is packaged as a repository artifact rather than only as a prose methodology paper.

---

# 5. How We Are Operationalizing DSR Through the Repositories

The current operationalization can be described as a three-layer artifact system.

## Layer 1: The DSR Framework repository

The root DSR Framework repository defines the general framework for planning, documenting, evaluating, reviewing, and publishing DSR artifacts. It includes package-control files, metadata, artifact profiles, conformance declarations, specs, models, vocabularies, schemas, templates, checklists, rubrics, records, crosswalks, examples, and documentation.

Its core claim should remain bounded: it is a reusable-stable DSR documentation and review framework. It should not yet claim independent external validation, universal disciplinary standard status, or automatic validation of downstream DSR projects.

## Layer 2: The DSR theory operational kernel

The nested DSR theory operational kernel turns the DSR theory synthesis into machine-readable and reviewable materials: concept inventory, competency questions, ontology, SKOS vocabulary, SHACL shapes, JSON Schema, YAML templates, crosswalks, source-basis records, and validation records.

This is the most direct example of DSR theory becoming operational. It translates concepts such as artifact universal, artifact instantiation, problem class, evaluation evidence, contribution claim, transparency trace, reliability, replication, and anti-patterns into controlled terms and validation targets.

## Layer 3: White paper and release package

This white paper should be added as its own bounded artifact package or documentation package. Recommended location:

```text
artifacts/dsr-framework-white-paper/
```

or, if you want it to be a public-facing documentation product rather than an internal artifact package:

```text
docs/white-papers/dsr-framework-operationalization/
```

For consistency with the repository's artifact-package logic, the stronger choice is `artifacts/dsr-framework-white-paper/` with a short public link from the root `README.md` and possibly a rendered copy under `docs/`.

Recommended retained files include:

```text
README.md
whitepaper/chapters/*.md
whitepaper/whitepaper_unified.md
metadata/CITATION.cff
metadata/zenodo-json-template.json
metadata/service-integration-profile.yaml
records/decisions/record-decision-0001-whitepaper-type-and-platforms.yaml
records/releases/record-release-checklist-whitepaper.yaml
repo_integration/repo-update-checklist.md
```

The repository update should preserve the same non-overclaiming discipline as the root framework: mark the white paper as draft or reviewable until human edit, citation review, build validation, and release decisions are retained.

---

# 6. Publication and Dissemination Strategy

The publication strategy should maximize visibility without creating multiple competing sources of truth. The recommended architecture is:

```text
Canonical living source: GitHub
Archival citation snapshot: Zenodo DOI release
Project/discovery hub: OSF project, optional OSF Preprint
Research-process publication: Octopus, optional after stable modularization
Data-only secondary deposits: Mendeley Data or Dryad only if releasing a genuine data package
Profile/dissemination mirrors: ResearchGate, Academia.edu, LinkedIn, Substack, ORCID, personal website
Teaching/OER derivative: OER Commons or VIVA Open only after adapting the paper into learning materials
```

## Recommended platform roles

| Platform | Recommended role | Use now? | Rationale |
|---|---|---:|---|
| GitHub | Canonical living source and source-of-truth repository. | Yes | Best fit for Markdown, metadata, version control, issue review, release records, schemas, validation scripts, and repo-native DSR logic. |
| Zenodo | DOI-bearing archival snapshot of GitHub release. | Yes | Best fit for citable release snapshot and long-term scholarly reference. |
| OSF | Project/discovery hub; optional preprint and linked materials. | Yes, after GitHub draft is stable | Useful for open-science visibility, supplemental files, and discovery. Keep GitHub/Zenodo canonical. |
| Octopus | Modular research-process record. | Optional | Useful if you want to publish problem, method, results/synthesis, interpretation, and application as linked units. Do after the paper is stable. |
| SSRN | Discipline-facing preprint for IS/management/social-science audiences. | Optional | Consider if you want social-science and management discovery; do not make it canonical. |
| Mendeley Data | Data package only. | Optional later | Use only for source extraction corpus, concept inventory, or artifact data that can be openly licensed and safely shared. |
| Dryad | Curated data package only. | Usually no for this paper | Not the right primary home for a white paper; use only if releasing reusable research data under compatible terms. |
| ResearchGate | Profile dissemination link or licensed full-text mirror. | Optional | Good for visibility, not canonicality. Link to GitHub/Zenodo. |
| Academia.edu | Profile dissemination link or licensed full-text mirror. | Optional | Good for visibility, not canonicality. Link to GitHub/Zenodo. |
| OER Commons / VIVA Open | Teaching derivative or workbook. | Not yet | Use after making an instructional version, not for the primary white paper. |
| arXiv | Preprint only if a suitable category and format fit. | Probably no | DSR framework/methodology may fit better on OSF Preprints or SSRN unless there is a clear computing/information-science framing. |
| bioRxiv / medRxiv | Not relevant. | No | The paper is not a life-science or medical preprint. |
| HAL | Optional institutional/open archive mirror. | Optional | Consider only if you want a European open-archive mirror and can maintain metadata consistency. |

The main rule is simple: do not scatter the white paper as unrelated uploads. Create one canonical GitHub release, archive it through Zenodo, then point all other platforms to that release or deposit a clearly labeled derivative.

---

# 7. Limitations, Evaluation, and Roadmap

The DSR Framework should be presented favorably but bounded. The available materials support a strong claim about conceptual synthesis, repository design, traceability, and self-application. They do not yet support a strong claim about external adoption, independent semantic adequacy, downstream empirical utility, or field-wide consensus.

## Current strengths

1. The framework preserves DSR's identity boundary: artifact-centered inquiry, problem relevance, rigorous grounding, evaluation, and design knowledge.
2. It operationalizes traceability instead of merely recommending it.
3. It distinguishes demonstration from evaluation and artifact utility from knowledge contribution.
4. It includes a theory operational kernel with ontology, SKOS, SHACL, schemas, competency questions, and concept inventory artifacts.
5. It uses conformance and release controls to avoid premature L5 claims.

## Current limitations

1. The framework has not yet been independently validated by external DSR experts.
2. The ontology and controlled vocabulary need semantic review before they should be treated as stable disciplinary representations.
3. Repository self-application supports coherence, not general empirical utility.
4. The source extraction corpus and generated summaries require final human review before publication.
5. Platform release work requires manual authentication and metadata checks.

## Recommended evaluation roadmap

| Stage | Evaluation action | Evidence retained |
|---|---|---|
| Internal review | Check consistency among white paper, repo status, artifact-profile, package inventory, and release records. | Review record and issue log. |
| Build validation | Render Markdown to HTML/PDF and check links, headings, tables, citations, and accessibility. | Build log and release checklist. |
| Source review | Verify all core literature references, DOIs, and claims against source records. | Citation audit record. |
| Expert review | Ask 2-3 DSR scholars or advanced reviewers to assess theory fit and overclaiming. | External review records and response matrix. |
| Downstream pilot | Use the framework in one or more DSR studies or teaching contexts. | Pilot package, evaluation report, revised rubrics. |
| Archival release | Freeze a release, mint DOI, preserve metadata, and update citation records. | GitHub release, Zenodo DOI, metadata freeze record. |

The roadmap should be published as a plan, not as evidence already completed.

---

# 8. Conclusion

Design Science Research needs more than persuasive prose. It needs a way to preserve the relations among problem, context, requirements, artifact, design rationale, evaluation, contribution, boundary conditions, and reuse. The DSR Framework addresses that need by operationalizing DSR as a repository-native artifact package.

The contribution is strongest when stated modestly and precisely. The framework does not solve all of DSR and does not replace scholarly judgment. It makes DSR claims more explicit, inspectable, reusable, citable, and challengeable. It gives researchers and reviewers a structured way to ask: What is the problem? What is the artifact? What knowledge grounds it? What was built? What was demonstrated? What was evaluated? What evidence supports the contribution? Where does the claim apply? What remains unknown?

The recommended next step is to release this white paper as a versioned GitHub artifact package, archive the release through Zenodo, link it through OSF, and use secondary services only as discovery or derivative channels. That path protects canonicality while making the work visible to both human readers and AI/repository systems.

---

# Appendix A. Source Basis and Provenance

This white paper was prepared from three primary review/synthesis files in the Dropbox `DSR Theory Synthesis` folder:

1. `Design science research theory synthesis.md` - theory synthesis, consensus commitments, artifact theory, process theory, evaluation theory, validity/reliability/replication, contribution theory, transparency, and propositions.
2. `operational_synthesis_dsr.md` - operational DSR definition, minimum DSR record architecture, system ontology, artifact operationalization, process model, evaluation model, validation rules, and anti-pattern controls.
3. `dsr_framework_narrative_review.md` - narrative review of the DSR Framework repository and Documentation Protocol, with emphasis on repository-native operationalization and the `artifacts/` directory.

The package also includes supporting structured materials copied into `sources/`, including the concept inventory, competency questions, SKOS vocabulary, unified extraction sidecar, unified extraction chunks, rubrics, and wicked-problem workflow.

## Source-use rule

The white paper should cite the review/synthesis documents as working synthesis materials only when needed. For publication, core DSR claims should cite the underlying literature listed in the references rather than treating the generated synthesis files as independent scholarly authorities.

## Copyright and publication caution

Do not publish copyrighted source PDFs or extraction records containing excessive verbatim source text unless rights have been checked. Publish derived metadata, citation records, concept inventories, and original synthesis text only after human review.

---

# Appendix B. Platform Matrix

| Platform | Canonical? | Best object to post | Recommended timing | Notes |
|---|---:|---|---|---|
| GitHub | Yes | Markdown source, build files, metadata, release records | First | Use as living source of truth. |
| Zenodo | Yes for archival snapshot | GitHub release archive, PDF, unified Markdown, metadata | After GitHub release | Use DOI-bearing snapshot. |
| OSF | No | Project page, optional preprint, links to GitHub/Zenodo, supplemental files | After draft is stable | Use for discovery and open-science hub. |
| Octopus | No | Modular research-process records | After stable paper | Publish problem/method/results/interpretation/application chain if useful. |
| SSRN | No | Preprint PDF | Optional | Use if you want social-science/management/IS preprint discovery. |
| Mendeley Data | No | Data package, not paper | Optional later | Use only for data/materials that are safe and legal to share. |
| Dryad | No | Curated data package, not paper | Usually not needed | Consider only for reusable data requiring data repository curation. |
| ResearchGate | No | Link or licensed full-text mirror | After DOI | Use for visibility. |
| Academia.edu | No | Link or licensed full-text mirror | After DOI | Use for visibility. |
| OER Commons / VIVA Open | No | Teaching derivative, workbook, module | Later | Create after adapting for instruction. |
| arXiv | No | Preprint if category fit is clear | Optional, probably not first | Use only if scope fits. |
| bioRxiv / medRxiv | No | None | Never for this paper | Not relevant. |
| HAL | No | Archive mirror or preprint | Optional | Consider only with metadata consistency plan. |

Decision: keep GitHub + Zenodo as the canonical pair. Everything else should point back to that pair or be clearly labeled as a derivative.

---

# Appendix C. Codex Build Plan

This package is optimized so Codex can finish the release with minimal token use.

## Files Codex should read first

1. `README.md`
2. `codex_handoff.md`
3. `whitepaper/whitepaper_unified.md`
4. `publication_strategy.md`
5. `repo_integration/repo-update-checklist.md`

## Files Codex should avoid reading unless necessary

1. `sources/dsr-source-operational-extractions-unified-part001.yaml`
2. `sources/dsr-source-operational-extractions-unified-part002.yaml`
3. Any full extraction YAML unless revising source registry appendices.

## First Codex task

Create a branch in the DSR Framework repo, add this package under `artifacts/dsr-framework-white-paper/`, run the Markdown assembly script, render HTML and PDF if Pandoc/LaTeX are available, and update only the necessary repository index files.

## Build commands

```bash
python scripts/assemble_whitepaper.py
make html
make pdf
```

If LaTeX is not available, skip PDF and produce HTML plus unified Markdown.

---

# Appendix D. Repository Update Checklist

- Create branch: `whitepaper/dsr-framework-operationalization`.
- Add package under `artifacts/dsr-framework-white-paper/` unless you decide it belongs under `docs/white-papers/`.
- Add or update package README.
- Add white paper entry to root `README.md` under repository map or publication artifacts.
- Add item to `package-inventory.yaml` if the repo inventory tracks white paper artifacts.
- Add item to `artifacts/README.md` if present.
- Add artifact profile or subpackage profile for the white paper package.
- Preserve decision record: white paper type and platform strategy.
- Preserve release checklist and metadata freeze record before DOI release.
- Run YAML/JSON/CFF validation already used by the repository.
- Render unified Markdown, HTML, and PDF if tooling exists.
- Confirm no L5 claims are introduced unless L5 release evidence is completed.
- Commit with a clear message: `Add DSR Framework white paper package`.
- Tag only after final human edit and metadata freeze.

---

# Appendix E. Glossary

| Term | Working meaning |
|---|---|
| Artifact | Designed entity or thing created, instantiated, or specified in DSR. |
| Artifact universal | Reusable artifact kind or design specification distinct from a concrete instance. |
| Artifact instantiation | Concrete implementation, prototype, case, or technical object used to demonstrate or evaluate an artifact. |
| Boundary condition | Contextual condition limiting where a claim applies. |
| Contribution claim | Statement of what reusable or projectable knowledge has been added. |
| Design knowledge | Prescriptive or methodological knowledge connecting problem, intervention, mechanism, outcome, and boundary. |
| Demonstration | Showing artifact feasibility or use; not the same as evaluation unless criteria and evidence are defined. |
| Evaluation evidence | Evidence used to assess artifact, use, effect, or contribution claim. |
| Problem class | Abstracted class of problems beyond the local problem instance. |
| Problem instance | Situated local problem in a specific context. |
| Repository-native operationalization | Representing methodological commitments as structured files, metadata, records, schemas, examples, and release artifacts. |
| Traceability | Explicit link from problem to requirements, design decisions, artifact, evaluation, contribution, and reuse conditions. |

---

# References and parsed source bibliography

The following APA-style list includes the individual literature citations parsed from the DSR source registry, plus repository and professional sources cited in the narrative review.

1. Akoka, J., Comyn-Wattiau, I., Prat, N., & Storey, V. C. (2017). Evaluating knowledge types in design science research: An integrated framework. In A. Maedche et al. (Eds.), Design Science Research in Information Systems and Technology (LNCS 10243, pp. 201-217). Springer. https://doi.org/10.1007/978-3-319-59144-5_12
2. Akoka, J., Comyn-Wattiau, I., Prat, N., & Storey, V. C. (2023). Knowledge contributions in design science research: Paths of knowledge types. Decision Support Systems, 166, 113898. https://doi.org/10.1016/j.dss.2022.113898
3. Alismail, S., Zhang, H., & Chatterjee, S. (2017). A framework for identifying design science research objectives for building and evaluating IT artifacts. In A. Maedche et al. (Eds.), Design Science Research (LNCS 10243, pp. 218-230). Springer. https://doi.org/10.1007/978-3-319-59144-5_13
4. Antony, J., Sony, M., Lameijer, B., Bhat, S., Jayaraman, R., & Gutierrez, L. (2024). Towards a design science research (DSR) methodology for operational excellence (OPEX) initiatives. The TQM Journal, 36(8), 2383-2397. https://doi.org/10.1108/TQM-01-2023-0017
5. Association for Computing Machinery. (2020). *Artifact review and badging policy* (Version 1.1). https://www.acm.org/publications/policies/artifact-review-badging
6. Bagni, G., Godinho Filho, M., Finne, M., & Thurer, M. (2025). Design science research in operations management: Is there a single type? Production Planning & Control, 36(6), 789-807. https://doi.org/10.1080/09537287.2024.2310230
7. Baskerville, R. L., Kaul, M., & Storey, V. C. (2018). Aesthetics in design science research. European Journal of Information Systems, 27(2), 140-153. https://doi.org/10.1080/0960085X.2017.1395545
8. Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. (2018). Design science research contributions: Finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358-376. https://doi.org/10.17705/1jais.00495
9. Baskerville, R., Kaul, M., Pries-Heje, J., & Storey, V. (2019). Inducing creativity in design science research. In B. Tulu, S. Djamasbi, & G. Leroy (Eds.), Extending the boundaries of design science theory and practice: 14th International Conference on Design Science Research in Information Systems and Technology, DESRIST 2019, Proceedings (LNCS 11491, pp. 3-17). Springer. https://doi.org/10.1007/978-3-030-19504-5_1
10. Beinke, J. H., Fitte, C., & Teuteberg, F. (2019). Towards a stakeholder-oriented blockchain-based architecture for electronic health records: Design science research study. Journal of Medical Internet Research, 21(10), e13585. https://doi.org/10.2196/13585
11. Benfell, A. (2021). Modeling functional requirements using tacit knowledge: A design science research methodology informed approach. Requirements Engineering, 26, 25-42. https://doi.org/10.1007/s00766-020-00330-4
12. Brendel, A. B. (2017). C - Synthesis of a design science research framework and methodology. In Applied design science research in the context of smart and sustainable mobility: The case of vehicle supply and demand management in shared vehicle services (p. 119). Cuvillier Verlag.
13. Brendel, A. B., Lembcke, T.-B., Muntermann, J., & Kolbe, L. M. (2021). Toward replication study types for design science research. Journal of Information Technology, 36(3), 198-215. https://doi.org/10.1177/02683962211006429
14. Bub, U. (2018). Towards an integrated method for the engineering of digital innovation and design science research. In A. Benczur et al. (Eds.), Advances in Databases and Information Systems (CCIS 909, pp. 327-338). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-00063-9_31
15. Cauffman, L., & Weggeman, M. (2024). Solution-focused applied psychology: A design science research based protocol. Routledge. https://doi.org/10.4324/9781003404477
16. Contell, J. P., Diaz, O., & Venable, J. R. (2017). DScaffolding: A tool to support learning and conducting design science research. In A. Maedche et al. (Eds.), DESRIST 2017, Lecture Notes in Computer Science, 10243, 441-446. Springer. https://doi.org/10.1007/978-3-319-59144-5_28
17. De Sordi, J. O. (2021). Design Science Research Methodology: Theory Development from Artifacts. Palgrave Macmillan. https://doi.org/10.1007/978-3-030-82156-2
18. Dickhaut, E., Janson, A., & Leimeister, J. M. (2022). Analyzing design knowledge representation in design science research and deriving recommendations to support design knowledge codification. In A. Drechsler et al. (Eds.), Design Science Research: DESRIST 2022, LNCS 13229 (pp. 417-428). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-031-06516-3_31
19. Drechsler, A., Gerber, A., & Hevner, A. (Eds.). (2022). The transdisciplinary reach of design science research: 17th International Conference on Design Science Research in Information Systems and Technology, DESRIST 2022, St Petersburg, FL, USA, June 1-3, 2022, Proceedings. Springer. https://doi.org/10.1007/978-3-031-06516-3
20. FAIR for Research Software Working Group. (2022). *FAIR principles for research software (FAIR4RS principles).* Research Data Alliance. https://doi.org/10.15497/RDA00068
21. Feine, J., Morana, S., & Maedche, A. (2019). Leveraging machine-executable descriptive knowledge in design science research - The case of designing socially-adaptive chatbots. In B. Tulu et al. (Eds.), DESRIST 2019, LNCS 11491 (pp. 76-91). Springer. https://doi.org/10.1007/978-3-030-19504-5_6
22. Gadola, S., Trabucchi, D., & Buganza, T. (2026). Enhancing collaboration and knowledge sharing through intra-organizational platforms: A design science research study. Review of Managerial Science. https://doi.org/10.1007/s11846-026-00996-0
23. Garayo Maiztegui, F. (2023). Design Cycle and Operationalisation of Design Science Research. In Design and Evaluation of an E-Learning Artefact for the Implementation of SAP S/4 Hana (pp. 85-133). Springer Fachmedien Wiesbaden. https://doi.org/10.1007/978-3-658-40731-5_5
24. Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly, 37*(2), 337-355. https://doi.org/10.25300/MISQ/2013/37.2.01
25. Gregor, S., & Zwikael, O. (2024). Design science research and the co-creation of project management knowledge. International Journal of Project Management, 42, 102584. https://doi.org/10.1016/j.ijproman.2024.102584
26. Hansen, M. R. P., & Pries-Heje, J. (2020). A situational knowledge network nexus: Exploring kernel theory extensions using design science research. In J. vom Brocke et al. (Eds.), Design Science Research. Cases (Progress in IS, pp. 261-288). Springer. https://doi.org/10.1007/978-3-030-46781-4_11
27. Henriques, T. A., & O'Neill, H. (2023). Design science research with focus groups - a pragmatic meta-model. International Journal of Managing Projects in Business, 16(1), 119-140. https://doi.org/10.1108/IJMPB-01-2020-0015
28. Hevner, A. R., & Storey, V. C. (2021). Externalities of design science research: Preparation for project success. In L. Chandra Kruse et al. (Eds.), Design Science Research in Information Systems and Technology (LNCS 12807, pp. 118-130). Springer. https://doi.org/10.1007/978-3-030-82405-1_14
29. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75-105.
30. Hevner, A. R., Parsons, J., Brendel, A. B., Lukyanenko, R., Tiefenbeck, V., Tremblay, M. C., & vom Brocke, J. (2024). Transparency in design science research. Decision Support Systems, 182, Article 114236. https://doi.org/10.1016/j.dss.2024.114236
31. Hofmann, S., Mueller, O., & Rossi, M. (Eds.). (2020). Designing for Digital Transformation: Co-Creating Services with Citizens and Industry: 15th International Conference on Design Science Research in Information Systems and Technology, DESRIST 2020, Kristiansand, Norway, December 2-4, 2020, Proceedings (LNCS 12388). Springer. https://doi.org/10.1007/978-3-030-64823-7
32. Hunziker, S., & Blankenagel, M. (2021). Design science research design. In Research Design in Business and Management (pp. 97-116). Springer Fachmedien Wiesbaden. https://doi.org/10.1007/978-3-658-34357-6_6
33. Iivari, J. (2020). Editorial: A critical look at theories in design science research. Journal of the Association for Information Systems, 21(3), 502-519. https://doi.org/10.17705/1jais.00610
34. ISO/IEC/IEEE. (2015). *Systems and software engineering-System life cycle processes* (ISO/IEC/IEEE Standard No. 15288:2015). International Organization for Standardization.
35. ISO/IEC/IEEE. (2019). *Systems and software engineering-Content of life-cycle information items* (ISO/IEC/IEEE Standard No. 15289:2019). International Organization for Standardization.
36. ISO/IEC/IEEE. (2022). *Software, systems and enterprise-Architecture description* (ISO/IEC/IEEE Standard No. 42010:2022). International Organization for Standardization.
37. Johannesson, P., & Perjons, E. (2021). An introduction to design science (2nd ed.). Springer. https://doi.org/10.1007/978-3-030-78132-3
38. Johannesson, P., & Perjons, E. (2021). Systems development and the method framework for design science research. In An Introduction to Design Science (pp. 161-169). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-78132-3_11
39. Krasikov, P., Legner, C., & Eurich, M. (2021). Sourcing the right open data: A design science research approach for the enterprise context. In L. Chandra Kruse et al. (Eds.), Design Science Research in Information Systems and Technologies: DESRIST 2021 (LNCS 12807, pp. 313-327). Springer. https://doi.org/10.1007/978-3-030-82405-1_31
40. Leimeister, J. M., Dickhaut, E., & Janson, A. (2021). Design pattern as a bridge between problem-space and solution-space. In S. Aier et al. (Eds.), Engineering the Transformation of the Enterprise (pp. 137-150). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-84655-8_9
41. Maedche, A., Gregor, S., Morana, S., & Feine, J. (2019). Conceptualization of the problem space in design science research. In B. Tulu et al. (Eds.), Design Science Research. Cases: DESRIST 2019 (LNCS 11491, pp. 18-31). Springer. https://doi.org/10.1007/978-3-030-19504-5_2
42. March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. *Decision Support Systems, 15*(4), 251-266. https://doi.org/10.1016/0167-9236(94)00041-2
43. Meijer, K., Nijssen, M., & Bulles, J. (2018). An evaluation of a design science research artefact in the field of agile enterprise design. In C. Debruyne et al. (Eds.), On the Move to Meaningful Internet Systems. OTM 2017 Workshops (LNCS 10697, pp. 212-219). Springer. https://doi.org/10.1007/978-3-319-73805-5_22
44. Moeller, F., Chandra Kruse, L., Schoormann, T., & Otto, B. (2022). Design principles for boundary spanning in transdisciplinary design science research. In A. Drechsler et al. (Eds.), The Next Wave of Sociotechnical Design (LNCS 13229, pp. 42-54). Springer. https://doi.org/10.1007/978-3-031-06516-3_4
45. Mohammad, J., & Husamaldin, L. (2025). Sustainable project portfolio management - A design science research approach. International Journal of Business Science and Applied Management, 20(3), 38-54.
46. Mullarkey, M. T., Hevner, A. R., Gill, T. G., & Dutta, K. (2019). Citizen data scientist: A design science research method for the conduct of data science projects. In B. Tulu et al. (Eds.), DESRIST 2019, Lecture Notes in Computer Science, 11491, 191-205. Springer. https://doi.org/10.1007/978-3-030-19504-5_13
47. Nagle, T., Sammon, D., & Doyle, C. (2017). Insights into practitioner design science research. In A. Maedche et al. (Eds.), Design Science Research: DESRIST 2017 (LNCS 10243, pp. 414-428). Springer. https://doi.org/10.1007/978-3-319-59144-5_25
48. National Information Standards Organization. (2021). *Reproducibility badging and definitions: A recommended practice* (NISO RP-31-2021). https://doi.org/10.3789/niso-rp-31-2021
49. Ochabski, D. (2026a). *Design Science Research Framework* (Version 1.3.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.20238033
50. Ochabski, D. (2026b). *Documentation Protocol* (Version 1.0.1) [Computer software]. GitHub. https://github.com/dochabski/documentation-protocol/releases/tag/v1.0.1
51. Opdenakker, R., & Talmar, M. (2021). What to consider in a systematic literature review: Three examples from design science research. In A. P. Cardoso Ermel et al. (Eds.), Literature Reviews (pp. 191-199). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-75722-9_8
52. Peffers, K., Tuunanen, T., & Niehaves, B. (2018). Design science research genres: Introduction to the special issue on exemplars and criteria for applicable design science research. European Journal of Information Systems, 27(2), 129–139. https://doi.org/10.1080/0960085X.2018.1458066
53. Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45-77. https://doi.org/10.2753/MIS0742-1222240302
54. Pekkola, S. (2023). Reflections on supervising the postgraduate students' design science research thesis. Journal of Information Systems Education, 34(3), 326-332.
55. Purao, S. (2021). Design science research problems … Where do they come from? In L. Chandra Kruse et al. (Eds.), Lecture Notes in Computer Science: Vol. 12807. DESRIST 2021 (pp. 99-111). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-82405-1_12
56. Reining, S., Ahlemann, F., Mueller, B., & Thakurta, R. (2022). Knowledge accumulation in design science research: Ways to foster scientific progress. The DATA BASE for Advances in Information Systems, 53(1), 10-24.
57. Schmid, A. (2022). Design Science Research Methodology. In Gamification of Electronic Negotiation Training (pp. 51-58). Springer Fachmedien Wiesbaden. https://doi.org/10.1007/978-3-658-38261-2_3
58. Schwartz, D. G., & Yahav, I. (2021). Knowledge Contribution Diagrams for Design Science Research: A Novel Graphical Technique. In L. Chandra Kruse et al. (Eds.), Design Science Research: The Next Wave of Sociotechnical Design (LNCS 12807, pp. 174-187). Springer. https://doi.org/10.1007/978-3-030-82405-1_19
59. Siedhoff, S. (2019). Design science research. In Seizing Business Model Patterns for Disruptive Innovations (pp. 29-43). Springer Fachmedien Wiesbaden. https://doi.org/10.1007/978-3-658-26336-2_3
60. Silva, D. M. A. da, Berkenbrock, G. R., & Berkenbrock, C. D. M. (2017). An approach using the Design Science Research for the development of a collaborative assistive system. In C. Gutwin et al. (Eds.), Collaboration and Technology (LNCS 10391, pp. 180-195). Springer. https://doi.org/10.1007/978-3-319-63874-4_14
61. Simon, H. A. (1996). *The sciences of the artificial* (3rd ed.). MIT Press.
62. Siponen, M., & Klaavuniemi, T. (2021). The primary scientific contribution is hardly a theory in design science research. In L. Chandra Kruse et al. (Eds.), DESRIST 2021, Lecture Notes in Computer Science, 12807, 137-146. Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-82405-1_16
63. Sjöström, J., Chandra Kruse, L., Haj-Bolouri, A., & Flensburg, P. (2018). Software-embedded evaluation support in design science research. In S. Chatterjee et al. (Eds.), Design Science Research in Information Systems and Technologies, DESRIST 2018, Lecture Notes in Computer Science, 10844, 348-362. Springer. https://doi.org/10.1007/978-3-319-91800-6_23
64. Skalli, D., Cherrafi, A., Charkaoui, A., Chiarini, A., Shokri, A., Antony, J., Garza-Reyes, J. A., & Foster, M. (2025). Integrating Lean Six Sigma and Industry 4.0: Developing a design science research-based LSS4.0 framework for operational excellence. Production Planning & Control, 36(8), 1060-1086. https://doi.org/10.1080/09537287.2024.2341698
65. Smuts, H., Winter, R., Gerber, A., & van der Merwe, A. (2022). "Designing" design science research: A taxonomy for supporting study design decisions. In A. Drechsler et al. (Eds.), The Transdisciplinary Reach of Design Science Research (LNCS 13229, pp. 483-495). Springer. https://doi.org/10.1007/978-3-031-06516-3_36
66. Storey, V. C., & Baskerville, R. L. (2021). The digital science field of design science research. In L. Chandra Kruse et al. (Eds.), DESRIST 2021, Lecture Notes in Computer Science, 12807, 343-355. Springer. https://doi.org/10.1007/978-3-030-82405-1_33
67. Storey, V. C., Baskerville, R. L., & Kaul, M. (2025). Reliability in design science research. Information Systems Journal, 35(3), 984-1014. https://doi.org/10.1111/isj.12564
68. Suero Montero, C., & Kapinga, A. F. (2019). Design science research strengthened: Integrating co-creation and co-design. In P. Nielsen & H. C. Kimaro (Eds.), ICT4D 2019, IFIP Advances in Information and Communication Technology (Vol. 551, pp. 486-495). Springer. https://doi.org/10.1007/978-3-030-18400-1_40
69. Thuan, N. H., Drechsler, A., & Antunes, P. (2019). Construction of design science research questions. Communications of the Association for Information Systems, 44, 332-363. https://doi.org/10.17705/1CAIS.04420
70. Trigo, A. (2026). Artefact-driven narrative literature review (ART-NLR): Supporting evidence synthesis for design science research. Journal of Documentation. https://doi.org/10.1108/JD-01-2026-0013
71. Tuunanen, T., Winter, R., & vom Brocke, J. (2024). Dealing with complexity in design science research: A methodology using design echelons. MIS Quarterly, 48(2), 427-458. https://doi.org/10.25300/MISQ/2023/16700
72. van Aken, J., Chandrasekaran, A., & Halman, J. (2016). Conducting and publishing design science research: Inaugural essay of the design science department of the Journal of Operations Management. Journal of Operations Management, 47-48, 1-8. https://doi.org/10.1016/j.jom.2016.06.004
73. van der Merwe, A., Gerber, A., & Smuts, H. (2020). Guidelines for conducting design science research in information systems. In B. Tait et al. (Eds.), Communications in Computer and Information Science (Vol. 1136, pp. 163-178). Springer. https://doi.org/10.1007/978-3-030-35629-3_11
74. Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77-89. https://doi.org/10.1057/ejis.2014.36
75. vom Brocke, J., & Maedche, A. (2019). The DSR grid: Six core dimensions for effectively planning and communicating design science research projects. Electronic Markets, 29, 379-385. https://doi.org/10.1007/s12525-019-00358-7
76. vom Brocke, J., Gau, M., & Maedche, A. (2021). Journaling the design science research process: Transparency about the making of design knowledge. In L. Chandra Kruse et al. (Eds.), Design Science Research (LNCS 12807, pp. 131-136). Springer. https://doi.org/10.1007/978-3-030-82405-1_15
77. vom Brocke, J., Hevner, A., & Maedche, A. (2020). Introduction to design science research. In J. vom Brocke, A. Hevner, & A. Maedche (Eds.), Design Science Research. Cases (Progress in IS, pp. 1-13). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-46781-4_1
78. vom Brocke, J., Hevner, A., & Maedche, A. (Eds.). (2020). Design Science Research. Cases. Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-46781-4
79. vom Brocke, J., Weber, M., & Grisold, T. (2021). Design science research of high practical relevance: Dancing through space and time. In S. Aier et al. (Eds.), Engineering the Transformation of the Enterprise (pp. 115-135). Springer Nature Switzerland AG. https://doi.org/10.1007/978-3-030-84655-8_8
80. Weber, R. (2018). Design-science research. In Research Methods: Information, Systems, and Contexts (pp. 267-288). Elsevier. https://doi.org/10.1016/B978-0-08-102220-7.00011-X
81. Weigand, H., Johannesson, P., & Andersson, B. (2021). An artifact ontology for design science research. Data & Knowledge Engineering, 133, 101878. https://doi.org/10.1016/j.datak.2021.101878
82. zur Heiden, P. (2020). Considering context in design science research: A systematic literature review. In S. Hofmann et al. (Eds.), Design Science Research. Cases (LNCS 12388, pp. 223-234). Springer. https://doi.org/10.1007/978-3-030-64823-7_21
83. Ågerfalk, P. J. (2018). Whither design science research? European Journal of Information Systems, 27(2), 127-128. https://doi.org/10.1080/0960085X.2018.1458065
