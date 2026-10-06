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

   Both thresholds are at the same critical order `k ≍ P` (mass = dimension),
   so the critical level is `λ* ≍ L·P`.
5. **Thm 4.2 (PROVED as a conjunction of cited results, within their
   scopes).** Both ES ceilings are this statement at the same scale, with
   the same mass `P ≍ 𝓛³` and one big prime per event:
   * The note/KARY3 and OMEGA13/14 instances are matched in the table of §4.2.
   * The exceptional ceiling is `κ(𝓛_c(λ)) ≍ λ^{3/4}` and the pointwise
     ceiling is `𝓛_c(λ) ≍ λ^{1/4}`, where `λ*(𝓛_c) = λ`.
   * Their product is `λ`. With Haar exponent `a` the exponents are
     `a/(a+1)` and `1/(a+1)`.
   * Remark 4.3: the two duals are a comparison measure on the avoiders and a
     planted measure on the hit set.
6. **EVIDENCE (§4.4).** An exact rational LP for i.i.d. bits (`n = 40`,
   `P = 2..8`):
   * the least order with a positive minorant is `2P−1`;
   * the least order with a ≥90% majorant saving is `≈ 2P ± 2`.

   So the threshold is common to both sides. Below it the majorant degrades
   gracefully (about `0.55k`), while the minorant is identically useless.

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
* **§4.2 multi-scale reading of KARY3's ledger:** this is labelled
  Assessment, as a description and not a proof.

## Not done / open

* A lower typical-size count `≥ π(x)e^{−C𝓛³polylog}` (Siegel Case A of
  OMEGA9 Thm 1.1 blocks a direct count).
* Nothing beyond either ceiling: the unification says that level-bounded
  (CRT) information cannot beat either one.
