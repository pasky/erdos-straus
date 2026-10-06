# AGENT_REPORT_O53 — weak SPW (branch side-agent/weak-spw), checkpoint 1

Deliverable: `EXCEPTIONAL_SPW2.md`; scripts `scripts/spw2_*.py`; data `data/spw2/`.

## Headline
**Weak SPW is still open.** I have neither a construction nor a refutation. What changed:
the requirement of the Prop 9.1 / Thm 5.2 route is now explicit (a sufficient condition;
necessity not claimed), the problem is reduced to a cleaner relaxation (RSPW), and the known
obstruction is extended to that relaxation. Assessment only (small-N LPs can mislead, SPW1 §2):
the finite-support lower bounds for N ≤ 80 show no N^{−1/2} decay. An apparent N^{−1/2} barrier came
up along the way; I checked it and withdrew it (Assessment 4.2).

## Proved (internal; review R53: no FATAL, M1 + m1–m13 applied)
* **Lemma 1.1 (requirement of the Prop 9.1 / Thm 5.2 route; sufficient, not necessary).** Via SPW1 Lemma 1.4 + IF2 Prop 9.1 + IF2 Thm 5.2, the
  hybrid saving is ≤ C′(log N)^{3/4} + log(K_N/η_N) + log(1 + Δ′_N/K_N) + O(1), where
  η_N is the full-class margin and K_N the sparse-class cap (needs η/K ≥ 4N^{−A₁}; Thm 5.2 used without its t, 1/Δ ≥ e^{−S_A} hypotheses, justified
  in a remark; the log log-free exponent is conditional on the KARY3 §4.3 pointer). So:
  - log(K/η) = O((log N)^{3/4}) gives the 3/4 cap;
  - log(K/η) ≤ (log N)^θ gives a θ-cap;
  - with σ = N^{−c} **this route** gives only B ≥ N^{1−c−o(1)} (no (log N)^θ cap). A
    different minorant construction might lose less; necessity is not proved.
* **Lemma 2.2 (near zone is invisible).** Classes of modulus > CN through [1,N] avoid
  Z = [N−CN, 0] ∪ [N+1, CN+1]. Consequence: at C = 2, once sparse classes may carry K ≥ 3/2, the
  2/5 bound of IF2 Lemma 9.3 disappears.
* **Lemma 2.3.** If R − λ_N is supported on an interval of ≤ Φ(D) integer points (sharp) = Σ_{d≤D}φ(d)
  (≈ 0.3D²), then R = λ_N. So mass at distance ≫ CN (far mass) is unavoidable for fixed C.
* **Theorem 3.1 (K-free edge bound).** If R has (P1) and R(s) ≤ 1 − η on the full classes of
  one modulus e = least multiple of lcm(1..M) above CN, with no other condition, then
  η ≲_C M^{−1/3} ≍ (log N)^{−1/3}. The proof is SPW1 Thm 3.2 with |T̂| ≤ 2N replacing
  |T| ≤ 1 (Lipschitz constant 4πm₀(m₀+1)N/e², corrected per R53 m9). So RSPW with fixed η is false for large N even with K = ∞; it only decays
  like a power of log N, harmless for Lemma 1.1.
* **Lemma 4.1 (dual of RSPW, K = ∞).** η* = 0 iff some ν = g + P ≥ 0 vanishes on [1,N],
  where g is a small-modulus combination and P ≠ 0 is a nonnegative combination of *full*
  large classes (stated on ℤ/Q′; transfer to ℤ via a K = ∞ lift, added per R53 m10).

