# AGENT REPORT O28 (branch side-agent/kary2-loglog) — checkpoint 2

Deliverable: `EXCEPTIONAL_KARY3.md`, `scripts/kary3_moments.py`,
`data/kary3/moments.txt`. Self-reviewed (`reviews/kary3-self-review.md`, deep-mode subagent; D1–D7 applied, none affecting Thm 4.1).

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
     `Cλ^{3/4} + 2d₀log(C(1+Λ³/d₀)) + O(d₀)`, with `d₀ = ⌊λ/L₀⌋`, `L₀ ≤ λ`. It adds one
     top block above `e^{L₀}` to the K2 block structure.
   * Cor 5.2: (A log N, k)-mixed majorants (prime order ≤ k) of any K2
     family save `≤ C_A[(log N)^{3/4} + k log log N]`. This is TU Cor 3.2
     for all K2 families.
   * Cor 5.3 covers class order k with `≤ r` large primes per modulus.
   * Cor 5.3's r counts primes above the *fixed* W. Twin moduli,
     η-twins and the 3/4 note's atoms are not bounded-r in this sense
     (self-review D1); Thm 4.1 still covers them.
   * Still open, under TU's hypothesis that class moduli are `≤ N^A`:
     class order k with
     `max(L^{4θ/3−1}, L^θ/(r log L)) ≲ k ≲ L^θ/log L`. This window is
     nonempty only when r is unbounded. EK Thm 2.5's locality is in prime
     coordinates; a version in class coordinates would be needed.
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
(X = 10¹²) and decrease over y = 7..31. The block profile has max `u⁴b = 0.385` over all complete blocks.

## Checkpoint 2 (after hostile review R28)

* **R28 defects 1–5 applied**, each in its own commit:
  1. ElT's second slip (reciprocity sign; the Kronecker character of
     −ka is never principal) is now recorded in §3.
  2. Threshold form (2.1′), cited in Lemma 3.1.
  3. Lemma 3.1(ii) now reads `h > K^{3/4}`, `(2/u)^k`.
  4. Thm 5.1, `L₀ > λ/2`: the top block can be treated as a linear block.
     ETw Cor 4.3's proof uses only 1-locality and the caps.
  5. The status line now lists the K2/EK dependencies ("PROVED given
     K2/EK as reviewed").
* **Goal (3), the TWIN4 middle window (§7, Lemma 7.1, PROVED):** §6 is
  now checked against TW2/TW4's own definitions.
  * TW2 Setting 3.0 charges all primes, and its classes are ℛ(M)-classes.
  * For admissible g (TW4 Setting 3.0^{(r)}), `g²` is a K2 majorant of
    level ≤ λ, and TW's saving is `log(1/E g²)`.
  * So TW4 Thm 7.1, Prop 9.1, Cor 9.3 and the middle window `r ≍ log L`
    are superseded *as caps*: the cap is `CA₀^{3/4}L^{3/4}` for every r,
    and B is not needed.
  * The TW4 §12 hub-count problem concerns only TW4's own Λ² mechanism
    and has no consequence for any cap. I deliberately did not pursue it;
    that would be padding.
* **Class-order window of TU Cor 3.4 (§7, Lemma 7.2, PROVED):** a residue
  class whose prime powers are ≤ N^A and with `log d ≤ (k−1)A log N/2` is
  an intersection of ≤ k classes of modulus ≤ N^A (next-fit packing plus
  CRT).
  * So TU Cor 3.4's *literal* hypothesis is, up to a factor 2 in k, a
    level hypothesis at λ ≍ kL.
  * Its window therefore cannot be closed from that hypothesis alone.
    Closing it would improve level-λ caps from λ^{3/4} to (λ/L)·polylog,
    which the KARY ledger cannot give. Attainability at such levels is
    ET §2.5's open question.
  * The window makes sense only for structured order: prime order (closed,
    Cor 5.2) or intersections of *family* classes. The latter is closed
    for boundedly many large primes per modulus (Cor 5.3) and open
    otherwise.
  * Assessment, not proved: in EK's abstract pattern model, class order k
    over m-prime conjunctions is indistinguishable from prime order km.
    So the remaining window is probably genuine and needs ES-specific
    (TC-type, O24) input.

Proposed DISCOVERIES addition for (D)16: "TW4's Λ² cap, including the
middle window r ≍ log L, is superseded as a cap by KARY3 Thm 4.1 / Lemma
7.1: `C L^{3/4}` for all r, no B." For (D)21: "TU Cor 3.4's literal
hypothesis equals a level-≍kL hypothesis (KARY3 Lemma 7.2). Prime order
is closed (Cor 5.2); family-class order is closed for bounded ω_{>W}
(Cor 5.3) and open otherwise."

Natural next step (not started): ES-specific structure of intersections
of forced classes with many large primes. This overlaps O24 (TC_θ), so I
stop here.
