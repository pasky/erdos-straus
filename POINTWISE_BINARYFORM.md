# POINTWISE_BINARYFORM — two-variable "Fermat + identity" certificates (task O159)

ES is not solved; nothing here proves any infinite case of it. Labels as in DISCOVERIES.md.

## 0. Question and answer in one paragraph

A prime `p ≡ 1 (4)` is `p = u² + v²`; more generally `p = Q(u,v)` for a binary form of discriminant
D. Computing (u,v) needs a modular square root, so a certificate "ES solution = polynomial in (u,v)"
is not a polynomial (or bounded procedure) in p, and Theorem C (POINTWISE_SIZE §2, linear P only)
does not apply. **Answer (§§1–5): the square specialisation kills every such certificate whose ET
coordinates (a,…,f) are polynomial or rational in (u,v), on every square class mod the joint modulus,
unconditionally and in every degree.** (R159 repair: qualifier added; certificates given only as
(x,y,z) ∈ Q[u,v]³ are NOT covered, see §4.4(iv), the main open case.) (O163 update: §8 closes
§4.4(iv): Theorem 3.2′ / Cor 3.4′ cover (x,y,z)-families too, with the same hypotheses.) If the ET coordinates (a,…,f)
are polynomials (or rational functions) in (u,v), then on every coset C mod M (8, 2D and the
families' denominators dividing M) with Q(C) a square unit mod M,
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

**Lemma 1.1 (square vanishing for N-points; PROVED, = ET Prop 1.6 / ET §4 with Jacobi refinements).**
(R159 repair: ET's Σ_n already carries no coprimality condition and ET §4 argues for arbitrary
N-points; the additions here are the Jacobi statements and even squares in Type II.)
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
if F is not integral on C there is nothing to prove. (R159 repair: validity allows the sign pattern
(−,−,−,+,+,+) too; apply (b) also to the dilate F⁻ = (−a,−b,−c,d,e,f), a polynomial family with the
same K_F, so that A_F ∪ A_{F⁻} = ∅.) ∎

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
(R159 repair, reference: Hecke, Math. Z. 1 (1918) 357–376 and 6 (1920) 11–51, via Grössencharacters
of K = Q(√D) of modulus f·M and infinity type (α/|α|)^k; the (u,v)-cones are transported by the
linear map (u,v) ↦ uω₁ + vω₂, so a δ-cone has angular measure ≤ C_Q δ.)

So **no Fermat + identity certificate** (compute a representation p = Q(u,v), then evaluate one of
finitely many polynomial or rational ET identities in (u,v), i.e. families whose ET coordinates
(a,…,f) are polynomial/rational) proves ES for all, or for a positive proportion of, the primes in
any square class mod the joint modulus M. (R159 repair: both qualifiers added; (x,y,z)-only families
are §4.4(iv), open.) The degree is unbounded and no hypothesis is used.
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
  (O163 update: done in §8, Theorem 3.2′; the residual case y(0,0) = 0 is handled by descent.)
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
constant, and the other is `(n² + 4c²d)/const ∈ Q[n]` (R159 repair: "neither factor is defined over Q"
needs d > 0, which validity forces; for any d ≠ 0 it suffices that every divisor in Q[u,v] of g(Q),
g ∈ Q[n], g(0) ≠ 0, lies in Q[n], because each Q − r, r ≠ 0, is irreducible over C). Then `a = (n + f)/4cd`, `b = (n + f′)/4cd` and
`e = (a + b)/c` lie in Q[n]. Type II: (2.21) reads `4c²dn + 1 = f·f′` with `f′ = 4bcd − 1`, an
irreducible conic. Again one factor is constant and everything lies in Q[n]. ∎
This extends O145's "no two-variable extension of the constant-level shape" (§5 there) to all
constant-level families and all forms.

**Prop 5.2 (Type II families valid on an open cone are one-variable; PROVED; dependency O145 Prop 3.2
re-derived and confirmed by R159 — R159 repair to the label).**
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
* **Cor 3.4** — every finite set of polynomial or rational "Fermat + identity" certificates (ET
  coordinates polynomial/rational in (u,v); R159 repair) misses almost all primes of every square
  class mod the joint modulus. Hence it misses infinitely many
  (indeed a positive proportion of) Mordell-hard primes. PROVED relative to Hecke's equidistribution
  theorem. Novelty: two-variable analogue of Mordell–Schinzel, folklore-level; the proof is standard.
* Prop 5.1 (constant level ⇒ one-variable, all forms): PROVED. Prop 5.2 (Type II on cones ⇒
  one-variable): PROVED (O145 Prop 3.2 dependency checked by R159).
* (O163) Theorem 3.2′ / Cor 3.4′ — the same for families given only as (x,y,z) ∈ Q[u,v]³ or
  Q(u,v)³, every square class mod M: PROVED (§8; Cor 3.4′ relative to Hecke).
* Open: indefinite forms in cusp regions (4.3); procedures with
  floor or factorisation in (u,v) (a two-variable Theorem C, would need H); unbounded families of
  forms (E1/B2); Type I analogue of O145 Prop 3.2.

## 8. (O163) Families given only as (x,y,z) ∈ Q[u,v]³ — closing §4.4(iv)

Setting as in §1–3: Q primitive positive definite, D < 0. An **(x,y,z)-family** is a triple
F = (x,y,z) ∈ Q[u,v]³ with `4/Q = 1/x + 1/y + 1/z` identically; F is **valid** at P ∈ Z² if
x(P), y(P), z(P) are positive integers. No ET coordinates are assumed. Q is irreducible in
Q[u,v] (definite ⇒ no rational linear factor), so Q[u,v] being a UFD, "Q | g" is meaningful.
For g ∈ Q[u,v] write g = Σ_j g_j (g_j homogeneous of degree j) and ord₀ g = min{j : g_j ≠ 0}.

**Lemma 8.1 (shapes; PROVED, elementary).** Up to permuting x, y, z exactly one of:
(0) Q divides all three; (I) Q | x, Q ∤ y, Q ∤ z ("Type I shape"); (II) Q | y, Q | z, Q ∤ x
("Type II shape"). In case (0), F is valid at no P with gcd(Q(P), δ) = 1, where δ ∈ N clears
the denominators of x/Q, y/Q, z/Q.
*Proof.* `4xyz = Q(xy + yz + zx)`, so Q | xyz, so Q divides at least one coordinate. Case (0):
write x = Qx₁ etc.; then `4 = 1/x₁ + 1/y₁ + 1/z₁`. If F is valid at P and n = Q(P) is prime to
δ, then n·x₁(P) ∈ Z and δx₁(P) ∈ Z give x₁(P) ∈ Z, and x₁(P) = x(P)/n > 0. Three positive
integers have reciprocal sum ≤ 3 < 4. ∎

**Lemma 8.2 (structure at the origin; PROVED, elementary).**
(I) Type I shape, x = Q·x̃. Either y + z = 0 (then F is never valid, and Theorem 3.2′ below is
vacuous for it), or there is h ∈ Q[u,v]
with `4x̃ − 1 = Qh` and `4yzh = (Qh + 1)(y + z)`. Consequently `x̃(0,0) = 1/4`;
`k := ord₀ y = ord₀ z`; and if k ≥ 1 then `z_k = −y_k`.
(II) Type II shape, y = Qỹ, z = Qz̃. There is h with `4ỹz̃ − ỹ − z̃ = Qh` and `xh = ỹz̃`.
Consequently `(4ỹ(0) − 1)(4z̃(0) − 1) = 1`, and if `x(0,0) = 0` then `ỹ(0,0) = z̃(0,0) = 0`.
*Proof.* (I) Multiply the identity by Qx̃yz: `yz(4x̃ − 1) = Qx̃(y + z)`. If 4x̃ = 1 then y = −z,
and y(P), z(P) are never both positive. Otherwise Q ∤ yz forces Q | 4x̃ − 1 =: Qh, and dividing by
Q gives `yzh = x̃(y+z)`, i.e. the stated identity (x̃ = (Qh+1)/4). At the origin Q = 0, so
x̃(0) = 1/4. Let k = ord₀ y ≤ l = ord₀ z (WLOG). The RHS is `(y+z) + Qh(y+z)`; its second summand
has order ≥ k + 2. If k < l, the degree-k part of the RHS is y_k ≠ 0, while the LHS has order
≥ k + l > k: impossible. So k = l. If k ≥ 1 the LHS has order ≥ 2k > k, so the degree-k part of
the RHS, y_k + z_k, vanishes.
(II) Multiply by Qxỹz̃: `x(4ỹz̃ − ỹ − z̃) = Qỹz̃`; Q ∤ x gives Q | 4ỹz̃ − ỹ − z̃ =: Qh and
`xh = ỹz̃`. At the origin `4ỹ₀z̃₀ = ỹ₀ + z̃₀`, equivalently `(4ỹ₀ − 1)(4z̃₀ − 1) = 1`. If x₀ = 0 then
ỹ₀z̃₀ = x₀h₀ = 0, hence ỹ₀ + z̃₀ = 0, hence both vanish. ∎

*Remark.* So in Type I shape y(0,0) = 0 ⇔ z(0,0) = 0, and the "bad" case of R159's route (Q(P)
sharing the factor gcd(u,v) with y(P)z(P)) is exactly k ≥ 1. One-variable families composed with
n = Q(u,v) always have k = 0 (Y(0) = 0 would mean n | Y in Q[n]), so k ≥ 1 needs a genuinely
two-variable family. Lemma 8.2 is what makes k ≥ 1 harmless (Lemma 8.3).

