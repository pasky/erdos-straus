# y1_gl3_cuspidal — no finite Eisenstein + GL(m)-cuspidal identity for N₋: size at primes kills it, T1 is not used (O209; R214 repair)

## Idea (brief item (c); O205 spark)
O205 Prop 2.3 kills finite GL(k)-Eisenstein combinations E(n) = Σ_k Σ_i c_{k,i} d_k(n; ψ…) by T1 at the square shapes ℓ^{2a};
"GL(3) cuspidal contributions are not excluded (would need Sym^{2a} averages)". Screen a = E + C,
C(n) = Σ_i c_i ψ_i(n) λ_{π_i}(n), π_i unitary cuspidal automorphic representations of GL(m_i)/ℚ (m_i ≥ 2: GL(2) Maass
or holomorphic, GL(3), …), ψ_i, and the characters inside E, of conductor dividing L.
(R214 repair, D6: the first version of this memo used T1 at ℓ₀^{2a} plus a one-prime genericity hypothesis; the reviewer
showed that neither is needed — the identity dies by **size at primes** alone, exactly O205's remark under Thm 2.2 that
"the mechanism is size, not T1".)

**Proposition G″ (PROVED relative to the prime number theorem for cuspidal L(s, π ⊗ ψ) on GL(m), m ≥ 2; R214 repair).**
For every finite family {π_i} of unitary cuspidal representations of GL(m_i)/ℚ (m_i ≥ 2), all Dirichlet characters ψ_i, and
every finite combination E as in Prop 2.3 (exponent-zero twisted divisor convolutions, any rank k, characters of conductor | L),
**N₋ ≠ E + C** on the odd integers.
*Proof.* (1) For a prime ℓ ≡ 1 (L), ℓ ∤ L: d_k(ℓ; ψ₁, …, ψ_k) = Σ_j ψ_j(ℓ) = k (d₀ := 1), so E(ℓ) = K′ := Σ_{k,i} k·c_{k,i}
(+ the d₀-part) is **constant** on these primes. (2) Σ_{ℓ ≤ X, ℓ ≡ 1 (L)} C(ℓ) = Σ_i c_i φ(L)⁻¹ Σ_{ψ mod L} Σ_{ℓ ≤ X, ℓ ∤ L}
ψ(ℓ)λ_{π_i}(ℓ) = o(X/log X): each π_i ⊗ ψ is cuspidal, and the PNT for its L-function holds (Jacquet–Shalika non-vanishing
on Re s = 1, plus the standard Rankin–Selberg/Tauberian step and |α_j(ℓ)| < ℓ^{1/2} to discard prime powers; e.g.
Iwaniec–Kowalski, *Analytic Number Theory*, Thm 5.13 — R214 repair, D8). (3) For p ≡ 1 (4), every prime q ≡ 3 (4) dividing
p + 1 gives the word (1, q + 1, (p + 1)/q + 1) ∈ X_p with A = q and χ = (q/p) = (p/q) = (−1/q) = −1; distinct q give
distinct words, so N₋(p) ≥ ω₃(p + 1) := #{q | p + 1 : q ≡ 3 (4) prime}. By Dirichlet's theorem in finitely many fixed
progressions (then letting the set of q grow; no Bombieri–Vinogradov needed), the mean of ω₃(p + 1) over primes
p ≡ 1 (mod lcm(4, L)), p ≤ X, tends to ∞; since N₋ ≥ 0 and these primes have positive relative density among primes
≡ 1 (L), the mean of N₋ over primes ℓ ≡ 1 (L), ℓ ≤ X, tends to ∞. (4) If N₋ = E + C, by (1)–(2) that mean is K′ + o(1).
Contradiction. ∎
*Scope.* Unconditional in the family: no genericity hypothesis, no T1, any m, any characters — in particular it covers the
self-dual orthogonal class (Ad(σ) ⊗ ψ) and the tetrahedral/dihedral examples of D7 below. Not covered: infinite sums of
cusp forms, shifted/derivative/non-standard-normalised coefficients, growing level, non-automorphic objects. The same
argument also gives O205 Prop 2.3's "in particular E ≠ N₋" without T1 (flagged by R214 to the O205 owner).

