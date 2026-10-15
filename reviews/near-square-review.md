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
| Prop 3.1, Lemma 3.2, Thm 3.3 (positivity propagation, integer T1 points) | SOUND |
| Thm 3.4 (Z_K⁺ sterile, Hilbert reciprocity in ℚ(√j)) | SOUND-AFTER-REPAIRS (proof correct; the closure parenthetical is false) |
| Prop 4.1 (clean levels ⟺ 4A − tΔ = □) | SOUND-AFTER-REPAIRS (two wording gaps in (b)/the "iff") |
| Per-prime form (T1-type = principal-form part) | SOUND (label "roughly" appropriate) |
| j = 8 coverage computation (uncovered = Z_K⁺ at L = 8064, 4480) | SOUND (reproduced with independent code) |
| CONJECTURE Y10-S | correctly labelled; evidence real but thin (2- and 7-adic factors only) |
| Escaping example 4/2801 and its family | SOUND |
| §2 EVIDENCE (0 escaping families for k > 0) | SOUND (reproduced, wider grid) |

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

### Prop 3.1, Lemma 3.2, Thm 3.3
* Lemma 3.2 re-derived: at the largest zero m₁ > ρ of a coordinate all coordinates are ≥ 0 and n(m₁) > 0; the six
  vanishing cases give e = −1/n, a = b = 0, 0 ≥ 1 (Type I) and e = −n, a = b = 0, 0 = n + 4a²d > 0 (Type II). Uses only
  identities (2.1), (2.2), (2.7) / (2.13), (2.14), (2.19), which hold identically in m. Correct. (Coordinates are
  non-zero polynomials because they are positive at large m.)
* Thm 3.3: integer-valued-at-large-t ⇒ integer-valued at all t (binomial basis) is correct and removes Prop 3.1's
  denominator hypothesis; F(m₀) is then an N-point for the odd square n(m₀) (n(m₀) = 1 included: Lemma 1.1 gives
  (−4d/1) = 1 ≠ −1), contradiction. Correct.
* Remark (iii): T1 points j = 8: 3; j = 15: 4, 8; j = 24: 5, 7 — checked. The example family a = 1, c = (m + 1)/2,
  d = (m − 1)/2, f = 7, b = (2m² + m − 15)/14, e = (2m − 1)/7 on m ≡ 53 (56): I verified (2.1)–(2.9) symbolically by
  hand (4acd − n = 7, b = (na + c)/7, e = (4a²d + 1)/7, ce = a + b) and integrality on m ≡ 53 (mod 56); at m = 53:
  (a, b, c, d, e, f) = (1, 404, 27, 26, 15, 7), (x, y, z) = (abdn, acd, bcd) = (29 421 704, 702, 283 608) for n = 2801
  (prime, ≡ 1 mod 4); 4/2801 = 1/29421704 + 1/702 + 1/283608 holds exactly (`scripts/review_r225_kadic.py`). The class
  m ≡ 53 ≡ −3 (mod 56) contains m ≡ −3 (mod 56L) with n ≡ 1 (mod L) for every L: correct ("escape" from congruences).

### Thm 3.4 (Z_K⁺ sterile)
Re-derived step by step:
* (i) For gcd(n(m), 2j) = 1: every q | n splits in K and is prime to the index [O_K : ℤ[√j]] (which divides 2f, j = f²j₀,
  and f | j); q ∤ π_m in ℤ[√j] (coefficient of √j is −1), so (π_m) = ∏𝔮^{v_q(n)} with one prime above each q, and
  ℤ/q^e ≅ O_K/𝔮^e. Hence (X/n) = (X/(π_m))_K for X ∈ ℤ. ✓ (gcd(n, 2j) = 1 is what makes the order harmless.)
* (ii) D̃(m) − D̃(√j) is divisible by m − √j in ℤ[√j][m] evaluated at integer m. ✓  α = 0 ⇒ (m² − j) | D̃ ⇒ (D/n) = 0. ✓
* (iii) For β ∈ O_K and π_m coprime to 2β: (β/(π_m))_K = ∏_{𝔮 | π_m}(β, π_m)_𝔮 = ∏_{v | 2β∞}(β, π_m)_v by the product
  formula (tame symbols at 𝔮 ∤ 2β; trivial symbols at finite v ∤ 2βπ_m). ✓