**Lemma 8.3 (pointwise descent; PROVED from ET Props 1.6, 2.2, 2.6 and Lemma 1.1).** Let λ be an
odd prime, w ≥ 1 odd, `n = λ²w²`, and (x,y,z) ∈ N³ with `4/n = 1/x + 1/y + 1/z`.
(a) If n | x, λ ∥ y, λ ∥ z and gcd(w, yz) = 1, then `( −(x/n)(y/λ)(z/λ) / λ ) = −1` (Legendre).
(b) If n | y, n | z, λ ∥ x and gcd(w, x) = 1, then `( (1 − 4y/n) / λ ) = −1`.
(c) n | x, λ² | y, λ² | z, gcd(w, yz) = 1 is impossible. (d) n | y, n | z, λ² | x, gcd(w, x) = 1
is impossible. (e) (ET Prop 1.6) n | x with gcd(n, yz) = 1, or n | y, z with gcd(n, x) = 1, is
impossible.
*Proof.* (a) Put `(x′,y′,z′) = (x,y,z)/λ` (λ | x as n | x) and `n′ = λw²`; then
`4/n′ = 1/x′ + 1/y′ + 1/z′`, `x′ = n′·(x/n)`, and gcd(n′, y′z′) = 1 (λ ∤ y′z′, and
gcd(w, y′z′) | gcd(w, yz) = 1). So (x′,y′,z′) is a Type I solution for the odd number n′. ET Prop
2.2 gives (A,…,F) ∈ N⁶ ∩ Σ^I_{n′} with `x′ = n′DAB, y′ = DAC, z′ = DBC`; Lemma 1.1(I) gives
`(−D/n′) = −1`. By (2.1) gcd(D, n′) = 1, so `(−D/n′) = (−D/λ)(−D/w)² = (−D/λ)`. Finally
`(x′/n′)y′z′ = D·(DABC)²` with λ ∤ (x′/n′)y′z′ (x′/n′ = DAB is prime to n′ by (2.1)), so
`(−D/λ) = (−(x′/n′)y′z′/λ) = (−(x/n)(y/λ)(z/λ)/λ)`.
(b) Same descent: (x′,y′,z′) = (x,y,z)/λ is a Type II solution for n′ = λw² (n′ | y′ = n′·(y/n),
n′ | z′, gcd(n′, x′) = 1). ET Prop 2.6 gives (A,…,F) ∈ N⁶ ∩ Σ^II_{n′} with y′ = ACDn′, and (2.18)
gives `F = 4ACD − 1 = 4y/n − 1 ≡ 3 (mod 4)`, F > 0. Lemma 1.1(II): `(n′/F) = −1`. By (2.21)
gcd(F, n′) = 1, so `(n′/F) = (λ/F)(w/F)² = (λ/F)`, and quadratic reciprocity with F ≡ 3 (4) gives
`(λ/F) = (F/λ)(−1/λ) = (−F/λ) = ((1 − 4y/n)/λ)`.
(c) `(x,y,z)/λ²` is a Type I solution for the odd square w² (w² | x/λ² = w²(x/n); gcd(w², yz/λ⁴) = 1);
ET Prop 1.6 (for w = 1: 4 = Σ 1/xᵢ has no solutions). (d) Same with Type II. (e) is ET Prop 1.6. ∎
*Check (CERTIFIED for the listed n).* `scripts/bf2_pointwise_check.py` enumerates all solutions for
every n = λ²w² ≤ 12 000 (λ ≤ 47 prime, w odd) and every ordering: the hypotheses of (a) occur 1 612
times and of (b) 688 times, the Legendre symbol is −1 every time, and (c), (d), (e) never occur
(`data/bf2/pointwise_check.txt`, 0 violations).
Note the symbols in (a), (b) are genuinely constraints, not tautologies: without them the descended
solution is an ordinary Type I/II solution for the non-square λw², which exists in abundance.

