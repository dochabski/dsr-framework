---
title: "From Design Science Research Theory to Repository-Native Operationalization: A Narrative Review of the DSR Framework"
date: "2026-05-16"
review_scope: "dochabski/dsr-framework, with documentation-protocol where relevant"
format: "markdown"
approximate_source_registry_size: "71 extraction records; 69 unique works after duplicate DOI/title collapse"
---

# From Design Science Research Theory to Repository-Native Operationalization: A Narrative Review of the DSR Framework

## Executive summary

The `dsr-framework` repository is best understood as a **Design Science Research (DSR) artifact package about DSR artifact packages**. Its object of design is not a single application, method paper, or ordinary documentation set. It is a repository-native framework for making DSR work explicit, inspectable, reusable, citable, and reviewable. In DSR terms, it functions as a compound artifact: a framework, method/protocol artifact, model/taxonomy package, set of templates and checklists, record system, validation scaffold, and documentation artifact (Ochabski, 2026a). Its sibling dependency, the `documentation-protocol` repository, supplies the meta-protocol for source-of-truth discipline, package conformance, review records, release controls, preservation logic, and non-overclaiming (Ochabski, 2026b).

The repository emerges coherently from the DSR literature. It preserves the core DSR commitments that run from artifact-centered inquiry and build/evaluate reasoning through problem relevance, rigorous knowledge grounding, evaluation, communication, and design-knowledge contribution (Hevner et al., 2004; March & Smith, 1995; Peffers et al., 2007; Weber, 2018). It then adds later DSR concerns that the field has increasingly made explicit: problem-space conceptualization, artifact ontology, knowledge contribution pathways, DSR transparency, design knowledge codification, reliability, replication, projectability, genre plurality, responsible use, and publication readiness (Akoka et al., 2023; Baskerville et al., 2018; Hevner et al., 2024; Maedche et al., 2019; Storey et al., 2025; Weigand et al., 2021).

The strongest feature of the repository is its **traceability discipline**. The framework does not merely tell DSR authors to be rigorous. It operationalizes rigor as structured files: manifests, artifact profiles, package inventories, conformance declarations, models, vocabularies, schemas, templates, checklists, records, crosswalks, examples, rubrics, and nested artifacts. This makes the repository more than a prose guide. It is a designed environment for retaining evidence from problem framing through contribution claims and release decisions. That design choice aligns strongly with recent calls for DSR transparency and design-knowledge accumulation (Dickhaut et al., 2022; Hevner et al., 2024; Reining et al., 2022; vom Brocke & Maedche, 2019).

The principal limitation is also visible in the repository's own non-claims: the framework has L4 reusable-stable package status, but it does not claim L5 archival/publication-ready status, independent external validation, semantic adequacy of its ontology, empirical proof of downstream utility, or automatic validation of artifacts that use it (Ochabski, 2026a). That restraint is methodologically important. In DSR terms, the repository has strong artifact specification, transparency, packaging, and self-application evidence; it does not yet have strong naturalistic or external-user evaluation evidence for utility claims.

## Review scope and source basis

This review distinguishes between two layers:

1. **DSR theory as captured in the scholarly and professional literature.** This includes the foundational DSR lineage, newer DSR methodology sources, and supporting professional documentation and artifact-stewardship norms.
2. **The repository operationalization.** This includes the `dsr-framework` GitHub repository and, where relevant, the `documentation-protocol` repository as the upstream documentation and packaging protocol.

The DSR source registry parsed for this review contains **71 extraction records** and **69 unique source works after collapsing duplicate DOI/title records**. Its role distribution is: process_model (31), validation_source (9), contribution_theory (8), other (8), vocabulary_source (5), evaluation_theory (4), transparency_guidance (3), artifact_typology (2), reporting_guidance (1). Its DSR genre distribution is: design_science_research_methodology (32), application_case (13), design_knowledge_synthesis (8), other (7), reporting_guidance (4), evaluation_framework (2), reliability_replication (2), artifact_typology (1), action_design_research (1), design_theory_contribution (1). Its source-type distribution is: methodology_paper (18), chapter (17), conceptual_paper (10), empirical_article (8), journal_article (7), book (7), conference_paper (1), book_chapter (1), review (1), other (1). Appendix A lists the parsed records as individual source citations rather than treating the combined extraction files as a single undifferentiated source.

