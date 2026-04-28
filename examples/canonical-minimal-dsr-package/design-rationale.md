# Design Rationale

## Chosen design

A rule-based prioritization method was selected because it is easier to inspect, explain, and adapt than a black-box predictive model in a minimal DSR worked example.

## Alternatives considered

| Alternative | Reason not selected |
|---|---|
| Machine-learning risk prediction | Would require real training data, stronger validity evidence, and fairness evaluation beyond this example. |
| Pure manual prioritization | Would not sufficiently exercise artifact specification, evaluation planning, or transparency crosswalks. |
| Full route optimization | Would shift focus from DSR documentation to algorithm engineering. |

## Rationale

The artifact is intentionally small so the example can exercise framework documentation without introducing unnecessary technical complexity.

## Risk controls

- Synthetic data only.
- Human review required.
- No deployment claim.
- No clinical or emergency decision claim.
- Limitations recorded in every release-facing example file.

## Traceability

Design choices map to:

- R1 data minimization;
- R2 ranked output;
- R3 explanation fields;
- R4 override rationale;
- R5 artificial demonstration;
- R6 limitation disclosure.
