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
