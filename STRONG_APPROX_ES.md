# STRONG_APPROX_ES — rank-4 quadratic encodings of ES with a fixed modulus (task O167, SPARK)

**ES is not solved, here or anywhere. Nothing below proves ES(p) for any new p.**
Labels as in DISCOVERIES.md.

## 0. Summary (checkpoint 1)

**Outcome so far: negative, with exact scope; no construction survives. ES is not proved.**
* §1: the only unconditional rank-4 SA with a congruence range is Sardari's `N ≫ q^{6+ε}` for a *fixed* form
  (main term `≍ N/q³ ≥ N^{1/2}`); exponent 4 (≙ BKS covering 4/3) is conjectural.
* Thm 2.3 (PROVED rel. Pila Thm A): for recipes that are piecewise rational of bounded degree, the
  non-degenerate pieces carry `≪ f(p) (√N/q)^{3/2+ε}` points, so SA certifies ES only through a finite menu of
  constant pieces (Mordell–Schinzel / B2). Any p-dependence of `Q_p, N_p, q_p` is allowed.
* Prop 3.1 (PROVED): congruence data mod q cannot see any factorisation of N coprime to q — every
  factorisation type occurs in every class. Factorisation recipes are idle.
* Thm 4.1 (PROVED rel. ET): bounded multiplicity forces all data to be `p^{o(1)}` in any SA range with
  exponent `1+η`; even the optimal conjectured exponent leaves `M ≥ q^{1−o(1)}`. The ES-natural quaternary
  representations (QUATERNION_ES) have expected count O(1), i.e. η = 0.
* §5 T1: for fixed data, local conditions at m² and at primes `p ≡ m²` coincide; the map fails at m²
  (EVIDENCE: det-form Type II control to n ≤ 6000).
