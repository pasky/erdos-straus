# POINTWISE_BINARYFORM — two-variable "Fermat + identity" certificates (task O159)

ES is not solved; nothing here proves any infinite case of it. Labels as in DISCOVERIES.md.

## 0. Question and answer in one paragraph

A prime `p ≡ 1 (4)` is `p = u² + v²`; more generally `p = Q(u,v)` for a binary form of discriminant
D. Computing (u,v) needs a modular square root, so a certificate "ES solution = polynomial in (u,v)"
is not a polynomial (or bounded procedure) in p, and Theorem C (POINTWISE_SIZE §2, linear P only)
does not apply. **Answer (§§1–5): the square specialisation kills every such certificate on every
square class, unconditionally and in every degree.** If the ET coordinates (a,…,f) are polynomials
(or rational functions) in (u,v), then on every coset C mod M (8D | M) with Q(C) a square unit mod M,
the family is valid at only a density-zero set of the prime points of C. The reason is that
`Q(u,v) = w²` is a conic with a rational point, so weak approximation puts odd-square values of Q in
every square-class coset and every sector. At those points the identity would produce a Type I/II
point for an odd square, which ET Prop 1.6 forbids. Families on non-square classes exist but are
not new territory: such classes are already reachable by one-variable identities in p.

## 1. Setup

`Q(u,v) = Au² + Buv + Cv²` ∈ Z[u,v], primitive, positive definite, `D = B² − 4AC < 0`.
Points `(u,v) ∈ Z²`; *prime points*: `Q(u,v)` prime.

A **Type I family** for Q is a sextuple `F = (a,b,c,d,e,f) ∈ Q[u,v]⁶` (in §6 also `Q(u,v)⁶`)
satisfying ET's equations (2.1)–(2.9) for `n = Q(u,v)` identically, e.g.
`4abd = ne + 1`, `ce = a + b`, `4acd = n + f`, `ef = 4a²d + 1`.
A **Type II family** satisfies (2.13)–(2.21) identically, e.g. `4abd = n + e`, `ce = a + b`,
`4acd = f + 1`, `4c²dn + 1 = f(4bcd − 1)`.
F is **valid at** a point P if `F(P) ∈ Z⁶` and it gives a positive solution
`(x,y,z) = (abdn, acd, bcd)` (Type I) resp. `(abd, acdn, bcdn)` (Type II). Since `abd`, `acd`, `bcd > 0`
force a, b, c to have one sign and `d > 0` (then `e = (a+b)/c > 0`, and `f > 0` from (2.6)/(2.18)),
validity is "F(P) ∈ ±N³×N³" up to the dilation `(a,b,c) ↦ −(a,b,c)` of ET (2.10). Hence WLOG
`F(P) ∈ N⁶`. No coprimality condition (`gcd(c,n) = 1`) is imposed: Lemma 1.1 does not need one.
This is the "(a,…,f) polynomial in (u,v)" certificate shape of the brief.

**Lemma 1.1 (square vanishing for N-points; PROVED, = ET Prop 1.6 without coprimality).**
Let n ≥ 1 and let `(a,…,f) ∈ N⁶` satisfy the equations above.
(I) Type I with n odd: the Jacobi symbol `(−d/n) = −1`. In particular n is not a perfect square.
(II) Type II: `(n/f) = −1` (Jacobi; f odd). In particular n is not a perfect square.

*Proof.* Let ψ(k) = (−d/k) be the Jacobi symbol for odd k > 0. Writing `d = 2^s d₁` with d₁ odd,
`ψ(k) = (−1/k)(2/k)^s (k/d₁)(−1)^{(d₁−1)(k−1)/4}`, so ψ depends only on `k mod 4d`; it extends to a real
Dirichlet character mod 4d (the Kronecker character of Q(√−d)), and ψ(−1) = −1. (Check: for
`k = 4d − 1` we have `4d ≡ 1 (k)`, so `−d ≡ −4⁻¹` and `ψ(k) = (−1/k) = −1`.)
(I) `ef = 4a²d + 1` gives `−d ≡ (2a)⁻² (mod f)`, so f is odd, coprime to 2d, and `ψ(f) = 1`.
`4abd = ne + 1` gives gcd(n, d) = 1. `f = 4acd − n ≡ −n (mod 4d)`, so
`1 = ψ(f) = ψ(−1)ψ(n) = −(−d/n)`. If `n = m²` then `(−d/n) = (−d/m)² = 1`, a contradiction.
(II) `4acd = f + 1` gives f odd, gcd(f, 4d) = 1 and `f ≡ −1 (mod 4d)`, so `ψ(f) = −1`.
`f | 4c²dn + 1` gives `−dn ≡ (2c)⁻² (mod f)`, so `(−dn/f) = 1`, i.e. `(n/f) = ψ(f)⁻¹ = −1`. If
`n = m²` then gcd(m, f) = 1 (as f | 4c²dn + 1) and `(n/f) = 1`, a contradiction. ∎

Remark. This is ET's quadratic-reciprocity proof (their §4), recorded for N-points because a
polynomial family need not keep `gcd(c, n) = 1` at the specialisation points. Type I needs n odd;
Type II needs nothing.

## 2. Odd squares in every square-class coset and every sector

A **sector** is an open cone `S = {r e^{iθ} : r > 0, θ ∈ I}` (I an open arc). A coset
`C = (u₀,v₀) + MZ²` is a **square class** if `Q(u₀,v₀) ≡ s² (mod M)` with gcd(s, M) = 1.

