<!-- SPDX-License-Identifier: CC0-1.0 -->

# Minimal L1/L2 DSR Documentation Example

This example shows a single-file L2 reviewable record for a hypothetical DSR documentation helper artifact. It demonstrates the minimal pathway without requiring the full L4 package structure.

## Files

- `minimal-documentation.yaml`: combined L2 reviewable record.

## Validate

From the repository root:

```bash
python scripts/validate-minimal-l1-l2.py examples/minimal-l1-l2-package --level l2
```

## Conformance claim

This example claims only `l2_reviewable` for demonstration purposes. It does not claim L4 reusable-stable or L5 archival/publication-ready status.
