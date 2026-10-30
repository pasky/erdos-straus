## Summary

- **What this is:** the single master TODO of *candidate connections* produced by wave z52b (10 breadth-first lanes,
  `data/z52b/<lane>.jsonl`). Nothing was dropped for being weak, already-screened, barrier-blocked or `seen:` in the
  repo. The only removals are **true duplicates**, which were fused. A fused item keeps every source id, the union of
  tags and refs, and the other lanes' first steps (`alt_first_steps` in `data/z52b/master.jsonl`).
- **Input hygiene:** all 3590 lines were valid JSON with the 9 mandatory fields, so nothing needed fixing. Lane-specific
  extra fields (`analogues.world`, `signature.raw_id`, `upgrades.upgrade`) are kept in `lane_extra`. 104 rows have
  first step "None…". These are mostly dividing-lane catalog/calibration rows. They are kept and flagged
  `reference-only`.
- **Dedupe pipeline** (fully reproducible from `data/z52b/merge/`):
  1. Candidate pairs: TF-IDF cosine on title+connection (≥ 0.30 cross-lane), bge-small-en-v1.5 embedding cosine
     (≥ 0.85 cross-lane; ≥ 0.90 same-lane), or a shared arXiv/OEIS ref with embedding ≥ 0.78. Distinct
     "Problem N" numbers of the Erdős-problems items were excluded. This gave 1212 pairs (`candidates.tsv`).
  2. Every pair was judged DUP or DISTINCT using the rule "same external object linked to the same ES-side object in
     the same way; when in doubt, DISTINCT". Result: 601 DUP and 611 DISTINCT (`dup_decisions.tsv`).
  3. The DUP pairs were joined into clusters by union-find. Transitive chains were then checked by hand. Every cluster
     with ≥ 4 members was read, and so were 64 random merged items. A second independent pass audited all 245 merged
     clusters. Wrong fusions were split, and those splits are recorded in `cluster_overrides.tsv`. Examples: Lenstra's
     bound vs Coppersmith's small roots; Croot vs Bloom; HKRS vs Rickards–Stange; Duke–Schulze-Pillot vs spinor ↔ T1;
     BGS expansion vs Chen's divisibility; primes vs composites near squares.
  4. Residual-duplicate check: a sample just below the thresholds (embedding cosine 0.83–0.85) had about 1 duplicate
     in 20. So the list may still hold a few dozen unmerged near-duplicates. That is the intended bias, since breadth
     beats over-merging.
- **Representative wording and first step:** the title and connection shown come from the clearest member. The
  heuristic prefers higher confidence, readable text over template rows and some refs; one manual choice is recorded in
  `rep_overrides.tsv`. The shown first step is picked separately as the most concrete one among the members.
- **Areas and flags** come from regexes over the tags and wording. They are approximate and meant for navigation
  only. The `computational`, `literature-check` and `proof-attempt` flags read the wording of the first step.
  `multi-lane` is exact.