This is a narrative review, not a new systematic review. The purpose is interpretive: to explain how the repository's architecture, especially the `artifacts/` directory and the nested DSR theory operational kernel, emerges from DSR theory and where the operationalization is strongest or still under-evaluated.

## 1. The DSR theory base: from artificial science to artifact-package governance

DSR begins from the artificial-science insight that designed artifacts can be legitimate objects of research when they are created, evaluated, and connected to knowledge (Simon, 1996). In information systems, March and Smith (1995) formalized design as build-and-evaluate work around constructs, models, methods, and instantiations. Hevner et al. (2004) then made the relevance/rigor framing canonical: DSR must address real problems in an environment while drawing from and contributing to a knowledge base. Peffers et al. (2007) offered a process methodology linking problem identification, objectives, design and development, demonstration, evaluation, and communication.

The `dsr-framework` repository carries this lineage forward by asking: **what would a DSR project look like if these commitments were encoded as repository-native information items?** The answer is a structured package in which artifact identity, problem relevance, solution grounding, design decisions, demonstration, evaluation, contribution positioning, transparency, review, and release evidence are separately represented and cross-linked (Ochabski, 2026a). This is not a rejection of DSR theory's narrative and judgment-based traditions. It is an operational layer that makes those traditions inspectable.

A key theoretical move is the shift from “the artifact” as a local thing to **the artifact as a reusable, typed design entity with evidence obligations**. Weigand et al. (2021) argue for an artifact ontology that distinguishes artifact universals, instantiations, make plans, use plans, and related claims. The DSR Framework mirrors this by separating the framework artifact type from its repository instantiation and by requiring downstream users not to confuse package completion with empirical utility or scholarly contribution (Ochabski, 2026a). That distinction is central to the repo's anti-overclaiming stance.

## 2. Problem relevance and problem-space operationalization

DSR literature repeatedly warns that artifact development without a well-grounded problem is weak DSR. Maedche et al. (2019) make problem-space conceptualization explicit, Purao (2021) interrogates where DSR problems come from, and zur Heiden (2020) emphasizes context. The repository responds by treating problem-space documentation as a first-class package concern rather than an introductory paragraph. The DSR Framework overview, artifact profile, templates, checklists, and wicked-problem workflow all require some form of problem/context/stakeholder articulation and boundary-condition logic (Ochabski, 2026a).

The repository's `docs/wicked-problem-resolution-workflow.md` is especially important here. It translates DSR problem theory into a process artifact: problem situation capture, problem instance/class abstraction, stakeholder and context mapping, causal/leverage modeling, requirements derivation, solution-space search, artifact design, pilot evaluation, claim-evidence mapping, knowledge codification, and scale/reframe decisions. This structure aligns with DSR's need to move from a situated problem instance toward a problem class without pretending that wicked socio-technical problems can be solved once and for all (Maedche et al., 2019; Purao, 2021; vom Brocke et al., 2021).

This is one of the repository's most persuasive operational contributions. It translates “problem relevance” from a general principle into a concrete trace: problem -> objective -> requirement -> design decision -> evaluation -> contribution. That trace is exactly what many DSR writeups lack when they present a working artifact but leave the reader uncertain about the relevance claim, design target, evaluation criteria, or transfer conditions.

## 3. Solution grounding, design rationale, and artifact ontology

DSR rigor requires more than “we built something.” The artifact must be grounded in prior knowledge, alternative solutions, theory, design patterns, methods, technologies, and contextual constraints (Hevner et al., 2004; Weber, 2018). The repository operationalizes that requirement through source-basis records, solution-space templates, crosswalks, controlled vocabularies, and build-transparency records (Ochabski, 2026a). In the DSR literature, this fits the move toward better representation of design knowledge and design rationale (Dickhaut et al., 2022; Leimeister et al., 2021; Reining et al., 2022).

