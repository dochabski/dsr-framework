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
