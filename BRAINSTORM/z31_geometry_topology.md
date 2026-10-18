# z31 — Geometry of numbers and topology (Minkowski, covering radius, degree/fixed-point and parity arguments) (O261 field memo 12)

Labels as in DISCOVERIES.md. No new sources; builds on SYNTHESIS_SPARKS8 §1.7 (Minkowski/Thue wall), (J)85 Thm 3.1 (covering
needs sub-power windows), ASTRA_BRIDGE Thm 3.4 (E4), BL Lemma 3.1 / LITERATURE_2026 §(ii) "real topology", INVOLUTION_ES(2).

## (a) Counterparts
1. **Minkowski / Thue / Dirichlet pigeonhole:** a lattice of index g in ℤ² has a non-zero point of norm ≪ √g. E4 asks for a
   *specific* point (2k, 1) of L_ρ(g) with k | (g + 1)/4.
2. **Inhomogeneous geometry of numbers (covering radius):** every translate of a convex body K contains a lattice point iff
   K + Λ = ℝⁿ, i.e. the covering radius μ(K, Λ) ≤ 1 (R-O261 repair M8: volume alone does not suffice — long thin bodies
   between lattice rows have large volume and miss Λ).
3. **Topological existence (Brouwer/Borsuk–Ulam/degree):** existence of a zero/fixed point from a non-zero degree or a parity.
   Discrete analogue: Zagier's involution (fixed-point parity) for p = a² + b² (WINDMILL_REDUCTION: the windmill is the
   dihedral symmetry of Conway rivers).

## (b) Pointwise status
All three are pointwise theorems (for every lattice / every prime p ≡ 1 (4)), with power-size or structural input: (1) volume;
(2) a covering-radius bound; (3) an involution on a finite set of odd size.

## (c) Transfer to B2 (each wall already located; recorded here for the dictionary)
* (1): the target is an exact point with Y = 1, not a short vector; Minkowski controls size, not the exact height, and the ES
  class depends on the height (SYNTHESIS_SPARKS8 Prop 1.5: "the barrier hypothesis that ES violates is 'the target class is
  fixed before the point is chosen'") — F3.
* (2): covering needs windows of size p^{O(1/log log p)} ((J)85 Thm 3.1, PROVED there) — far from what a forced window gives.
* (3): the real points U_n(ℝ)^+ form a whole connected component (BL Lemma 3.1) and graph moves jump between real branches,
  so no degree of real paths constrains them (LITERATURE_2026 §(ii)); parity/windmill arguments: T1 kills the odd set on
  square classes, and finite-menu affine involutions are barred conditionally ((J)2, Thm 6.1). A topological existence proof
  would need an involution whose fixed-point set is odd *at primes and even at odd squares* — the parity must see the
  quadratic character (F6) and the size layer at once.

## (d) Verdict: ANALOGUE throughout (exact walls known). **NOT SHARP.**
