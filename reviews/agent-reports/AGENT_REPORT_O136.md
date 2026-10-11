# AGENT REPORT O136 — long shot B: fibred encodings

Branch `side-agent/longshot-fibred`. Deliverable: `LONGSHOT_FIBRED.md`. Scripts: `scripts/lsb_*.py`. Data:
`data/lsb/`. **ES is not proved. Nothing here proves ES(p) for any new p.**

## Outcome
The result is negative, with an exact scope (Thm 5.4). The brief hoped that making each solution correspond to
`≍ H^δ` objects would escape the scale constraint. It does not, for any encoding in class X:
* algebraic recipes on Zariski-dense pieces;
* orbit recipes under lattices whose stabiliser covolumes vary by at most a factor R.

The fibre factor `H^δ` cancels. What remains, `c(n)`, is a weighted solution count (Lemma 1.2, Thm 3.1).

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
     by a research subagent. DRS Thm 1.2 was quoted second-hand.
4. **Catalogue F1–F6 (§4).**
   * F2, the Type II Pell unit, is not power-fibred and its orbit is ES-dead after k = 1. Its regulator weights
     are capped at `O(log p)` because the solution *is* the unit, which closes the "regulator weights" escape for
     this encoding.
   * F4, Type II as `SL₂(ℤ)`-orbits of Gram pairs (Q,S), is the canonical power-fibred encoding. Its stabiliser is
     trivial and `c = κ·F_{c,d}`.
5. **T1 (§5).**
   * Prop 5.1 (PROVED under hypothesis (U)): for mass-formula main terms, T1 can only be passed at the primes dividing m.
   * Such factors exist. For the spinor exceptions of `3x²+4y²+9z²` (Earnest 2022 Prop 5.1, Jones–Pall,
     Schulze-Pillot) the script re-checked all 29 cases to 5·10⁴.
   * The ES-natural T1-passing factor is the genus set `𝔊⁻_d`. It is empty at odd squares and half the classes at
     primes `p ≡ 1 (4)` (PROVED, 5.3). It is **invalid**: `h/2` classes against polylog ES points, and the ES count
     `F_d(p)` was 0 in 19 of 40 tested (prime, level) pairs.
6. **EVIDENCE (§6).**
   * F4 orbit counts are equal across orbits to within 1.5% at H = 3000.
   * At 9, 25 and 49 the genus-full set has 4 orbits (including Q₀) and the ES set is empty.

## What escapes (§5.5, Assessment)
* (E-a) Orbit weights that vary by a power of n and are not capped by the solution. None was found.
* (E-b) A *valid* genus-full criterion with a Brauer–Manin factor at p. This is a theorem of ES strength, and it
  would make counting unnecessary (CTX).
* (E-c) Recipes that are neither algebraic nor orbit-invariant. These fall under POINTWISE_SIZE Thm M.
* Fibring adds nothing to FI/HB parity-breaking: it would only add free parameters, as in F1.

## Points for the referee
* Thm 5.4(3) uses CTX Thm 3.7. Its hypotheses (G simply connected, H connected, non-compactness) are assumed for the
  genus-full alternative. I did not check that they hold for every conceivable V; they hold for the F4/X_d settings
  up to replacing SO by Spin.
* Prop 5.1 needs the uniformity hypothesis (U). It is stated as such and not proved for general families.
* Novelty is modest. Lemma 2.1 and Thm 3.1 are elementary consequences of standard theorems. Their value is the
  exact scope statement that answers RT1 §5.5's "blind spot" (T8, μ ≥ p^η).
