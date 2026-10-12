# AGENT REPORT O149 — brainstorm: p-adic / adelic / tropical / Newton-polygon angles

ES is not solved; no memo is LIVE. Branch `side-agent/bs-padic-tropical`. The memos are in `BRAINSTORM/`;
the scripts are `scripts/bs_padic_{counts,classbias,valpatterns}.py` (tiny, run in seconds to minutes).

**(a) `padic_adelic_scaling.md`: COLLAPSES to B1 (local data) and B2/B6 (global data).**
* *Strongest reason.* Prop A, the scaling lemma (PROVED): 𝒰_n ⊗ ℤ_ℓ ≅ 𝒰_{ℓ^{v_ℓ(n)}} ⊗ ℤ_ℓ, and the positive real
  locus is n-independent up to scaling. So every local invariant of U_p (densities, Igusa data, Berkovich spaces,
  tropicalisations) is independent of p mod q for q ≠ p.
* *Evidence against local main terms.* The actual counts vary strongly by class (EVIDENCE, all 470 primes in
  [3000, 7000]): mean f/log³p is 0.088 for p ≡ 1 (8) against 0.291 for p ≡ 7 (8), and 0.046 on the square
  classes mod 840 against 0.173 elsewhere. So any adelic-volume main term misses even the class means. The
  class signal enters only through global objects (the ℚ-structure, and BL's α through Hilbert reciprocity).
* Prop B (PROVED): ℓ-adic or ℤ̂ interpolation of f_I or f_II at odd squares can only force *divisibility* on
  the hard classes, never positivity.
* Prop C (PROVED, folklore in substance): ES ⟺ every prime is the exact denominator of a positive rational point
  of the fixed surface Σ1/X = 4. This is an M-point problem in Moerman's sense (arXiv:2407.03048, abstract
  verified), but every known theorem there is an average count.

**(b) `tropical_newton.md`: COLLAPSES to B1/B2.**
* *Strongest reason.* The adelic tropicalisation is injective on positive rationals. A tropical certificate is
  therefore a factorisation pattern, i.e. a slice, and whether it lifts is the slice divisor event. Newton
  polygons see valuations, never the residue classes of cofactors. In the amoeba limit the integral lattice
  becomes infinitely fine.
* By-product (PROVED, elementary, probably folklore; checked on 3756 solutions, p < 600): for prime p the p-adic
  patterns are exactly (0,0,1) (Type I) and (0,1,1) (Type II). Pole order ≥ 2 at p is excluded by the
  archimedean place alone. At every ℓ ≠ p, the maximal ℓ-adic valuation among the denominators is attained at
  least twice.

**(c) `padic_functionfield_igusa.md`: COLLAPSES.**
* Igusa and Berkovich data are local, hence p-mod-q-blind by Prop A (B1). Tilting changes only the place p,
  where everything is already locally solvable.
* The 𝔽_q[T] analogue is ill-posed as stated. A unit numerator makes it trivial, so it needs a square numerator
  M = Q² of positive degree. "Monic" does not forbid cancellation at ∞.
* In the large-q regime (degree fixed), pointwise truth becomes "the bad Frobenius set C in a fixed monodromy
  group is empty", a finite group covering. That is the function-field image of the polynomial-covering route
  excluded by Theorem C / redteam-2 Thm 2.2(iii).
* UNCLEAR side question, not an ES route: is C = ∅ for M = T² and small degree? A small brute force over
  𝔽_q[T] would decide it.

**Overall.** All three angles fail at their first step: local or valuation data cannot see what decides ES,
which is global. No angle survives the barrier screens. The reusable by-products are Prop A (with the
class-bias table), Prop B, and the exact p-adic pattern lemma.
