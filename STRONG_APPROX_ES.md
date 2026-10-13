# STRONG_APPROX_ES — rank-4 quadratic encodings of ES with a fixed modulus (task O167, SPARK)

**ES is not solved, here or anywhere. Nothing below proves ES(p) for any new p.**
Labels as in DISCOVERIES.md. Work in progress; sections are added one at a time.

## 1. Inputs (literature, as verified by a research subagent; statements only)

* (S4) Sardari, *Optimal strong approximation for quadratic forms*, Duke 168 (2019), arXiv:1510.00462,
  Thm 1.2/1.6. Fixed nondegenerate integral F in k variables. If the congruence-restricted local
  conditions hold, `F(x) = N`, `x ≡ λ (mod m)` (with `x/√N` in a real ball of radius r) is solvable for
  `N ≫_{F,ε} (m/r)^{4+ε}` when k ≥ 5 (optimal), and `N ≫ (m/r)^{6+ε}`, N odd, when **k = 4**.
  Exponent 4 for k = 4 is Sardari's Conjecture 1.3 (open). Count: main term
  `≍ σ_loc·(r/m)^{k−1} N^{(k−2)/2}`; for k = 4 the relative error is `O(((r/m)³√N)^{−1/2} N^ε)`.
  Constants depend on F: **no uniformity in disc F** is claimed.
* (BKS) Browning–Kumaraswamy–Steiner (Duke 2019, arXiv:1609.06097): covering exponent 4/3 for S³
  under their Twisted Linnik conjecture (CONDITIONAL; S³ = sums of four squares).
* (LPS) Lubotzky–Phillips–Sarnak: paths in X^{ℓ,q} ↔ products of norm-ℓ quaternions mod q;
  diameter ≤ 2 log_ℓ|G| + O(1) (exact constant not re-verified); Sardari arXiv:1511.09340: diameter
  ≥ (4/3) log_ℓ|G| + O(1) for an infinite family.
* (DSP) Duke–Schulze-Pillot (ternary): ineffective, fixed form, spinor exceptions; no growing-q version
  verified.

**Consequence for this task.** The only *unconditional* pointwise theorem with an explicit congruence range
in rank 4 is (S4), for a form F **independent of p**, at `N ≫ m^{6+ε}`, with main term
`≍ N/m³ ≥ N^{1/2}` there. A form `Q_p` whose discriminant grows with p needs a disc-uniform version,
which was not found (the classical theorems are for fixed forms). Below, "(SA_C)" denotes the
hypothetical statement with exponent C, uniform in whatever the encoding needs; C = 6 is (S4).

## 2. Setting, and the first obstruction: rational recipes make SA idle

**Definition 2.1 (SA-encoding).** For each large prime p fix: a nondegenerate integral quaternary form `Q_p`,
an integer `N_p ≠ 0`, a modulus `q_p ≥ 1`, a class `λ_p ∈ (ℤ/q_p)⁴`, and a box radius `B_p`. Put
`V_p = {x ∈ ℂ⁴ : Q_p(x) = N_p}` and `R_p = {x ∈ ℤ⁴ ∩ V_p : x ≡ λ_p (q_p), |x|_∞ ≤ B_p}`. A *recipe* of
complexity `(J, D)` is a partition `R_p = R_p^{(1)} ⊔ … ⊔ R_p^{(J)}` (arbitrary side conditions) and rational
maps `φ_{j,p} ∈ ℂ(x)³` of degree ≤ D (numerators, denominators), regular on `R_p^{(j)}`, with
`φ_{j,p}(R_p^{(j)}) ⊆ Sol(p)`. Coefficients may depend on p arbitrarily. Piece j is *degenerate at p* if
`φ_{j,p}` is constant on V_p. An *SA input* is a lower bound `#R_p ≥ M_p > 0`; the model case is (S4):
`M_p ≍ σ_p (B_p/q_p)²·(B_p²/N_p)` with `B_p ≍ √N_p`, i.e. `M_p ≍ σ_p N_p/q_p³`, valid for `N_p ≫ q_p^{6+ε}`.

**Lemma 2.2 (geometry; PROVED, elementary).** V_p is irreducible and contains no affine plane.
*Proof.* Its projective closure `{Q_p(x) = N_p x₀²} ⊂ ℙ⁴` is a quadric of rank 5, hence smooth and irreducible.
A smooth quadric of dimension 3 contains no plane (maximal linear subspaces of a smooth quadric of dimension
r have dimension ⌊r/2⌋ = 1). The closure of an affine plane in V_p would be such a plane. ∎