**Lemma 8.4 (coprime square points on a prime dilate; PROVED: Hasse–Minkowski, Dirichlet, and an
elementary two-variable coprimality sieve of Ekedahl type).** Let 8 | M, 2D | M, C a square class
mod M, S an open sector, R, λ₁ > 0, G ∈ Z[u,v] with Q ∤ G, and H₁,…,H_r ∈ Z[u,v] nonzero forms.
Then there are a prime λ > λ₁ and X ∈ Z² such that
(1) λX ∈ C ∩ S and |λX| > R; (2) Q(X) = w² with w odd; (3) gcd(w, G(λX)) = 1;
(4) λ ∤ w·H₁(X)⋯H_r(X).
*Proof.* Step 1 (a primitive square point and its class). The proof of Lemma 2.1 (applied to a
closed subsector S₁ ⋐ S) gives a primitive (u₁,v₁,w₁) ∈ Z³, w₁ > 0, `Q(X₁) = w₁²` for `X₁ = (u₁,v₁)`,
arg X₁ ∈ S₁, and μ ∈ (Z/M)* such that λX₁ ∈ C for every integer λ ≡ μ⁻¹ (mod M). Then w₁ is
prime to M (Q(C) is a unit) and odd.
Step 2 (base point). Choose a primitive `X₀ = (P₀, w₀) ∈ Z³`, `Q(P₀) = w₀²`, w₀ > 0, with
gcd(w₀, M w₁) = 1: apply Lemma 2.1 with modulus M w₁ to a class that is C mod M and has Q ≡ 1 mod
each ℓ^e ∥ w₁ (ℓ ∤ 2D, so Q mod ℓ is nondegenerate, represents 1, and Hensel lifts), and take the
primitive triple produced there.
Step 3 (parametrisation). For Y ∈ Z² let `β₀(Y) = Q(P₀+Y) − Q(P₀) − Q(Y)` (= 2B(P₀,Y), B the
bilinear form of Q) and `ψ(Y) = (Q(Y)P₀ − β₀(Y)Y, w₀Q(Y)) ∈ Z³`. Expanding,
`Q(Q(Y)P₀ − β₀Y) = Q(Y)²Q(P₀) − Q(Y)β₀² + β₀²Q(Y) = ψ₃(Y)²`. ψ(Y) is the second intersection with
the conic X: Q = w² of the line through X₀ and (Y, 0). Hence every X ∈ X(Q) is proportional to
ψ(Y) for some primitive Y (Y ∝ w₀P − wP₀ if X ≁ X₀; Y ⊥_B P₀ if X ∼ X₀). ψ(Y) ≠ 0 for real Y ≠ 0,
since ψ₃(Y) = 0 forces Q(Y) = 0. (ii) If Y is primitive and a prime ℓ ∤ 2Dw₀ divides all coordinates
of ψ(Y), then ℓ | Q(Y) and ℓ | β₀(Y)Y, so ℓ | β₀(Y); over F_ℓ (Q nondegenerate) Y is isotropic and
B-orthogonal to P₀, so P₀ ∈ F_ℓY and Q(P₀) ≡ 0, i.e. ℓ | w₀: contradiction.
Take Y° primitive with ψ(Y°) ∝ X₁; as ψ₃ > 0, `ψ(Y°) = k₀·(u₁,v₁,w₁)` with k₀ ≥ 1. By (ii) the primes
of k₀ divide 2Dw₀, and w₀ | k₀ because `w₀Q(Y°) = k₀w₁` with gcd(w₀,w₁) = 1.
Step 4 (the family). Put N = k₀M and, for Z ∈ Z², `Y_Z = Y° + NZ`, `X_Z = ψ₁₂(Y_Z)/k₀`,
`F₁(Z) = ψ₃(Y_Z)/k₀`. Expanding ψ(Y° + NZ) = ψ(Y°) + N·(bilinear) + N²ψ(Z) shows X_Z, F₁ ∈ Z[Z],
`X_Z ≡ X₁` and `F₁ ≡ w₁ (mod M)`, `Q(X_Z) = F₁(Z)²`, F₁ > 0, and every non-constant coefficient of F₁
is divisible by w₀M. By Dirichlet pick a prime λ ≡ μ⁻¹ (mod M) with λ > λ₁, λ ∤ N and λ larger than
the finitely many constants named below. Then λX_Z ∈ C for all Z. Put `G₁(Z) = G(λX_Z) ∈ Z[Z]`.
Step 5 (sector). Y ↦ arg ψ₁₂(Y) is continuous on R² ∖ 0 and arg ψ₁₂(Y°) = arg X₁ ∈ S₁, so there is
an open cone Γ ∋ Y° with arg ψ₁₂(Γ) ⊂ S₁. Let B₀ be a closed box inside Γ. For T large and
Z ∈ TB₀, Y_Z ∈ Γ, so λX_Z ∈ S, and `|λX_Z| ≥ c_ψ|Y_Z|²/k₀ > R`.
Step 6 (local densities). For a prime ℓ let ρ_ℓ be the proportion of Z mod ℓ that are *good at ℓ*:
not (ℓ | F₁(Z) and ℓ | G₁(Z)), and, for ℓ = λ, `λ ∤ F₁(Z)∏H_i(X_Z)`.
ℓ | M: F₁ ≡ w₁ ≢ 0, ρ_ℓ = 1. ℓ | k₀, ℓ ∤ M: then ℓ | w₀, so F₁ ≡ w₁ ≢ 0 (mod ℓ), ρ_ℓ = 1.
ℓ ∤ N: Z ↦ Y_Z is a bijection mod ℓ, ℓ ∤ k₀w₀, so ℓ | F₁ ⇔ ℓ | Q(Y_Z); ℓ ≥ 3 and Q mod ℓ is a
nondegenerate form, vanishing on ≤ 2ℓ − 1 points, so ρ_ℓ ≥ 1 − (2ℓ−1)/ℓ² > 0. Moreover, for ℓ ∤ N
outside a finite set, ρ_ℓ ≥ 1 − (4 deg G + 1)/ℓ²: the zeros of Q(Y) mod ℓ are 0 or two lines F_ℓY_ℓ
(ℓ split), Y_ℓ the reduction of an isotropic vector V ∈ O_K² (K = Q(√D)) at a prime 𝔩 | ℓ; on such a
line `ψ₁₂(tY_ℓ) = −t²β₀(Y_ℓ)Y_ℓ` with β₀(Y_ℓ) ≢ 0 (else ℓ | w₀), so G₁ restricts to
`t ↦ G(−λt²β₀(Y_ℓ)Y_ℓ/k₀)`, which is ≢ 0 mod 𝔩 once 𝔩 does not divide the nonzero (as Q ∤ G, G does
not vanish on the isotropic line KV) top coefficient `G_j(V) ≠ 0` of s ↦ G(sV); then it has
≤ 2 deg G zeros t.
ℓ = λ: λ ∤ N, bijection again; bad Y_Z have Q(Y_Z) ≡ 0 (≤ 2λ − 1 points) or `H_i(ψ₁₂(Y_Z)) ≡ 0`
(H_i∘ψ₁₂ is a nonzero form of degree 2 deg H_i, ψ₁₂ having Zariski-dense image; for λ large it stays
nonzero mod λ and vanishes on ≤ 2 deg H_i·λ points). So ρ_λ ≥ 1 − (2 + 2Σ deg H_i)/λ > 0.
Hence `ρ := ∏_ℓ ρ_ℓ > 0`.
Step 7 (sieve). Write Z = (a, b). F₁ is irreducible in Q[a,b] (an affine image of Q(Y)), its
b²-coefficient is the constant w₀N²Q(0,1)/k₀ ≠ 0, and F₁ ∤ G₁: otherwise G vanishes on
λψ₁₂(isotropic line)/k₀, which is the whole isotropic line KV' (ψ₁₂(tV) = −t²β₀(V)V with β₀(V) ≠ 0
because P₀ is not isotropic), forcing Q | G. So `Res_b(F₁, G₁) =: ℛ(a) ∈ Z[a]` is ≢ 0. Fix L. By CRT
the Z ∈ TB₀ good at all ℓ ≤ L and at λ number `ρ_{≤L}·vol(B₀)T² + O_L(T)` with
ρ_{≤L} ≥ ρ. Z ∈ TB₀ with ℓ | F₁, ℓ | G₁ for some prime ℓ > L, ℓ ≠ λ: for L < ℓ ≤ T, at most
`O((T/ℓ + 1)²)` each (O(1) common zeros mod ℓ by Step 6), total `O(T²/L + T)`; for ℓ > T, ℓ | ℛ(a),
and for each of the O(T) values a with ℛ(a) ≠ 0 there are O(1) such ℓ (|ℛ(a)| ≤ T^{O(1)}), each
leaving ≤ 2 residues of b mod ℓ (F₁(a, ·) mod ℓ has the constant leading coefficient), hence ≤ 2
values in an interval of length O(T) < ℓ; the O(1) roots of ℛ add O(T). So the good Z in TB₀ number
≥ `(ρ − O(1/L))vol(B₀)T² − O_L(T) > 0` for L, then T, large. Any good Z gives X = X_Z, w = F₁(Z):
(1) by Steps 4–5, (2) by Step 4, (3) because no prime divides both F₁(Z) and G₁(Z) (including λ,
since λ ∤ F₁(Z)), (4) by goodness at λ. ∎
*Check.* `scripts/bf2_sieve_check.py` (`data/bf2/sieve_check.txt`): G = u(u−2v+3)(v²+u−1)(u+v)
(G(0,0) = 0, Q ∤ G), H = (u+2v)(3u−v), λ ≤ 200. For Q ∈ {u²+v², u²+uv+v², u²+2v², u²+5v²} and
M ∈ {8, 24, 40, 16, 24, 40} (8, 2D | M), every (square class mod M, octant) pair contains a point
λX with (2)–(4): 0 of 5 568 pairs missing (after enlarging the box for u²+2v², u²+5v²; the first
pass missed 411 pairs, a box effect). Between 50% and 75% of the square classes contain *no*
primitive square point; there every square point P has gcd(u,v) > 1 dividing gcd(Q(P), G(P)),
so R159's direct route (coprimality at P itself) fails and the descent of Lemma 8.3 is needed.

