# z52d audit — shard A2 (13 items; Opus blind redo, then comparison with Haiku Pass 1)

ES is OPEN; nothing here bears on that. Files: `opus_A2.jsonl` (blind, committed before opening Haiku), `compare_A2.jsonl`,
scripts `scripts/z52d_audit_A2_*`, data `data/z52d/audit/A2/`.

**Verdict counts:** AGREE 5 · MISS-MINOR 6 · MISS-MAJOR 1 · HAIKU-WRONG-COVERED 1 · HAIKU-BETTER 0.
Opus outcomes: covered 7, nothing 5 (Z0975 has content 2), interesting 1 (Z3155). Content scores: 0×1, 1×10, 2×2, 3×0.

**MISS-MAJOR / WRONG-COVERED items**
- Z0975 (MISS-MAJOR): Haiku did not split by p mod 4 and stopped at p ≤ 1500, so its numbers ("51% have y−x ≤ 2") describe only the
  p≡3(4) isosceles case and point the wrong way. At p≡1(4) ≤ 2·10⁵: min(y−x) ≍ p^{0.75}, never ≤ log²p beyond 5·10⁴, and
  min(z−y) ≥ p. This refutes the lead (EVIDENCE). There is also an exact lemma: gap-g Type I solutions ⟺ (2mg)² + (pm+1)² = □.
- Z3155 (WRONG-COVERED, with real content lost): Haiku cited a Sun 1-3-5 quaternion memo, not the ES refinement mining, and did not run
  the search. I ran 16 new predicates on all primes ≤ 10⁶; their survivors are positive-share sub-lotteries. The run also gave a
  universal fact, PROVED relative to N. X. Tho (Ann. Math. Inform. 54, 2021): no ES solution of 4/n has n | x+y+z, because
  (x+y+z)(1/x+1/y+1/z) = 4s/n is never an integer ≡ 0 (mod 4) for positive integers. This is new to the repo; it is a small
  lane at most.

**Pattern in Haiku's misses**
1. *Skipping as "vague/generic/restatement"* (Z0600, Z1303, Z1993, Z1100): each item had an obvious cheap concrete step. In this shard
   these skips lost only routine content: they re-derived known repo results ((I)7 genus condition, the additive-character expansion,
   the (★) form). The process failure is real, but the loss is small.
2. *Truncated computations* (Z0975, and Z0698 on 372 primes): the one major loss came from scope cuts. Haiku used a small range and did
   not condition on the residue class the item named, so the numbers answered a different question.
3. *"Covered" via sibling pass-1 entries rather than depth files* (Z1767 fair; Z3155 wrong): Haiku tends to cite a nearby z52b
   pass-1 record without checking that it does the item's step.
4. Where Haiku did the step (Z0698, Z2152, Z2117, Z2572), its record matched mine. On Z0698 it got the same −0.22 partial correlation.

**Calibration (Assessment):** in this shard the false-negative rate is about 2/13 for losses of some substance, and 0/13 for losses
that could matter for an ES proof. "Skipped" verdicts were reliable about value but not about actionability.
