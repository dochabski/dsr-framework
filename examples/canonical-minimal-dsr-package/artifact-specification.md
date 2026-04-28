# Artifact Specification

## Artifact name

Neighborhood Heat-Risk Cooling Route Advisor

## Artifact type

Primary type: method
Secondary types: lightweight prototype specification, prioritization model, documentation package

## Artifact boundary

The artifact consists of:

- a synthetic input table specification;
- a rule-based scoring method;
- a route-prioritization output format;
- explanation fields;
- human override logging;
- evaluation and transparency records.

The artifact does not include:

- live data ingestion;
- geospatial optimization;
- emergency dispatch;
- resident-level risk scoring;
- production deployment.

## Inputs

| Field | Description | Example |
|---|---|---|
| neighborhood_id | Synthetic neighborhood label. | N1 |
| heat_index_level | Synthetic ordinal heat exposure. | high |
| cooling_center_distance | Synthetic distance band. | near |
| outreach_capacity | Synthetic staff capacity estimate. | medium |
| vulnerability_indicator | Synthetic aggregate need indicator. | elevated |

## Output

A ranked outreach list with:

- rank;
- neighborhood ID;
- priority score;
- score explanation;
- recommended outreach action;
- override field;
- limitation note.

## Method logic

Priority score is a transparent weighted sum of heat exposure, aggregate vulnerability indicator, cooling-center access barrier, staff feasibility, and override rationale when used.

## Use context

The method is intended only for this synthetic DSR example. A real implementation would require local validation, stakeholder review, governance, and public-health expertise.

## Artifact quality criteria

| Criterion | Meaning |
|---|---|
| Transparency | Score components are visible. |
| Reviewability | Requirements, design choices, and evaluation criteria are traceable. |
| Data minimization | No personal data is required. |
| Adaptability | Weights and criteria can be modified with rationale. |
| Boundary clarity | Non-goals and non-deployment status are explicit. |
