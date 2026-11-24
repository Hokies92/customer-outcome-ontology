# COO project instructions for Claude Code and review

## Purpose and evidence boundaries

The Customer Outcome Ontology is a research-stage, customer-origin ontology for desired outcomes and their conditions, not a supplier product taxonomy or a universal theory of economic value. Preserve the historical 2006 source categories separately from new, explicitly attributed design hypotheses. The project's ISO standards usage is *informed by* standards, not a conformance claim.

- Customer reality is not the same as a supplier's customer MODEL.
- A business driver, objective, strategy, desired outcome, observed outcome, capability, contract, and transaction are distinct types.
- Supplier capability may *contribute to* an outcome under conditions; do not equate capabilities and outcomes.
- Claims need source, observer/author, date, evidence status, and identified uncertainty.
- Contradictions and alternative interpretations remain visible until resolved by appropriate evidence or explicit governance decision.
- Source-faithful architecture is MAP (supplier left) — MATCH (interface) — MODEL (customer right). The name/reasoning order remains Model–Map–Match.
- The original source blueprint images may be copyrighted. Do not publish those binaries to this public repository without an explicit rights/privacy review.

## Before editing

1. Read README.md, the relevant ontology definitions, docs/SHIP_GOVERNANCE.md, and the current PR diff.
2. State the exact claim, interface, behavior, or schema being changed, its evidence level, and the impact on old identifiers.
3. Favor small, reversible PRs. Do not silently add supposedly universal customer categories or assert ISO certification.
4. Where ontology classes/properties change, update the definition, mapping contract, fixtures, tests, and change log together.
5. Never turn a tentative analyst interpretation into a historical fact merely because it is stored in Notion or a document.

## Code review

Review for correctness, provenance, semantic type safety, backward compatibility, source integrity, and tests. Cite file and line or a reproducible counterexample. Report material risks as Important; don't substitute speculative stylistic preferences for defects. Use REVIEW.md for instructions specific to Anthropic Code Review.

## PR stewardship (fixing review/CI problems)

Work only on an authorized PR branch. Fix reproducible errors, review findings, and conflicts without altering the intended ontology semantics or creating evidence. After each fix, explain exactly what changed, tests rerun, remaining issues, and rollback. Do not dismiss unresolved semantic concerns as stylistic nits. Escalate changes to core classes, governance policies, historical attributions or conceptual boundaries to the human maintainers. The PR Steward role never approves, merges, bypasses checks, or modifies branch rules.

## Approval and merge authority

The author or AI agent cannot approve its own changes. Each PR needs at least one independent human approval; high-risk ontology/governance changes require two under .claude/approvals.yml. Applicable CODEOWNER approval and green required checks are additional gates, not substitutes. Review the latest diff after all fixes. No auto-merge and no bypass. Claude Approvals is configured to comment only, not approve, and starts in observe mode. Only authorized human maintainers may approve or merge in accordance with protected-branch rules.

## Interaction with Claude Ship

Anthropic's managed Code Review, PR Steward, and Claude Approvals require separate setup in a qualifying Claude organization with the Claude GitHub App. This repository's files define instructions and policies; they do not run cloud agents by themselves. Start PR Steward manually with @claude steward once the service is enabled. Stop it with @claude stop. Never claim services are active solely because these files exist.