The artifact-ontology dimension is particularly important. A common DSR failure mode is to treat a software prototype, workshop method, checklist, framework, or dataset as self-explanatory. Weigand et al. (2021) show why artifact identity requires ontological precision. The DSR Framework follows that logic by distinguishing artifact type, artifact boundary, artifact instance, make plan, use plan, capacity claims, contribution claims, and reuse constraints (Ochabski, 2026a). This improves reviewability because a reviewer can ask: what exactly is the designed entity, what instantiates it, what claim is made about it, what evidence supports that claim, and what remains outside scope?

The framework also accounts for artifact plurality. The source registry includes artifact typology, methodology, application-case, evaluation, reporting, contribution, and replication sources. That breadth matters because DSR artifacts are not only software applications. They can be methods, models, constructs, taxonomies, design principles, frameworks, ontologies, socio-technical interventions, templates, checklists, and documentation packages (Baskerville et al., 2018; Johannesson & Perjons, 2021; Smuts et al., 2022; Weber, 2018). The repository's compound artifact profile is therefore theoretically defensible: a DSR documentation framework can itself be a DSR artifact when it is designed, bounded, evaluated, and positioned as a design-knowledge contribution.

## 4. Contribution theory: from artifact delivery to design knowledge

The repository's contribution logic is anchored in a major DSR distinction: a useful artifact is not automatically a scientific contribution. Gregor and Hevner (2013) argued for positioning and presenting DSR contributions for maximum impact; Baskerville et al. (2018) warned against an unbalanced artifact/theory framing; Siponen and Klaavuniemi (2021) argued that the primary scientific contribution in DSR need not always be a theory. Akoka et al. (2023) further refined contribution logic by representing DSR knowledge contributions as paths of knowledge types, combining knowledge goals, knowledge scope, and dynamic progression.

The DSR Framework operationalizes contribution theory in three ways. First, it distinguishes **artifact utility**, **artifact quality**, and **knowledge contribution**. Second, it captures knowledge goals and scope, including local/idiographic and broader/nomothetic or projectable claims. Third, it requires contribution claims to be supported by source-basis, evaluation, boundary-condition, and transparency records rather than by author assertion alone (Ochabski, 2026a). This corresponds to the literature's shift from one-size-fits-all contribution claims toward more nuanced contribution positioning (Akoka et al., 2023; Baskerville et al., 2018; Iivari, 2020; Peffers et al., 2018).

The source-to-framework alignment crosswalk is a notable implementation of this principle. It does not merely cite DSR literature in a bibliography; it maps sources to framework constructs and target files. That move advances design knowledge accumulation because it turns references into traceable design dependencies. The limitation is that source-to-framework mapping remains a scholarly and design judgment. It should not be mistaken for independent evidence that every mapping is semantically adequate or that the framework exhausts DSR theory.

## 5. Evaluation, validity, reliability, replication, and projectability

Evaluation is a core DSR obligation but also one of the most misapplied. Venable et al. (2016) distinguish evaluation strategies and settings; Akoka et al. (2017) connect knowledge types to evaluation; Sjöström et al. (2018) explore software-embedded evaluation support; Johannesson and Perjons (2021) present evaluation as part of the method framework for design science. The DSR Framework translates these concerns into evaluation-plan and evaluation-report templates, evaluation-alignment models, checklists, and claim-evidence matrices (Ochabski, 2026a).

The strongest operational decision is the repository's strict distinction between **demonstration** and **evaluation**. Demonstration can show feasibility, use, or instantiation; evaluation tests claims against criteria, evidence, stakeholders, context, methods, and limitations. This distinction protects the framework from a common DSR overclaim: “we showed the artifact, therefore we evaluated it.” It also supports projectability because downstream users need to know not only that an artifact was used but under what conditions its claims were assessed.