**Theorem 3.2′ ((x,y,z)-families; PROVED, unconditional, any degree).** Let F = (x,y,z) be a
polynomial (x,y,z)-family for Q, δ ∈ N clearing the denominators of x, y, z and of every
coordinate quotient by Q that is a polynomial, and M divisible by 8, 2D and δ. Let
`A_F = {θ : x_top, y_top, z_top > 0 at (cos θ, sin θ)}` (top-degree forms).
(b′) If F is integral at some point of a square class C mod M, then A_F = ∅.
(c′) Hence for every square class C mod M and δ′ > 0 the points of C where F is valid lie, outside a
bounded set, within angle δ′ of the finitely many zero directions of x_top, y_top, z_top.
*Proof.* Integrality of F at P depends only on P mod δ, so F is integral on all of C. Suppose A_F
contains an open arc; take a closed subarc I and S the open sector over a slightly smaller open arc. By
Lemma 3.1 there is R with F valid at every P ∈ C ∩ S, |P| > R. For P ∈ C, n = Q(P) is prime to δ,
so `x(P) = n·x̃(P)` with x̃(P) ∈ Z whenever x = Qx̃ (as in Lemma 8.1).
Shape (0) is impossible by Lemma 8.1 (C ∩ S has points beyond R).
Shape (I), x = Qx̃, `k = ord₀ y = ord₀ z` (Lemma 8.2). Apply Lemma 8.4 with `G = (δy)(δz)`, r = 1,
`H₁ = δy₁` if k = 1 (H₁ = 1 otherwise), and λ₁ ≥ δ, |G(0,0)|. Let P = λX, n = λ²w². F is valid at P.
Since (δy)(λX) = Σ_{j≥k} λ^j(δy_j)(X) and λ ∤ δ, `λ^k | y(P)`, `λ^k | z(P)`, and gcd(w, y(P)z(P)) = 1
by (3).
• k = 0: G(P) ≡ G(0,0) ≢ 0 mod λ, so gcd(n, y(P)z(P)) = 1: a Type I solution for the odd square n,
  contradicting Lemma 8.3(e).