**Theorem 2.3 (nondegenerate pieces are thin; PROVED relative to Pila, Astérisque 228 (1995) Thm A).**
Pila: an irreducible affine variety of dimension n and degree d in 𝔸^N has `≤ c(n,d,N,ε) H^{n−1+1/d+ε}`
integral points of height ≤ H (uniform in the variety; statement checked in the source).
Then, with `H_p := 1 + 2B_p/q_p`,
`#{x ∈ R_p in nondegenerate pieces} ≤ C(J, D, ε)·f(p)·H_p^{3/2+ε}`.

*Proof.* Fix a nondegenerate j and `s ∈ Sol(p)`. `F_s = {x ∈ V_p : φ_{j,p}(x) = s}` (clear denominators, add
the points where a denominator vanishes; they are not in the domain) is a proper closed subset of the
irreducible 3-fold V_p, cut out by polynomials of degree ≤ max(D,2). By Bézout it has ≤ C(D) irreducible
components, each of dimension ≤ 2 and degree ≤ C(D). Substitute `x = λ̃ + q_p y` (λ̃ a fixed lift,
|λ̃| < q_p): the integral points of `R_p ∩ F_s` become integral points y of height ≤ H_p on the images
Y' of the components Y (same dimension and degree). A component not stable under complex conjugation has its
real points in `Y' ∩ Ȳ'`, of lower dimension; so assume Y' real. Dimension 2: Y' is not a plane (Lemma 2.2),
so `d ≥ 2` and Pila gives `≪ H_p^{3/2+ε}`. Dimension 1: `≪ H_p` (lines) ≤ `H_p^{3/2}`. Dimension 0: ≤ C(D).
Sum over components, over the ≤ f(p) values s, and over j ≤ J. ∎

**Corollary 2.4 (SA is idle for rational recipes; PROVED relative to Pila and the SA input).** If
`M_p > 2C(J,D,ε) f(p) H_p^{3/2+ε}`, then at least half of R_p lies in degenerate pieces; in particular some
degenerate piece is nonempty and its constant value `s_j(p)` is an ES solution. In the (S4) model
(`B_p ≍ √N_p`, `M_p ≍ σ_p N_p/q_p³`, `H_p ≍ √N_p/q_p`) the hypothesis reads
`σ_p (√N_p/q_p)^{1/2−ε} ≫ f(p)`; in the (S4) range `N_p ≥ q_p^{6+ε}` one has `√N_p/q_p ≥ N_p^{1/3}`, so it
holds as soon as `N_p^{1/6−ε} ≫ f(p)/σ_p`. With `σ_p ≥ N_p^{−o(1)}` (local densities of a quaternary form at
a locally represented integer are `≫ N^{−ε}` away from anisotropic-prime blowups) and Lemma 2.1 of
CONDITIONAL_ES (`f(p) ≤ p^{δ}` outside `O(N^{1−δ}log³N)` primes), it holds whenever `N_p ≥ p^{7δ}`, for all p
outside that sparse set.

*Reading.* Every certificate of this shape reduces to a **finite menu** `{s_j(p) : j ≤ J}` of candidate
solutions that do not depend on the lattice point at all; SA only certifies that some degenerate piece is
nonempty, i.e. it contributes a local (congruence) fact. If the recipe is uniform in p (coefficients of `φ_j`
rational functions of p, and degeneracy holding for all large p in a congruence class), then `s_j(p) ∈ ℚ(p)³`
and "s_j(p) ∈ Sol(p)" is a polynomial identity on a residue class: Mordell–Schinzel, which misses every
square class (POINTWISE_TERNARY Lemma 3.1/Cor 3.2; ET Prop 1.6). If `N_p < p^{7δ}` then all data
`(N_p, q_p, λ_p, B_p)` are `p^{o(1)}`-bounded and the recipe is a bounded-slice search (B2, POINTWISE_SIZE Thm C).
*Scope.* Bounded degree D and piece count J (uniform in p); arbitrary p-dependence of `Q_p, N_p, q_p, λ_p`
and of the side conditions; definite or indefinite. This is the rank-4, explicit-SA analogue of
POINTWISE_TERNARY Thm 4.1 (which was rank 3, fixed Q). **Not covered:** recipes that are not piecewise rational
of bounded degree — gcd/valuation/factorisation recipes ("arithmetic recipes"), lattice-reduction recipes,
and recipes of degree growing with p. These are the only escape, and §3 hunts there.
