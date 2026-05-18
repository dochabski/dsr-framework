# How we are operationalizing DSR through the repositories

The current operationalization can be described as a three-layer artifact system. The layers should be presented as an evolving DSR artifact package, not as final evidence of field-wide validation.

## Layer 1: The DSR Framework repository

The root DSR Framework repository defines the general framework for planning, documenting, evaluating, reviewing, and publishing DSR artifacts. It includes package-control files, metadata, artifact profiles, conformance declarations, specs, models, vocabularies, schemas, templates, checklists, rubrics, records, crosswalks, examples, and documentation [@ochabski_2026_dsr_framework].

Its core claim should remain bounded: it is a reusable-stable DSR documentation and review framework. It should not yet claim independent external validation, universal disciplinary standard status, or automatic validation of downstream DSR projects.

## Layer 2: The DSR theory operational kernel

The nested DSR theory operational kernel turns the DSR theory synthesis into machine-readable and reviewable materials: concept inventory, competency questions, ontology, SKOS vocabulary, SHACL shapes, JSON Schema, YAML templates, crosswalks, source-basis records, and validation records. This layer operationalizes DSR concepts such as artifact universal, artifact instantiation, problem class, evaluation evidence, contribution claim, transparency trace, reliability, replication, and anti-patterns [@weigand_johannesson_andersson_2021_artifact_ontology; @hevner_2024_transparency; @storey_baskerville_kaul_2025_reliability].

This is the most direct example of DSR theory becoming operational: it translates concepts into controlled terms, file structures, validation targets, and review questions.

## Layer 3: White paper and release package

This white paper remains a bounded artifact package under:

```text
artifacts/dsr-framework-white-paper/
```

Recommended retained files include:

```text
README.md
whitepaper/chapters/*.md
whitepaper/whitepaper_unified.md
whitepaper/references.bib
metadata/CITATION.cff
metadata/zenodo-json-template.json
metadata/service-integration-profile.yaml
records/decisions/record-decision-0001-whitepaper-type-and-platforms.yaml
records/reviews/record-whitepaper-citation-and-build-audit.md
records/releases/record-release-checklist-whitepaper.yaml
repo_integration/repo-update-checklist.md
```

This v1.0.0 white paper release preserves the same non-overclaiming discipline as the root framework: it is a citable methodological white paper and artifact package, not a claim of independent external validation, semantic consensus, or L5 archival/publication-ready status.
