# Agent operating protocol — COO pull requests

This file applies to ChatGPT, Claude Code, and other assistants working through authorized repository access. It provides process guidance, not an unattended agent.

## Code reviewer
1. Inspect the actual PR diff, related definitions, tests, source attributions, and current rules.
2. Report findings ordered by severity with exact path/line, reproducible counterexample, evidence and minimal fix.
3. Separate syntactic failures from semantic/type failures and source-provenance disputes.
4. If no material findings are identified, say what was inspected and what remains untested; never claim proof of correctness.
5. Do not approve work that this agent authored or modified; independent human review remains required.

## PR steward
1. Inspect failing checks, review threads and merge state before editing.
2. Fix only problems within the PR's authorized scope, on its branch. Keep the fix small and reversible.
3. When scope or core ontology meaning needs to change, stop and escalate the choice; don't silently make a new ontology decision.
4. Re-run relevant tests and report results, remaining risk and rollback in the PR.
5. Never approve, merge, bypass branch protection, dismiss a human review or claim that a bot approval is independent human approval.

## Approval coordinator
Track and report on the latest commit: changed sensitive files, Code Review status, CI status, independent human approvals, CODEOWNER reviews, open blocking discussions, and unresolved conceptual decisions. State READY only if GitHub's enforced rules actually pass. The policy file in observe mode is **advisory**, not merge protection.

## Sources and integrity
Historical blueprint observations, later analytical hypotheses, customer instance evidence, and synthetic fixtures must stay distinguishable. Do not upload unapproved original 2006 artwork or private customer files to this public repository. The persistent work of monitoring PRs requires Claude Ship or other explicitly configured automation; this file alone does not schedule or run an assistant.
