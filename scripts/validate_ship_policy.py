#!/usr/bin/env python3
"""Fail closed on unsafe changes to the COO Claude Ship approval configuration.

This validates the policy's documented safety invariants, NOT Anthropic's full
policy schema or actual GitHub branch-protection settings. The latter require
separate human administrator setup and verification.
"""
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / ".claude" / "approvals.yml"
PROTECTED = {
    "ontology/**", "schemas/**", "reference/**", "source/**",
    "scripts/**", ".claude/**", ".github/**", "CLAUDE.md", "REVIEW.md",
}
REQUIRED = {
    "CLAUDE.md", "REVIEW.md", "AGENTS.md", ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md", "docs/SHIP_GOVERNANCE.md",
    ".github/workflows/governance.yml",
}


def check(test, message):
    if not test:
        raise ValueError(message)


def independent_human_seats(rule):
    verdict = rule.get("verdict") or {}
    check(verdict.get("claude") == "comments",
          "Claude must comment only; it must not approve or block independently")
    check(not rule.get("override"), "Risk-lowering overrides are forbidden")
    check(not rule.get("reuse"), "Reusing stale approvals is forbidden")
    seats = verdict.get("seats")
    check(isinstance(seats, list) and seats,
          "Approval seats must explicitly exclude PR authors")
    counts = []
    for seat in seats:
        check(isinstance(seat, dict), "Approval seat must be a mapping")
        people = seat.get("from")
        check(isinstance(people, list) and "humans" in people
              and "!pr/authors" in people,
              "Each approval seat must require non-author humans")
        number = seat.get("count")
        check(type(number) is int and number >= 1,
              "Each approval group must have at least one reviewer")
        counts.append(number)
    return max(counts)


def validate():
    raw = POLICY.read_text(encoding="utf-8")
    policy = yaml.safe_load(raw)
    check(isinstance(policy, dict), "Policy must be a YAML object")
    check(policy.get("version") == 1, "Claude Approvals version must be 1")
    check(policy.get("mode") in {"observe", "enforce"}, "Invalid mode")
    rules = policy.get("rules")
    check(isinstance(rules, list) and rules, "Rules cannot be empty")
    found_default = False
    protected = set()
    for rule in rules:
        check(isinstance(rule, dict), "Every rule must be an object")
        check(bool(rule.get("purpose")), "Each rule needs a purpose")
        paths = rule.get("paths")
        check(isinstance(paths, list) and paths, "Rule needs path patterns")
        reviewer_count = independent_human_seats(rule)
        advisory = rule.get("advisory") or []
        check("claude/code_review" in advisory,
              "Keep Anthropic Code Review for every approval rule")
        if "**" in paths:
            found_default = reviewer_count >= 1
        if reviewer_count >= 2:
            protected.update(paths)
    check(found_default, "Every path requires at least one independent human")
    check(PROTECTED.issubset(protected),
          "Sensitive code, ontology and governance paths must require two humans")
    for relative in REQUIRED:
        check((ROOT / relative).is_file(), "Missing governance file: " + relative)
    owners = (ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
    check("@Hokies92" in owners, "Initial code owner must be specified")
    print("COO Ship policy check passed. Mode:", policy["mode"])
    print("Note: Branch protection, Code Owners, and Claude services are not validated.")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError, yaml.YAMLError) as exc:
        print("COO Ship policy check failed:", exc, file=sys.stderr)
        sys.exit(1)
