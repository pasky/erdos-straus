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