* §6: six construction attempts (C1–C6) with the barrier hypothesis each tried to violate; §7: the rank-4
  (weight-2 Eisenstein) dictionary for Type II and why fibre weights do not escape; §8 escape table.

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
`σ_p N_p^{1/4−ε} q_p^{−3/2} ≫ f(p)` (since `M/H^{3/2+ε} ≍ σ H^{1/2−ε}/q`). In the (S4) range
`N_p ≥ q_p^{6+ε₀}` (ε₀ > 0 Sardari's fixed loss) one has `q^{3/2} ≤ N^{1/4−κ}`, `κ = ε₀/(24+4ε₀)`, so it holds as
soon as `σ_p N_p^{κ−ε} ≫ f(p)`. *(Self-check repair: a first draft used `N/q²` for M and claimed exponent
1/6; exactly at the boundary `N = q⁶` the two sides are of the same order `q³`, so the margin is only the
fixed ε₀ of the range.)* With `σ_p ≥ N_p^{−o(1)}` (local densities of a quaternary form at a locally
represented integer are `≫ N^{−ε}` away from anisotropic-prime blowups; not re-proved here) and Lemma 2.1 of
CONDITIONAL_ES (`f(p) ≤ p^{δ}` outside `O(N^{1−δ}log³N)` primes), it holds whenever `N_p ≥ p^{2δ/κ}`, for all p
outside that sparse set. **Gap:** an encoding using a *better* range (e.g. Sardari's conjectural `N ≫ q^{4+ε}`)
near its boundary, `q⁴ ≤ N ≤ q⁶ f(p)⁴`, is not covered: there Pila's `H^{3/2}` per fibre is too weak.

*Reading.* Every certificate of this shape reduces to a **finite menu** `{s_j(p) : j ≤ J}` of candidate
solutions that do not depend on the lattice point at all; SA only certifies that some degenerate piece is
nonempty, i.e. it contributes a local (congruence) fact. If the recipe is uniform in p (coefficients of `φ_j`
rational functions of p, and degeneracy holding for all large p in a congruence class), then `s_j(p) ∈ ℚ(p)³`
and "s_j(p) ∈ Sol(p)" is a polynomial identity on a residue class: Mordell–Schinzel, which misses every
square class (POINTWISE_TERNARY Lemma 3.1/Cor 3.2; ET Prop 1.6). If `N_p < p^{2δ/κ}` then all data
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

## 5. The T1 test (odd squares)

**Proposition 5.1 (T1 for fixed data; PROVED relative to the SA input and ET Prop 1.6).** Let `Q, q, λ` be fixed
and `N_n = κn + η`. Local solubility of `Q(x) = N_n, x ≡ λ (q)` at primes `ℓ ∤ 2q·disc Q` is automatic (rank 4,
ℓ-unimodular), and at the finitely many `ℓ | 2q·disc Q` it depends only on `n mod L` for a fixed L (away from
the finitely many n with large `v_ℓ(N_n)` at anisotropic ℓ). So for every odd `m` and every prime `p ≡ m² (L)`
the local conditions at `n = m²` and `n = p` coincide, and SA produces points of `R_{m²}` as soon as it produces
points of `R_p`. Any recipe whose validity proof uses p only through `p mod L` would therefore give a Type I/II
solution of `4/m²`, which does not exist (ET Prop 1.6). *Which step fails at m²:* the **map** — the validity
of Φ must use primality of p; the local conditions and the range do not fail. With Thm 2.3, a bounded rational
recipe is valid only via identities on classes mod L, hence certifies no prime in a square class mod L.

For p-dependent data (`q_p = p`, `p | disc Q_p`, …) the local conditions can differ at n = p and n = m²
only at the place p itself or at the primes `ℓ | m`, by LONGSHOT_FIBRED Prop 5.1 (proved there for
mass-formula main terms under its uniformity hypothesis (U)).

**EVIDENCE / control (`scripts/sa_typeII_matrix.py 6000`, ~10 min).** For every odd n ≤ 6000 that is a prime
or a square, all γ = [[f, 4cd],[cn, f']] ∈ SL₂(ℤ) with `f ≡ f' ≡ −1 (mod 4cd)` were enumerated; det γ = 1
and `4/n = 1/(abd) + 1/(acdn) + 1/(bcdn)` were checked in exact rationals for each. Every prime 5 ≤ p ≤ 6000
has such a γ; no odd square has one (the matrix form of ET Prop 1.6). The split quaternary form `det` with
`γ ∈ Γ₀(n)` satisfies all local conditions at `n = m²`; what fails is the self-referential congruence
`γ₁₁ ≡ −1 (mod γ₁₂)`.

## 6. Construction attempts (iteration log; each entry names the barrier hypothesis it tried to violate)

* **C1 — det-form Type II, fix the modulus by a universal level.** Encoding §3: `γ ∈ SL₂(ℤ) ∩ Γ₀(p)`,
  `γ₁₁ ≡ −1 (mod γ₁₂)`. Variable modulus = γ₁₂. *Iteration:* impose `γ ≡ λ (mod q_p)` with `q_p = lcm(1..L)` and
  `λ₁₁ ≡ −1`, hoping to make `γ₁₁ ≡ −1 (mod γ₁₂)` automatic whenever `γ₁₂ | q_p`. But `γ₁₂ | q_p` is not a
  congruence condition on γ: one must fix `γ₁₂ = M` exactly, which is a two-coordinate slice → B2 divisor-class
  form `f | 4c²dp + 1, f ≡ −1 (M)`, fixed finite menu of M → POINTWISE_SIZE Thm C (fails i.o. under H).
  Also `γ₁₁ ≡ γ₂₂ ≡ −1 (mod q_p)` forces `f, f' ≥ q_p − 1`, while `min(f, f') ≤ √(4c²dp+1)`: so
  `q_p ≤ 2c√(dp) + 2`. Dead (B2).
* **C2 — quaternion lines → full lattices.** QUATERNION_ES Lemma 3.1 puts Type II on the lines `2xi ± j` of
  `(−d,−p)` (a rank-2 object). Replacing the lines by the whole order makes it rank 4, but the ES content
  (`N(α) ≡ p (4d)`, the coupling `αβ ∈ e(1 + 2ℤk)`) lives on the lines; a general factorisation of
  `e(1 + 2ck)` carries no congruence on `N(α)`. And the window: these norms are at expected count O(1)
  (§4). Dead (scale window, η = 0).
* **C3 — Hurwitz/Eichler factorisation recipe** (`x ↦` the left ideal of norm g containing x, `g | N_p`):
  violates "algebraic recipe" (it is arithmetic), so Thm 2.3 does not apply; but all factorisation types occur
  in every class mod q (Prop 3.1). Dead (invisibility).
* **C4 — projection recipe** `Φ = ψ(x₁)`, ψ arithmetic: fibres `{x₁ = c}` have `≍ √N/q²` points (power
  multiplicity, the brief's escape route); but `π(R_p)` is an AP up to local conditions, so the certificate is
  the lottery over an AP and the fibre factor cancels (LONGSHOT_FIBRED Thm 5.4). Dead (B6/fibred).
* **C5 — Thue/Minkowski (non-algebraic, deterministic).** Type II with d fixed: find `(a,b) ≡ (r,−r) (e)` with
  `p < 4abd < p + 2e` (then `4abd − p = e` is forced). The region is a thin *hyperbolic* strip (not convex),
  expected lattice count `≍ log p/(de)`: no Minkowski body. Convexifying (allowing `|4abd − p| < 2e`) admits
  `e ↦ −e`, i.e. signed solutions; equivalently a divisor `≡ ±1 (mod 4c)` of `4c²p + 1`, where `+1` is the
  trivial divisor. Dead → H-B (sign/parity), as LONGSHOT_PIGEONHOLE.
* **C6 — LPS with p as the generator norm.** Paths of length k in the `(p+1)`-tree mod q ↔ norm-`p^k`
  elements mod q; covering at `k ≈ (4/3…2)·log_p|G|`. In the split model these are det-`p^k` matrices; Type II
  is det-p `[[e, 2a],[2ad, f]]` with `2a | 2ad`, `f ≡ −1 (mod 4ad)` — the variable modulus again. In the ES
  quaternion algebras `(−d,−p)`, `B_{p,∞}` the prime p is *ramified*, so there is no p-adic tree at all.
  Dead (B2 + wrong place).

## 7. Weighting by the fibre: the weight-2 (rank-4) dictionary

**Proposition 7.1 (PROVED, classical orthogonality).** For `(r, g) = 1` put
`σ(n; r, g) := Σ_{m | n, m ≡ r (g)} m = φ(g)^{−1} Σ_{χ (g)} χ̄(r) σ_χ(n)`, `σ_χ(n) := Σ_{m|n} χ(m) m`.
The `σ_χ(n)` are Fourier coefficients of weight-2 Eisenstein series (`E₂^{χ,1}`-type; up to normalisation and
the χ ↔ χ̄ convention, which we did not recheck), i.e. exactly the objects that the Siegel–Weil formula
attaches to genera of *quaternary* forms of level ≍ g². Since `σ(n; r, g) > 0 ⟺ n` has a divisor `≡ r (g)`,
Type II (CONDITIONAL_ES (3.1), with `n_g = gp + 1`, `4 | m`, `m ≡ −1 (g)`) is a positivity statement for rank-4
genus coefficients — the rank-4 counterpart of the weight-1 (binary-form) expansion (3.2) used there.

**Corollary 7.2 (weighting does not escape; PROVED).** In `σ(n; r, g)` the divisor m carries weight m, a
power-varying weight (LONGSHOT_FIBRED §5.5 (E-a)). But it is capped by the solution: every term is `≤ n`,
while the main term is `σ(n)/φ(g) ≍ n/φ(g)` up to `n^{o(1)}`. The normalised main term is `≤ n^{o(1)}/φ(g)`,
so FIBRED Lemma 1.3 (`M/w_max ≤ 2f`) returns the polylog scale. Equivalently: the weighted sum is
`n·Σ_{m' | n, n/m' ≡ r (g)} 1/m'`, dominated by the *small* cofactors m', and the `m' = 1` term is the
congruence `n ≡ r (g)` (B1). The rank-4 reading thus re-expresses the lottery on the small cofactor.

## 8. Escape analysis: which hypothesis would have to fail

| barrier used here | hypothesis | what violating it requires |
|---|---|---|
| Thm 2.3 (rational recipes idle) | recipe piecewise rational, degree ≤ D uniformly | recipes of degree growing with p, or non-algebraic |
| Prop 3.1 (invisibility) | recipe reads factorisation data coprime to q_p | `q_p` sharing the *unknown* divisor — impossible for fixed q_p (only `gcd(N_p, q_p^∞)`, known, is seen) |
| Thm 4.1 (scale window) | SA range exponent `1+η`, η > 0 | an SA statement at expected count `p^{o(1)}` (η = 0): ES-strength, not a known or conjectured SA |
| Principle 3.3 / C4 | Φ factors through a projection whose image is an AP | an image that is *not* congruence-describable — then SA is not what supplies it |
| Cor 7.2 | weights capped by the solution | uncapped weights (FIBRED (E-a)); none found |

**Assessment.** The task's premise — power-size counts are not divisor-in-class lotteries — is right about the
counts, but in every encoding found the *map back* to ES solutions turns the power-size count into either a
finite menu (Thm 2.3), a factorisation-blind statement (Prop 3.1), or an AP lottery (C4/Cor 7.2). The quaternary
objects that do carry ES solutions sit at expected count O(1) (§4), exactly where SA says nothing.

# Part II (checkpoint 2): sparks — exact identities, double cosets, uncapped weights

## 9. Exact positive identities (H-E): finite Eisenstein combinations are killed by T1

Let `E(n) = Σ_i c_i σ_{k_i}(n; χ_i, ψ_i)`, `σ_k(n; χ, ψ) := Σ_{d | n} χ(d) ψ(n/d) d^k`, a finite combination
(k_i ≥ 0 integers, χ_i, ψ_i Dirichlet characters of conductor dividing L, c_i ∈ ℂ). This contains every
Eisenstein part of every integral-weight theta series, in particular all rank-4 one-class genera (Siegel–Weil),
and Jacobi's `r₄(n) = 8σ(n)` (n odd). Old-form shifts `σ(n/δ)` (δ > 1) vanish at large primes and at `ℓ²`
(ℓ ∤ δ), so they change nothing below.

**Theorem 9.1 (T1 kills finite Eisenstein identities; PROVED, elementary).**
(a) If `E(ℓ²) = 0` for infinitely many primes `ℓ ≡ 1 (mod L)`, then `E(p) = 0` for every prime `p ≡ 1 (mod L)`.
(b) If `E(ℓ²) ≤ 0` for all large primes `ℓ ≡ 1 (mod L)` (E real), then `E(p) ≤ 0` for all large primes
`p ≡ 1 (mod L)`.
*Proof.* For primes ℓ, p ≡ 1 (L) all character values are 1, so with `C_k := Σ_{i: k_i = k} c_i`:
`E(ℓ²) = P(ℓ) := Σ_k C_k(1 + ℓ^k + ℓ^{2k})` and `E(p) = Σ_k C_k(1 + p^k)`. Let K be the largest k with
`C_k ≠ 0`. If K ≥ 1, the monomial `x^{2K}` of P comes only from k = K (a term `x^{k'}` with k' = 2K would need
`C_{2K} ≠ 0`), so P has leading coefficient `C_K`. (a) P vanishes at infinitely many points, so `P ≡ 0`, so
`C_K = 0`, contradiction; hence K = 0 or no K, and then `P = 3C_0 ≡ 0` forces `C_0 = 0`; so `E(p) = 0`.
(b) `P(ℓ) ≤ 0` for large ℓ forces `C_K < 0` if K ≥ 1, and then `E(p) = C_K p^K + O(p^{K−1}) < 0`; if K = 0 then
`3C_0 ≤ 0`, so `E(p) = 2C_0 ≤ 0`. ∎

**Corollary 9.2.** Let `W(n) ≥ 0` be *any* weighted count of Type I/II certificates (so `W(m²) = 0` for odd m,
ET Prop 1.6). No identity `W = E` and no minorant `W ≥ E` with E a finite Eisenstein combination can give
`W(p) > 0` for the primes `p ≡ 1 (mod L)` (the Mordell-hard class, since 24 | L can be assumed). The same holds
for every n-local object whose values at primes and at prime squares are quasi-polynomials in the prime.
*Reading.* At primes, finite Eisenstein combinations are quasi-polynomials in p (Jacobi: `r₄(p) = 8(p+1)`).
The only freedom is the shape of the polynomial; T1 at prime squares `ℓ² ≡ 1 (L)` pins it down
coefficientwise. Exactness of r₄ is therefore not transferable: the positive closed form is
congruence-plus-size data, i.e. B1.

**Escape (the hypothesis to violate).** *Shifted* arguments: `E(A_i n + B_i)`, e.g. `σ(gn+1; −1, g)` (§7). At
primes these are not quasi-polynomial. But a *finite* set of shifts `(A_i, B_i)` is a fixed finite set of
slices (B2: POINTWISE_SIZE Thm C, fails i.o. under H), and Type II needs all g ≤ n. So an exact identity must
involve an *unbounded* family of shifts, and its closed form would be a shifted-convolution identity. §9.1
tests this numerically.
