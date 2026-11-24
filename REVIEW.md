# Code Review instructions — Customer Outcome Ontology

Review the current diff against the surrounding repository and CLAUDE.md. Prioritize **falsifiable correctness issues** and avoid stylistic noise. Report at most three Nits; do not duplicate findings automatically checked by CI.

## Important findings

Mark Important when a changed file:
- equates customer-desired outcomes with supplier capabilities, products, business drivers, strategic initiatives, offers, or observed outcomes;
- asserts a universal or source-observed ontology fact without appropriate historical or customer evidence;
- removes provenance, time, uncertainty, source identity, or an existing conflicting interpretation without explicit disposition;
- silently changes meaning of a stable class/property/identifier or breaks old instances, JSON Schema, RDF/OWL parsing, SHACL shapes, or mapping contracts;
- presents a simulated customer fixture as a real customer observation or a proposed relation as validated causation;
- breaks the independent customer/supplier boundary or mislocates MATCH as a final internal supplier processing station;
- weakens the independent-human or CODEOWNER approval requirement, enables AI self-approval/auto-merge, or allows unreviewed changes to main;
- publishes historical source images, private customer data, credentials, or other unapproved materials into this public repository;
- produces a mismatch between the actual implementation and tests or omits tests for changed behavior.

## Severity and evidence

Prove each material finding with a source location, concrete counterexample, or reproducible failure. Distinguish a genuine defect from an unresolved ontological decision. Note the smallest viable fix and the consequence if the finding remains.

Changes to ontology boundaries, definitions, transaction/commitment semantics, governance, or review policy deserve close review even when syntactically valid. Report a missing human decision as *needs review*, not as an automatically fixable formatting issue.

## What not to flag

- Trivial formatting or naming preferences unless they change formal semantics.
- CI-enforced YAML/JSON parsing and policy checks, unless CI itself is broken.
- Deliberately synthetic data clearly marked as such.
- A No Match or Insufficient Evidence outcome merely because a positive supplier match would be commercially convenient.
