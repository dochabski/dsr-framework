# Contributing

This repository is a draft research-artifact package. Contributions should improve traceability, coherence, usability, validation, or literature alignment without weakening the DSR distinctions preserved by the framework.

## Contribution Types

- Corrections to terminology, citations, metadata, or file placement.
- Improvements to schemas, templates, checklists, and validation logic.
- Literature-alignment notes that cite source IDs or bibliographic records.
- Documentation changes that make structured YAML/JSON content easier to use.
- Examples that are clearly separated from required package-control files.

## Review Expectations

Before proposing changes, check whether the affected file is controlled source material, a human-facing explanation, a template, a schema, or a retained record. Preserve stable IDs where possible.

Every substantive change should identify:

- the affected file or information item;
- the reason for the change;
- the related source basis, model, schema, checklist, or protocol rule;
- whether the change affects conformance, validation, or publication readiness.

## Content Rules

- Do not copy copyrighted source text into framework files beyond short, permitted excerpts.
- Do not add raw tokens, credentials, private notes, or local-only paths to public package files.
- Do not overclaim evaluation, publication readiness, reproducibility, generalization, or scholarly consensus.
- Mark unresolved evidence as `not_yet_mapped`, `not_checked`, or a similarly explicit status instead of inventing authority.

## Validation

Run YAML/JSON parsing and schema checks when changing controlled files. If a schema does not yet match a template or instance, record the gap rather than silently changing conformance claims.
