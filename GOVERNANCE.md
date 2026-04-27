# Governance

The DSR Framework is governed as a maintained research-artifact package. Until a public repository and named maintainers are finalized, governance decisions are draft and should be recorded through retained records.

## Roles

- `framework_maintainer`: owns package structure, release decisions, and conformance declarations.
- `dsr_methodology_reviewer`: reviews DSR terminology, literature alignment, contribution claims, and evaluation logic.
- `repository_quality_reviewer`: reviews repository completeness, metadata, schema alignment, and publication readiness.

## Decision Policy

Structural changes to schemas, controlled vocabularies, package metadata, conformance levels, or publication records should be made through explicit records or changelog entries. Minor editorial changes may be made directly when they do not alter controlled meaning.

## Release Policy

No release should be marked publication-ready until:

- required root files are complete;
- package inventory and manifest reflect actual paths;
- schema/template contracts are reconciled or exceptions are documented;
- source-basis records are reviewed;
- citation and archival metadata are checked;
- release and preservation records are created.

## Conflict Resolution

When framework files disagree, prefer this order:

1. User-approved release decisions and retained records.
2. Documentation-protocol package rules.
3. DSR source-basis records and extraction evidence.
4. Controlled YAML/JSON specifications, models, schemas, and vocabularies.
5. Human-facing Markdown guides.
