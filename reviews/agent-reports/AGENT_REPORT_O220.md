# AGENT_REPORT_O220 — small-q function-field sterility (wave Y-f), checkpoint 1

Main file: `FF_STERILE_SMALL.md`. Scripts `scripts/fz_*`. Log `data/fz/certify.txt`.

**SHARP:** *A monic factor of degree > deg v₁ determines v₁ by Euclidean division* (FF_STERILE_SMALL Lemma 1.1/1.3:
v₁ ≡ −T^{s−2} mod every factor of m'w₁C₁). Every O216 route that "paid for v₁ and then for a factor" paid twice. Together
with the trivial T-adic refinement of class-divisor bounds below the Coppersmith threshold (Lemma 1.4: cost q^j for j
extra digits, instead of losing the class bound) this moves the r = 3 continuum exponent from 0.000 to **−0.100**
(the Elsholtz–Tao point (1/5,1/5,1/5,2/5), all routes = 2/5), and with fixed-q divisor bounds (Lemma 4.1, divisor counts
are q^{o(n)} at fixed q) the exponent is 2/5 for **every** odd q, including q = 3 and 9. The barrier at small q is now
purely the *finite* part of the union bound.

## Results
1. **Theorem 3.1 (PROVED, computer-assisted; same standard as (J)51):** q = 27, k ≥ 2: O(27, T^k) ≠ ∅, ES₂₇(T^k) has no finite
   linear covering; covered measure summed over the 26 c-slices ≤ 3.06 (finite s ≤ 80: 3.0180; tail ≤ 2.9·10⁻⁴; Case A ≤ 0.0097),
   so ≥ 20 slices are more than half uncovered. With (J)51 this gives **all q = 3^r, r ≥ 3**.
   Cross-checks: independent exact-rational re-implementation `fz_sum_check.py` (3.017899 ≤ 3.018046); new routes vs exact
   bsE_famcount counts q = 3 (s ≤ 19), 5 (s ≤ 13), 7 (s ≤ 11): 0 violations; Lemma 4.1 brute force: 0 violations;
   `fz_tail` with new routes off reproduces `fs_tail` exactly.
2. Lemma 2.1 (PROVED): Case A count ≤ (α+1)³ q^{(α−1)/2} 3^{α/2} (replaces 6^α, whose geometric tail diverged at q = 27).
3. q = 9 (CERTIFIED statement about the method): with all routes the finite sum is 41.9 > 8, and Σ_{s≤8} alone is 9.2 > 8;
   tail is negligible (terms 10⁻⁶ at s = 80). (Σ) at q = 9 needs exact Case B counts up to s ≈ 20–24 (or sharper small-s
   bounds). Not attempted.
4. Goals (2) A = T and (3) cyclotomic thirds-corner vs x*_c: not started.

## Requests / decisions for the parent
* Review Thm 3.1 (the new lemmas 1.1–1.4, 2.1, 4.1 are elementary; the certificate reuses the O216 harness).
* Should I (a) push q = 9 (needs an F_9 exact enumerator of Case B tuples for s ≤ ~20 — substantial compute, outcome uncertain),
  or (b) go to goal (2) A = T / goal (3)?

## Sparks
* The division duality (short interval T^{s−2} + v₁ ↔ residue class mod a factor) is the F_q[T] face of "ab | N, N in a short
  interval ⇒ N determined mod a" — over ℤ: for the Type II slice, n = (p+e)/4 with e small is in a short interval; a divisor
  > e of 4n determines e mod it. Might sharpen the ℤ box bounds of MORDELL17 (the (J)26 r₀) the same way.
* Corollary 4.2 at q = 3: the union bound tail beyond s₀ converges like 3^{−s/10}·exp(O(s/log s)); combined with the exact
  union to s = 21 (FF_STERILE_PROOF §5, ≈ 0.49 covered per slice) this is a *finite* computation problem for Conjecture 0.2 —
  but s₀ is probably several hundred; needs an estimate.
* q = 9: for t ∈ {2, 3}, R1 is the triple-factorisation count of the single polynomials T^{s−2} + v₁ (≤ 8 of them per s):
  exact via factoring, for all s — cheap partial improvement.
