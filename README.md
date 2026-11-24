# Customer Outcome Ontology (COO)

Research-stage ontology of customer-desired outcomes and their context, inspired by the 2006 Customer-Centered Conversation Solution Blueprint.

**Status:** research draft; not a ratified or ISO-certified ontology. The full v0.1.0 ontology archive has not yet been imported into this GitHub repository. Original historical blueprint images have deliberately NOT been published into this public repository.

## Project governance

This repository uses the [Claude Ship](https://code.claude.com/docs/en/claude-ship) conventions for Code Review, PR Steward, and Claude Approvals, combined with mandatory independent human review:

- [CLAUDE.md](CLAUDE.md): project instructions for Claude Code and review.
- [REVIEW.md](REVIEW.md): Claude Code Review criteria.
- [.claude/approvals.yml](.claude/approvals.yml): human-only approval policy, initially **observe mode**.
- [AGENTS.md](AGENTS.md): review and PR-stewardship rules for any assistant.
- [docs/SHIP_GOVERNANCE.md](docs/SHIP_GOVERNANCE.md): setup, risk controls, and operating instructions.
- [.github/workflows/governance.yml](.github/workflows/governance.yml): automated policy validation.

**Creating these files does not enable Anthropic's managed services or protect the main branch.** Those are separate admin actions. No AI reviewer may approve its own changes or merge them under this policy.

Customer world MODEL and supplier MAP remain separate; MATCH is their interaction interface. For source-faithful system diagrams use MAP (supplier, left) — MATCH (center) — MODEL (customer, right), not a three-stage horizontal supplier workflow.

## Contributing

Make changes on a branch, open a PR, provide source provenance and tests, obtain an independent human review and any applicable CODEOWNER review, and merge only under GitHub's protected-branch checks. See the PR template and governance guide.
