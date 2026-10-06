# AGENT REPORT O60 — unify the 3/4 and 1/4 ceilings

Branch `side-agent/unify-ceilings`. Deliverable: `CEILINGS_UNIFIED.md`,
`scripts/unify_toy_lp.py` (+ output `data/unify_toy_lp.txt`).

## Results (labels as in the file)

1. **Prop 1.1 (PROVED given the 3/4 note).** `log(1/δ*(T)) ≫ (log T)³`, no
   `log𝓛` loss. The note's void lemma, read under the unit Haar measure (unit
   `c` ⇒ full multiplier family, exact fibre product over the big primes ℓ),
   is a Haar bound. POINTWISE_HAAR's Janson route gave `𝓛³/log𝓛`. Now
   `𝓛³ ≪ log(1/δ*) ≪ 𝓛³(log𝓛)^5`.
2. **Thm 2.1 (PROVED given the note + Page's theorem).**
   `#{p ≤ x: W(p) > T} ≪ π(x)e^{−c(log T)³}`, uniformly for
   `log T ≤ c₁(log x)^{1/4}`. Goal (b), with no polylog loss. Large `T`: the
   note's integer bound. Small `T` (`(log T)³ ≲ log log x`): the Page expansion
   on primes. Here a possible Siegel zero costs only a factor `1+ε ≤ 3`,
   because the majorant is non-negative on units. This upgrades ledger (A)9
   (CLAIMED/PROVISIONAL, `N`-normalised).
3. **Goal (a), honest answer.** The "Haar-side route" is the note's own
   route: Haar void plus Bonferroni of order ≍ mass at level `t⁴`. It
   reproves the 3/4 bound for primes (in `π(N)` form). It does not improve
   it, and it cannot (KARY3). Cor 3.3: certifying a Haar saving `s` needs
   level `≥ (s/C)^{4/3}`, so certifying the true void costs `≍ 𝓛⁴`.
4. **Thm 4.1 (PROVED; novelty none claimed).** A two-sided order-k sieve
   limit in the one-big-coordinate setting (OMEGA14 Setting 1.2):
   * Majorants: (U−) KARY binomial extrapolation, (U+) Bonferroni.
   * Minorants: (L−) OMEGA14 planting, (L+) Bonferroni.

   Both sides have the same critical *order* `k ≍ P` (mass = dimension). The
   critical level `≍ L·P` is claimed only when the big costs are comparable
   and the small-coordinate cost is booked separately.
5. **Prop 4.2 (PROVED given the note's Cor 4.3 and OMEGA14 Lemma 4.1).**
   The note's atoms block every positive minorant of `F_T` with
   `log D ≤ c(log T)⁴`, on every fibre with `log Q ≤ T^{0.05}`.
   * The note's fibre mass `≍ t³` is uniform in *every* unit `c`, so
     planting applies deterministically.
   * This sharpens OMEGA14 Thm 4.5 (`c𝓛⁴/log𝓛`, modulo (G)+Page+FL).
   * OMEGA13's 1/4 is now optimal in that architecture up to
     `(log log p)^{1/4}` (was `^{1/2}`).
   * The idea came from the self-review.
6. **Thm 4.3 (PROVED as a conjunction of cited results, within their
   scopes).** Both ceilings come from one relation `λ ≍ 𝓛·𝓛³` between level
   and usable cutoff:
   * majorants: the sup-saving `S(λ) ≍ λ^{3/4}`, upper bound for every
     mixture, attained by the note;
   * minorants: the least positive level is `≍ 𝓛⁴` up to one `log𝓛`;
   * the budget `λ ≍ log N` resp. `log x` gives 3/4 resp. 1/4.

   The "product = level" observation is an identity. The `a/(a+1)`,
   `1/(a+1)` extrapolation is CONDITIONAL on the same one-big-prime
   mechanism. The mechanism reading (one-big-prime subfamily, §4.2) is an
   Assessment.
7. **EVIDENCE (§4.4).** An exact rational LP with asserted primal
   certificates, for i.i.d. bits (`n = 40`, `P = 2..8`):
   * the least order with a positive minorant is `2P−1`;
   * the least order with a ≥90% majorant saving is `≈ 2P ± 2`.

## What the parent should check hardest

* **Thm 2.1, Case B:**
  * the Page/Davenport Ch. 20 statement was recalled, not checked against a
    PDF (caveat in the text);
  * the unit-Haar identity for the χ₁-twist (primitivity argument);
  * `ν ≥ 0` on `Ẑ^×`.
* **Prop 1.1:**
  * the conditioning on `n ≡ 1 (24)`;
  * the applicability of note Cor 4.3 to every unit `c` mod `L_K`;
  * the containment `{no event ≤ T} ⊆ {H_X = 0}` (atoms are ℛ(kℓ) classes,
    `kℓ ≤ T`).
* **Thm 4.1 (U−):** check that KARY Thm 2.5/Cor 2.6 apply fibrewise with every
  coordinate light and `M = P` deterministic.
* **Prop 4.2:**
  * uniformity of note Cor 4.3 over *all* unit `c` (the BV step in note
    Thm 4.2 is claimed uniform in `c`, `J`);
  * `f_c(ℓ) ≤ ℓ^{1/3}`;
  * the bookkeeping of big primes dividing `Q`.
* **§4.2 multi-scale reading of KARY3's ledger:** this is labelled
  Assessment, as a description and not a proof.

## Not done / open

* A lower typical-size count `≥ π(x)e^{−C𝓛³polylog}` (Siegel Case A of
  OMEGA9 Thm 1.1 blocks a direct count).
* Nothing beyond either ceiling: the unification says that level-bounded
  (CRT) information cannot beat either one.

## Self-review

A `review` subagent (deep mode) found no FATAL issues. Prop 1.1, Thm 2.1
and the four inequalities of Thm 4.1 passed. It independently replayed the
LP thresholds with exact dual certificates. Three MAJOR overclaims were
repaired:
* the level claim of Thm 4.1 for non-comparable costs;
* Cor 3.3 "certifying the full Haar void";
* the quantifiers of Thm 4.3 (any vs some mixture, good fibre vs every
  fibre, the full system vs a one-big-prime subfamily, and a universal
  impossibility claim).

The minor items were applied: the `k ≥ 1` case, the generalised inverse,
the precise PNT-in-AP input, the "0.55k" wording and the LP certificates.
