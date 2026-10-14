# y3_euclid_schur_forcing — ES firing classes are exactly the "Euclidean" classes (Schur–Murty) (O211 (b)/(c))

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
A deterministic way to produce primes in a class a mod m is a *Euclidean proof*: a polynomial F whose prime divisors
(up to finitely many) lie in a subgroup, plus a forcing step. **Schur (1912) / Murty (1988): a Euclidean proof for
primes ≡ a (mod m) exists iff a² ≡ 1 (mod m).** The ES Type II class a = −1 mod 4cd always qualifies — semi-
primitivity of h is precisely "Euclidean class". Type I's class −p mod 4cd qualifies iff 4cd | p² − 1. Can Euclidean
forcing manufacture a prime h ≡ −1 (mod 4cd) dividing p + 4c²d?

## Literature
I. Schur, Sitzungsber. Berlin Math. Ges. 11 (1912) 40–50; M. R. Murty, "Primes in certain arithmetic progressions",
J. Madras Univ. (1988) 161–169; K. Conrad, "Euclidean proofs of Dirichlet's theorem" (expository note); for −1 mod m
the polynomial is Ψ_m, the minimal polynomial of 2cos(2π/m): non-exceptional prime divisors h of Ψ_m(n) are ≡ ±1
(mod m), and ≡ −1 iff (n² − 4 / h) = −1 (the root of unity lives in the norm-1 torus T(F_h)).

## Findings
**Prop E1 (single-integer forcing is the genus layer; PROVED, elementary).** Let G = (ℤ/m)^*, a, b ∈ G. "Every
M ≡ a (mod m) with gcd(M, m) = 1 has a prime factor ≡ b" holds iff a ∉ ⟨G ∖ {b}⟩. If |G| ≥ 3 then G ∖ {b} generates G
(a subgroup containing ≥ |G| − 1 > |G|/2 elements is G), so forcing needs |G| = 2, i.e. m ∈ {3, 4, 6}, a = b = −1.
For Type II (M = p + 4c²d ≡ p mod 4cd, b = −1) this is m = 4, c = d = 1, p ≡ 3 (mod 4): **the only slice on which
a prime-modulus Type II certificate is forced by residues alone is the trivial one** (p + 4 ≡ 3 mod 4 has a prime
factor ≡ 3 mod 4).
**Prop E2 (Euclidean dictionary; PROVED).** Type II fires at a prime h on slice (c, d) iff ∃ n ∈ F_h with
Ψ_{4cd}(n) ≡ 0, ((n² − 4)/h) = −1 and h | p + 4c²d. (h ≡ −1 mod m ⟺ μ_m ⊂ T(F_h) ⟺ some primitive ζ ∈ T, n = ζ + ζ⁻¹.)
So Euclidean forcing produces primes ≡ −1 (mod 4cd) as divisors of Ψ_{4cd}(n), but to fire they must also divide the
prescribed M = p + 4c²d: h | gcd(Ψ_m(n), M) — a common-divisor condition, i.e. B2 (the modulus is part of the
solution). Choosing n with M | Ψ_m(n) requires M's prime factors to be ≡ ±1 already (circular).
**Prop E3 (joint forcing across slices; PROVED in the residue-only class).** For a finite slice set S and residue
data only (each M_s known mod m_s and mod finitely many auxiliary primes), there is no forcing: by CRT plus Dirichlet one
can realise M_s with all prime factors ≢ −1 (mod m_s) simultaneously, unless some |G_s| = 2. (This is POINTWISE_SIZE
Thm M / B1 in the language of prime-factor classes.)

## Barrier screen
B1 (E3), B2 (E2), T1: at n = m², E1's trivial slice is unavailable (m² + 4 ≡ 1 mod 4), consistent. B4: Euclidean
forcing is a pigeonhole on prime-factor classes and inherits LONGSHOT_PIGEONHOLE Thm 2.2.

## Cheap numerics
Not needed beyond y3_census (E1 is a group-theory statement; E2 is checked implicitly by y3_gauss check (2)/(4)).

## Assessment
COLLAPSES (PROVED): residue forcing lives only in |G| = 2 (the genus layer, again gcd = 2 as in TORSION_FIRING
Thm 3.1). By-product (Assessment, plausibly new as phrasing): **ES firing classes are exactly Schur–Murty
Euclidean classes**; Type I's class is Euclidean iff 4cd | p² − 1. This explains why semi-primitivity is the
natural ES condition (Euclidean = self-inverse class = Frobenius is complex conjugation on ℚ(ζ_m)), but Euclid's
argument produces primes, not divisors of a prescribed integer.
