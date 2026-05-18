# Publication and dissemination strategy

The publication strategy should maximize visibility without creating multiple competing sources of truth. The recommended architecture is:

- Canonical living source: GitHub.
- Archival citation snapshot: Zenodo DOI release.
- Project/discovery hub: OSF project, optional OSF Preprint.
- Research-process publication: Octopus, optional after stable modularization.
- Data-only secondary deposits: Mendeley Data or Dryad only if releasing a genuine data package.
- Profile/dissemination mirrors: ResearchGate, Academia.edu, LinkedIn, Substack, ORCID, and personal website.
- Teaching/OER derivative: OER Commons or VIVA Open only after adapting the paper into learning materials.

This strategy follows a repository-artifact logic rather than a scatter-and-mirror logic. The living source, archived release, and dissemination links should have distinct roles.

## Recommended platform roles

| Platform | Recommended role | Use now? | Rationale |
|---|---|---:|---|
| GitHub | Canonical living source and source-of-truth repository. | Yes | Best fit for Markdown, metadata, version control, issue review, release records, schemas, validation scripts, and repo-native DSR logic. |
| Zenodo | DOI-bearing archival snapshot of GitHub release. | Yes | Best fit for citable release snapshot and long-term scholarly reference. |
| OSF | Project/discovery hub; optional preprint and linked materials. | Yes, after GitHub release and Zenodo DOI are available | Useful for open-science visibility, supplemental files, and discovery. Keep GitHub/Zenodo canonical. |
| Octopus | Modular research-process record. | Optional | Useful if you want to publish problem, method, results/synthesis, interpretation, and application as linked units. Do after the paper is stable. |
| SSRN | Discipline-facing preprint for IS/management/social-science audiences. | Optional | Consider if you want social-science and management discovery; do not make it canonical. |
| Mendeley Data | Data package only. | Optional later | Use only for source extraction corpus, concept inventory, or artifact data that can be openly licensed and safely shared. |
| Dryad | Curated data package only. | Usually no for this paper | Not the right primary home for a white paper; use only if releasing reusable research data under compatible terms. |
| ResearchGate | Profile dissemination link or licensed full-text mirror. | Optional | Good for visibility, not canonicality. Link to GitHub/Zenodo. |
| Academia.edu | Profile dissemination link or licensed full-text mirror. | Optional | Good for visibility, not canonicality. Link to GitHub/Zenodo. |
| OER Commons / VIVA Open | Teaching derivative or workbook. | Not yet | Use after making an instructional version, not for the primary white paper. |
| arXiv | Preprint only if a suitable category and format fit. | Probably no | DSR framework and methodology may fit better on OSF Preprints or SSRN unless there is a clear computing or information science framing. |
| bioRxiv and medRxiv | Not relevant. | No | The paper is not a life science or medical preprint. |
| HAL | Optional institutional/open archive mirror. | Optional | Consider only if you want a European open-archive mirror and can maintain metadata consistency. |

The main rule is simple: do not scatter the white paper as unrelated uploads. Create one canonical GitHub release, archive it through Zenodo, then point all other platforms to that release or deposit a clearly labeled derivative.
