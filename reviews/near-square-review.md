# R225 — hostile review of O221 (NEAR_SQUARE.md, checkpoint 1)

Reviewer: R225 side agent (branch side-agent/review-near-square, merged side-agent/near-square at review start).
From-scratch scripts: `scripts/review_r225_*.py`. ES is not solved; nothing below changes that.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 (Type I witness (−4d/n) = −1) | SOUND |
| Lemma 1.3 (Type II witness (f/n) = −1; (de/n) under gcd) | SOUND |
| Prop 1.4 (Hecke reading) | SOUND-AFTER-REPAIRS (minor: the "does not factor through N(π)" clause is unproved) |
| Thm 2.2 (no escaping families for k > 0) | SOUND (for ET-parametrised families; wording repairs) |
| Lemma 2.3 (Z_k^□ ≠ ∅ ⟺ k ≡ 0, 1, 5 mod 8) | SOUND |

## Claim-by-claim

### Lemmas 1.1, 1.3 (witness dictionary)
Re-derived independently.
* 1.1: ef = 4a²d + 1 ⇒ f odd, every q | f has q ∤ 2ad and (2a)²d ≡ −1, so −d ≡ (2a)⁻² is a square mod q:
  Jacobi (−d/f) = 1. The Kronecker symbol χ = (−4d/·) is a character mod 4d (−4d ≡ 0 mod 4) with χ(−1) = −1 and
  χ(f) = (−d/f) for odd f > 0. 4acd = n + f ⇒ f ≡ −n (mod 4d) ⇒ 1 = χ(f) = −χ(n). No gcd hypothesis needed
  (gcd(n, d) = 1 follows since f is prime to d). Correct.
* 1.3: (2.21) ⇒ −dn ≡ (2c)⁻² mod every q | f, so (−dn/f) = 1; f = 4acd − 1 ≡ −1 (mod 4d) ⇒ (−d/f) = χ(−1) = −1 ⇒
  (n/f) = −1 = (f/n) by reciprocity (n ≡ 1 mod 4, both odd positive). The (de/n) clause: ef ≡ 4a²d (mod n), and
  gcd(e, n) = 1 follows from gcd(n, 2ad) = 1. Correct; the n = 21 counterexample to the unconditional form checks.
* From scratch (`scripts/review_r225_witness.py 400`): enumerates ALL N-points of Σᴵ_n (all odd n < 400) and Σᴵᴵ_n
  (n ≡ 1 mod 4, n < 400) in BOTH orientations (a ≤ b by enumeration with acd ≤ n, a > b via ET's reflections):
  8 501 Type I and 1 034 Type II points, 0 failures of (−4d/n) = −1, (f/n) = −1, (de/n) = −1 [gcd case]. Odd
  squares produce no points (consistent with ET Prop 1.6).

### Prop 1.4
The identity (D(m)/n) = (D(−√−k)/π)_K is immediate (ℤ[√−k]/(π) ≅ ℤ/n because N(π) = n is prime, so the
non-maximality of ℤ[√−k] is harmless; denominators of D must be prime to n — implicit). The second sentence
("if D(−√−k) ∉ ℚ·K^{×2} it … does **not** factor through N(π) = n") is asserted, not proved: the symbol is a
Hecke character of K that is not of the form ψ∘N on *all* ideals, but the claim concerns its restriction to the
thin set of principal primes (m + √−k), m in a class, and "does not factor through n" on that set needs a
Chebotarev-type argument (e.g. in K(√α, √q₁, …)) for primes of the special shape m² + k — which is a
Bunyakovsky-type statement. Not used anywhere downstream (Thm 2.2 proves the algebraic statement; Thm 3.4 needs no
escape hypothesis), so MINOR.

### Thm 2.2 (k > 0: no escaping families)
Re-derived every shape by hand (independently of the text), then checked the key eliminations with sympy
(`scripts/review_r225_shapes.py`, Gröbner bases; `scripts/review_r225_shapes2.py`, generic branches).
Degrees: ET Lemma 2.8 (checked against the PDF, sources/elsholtz-tao-1107.1010.pdf p. 15: n/4 < acd ≤ 3n/4 for
Type I, n/4 < acde ≤ n for Type II, both under a ≤ b) ⇒ deg acd = 2, resp. deg acde = 2. Normalisation a ≤ b via ET's
reflections is legitimate (Type I keeps d; Type II f ↦ f′ = (4c²dn + 1)/f with ff′ ≡ 1 mod n, so (f/n) = (f′/n)).
Type I (d non-constant), my derivations:
* (0,0,2): f = (Λ−1)m² + Λu m + Λv − k; f | am² + (ak + c) (no m-term): deg f = 2 ⇒ u = 0; deg f = 1 ⇒ real root
  of a positive definite quadratic, impossible; deg f = 0 ⇒ Λ = 1, Λu = 0. Agrees (sympy: the only branch has u = 0).
* (1,0,1), Λ = 1: m₀ = (rs − k)/(r + s) with r + s < 0; λ_a(m₀ − r)(m₀² + k) = −c < 0 ⇒ m₀ < r ⟺ k < −r². Agrees.
  Λ > 1: with b = λ_a(m − ρ)/(Λ − 1) I get α = ρ − r, β = k + ρ² − ρr, s = −(Λ−1)α/Λ − r and the f-constant equation
  (Λ − 1)(k + ρ²) + r² + k = 0 — exactly the text's identity; impossible for k > 0. (The constant term of na + c is
  not even needed.)