The repository also incorporates emerging reliability and replication concerns. Brendel et al. (2021) develop replication study types for DSR, and Storey et al. (2025) analyze reliability in DSR. The DSR Framework's reliability, replication, and projectability layer is therefore well grounded. It appropriately avoids treating exact replication as the only cumulative-science ideal for situated DSR. Instead, it supports adaptation, boundary-condition awareness, context documentation, design-knowledge codification, and re-instantiation logic (Brendel et al., 2021; Reining et al., 2022; Storey et al., 2025).

## 6. Transparency as the repository's central design principle

Recent DSR literature has moved transparency from a generic reporting virtue to a specific DSR quality construct. vom Brocke and Maedche (2019) proposed the DSR Grid for planning and communicating DSR across six dimensions. vom Brocke et al. (2021) emphasized journaling the making of design knowledge. Hevner et al. (2024) formalized transparency across process, problem space, solution space, build, evaluation, and contribution. The DSR Framework is deeply shaped by this transparency turn.

The repository operationalizes transparency by making it structural. Process transparency appears through change histories, decisions, records, and release traces. Problem-space transparency appears through problem/context/stakeholder materials. Solution-space transparency appears through source-basis records and crosswalks. Build transparency appears through design rationale and artifact specification. Evaluation transparency appears through evaluation plans, reports, criteria, and claim-evidence mapping. Contribution transparency appears through contribution models and positioning records (Ochabski, 2026a).

This is the point at which GitHub becomes more than a host. In the DSR Framework, GitHub functions as a research artifact stewardship environment: version control, metadata, root package files, schemas, records, crosswalks, release notes, and examples become part of the designed artifact. This move is compatible with professional artifact-review and reproducibility practices, including artifact badging, reproducibility definitions, FAIR research software principles, and systems/software information-item standards (Association for Computing Machinery, 2020; FAIR for Research Software Working Group, 2022; ISO/IEC/IEEE, 2019; National Information Standards Organization, 2021).

## 7. The Documentation Protocol as meta-protocol

The `documentation-protocol` repository is not merely ancillary. It is the meta-protocol that explains why the DSR Framework is structured as a package of YAML source-of-truth specifications, Markdown guidance, templates, checklists, schemas, inventories, traceability matrices, validation records, release records, and conformance declarations (Ochabski, 2026b). It generalizes a repository-centered documentation discipline for open research and design artifacts, while the DSR Framework applies that discipline to the DSR domain.

The relationship is recursive but controlled. The Documentation Protocol uses the DSR Framework as its first retained pilot validation. The DSR Framework uses the Documentation Protocol as its package-governance model. This is a legitimate DSR self-application pattern, but it has a known risk: self-application can support coherence and structural adequacy, but it cannot by itself prove external adoption, independent validity, empirical effectiveness, or semantic adequacy (Ochabski, 2026b). The repositories are clear about this boundary, which is methodologically sound.

The meta-protocol also imports professional norms that DSR theory alone does not fully provide: package conformance levels, source-of-truth separation, release and preservation records, citation metadata, licensing, validation scaffolds, and service integration. These are not replacements for DSR evaluation. They are infrastructure for making DSR artifacts more reviewable, reusable, and preservable.

## 8. The `artifacts/` directory and the DSR theory operational kernel

The `artifacts/` directory is central to the repository's current maturity. The directory explicitly separates **examples** from **bounded artifact packages**. Examples demonstrate framework use; artifacts are independently reviewable theory, model, validation, or domain artifacts developed inside the repository before they are ready for their own repository, DOI, release cadence, or audience (Ochabski, 2026a).

The main nested artifact is `artifacts/dsr-theory-operational-kernel`. Its purpose is to translate DSR theory synthesis into a machine-readable and reviewable kernel: concept inventory, competency questions, OWL/RDF ontology, SKOS controlled vocabulary, SHACL shapes, JSON Schema, YAML templates, crosswalks, source-basis records, validation records, and validation targets (Ochabski, 2026a). This is one of the most ambitious aspects of the repository because it moves from prose theory to semantic and validation artifacts.

