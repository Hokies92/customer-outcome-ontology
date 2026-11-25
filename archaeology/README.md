# Archaeology of MODEL: evolving representations of the customer

The aim is to compare what different versions, viewpoints, and reconstructions of **MODEL the Customer** actually represent, so future models improve in explanatory power without rewriting the historical evidence.

### Three independent timelines
- **Historical source:** the ©2006 BluePrint Marketing source family's exact drawing dates are unknown. V1.1 is a *blueprint-family* version, not proof that MODEL had a formal V1.1 version.
- **Design viewpoint:** 2006 Current and Future are different representations in the same historical family, **not successive chronological software releases**.
- **Research/ontology version:** COO v0.1.0 is a **2026 analyst reconstruction**, not a model the historical author formally defined in 2006. Actual customer-instance timestamps are separate again.

### Compare seven dimensions
Object modeled; boundary; observer/purpose; level of abstraction; concepts; relationships; and source/evidence status. Absence from a bounded model is not deletion from reality.

Initial records are in `snapshots/`, with explicit, falsifiable crosswalks in `crosswalks/`. These are conservative, **not exhaustive transcriptions**. Run:

```bash
python archaeology/compare.py archaeology/snapshots/2006-current.json archaeology/snapshots/2006-future.json archaeology/crosswalks/current-to-future.json
python archaeology/compare.py archaeology/snapshots/2006-future.json archaeology/snapshots/2026-coo.json archaeology/crosswalks/future-to-coo.json
python -m unittest discover -s archaeology/tests -v
```

See `docs/MODEL_EVOLUTION_CHARTER.md` and `diagrams/lineage.mmd`. Exact original source image SHA hashes are retained; copyrighted blueprint bitmaps and private customer records are **not** published into this public repository. They remain in the separate research archive.

**A valid next MODEL version must specify which existing concept definitions survive, which meanings change, what was deliberately excluded or relocated, why the new boundary was chosen, and which competency questions it can now answer.** No power score is inferred from larger class counts.
