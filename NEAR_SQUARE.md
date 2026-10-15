# NEAR_SQUARE — T1 deformed to polynomially-near squares p = m² + k (task O221, spark relay Y10)

Status: work in progress (O221). **ES is not solved here, nor any infinite case of it unless explicitly stated with a
complete proof.** Labels as in DISCOVERIES.md. Builds on THREE_SQUARES.md Lemma 1.4 (R224), ET §10 (Prop 1.9),
STERILE_STEER Prop 3.1, POINTWISE_BINARYFORM (J)3. Memos BRAINSTORM/y10_*.md, scripts `scripts/ns_*`.

Notation: n = n(m) = m² + k, k ∈ ℤ fixed (k < 0 allowed: "p = m² − j"). ET coordinates (a, …, f) as in ET §2
(Type I: 4abd = ne + 1, ce = a + b, 4acd = n + f, ef = 4a²d + 1, n² + 4c²d = f(4bcd − n); Type II: 4abd = n + e,
ce = a + b, 4acd = f + 1, ef = n + 4a²d). A *polynomial family* on a class C = {m ≡ m₀ mod M} is a choice of
(a, …, f) ∈ ℚ[m]⁶ on Σ_{n(m)}, giving N-points for all large m ∈ C (ET's notion, with the parameter m in place of n).
Z_k := {m ∈ Ẑ : m² + k ∈ S}, S ⊂ Ẑ the sterile set (STERILE_STEER Prop 3.1); Z_k ⊇ {m : m² + k ∈ (Ẑ^odd)²}.

## 0. Iteration log
(I1) Lemma 1.4 (T1-type levels) says what is *forbidden* on p = m² + k. Goal (c) asks what is *possible*: ET §10 for
linear families has a final case killed by "p² + 4c²d is irreducible over ℝ". In the variable m the quartic
(m² + k)² + 4c²d can split over ℚ (Sophie Germain / Aurifeuille): first new shape found, but it lives only on
m-classes where n is a non-square for a fixed character — Lemma 1.1 below explains why (the T1 obstruction survives
any family with a constant gcd-parameter d).

## 1. The Jacobi constraint of a Type I solution (PROVED)

**Lemma 1.1.** Let n be odd and (a, …, f) an N-point of Σᴵ_n with gcd(f, 2cd) = 1 (automatic if n = p is a prime,
p > 4cd... see proof). Then (−4d / n) = −1 (Kronecker symbol).
*Proof.* From n² + 4c²d = f(4bcd − n): every prime q | f has q ∤ 2cdn (q | n would give q | 4c²d), so −d ≡ (n/2c)²
(mod q) and the Jacobi symbol (−d/f) = 1. As f is odd and positive, (−d/f) = (−4d/f) = χ(f) with χ = (−4d/·) a
character mod 4d, odd (χ(−1) = sign(−4d) = −1). From 4acd = n + f, f ≡ −n (mod 4d), so 1 = χ(−n) = −χ(n). For n = p
prime: a common prime of f and 2cd divides n + f − f = n (n odd, so not 2, and f is odd as n + f ≡ 0 mod 4), hence is
p, impossible since cd ≤ acd < n. ∎
This is ET Prop 1.6's mechanism in its bare form (for a square n, χ(n) = +1: contradiction). Consequences:
* (Cor 1.2) A Type I polynomial family whose d is a constant is valid only on m-classes where the fixed character
  (−4d/·) takes the value −1 at m² + k; such a class contains no m ∈ Ẑ with m² + k a square in ℤ_ℓ for all ℓ | 2d,
  in particular it is disjoint from {m : m² + k ∈ (Ẑ^odd)²}.
* The only escape is a *growing* d (H-A: moving modulus): (−4d(m)/n(m)) is then a "polynomial Jacobi symbol", which
  by reciprocity becomes a character *of m* (not of n), e.g. d = (m − r)/g gives (n(r)/·)-type characters of m.

**Lemma 1.3 (Type II analogue; PROVED).** Let n ≡ 1 (mod 4) and (a, …, f) an N-point of Σᴵᴵ_n with gcd(f, 2dn) = 1
(automatic for n = p prime). Then (de / n) = −1.
*Proof.* (2.21): 4c²dn + 1 = f(4bcd − 1), so for q | f, −dn ≡ (2c)⁻² is a square: (−dn / f) = 1. f = 4acd − 1 ≡ −1
(mod 4d), so (−d/f) = (−4d/f) = χ_{−4d}(−1) = −1, hence (n/f) = −1. Reciprocity with f ≡ 3 (4), n ≡ 1 (4):
(f/n) = −1. From ef = n + 4a²d, f ≡ 4a²d·e⁻¹ (mod n) (gcd(e, n) = 1 as e | n + 4a²d and gcd(n, 2ad) = 1), so
(de/n) = (f/n) = −1. ∎
So every Type I/II solution of an n ≡ 1 (4) carries a *witness* D (D = d for Type I, D = de for Type II) with
(D/n) = −1 — the analogue of χ = −1 for five-slice words. (Check: `scripts/ns_witness_check.py`.)

**Prop 1.4 (Hecke-character reading of polynomial witnesses; PROVED, elementary).** Let n = m² + k be a prime with
k > 0, K = ℚ(√−k), π = m + √−k (so n = N(π) and ℤ/n ≅ O_K/π when π is a prime of degree one). For D ∈ ℤ[m],
(D(m)/n) = (D(−√−k) / π)_K, the quadratic residue symbol of K. If D is constant this factors through the norm
(it is (D/n)); if D(−√−k) ∉ ℚ·K^{×2} it is (by quadratic reciprocity in K) a ray-class character of the principal
ideal (m + √−k), which does **not** factor through N(π) = n.
*Proof.* m ≡ −√−k (mod π). ∎
Reading: T1 (k = 0) is the degenerate case where √−k = 0 and every polynomial witness is rational. For k ≠ 0 the
T1 obstruction (a fixed character of n) disappears for families whose witness D is non-constant: the witness can
use the "imaginary direction" of ℚ(√−k), which no congruence condition on n sees.

## 2. Classification of polynomial families on n = m² + k (ET §10 in the variable m)

Definition. A *Type I (II) polynomial family* for n = m² + k on the class C is (a, …, f) ∈ ℚ[m]⁶ lying on Σᴵ_{n(m)}
(Σᴵᴵ_{n(m)}) identically, with positive integer values at all large m ∈ C. (ET's reduction from (x, y, z) ∈ ℚ[m]³
to such parameters needs n(m) prime for infinitely many m ∈ C — Bunyakovsky — so we take the parametrised form as the
definition.) Its *witness* is D = d (Type I) or D = de (Type II); by Lemmas 1.1/1.3, (D(m)/n(m)) = −1 on C.
The family *escapes* if D mod (m² + k) has a non-zero m-coefficient, i.e. D(−√−k) ∉ ℚ (Prop 1.4); otherwise
(D(m)/n) is a fixed character ψ(n) and C avoids Z_k^□ := {m ∈ Ẑ : m² + k ∈ (Ẑ^odd)²}.
Degrees: by ET Lemma 2.8, deg a + deg c + deg d = 2 (Type I), deg a + deg c + deg d + deg e = 2 (Type II).
Charts: Type I: f = 4acd − n, b = (na + c)/f, e = (4a²d + 1)/f; Type II: f = 4acd − 1, e = (n + 4a²d)/f, b = ce − a.

**Theorem 2.2 (no escaping families above the squares; PROVED).** Let k > 0. Every Type I or Type II polynomial family
for n = m² + k is non-escaping: its witness satisfies (D(m)/n(m)) = ψ(n(m)) for a fixed Kronecker character ψ, so its
class C contains no m ∈ Ẑ with m² + k ∈ (Ẑ^odd)². Consequently every finite set of polynomial families misses every
m-class around a point of Z_k^□, i.e. misses infinitely many m whenever Z_k^□ ≠ ∅, i.e. (Lemma 2.3) whenever k ≡ 0, 1, 5 (mod 8).
*Proof.* Write Λ for 4 × (product of the leading coefficients of a, c, d) and use real roots r, s, ρ (all rational).
Type I (chart f = 4acd − n, f | na + c, f | 4a²d + 1). If d is constant, Lemma 1.1 gives ψ = (−4d/·). Otherwise
(deg a, deg c, deg d) ∈ {(0,0,2), (1,0,1), (0,1,1)}.
(0,0,2): d = λ(m² + um + v), na + c = a·m² + ak + c has no m-term. If deg f = 2, f ∝ na + c, so f has no m-term,
u = 0 and d ≡ const (mod n): non-escaping. If deg f = 1 its root m₀ is a real root of a m² + ak + c > 0: impossible.
If deg f = 0 then u = 0.
(1,0,1): a = λ_a(m − r), d = λ_d(m − s). If Λ = 1, f = −(r + s)m + rs − k is linear, needs −(r + s) > 0, and its
root m₀ = (rs − k)/(r + s) must be a root of na + c = λ_a(m² + k)(m − r) + c, so m₀ < r; but with r + s < 0,
m₀ < r ⟺ rs − k > r² + rs ⟺ k < −r², impossible. (Λ = 1, r + s = 0 gives f = −r² − k < 0.) If Λ > 1, f is quadratic
and divides the cubic na + c, so na + c = λ_a(m − ρ)(m² + αm + β) with f = (Λ − 1)(m² + αm + β); comparing
coefficients, α = ρ − r, β = k + ρ² − ρr, s = −(Λ − 1)α/Λ − r, and the constant term of f gives
(Λ − 1)(k + ρ²) = −(r² + k): LHS > 0 > RHS. Impossible.
(0,1,1): c = λ_c(m − r), d = λ_d(m − s), na + c quadratic. Λ > 1: na + c = μf with μ = a/(Λ − 1) > 0; the m- and
constant coefficients force k = −r². Λ = 1: as in (1,0,1), k < −r². Λ = 1, r + s = 0: f < 0.
Type II (chart f = 4acd − 1, f | n + 4a²d). If deg e = 2 then a, c, d are constant and e = (n + 4a²d)/f ≡ 4a²d/f
(mod n): non-escaping. If deg e = 1: f is linear with a real root, but n + 4a²d is positive definite when a or c is
the linear one (a const & d linear: value at the root of f is m₁² + k + a/c > 0; c linear, a, d const or a linear:
n + 4a²d > 0 everywhere) — impossible. If deg e = 0 (deg acd = 2): (a, c, d) with d quadratic forces (linear
coefficient) u(a − ec) = 0 and (quadratic coefficient) a ≠ ec, so u = 0, non-escaping; (a const, c, d linear)
forces k + s² = −e < 0; (a, c linear, d const) has D = de constant; (a, d linear) makes n + 4a²d cubic ≠ e·f;
(a quadratic) makes it quartic. The remaining shapes have d and e constant. In every non-escaping case D ≡ D₀
(mod n) for a rational D₀, and ψ = (D₀'/·) with D₀' the integer numerator–denominator product of D₀. ∎
**Lemma 2.3 (PROVED).** Z_k^□ ≠ ∅ ⟺ k ≡ 0, 1, 5 (mod 8). *Proof.* For odd ℓ, m = (k − 1)/2, w = (k + 1)/2 ∈ ℤ_ℓ
give m² + k = w². At 2, unit squares are 1 + 8ℤ₂ (Hensel), and m² + k ≡ 1 (8) is solvable iff k ≡ 0 (m odd), 1 (4 | m)
or 5 (m ≡ 2 mod 4) (mod 8). CRT. ∎ (For the other k, n = m² + k is never ≡ 1 mod 8 at odd n, so Mordell's classes
already cover all odd n of the family; nothing to do.)

Every impossibility above is the positivity of the binary norm form x² + ky² of ℚ(√−k) at a real point — the
archimedean place (cf. (J)52) — e.g. (Λ − 1)·N(ρ + √−k) + N(r + √−k) = 0. For k < 0 all of them become possible.
EVIDENCE (`scripts/ns_polyfam.py K 3`, roots in ½ℤ ∩ [−3, 3], 16 leading coefficients): 0 escaping families for
k = 1 (and 16, 24: see §7); 80, 161, 263 for k = −8, −15, −24.

## 3. Below the squares: k < 0 (p = m² − j)

**Prop 3.1 (integer T1 points; PROVED, trivial).** Let F be a polynomial family on the class C = {m ≡ g mod L}, L a
multiple of all coefficient denominators of F. If m₀ ∈ ℤ, m₀ ≡ g (mod L) and n(m₀) is an odd perfect square, then
some coordinate of F(m₀) is ≤ 0.
*Proof.* Integrality of a polynomial with denominators dividing L is L-periodic, so F(m₀) ∈ ℤ⁶ lies on Σ_{n(m₀)}; if all
coordinates were positive it would be an N-point of Type I/II for the square n(m₀), contradicting ET Prop 1.6. ∎
So for k < 0 the T1 points of the family (m₀ with m₀² − j = w², finitely many) are *archimedean-adelic* obstructions:
a family can cover the Ẑ-neighbourhood of m₀ only if one of its coordinates has a real root above m₀... more precisely is
non-positive at m₀. Example (`scripts/ns_polyfam.py -8 3`): no family found covers m ≡ 3 (mod 8064), while 8 cover
m ≡ −3, e.g. a = 1, c = (m + 1)/2, d = (m − 1)/2, f = 7, b = (2m² + m − 15)/14, e = (2m − 1)/7 on m ≡ 53 (mod 56)
(c(−3) = −1, d(−3) = −2). The point m₀ and −m₀ give the same n but sit on different sides of the real roots.

**Lemma 3.2 (positivity propagates down to the largest real root of n; PROVED).** Let n(m) ∈ ℝ[m] and let F be a
polynomial family (Type I or II) whose coordinates are positive for all large m. Then every coordinate of F is
positive on (ρ, ∞), where ρ is the largest real root of n (ρ = −∞ if none).
*Proof.* Otherwise let m₁ > ρ be the largest real zero of a coordinate; at m₁ all coordinates are ≥ 0, n(m₁) > 0.
Type I: if a, b or d vanish, 4abd = ne + 1 gives e = −1/n < 0; if c or e vanish, ce = a + b gives a = b = 0, already
excluded; if f vanishes, ef = 4a²d + 1 gives 0 ≥ 1. Type II: if a, b or d vanish, 4abd = n + e gives e = −n < 0; c or
e: a = b = 0 as before; f: ef = n + 4a²d gives 0 > 0. ∎
**Theorem 3.3 (integer T1 points obstruct every polynomial family; PROVED).** Let n(m) ∈ ℤ[m] have positive leading
coefficient and largest real root ρ. If m₀ ∈ ℤ, m₀ > ρ and n(m₀) is an odd perfect square, then no Type I/II polynomial
family is valid on a class C ∋ m₀. Hence every finite set of polynomial families misses all m in some class
m ≡ m₀ (mod L), i.e. infinitely many m.
*Proof.* Lemma 3.2 makes F(m₀) positive; Prop 3.1 makes it an integral point of Σ_{n(m₀)}; ET Prop 1.6. For the
second statement take L = lcm of the moduli of the finitely many families. ∎
Remarks. (i) For n = qt + r this recovers ET/Schinzel's "square classes are not solvable by polynomials" (t₀ with
qt₀ + r = w² lies above the root −r/q). (ii) For n = m² + k, k > 0, ρ = −∞, so every integer T1 point obstructs
(subsumed by Thm 2.2). (iii) For k = −j < 0 the T1 points are the m₀ with j = (m₀ − w)(m₀ + w), w odd; m₀ > √j obstructs, −m₀ < −√j does not (there n > 0 but it is the other real component) — matching the
numerics (8 families cover m ≡ −3, none m ≡ 3, for j = 8). (iv) Numerics: max real root over all coordinates of all
families found is 2.818, 3.865, 4.895 < √j = 2.828, 3.873, 4.899 (j = 8, 15, 24).

**Theorem 3.4 (the K-adic square set is sterile for every polynomial family; PROVED).** Let k = −j < 0, j not a square,
K = ℚ(√j), π_m := m − √j (so n(m) = N(π_m)), and
  Z_K⁺ := {m* ∈ Ẑ : π_{m*} is a non-zero square in K_v for every finite place v of K}.
Then no Type I/II polynomial family for n = m² − j has a class C (m ≡ g mod L) whose closure in Ẑ meets Z_K⁺.
(We use the m with gcd(n(m), 2j) = 1; the classes where a prime of 2j divides n are non-primitive or 2-adically trivial.)
*Proof.* Let α := D(√j) ∈ K (D the witness). If α ∈ ℚ the family is non-escaping: (D(m)/n) = ψ(n(m)) for a fixed
Kronecker character ψ, and n(m*) = N(π_{m*}) is a local square everywhere, so ψ(n(m)) ∈ {0, +1} for m ∈ C near m*.
Otherwise, for m ∈ C large with gcd(n, 2j) = 1: (i) the prime ideals dividing (π_m) have degree one and are prime to the index of ℤ[√j] (an inert q dividing π_m would
divide m − √j, impossible; ramified or index primes divide 2j), so
(X/n) = (X/(π_m))_K for X ∈ ℤ (Jacobi symbol of K); (ii) D(m) ≡ α (mod π_m); (iii) by the Hilbert product formula,
(α/(π_m))_K = ∏_{v | 2α∞} (α, π_m)_v (v | π_m cannot divide α, else (D(m)/n) = 0). If m* ∈ Z_K⁺ ∩ closure(C), choose
m ∈ C, m > √j, so close to m* that π_m/π_{m*} is a square in K_v for the finitely many finite v | 2α (squares are
open); then (α, π_m)_v = 1 there, and at the two real places π_m > 0, so (α, π_m)_∞ = 1. Hence (D(m)/n(m)) = +1,
contradicting Lemmas 1.1/1.3. ∎
Remarks. (i) Z_K⁺ ⊊ Z_k^□ (= {m : N(π_m) a local square}): at a split prime ℓ = 𝔩𝔩′ both m − s and m + s (s² = j in ℤ_ℓ)
must be squares (density 1/4 instead of 1/2); at inert and ramified ℓ the conditions agree with Z_k^□ up to the
ramified residue condition. So **below the squares the sterile set of polynomial families shrinks from "n is a local
square" to "π = m − √j is a local square in K"** — T1 deformed is a square *in K*, not in ℚ. (ii) For k > 0 (K imaginary)
the same proof gives only Z_K ⊆ Z_k^□; Thm 2.2 shows the true sterile set is the larger Z_k^□ ∪ (Z_k), because no
escaping family exists: with a complex place there is no sign at ∞ to absorb the positivity constraint. (iii) The
integer T1 point m₀ = 3 (j = 8) lies in Z_K⁺ (3 − 2√2 = (1 − √2)²); m₀ = 4 (j = 15) does not (4 − √15 ∈ 6·K^{×2} is not a
square at 2), but is excluded by Thm 3.3 (size: 4/1 is not a sum of three unit fractions).
EVIDENCE (`scripts/ns_padic_cover.py -8 L /tmp/fam_-8.txt`, all seven ET congruence families with modulus | L plus
the 76 escaping families of `ns_polyfam.py -8 3`): the uncovered m-classes with n ≡ 1 (4) are, at L = 8064 = 2⁷·3²·7,
the 96 classes {m ≡ 3 (8), m ≡ 0 (3), m ≡ 1, 3 (7)}, and at L = 4480 = 2⁷·5·7 the 64 classes {m ≡ 3 (8), m ≡ ±2 (5),
m ≡ 1, 3 (7)}. Z_K⁺ for K = ℚ(√2) predicts exactly: at 2, m − 2√2 ≡ (a + b√2)² mod 4√2 forces a, b odd, i.e. m ≡ 3 (8);
at 3 and 5 (inert) N(π) ≡ □, i.e. m ≡ 0 (3), m ≡ ±2 (5); at 7 = 𝔩𝔩′ (√8 ≡ ±1) both m ∓ 1 squares: m ≡ 3 (7)
(m ≡ 1 (7) is the degenerate 7 | n class). So at these levels the polynomial-sterile set is exactly Z_K⁺ (CONJECTURE in
general: CONJECTURE Y10-S below).

**CONJECTURE Y10-S (sterile set below the squares).** For k = −j < 0, j not a square, an m* ∈ Ẑ (with n(m*) a 2-adic
unit ≡ 1 mod 4) lies in the closure of the class of no polynomial family iff m* ∈ Z_K⁺ or m* is a positive integer T1
point (Thm 3.3). Equivalently: the T1 obstruction for polynomial families on p = m² − j is "π = m − √j is a square in
K", one level finer than the T1 obstruction for congruences ("n = N(π) is a square in ℚ").
Status: Thm 3.3 + Thm 3.4 give "⊇". "⊆" is EVIDENCE at j = 8 for L = 8064 and 4480 (the families found so far have
moduli built from 2, 3, 7, so the test cannot see finer levels); for j = 15, 24 the found families are too thin
(30 % / 16 % of classes uncovered at L = 63360 / 132480), so no test. Consequence if true: ES for n = m² − j holds for every m
outside an Ẑ-neighbourhood of Z_K⁺, i.e. polynomial families do *strictly* better than congruences below the squares
and *exactly as well* above them (Thm 2.2).

## 4. Deterministically clean levels (goal (a))

Convention (THREE_SQUARES Prop 1.3): level t is *odd-clean* at odd n if (−t/r) = +1 for every odd prime r | tn + 1, r ∤ t
(for n = p prime this is (r/p) = +1, so all level-t words have χ = +1 when moreover 2 ∤ tp + 1 or (2/p) = 1).

**Prop 4.1 (classification for quadratic families; PROVED).** Let Q(m) = Am² + Bm + C ∈ ℤ[m], A > 0, Δ = B² − 4AC,
t ≥ 1, E := 4A − tΔ. Identity: 4A(tQ(m) + 1) = t(2Am + B)² + E.
(a) If E = c² is a perfect square, level t is odd-clean at n = Q(m) for every m with gcd(2Am + B, c) = 1 and
gcd(tQ(m) + 1, 2A) = 1 (and then χ = +1 on level t at primes, under the 2-condition above).
(b) If E is not a perfect square and E ≠ −t·□, there is a prime r ∤ 2tAE with (−t/r) = −1 and (E/r) = −1; for every
such r, level t is NOT odd-clean at Q(m) for all m in a residue class mod r (namely tX² ≡ −E, X = 2Am + B). If
E = −t s² (s ≥ 0), tQ + 1 = t(X − s)(X + s)/(4A) is reducible and level t is not odd-clean on a class of m as well.
So "level t is odd-clean along the whole family" ⟺ 4A − tΔ is a perfect square.
*Proof.* (a) r | tQ + 1, r ∤ 2Ac ⇒ tX² ≡ −c² (r), r ∤ X ⇒ −t ≡ (c/X)². (b) r with (−tE/r) = 1 (so tX² ≡ −E is
solvable mod r) and (−t/r) = −1 exist by Dirichlet/Chebotarev in ℚ(√−t, √E) as soon as −t·E and −t are independent
modulo squares, i.e. E ∉ □ ∪ (−t)□. ∎
Examples. Q = m² + k: E = 4(1 + tk): clean ⟺ tk + 1 = □ (THREE_SQUARES Lemma 1.4 is exactly the "if"; this is the
"only if"). Q = 2m² + k: 8(1 + tk) = □ ⟺ tk + 1 = 2□ (k = 1: t = 1, 7, 17, 31, …). Q = m² + m + k: E = 4 + t(4k − 1).
Families p = m² + k·j² with j varying: level t clean ⟺ (c, j) solves the Pell equation c² − tk·j² = 1.
**Per-prime form (PROVED, elementary).** At a single prime p, level t is *T1-type* if tp + 1 = c² + t·m² with gcd(m, c) = 1;
equivalently K := p − m² > 0 satisfies tK + 1 = c². Every prime has the T1-type levels t = K ± 2 (c = K ∓ 1... i.e.
(K − 2)K + 1 = (K − 1)², (K + 2)K + 1 = (K + 1)²) for each m < √p with the gcd condition, and more generally
t = (c² − 1)/K for every square root c of 1 mod K. T1-type ⟺ tp + 1 is primitively represented by the PRINCIPAL form
x² + ty² — while "clean" ⟺ every prime of tp + 1 splits in ℚ(√−t) ⟺ (essentially) primitively represented by SOME form of
discriminant −4t. So T1-type levels are the principal-genus-class part of the clean levels.
EVIDENCE (`scripts/ns_census.c`, all 34 392 primes p ≡ 1 (4) in (10⁵, 10⁶), 5 570 014 ordered words): 432 677 words lie on
clean levels, 356 023 (82 %) of them on T1-type levels; 0 χ = −1 words on either (Lemma 1.4 and Lemma 1.2(a) at scale).

## 5. Hardness beyond the adelic cell (goal (b); EVIDENCE)

Data: `scripts/ns_census.c 100000 1000000` (34 392 primes p ≡ 1 (4)), `scripts/ns_hardness.py census RMAX`. Adelic cell
= (p mod 8, (r/p) for odd r ≤ RMAX, lnr capped); all residuals are within-cell. φ_cl = fraction of words on clean
levels, φ_T1 = on T1-type levels, K0 = p − ⌊√p⌋².
* Within cells (RMAX = 31, 2 048 cells), corr(φ_cl, N₋/N) = −0.57; regression of N₋/N on (φ_cl, φ_T1): slopes −0.78, +0.02.
  **Given exact cleanliness, the T1-type (principal-form) indicator adds nothing.** The R224 coin model is the adelic
  approximation of φ_cl; φ_cl itself is exact (Legendre symbols of all prime factors of tp + 1).
* Archimedean gradient. Residual of N₋/N by K0: −0.019 (K0 = 1, 61 primes), −0.050 ([2, 5)), −0.046 ([5, 10)), −0.042
  ([10, 17)), −0.029 ([17, 30)), −0.015 ([30, 100), 1 828), −0.0067 ([100, 300), 5 344), +0.0035 (≥ 300, 26 414). By
  offset: K0 = 24: −0.153 (36 primes), 16: −0.056, 4: −0.050, 9: −0.013, 1: −0.019, 25: +0.003, 36: +0.019 — ordered by the
  number of small T1-type levels {t : tK0 + 1 = □} (24: t = 1, 2, 5, 7, 12, …; 25, 36: first t = 23, 35).
* About half of the gradient survives removing all words on clean levels: residual of N₋/(N − N_cl): −0.041 ([5, 10)),
  −0.024 ([10, 17)), −0.019 ([17, 30)), −0.0093 ± 0.0014 ([30, 100)), −0.0045 ± 0.0008 ([100, 300)), +0.0022 (≥ 300); K0 = 24:
  −0.068 ± 0.010. So near-squares are depleted of χ = −1 words also on UNclean levels. Mechanism not identified (tried:
  T1-type levels with gcd(m, c) > 1, levels with tK0 + 1 = s·□ for small s where χ = (s/A) — neither is depleted in a
  sample of 800 primes m² + K, K < 30; `/tmp`-only script, not kept). Open (spark S2).
* Hard primes. Of the 17 (J)45 hard primes plus 3361, two are m² − 3 with m ≡ 2 (4): 3361 = 58² − 3 and 1 249 921 =
  1118² − 3 (both with m ≡ ±2 mod 3, 5, 7: adelically next to the T1 point m₀ = 2, n(2) = 1, of the family m² − 3);
  372 121 = 610² + 21. The other 15 sit at generic distance (min(p − m², (m+1)² − p)/√p spread over (0.15, 1)).
  Assessment: hardness is driven by the adelic pattern (square mod small primes) and, *pre-asymptotically*, by
  T1 points of polynomial families: m² − 3 is the cheapest way to be a square mod every small prime simultaneously.