* Approximation: n(m*) ∈ Ẑ^× (norm of a unit), so integers m ∈ C ℓ-adically close to m* at the finitely many ℓ | 2jgN(α)
  have n(m) coprime to 2jgN(α); unit squares are open in O_{K,v}^×, so π_m is a square in K_v for v | 2αg; m > √j
  makes π_m totally positive. Then (D(m)/n) = (D̃(m)/n)(g/n) = (α/π_m)(g/π_m) = +1. Since π_{m*} is a 2-adic unit
  square, n(m*) is a unit square in ℚ₂, so n(m) ≡ 1 (mod 8) and Lemma 1.1 (as (d/n) = −1) and Lemma 1.3 both apply. ✓
  No escape hypothesis is used. The order ℤ[√j], gcd(n, 2j) = 1 and the denominator g are all handled correctly.
* "Closure": classes are clopen in Ẑ, so "closure(C) meets Z_K⁺" = "C ∋ a point of Z_K⁺"; the uncovered set is closed. ✓
**Defect (see D3):** the parenthetical "(which also contains non-unit square points, e.g. the R-O221 examples
j = 648, m* = 27)" is false. Z_K⁺ ⊂ U := {m ∈ Ẑ : n(m) ∈ Ẑ^×}, and U is closed (each condition ℓ ∤ n(m) is clopen),
so closure(Z_K⁺) ⊂ U; but n(27) = 729 − 648 = 81. Concretely every m ≡ 27 (mod 9) has 81 | m² − 648, so no integer
near 27 is in Z_K⁺'s neighbourhood structure either. (27 − 18√2 = (3 − 3√2)² is a non-unit square; whether 27 is
polynomially sterile is simply not decided by Thm 3.4.)
* Remark (i) re-derived: inert ℓ: x ∈ F_{ℓ²}^× is a square iff N(x) is a square in F_ℓ ✓; ramified odd ℓ | j₀ with
  ℓ ∤ m: π ≡ m (mod 𝔩), so Z_K⁺ adds (m/ℓ) = 1 while N(π) ≡ m² is automatically a square ✓; split: both m ∓ s squares ✓.

### Prop 4.1
* Identity 4A(tQ + 1) = t(2Am + B)² + E: expanded by hand ✓.
* (a) re-derived: for an odd r | tQ + 1, r ∤ t: gcd(tQ + 1, 2A) = 1 gives r ∤ 2A; if r | c then tX² ≡ 0 so r | X,
  contradicting gcd(X, c) = 1; if r | X then r | c, same. So −t ≡ (c/X)² (mod r). ✓ The m² + 8, t = 1, m = 3
  example (X = 6, c = 6; 3 | 18, (−1/3) = −1) shows the exceptional classes are essential ✓.
* (b) re-derived: (−t/r) = (E/r) = −1 ⇒ (−tE/r) = 1 ⇒ tX² ≡ −E solvable, and X = 2Am + B hits it on a class mod r ✓;
  existence of r by Chebotarev in ℚ(√−t, √E) needs −t, E, −tE all non-squares ✓.
  Gap 1 (MINOR): the exceptional case should read "−tE is a perfect square" (equivalently E ∈ −t·ℚ^{×2}), not
  "E = −ts² with s ≥ 0 an integer": e.g. t = 4, E = −1 has −tE = 4 but is not of the form −4s². The reducible-case
  argument works verbatim with rational s.
  Gap 2 (MINOR): the "⟺" sentence quantifies over "m outside the gcd-exceptional classes", which are defined via c
  and so only exist when E = c². State it as: (E = □) ⇒ clean outside the exceptional classes of (a); (E ≠ □) ⇒
  unclean on a full residue class mod r (r ∤ 2tAE), in particular on m with gcd(tQ(m) + 1, 2A) = 1 when that is
  possible (CRT).
  Also: the convention line "for n = p prime this is (r/p) = +1" needs p ≡ 1 (mod 4) ((−t/r) = (p/r) = (r/p)).
