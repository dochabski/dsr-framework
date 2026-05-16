<!-- SPDX-License-Identifier: CC0-1.0 -->

# Minimal L1/L2 Documentation Pathway

## Controlled source links

- [templates/minimal-l1-documentation-template.yaml](../../templates/minimal-l1-documentation-template.yaml)
- [templates/minimal-l2-reviewable-documentation-template.yaml](../../templates/minimal-l2-reviewable-documentation-template.yaml)
- [templates/minimal-l1-l2-readme-template.md](../../templates/minimal-l1-l2-readme-template.md)
- [checklists/minimal-l1-l2-documentation-checklist.yaml](../../checklists/minimal-l1-l2-documentation-checklist.yaml)
- [schemas/minimal-l1-l2-documentation.schema.json](../../schemas/minimal-l1-l2-documentation.schema.json)
- [examples/minimal-l1-l2-package/minimal-documentation.yaml](../../examples/minimal-l1-l2-package/minimal-documentation.yaml)
- [scripts/validate-minimal-l1-l2.py](../../scripts/validate-minimal-l1-l2.py)

## Purpose

This pathway gives users a minimal viable way to document a Design Science Research artifact at **L1 documented** or **L2 reviewable** conformance without adopting the full L4 reusable-stable package structure used by this repository.

It is intended for early-stage studies, small artifact records, coursework, dissertation planning, prereview packets, internal lab records, and downstream adopters who need a structured but low-burden documentation record.

This pathway is deliberately **not** a replacement for the full DSR Framework package structure. It is a lightweight entry lane that preserves the framework's core distinctions while reducing file count, automation burden, and release obligations.

## When to use this pathway

Use this pathway when:

- the artifact or study needs to be understandable by another person;
- the work is not yet ready for the full L3/L4 package structure;
- the user needs enough structure to avoid README-only documentation;
- a reviewer needs to inspect basic problem, artifact, evidence, contribution, and boundary claims;
- the user wants a future upgrade path to L3/L4 without starting over.

Do not use this pathway to claim:

- full L4 reusable-stable package status;
- L5 archival/publication-ready status;
- empirical validation not supported by retained evidence;
- downstream artifact certification merely because this framework was used.

## Conformance interpretation

| Level | Minimal meaning in this pathway | Required evidence |
|---|---|---|
| L1 documented | A reader can identify what the artifact is, why it exists, who it is for, what is in scope, how it is licensed, and what its status is. | README, minimal metadata, artifact profile, conformance declaration, package inventory. |
| L2 reviewable | A reviewer can inspect problem framing, requirements, design description, evaluation plan or evidence, contribution claim, traceability, limitations, and review status. | All L1 evidence plus traceability, evaluation plan/evidence, acceptance criteria, review checklist, and tailoring notes. |

## Minimal file set

### L1 documented file set

```text
README.md
LICENSE or LICENSE.md
metadata.yaml
artifact-profile.yaml
conformance-declaration.yaml
package-inventory.yaml
```

### L2 reviewable file set

```text
README.md
LICENSE or LICENSE.md
metadata.yaml
artifact-profile.yaml
conformance-declaration.yaml
package-inventory.yaml
traceability-matrix.yaml
evaluation-plan.yaml or evaluation-record.yaml
review-record.yaml
```

A single combined YAML record is acceptable at L1 or L2 when the user is not ready to maintain separate files. The combined record should use `templates/minimal-l1-documentation-template.yaml` or `templates/minimal-l2-reviewable-documentation-template.yaml`.

## Minimal DSR content requirements

### Identity and scope

- artifact title and short identifier;
- artifact type;
- authors or responsible party;
- version or date;
- repository or storage location, if any;
- intended audience;
- license decision;
- maintenance status;
- non-goals.

### Problem and context

- situated problem instance;
- problem class or generalized problem type;
- context and stakeholder groups;
- practical relevance;
- boundary conditions.

### Artifact and design

- artifact boundary;
- artifact universal or design entity, where applicable;
- concrete instantiation, prototype, document, method, model, template, software object, or intervention;
- design objectives and requirements;
- design rationale or source of design decisions.

### Demonstration and evaluation

- demonstration or use scenario;
- evaluation object;
- evaluation criteria;
- evaluation timing and setting, if known;
- evidence plan or evidence collected;
- limitations of evidence.

### Contribution and reuse

- contribution claim;
- knowledge scope: local, projectable, reusable, general, or not yet claimed;
- intended reuse conditions;
- limitations and anti-overclaiming notes.

### Traceability

At L2, include at least the following edges:

```text
problem -> objective_or_requirement
requirement -> design_decision_or_artifact_feature
design_decision_or_artifact_feature -> evaluation_criterion
evaluation_finding_or_plan -> contribution_claim
contribution_claim -> boundary_condition
```

## Minimal pathway workflow

1. **Select level.** Choose L1 if the goal is documented orientation. Choose L2 if a reviewer must inspect claims and evidence.
2. **Create file set.** Use the L1 or L2 templates. A single combined YAML file is acceptable for small records.
3. **Declare tailoring.** Explain why the full L4 package structure is not being used.
4. **Document artifact boundary.** Separate what was built or specified from the knowledge or contribution being claimed.
5. **Trace core claims.** At L2, link problem, requirement, design, evaluation, contribution, and boundary conditions.
6. **Run validation.** Use `scripts/validate-minimal-l1-l2.py` or equivalent human review.
7. **Record review status.** Mark the record as draft, reviewable draft, reviewed, or superseded.
8. **Upgrade only when needed.** Move toward L3/L4 only when executable procedures, examples, adaptation guidance, provenance, and reusable package controls are needed.

## Upgrade path

| From | To | Add |
|---|---|---|
| L1 | L2 | Traceability, evaluation plan, review checklist, acceptance criteria, limitations. |
| L2 | L3 | Executable or inspectable procedures, examples, validation commands, reproducible checks. |
| L3 | L4 | Adaptation guidance, provenance records, modular documentation, examples, maintained inventory, release discipline. |
| L4 | L5 | Tagged release, DOI-ready metadata, publication/preservation records, archival fixity, final publication appendix, and stronger external review where selected. |

## Acceptance criteria

### L1 acceptance criteria

- The artifact can be identified without private context.
- Scope, audience, status, license, and maintenance expectations are explicit.
- The file set or combined record is parseable and internally consistent.
- Unsupported claims are marked as not claimed, unknown, or pending.

### L2 acceptance criteria

- All L1 criteria pass.
- The problem instance and problem class are documented.
- At least one stakeholder or audience is documented.
- Requirements or objectives are traceable to the problem/context.
- Artifact features or design decisions are traceable to requirements/objectives.
- Evaluation criteria or evidence are traceable to artifact claims.
- Contribution claims are bounded by evidence and limitations.
- A reviewer can mark pass, revise, block, or not applicable for each checklist item.

## Anti-patterns this pathway avoids

- README-only artifact documentation;
- hidden tailoring decisions;
- local implementation described as a general contribution without evidence;
- demonstration treated as evaluation without criteria;
- artifact usefulness treated as sufficient design-knowledge contribution;
- full L4 structure imposed on users who only need L1/L2;
- L5 DOI/publication language used before archival/publication closure.

## Repository integration note

In this repository, the full package may remain L4 reusable-stable while this pathway file and its starter materials support lower-burden downstream L1/L2 adoption. These are different conformance targets and should not be conflated.