• k = 1: `y(P)/λ ≡ y₁(X)`, `z(P)/λ ≡ z₁(X) = −y₁(X)` (Lemma 8.2) and `x̃(P) ≡ x̃(0,0) = 1/4 (mod λ)`.
  By (4) λ ∤ y₁(X), so λ ∥ y(P), λ ∥ z(P), and Lemma 8.3(a) gives `(−x̃(P)(y(P)/λ)(z(P)/λ)/λ) = −1`.
  But `−x̃(P)(y(P)/λ)(z(P)/λ) ≡ (y₁(X)/2)² ≢ 0 (mod λ)`, a nonzero square: contradiction.
• k ≥ 2: λ² | y(P), z(P), contradicting Lemma 8.3(c).
Shape (II), y = Qỹ, z = Qz̃, `k = ord₀ x`. Apply Lemma 8.4 with G = δx, H₁ = δx₁ if k = 1. Then n | y(P),
n | z(P), λ^k | x(P), gcd(w, x(P)) = 1.
• k = 0: λ ∤ x(P) ≡ x(0,0) ≠ 0: Type II for the odd square n, contradicting Lemma 8.3(e).
• k = 1: λ ∥ x(P) by (4); Lemma 8.3(b) gives `((1 − 4ỹ(P))/λ) = −1`; but ỹ(0,0) = 0 (Lemma 8.2(II),
  x(0,0) = 0), so 1 − 4ỹ(P) ≡ 1 (mod λ): contradiction.
