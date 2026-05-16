<!-- SPDX-License-Identifier: CC0-1.0 -->

# [Artifact title]

## Status

- Conformance target: `l1_documented` or `l2_reviewable`
- Version/date: `[version or date]`
- Review status: `[draft | reviewable_draft | reviewed | superseded]`
- Full L4 package adopted: `false`

## Purpose

Describe the artifact in one paragraph. State what it is for and what problem it helps address.

## Audience

List the primary users, reviewers, maintainers, or adopters.

## Scope

### In scope

- ...

### Out of scope

- ...

### Non-goals

- ...

## DSR positioning

### Problem instance

Describe the situated problem.

### Problem class

Describe the generalized class of problems this instance represents.

### Artifact or design entity

Describe the artifact boundary and whether the documented object is a reusable design entity, a concrete instantiation, a method, a model, a template, a software object, a process artifact, or another artifact type.

## Evaluation and evidence

For L1, state current evidence status. For L2, summarize evaluation criteria, evidence plan, findings, or limitations.

## Contribution and reuse

State what contribution is claimed and what is not claimed. Include boundary conditions and reuse conditions.

## Files

| File | Role | Required for |
|---|---|---|
| `metadata.yaml` or combined YAML record | Basic identity and status metadata | L1 |
| `artifact-profile.yaml` or combined YAML record | Artifact scope and DSR positioning | L1 |
| `conformance-declaration.yaml` or combined YAML record | Declared conformance and tailoring | L1 |
| `traceability-matrix.yaml` or combined YAML record | Problem/design/evaluation/contribution trace | L2 |
| `evaluation-plan.yaml` or combined YAML record | Evaluation plan or evidence record | L2 |
| `review-record.yaml` or combined YAML record | Review status and acceptance criteria | L2 |

## License

State the license and any restrictions or third-party content notes.
