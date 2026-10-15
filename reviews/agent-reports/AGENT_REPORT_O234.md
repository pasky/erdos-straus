# AGENT_REPORT_O234 — the exponent cap as a sieve-dimension knob, uniformly; pointwise e*(n); the exact family 𝒟_e(M)

Branch `side-agent/cap-interpolation` (merged side-agent/cap-growing and side-agent/review-cap-growing first).
Deliverables: `CAP_INTERPOLATION.md` (deep file, §§0–7), memos `BRAINSTORM/z10_*.md` (4, indexed in
BRAINSTORM/README.md), scripts `scripts/z10_*`, outputs `data/z10/` (tiny). **ES is not solved; no infinite case of
ES is claimed.**

## SHARP:
1. **Exact dictionary (Prop 5.1, PROVED, exhaustively checked M < 1200).** In the overflow cube the solution depends
   only on D = c²d: for ANY modulus M ≡ 3 (4), A = (M+1)/4, p ≡ −4D (mod M): x = (p+E)/4, y = pA, z = pxA/D.
   It is an ES^{(y,e)}(p) solution iff **D ∈ 𝒟_e(M): rad D | A and per prime s | D, v_s(D) ≤ 2v_s(A) or (s odd,
   v_s(D) even ≤ 2v_s(A) + 2e)**. e = 0 is exactly the 3/4 note's ℛ(M) = {−4D : D | A²}. Consequences: the cube
   (c, d, j) and any "several overflow parameters" are redundant coordinates; supply dimension is exactly e + 3 at
   composite moduli (Cor 5.2) — no tower at fixed e; the extra dimensions are exactly non-integrality of z
   (Prop 5.3: nothing hidden at e = 0); T1 for every e and M ((−D/M) = −1). KARY3 does not literally apply for
   e ≥ 1 (that is why (e+2)/(e+3) > 3/4 is no contradiction); the (e+3)/(e+4) analogue is now a concrete target.
2. **The knob saturates at e ≍ log log N, with a matching ceiling that holds even at e = ∞ (Thms 2.1, 3.1).**
   Uniformly in e ≤ log log N: exceptions ≤ N exp(−c(log N)^{(e+2)/(e+3)}/((e+2)log(e+3))) — c_e ≍ 1/(e log e)
   (O229 feared ((e+1)(e+2))^{−e}). At e ≍ log log N: N exp(−c log N/(log₂N log₃N)). Rankin: the prime-modulus large
   sieve with cube classes cannot beat this at ANY cap — although ES^{(y)} = ES^{(y,∞)} is a pointwise THEOREM. A
   quantitative B6: this sieve can never meet "all p ≥ p₀", not even for a true statement.
3. **Scale coincidence + GRH pointwise cap (§4).** Covering arguments need e ≥ (log log p)^{1−o(1)} for infinitely
   many p (Prop 4.1, PROVED, Linnik) — the same scale as the sieve saturation. Under GRH (Hooley–Lenstra +
   Lagarias–Odlyzko; citation-level sketch) the minimal cap is e*(p) ≤ C_ε(log p)^{2+ε} (one mute prime) and
   e*(p) ≤ exp(O(√(log₂p·log₃p))) (≍ √(log₂p/log₃p) mute primes + Minkowski II). Unconditionally no bound on e*(n)
   in terms of n is known (FROBENIUS Thm 4.2 is ineffective; (J)43 Thm 5.1 is family-form).

## Results by goal
* Goal 1 (uniformity / growing e / phase boundary): Thm 2.1 (PROVED rel. Gallagher's PNT (G) — cited, not re-derived
  — plus BV for finitely many small e and Montgomery's large sieve). The fix: moduli 4c₀d₀ ≤ X^{1/(10κ)}, so
  log x/log q ≥ 4κ and Gallagher gives relative error e^{−cκ} per modulus — BV's divisor weights (the non-uniform
  step) disappear; mass via a Rankin lower bound (Lemma 1.1). Remark 1.3: O229's exactness hypothesis
  v_s(c₀) = v_s(K) is unnecessary. Phase boundary: no power saving, no "all n" from this side at any e (Thm 3.1);
  pointwise side in §4. The "target theorem shape" (ES^{(y,e(n))} for ALL large n, e(n) small) is obtained only
  under GRH (Thm 4.2), with e(p) = exp(O(√(log₂p log₃p))).