## Evidence (floating-point LP, HiGHS; not certified)
* **RSPW optimum η (C = 2, K = ∞, support [−L, N+L]):**
  - N = 30: 0.905 at L = 128N.
  - N = 50: 0.820 at L = 64N.
  - N = 80: ≥ 0.732 at L = 32N (runs at N = 80, L = 64N and N = 100, L = 5000 were killed unfinished at the parent's request).
  - Actually run at L ≈ N²/2: 0.861 / 0.832 / 0.798 for N = 30 / 40 / 60 (earlier "~0.78"
    at N = 50 and "~0.75" at N = 80 were interpolated/extrapolated).
  - These are only lower bounds for η* and they grow with L, so no decay rate can be read
    off; no N^{−1/2} decay of the lower bounds is visible for N ≤ 80.
* **Genuine measures.** Every finite-support optimum is a genuine measure on ℤ, e.g.
  RSPW(2, 0.755, K = 1.60) at N = 50 (one run, L = 16N), which gives SPW(2, ≈ 0.24) via
  SPW1 Lemma 1.4 — weaker than IF2 §9's SPW(2, 2/5) LP evidence, so not new.
* **Displaced pseudo-windows.** With C = 8 the LP gives η = 1 at N = 30, 50 (R ≡ 0 on
  [1,N], all mass within distance CN).
* **Single-modulus bounds (upper bounds for η*, K = ∞).** They stay near 0.8: 0.799 at
  N = 300 (e = 630); 0.795 at N = 300 (e = 55440); 0.873 at N = 1150 (e = 2310).
* **Shape of a spread optimum** (QP, N = 30). R ≡ 0 on W. About 1/3 of the mass is in the
  near zone and 2/3 is spread far. The class averages of the far part carry the window's
  sawtooth as a ±25% modulation, but only 34% of its variance is explained by V_D.

## Assessment (heuristic, §4)
* The near part cannot reproduce the window's edge content on the dense part of the Farey
  set. So the far part must carry F_D-content of ℓ²-size ≳ ηN^{3/2}.
* A *bounded-relative-density* far part would force η ≲ C/√N (BDW mechanism). I first took
  this as likely and then withdrew it: absolute line loads, not relative density, are what
  matter.
* An exponentially tilted (Gibbs / max-entropy) far part ∝ exp(Σ_d φ_d(x mod d)) looks
  compatible with η* decaying like a power of log N, i.e. weak SPW true. This is not proved.
* The sawtooth test function gives no obstruction: its maximum on the near zone (≈ D²/25)
  is as large as its average on W (§6 table).

## Not done / open
* No proof of weak SPW. The natural constructions all reduce to the problem itself:
  - translates, positive combinations, lifts;
  - big-prime re-randomisation (IF2), which cannot reach primes ≤ D/log N;
  - "W + U₁ − U₂" with uniform-profile U_i, which is equivalent to the problem.
  The most promising route seems to be a quantitative analysis of a max-entropy far part.
* No refutation beyond (log N)^{−1/3}. Single-modulus arguments look capped near that rate.
  A stronger obstruction would have to couple many moduli.
* Not touched: right-signed mass on (N, CN].
* Possible weaker theorem: weak SPW with C = N^{O(1)}. Thm 5.2 tolerates polynomial C in
  the level, but it needs medium deviations Δ ≤ e^{S}. This would follow from a displaced
  pseudo-window: a measure supported off [1,N] within distance N^{O(1)}, with bounded
  point masses. Such measures exist at N ≤ 50 by LP; they are unproved in general (§2).

## Decision (parent)
Option (c): stop here; a reviewer will check Lemmas 1.1, 2.2, 2.3, Thm 3.1, Lemma 4.1.

## Decision requested (original)
Should I (a) keep going on a construction (max-entropy analysis, larger-N structured LPs),
(b) aim for the weaker polynomial-C statement, or (c) stop here with the reductions and
Theorem 3.1?

## Review R53 repairs (applied, commit-by-commit)
M1 (Lemma 1.1 retitled, bullet 3 and closing paragraph limited to "this route"); m1 (remark:
hypothesis-free use of Thm 5.2); m2 (η/K ≥ 4N^{−A₁}); m3 (KARY3 pointer conditional); m4
(IF2 Lemma 9.3); m5 (K ≥ 3/2 is C = 2); m6 (σ ≲ m₀²/(η log N), paragraph superseded by
Thm 3.1); m7 (Φ(D) ≥ 3N + 2 for N ≥ 38); m8 (ℓ integer points, sharp); m9 (m₀(m₀+1));
m10 (Lemma 4.1 periodic model and K = ∞ lift); m11–m13 (numerics: lower bounds only,
interpolated values flagged, headline softened to Assessment).