**Lemma 2.1 (square points are dense; PROVED, Hasse–Minkowski + weak approximation on P¹).**
Let `2D | M`, `8 | M`, C a square class mod M, S a sector, R > 0. Then there is `(u,v) ∈ C ∩ S` with
`u² + v² > R²` and `Q(u,v) = w²`, w odd.

*Proof.* Let X ⊂ P² be the conic `Q(u,v) = w²`; it is smooth because the ternary form has
determinant `−D/4 ≠ 0`. Local points: (i) for ℓ ∤ M, ℓ ∤ 2D, X has good reduction, a smooth conic
over F_ℓ has ℓ + 1 points, and Hensel lifts them. (ii) For ℓ | M, `Q(u₀,v₀)` is an ℓ-adic unit that
is a square mod ℓ (ℓ odd) or ≡ 1 mod 8 (ℓ = 2), hence a square `w_ℓ²` in Z_ℓ;
`P_ℓ = (u₀ : v₀ : w_ℓ) ∈ X(Q_ℓ)`. (iii) `X(R) ∋ P_∞ = (cos θ₀ : sin θ₀ : Q(cos θ₀, sin θ₀)^{1/2})`,
θ₀ ∈ I. By Hasse–Minkowski X(Q) ≠ ∅, so `X ≅ P¹_Q`, and X(Q) is dense in `∏_{v ∈ T} X(Q_v)` for
`T = {∞} ∪ {ℓ | M}`. Take `x ∈ X(Q)` close to every P_v, written as a primitive integer triple
(u₁, v₁, w₁). Since u₀ or v₀ is an ℓ-adic unit, closeness at ℓ means
`(u₁,v₁,w₁) ≡ μ_ℓ (u₀,v₀,w_ℓ) (mod ℓ^{k_ℓ})` for some `μ_ℓ ∈ Z_ℓ*` (ℓ^{k_ℓ} ∥ M). Closeness at ∞
means `(u₁,v₁) = t(cos θ, sin θ)` with θ ∈ I and t ≠ 0 real; replacing the triple by its negative
(and μ_ℓ by −μ_ℓ) we may take t > 0. By CRT choose μ ∈ (Z/M)* with μ ≡ μ_ℓ (ℓ^{k_ℓ}) and an integer
`λ > 0`, `λμ ≡ 1 (mod M)`, as large as we like. Then `(λu₁, λv₁) ∈ C ∩ S`, its norm exceeds R, and
`Q(λu₁, λv₁) = (λw₁)²`. It is odd, since Q(C) is a unit mod M and 2 | M. ∎

*Remarks.* (1) The hypothesis `D | M` cannot be dropped. If Q is not in the principal genus, it
never represents a square prime to D (genus characters are trivial on squares), although `Q(C)` can
be a square mod an M prime to D. Then the family question is the classical one-variable one, since
p lies in a non-square class mod 4|D|. (2) Without `8 | M` the 2-adic condition is invisible: for
`u² + v²` and M = 4, every unit class has `Q ≡ 1 (4)`, but only half are of the form below.

**Lemma 2.2 (Gaussian case, profinite form; PROVED, + CERTIFIED table).** Let Q = u² + v² and
8 | M. A unit class `u₀ + iv₀ ∈ (Z[i]/M)*` lies in `(Z/M)*·⟨i⟩·((Z[i]/M)*)²` iff `Q(u₀,v₀)` is a
square mod M. Then `u + iv = λ i^j α²` (`λ ∈ N`, `α ∈ Z[i]`) gives Lemma 2.1 explicitly, with
`Q = (λ N(α))²`.
*Proof.* By CRT, `G_M := (Z[i]/M)* / ((Z/M)*·⟨i⟩·squares)` is the quotient of the product of the
local groups `G_{ℓ^k} = (Z[i]/ℓ^k)*/((Z/ℓ^k)*·squares)` by the diagonal image of i. Odd ℓ: unit squares
mod ℓ^k are detected mod ℓ (Hensel). For split ℓ, `(Z[i]/ℓ)* ≅ F_ℓ* × F_ℓ*`; modulo squares and the
diagonal F_ℓ*, the class of (x, y) is the class of xy = Q mod ℓ. For inert ℓ, `F_{ℓ²}*` modulo squares
has order 2 and contains F_ℓ*, and the class is that of the norm Q mod ℓ. In both cases
`N(i) = 1`, so i dies. ℓ = 2, k ≥ 3: `Z₂[i]*/squares ≅ (Z/2)³` (`Z₂[i]* ≅ μ₄ × Z₂²`). The classes of
5 and i are nontrivial and distinct (5 is not a square in Q₂(i) because −5 ≡ 3 (8); i is not a
square because ζ₈ ∉ Q₂(i)), and both have square norm. The norm map onto `(1 + 4Z₂)/squares` has
order 2, so the quotient is Z/2, detected by `Q mod 8`. (−1 = i² is already a square.) ∎
`scripts/bf_reach_check.py` checks the equivalence by brute force for M = 8, 16, 24, 40, 56, 88,
104, 120, 136, 168, 264 (0 mismatches). It fails for M = 4 (4 of 8 unit classes unreachable,
`data/bf/reach_check.txt`).

So "square class" is exactly the two-variable **class of one**: the trivial element of the
profinite group `lim G_M`. Item (ii) of the brief (a profinite trap at `(u,v) ≡ (1,0)`-type points) is
the same object. Unlike the one-variable trap of O145 Lemma 3.1, it contains genuine rational
square points, so no Hypothesis H is needed.