• k ≥ 2: contradicts Lemma 8.3(d).
So A_F = ∅. (c′) follows from (b′) and Lemma 3.1 as in Theorem 3.2(c); no sign dilation is needed,
validity being x, y, z > 0. ∎

**Corollary 3.4′ (PROVED, relative to Hecke as in Cor 3.4).** Cor 3.4 holds verbatim for finite sets 𝔉
of (x,y,z)-families with coordinates in Q[u,v] or Q(u,v): a family with a non-polynomial coordinate
is valid at ≪ X^{1+ε} points of norm ≤ X (Lemma 3.3 applied to that coordinate), and polynomial ones
are handled by Theorem 3.2′(c′). M must be divisible by 8, 2D and the δ's of the polynomial families.
So **no "Fermat + identity" certificate whatsoever** — (x,y,z) or (a,…,f), polynomial or rational in
(u,v) — covers a positive proportion of the primes of any square class mod the joint modulus M.
This closes §4.4(iv) and R159 D6.

**8.5 Remarks and exact scope (O163).**
* *Why R159's route alone does not suffice.* If y(0,0) = 0 (equivalently z(0,0) = 0, Lemma 8.2)
  then gcd(u,v) divides gcd(Q(P), y(P)z(P)) at every point, and in 50–75% of the square classes of
  the tested (Q, M) every square point is imprimitive (check after Lemma 8.4). So "square points with
  gcd(Q(P), y(P)z(P)) = 1" do not exist there. The fix is to use square points λX with λ a prime in
  the forced class mod M, descend by λ or λ² (Lemma 8.3), and use the identities at the origin
  (Lemma 8.2: x̃(0) = 1/4, z₁ = −y₁; resp. ỹ(0) = 0) to show that the Legendre symbol that ET's
  reciprocity argument forces to be −1 for the non-square λw² is in fact +1.
