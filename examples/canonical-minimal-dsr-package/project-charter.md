<!--
SPDX-License-Identifier: CC0-1.0
item_id: example_heat_route_project_charter
item_type: example_record
status: v1_release_candidate
version: 1.0.0-rc.1
-->

# Project Charter: Neighborhood Heat-Risk Cooling Route Advisor

## Project identity

- Project name: Neighborhood Heat-Risk Cooling Route Advisor
- Project class: synthetic DSR worked example
- Artifact class: decision-support method plus lightweight prototype specification
- Primary artifact type: method
- Secondary artifact types: model, interface specification, evaluation plan
- Package role: canonical minimal example for the DSR Framework

## Problem context

Community health workers may need to prioritize outreach to residents during heat-risk events. Outreach planning can be constrained by limited staff time, incomplete local knowledge, distance between cooling centers, and uncertainty about which neighborhoods need support first.

This example uses only synthetic data and does not represent a real community, agency, or resident population.

## Stakeholders

| Stakeholder | Interest | Involvement |
|---|---|---|
| Community health worker | Needs practical route-prioritization support. | Walkthrough participant in artificial evaluation. |
| Public-health coordinator | Needs accountable decision logic. | Reviewer of objectives and constraints. |
| Resident advocate | Needs fairness and accessibility safeguards. | Reviewer of risk and limitation statements. |
| Data steward | Needs data minimization and provenance controls. | Reviewer of input assumptions. |

## Scope

Included:

- synthetic neighborhood risk table;
- rule-based prioritization method;
- route-prioritization output specification;
- explanation fields for each priority score;
- evaluation plan using artificial demonstration and expert walkthrough.

Excluded:

- real resident data;
- emergency dispatch;
- clinical triage;
- automated decision-making without human review;
- deployment in a real public-health agency.

## DSR framing

The example distinguishes local artifact utility, artifact quality, knowledge contribution, demonstration, evaluation, and projectability limits.

## Success criteria

The example succeeds if a reviewer can trace:

1. problem/objective statements to artifact requirements;
2. artifact requirements to design features;
3. evaluation criteria to artifact and contribution claims;
4. transparency evidence to framework dimensions;
5. limitations to non-overclaiming statements.
