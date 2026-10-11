# AGENT REPORT O136 — long shot B: fibred encodings

Branch `side-agent/longshot-fibred`. Deliverable: `LONGSHOT_FIBRED.md`. Scripts: `scripts/lsb_*.py`. Data:
`data/lsb/`. **ES is not proved. Nothing here proves ES(p) for any new p.**

## Outcome
The result is negative, with an exact scope (Thm 5.4). The brief hoped that making each solution correspond to
`≍ H^δ` objects would escape the scale constraint. It does not, for any encoding in class X:
* algebraic recipes on Zariski-dense pieces;
* orbit recipes under lattices whose stabiliser covolumes vary by at most a factor R.

The fibre factor `H^δ` cancels. What remains, `c(n)`, is a weighted solution count (Lemma 1.2, Thm 3.1).
*(R136 repair, D1)* The bound is `M ≤ 2Rμf`, with μ (pieces per solution) and R (weight spread) unrestricted in
class X. So fibring alone buys nothing, but the red team's T8 blind spot (μ or R ≥ p^η) is **not** closed. It moves
from fibre size to the number of pieces per solution.

*(R136 repair)* Hostile review: `reviews/longshot-fibred-review.md`. There are two MAJOR defects. D1 is the scope
overclaim, and D2 is a hidden hypothesis in Thm 2.3(c): φ_i must map into the ES variety. Thm 5.4 item 3 and (E-b)
are relabelled CONDITIONAL, because the CTX hypotheses fail for F5 (D14). Minor fixes D3–D13 are applied in
`LONGSHOT_FIBRED.md`, marked "(R136 repair)".

## Main items (labels as in the file)
1. **Rigidity (Lemma 2.1, PROVED).** A rational recipe is constant on any Zariski-dense set of points.
   * Lattice orbits are Zariski-dense (Borel density; Lemma 2.2).
   * So for algebraic recipes the counting is idle: the solution is written into the equations (Thm 2.3).
   * With ℤ-polynomial recipes, local solubility alone already forces a solution (Thm 2.3(c)).
2. **Cor 2.4 (PROVED rel. ET Prop 1.6 + Dirichlet).** Uniform algebraic encodings of bounded complexity miss all
   large `p ≡ 1 (mod D')`, whatever their fibre sizes. The proof is self-contained (polynomiality of the section,
   then transport to an odd square). It is known in substance (Mordell–Schinzel; POINTWISE_SIZE Thm C instances).
3. **Thm 3.1 (PROVED rel. counting input (C)).** For orbit recipes, `c(n) = Σ_orbits w_O`, where `w_O` is the
   stabiliser covolume. With compact or finite stabilisers the scale constraint returns, with multiplicity `C·μ`.
   * The statements of EM Thm 1.4, EMS Thm 1.16, BR Thm 0.6 and CTX Thm 3.7 were checked against the primary texts
     **only by the author's research subagent**. DRS Thm 1.2 was quoted second-hand. *(R136 repair)* The hostile
     reviewer could not access any of these texts, so they are not independently verified.
4. **Catalogue F1–F6 (§4).**
   * F2, the Type II Pell unit, is not power-fibred and its orbit is ES-dead after k = 1. Its regulator weights
     are capped at `O(log p)` because the solution *is* the unit, which closes the "regulator weights" escape for
     this encoding. (R136 re-checked F2 for all Type II quadruples of p < 1500.)
   * F4, Type II as `SL₂(ℤ)`-orbits of Gram pairs (Q,S), is the canonical power-fibred encoding. Its stabiliser is
     trivial and `c = κ·F_{c,d}`. Fibres grow like `≍ H`, not `H²` (R136 repair, D10).
5. **T1 (§5).**
   * Prop 5.1 (PROVED under hypothesis (U)): for mass-formula main terms, T1 can only be passed at the primes dividing m.
   * Such factors exist. For the spinor exceptions of `3x²+4y²+9z²` (Earnest 2022 Prop 5.1, Jones–Pall,
     Schulze-Pillot) the script re-checked all 29 cases to 5·10⁴.
   * The ES-natural T1-passing factor is the genus set `𝔊⁻_d`. It is empty at odd squares and half the classes at
     primes `p ≡ 1 (4)` (PROVED, 5.3). It is **invalid**: `h/2` classes against polylog ES points, and the ES count
     `F_d(p)` was 0 in 19 of 40 tested (prime, level) pairs. *(R136 repair, D6)* The test primes lie in the hard
     square classes mod 120. The per-level criterion is refuted, while the aggregate criterion is vacuous (it is ES
     for p ≡ 1 (4)), not false. R136 reproduced all numbers.
6. **EVIDENCE (§6).**
   * F4 orbit counts are equal across orbits to within 1.5% at H = 3000.
   * At 9, 25 and 49 the genus-full set has 4 orbits (including Q₀) and the ES set is empty.

## What escapes (§5.5, Assessment)
* (E-a) Orbit weights that vary by a power of n and are not capped by the solution. None was found.
* (E-b) A *valid* genus-full criterion with a Brauer–Manin factor at p. This is a theorem of ES strength, and it
  would make counting unnecessary (CTX).
* (E-c) Recipes that are neither algebraic nor orbit-invariant. These fall under POINTWISE_SIZE Thm M.
* (E-d) *(R136 repair, D1)* Class-X encodings with `μ ≥ n^η` pieces per solution. Thm 5.4 is vacuous for them, and
  this is the open T8 blind spot.
* Fibring adds nothing to FI/HB parity-breaking: it would only add free parameters, as in F1.

## Points for the referee
* Thm 5.4(3) uses CTX Thm 3.7. *(R136 repair, D14)* It is CONDITIONAL: for F5's pair space the hypotheses fail
  (`G = SL₂` gives stabiliser `μ₂`, not connected; `G = SO ≅ PGL₂` is not simply connected). Its hypotheses (G simply connected, H connected, non-compactness) are assumed for the
  genus-full alternative. I did not check that they hold for every conceivable V; they hold for the F4/X_d settings
  up to replacing SO by Spin.
* Prop 5.1 needs the uniformity hypothesis (U). It is stated as such and not proved for general families.
* Novelty is modest. Lemma 2.1 and Thm 3.1 are elementary consequences of standard theorems. Their value is the
  exact scope statement. *(R136 repair, D1)* It shows that continuous (`H^δ`) fibring does not reach RT1 §5.5's
  blind spot (T8, μ ≥ p^η). The blind spot itself remains open.