* Goal 2: composite multipliers / higher overflow — Prop 5.1 + Cor 5.2: dimension exactly e + 3, no unbounded tower;
  3/4-note architecture should give (e+3)/(e+4) (Assessment: only the class supply changes); KARY3-type ceiling
  (e+3)/(e+4) is an Assessment. Exponent table in §5.
* Goal 3 (e = 0): Prop 5.3 — the overflow dimension IS non-integrality of z; x is always integral in the family;
  at e = 0 the family is ℛ(M) and CRT architectures are capped at 3/4 by KARY3 (no fourth dimension to unlock).
* Goal 4: PM-SQ_± in C to 10⁷: 0 exceptions among 1 248 419 non-squares n ≡ 1 (8), all 1580 odd squares unfired;
  least |u| record 19 (≤ 10⁶, n = 33 201) → 41 (≤ 10⁷, n = 8 452 161, word (4, 41, 51 854), A = 163), both
  re-verified independently with the exact word identity and Jacobi symbol.

## Checks run (all in data/z10/)
z10_cube_check (2000 cube solutions, 1505 composite M, 486 non-exact; exact rationals + Def 1.1); z10_rfamily_check
(random, e = 2: 3000/3000, e = 0: 2000/2000) and z10_rfamily_exh (exhaustive M < 1200, all D, e = 0, 1, 3:
36 458/36 458 each); z10_t1 (7820 classes, none contains a square); z10_mass (S_e(X) to 4·10⁶, saturation at small
e for small X); z10_leastmod (all 78 496 primes ≤ 10⁶, least certifying prime modulus per e; 0 odd squares hit);
z10_grh_r (Thm 4.2(a) prime ≤ 251 for all p ≡ 1 (4) < 10⁶; adversarial p ≈ e^{32}: 47/71; 396 solutions exact);
z10_sqpm.c (10⁶ and 10⁷).

## Points for the hostile reviewer
* Input (G): the exact form/range of Gallagher's Theorem 7 (cited from memory) and the exceptional-modulus handling
  in Prop 1.2 (drop one prime of the odd part of q₁; χ₋₄ not exceptional for large T).
* Thm 2.1's parameter bookkeeping (u, k, collision term) — rewritten once; Lemma 1.1's Rankin truncation.
* Thm 3.1: the Euler-product bound Σ_s log(1 + 1/(2σ s log s)) ≪ 1/(σ log(1/σ)).
* Thm 4.2 is a SKETCH: Hooley error ranges, linear disjointness with ℚ(√p), the k ≥ 2 large-index range via the
  lattice count, and that only the small range sees log p (forcing x ≥ (log p)^{2+ε}). Label CONDITIONAL.
* Prop 5.1: s = 2 case (D may be even only with v₂(D) ≤ 2v₂(A)); the claim "every certificate of shot shape" is
  scoped to solutions of the displayed form (y = pA); Type I-shape overflow is NOT analysed.

## Sparks (not pursued)
1. Prove the KARY3 analogue for 𝒟_e(M) (cap (e+3)/(e+4) for CRT architectures over 𝒟_e classes) and run the 3/4
   note's harvest with 𝒟_e atoms to get (e+3)/(e+4) — a mechanical but long transfer.
2. Type I-shape analogue of 𝒟_e (overflow with p | x): does Type I add its own e dimensions (total 2e + 3?).
3. Unconditional EFFECTIVE bound for e*(n) via log-free zero density + Deuring–Heilbronn at modulus ≈ n (would give
   e*(n) ≤ n^{o(1)} or exp(n^{o(1)})?).
4. Composite-modulus version of the Thm 3.1 ceiling (the e = ∞ supply at composite M is still de Bruijn-type).
5. Pointwise target CONJECTURE "e*(p) ≤ C log log p": under GRH it needs the discrete-log non-concentration of
   EXPONENT_CAP Dictionary 3.3(c) for some r ≤ polylog p — an "averaged over r" version may be provable under GRH.
