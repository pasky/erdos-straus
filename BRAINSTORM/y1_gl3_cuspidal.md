# y1_gl3_cuspidal — T1 also kills GL(3) (and GL(m)) cuspidal additions, except self-dual orthogonal ones (O209)

## Idea (brief item (c); O205 spark)
O205 Prop 2.3 kills finite GL(k)-Eisenstein combinations E(n) = Σ_k Σ_i c_{k,i} d_k(n; ψ…) by T1 at the square shapes ℓ^{2a};
"GL(3) cuspidal contributions are not excluded (would need Sym^{2a} averages)". Screen a = E + C,
C(n) = Σ_i c_i ψ_i(n) λ_{π_i}(n), π_i unitary cuspidal automorphic representations of GL(m_i)/ℚ (m_i ≥ 2: GL(2) Maass
or holomorphic, GL(3), …), ψ_i, and the characters inside E, of conductor dividing L. Construction-first: find the
hypothesis of Prop 2.3 that a cusp form could violate — **a Satake parameter equal to ±1 at every prime**.

**Proposition G (PROVED relative to the prime number theorem for cuspidal L(s, π ⊗ ψ), i.e. Jacquet–Shalika
non-vanishing on Re s = 1).** Suppose a(m²) = 0 for all odd m, and there is one prime ℓ₀ ≡ 1 (mod L), unramified for all
π_i, such that for every i no Satake parameter α of π_i at ℓ₀ has α² = 1. Then a ≠ N₋.
*Proof.* (1) For a ≥ 0, E(ℓ₀^{2a}) = Σ_k C_k·binom(2a + k − 1, k − 1) (all characters are 1 at ℓ₀), a polynomial in a, with
C_k := Σ_i c_{k,i} global constants. (2) λ_{π}(ℓ₀^{2a}) = h_{2a}(α₁, …, α_m) (complete homogeneous polynomial; Hecke
relations for unramified GL(m)) is an exponential polynomial Σ_β P_β(a) β^a with bases β ∈ {α_j²}, all ≠ 1 by
hypothesis. (3) a(ℓ₀^{2a}) = 0 for all a and linear independence of {a^r β^a} force the polynomial part to vanish
identically; Prop 2.3's induction gives C_k = 0 (k ≥ 2), C₀ + C₁ = 0. Hence E ≡ C₀ + C₁ = 0 on the semigroup S_L of
integers composed of primes ≡ 1 (L). (4) So N₋(ℓ) = C(ℓ) for all primes ℓ ≡ 1 (L), and
Σ_{ℓ ≤ X, ℓ ≡ 1 (L)} C(ℓ) = Σ_i c_i φ(L)⁻¹ Σ_{ψ mod L} Σ_{ℓ ≤ X, ℓ ∤ L} ψ(ℓ)λ_{π_i}(ℓ) = o(X/log X) (ψ_i(ℓ) = 1 there;
π_i ⊗ ψ is cuspidal, PNT for its L-function). (5) But N₋ ≥ 0 and N₋(ℓ) ≥ 1 for all primes ℓ ≡ 1 (mod L), ℓ ≡ 1 (4), ℓ ≡ −1 (q), for a fixed
prime q ≡ 3 (4), q ∤ L (SIGN_IDENTITY Lemma 1.2) — a set of primes of positive density. Contradiction. ∎
*Scope.* Any finite set of cusp forms on any GL(m), with characters; E as in Prop 2.3. The hypothesis is mild: it fails
for π_i only if at **every** good prime ℓ ≡ 1 (L) some parameter is ±1.
**The residual class (Assessment, with the classical input).** Self-dual orthogonal π on GL(3) — by Ramakrishnan
(*An exercise concerning the selfdual cusp forms on GL(3)*, 2014) twists of Gelbart–Jacquet lifts Ad(σ) ⊗ ψ (ψ quadratic) —
have parameters {ψα/β, ψ(ℓ), ψβ/α}: **every element of SO(3) has eigenvalue 1**. There λ(ℓ^{2a}) contains the base β = 1
with constant (degree 0) coefficient κ(ℓ) = −α²/(1 − α²)² = 1/(4 sin²θ_ℓ) (α = e^{iθ_ℓ}/normalised, β = 1/α for σ of
trivial central character). This can absorb only the rank-0/1 constant C₀ + C₁ (rank ≥ 2 Eisenstein terms still die,
since the cusp side has no polynomial of degree ≥ 1 in a at a generic prime). The remaining identity would force
N₋(ℓ) = Σ_i c_i (λ_i(ℓ) − κ_i(ℓ)) on primes ℓ ≡ 1 (L): bounded-on-average versus the proved growth (below). Excluding
this rigorously needs a mean of the unbounded κ(ℓ) = 1/(4 sin²θ_ℓ) over primes (Sato–Tate with uniform integrability) —
not attempted. So the GL(3) escape route is **exactly the orthogonal (Sym²/Ad) one** that O205's spark pointed at, and
it is a rank-0/1 escape: no d₃-size main term can come from it.

## Literature
Jacquet–Shalika, *A non-vanishing theorem for zeta functions of GL_n*, Invent. Math. 38 (1976); Gelbart–Jacquet (1978);
Ramakrishnan (2014, above); Barnet-Lamb–Geraghty–Harris–Taylor (Sato–Tate for non-CM holomorphic f, 2011).

## Barrier screen
T1-killed (Prop G) except the orthogonal residual; size: cuspidal parts have mean 0 (no pole), so the d₃ main term must
come from E, whose rank ≥ 2 part T1 kills on S_L — the identity class "Eisenstein + cuspidal (any GL(m))" is dead except
rank ≤ 1 + orthogonal. B3/B6: identities of this shape are averages anyway.

## Cheap numerics
Census (`scripts/si_census.c`, 10⁶): the mean of N₋(p) over primes p ≡ 1 (8) is 38.8, 62.1, 92.0 at X = 10⁴, 10⁵, 10⁶
(ratio to log²X: 0.457, 0.469, 0.482), min 4 — growing, as a bounded cuspidal-plus-constant model on S_L cannot be.
(Unconditional growth of the mean over primes p ≡ 1 (4L) is provable: N₋(p) ≥ #{q | p + 1 : q ≡ 3 (4) prime}, whose
mean is ≫ log log X by Bombieri–Vinogradov — Assessment-level sketch, not written out.)

## Assessment
PROVED (relative to Jacquet–Shalika) screen; closes O205's GL(3)-cuspidal spark except self-dual orthogonal π, which can
only touch the constant. Promise 0–1/5 as a route; useful as a steering result: **no GL(m) automorphic identity
(Eisenstein + cuspidal, any finite combination) gives N₋**, up to the orthogonal rank-0/1 residue.