The operational kernel is an appropriate DSR artifact because it tries to solve a real methodological problem: DSR concepts are rich, heterogeneous, and often inconsistently documented. The kernel offers a controlled vocabulary and ontology-backed scaffold for validation. Its design is well aligned with artifact ontology, knowledge contribution, transparency, and reviewability literature (Akoka et al., 2023; Hevner et al., 2024; Weigand et al., 2021). However, the kernel's own non-claims matter: identifier-level coverage is not semantic adequacy, OWL/RDF coverage is not disciplinary consensus, and local validation is not independent semantic review. This restraint should be preserved.

A helpful way to read the artifacts directory is as a **DSR laboratory inside the DSR Framework**. The root package defines the framework, while the nested operational kernel tests whether DSR theory can be made into a structured, machine-readable, validation-oriented artifact. That makes the repository more convincing because it does not leave the framework as only a documentation proposal; it uses the framework to generate and review a concrete subordinate artifact.

## 9. Assessment rubrics and reviewability

The current v1.3.0 repository includes DSR assessment rubrics for problem research-worthiness, solvability, problem framing, context and stakeholder adequacy, requirements traceability, input knowledge, design rationale, demonstration, evaluation alignment, contribution quality, projectability, reliability/replication, responsible design, repository documentation conformance, and transparency trace quality (Ochabski, 2026a). This addition is methodologically important because it turns reviewability into a reusable instrument layer.

The rubrics align with the literature's insistence that DSR quality is multidimensional. There is no single “pass/fail” criterion for DSR: contribution, artifact maturity, context, evaluation burden, genre, transparency, validity, and reuse conditions interact (Baskerville et al., 2018; Peffers et al., 2018; Smuts et al., 2022; Venable et al., 2016). The rubrics provide structured prompts for reviewer judgment. They should not be hardened prematurely into universal SHACL-style validation rules, because many DSR judgments remain contextual and genre-sensitive.

## 10. Strengths of the operationalization

The repository has six major strengths.

First, it preserves DSR's identity boundary. It repeatedly distinguishes DSR from routine implementation, consulting, retrospective documentation, and purely explanatory research. This aligns with core DSR commitments to artifact creation, problem relevance, rigorous grounding, evaluation, and design knowledge (Hevner et al., 2004; Weber, 2018).

Second, it operationalizes traceability rather than merely recommending it. The package architecture creates places for problem-to-requirement, requirement-to-design, design-to-evaluation, evaluation-to-claim, and claim-to-contribution evidence. This is a significant practical advance over prose-only DSR guidance.

Third, it makes non-overclaiming a design rule. L4 reusable-stable status is separated from L5 archival/publication-ready status; demonstration is separated from evaluation; package completion is separated from utility evidence; self-application is separated from external validation (Ochabski, 2026a, 2026b). This supports review trust.

Fourth, it treats design knowledge as codifiable and reusable without denying context. The framework supports knowledge goals, knowledge scope, boundary conditions, projectability, and reliability/replication concerns (Akoka et al., 2023; Brendel et al., 2021; Storey et al., 2025).

Fifth, it bridges scholarly and professional literatures. DSR theory supplies the artifact, contribution, evaluation, and transparency logic. Professional artifact/documentation standards supply package structure, metadata, records, conformance, licensing, release, and preservation logic (Association for Computing Machinery, 2020; ISO/IEC/IEEE, 2019; National Information Standards Organization, 2021).

Sixth, the artifacts directory demonstrates self-application. The DSR theory operational kernel is a concrete artifact that uses the framework's own logic to structure DSR theory into ontology, vocabulary, schemas, and validation records. That gives the repository a stronger DSR identity than a static guide would have.

## Conclusion

The `dsr-framework` repository is a credible and unusually explicit attempt to operationalize DSR theory as a GitHub-native artifact package. It emerges from the DSR literature by translating artifact centrality, problem relevance, rigorous grounding, build/evaluate logic, contribution positioning, evaluation alignment, transparency, reliability, replication, projectability, and genre plurality into structured repository files and review instruments. The `documentation-protocol` provides the meta-level documentation and release discipline; the `artifacts/` directory, especially the DSR theory operational kernel, demonstrates the framework's self-application as a nested DSR artifact.

