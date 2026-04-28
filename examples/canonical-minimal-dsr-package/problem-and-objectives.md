# Problem and Objectives

## Problem statement

During heat-risk events, outreach teams need a transparent and reviewable way to prioritize neighborhoods for cooling-center outreach. Existing ad hoc prioritization may be difficult to explain, repeat, adapt, or evaluate.

## Problem class

Operational prioritization under constrained resources, uncertain need, and public-accountability requirements.

## Local synthetic instance

A fictional public-health team must plan a two-hour outreach route across six synthetic neighborhoods using public, aggregate, non-identifying indicators.

## Objectives

1. Represent prioritization criteria in a transparent form.
2. Produce a ranked list of outreach stops.
3. Explain each ranking using visible criteria.
4. Allow human override with recorded rationale.
5. Keep data requirements minimal and non-identifying.
6. Separate demonstration of the method from evaluation of effectiveness.

## Requirements

| Requirement ID | Requirement | Type | Acceptance criterion |
|---|---|---|---|
| R1 | Use only synthetic aggregate indicators. | constraint | No person-level data fields appear. |
| R2 | Produce ranked outreach stops. | functional | Output includes ordered stops with scores. |
| R3 | Explain score components. | transparency | Each score has visible contributing factors. |
| R4 | Permit human override. | governance | Override reason is recorded. |
| R5 | Support artificial demonstration. | evaluation | Synthetic scenario can be executed end-to-end. |
| R6 | State limits. | non-overclaiming | Output warns against real deployment without local validation. |

## Success criteria

The artifact is acceptable for this worked example if it can be demonstrated on synthetic data and reviewed against transparency, evaluation, and contribution checklists.
