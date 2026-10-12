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
Let `8 | M` and either `2D | M` or Q in the principal genus. Let C be a square class mod M, S a sector, R > 0. Then there is `(u,v) ∈ C ∩ S` with
`u² + v² > R²` and `Q(u,v) = w²`, w odd.

*Proof.* Let X ⊂ P² be the conic `Q(u,v) = w²`; it is smooth because the ternary form has
determinant `−D/4 ≠ 0`. Local points: (i) for ℓ ∤ M, ℓ ∤ 2D, X has good reduction, a smooth conic
over F_ℓ has ℓ + 1 points, and Hensel lifts them. (If instead Q is in the principal genus, Q
represents a square prime to D rationally, so X(Q) ≠ ∅ directly and (i) is not needed.) (ii) For ℓ | M, `Q(u₀,v₀)` is an ℓ-adic unit that
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

*Remarks.* (1) Some hypothesis ensuring X(Q) ≠ ∅ is needed. If Q is not in the principal genus, it
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

## 3. The obstruction theorem

For a polynomial family F let `K_F` be a modulus such that `F(P) ∈ Z⁶` depends only on `P mod K_F`
(take K_F = a common denominator of the coefficients: `δ·g ∈ Z[u,v]`, and `δg(P) mod δ` is
`δ`-periodic). Let `H_j` be the top-degree form of the j-th coordinate (all coordinates are nonzero
polynomials: ET Σ-points have no zero coordinate), and
`A_F = {θ : H_j(cos θ, sin θ) > 0 for j = 1,…,6}` (an open subset of the circle).

**Lemma 3.1 (signs at infinity; PROVED, elementary).** Let `Z_F` be the finite set of directions
where some H_j vanishes. For every δ > 0 there is R_δ such that if `|P| > R_δ` and
`dist(arg P, Z_F) > δ`, then all coordinates of F(P) are positive iff `arg P ∈ A_F`.
*Proof.* On the compact set `{dist(θ, Z_F) ≥ δ}`, `|H_j| ≥ c_δ > 0`; the lower-degree terms are
`O(|P|^{deg − 1})`. ∎

**Theorem 3.2 (no two-variable identity on a square class; PROVED, unconditional, any degree).**
Let F be a polynomial Type I or Type II family for Q (§1). Let M be divisible by 8, 2D and K_F.
(a) F is valid at no point P with `Q(P)` an odd square.
(b) If F is integral at some point of a square class C mod M, then `A_F = ∅`.
(c) Hence, for every square class C mod M and every δ > 0, the points of C where F is valid lie,
outside a bounded set, within angle δ of the finite set Z_F of directions.
*Proof.* (a) is Lemma 1.1, since a valid F(P) is an N-point of Σ_I resp. Σ_II for `n = Q(P)` (§1).
(b) If F is integral at one point of C, it is integral on all of C because K_F | M. If A_F ≠ ∅,
it contains an open arc I; by Lemma 3.1 (with δ smaller than the distance from a closed subarc to
Z_F) F is valid at every point of C in the sector over that subarc and beyond some radius. Lemma 2.1
gives such a point with Q(P) an odd square, contradicting (a). (c) follows from (b) and Lemma 3.1:
if F is not integral on C there is nothing to prove. ∎

