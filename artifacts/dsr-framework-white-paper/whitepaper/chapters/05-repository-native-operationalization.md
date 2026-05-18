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
