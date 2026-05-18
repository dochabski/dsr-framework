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