* Examples checked: m² + k ⇒ E = 4(1 + tk) ✓; 2m² + k ⇒ 8(1 + tk) = □ ⟺ 1 + tk = 2□, k = 1: t = 1, 7, 17, 31 ✓;
  m² + m + k ⇒ E = 4 + t(4k − 1) ✓; m² + kj² ⇒ Pell c² − tkj² = 1 ✓.
* Per-prime form: tp + 1 − tm² = tK + 1 ✓; t = K ± 2 ✓ ((K ∓ 1)² identities); principal-form reading ✓ (tm² < tp + 1
  forces m < √p). The census "clean" (ns_census.c) also demands (2/p) = +1 when tp + 1 is even, while Prop 4.1 uses
  "odd-clean"; §4's EVIDENCE line should say which definition the 432 677 refers to (it is the census one, incl. 2).

### Family-search numerics (§2 EVIDENCE, §7) — independent search
`scripts/review_r225_famsearch.py K RMAX QMAX [dump]` is a from-scratch search over all 6 + 10 degree shapes with
rational roots p/q (q ≤ QMAX, |p/q| ≤ RMAX), leading coefficients {1,2,3,4,6,8,12}/{1,2,3,4}, constants 1..12, ½, 3/2, ⅓, ¼,
and (unlike ns_polyfam, which uses only products of linear factors) irreducible quadratics λ((m + u)² + v), v > 0.
Results (escaping = witness non-constant mod m² + k):
| k | grid | families found (I / II) | escaping |
|---|---|---|---|
| 1 | roots ⅓ℤ ∩ [−5, 5] | 454 / 4079 | 0 / 0 |
| 9 | roots ⅓ℤ ∩ [−5, 5] | 118 / 4024 | 0 / 0 |
| 5, 8 | roots ½ℤ ∩ [−3, 3] | 268 / 4054, 157 / 4034 | 0 / 0 |
| −8 (control) | roots ½ℤ ∩ [−3, 3] | 1568 / 4093 | 900 / 65 |
So with denominators 3 and roots up to ±5 and irreducible quadratic coordinates, still no escaping family for k > 0,
consistent with Thm 2.2, while the same code finds many for k = −8 (the positive control works). (The k = 1 counts
did not grow from the ½ℤ ∩ [−3, 3] grid to the ⅓ℤ ∩ [−5, 5] grid; most found families are the constant-shape
congruence families and their dilates.)

### j = 8 coverage (Thm 3.4 EVIDENCE, CONJECTURE Y10-S)
`scripts/review_r225_kadic.py 8 L FAMFILE` (from scratch): (1) tests "m − 2√2 is a unit square in ℤ₂[√2] / ℤ_ℓ[√8]"
by brute force (mod 2⁵ in ℤ₂[√2], i.e. beyond the Hensel precision 4√2; mod ℓ for odd ℓ); (2) enumerates all seven ET
Prop 1.9 congruence families with modulus | L (re-implemented from the PDF statement); (3) adds the polynomial
families of a family file whose denominators divide L, computing their integrality classes. Results:
* Local conditions: m ≡ 3 (mod 8) [2-adic], m ≡ 0 (3), m ≡ 3 (7) — as claimed.
* With the author's 76 escaping families (regenerated with ns_polyfam.py −8 3 as *data*; coverage computed by my code)
  plus my 5 661 families: uncovered classes with n ≡ 1 (mod 4) are 96 at L = 8064 (= the 48 Z_K⁺ classes + the 48
  degenerate classes m ≡ 1 (mod 7), 7 | n) and 64 at L = 4480 (32 + 32). Exactly the text's sets. ✓
* With only my own 5 661 families the uncovered set is larger (192 / 128; extra classes such as m ≡ 7 (mod 8)), i.e. my
  grid misses some of the author's families (leading coefficients with denominator 8) — this does not affect the
  claim, but shows the "= Z_K⁺" evidence is sensitive to the family grid: it is a statement about the families found.
* What the evidence actually discriminates: congruence families alone leave every odd m with n a square mod 3, 7
  (Z_k^□); the escaping families remove the 2-adic classes m ≡ 1, 5, 7 (8) and the 7-adic class m ≡ 4 (7) — a factor
  4 · 2 = 8 — and nothing else. Y10-S is a reasonable conjecture; the evidence is two levels built from 2, 3, 5, 7
  at one j. Label CONJECTURE is correct.
