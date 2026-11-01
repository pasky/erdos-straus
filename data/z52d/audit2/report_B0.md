# z52d audit2 — shard B0 (16 Haiku Pass-2 records vs blind Opus redo)

ES remains OPEN. Files: `opus_B0.jsonl` (blind, committed before opening Haiku's), `compare_B0.jsonl`, `scripts/z52d_audit2_B0_*`.

**Verdict counts (16):** AGREE 7 · MISS-MINOR 7 · MISS-MAJOR 1 · HAIKU-BETTER 1 · HAIKU-WRONG-COVERED 0.
Outcomes: Haiku 16/16 `nothing`. Opus: 9 `covered`, 7 `nothing`, 0 `interesting`; content scores are 2 for Z2112 and 1 for the other 15.
No item in this shard is an ES lead under either reading.

**MISS-MAJOR** — Z2112 (semi-integral Markoff, Mitankin–Uhlemann): Haiku read only the abstract. The ES pair has the same boundary triangle as
  Markoff, so MU Thm 2.15 applies verbatim. Strict Darmon-2 points are solutions of ES_{nq²} with the q-part in one coordinate:
  abundant for n ≥ 2, while at n = 1 they are exactly the Type I solutions of odd squares (empty by T1) and Campana points exist. Calibration
  value only.

**HAIKU-BETTER** — Z2764 (Smith theory): Haiku's fixed-p word complex is F₂-acyclic with trivial forced fixed points, a sharper reason than my
  off-target all-n' complex. Haiku did miss the covering memo (invol_topological Lemma T).

**Patterns in Haiku's failures**
1. *Coverage blindness.* In 7 items that the repo covers (Z2210, Z2929, Z1849, Z2036, Z3053, Z2485, Z2764), Haiku's record cites no covering memo.
   Its outcome (`nothing`) is right, but the record loses the structural reason, e.g. "no Vieta involution because the equation is
   linear in each variable", "Kuznetsov never enters at fixed p", "invariant = BL class χ_{−t}(d)".
2. *Half-done cheap steps, now honestly flagged.* After the hardened brief and the lint round, `not_done` is filled truthfully
   (Z2112, Z2858, Z1849, Z2036, Z2726), but cheap completions are still skipped: formulating the relaxation, plugging in a constant,
   one more conjugation.
3. *When Haiku computes, it is sound* (Z1116, Z2485 caught its own artefact, Z2764). It never over-claims, and no `covered` was wrong.
4. Net: Pass-2 Haiku `nothing` verdicts are reliable as *decisions* in this shard (1 real miss out of 16). They are weak as
   *records* in about half the items.

Contamination note: while grepping the repo for "mitsui" during Z0508 I saw one line of a Pass-1 outcome script
(`scripts/z52b_p1_U09_outcomes_fix.py`; Pass-1, not the Pass-2 records under audit). After that I excluded those paths. It did not
affect the Pass-2 comparison.
