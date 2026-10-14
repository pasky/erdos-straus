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
