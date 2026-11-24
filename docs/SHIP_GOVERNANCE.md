# Claude Ship adoption and human approval rules

**Status:** repository configuration draft. The files in this PR do not themselves turn on any Anthropic cloud agent or enforce GitHub merge rules.

## Three distinct roles

1. **Code Review** (Anthropic): read PR diffs and surrounding repository for correctness and risk. Repository-level guidance: REVIEW.md and CLAUDE.md. Reviews report findings but do not approve or block merges alone.
2. **PR Steward** (Anthropic beta): assist with failing checks, conflicts and comments; may commit fixes to the PR branch. It must never approve or merge. Start in **Manual** mode with a PR comment: @claude steward. Stop via @claude stop.
3. **Claude Approvals** (Anthropic beta): evaluate .claude/approvals.yml. It starts in **observe** mode and is configured here for **comments only**, not approving reviews.

The repo is public and no original historical blueprint PNGs have been imported here. Check copyright and privacy before adding images, real customer material or account data.

## Initial repository configuration for an Owner

1. In a qualifying Claude **Team or Enterprise** organization, open Organization Settings > Claude Ship. Install/link the **Claude GitHub App** for this specific repository. This is a separate connection from ChatGPT's GitHub integration.
2. Enable **Code Review** first. Start with Standard review level and Once after PR creation; choose a budget cap. Consider Every push after the workflow is stable.
3. Enable **PR Steward** in **Manual (@claude steward)** mode, with a spending limit. It can modify the branch after prompting and therefore all fixes must be re-reviewed.
4. Merge .claude/approvals.yml to main only after a human reviews the policy. Run Claude Approvals initially in **observe** mode. This is still billable if it invokes Code Review. Check the checks and policy interpretation on test PRs.
5. In GitHub branch protection/rulesets for **main**, require pull requests, the governance-policy CI check, at least one independent human approval, applicable CODEOWNER review, no bypass/force push, and dismissal of stale approvals (or approval after most recent push). Keep auto-merge off.
6. Invite an additional independent human reviewer with appropriate GitHub write/review access. With only Hokies92 listed as CODEOWNER, a PR authored by Hokies92 cannot receive an independent CODEOWNER approval from its own author; add another qualified CODEOWNER before requiring that combination in practice.
7. Before changing mode from observe to enforce, test a routine docs PR, a sensitive ontology-change PR, a steward fix after approval and a policy-file change. Explicitly approve a human-governed rollout.

**Important:** A GitHub required check for Claude Approvals (when enforced) is a separate GitHub setting. Observe mode alone does not prevent a merge. Even in enforce mode, the branch rules decide whether a merge is possible. The policy's seats never count the PR author; a simulated human account may still be indistinguishable from a natural person, so maintainers must audit actual identities.

## Approval policy

Default: one approval from an independent human reviewer. For ontology, schemas, source, scripts and governance rules: **two independent human approvals** and an applicable CODEOWNER review. Claude is set to comments only, never approving. The strictest matching rule applies. Reusing stale approvals is intentionally absent.

If the repository initially has no available independent human, the intended result is **blocked/awaiting reviewer**, not automatic exception or implicit approval. Never mark READY merely because an AI comment says the diff looks good.

## Change lifecycle

Proposed change -> short-lived feature branch -> draft PR with evidence and risk -> automated governance check -> Code Review -> PR Steward (if requested) -> refreshed CI and review after each push -> independent human and CODEOWNER approval -> authorized human merge.

Reviews, stewardship and approvals operate on the latest diff, and a fix may invalidate earlier conclusions. GitHub and Claude configuration can change without changing a file, so do not assume the repository policy itself guarantees enforcement.

## Ontology-specific review gates

- Historical source labels, dates and version are traceable. No invented source facts.
- Each concept retains identity, definition, boundaries, exclusions and evidence state.
- No conflation among BusinessDriver, BusinessObjective, DesiredOutcome, ObservedOutcome, SupplierCapability or Contract.
- Conditional capability-to-outcome associations are not equivalence or guarantees.
- Customer-specific claims are identified, dated and supported independently of synthetic fixtures.
- Schema changes include migration compatibility and negative/counterexample tests.
- Supplier MAP, MATCH interface, Customer MODEL remain distinct spatial domains.

## Required manual stewardship report

Every PR Steward change should report: (a) original failure, (b) files/lines changed, (c) tests run and outcomes, (d) unresolved findings, (e) semantic or provenance risks, (f) reversal instructions, and (g) whether a fresh human review is needed.

## Official references (consult for current details)

- https://code.claude.com/docs/en/claude-ship
- https://code.claude.com/docs/en/code-review-customize
- https://code.claude.com/docs/en/pr-steward
- https://code.claude.com/docs/en/approvals-policy
- https://code.claude.com/docs/en/approvals-github-rules

This is a faithful initial application of Claude Ship's file names and roles, with stricter project-specific human approval conditions. It is not a claim of active cloud agent setup, ISO conformance, or automated enforcement.
