# Design Science Research Theory: Operational Kernel and Repository Validation Framework

This draft artifact package contains the current operational synthesis of DSR theory into a machine-readable kernel for repository-based artifact validation.

## Status

- Artifact status: draft internal artifact package
- Host repository status: v1.0.2 stable DSR Framework package
- Artifact conformance posture: reviewable draft, not a separate stable release
- L5 archival/publication-ready claim: false

This package is retained inside `dsr-framework` so it can be reviewed against the framework before a separate repository or release is considered.

## Purpose

The artifact translates DSR theory synthesis into controlled materials for:

- concept inventory and competency questions;
- OWL/RDF ontology terms;
- SKOS controlled vocabulary terms;
- SHACL validation shapes;
- JSON Schema and YAML authoring templates;
- source-basis and validation records;
- concept-to-ontology coverage review.

## Included files

| Path | Role |
|---|---|
| `concept-inventory.yaml` | Normalized DSR concept inventory for operational framework development. |
| `competency-questions.yaml` | Ontology competency questions for semantic validation. |
| `ontology/dsr-ontology.ttl` | Draft OWL/RDF ontology. |
| `shapes/dsr-shapes.ttl` | Draft SHACL validation shapes. |
| `vocabularies/dsr-skos-controlled-vocabulary.yaml` | YAML SKOS vocabulary source. |
| `vocabularies/dsr-skos-controlled-vocabulary.ttl` | TTL SKOS vocabulary rendering. |
| `schemas/dsr-project.schema.json` | JSON Schema for DSR project/module authoring records. |
| `templates/*.yaml` | YAML authoring templates validated against the schema. |
| `crosswalks/concept-to-ontology-coverage.yaml` | Retained coverage disposition for concept inventory to ontology/SKOS/SHACL alignment. |
| `records/source-basis/record-source-basis-dsr-theory-operational-kernel.yaml` | Source-basis record for local synthesis inputs and extraction corpus context. |
| `records/validation/record-validation-0001-local-preflight.yaml` | Local technical and coverage preflight record. |

## Non-claims

This artifact does not claim:

- that the DSR theory synthesis is complete or exhaustive;
- that identifier-level OWL/RDF coverage is the same as mature semantic adequacy;
- that the ontology has passed independent semantic review;
- that the framework has empirical proof of downstream utility;
- that this artifact is a standalone stable release;
- that L5 archival/publication-ready status has been achieved.

## Next use

Use this artifact as the first self-application target for the DSR Framework. The next substantive step is to validate `documentation-protocol` and `dsr-framework` against the operational kernel, while retaining semantic-review limits around lightweight ontology declarations.
