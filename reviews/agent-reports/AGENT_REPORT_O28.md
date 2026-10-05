# AGENT REPORT O28 (branch side-agent/kary2-loglog) — checkpoint 1

Deliverable: `EXCEPTIONAL_KARY3.md`, `scripts/kary3_moments.py`,
`data/kary3/moments.txt`. Unreviewed.

## Results

1. **Goal (1) done: the `(log log N)^{3/4}` loss of K2 Thm 5.1 is removed.**
   Thm 4.1: every mixture of ℛ(M)-, (a,D)-, Case-A and selector classes,
   arbitrary moduli, no B: `log(1/Eν) ≤ Cλ^{3/4}`. Cor 4.2: coefficient-sum
   CRT methods save `≤ C_A(log N)^{3/4}`.
   * The diagnosis (§1): the loss is Rankin's. A dyadic block of y-smooth
     moduli is bounded by `e^{−u}` times the whole smooth sum `≍ log y`,
     which forces `u₀ ≍ log log y`. Hölder variants lose the same.
   * The fix (§§2–3) is a *local moment*. Put
     `Z_y(M) = Σ_{p^ν|M, p^ν≤y}Λ(p^ν)/log y`. It has bounded mean. On a
     smooth M of size `y^u` it is `≥ u/2`, unless M has a squarefull part
     `> M^{1/2}` (Lemma 2.1).
   * Its 4th moment needs only `D | M` with `D ≤ y⁴`. Shiu in progressions
     to small moduli then gives smooth blocks `≪ K(log K)²u^{−4}` (Lemma 2.3).
     This is summable against the `u²` growth, so `𝔐_R(y) ≪ (log y)³`.
   * Case A (Lemma 3.1) splits on `r ≷ K^{1/4}`. For large r it puts the
     moment on r and uses ElT Cor 7.4 (linear). Otherwise it puts the
     moment on h and uses ElT Thm 7.1 per fixed r, with
     `ρ_{4rL²} ≤ ρ_{4r}`, which removes the moment modulus L. ElT (7.10)
     with `k = 4s` then handles the sum over r.
   * Applying ElT Prop 1.4 directly would lose `log(1+k)`, i.e. a full
     `log y`. The split above avoids that.
2. **Goal (2) done for prime order; exact open scope stated for class order.**
   * Thm 5.1 is the truncated-weight cap
     `Cλ^{3/4} + 2d₀log(CΛ³/d₀) + O(d₀)`, with `d₀ = λ/L₀`. It adds one
     top block above `e^{L₀}` to the K2 block structure.
   * Cor 5.2: (A log N, k)-mixed majorants (prime order ≤ k) of any K2
     family save `≤ C_A[(log N)^{3/4} + k log log N]`. This is TU Cor 3.2
     for all K2 families.
   * Cor 5.3 covers class order k with `≤ r` large primes per modulus.
   * Still open: class order when moduli have unboundedly many large
     primes. EK Thm 2.5's locality is in prime coordinates; a version in
     class coordinates would be needed.
3. **Goal (3): the Λ² middle window is subsumed for the cap (§6).** Λ²
   majorants are in Thm 4.1's class, which has no ω-hypothesis, so the cap
   is `CL^{3/4}` for all r. The TW4-internal route (hub count) is moot for
   the caps and was not pursued.

## Inputs, risks, what to check hardest

* External inputs:
  * Shiu Thm 1 (as in K2/ET);
  * ElT Cor 7.4, Thm 7.1 and display (7.10).
* (7.10) is an intermediate display inside ElT's proof of Prop 1.4, not a
  numbered proposition. I checked from the text (pp. 30–32) that its
  proof puts no size condition on k. Please re-verify this.
* Uniformity checks:
  * ElT Cor 7.4 in Lemma 3.1(i): coefficient `4h²L ≤ R'^{14}`;
  * Thm 7.1 in (ii): coefficients `≤ N²`, `ρ ≤ 2`.
* The claim that EK Thm 4.1 works for the truncated-level function class
  (closure under conditioning) and with one wide "top block".
* §4.3 downstream pointers (PRIMELAW, LARGESIEVE, INTERFREQ, TUPLES) are
  pointer-level. PRIMELAW's Γ* satisfies the four facts used.

## Proposed DISCOVERIES edits (for the parent, after review)

* (D)18: replace `C(log N)^{3/4}(log log N)^{3/4}` by `C(log N)^{3/4}` (via
  KARY3 Thm 4.1 / Cor 4.2), and delete "Still excluded item 1".
* (D)19, (D)20, (D)22: drop the `(log log N)^{3/4}` and `(log λ)^{3/4}`
  factors.
* (D)21: add Cor 5.2 (prime order, all K2 families) and the open
  class-order scope.
* (D)16: note that the middle window is subsumed for the cap.
* STATUS "up to a (log log N)^{3/4} factor without a B-hypothesis": delete.

Numerics (EVIDENCE): the smooth first moments `S(y)/(log y)³` converge
(X = 10¹²) and decrease over y = 7..31. The block profile has `u⁴b ≤ 0.25`.
