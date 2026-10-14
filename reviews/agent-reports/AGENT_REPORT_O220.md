# AGENT_REPORT_O220 — checkpoint 2 (q = 9 decided: CLOSED)

**SHARP:** exact small-level enumeration is cheap once the class-divisor routes are made *exact by factoring*: factor F
(1 + T^s m'g'², g'T^{s−1} + w₁, T^{s−2} + m'w₁², m'C₁, w₁C₁) over F_q and run over all its divisors of the required degree. This
speeds up the enumeration about 1000× compared with candidate search (q = 9, s = 12: 90 s → 0.06 s). At q = 9 the route bounds
overcount the true tuple counts by factors 10³–10⁴ at s ≈ 12–18.

## New results (checkpoint 2)
1. **Theorem 5.2 (PROVED, computer-assisted):** q = 9, k ≥ 2: O(9, T^k) ≠ ∅, no finite linear covering of ES₉(T^k). Covered measure
   summed over the 8 c-slices ≤ 3.58 (exact counts s ≤ 22: 0.5922; route bounds 23 ≤ s ≤ 80: 2.695; tail s > 80 ≤ 0.080, with
   Lemma 4.1 linearised (Lemma 5.1); Case A ≤ 0.175). `scripts/fz_certify9.sh` (fail-closed), log `data/fz/certify9.txt`.
   **With (J)51 and Thm 3.1: all q = 3^r, r ≥ 2, k ≥ 2.** Only q = 3 remains (Conjecture 0.2).
   Validation of `fz_enum.c`: all 8 routes forced separately reproduce bsE_famcount (q = 3, 5, 7); at q = 9 factoring vs
   candidate-search routes agree (all s ≤ 13; 1053 patterns 14 ≤ s ≤ 17); factorisations self-checked fail-closed (product +
   Rabin irreducibility); R220's independent q = 9 enumeration through s = 9 matches.
   Exact q = 9 per-level masses decay fast (1.8·10⁻⁵ at s = 22), so the true sum is probably ≈ 0.59 < 1 (EVIDENCE; that would give
   every c-slice).
2. **q = 3, s₀ estimate (§5.3, Assessment):** the bound tail drops below 0.5 only at s₀ ≈ 80–85. An exact union of cylinders up to
   s₀ is infeasible (~10²⁰ enumeration work). Conjecture 0.2 is **not** a feasible finite computation with these tools.
3. **Goal (2) A = T (§6):** Prop 6.1 (PROVED): for k = 1, depth-1 families (whole classes u₀) occur only for u₀ ∈ {−1, −2}
   (the constant families of FUNCTIONFIELD_ES Prop 1.4, plus three Case B tuples, all in class −1). So for q = 3^r ≥ 9 the q − 3
   slices u₀ ∉ F₃^* have all cylinders of depth ≥ 2, i.e. (H1) is restored. On them the tuples are (B^{k=1}): m'wC = T^s + v,
   w + C = g'v, T ∤ m'g'wCv, mass q^{−⌈(s−1)/2⌉}. The k = 1 counting certificate (Case B routes without the T-adic constraints;
   Case A redone with T ∤ K) is **not done**.
4. R220 review merged, repairs m-1..m-9 applied ("(R220 repair)").

## For the parent
* Please review §5 (Thm 5.2) — the new trust points are `fz_enum.c` (factoring routes), `fz_hybrid.c`, and the linearised Rankin
  tail in `fz_tail.c` (RANK = 1; the q = 27 certificate pins RANK = 0, so §3 is unchanged).
* Next (if wanted): the k = 1 certificate on the q − 3 slices for q = 3^r ≥ 9 (adapt fz_sum/fz_tail/fz_enum to (B^{k=1}), redo Case A),
  then goal (3).

## Sparks (new)
* At q = 3, exact counts could replace the bounds up to s ≈ 35–40 (fz_enum at q = 3 is about √3^s ≈ 3^{s/2}); that still leaves the bound
  tail of §5.3 (≈ 500 at s ≈ 40), so the union-bound-free route needs a structural idea, not compute.
* The overcount factor 10³–10⁴ at moderate s suggests the route bounds lose mostly in the class-divisor step. An *average* version
  of Lemma 1.5 (over the data fixed before the class step) might give the missing constant factor at q = 3.

---

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
* Corollary 4.2 at q = 3 (R220 repair m-8: rephrased): the union-bound tail beyond s₀ converges like 3^{−s/10}·exp(O(s/log s)),
  but at q = 3 union bounds fail even with exact counts, so one would need the exact *union* of cylinders up to s₀ — finite in
  principle, infeasible unless s₀ is small, and it would give the *conclusion* of Conjecture 0.2 (no finite linear covering),
  not x*_c ∈ O. Estimate of s₀: see checkpoint 2.
* q = 9: for t ∈ {2, 3}, R1 is the triple-factorisation count of the single polynomials T^{s−2} + v₁ (≤ 8 of them per s):
  exact via factoring, for all s — cheap partial improvement.
