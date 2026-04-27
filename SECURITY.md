# Security

This repository is primarily a documentation and research-artifact package, but security still matters for automation, metadata, examples, and publication workflows.

## Reporting

Report security concerns through the repository issue tracker or maintainer contact once the public repository is created. Until then, do not publish sensitive details in shared artifacts.

## Sensitive Information

Do not commit:

- API tokens, access keys, passwords, or private certificates;
- local secret-file paths beyond documented private operational notes;
- unpublished personally identifiable information;
- restricted source PDFs or copyrighted source text;
- private reviewer comments unless explicitly approved for release.

## Supported Versions

The package is currently a draft `0.1.0` working version. Security and maintenance support policies should be finalized before public release.

## Automation

Any validation workflow, release workflow, or archival workflow should use repository secrets rather than committed credentials. External publication actions, including DOI publication, require explicit confirmation at action time.