**Lemma 3.3 (rational-function families reduce to polynomial ones; PROVED, elementary).** Let
`g = A/B` (A, B ∈ Z[u,v] coprime, B nonconstant). Then `#{P ∈ Z² : |P| ≤ X, B(P) ≠ 0, g(P) ∈ Z} ≪_{g,ε} X^{1+ε}`.
*Proof.* Take an irreducible factor B₁ of B, of positive v-degree say. `R(u) = Res_v(A, B₁) ≢ 0`
(Gauss's lemma), and `κR = αA + βB₁` with α, β ∈ Z[u,v], κ ∈ Z∖0. If `g(P) ∈ Z` then `B₁(P) | A(P)`,
so `B₁(P) | κR(u)`. For each of the O(X) values u with `R(u) ≠ 0` and `B₁(u,·)` nonconstant,
`B₁(u,v)` takes one of `≤ 2τ(κR(u)) ≪ X^ε` values, each at `≤ deg_v B₁` values v. The finitely many
exceptional u contribute O(X). If B₁ = B₁(u), swap the roles of u and v. ∎
Prime points number `≍ X²/log X` in every square class (Q in the principal genus), by Hecke (below), so a rational-function
family with a non-polynomial coordinate is valid at a density-zero set of prime points.

**Corollary 3.4 (finite certificate sets miss almost all primes of every square class; PROVED,
relative to Hecke's equidistribution of prime ideals in sectors and ray/ring classes).** Let 𝔉 be a
finite set of polynomial or rational-function Type I/II families for Q. Let M be divisible by 8,
2D and all K_F. Let r be a square unit mod M such that the primes `p ≡ r (M)` represented by Q have
positive density (for Q = u² + v²: every r ≡ 1 (4)). Then the primes `p ≡ r (mod M)` with
`p = Q(P)` for some P at which some F ∈ 𝔉 is valid have relative density 0 among these primes.
In particular, for every Mordell-hard class r₀ mod 840 (all are squares: 1, 121, 169, 289, 361, 529)
and every such 𝔉, almost all primes `p ≡ r₀ (mod 840)` that are squares mod M are not certified by 𝔉.
These primes have relative density `∏_{ℓ | M, ℓ ∤ 840} 1/2 > 0` within the class.
*Proof.* Every representation P of such a p lies in a square class mod M (`Q(P) = p ≡ r`). Each p
has at most `2w(D) ≤ 12` representations (8 for u² + v²). By Lemma 3.3 and Theorem 3.2(c),
the valid points of each F lie, up to a set of zero density among prime points, in `δ`-sectors around
`|Z_F|` directions. By Hecke's theorem (Gaussian primes, resp. prime ideals of the order of
discriminant D in a fixed ring class, equidistribute in angle within each ray class mod M), their
share of prime points is `≤ C_𝔉 δ + o(1)`. Let δ → 0. ∎

So **no Fermat + identity certificate** (compute a representation p = Q(u,v), then evaluate one of
finitely many polynomial or rational ET identities in (u,v)) proves ES for all, or for a positive
proportion of, the primes in any square class. The degree is unbounded and no hypothesis is used.
This is the two-variable analogue of Mordell–Schinzel (one-variable identities cannot cover square
classes; ET p. 8). The proof is the same: odd squares in the parameter set.

## 4. Extensions and exact scope

**4.1 Any polynomial parametrisation (PROVED, the abstract principle).** Lemma 1.1 is pointwise. If
`N ∈ Z[x₁,…,x_k]` and F(x) is a polynomial ET family with `n = N(x)`, then F is invalid at every x
with N(x) an odd square (Type I) or a square (Type II). Theorem 3.2 holds whenever the integral points
of `{N(x) = w²}` meet every set on which F is valid "generically", i.e. every congruence class times
open cone. Lemma 2.1 proves this for positive definite binary quadratic N.

**4.2 One-parameter families of forms (PROVED for fixed s; scope).** Let
`Q_s = A(s)u² + B(s)uv + C(s)v²` and let F(s, u, v) be polynomial with `n = Q_s(u,v)`. For every s₀
with `Q_{s₀}` positive definite and in the principal genus, `F(s₀, ·, ·)` is a two-variable family
for `Q_{s₀}`. Its integrality modulus divides `K_F`, independently of s₀, so Theorem 3.2 and
Cor 3.4 apply with `M = lcm(8, K_F)`; the principal-genus clause of Lemma 2.1 removes `D(s₀) | M`.
So for each fixed s₀, and for each bounded set of s, the certificate misses almost all primes of
every square class. A certificate that lets s grow with p (pick, for each p, a form `Q_s` with s
unbounded) is outside the theorem. It is the O145 "k unbounded" escape (E1): choosing s is choosing a
divisor or class, i.e. B2. Forms outside the principal genus represent only primes in non-square
classes mod 4|D| (genus characters), where the classical one-variable theory already applies.

**4.3 Indefinite Q (partial).** Lemma 2.1 holds with S inside the cone `{Q > 0}`, and Theorem
3.2(a),(b) hold verbatim, with A_F replaced by its intersection with that cone. Cor 3.4 does not
follow. Each p has infinitely many representations, which accumulate at the two null directions of
Q, and Lemma 3.1 says nothing in cusp regions `{0 < Q(P) ≤ g(|P|)}` with g = o(|P|²). Square points do
reach the cusps: automorph orbits `γ^k P₀`, γ ≡ 1 (M), have fixed square value and |P| → ∞. Whether a
family can be valid on a cusp is OPEN. The positive-definite case is the one relevant to Fermat
certificates (p = u² + v², u² + 2v², …).

**4.4 What Theorem 3.2 covers, and what it does not.**
* Covered: finitely many polynomial or rational ET identities in (u,v) (or in (s,u,v), s bounded),
  chosen by congruence conditions on (u,v) and by sign/semialgebraic conditions. A congruence-case
  split is a finite set of families, and a semialgebraic validity region is absorbed by Lemma 3.1.
  The choice among the ≤ 12 representations of p is also covered. Any degree; no hypothesis.
* Not covered: (i) procedures with floor division by non-constants or with factorisation of values
  in (u,v). That is the two-variable version of Theorem C, which would need a two-variable
  Hypothesis H for binary forms; not attempted. (ii) Unbounded families of forms (4.2). (iii)
  Indefinite forms in cusps (4.3). (iv) Families given only by (x,y,z) ∈ Q[u,v]³, whose canonical ET
  coordinates are gcd-defined and need not be polynomial. At a square point the specialised (x,y,z) is
  a solution for m², but Lemma 1.1 needs the N-point. Reducing (iv) to the ET-coordinate case
  needs either polynomial gcds or square points P with `gcd(Q(P), y(P)z(P)) = 1`; not done.
* **Non-square classes are not an escape worth having.** A family integral on a non-square class mod
  K_F exists trivially: any one-variable identity in n, composed with n = Q(u,v), works. So positive
  proportions of a Mordell-hard class mod 840 are certainly coverable by identities, e.g. the
  `(p/13) = −1` primes outside six classes mod 720720 (MORDELL Thm 3.1, ET Prop 1.9 classes). The
  invariant content of Cor 3.4 is: **after refining to the joint modulus, every square class is
  almost entirely uncovered**, exactly as in one variable.

## 5. Structure of two-variable families (question (1) of the brief)

Theorem 3.2 settles square classes. On non-square classes, which families are genuinely two-variable,
i.e. not in `Q[n]⁶` with n = Q(u,v)?

**Prop 5.1 (constant level gives nothing new; PROVED, any nondegenerate Q).** If c, d are constants,
every Type I or Type II family for Q lies in `Q[n]⁶`.
*Proof.* Type I: (2.9) reads `n² + 4c²d = f·f′` with `f′ = 4bcd − n`. Over C,
`Q² + 4c²d = (Q − 2ic√d)(Q + 2ic√d)`, and each factor is a smooth affine conic `Q = const ≠ 0`, hence
irreducible. Neither factor is defined over Q, so `Q² + 4c²d` is irreducible in Q[u,v]. Thus f or f′ is
constant, and the other is `(n² + 4c²d)/const ∈ Q[n]`. Then `a = (n + f)/4cd`, `b = (n + f′)/4cd` and
`e = (a + b)/c` lie in Q[n]. Type II: (2.21) reads `4c²dn + 1 = f·f′` with `f′ = 4bcd − 1`, an
irreducible conic. Again one factor is constant and everything lies in Q[n]. ∎
This extends O145's "no two-variable extension of the constant-level shape" (§5 there) to all
constant-level families and all forms.

**Prop 5.2 (Type II families valid on an open cone are one-variable; PROVED relative to O145 Prop 3.2,
which is brainstorm-level and not separately reviewed).**
Let F be a Type II family for positive definite Q with `A_F ≠ ∅`. Then `F ∈ Q[n]⁶`.
*Proof.* Fix a rational direction θ ∈ A_F and a rational line `ℓ(t) = P₀ + tθ` not through 0. `P(t) = Q(ℓ(t)) > 0` on R, and all
coordinates of `F∘ℓ` are positive for large t. O145 Prop 3.2 (Type II coordinates `p = 4dgg′ − h`,
`g + g′ = ch` with (g, g′, h) = (a, b, e)) gives `G∘ℓ ∈ Q[P]` for every coordinate G. P(t) is
symmetric about its vertex, so `G∘ℓ` is too. Hence `G∘σ_θ = G` on ℓ, where
`σ_θ(x) = x − 2B(x,θ)θ/Q(θ)` is the Q-reflection along θ (B the bilinear form of Q). The lines ℓ are
Zariski dense, so G is invariant under σ_θ for all θ in the open arc A_F. Products of two such
reflections are Q-rotations through all small angles, so they generate SO_Q(R). Thus G is
O_Q(R)-invariant, and `G ∈ R[Q] ∩ Q[u,v] = Q[Q]`. ∎
So on cones Type II gives nothing new, and genuinely two-variable families, if any, are Type I with
non-constant level. Prop 5.2's input for Type I (a Type I analogue of O145 Prop 3.2 for quadratic P)
is O145's open question. §6 searches for them.

## 6. Search for genuinely two-variable Type I families (EVIDENCE)

`scripts/bf_search_typeI.py`. For levels c ∈ {1, 2, 3} (`const`) or c ∈ {1, 2} ∪ {affine-linear
αu + βv + γ, coefficients in {−1, 0, 1, 2}} (`lin`, 62 values), and d any nonzero polynomial of degree ≤ 2
with coefficients in {−1, 0, 1} (728 values), it factors `N = n² + 4c²d` over Q (ET (2.9)). It tries
every divisor `f = κf₀` (κ fixed by `4cd | n + f`; if κ is free, all ±m/n with m, n | 64·content)
and keeps polynomial solutions. It verifies the ET equations symbolically and discards families in
`Q[n]⁶`, i.e. those invariant under the infinite-order rational rotation (3/5, −4/5; 4/5, 3/5).
* **Positive control:** on the degenerate form `u² + 21` (v a dummy) it rediscovers the O145 k = 21
  family `(c, d) = (1, 22)`, `f = u² ∓ 2u + 23`.
* **Q = u² + v²: 0 genuinely two-variable families** in both ranges (`data/bf/search_sum2_const.txt`,
  `data/bf/search_sum2_lin.txt`; 3 × 728 and 62 × 728 level pairs).
  For constant levels this is Prop 5.1. For linear c it is new, and only EVIDENCE: the search box is
  small, κ is restricted, and a, b, e must come out polynomial (not merely integer-valued on a coset).
* Engineering note: the integrality and square-class audit (an M² loop) is skipped when
  `M = lcm(8, K, 2|D|) > 1500`. It did not trigger for u² + v², since no families were found.

Assessment: genuinely two-variable ET families for a definite binary form are at least rare. Type II
has none on cones (Prop 5.2), constant levels give none (Prop 5.1), and the small linear-level box
gives none. Theorem 3.2 makes this moot on square classes. On non-square classes,
one-variable identities already do the work.

## 7. Summary and labels

* Lemma 1.1 — square vanishing for arbitrary N-points (ET Prop 1.6 without coprimality): PROVED.
* Lemma 2.1 — odd-square values of Q in every square-class coset and sector (Hasse–Minkowski + weak
  approximation): PROVED. Lemma 2.2 — profinite "class of one" for u² + v²: PROVED, table CERTIFIED.
* **Theorem 3.2** — no polynomial Type I/II family (any degree) is valid on a cone of a square
  class; its valid points in square classes lie near finitely many directions: **PROVED,
  unconditional.** Lemma 3.3 (rational families): PROVED.
* **Cor 3.4** — every finite set of polynomial or rational "Fermat + identity" certificates misses
  almost all primes of every square class mod the joint modulus. Hence it misses infinitely many
  (indeed a positive proportion of) Mordell-hard primes. PROVED relative to Hecke's equidistribution
  theorem. Novelty: two-variable analogue of Mordell–Schinzel, folklore-level; the proof is standard.
* Prop 5.1 (constant level ⇒ one-variable, all forms): PROVED. Prop 5.2 (Type II on cones ⇒
  one-variable): PROVED relative to O145 Prop 3.2.
* Open: indefinite forms in cusp regions (4.3); (x,y,z)-only families (4.4(iv)); procedures with
  floor or factorisation in (u,v) (a two-variable Theorem C, would need H); unbounded families of
  forms (E1/B2); Type I analogue of O145 Prop 3.2.
