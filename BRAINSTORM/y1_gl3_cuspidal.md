# y1_gl3_cuspidal — T1 also kills GL(3) (and GL(m)) cuspidal additions, self-dual orthogonal ones included, under a one-prime genericity hypothesis (O209)

## Idea (brief item (c); O205 spark)
O205 Prop 2.3 kills finite GL(k)-Eisenstein combinations E(n) = Σ_k Σ_i c_{k,i} d_k(n; ψ…) by T1 at the square shapes ℓ^{2a};
"GL(3) cuspidal contributions are not excluded (would need Sym^{2a} averages)". Screen a = E + C,
C(n) = Σ_i c_i ψ_i(n) λ_{π_i}(n), π_i unitary cuspidal automorphic representations of GL(m_i)/ℚ (m_i ≥ 2: GL(2) Maass
or holomorphic, GL(3), …), ψ_i, and the characters inside E, of conductor dividing L. Construction-first: find the
hypothesis of Prop 2.3 that a cusp form could violate — **a Satake parameter equal to ±1 at every prime**.

**Proposition G (PROVED relative to the prime number theorem for cuspidal L(s, π ⊗ ψ), i.e. Jacquet–Shalika
non-vanishing on Re s = 1).** Suppose a(m²) = 0 for all odd m, and there is one **odd** prime ℓ₀ ≡ 1 (mod L), unramified for all
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
*Scope.* Any finite set of cusp forms on any GL(m), with characters; E as in Prop 2.3. The hypothesis is mild (R209: it is a *common*-prime condition over the family): it fails
only if at **every** odd good prime ℓ ≡ 1 (L) some π_i has a parameter ±1.
**The orthogonal class (Assessment, with the classical input).** Self-dual orthogonal π on GL(3) — by Ramakrishnan
(*An exercise concerning the selfdual cusp forms on GL(3)*, 2014) twists of Gelbart–Jacquet lifts Ad(σ) ⊗ ψ (ψ quadratic) —
have parameters {ψα/β, ψ(ℓ), ψβ/α}: **every element of SO(3) has eigenvalue 1**. There λ(ℓ^{2a}) contains the base β = 1
with constant (degree 0) coefficient κ(ℓ) = −α²/(1 − α²)² = 1/(4 sin²θ_ℓ) (α = e^{iθ_ℓ}, β = 1/α for σ of trivial central
character **when σ is tempered at ℓ** — R209: unitarity alone does not put Maass parameters on the unit circle; the formula
is only illustrative, G′ does not use it). This can absorb only the rank-0/1 constant K := C₀ + C₁ (rank ≥ 2 Eisenstein terms still die,
since the cusp side has no polynomial of degree ≥ 1 in a at a prime where 1 is a *simple* squared parameter).
The orthogonal case is closed by the next statement.

**Proposition G′ (PROVED relative to Jacquet–Shalika and Bombieri–Vinogradov).** Prop G holds with the weaker
hypothesis: some odd prime ℓ₀ ≡ 1 (L), unramified for all π_i, at which for every i the value 1 occurs **at most once** among the
squared Satake parameters α_j(ℓ₀)² (for Ad(σ) ⊗ ψ: α⁴ ≠ 1 at ℓ₀, i.e. a_{ℓ₀}(σ)² ∉ {0, 4} after normalisation |a| ≤ 2 — R209 repair).
*Proof.* As in Prop G, the base-1 component of C(ℓ₀^{2a}) is now a constant (degree 0 in a), so the degree ≥ 1 part of
Σ_k C_k binom(2a + k − 1, k − 1) vanishes: C_k = 0 for k ≥ 2, and E ≡ K = C₀ + C₁ on S_L (K need not vanish). Hence
N₋(ℓ) = K + C(ℓ) for primes ℓ ≡ 1 (L), and the mean of N₋ over primes ℓ ≡ 1 (L), ℓ ≤ X, is K + o(1) (PNT for the cuspidal
π_i ⊗ ψ). But for p ≡ 1 (4), every prime q ≡ 3 (4) dividing p + 1 gives the word (1, q + 1, (p + 1)/q + 1) with A = q and
χ = (q/p) = (p/q) = (−1/q) = −1, so N₋(p) ≥ ω₃(p + 1) := #{q | p + 1 : q ≡ 3 (4) prime}; by Bombieri–Vinogradov the mean
of ω₃(p + 1) over primes p ≡ 1 (mod lcm(4, L)), p ≤ X, is ≥ (1 − o(1))·Σ_{q ≤ X^{1/3}, q ≡ 3 (4), q ∤ L} 1/(q − 1) → ∞.
Contradiction. ∎
So **no finite combination of GL(k)-Eisenstein terms and GL(m)-cuspidal terms (any m, characters allowed) equals N₋**,
under the genericity hypothesis at a single prime ℓ₀ — including the self-dual orthogonal (Sym²/Ad) class that O205's spark
pointed at: orthogonality only lets the cusp side absorb a constant, and a constant is killed by the growth of N₋ on primes.
(Not covered: finite families {π_i} with **no common** odd good prime ℓ₀ ≡ 1 (L) at which 1 is a simple squared parameter for
all i simultaneously (R209: this is a quantifier over the family, not a property of a single π_i) — for a single π, those with 1 a
repeated squared parameter at every good prime ≡ 1 (L) — e.g. parameters {1, −1, α}
everywhere; we do not know whether cuspidal such π exist; infinite sums of cusp forms; non-automorphic objects.)

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
(Unconditional growth of the mean over primes p ≡ 1 (4L): N₋(p) ≥ ω₃(p + 1), mean ≫ log log X by Bombieri–Vinogradov,
used in Prop G′.)

## Assessment
PROVED (relative to Jacquet–Shalika and Bombieri–Vinogradov — BV is not even needed for divergence: PNT in finitely many
fixed progressions q, then let the set of q grow; R209) screen; closes O205's GL(3)-cuspidal spark, including the
self-dual orthogonal class (Prop G′), under the common-prime genericity hypothesis. Scope (R209 repair): the excluded
class is *finite combinations of exponent-zero character-twisted divisor convolutions d_k(n; ψ…) (Prop 2.3's E) plus
coefficients λ_π(n)ψ(n) of unitary cuspidal π on GL(m)* — not "every automorphic identity" (no shifted/derivative/
non-standard-normalised coefficients, no infinite sums, no growing level). Promise 0–1/5 as a route; useful as a steering
result.
