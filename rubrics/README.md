<!--
SPDX-License-Identifier: CC0-1.0
item_id: rubrics_readme
item_type: documentation
status: 1.3.0_stable
version: 1.3.0
-->

# DSR Assessment Rubrics

This directory contains DSR assessment rubrics for review, source-grounding, and framework-use assessment.

The individual `*_rubric.yaml` files are the canonical editable rubric records. The generated file
`dsr_assessment_rubrics_unified.yaml` preserves each rubric as a distinct collection item for review, search, AI ingestion,
and distribution convenience.

Regenerate the unified collection with:

```bash
python scripts/build-rubric-collection.py
```

The unified collection reports dependency references that are not present in this directory as warnings. Missing referenced
rubrics should be added only from real source files or retained decisions, not fabricated during collection generation.

These rubrics support DSR reviewability and reuse-readiness. They do not replace reviewer judgment, convert guidance into
hard validation rules by themselves, certify downstream artifacts, or claim L5 archival/publication-ready status.
