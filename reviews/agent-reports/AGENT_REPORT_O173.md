# AGENT_REPORT_O173 — function-field sterile point x*_c (q = 3, A = T²), checkpoint 1

Branch side-agent/ff-sterile-point. Main file FUNCTIONFIELD_ES3.md. Scripts scripts/ff3_caseB.c (fast exact
search), scripts/ff3_check.py (independent checker, sympy factorisation + end-to-end ES identity),
scripts/ff3_ctl.sh (control). Data data/ff3_*.txt (tiny).

## SHARP:
1. **Conjecture 0.2 looks like a lottery statement (heuristic), and the better target is O(3, T²) ≠ ∅.** The O166/R166 heuristic
   ("expected number of covering families diverges over deg L'") is wrong: Lemma 2.1 (PROVED) bounds
   deg L' ≤ 2N − k − 1 at level N, so each level carries finitely many families, and the corrected heuristic gives
   a *convergent* expected count ≈ Σ_N poly(N)·3^{−N} at a random slice point. Heuristically O(3, T²) ∩ slice then
   has positive Haar measure (Assessment; finiteness per level alone does not imply it). Control data: random
   points agreeing with x*_1 mod T⁶ showed a family in 1 of 40 cases (truncated search, deg L' ≤ 9), so the
   empty search at x*_c is consistent with x*_c being typical; no structural obstruction was seen.
2. **Dictionary (analogy): proving NON-existence of a finite covering of ES₃(T²) by the measure route needs
   a count of a Kloosterman-type hyperbola mod T^s that beats square-root size by a summable factor.** Lemma 3.1 (PROVED) shows only families with j − γ ∈ {0, 1} matter for the union,
   and there a family is a point of EE' = 1 + T^s·L'g', E ≡ E' ≡ −1 (mod L'), in a degree box. Under T ↦ 1/T
   this becomes a factorisation T^{s} + v = m'·w·C with v | w + C (a short-interval divisor problem). The
   elementary count gives q^{s/2} ≈ q^N cylinders per level — square-root size (exponent match, not a
   proved barrier), i.e. mass ≈ q^{−k/2} per level, no decay. Any summable saving (1/N², q^{−δN}) plus a finite
   census and a Case A count would prove O(3, T²) ≠ ∅ (no finite linear covering). This is barrier B3 in function-field form, now in the depth aspect (modulus T^s) where
   special tools might exist.

## Results (labels)
* Lemma 1.1, 1.2 (PROVED): exact Case B reduction at slice points; the divisor E (or E') is the least CRT
  residue and g' is forced, so the search needs one xgcd per (L', j, branch) and no factoring.
* Lemma 2.1 (PROVED): parametrisation m'wC = T^s + v, w + C = g'v; deg L' ≤ s − 3 ≤ 2N − k − 1; j = 0 (more
  precisely N + γ ≤ 2) impossible — proves the O166 claim "j = 0 impossible".
* Lemma 2.2 (PROVED): Z, Z' ≠ 0, L' | Z + Z', Z + Z' ≠ 0 (O166 claims, R166 D5, now proved).
* Lemma 2.3 (PROVED, x*-specific): z ≠ z', |z − z'| ≥ N − γ, v_T(Z + (1 + cT)Z') = γ, and
  **(N + 1)/4 ≤ deg L' ≤ 2N − k − 1** at x*_c. So a search over all j ≤ 4 deg L' − k is complete per deg L'.
* Lemma 3.1 (PROVED): (j, γ) → (j − 1, γ + 1) keeps validity and enlarges the cylinder.
* EVIDENCE (complete range, independently cross-checked on small ranges): **no linear family of level N ≤ 8
  and no family with deg L' ≤ 13 (any level) is valid at x*_c, c = 1, 2** (with the ES2 Case A theorem).
  A = T³ (k = 3): 0 Case B families at x*_c for deg L' ≤ 11, complete j-range (all levels N ≤ 7 excluded).
* Elementary count (PROVED, sketched in §3): ≤ q^{(N+1+γ)/2 + o(N)} Case B cylinders at level N for given γ.
* Neither (A) a proof of Conjecture 0.2 nor (B) a covering family at x*_c was obtained. (B) looks unlikely at
  x*_c on heuristic grounds (the poly(N)·3^{−N} heuristic leaves a small tail). For (A) no x*-specific
  obstruction was found beyond Lemma 2.3, and the control gives no sign of one (Assessment).

## What I did not do
* (C) q = 4: needs F₄ arithmetic in ff3_caseB.c (prime fields only now). Not done.
* No census U(m) of the covered slice mass yet (needed for the measure route).

## Sparks
* Depth-aspect tools: Kloosterman sums mod T^s are explicitly computable (T-adic stationary phase); the needed
  count is "points of xy ≡ 1 mod T^s with deg x + deg y = s + r and x ≡ y ≡ −1 mod L'". Beyond-square-root
  counts in the depth aspect (Postnikov-type, Milićević) might transfer to F_q[T] at fixed q.
* Reversal T ↦ 1/T turns it into divisor sums of T^{s+r} + F̃ over the short interval deg F̃ ≤ r: short-interval
  divisor problems in F_q[T] are known for large q (Keating–Rodgers–Roditty-Gershon–Rudnick); for q = 3 fixed,
  open. A large-q version (q → ∞ along char 3: F_{3^r}, A = T²) might be provable — a "large-q" theorem that
  O(q, T²) ≠ ∅ for q = 3^r, r ≫ 1.
* A census of U(m) (slice mass uncovered at level ≤ m) to m ≈ 12 would make the measure route quantitative.
* Choose the point differently: points where L'-congruences are adversarial (x ≢ 1 off T) might admit a
  structural proof even though x*_c does not.