**Remark G (the T1 analysis, demoted; PROVED, relative to the same Hecke relations).** What T1 *does* give: if a = E + C
vanishes on all odd squares and there is an odd prime ℓ₀ ≡ 1 (L), unramified for all π_i, at which for every i the value 1
occurs at most once among the squared Satake parameters α_j(ℓ₀)², then E ≡ K := C₀ + C₁ on the semigroup S_L of integers
composed of primes ≡ 1 (L). *Proof.* E(ℓ₀^{2a}) = Σ_k C_k binom(2a + k − 1, k − 1) is a polynomial in a; λ_π(ℓ₀^{2a}) =
h_{2a}(α₁, …, α_m) is an exponential polynomial in a with bases α_j², whose base-1 part is constant under the hypothesis;
linear independence of {a^r β^a} and Prop 2.3's top-degree induction give C_k = 0 for k ≥ 2. ∎ For Ad(σ) ⊗ ψ the squared
parameters are {α⁴, 1, α⁻⁴}, so the hypothesis at ℓ₀ means a_{ℓ₀}(σ) ∉ {0, ±2} (normalised).
*The hypothesis can fail at every admissible prime (R214 repair, D7; the earlier "we do not know whether such π exist"
was wrong).* Let σ be a tetrahedral weight-one newform (projective image A₄; modular by Langlands–Tunnell) and Π = Ad(σ),
cuspidal on GL(3) (Gelbart–Jacquet; σ not dihedral). If L is divisible by the conductor of the cyclic cubic field K₃ fixed by
V₄ ⊲ A₄, then for every unramified ℓ ≡ 1 (L) Frob_ℓ is trivial on K₃, its projective image lies in V₄, and Ad(σ)(Frob_ℓ) has
eigenvalues {1, 1, 1} or {1, −1, −1}: 1 is a triple squared parameter at every admissible ℓ₀. Likewise D₄-type dihedral
weight-one GL(2) forms (ring-class character of order 4, L divisible by the genus-field conductor) have squared parameters
{1, 1} at every ℓ ≡ 1 (L). So Remark G is genuinely conditional; Prop G″ does not need it.

## Literature
Jacquet–Shalika, *A non-vanishing theorem for zeta functions of GL_n*, Invent. Math. 38 (1976); Iwaniec–Kowalski Thm 5.13;
Gelbart–Jacquet (1978); Ramakrishnan, *An exercise concerning the selfdual cusp forms on GL(3)* (2014); Langlands–Tunnell
(tetrahedral/octahedral weight-one forms).

## Barrier screen
Killed by size at primes (B3-type: a finite automorphic combination has a constant main term on primes ≡ 1 (L), N₋ does
not), independently of T1. T1 only enters Remark G. B3/B6: identities of this shape are averages anyway.

## Cheap numerics
Census (`scripts/si_census.c`, 10⁶): the mean of N₋(p) over primes p ≡ 1 (8) is 38.8, 62.1, 92.0 at X = 10⁴, 10⁵, 10⁶
(ratio to log²X: 0.457, 0.469, 0.482), min 4 — growing. R214 (from scratch): N₋(p) ≥ ω₃(p + 1) at every prime p ≡ 1 (4)
< 10⁶.

## Assessment
PROVED (relative to the PNT for cuspidal GL(m) L-functions) screen; closes O205's GL(3)-cuspidal spark completely, for all
finite families, by size at primes; T1 is not used. Scope: *finite combinations of exponent-zero character-twisted divisor
convolutions d_k(n; ψ…) plus coefficients λ_π(n)ψ(n) of unitary cuspidal π on GL(m)* — not "every automorphic identity".
Promise 0/5 as a route; steering: any exact identity for N₋ must have a non-constant main term at primes, i.e. carry
genuinely n-dependent (d₃-type, unboundedly many levels, or non-automorphic) structure.
