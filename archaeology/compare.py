#!/usr/bin/env python3
"""Source-faithful, temporal-safe archaeological MODEL comparator. Python stdlib only."""
import json
import sys
from pathlib import Path

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def validate_model(m):
    required = {"id", "kind", "view", "source", "modeled_object", "purpose", "boundary", "concepts", "recorded_at"}
    if not required.issubset(m): raise ValueError("Incomplete MODEL record")
    ids = [x["id"] for x in m["concepts"]]
    if len(ids) != len(set(ids)): raise ValueError("Duplicate concept identities")
    if not all(x.get("epistemic") for x in m["concepts"]): raise ValueError("Every concept needs epistemic status")
    source = m["source"]
    if m["kind"] == "historical_view":
        if source.get("original") is not None: raise ValueError("Invalid source shape")
        if m.get("original", {}).get("precision") == "copyright_year_only" and m["original"].get("exact_creation_date") is not None:
            raise ValueError("Copyright year is not a known creation date")
    return m

def compare(a, b, crosswalk):
    validate_model(a); validate_model(b)
    if crosswalk["from"] != a["id"] or crosswalk["to"] != b["id"]:
        raise ValueError("Crosswalk is for a different record pair")
    if a["kind"] == b["kind"] == "historical_view" and crosswalk["comparison_kind"] != "same_era_different_viewpoints":
        raise ValueError("2006 blueprint viewpoints are not established chronological MODEL releases")
    ids_a = {c["id"] for c in a["concepts"]}
    ids_b = {c["id"] for c in b["concepts"]}
    for row in crosswalk["mappings"]:
        if row["from"] not in ids_a or row["to"] is not None and row["to"] not in ids_b:
            raise ValueError("Crosswalk references unknown concept")
        if not row.get("why") or not row.get("relation"): raise ValueError("Unjustified mapping")
    return {
        "comparison_kind": crosswalk["comparison_kind"],
        "from": {"id":a["id"],"modeled_object":a["modeled_object"],"purpose":a["purpose"],"boundary":a["boundary"]},
        "to": {"id":b["id"],"modeled_object":b["modeled_object"],"purpose":b["purpose"],"boundary":b["boundary"]},
        "crosswalk_assertions": crosswalk["mappings"],
        "unmapped_source_ids": sorted(ids_a - {row["from"] for row in crosswalk["mappings"]}),
        "unmapped_target_ids": sorted(ids_b - {row["to"] for row in crosswalk["mappings"] if row["to"] is not None}),
        "warning": "Unmapped/absent does not mean removed from reality. Historical viewpoints are not chronological releases."
    }

def report(data):
    rows=[f"# MODEL comparison: {data['from']['id']} → {data['to']['id']}", "",
          f"**Kind:** {data['comparison_kind']}", "",
          "**Object of inquiry:** " + data["from"]["modeled_object"] + " → " + data["to"]["modeled_object"], "",
          "| Relationship | Source | Target | Rationale |","|---|---|---|---|"]
    for r in data["crosswalk_assertions"]:
        rows.append(f"| {r['relation']} | {r['from']} | {r['to'] or '—'} | {r['why']} |")
    rows += ["", "**Caution:** " + data["warning"], "", "**Unmapped source categories:** "+", ".join(data["unmapped_source_ids"]), "",
             "**Unmapped target categories:** "+", ".join(data["unmapped_target_ids"]), ""]
    return "\n".join(rows)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: compare.py BEFORE.json AFTER.json CROSSWALK.json")
        print(report(compare(*[load(Path(p)) for p in sys.argv[1:]])))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print("Invalid MODEL comparison:", exc, file=sys.stderr)
        sys.exit(2)
