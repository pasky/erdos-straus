# AGENT REPORT O150 — brainstorm: combinatorial / graph / game / dynamical structure of the ES solution set; covering duals

Branch `side-agent/bs-graph-covering`. Memos are in BRAINSTORM/ and scripts in `scripts/bs_graph_*.py`. Nothing here
is LIVE, and ES is not solved.

**(a) `BRAINSTORM/graph_cayley_moves.md` — COLLAPSES (to B1/B2), with one PROVED by-product.**
* Setup: ES solutions are the level-4 positive integral points `(−n,4x,4y,4z)` on Cayley's cubic σ₃ = 0. This is
  folklore (ET Rem. 2.10, BL §2.1). For prime p, all of ES(p) is the level-4 condition (Lemma A.0).
* The natural move classes are:
  * (M1) scaling/Hecke: multiplicative, so it never reaches primes;
  * (M2) ET parameter translations: affine in n, so the orbits are congruence classes (B1);
  * (M3) Bir(𝒞) ≅ Cremona: transitive, so it has no content;
  * (M4) chord–tangent (Manin) moves.
* **Theorem A.1 (PROVED, real-geometric; arc-parity argument plus an exhaustive 16-case table,
  `bs_graph_arcs.py`).** No real line meets the type-(1,3) ("positive") real locus of the Cayley cubic in three
  distinct points.
* So a chord through two positive solutions *never* yields a positive solution, only signed (2,2) points or
  boundary points (Cor A.2). Check: 0 positives among 65 703 integer chords of the ES points with n ≤ 30; the
  tangent case is EVIDENCE only.
* Every positive point for p is the chord of a fixed positive seed with a signed point (Cor A.3), which is the
  divisor lottery restated (B2).
* Strongest reason for the collapse: the only non-multiplicative move that produces positive points must pass
  through signed points, and landing on N = p is a divisor event.
* Novelty of A.1: unverified, probably minor (elementary).

**(b) `BRAINSTORM/greedy_algorithm_dynamics.md` — COLLAPSES (fixed algorithms to B1; growing families exactly to
the window frame).**
* Prop B.1 (PROVED): greedy, Engel and Golomb/Farey all need ≥ 4 terms for *every* p ≡ 1 (24). Confirmed on
  3 202 primes < 3·10⁵.
* Prop B.2 (PROVED dictionary, via notes Lemma 77.1): the natural growing-parameter family, offset greedy G_J, has
  `J(p) = (a_min(p) − 3)/4`.
* So the brief's target "failure set provably not a whole residue class" is already POINTWISE_SIZE Lemma 11.3.
  Fixed J fails i.o. under Dickson (Prop 8.4), the densities are XWIN's, and the sufficient statement is X_win.
  Data: max J = 14 at p = 118801 below 3·10⁵.
* Strongest reason: the parameter of the natural algorithm family *is* a_min.

**(c) `BRAINSTORM/covering_distortion_dual.md` — COLLAPSES (to B1/B6); one UNCLEAR Haar-side program.**
* Non-coverability of the primes by ET identity classes is classical and unconditional: odd-square classes, ET
  Prop 1.6.
* The H in Theorem C concerns factorisation-shape steps. Removing it is the parity-blocked multi-slice sieve
  problem (WINDOW2 Thm P1), which covering methods (Haar statements, parity-blind) cannot touch.
* The dual covering complexity is already exactly quantified by the campaign:
  * δ*(T), with Haar exponent 3;
  * W(p) Ω-results;
  * the POINTWISE_TAIL proportion, which is the Hough-type "a modulus ≥ exp(c(log x)^{1/4−o(1)}) is needed to cover
    the primes ≤ x".
* A dictionary table is given. BBMST Thm 3.1 is *inapplicable* to the raw ES system, since the Mordell classes make
  η ≥ 1.
* UNCLEAR program: distortion inside the quarantined fibre might remove OMEGA13's `(log𝓛)^5`, giving
  `log 1/δ* ≍ 𝓛³`. That is Haar-side only and has no ES value.
* The game/determinacy view (Gale–Stewart) is exactly TYPEI2 Thm A compactness.
* Strongest reason: covering technology lower-bounds uncovered Haar mass, and B1 already says that mass exists.

Suggested follow-up, low priority:
* write out the tangent/multiplicity case of Theorem A.1 (the double-root split);
* do a quick literature check on whether the "no three positive collinear points on Σ1/Xᵢ = 0" fact is known (it
  should be classical in real-cubic-surface or Egyptian-fraction folklore).
