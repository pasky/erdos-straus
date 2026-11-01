# z52d audit2 — shard B1 (16 Haiku Pass-2 records, blind Opus redo)
ES is OPEN; nothing here bears on a proof. Files: `opus_B1.jsonl` (blind, committed first), `compare_B1.jsonl`, `scripts/z52d_audit2_B1_*`, `B1/`.

**Verdicts:** AGREE 8 · MISS-MINOR 8 · MISS-MAJOR 0 · HAIKU-WRONG-COVERED 0 · HAIKU-BETTER 0.
Opus outcomes: covered 8, nothing 8 (content: 0 ×1, 1 ×15; no item scored ≥ 2). Haiku: covered 1, skipped 1,
needs-compute 1, nothing 13.

**MISS-MAJOR items:** none — no item yielded a lead or substantive result that Haiku dropped. **MISS-MINOR:**
- Z1867 — skipped as organisational; the CSV export was trivial and FRONTIER §3/§4/§6 already is the table.
- Z2814 — needs-compute (~1 h est.), but the lattice step takes minutes: 9 nef conic classes = GEOMETRY_ES F1–F3.
- Z0321 — step not run, and the repo answer (local densities n-flat; ×14 class variation mod 840) was not found.
- Z2534 — only untwisted reciprocity checked; twisted Berndt-type sums are a clean structural negative.
- Z3090 — "κ undefined" although the item lists candidates; the κ correlations collapse within the Mordell-hard classes.
- Z2134 — only the abstract was read; the operator is a special pivot and applies to no prime solution pair (p < 3000).
- Z0369 — comparison not applied; the answer is EXSET_BEYOND_CRT §4.3 D7.
- Z2312 — "family list missing"; HARDNESS_MAP l.230 proves that finite families share a failure class.

**Pattern in Haiku's Pass-2 records**
1. Where Haiku computes, its numbers agree with mine (Z0773 ESC floor 0.10–0.11; Z2430 Q vs ⟨res⟩ rates; Z1196
   DP/enumeration). It is sometimes slightly richer (Z0773 exponent fit, Z2430 per-k table, Z1196 XP-vs-FPT remark).
2. The dominant failure is **under-recorded coverage**: 4 items (Z0321, Z0369, Z2312, Z2107) are answered by an existing
   repo section that Haiku did not find, so it recorded "nothing" or "step not run" instead of "covered".
3. Steps that are cheap but look unfamiliar get deferred or narrowed. A small lattice enumeration was estimated at 1 h
   (Z2814). A paper was read only to the abstract (Z2134). Loosely specified items are declared undefined although the
   item names concrete candidates (Z3090, Z2312), or are skipped as organisational (Z1867).
4. The hardened brief worked on the core requirement: every record states what was not done (`not_done`), and no
   `covered` claim was wrong.
Assessment: on this shard the Pass-2 records lose no ES-relevant content. Their weakness is calibration and
bookkeeping (missed "covered", unfinished cheap steps), not missed leads.
