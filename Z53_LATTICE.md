# Z53_LATTICE — B2 via geometry of numbers: what lattice pigeonhole can and cannot give

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only (not refereed).

Lane: z53 LATTICE (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z53_lanes.md` §LATTICE). Scripts
`scripts/z53_lattice_*`, data `data/z53/lattice/`.

**Status: checkpoint 1 (skeleton).**

## 0. Notation and the statements attacked

n odd ≥ 3 (the prime p ≡ 1 (24) is the case of interest; odd squares and near-squares are controls). The (★) surface is

  G_n(u, B, C) := 4CuB − u − B − n,  V_n := {G_n = 0},  R(n) := #(V_n ∩ ℕ³)   (FRONTIER §2.1).

Equivalently X = 4Cu − 1, Y = 4CB − 1: XY = N_C := 4Cn + 1, X ≡ Y ≡ −1 (mod 4C).

**Thue's mechanism** (p = x² + y²): a lattice Λ of index D on which the target polynomial is ≡ target (mod D) identically,
and a convex body K of volume ≥ index on which |polynomial − target| < D. Geometry of numbers gives a lattice point in K;
the congruence plus the size bound force exact equality ("exactness").

**Definition (convex Thue scheme for (★) at n).** A triple (Λ + t, D, K) with Λ ⊆ ℤ³ a lattice of index D′, t ∈ ℤ³, D ≥ 1,
K ⊆ [1, ∞)³ convex, such that
* (E) exactness congruence: G_n(v) ≡ 0 (mod D) for every v ∈ Λ + t;
* (S) size: |G_n(x)| < D for every x ∈ K;
* (V) volume: vol(K) ≥ D′ (necessary for every translation-uniform geometry-of-numbers existence theorem: covering
  radius ≤ 1, i.e. K + Λ = ℝ³, forces vol K ≥ covol Λ = D′).
If such a scheme exists *and* the GoN theorem used actually certifies (Λ + t) ∩ K ≠ ∅, then every point of (Λ + t) ∩ K is
a (★) solution. (Thue: Λ = {x ≡ ιy (p)}, D = D′ = p, K = disc of area 2πp, target x² + y² = p.)

### Statements attacked
* **(A) No-go for convex Thue schemes in natural coordinates.** For all n ≥ n₀ (explicit) there is no convex Thue scheme
  for (★). — target label PROVED.
* **(A1) algebraic core.** If G_n ≡ 0 (mod D) on a coset of index D′ in ℤ³, then D′ ≥ D^{4/3}/c₀ (c₀ absolute). — PROVED
  (proof below; brute-force cross-check CERTIFIED for small ℓ^f).
* **(A3) non-convex escape is lattice-point counting.** Dropping convexity, the coset choice cannot raise the expected
  (volume) mass of the shell {|G| < D} above c₀·(the trivial-lattice mass ≍ log²n): no lattice amplifies the lottery.
* **(B) polynomial encodings.** For a polynomial encoding Φ: ℤ^k → ℤ³, every exactness prime ℓ > 3 deg Φ (ℓ ∤ 2n) either
  pins Φ(Λ + t) to a point mod ℓ (congruence data, B1) or *designates ℓ as a prime factor* of u, B, C, X or Y (the five
  lines of V_n) — the transparent-certificate shape of B4.
* **(C) Coppersmith / Lenstra.** Precise regimes for the (★) slices; the CHN/LLL lattice guarantees are uniform in n and
  hold at odd squares where the root set is empty (T1), so no existence statement follows from them; Coppersmith =
  Thue-exactness applied to an *assumed* root (Howgrave-Graham's lemma).
* **(N) numerics.** Coset maxima mod ℓ^f; mass of R(p) in the Lenstra/CHN regimes; natural lattice invariants at the
  14 (★)-zero primes vs controls.

### Why this is not already closed
FRONTIER's M1b row ("Thue/Minkowski: target class depends on the exact height; covering needs sub-power windows") is an
**Assessment**; the sub-power-window part ((J)85 Thm 3.1) is a theorem about *covering* by divisor boxes in relation lattices,
not about Thue-type exactness. LATTICE_MEETING, s4_minkowski_sail, s3_lll_lenstra and gon_lll_relation_lattice record that
Minkowski is sign-blind / Coppersmith has no existence content, also as Assessments or for specific lattices
(Λ_A, L_ρ(g)). No theorem says that *no* lattice and *no* convex body of any index can carry a Thue argument for (★).
(A) is that theorem for the natural coordinates; (B) extends it to polynomial encodings, and (A3) identifies the exact
escape (non-convex counting = §7.1).

## 1. First lemma (checkpoint 1): the algebraic core (A1)

Taylor expansion at t: G(t + h) = G(t) + L_t(h) + Q_t(h) + T(h), with
L_t(h) = (4CB − 1)h_u + (4Cu − 1)h_B + 4uB h_C, Q_t(h) = 4(C h_u h_B + u h_B h_C + B h_u h_C), T(h) = 4 h_u h_B h_C
(coefficients at t = (u, B, C)).

**Facts.** (i) V_n is smooth mod every prime ℓ: for ℓ = 2, ∂_uG = 4CB − 1 is odd; for ℓ odd, 4CB ≡ 4Cu ≡ 1 forces u, B
units, contradicting 4uB ≡ 0. (ii) G_n is irreducible over F_ℓ for every odd ℓ (degree 1 in C, content
gcd(4uB, u + B + n) = 1), so V_n mod ℓ contains no plane.

**Proof sketch of (A1)** (full proof in §2): if G ≡ 0 (mod ℓ^f) on t + H then, using h, −h, 2h ∈ H,
L ≡ Q ≡ T ≡ 0 on H modulo ℓ^{f−O(1)} (exactly mod ℓ^f for ℓ ≥ 5). H lies in ker L_t, a free rank-2 module; Q_t, T are not
both ≡ 0 mod ℓ on it (fact (ii)); a submodule isotropic for a binary quadratic (resp. cubic) form that is nonzero mod ℓ has
order ≤ ℓ^{3f/2} (resp. ℓ^{5f/3}). Hence [ℤ_ℓ³ : H] ≥ ℓ^{4f/3} up to bounded losses at 2 and 3.

**First falsifier (to run):** brute-force the largest coset inside V_n mod ℓ^f for ℓ^f ∈ {4, 8, 16, 9, 27, 5, 25, 7, 49}
and all n mod ℓ^f; any coset larger than the bound kills (A1).
