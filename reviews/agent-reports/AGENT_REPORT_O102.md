# AGENT REPORT — O102 (m/n: pin down the density transition)

Branch `side-agent/mn-transition`. Deliverable: `EXCEPTIONAL_MN2.md`; scripts `scripts/emn2_*`.
One self-review pass has been done (deep reviewer over `f272550..`). It found 1 FATAL, 4 MAJOR and
several MINOR issues; all were repaired in later commits (details below). There has been no
independent hostile review yet.

## Results

Notation: `A = log N / m^{1/3}`; ρ_exc and ρ_rep are the proportions of m-exceptional and
m-representable primes in (N/2, N].

1. **Theorem U (upper side, g ≡ 1). PROVED relative to MN Cor 3.2, Bombieri–Vinogradov and Shiu.**
   * For every ε there is an `A_ε` with `ρ_exc ≤ ε` whenever `log N ≥ A_ε m^{1/3}`, uniformly in m ≥ 4.
   * This removes the `(log m)^{4/3}` from MN Cor D.
   * MN Cor D lost that factor only in the integer→prime transfer (it divided by π(N)).
   * The fix works directly with primes:
     * Bonferroni of bounded depth r ≍ s in the *reduced* CRT model. For primes every fibre c mod L_K is reduced, so MN Cor 3.2's two-sided mass `μ_c ≍ t³/m` applies to every fibre, and no selector or bad-fibre event is needed.
     * BV at level N^{0.45} handles the error terms, with Cauchy–Schwarz against a term-multiplicity bound `Σ M(q)²/φ(q) ≤ t^{O_r(1)}` (Shiu).
   * The dependence on ε is ineffective, through Siegel in BV at level `L^{−A'(r)}`.
2. **Theorem L (lower side). PROVED relative to ET Thm 7.1 and the structure of ET's proof of Prop 1.4, plus BT and Shiu.**
   * Statement: `ρ_rep ≪ L³/m + (L³ + L² log² m) log L/φ(m) + m^{−0.35}`. So `ρ_rep → 0` once `A (m log m/φ(m))^{1/3} → 0`.
   * This beats PW's `L³ log² m/φ(m)` by a factor of log m.
   * Type II is made sharp (`≪ L³/m`) via ET's three-way flip with m, plus the coprimality gain from (e, m) = 1.
   * In Type I, ET Prop 1.4's `log(1+k)` is confined to a lower-order range by Pólya–Vinogradov (Lemma 3.3).
3. **Gap now** a factor `(m log m/φ(m))^{1/3} ≪ (log m log log m)^{1/3}` in log N. It was `(log m)²(m/φ(m))^{1/3}`.
   What remains is exactly two things:
   * ET's Type I Brun–Titchmarsh `log log N`, which is open even for m = 4 (ET §9 says so);
   * the `m/φ(m)` gain in ET Prop 1.4, which is lost at the square-q main terms.
4. **Numerics (EVIDENCE)** for m ≤ 300, using an exact representability scanner based on PW Cor 2.2/2.4.
   It was validated per prime against a brute force: 1464 exceptional (m, p) pairs, 0 mismatches.
   * Even m in [60, 300]: `L_{1/2} = (1.95 ± 0.05) m^{1/3}`, with local exponent 0.333.
   * Odd m sit lower (1.63–1.92) and drift upward (local exponents 0.36–0.40). This is a parity effect.
   * The profile in A fits `1 − exp(−κA³)` with κ ≈ 0.094, which is PW's Poisson heuristic with an effective constant.
   * The mean solution counts are strongly overdispersed.
5. **Conjecture C2:** `ρ_rep = F(A) + o(1)`, with F non-degenerate. That would mean there is **no sharp threshold constant**: the window is of order m^{1/3}. Supporting this so far is only finite data plus the Poisson model.

## Self-review repairs
* **FATAL — Lemma 3.1(b).** It had used Shiu on short progressions. It is re-proved by truncating s ≤ U^{1/2} via Rankin, applying Shiu only for u > s^{1.1}, and swapping the order of summation for small u.
* **MAJOR — Lemma 3.3.** It had put absolute values inside ET's signed (7.11). It is rewritten to keep ET's signed treatment of q < D and q > kD; absolute values are taken only in the middle range. The odd-d reduction is accounted for, so the condition is now `D ≥ k log⁴`.
* **MAJOR — Lemma 1.2.** Restricted to k ≤ K.
* **MAJOR — Lemma 3.1(a).** Added the hypothesis `Y ≥ log m`.
* **MAJOR — numerics.** "Composite vs prime" is corrected to "even vs odd", and the odd-m data have been added.
* **MINOR fixes:**
  * the BV constant;
  * the profile ranges;
  * per-prime validation with a failing exit status;
  * documenting that p | m is skipped;
  * the ET theorem number (1.1, not 1.7) and a lemma cross-reference.

## Points for the parent's hostile review
* **Theorem U** is the main claim; please re-check it independently. In particular:
  * MN Cor 3.2's reduced-fibre lower bound is used for *every* reduced c;
  * the definition of the reduced CRT model and the exact main-term identity in Thm 1.3;
  * the Shiu application in Lemma 1.2: modulus k ≤ X^κ, n ∈ (kx, 2kx];
  * the claim that B with repeated ℓ have empty intersection.
* **Theorem L** depends on reproducing ET's (7.11) argument with a modified middle range. This is only a sketch-level re-derivation; it is not line-by-line. It deserves a careful check, or else a downgrade of Theorem L to "PROVED modulo Lemma 3.3". PW's own Type II/I bounds remain as a fallback, giving PW's weaker lower range.
* Prop 3.4's small-box bookkeeping (k^{0.03} terms) is terse.
* Not done:
  * ledger lines in `DISCOVERIES.md` / `STATUS.md` (left to the parent to avoid merge conflicts);
  * a literature check that "prime-model Bonferroni + BV" at the transition is new. It is very plausibly standard technique; what is new is the statement for m/p.
