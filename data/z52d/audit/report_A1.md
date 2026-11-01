# z52d audit — shard A1 (14 items; Opus blind redo, then comparison with Haiku Pass 1)

**Counts.** AGREE 5 (Z1478, Z0213, Z2232, Z1867, Z1012) · MISS-MINOR 8 (Z0656, Z2290, Z0665, Z1854, Z2194, Z1575,
Z0845, Z1285) · MISS-MAJOR 0 · HAIKU-WRONG-COVERED 1 (Z2134) · HAIKU-BETTER 0. Blind outcomes (Opus): covered 5, nothing 8,
skipped 1. Haiku: nothing 6, covered 4, skipped 4. Content scores (Opus): 0 ×5, 1 ×8, 2 ×1 (Z0665); none ≥ 3.

**MISS-MAJOR items:** none. Nothing in this shard was a lost lead for ES. The largest gaps:
- Z0665: Haiku's "covered" was right. My stratification of the residue model by the Legendre vector at 11..31
  removes about 2/3 of the log-correlation between certificate families (ratio 9.5·10⁵ → 148 at X = 1000; EVIDENCE). This only
  replicates EXSET_SHIFT_DIVISORS §6 (U line: about 2/3 of the e^{5.6} excess removed by a 9-prime quadratic profile).
- Z1575: closure hypotheses refuted. E(★) ∩ odd ≤ 10⁶ = 499 squares + 481 non-squares, so it is not "squares + sporadic"
  for composites, and n → n·m² preserves exceptions only 12/2336 times (CERTIFIED counts).
- Z0845: the compounding test that Haiku said it "did not run" gives hard×hard semiprimes ≈ residue-matched controls (0.23 vs 0.25).

**HAIKU-WRONG-COVERED:** Z2134 cites BRAINSTORM/z52b_signature.md, which holds only the generated idea items (the item's own
siblings), not an analysis. The step itself is empty: the 2→2 rewriter applies to 2 of 1559 solutions for p < 300.

**Patterns in Haiku's failures (Assessment).**
1. *Citing the item's own origin as coverage.* Z2134 (z52b_signature), Z1854 (z52b_free_opus #266) and partly Z0665
   cite the generating brainstorm list or the item's own sanity check. A lint rule "covered must not cite
   BRAINSTORM/z52b_* item lists" would catch these.
2. *Step not done, outcome recorded anyway.* In Z2194 the page was not retrieved (an inconclusive "nothing"). In Z0845 the
   compounding test was explicitly not run, and in Z1854 the proposed next step was ignored. In Z1285/Z1012 a cheap concrete
   computation was skipped as a "restatement". The outcomes happened to be right because the items were weak.
3. *Shallow literature checks.* In Z0656 one almost-all paper stood in for the scale calibration (proved power width, GRH
   X^{−1/2} floor, ES needs 1/p).
4. Where Haiku did compute (Z1478, Z1575 literal question, Z2232), its numbers are consistent with mine. In Z2232 it found
   the repo's isosceles law, which I re-proved without noticing it was banked (a small point in Haiku's favour).

**Bottom line for this shard (Assessment).** Haiku under-records depth (8/14 MISS-MINOR) but did not lose anything
that matters for an ES proof here. Its "nothing/skipped" verdicts on weak items are reliable as verdicts, not as
records of work done.

Caveat: my blind pass for Z1478 was contaminated, because a key-term grep showed Haiku's ES_CONNECTIONS_TODO line before I computed.
Files: `opus_A1.jsonl`, `compare_A1.jsonl`, `A1/*.txt`, `scripts/z52d_audit_A1_*`.