* (0,1,1): Λ > 1 is impossible already by degrees (e = (4a²d + 1)/f with deg(4a²d + 1) = 1 < 2 = deg f); the text's
  "k = −r²" is also correct (I re-derived it: k(a + μ) = −μΛr² and μΛ = a + μ). Λ = 1: sympy gives k = −s² − 1/e < 0
  (another form of the text's k < −r²).
Type II (witness f): deg e = 2 ⇒ f constant ✓. deg e = 1: f linear with real root m₁; n + 4a²d at m₁ is
m₁² + k + 4dλ²(m₁ − r)² (a linear), m₁² + k + 4a²d (c linear), m₁² + k + a/c (d linear) — all > 0 ✓.
deg e = 0: (0,0,2): m-coefficient gives 4aλu(ce − a) = 4aλu·b = 0 ⇒ u = 0 ✓; (0,1,1): comparing m², m, 1:
eΛ = 1, −(r + s) = 4a²λ_d, −e = k + s² ✓; (1,1,0): RHS m² + k + 4dλ_a²(m − r)² > 0 on ℝ, LHS e·f with f(r) = −1 < 0 ✓;
(1,0,1), (2,0,0): degree mismatch (3, 4 vs 2) ✓; (0,2,0): f = (n + 4a²d)/e ≡ const ✓. All ten Type II and six
Type I distributions are covered. The passage from "D ≡ D₀ (mod n), D₀ ∈ ℚ" to "class avoids Z_k^□" is fine (if
q·D ≡ p (mod n) then (D/n) = (pq/n) whenever (D/n) ≠ 0; near a point of Z_k^□ the Jacobi symbol (pq/n(m)) is
+1 or 0, never −1, using n ≡ 1 mod 8 and n a square mod every odd prime of pq).
Also checked the report's Aurifeuillean example (k = 1, a = (m² + m + 2)/4, b = (m² − m + 2)/4, c = 1, d = 2,
e = (m² + 2)/2, f = m² + 2m + 3): all of (2.1)–(2.9) hold identically; witness (−8/n) = −1 for n ≡ 5 (mod 8) ✓.

### Lemma 2.3
Re-derived: ((k − 1)/2)² + k = ((k + 1)/2)²; at 2, m² + k ≡ 1 (mod 8) with m² ∈ {0, 1, 4} mod 8 is solvable iff
k ≡ 0, 1, 5 (mod 8), with the stated m-classes. The parenthetical (other k: n ≢ 1 mod 8, covered by Mordell/the
mod-8 identities) is correct. SOUND. Note: the witness Z_k^□ points produced at odd ℓ | (k + 1) are non-unit squares;
this is harmless (the symbol is then 0 ≠ −1) but the summary's "local square" and §2's "(Ẑ^odd)²" should be
stated as the same set ("square in ℤ_ℓ for every ℓ, unit square at 2").
