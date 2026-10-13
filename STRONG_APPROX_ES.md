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

## 3. Arithmetic recipes: congruence data mod q cannot see a factorisation

ES in every known chart asks for a *divisor of a p-dependent integer in a residue class whose modulus is part of
the solution* (B2). Example used below (Type II, ET (2.18)/(2.19), proved in CONDITIONAL_ES §1): with
`t = 4c²d`, `tp + 1 = f f'`, `f ≡ f' ≡ −1 (mod 4cd)`. In matrix form (PROVED, direct check of the
determinant): **Type II(p) ⟺ ∃ γ = [[f, M],[cp, f']] ∈ SL₂(ℤ), M = 4cd, with γ₁₁ ≡ γ₂₂ ≡ −1 (mod γ₁₂)**, i.e.
`−γ ∈ Γ^1(M) ∩ Γ₀(p)` with `|γ₁₂| = M` exactly (plus `4(γ₂₁/p) | γ₁₂` and positivity). The congruence modulus is
again the entry γ₁₂ itself: the rank-4 split form `det` is present, but the level is a coordinate.

**Proposition 3.1 (invisibility; PROVED, elementary).** Let `n, q ≥ 1`, `gcd(n, q) = 1`, and `λ ∈ M₂(ℤ/q)`
with `det λ ≡ n (q)`. For every factorisation `n = g g'` there are infinitely many `γ ∈ M₂(ℤ)` with
`det γ = n`, `γ ≡ λ (mod q)`, and first-column content `gcd(γ₁₁, γ₂₁) = g`.
*Proof.* Put `D = diag(g, g')`, invertible mod q. `A₀ := λD^{−1}` has determinant 1 mod q; lift it to
`A ∈ SL₂(ℤ)` (surjectivity of `SL₂(ℤ) → SL₂(ℤ/q)`). For every `δ ∈ Γ(q)`, `γ = AδD` works: `γ ≡ A₀D = λ`,
`det γ = n`, and the first column is g·(first column of Aδ), which is primitive. ∎
*Definite analogue (classical).* For n odd, every primitive Hurwitz quaternion α of norm n factors as `α = βγ`
with `N(β) = g` for **every** `g | n`, uniquely up to units (unique factorisation for primitive Hurwitz
quaternions). So a factorisation is not a *property* that distinguishes points of a norm-n level set at all.

**Corollary 3.2 (what a fixed modulus can and cannot see; PROVED from 3.1).** Let the data be as in Def 2.1 with
`Q_p = det` (or the reduced norm of an Eichler order, by strong approximation for its norm-one group at the
primes ∤ disc). Fix any rule `ψ` that reads off from `x ∈ R_p` a divisor `g(x)` of `N_p` coprime to q_p
(content of a row/column, `gcd(L(x), N_p)` for a linear form L, the norm of the left ideal `Ox + gO`, …).
Then the set `{g(x) : x ≡ λ (q_p)}` is **all** divisors of `N_p` (Prop 3.1, for every class λ). Hence a recipe
that is valid on every point of a congruence class must be valid for every divisor of `N_p`, in particular for
`g = 1` and `g = N_p`: ES is then certified by the trivial factorisation alone, i.e. by congruence data
(B1: POINTWISE_SIZE Thms M, C, F). Divisors sharing primes with q_p *are* seen, but they are divisors of
`gcd(N_p, q_p^∞)`, which is known without any lattice point.

**Principle 3.3 (SA is a local statement; Assessment, with the proved pieces cited).** Every SA theorem has the
form "local solubility in the class ⇒ a point exists". A certificate "SA ⇒ ES(p)" therefore needs a universal
statement *every point of R_p (in some class and box) yields an ES solution*. Thm 2.3 shows such universal
statements are idle when the recipe is rational of bounded degree (they collapse to the finite menu of degenerate
pieces). Prop 3.1 shows they are idle when the recipe reads factorisation data coprime to q_p (all types occur in
every class). Projecting first (`Φ = ψ∘π` with π a coordinate or linear form) does not help: `π(R_p)` is,
up to local conditions, an arithmetic progression (ternary fibres are locally soluble), so the certificate is
the ordinary ES lottery over an AP, and the fibre factor cancels exactly as in LONGSHOT_FIBRED Thm 5.4.
Used as a *count* instead of an existence statement, SA meets the scale constraint: its main term is
`σN/q³ ≥ N^{1/2−o(1)}` in the (S4) range, so the map to solutions must be `p^{η}`-to-one (CONDITIONAL_ES
Prop 2.3), which is exactly the fibre factor that cancels.

## 4. The scale window: even *optimal* strong approximation is a power too large

Let `Q_p` have Gram determinant `D_p`. The Eisenstein (genus) main term for `#{Q_p(x) = N, x ≡ λ (q)}` is
`M = σ·N/(√D_p · q³)` (σ = product of local densities, `N^{−o(1)} ≤ σ ≤ N^{o(1)}` away from anisotropic-prime
blowups); for (S4), D fixed, this is Sardari's `σ (r/m)³ N`.

**Theorem 4.1 (scale window; PROVED relative to CONDITIONAL_ES Prop 2.3, i.e. relative to ET).** Suppose an
SA statement of *range exponent* `1 + η` is available: `R_p ≠ ∅` (indeed `#R_p ≥ M/2`) whenever local conditions
hold and `N ≥ (√D_p q_p³)^{1+η}`. Let an SA-encoding use it with a map `R_p → Sol(p)` of multiplicity
`μ(p) ≤ p^{o(1)}`. Then for all p outside a set of density 0, `√D_p q_p³ ≤ p^{o(1)}` and `N_p ≤ p^{o(1)}`.
*Proof.* In range, `M ≥ σ (√D q³)^{η} ≥ (√D q³)^{η} N^{−o(1)}` and `M ≥ σ N^{η/(1+η)}`. Prop 2.3 gives
`M ≤ 2μ f(p) ≤ p^{o(1)}` off a density-0 set. Both bounds then force `N^{η/(1+η) − o(1)} ≤ p^{o(1)}`. ∎

*Calibration.* (S4) has `1 + η = 2` (`N ≫ q⁶`, D fixed). Sardari's Conjecture 1.3 (exponent 4) has
`1 + η = 4/3`; BKS's covering exponent 4/3 for S³ (conditional on Twisted Linnik) is the same threshold. So
**even the optimal conjectured strong approximation leaves a power main term `M ≥ q^{1−o(1)}`**, and a valid
encoding through it needs `μ ≥ q^{1−o(1)}/f(p)`. The window `η = 0` (expected count p^{o(1)}) is where no SA
statement is true in general: at expected count O(1) the representation numbers of a quaternary form fluctuate
by the cusp-form part, which there is of the same size as the main term.

*The ES-natural quaternary forms live exactly at η = 0.* QUATERNION_ES Lemma 3.1: Type II elements `α = 2ai + j`
of `(−d,−p)` have norm `N = 4a²d + p` for the form `x₀² + dx₁² + px₂² + dpx₃²` (`√D = dp`), so
`N/√D ≍ (4a²d + p)/(dp) = O(a²/p + 1/d)`, i.e. expected count O(1) — below every SA range. The same holds for the
Type I order of reduced discriminant `pe` (Prop 1.3 there). This is the quaternionic form of the scale constraint:
the solution-carrying representations are the ones a representation theorem cannot see.

**Corollary 4.2 (PROVED, combining 2.3, 3.1, 4.1).** A rank-4 SA certificate of ES(p) for almost all p must have
multiplicity `μ(p) ≥ p^{η'}`, and its recipe must be neither rational of bounded degree (Thm 2.3) nor a function
of factorisation data coprime to `q_p` (Prop 3.1/Cor 3.2), nor factor through a linear projection (Principle 3.3,
fibre cancellation). *Scope:* Prop 2.3 needs nothing about the recipe; 2.3/3.1 are as stated there. Not covered:
recipes of p-growing algebraic degree, and non-algebraic non-factorisation recipes (lattice reduction of an
x-dependent lattice, continued fractions of ratios of coordinates, …), which are `POINTWISE_SIZE` Thm M's
"arbitrary search" territory.
