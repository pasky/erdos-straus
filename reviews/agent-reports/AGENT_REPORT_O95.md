# AGENT_REPORT_O95 — x* (r=13) as a Diophantine problem: checkpoint 1

Branch `side-agent/r13-diophantine`. File: POINTWISE_MORDELL13B.md. Not reviewed.
Stopped at the context checkpoint (brief: report before 25%); goal (1) partly done, goals (2), (3) not started.

Done:
* **Lemma 1.1 (PROVED, checked):** explicit conditions for `x(u)` (u at 11 and 13, 1 elsewhere) to lie in
  a class of each of the seven families. At x* = x(2) every box condition is a single congruence mod
  `F = M_T` with RHS −1/−2: e.g. II2 `f_T | 2a²d+1`, I3 `f_T | c²d+1`, I2 `c ≡ −2a (f_T)`.
  `scripts/m13b_table_check.py`: 14000 random (family, P, u, w) samples against literal class membership,
  0 mismatches, 3605 hits.
* **Lemma 1.2 (PROVED):** reciprocity parities at x*: T-level odd for II1, I4, II2, I2;
  `v_T(d)` odd for I1, I3; `v_T(d)+v_T(e)` odd for II3. No family is killed (no uniform quadratic obstruction).
* **Lemma 2.1 (PROVED):** II3 data at `x(u)`, for every placement of 11 and 13 (pure P, pure Q, mixed),
  are ES solutions of `4/N` with `N = e_T·a_T²·d_T`. This unifies MORDELL17 Lemmas 2.1 and 2.3 and
  covers the mixed P/Q case.

Next steps (proposed):
1. Same correspondence for I1, I2 (mixed U/Q⁻¹), I3 (mixed P/√Q), II1/I4, II2.
2. `m13b_enum`: complete enumeration (any height) of all data with ES level `N | 11^i13^j` for small (i,j),
   testing Lemma 1.1 at u=2, and an independent cross-check against `mordell_point.py` (M ≤ 10⁶) on overlaps.
3. Look for a uniform kill. Reciprocity alone fails (Lemma 1.2). Candidates: a 2-adic or quartic-symbol
   argument using the fact that u=2 is an integer, or a descent on the ES level.
Honest expectation: as for r=17 (MORDELL17 §6), proving sterility probably needs a tail bound that
nobody has. A per-level complete search plus a precise blocking statement is the realistic outcome.