* *Polynomial ET coordinates exist but are not needed.* In the UFD Q[u,v], ET's proof of Prop 2.2 /
  2.6 runs verbatim with polynomial gcds (Q is prime and Q ∤ y′, z′), so every Type I/II-shaped family
  has ET coordinates (a,…,f) ∈ Q[u,v]⁶. They need not be integral where x, y, z are, so Theorem 3.2
  does not apply directly; §8 avoids them and works with the integer solution at each point.
* *Where k ≥ 1 can occur.* Composed one-variable families have k = 0 (Remark after Lemma 8.2), so the
  descent cases concern genuinely two-variable families only, none of which is known (§6). The k ≥ 1
  part of Theorem 3.2′ may therefore be vacuous; it is proved anyway.
* *Same scope as Theorem 3.2 otherwise.* Still not covered: procedures with floor/factorisation in
  (u,v) (§4.4(i)), unbounded families of forms (§4.2), indefinite forms in cusps (§4.3), and
  parametrisations n = N(u,v) other than a positive definite binary quadratic form in the principal
  genus. (For x, y, z with n = Q(u,v)/g, g a fixed integer, apply the theorem to the form Q/g if
  integral; otherwise not covered.) Novelty: folklore-level, like Theorem 3.2; the descent through a
  non-square λw² and the Legendre-symbol evaluation at the origin are the only new ingredients.
* Checks: `bf2_square_patterns.py` (gcd patterns, explains why one-sided coprimality is useless),
  `bf2_pointwise_check.py` (Lemma 8.3, CERTIFIED for n ≤ 12 000), `bf2_sieve_check.py` (Lemma 8.4
  existence, all tested class/octant pairs), `bf2_origin_check.py` (Lemma 8.2 algebra on formal power
  series; sanity check only).