The review judgment is favorable but bounded. The repository is strong as an L4 reusable-stable operational framework and as a design-knowledge codification artifact. It should not yet be treated as empirically validated, independently semantically reviewed, or L5 archival/publication-ready. Its greatest methodological contribution is not that it “solves” DSR documentation; it makes DSR claims, evidence, boundaries, and reuse conditions sufficiently explicit that they can be reviewed, challenged, improved, and accumulated.

# Appendix A. Parsed DSR source registry records

The following table is generated from the parsed operational extraction corpus. Duplicate-record works are retained in the table for provenance, while the reference list collapses duplicate DOI/title records.

| # | Short citation | Year | Source role | DSR genre | Title |
|---:|---|---:|---|---|---|
| 1 | Akoka et al. (2023) | 2023 | contribution_theory | design_knowledge_synthesis | Knowledge contributions in design science research: Paths of knowledge types |
| 2 | Hevner et al. (2024) | 2024 | transparency_guidance | design_science_research_methodology | Transparency in design science research |
| 3 | Weigand, Johannesson, and Andersson (2021) | 2021 | artifact_typology | artifact_typology | An artifact ontology for design science research |
| 4 | Gregor & Zwikael, 2024 | 2024 | process_model | design_science_research_methodology | Design science research and the co-creation of project management knowledge |
| 5 | Weber (2018) | 2018 | evaluation_theory | design_science_research_methodology | Design-science research |
| 6 | Reining et al. (2022) | 2022 | other | design_knowledge_synthesis | Knowledge Accumulation in Design Science Research |
| 7 | Bub (2018) | 2018 | process_model | design_science_research_methodology | Towards an Integrated Method for the Engineering of Digital Innovation and Design Science Research |
| 8 | Suero Montero & Kapinga (2019) | 2019 | process_model | design_science_research_methodology | Design Science Research Strengthened: Integrating Co-creation and Co-design |
| 9 | Baskerville et al. (2019) | 2019 | process_model duplicate-record work | design_science_research_methodology | Inducing Creativity in Design Science Research |
| 10 | Baskerville et al. (2019) | 2019 | process_model duplicate-record work | design_science_research_methodology | Inducing Creativity in Design Science Research |
| 11 | Mullarkey et al. (2019) | 2019 | process_model | action_design_research | Citizen Data Scientist: A Design Science Research Method for the Conduct of Data Science Projects |
| 12 | Maedche et al. (2019) | 2019 | vocabulary_source | design_science_research_methodology | Conceptualization of the Problem Space in Design Science Research |
| 13 | Feine, Morana, and Maedche (2019) | 2019 | other | design_science_research_methodology | Leveraging Machine-Executable Descriptive Knowledge in Design Science Research - The Case of Designing Socially-Adaptive Chatbots |
| 14 | van der Merwe et al. (2020) | 2020 | process_model | design_science_research_methodology | Guidelines for Conducting Design Science Research in Information Systems |
| 15 | vom Brocke, Hevner, and Maedche (2020) | 2020 | other | other | Design Science Research. Cases |
| 16 | vom Brocke, Hevner, and Maedche (2020) | 2020 | process_model | design_science_research_methodology | Introduction to Design Science Research |
| 17 | Hansen and Pries-Heje (2020) | 2020 | other | application_case | A Situational Knowledge Network Nexus: Exploring Kernel Theory Extensions Using Design Science Research |
| 18 | Hofmann, Mueller, and Rossi (2020) | 2020 | vocabulary_source | other | Designing for Digital Transformation |
| 19 | zur Heiden (2020) | 2020 | transparency_guidance | reporting_guidance | Considering Context in Design Science Research |
| 20 | Opdenakker and Talmar (2021) | 2021 | other | design_knowledge_synthesis | What to Consider in a Systematic Literature Review: Three Examples from Design Science Research |
| 21 | Johannesson & Perjons (2021) | 2021 | process_model | design_science_research_methodology | An Introduction to Design Science |
| 22 | Johannesson and Perjons (2021, ch. 11) | 2021 | process_model | design_science_research_methodology | Systems Development and the Method Framework for Design Science Research |
| 23 | De Sordi (2021) | 2021 | process_model | design_science_research_methodology | Design Science Research Methodology |
| 24 | Purao (2021) | 2021 | process_model | design_science_research_methodology | Design Science Research Problems … Where Do They Come From? |
| 25 | Hevner and Storey (2021) | 2021 | process_model | design_science_research_methodology | Externalities of Design Science Research: Preparation for Project Success |
| 26 | vom Brocke, Gau, and Maedche (2021) | 2021 | transparency_guidance | reporting_guidance | Journaling the Design Science Research Process. Transparency About the Making of Design Knowledge |
| 27 | Siponen & Klaavuniemi (2021) | 2021 | contribution_theory | other | The Primary Scientific Contribution is Hardly a Theory in Design Science Research |
| 28 | Schwartz and Yahav (2021) | 2021 | contribution_theory | reporting_guidance | Knowledge Contribution Diagrams for Design Science Research: A Novel Graphical Technique |
| 29 | Krasikov et al. (2021) | 2021 | process_model | application_case | Sourcing the Right Open Data: A Design Science Research Approach for the Enterprise Context |
| 30 | Storey & Baskerville (2021) | 2021 | other | other | The Digital Science Field of Design Science Research |
| 31 | vom Brocke, Weber, and Grisold (2021) | 2021 | process_model | design_science_research_methodology | Design Science Research of High Practical Relevance |
| 32 | Leimeister, Dickhaut, and Janson (2021) | 2021 | vocabulary_source | design_knowledge_synthesis | Design Pattern as a Bridge Between Problem-Space and Solution-Space |
| 33 | Drechsler, Gerber, and Hevner (2022) | 2022 | vocabulary_source | other | The Transdisciplinary Reach of Design Science Research |
| 34 | Dickhaut, Janson, and Leimeister (2022) | 2022 | reporting_guidance | design_knowledge_synthesis | Analyzing Design Knowledge Representation in Design Science Research and Deriving Recommendations to Support Design Knowledge Codification |
| 35 | Smuts et al. (2022) | 2022 | artifact_typology | design_science_research_methodology | "Designing" Design Science Research - A Taxonomy for Supporting Study Design Decisions |
| 36 | Moeller et al. (2022) | 2022 | contribution_theory | design_knowledge_synthesis | Design Principles for Boundary Spanning in Transdisciplinary Design Science Research |
| 37 | Akoka et al. (2017) | 2017 | evaluation_theory | evaluation_framework | Evaluating Knowledge Types in Design Science Research |
| 38 | Alismail et al. (2017) | 2017 | other | design_science_research_methodology | A Framework for Identifying Design Science Research Objectives for Building and Evaluating IT Artifacts |
| 39 | Nagle, Sammon, and Doyle (2017) | 2017 | process_model | design_science_research_methodology | Insights into Practitioner Design Science Research |
| 40 | Contell, Diaz, and Venable (2017) | 2017 | process_model | design_science_research_methodology | DScaffolding: A Tool to Support Learning and Conducting Design Science Research |
| 41 | Silva, Berkenbrock, and Berkenbrock (2017) | 2017 | validation_source | application_case | An Approach Using the Design Science Research for the Development of a Collaborative Assistive System |
| 42 | Meijer, Nijssen, and Bulles (2018) | 2018 | validation_source | application_case | An Evaluation of a Design Science Research Artefact in the Field of Agile Enterprise Design |
| 43 | Sjöström et al. (2018) | 2018 | evaluation_theory | evaluation_framework | Software-Embedded Evaluation Support in Design Science Research |
| 44 | Siedhoff (2019) | 2019 | process_model | application_case | Design science research |
| 45 | Hunziker and Blankenagel (2021) | 2021 | process_model | design_science_research_methodology | Design Science Research Design |
| 46 | Schmid (2022) | 2022 | process_model | application_case | Design Science Research Methodology |
| 47 | Garayo Maiztegui (2023) | 2023 | process_model | application_case | Design Cycle and Operationalisation of Design Science Research |
| 48 | Baskerville, Kaul, and Storey (2018) | 2018 | evaluation_theory | design_science_research_methodology | Aesthetics in design science research |
| 49 | Brendel et al. (2021) | 2021 | validation_source | reliability_replication | Toward replication study types for design science research |
| 50 | Thuan, Drechsler, and Antunes (2019) | 2019 | vocabulary_source | design_science_research_methodology | Construction of Design Science Research Questions |
| 51 | Peffers, Tuunanen, and Niehaves 2018 | 2018 | contribution_theory | design_knowledge_synthesis | Design science research genres |
| 52 | Bagni et al. (2025) | 2025 | other | other | Design science research in operations management: is there a single type? |
| 53 | Baskerville et al. (2018) | 2018 | contribution_theory | design_knowledge_synthesis | Design Science Research Contributions |
| 54 | Tuunanen, Winter, and vom Brocke (2024) | 2024 | process_model | design_science_research_methodology | Dealing with Complexity in Design Science Research: A Methodology Using Design Echelons |
| 55 | Mohammad and Husamaldin (2025) | 2025 | validation_source | application_case | Sustainable Project Portfolio Management - A Design Science Research Approach |
| 56 | van Aken et al. (2016) | 2016 | process_model duplicate-record work | design_science_research_methodology | Conducting and publishing design science research |
| 57 | Iivari (2020) | 2020 | contribution_theory | design_theory_contribution | Editorial: A Critical Look at Theories in Design Science Research |
| 58 | Henriques and O'Neill (2023) | 2023 | process_model | design_science_research_methodology | Design science research with focus groups - a pragmatic meta-model |
| 59 | Storey et al. (2025) | 2025 | validation_source | reliability_replication | Reliability in design science research |
| 60 | Skalli et al. (2025) | 2025 | validation_source | application_case | Integrating Lean Six Sigma and Industry 4.0: developing a design science research-based LSS4.0 framework for operational excellence |
| 61 | van Aken et al. (2016) | 2016 | process_model duplicate-record work | design_science_research_methodology | Conducting and publishing design science research |
| 62 | Trigo (2026) | 2026 | process_model | design_science_research_methodology | Artefact-driven narrative literature review (ART-NLR): supporting evidence synthesis for design science research |
| 63 | Benfell (2021) | 2021 | process_model | application_case | Modeling functional requirements using tacit knowledge: a design science research methodology informed approach |
| 64 | Pekkola (2023) | 2023 | process_model | design_science_research_methodology | Reflections on Supervising the Postgraduate Students' Design Science Research Thesis |
| 65 | Gadola et al. (2026) | 2026 | validation_source | application_case | Enhancing collaboration and knowledge sharing through intra-organizational platforms: a design science research study |
| 66 | Cauffman and Weggeman (2024) | 2024 | validation_source | application_case | Solution-Focused Applied Psychology |
| 67 | Brendel (2017) | 2017 | process_model | design_science_research_methodology | C - Synthesis of a Design Science Research Framework and Methodology |
| 68 | vom Brocke and Maedche (2019) | 2019 | process_model | reporting_guidance | The DSR grid: six core dimensions for effectively planning and communicating design science research projects |
| 69 | Beinke et al. (2019) | 2019 | validation_source | application_case | Towards a Stakeholder-Oriented Blockchain-Based Architecture for Electronic Health Records: Design Science Research Study |
| 70 | Antony et al. (2024) | 2024 | process_model | design_science_research_methodology | Towards a design science research (DSR) methodology for operational excellence (OPEX) initiatives |
| 71 | Ågerfalk (2018) | 2018 | contribution_theory | other | Whither design science research? |

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
