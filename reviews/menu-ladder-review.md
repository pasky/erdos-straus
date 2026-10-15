# Review R255 of O245 (MENU_LADDER.md, memos BRAINSTORM/z18_*) — hostile review

Reviewer: R255 side agent (branch side-agent/review-menu-ladder, merged side-agent/menu-ladder at 7ecab42c).
From-scratch scripts: `scripts/review_r255_*.py`. ES is not solved; nothing below changes that.

## Summary verdicts (filled in progressively)

| claim | verdict |
|---|---|
| Prop 1.1 (μ = 0 ∈ Ster iff θ(θ−1) ∈ (A⊗ℚ₂)^{×2}) | SOUND |
| Computation 1.2 (D = 2…10, six (c₀, k)) | SOUND (independently reproduced, different method) |
| Lemma 2.1 (specialisation) | SOUND |
| Lemma 2.2 (normal form) | SOUND |
| Lemma 2.3 (real place) | SOUND-AFTER-REPAIRS (minor: t = t′ case; label of consequence (ii)) |
| Theorem 4.1 (rung 2, Type II) | SOUND (shape analysis redone; from-scratch exhaustive-per-(a,b) search, 0 violations; negative control fires) |

## Claim-by-claim

### Prop 1.1 — SOUND
Re-derived against MENU_STERILITY Theorem A's definition of Ster(φ).
* φ = c₀Y^D + k is separable (c₀k ≠ 0), positive leading coefficient: Theorem A applies.
* (i): φ(Y*) = c₀ + k = 4^J is an ℓ-adic unit for ℓ odd; φ(Y*) = k ≡ 1 (8) in ℤ₂. ✓
* (ii) ⇒: γ(1 − θ) ∈ (A⊗ℚ_ℓ)^{×2} for all odd ℓ means, in each component field K, a local square at all places above
  odd primes, i.e. all finite places but finitely many. If it were not a square, K(√·)/K would be a quadratic extension with
  a positive density of inert primes (Chebotarev) — contradiction. So γ ∈ (1 − θ)A^{×2} (1 − θ is a unit of A since
  φ(1) = 4^J ≠ 0). ✓
* Real places: D even — none; D odd — the single real root −(k/c₀)^{1/D} < 0, where 1 − θ > 1. So every γ ∈ (1 − θ)A^{×2}
  is totally positive, and total positivity imposes nothing extra. ✓
* At ℓ = 2: γ(0 − θ) ∈ (1 − θ)(−θ)A^{×2}, so (ii) at 2 ⟺ θ(θ − 1) ∈ (A⊗ℚ₂)^{×2} (θ is a unit as φ(0) = k ≠ 0). ✓
* ⇐ with γ = 1 − θ. ✓   D = 1: θ(θ − 1) = k·4^J/c₀², a 2-adic square iff k ≡ 1 (8). ✓
* "Reading": for odd D the x − θ map J(ℚ₂)/2J(ℚ₂) → (A⊗ℚ₂)^×/□ is injective (odd-degree model), and the image of
  P₁ − P₀ is (1 − θ)/(−θ) ≡ θ(θ − 1) mod squares, so the [P₁ − P₀] ∈ 2J(ℚ₂) reading is correct. The heuristic sentence
  has a wrong formula (D1 below).
* Hand check D = 2, c₀ = 15 re-done: (−7)² = 49 ≡ −15 (mod 64) so σ ≡ −7 (mod 32) is consistent; v₂(1 + σ) = 1,
  v₂(1 − σ) = 3, sum 4 = v₂(1 − σ²) = v₂(16). ✓

### Computation 1.2 — SOUND (CERTIFIED label acceptable)
`scripts/review_r255_descent.py` uses a method independent of the author's `nfislocalpower`: β is a square in K_𝔭 iff
β is a global square (nffactor of x² − β) or 𝔭 splits in K(√β)/K (`rnfidealprimedec`, two primes above 𝔭). The integral
representative c₀²·θ(θ − 1) = η(η − c₀) (η = c₀θ, monic model) is used. In all 6 × 9 cases φ is irreducible over ℚ.
Output (per prime above 2): every D ∈ 2…10 for every pair has at least one NS; the square components are exactly the ones
the author reports (D = 9: one sq component for all six pairs; D = 4: one sq for (63,1), (31,33), (7,57)); D = 1 is
square for all six (Schinzel). Full agreement with Computation 1.2.

### Lemma 2.1 — SOUND
R = R₁/N. Odd ℓ^e ∥ N: on s/D ≡ 0 (mod ord_{ℓ^e} 2), Y ≡ 1 (ℓ^e), so R₁(Y) ≡ R₁(1); 2^e ∥ N: for s/D ≥ e, Y ≡ 0 (2^e).
Sufficiency and necessity both follow (the class s ≡ 0 (L), s ≥ s₀ contains s with s/D divisible by any given order and
arbitrarily large). Only classes s ≡ 0 (mod L) have μ = 0 in their closure, so "clopen neighbourhood" = such a class. ✓

### Lemma 2.2 — SOUND
1/(abd) + 1/(acdn) + 1/(bcdn) = (cn + a + b)/(abcdn) = 4/n ⟺ cn + a + b = 4abcd. With m = 4abd − n: a + b = c·m. ✓
With a = λ, σ = c/λ (a polynomial in general), T = 4λ²d, T′ = m: b = cm − λ = λ(σT′ − 1), 4abd = T(σT′ − 1) = n + T′, so
n = σTT′ − T − T′; f = 4acd − 1 = σT − 1. Converse: d := T/(4λ²), c := σλ, b := λ(σT′ − 1) satisfies the relation. ✓
(Wording: "gives a family" means a polynomial identity; integrality/positivity of b (needs σT′ > 1 eventually) is separate.)

### Lemma 2.3 — SOUND-AFTER-REPAIRS (minor)
n(t) = −T′(t) at T(t) = 0 and n(t′) = −T(t′) at T′(t′) = 0 are immediate from n = σTT′ − T − T′. T = 4λ²d and T′ = m =
(a + b)/c have positive leading coefficients. Largest real root t* of TT′ (say of T): T′(t*) ≥ 0, so n(t*) ≤ 0; for even D
(n > 0 on ℝ) impossible ⇒ no real roots. For odd D, n is increasing, so t* ≤ the real root of n. ✓
Consequence (i), odd D: with roots t ≠ t′, n(t) and n(t′) have signs inconsistent with monotonicity ✓; the case t = t′
(then t is the real root of n) is not addressed — see D2. Consequence (ii): for even D it is immediate from the lemma (m
linear has a real root); for odd D it is only grid EVIDENCE but sits inside a "PROVED" lemma — see D3.

### Theorem 4.1 — SOUND
Re-derived independently.
* m = 4abd − n = (a + b)/c, lc(m) > 0. deg(abd) < 2 ⇒ lc(m) = −c₀ < 0 ✗. deg(abd) > 2 ⇒ deg a + deg b + deg d =
  max(deg a, deg b) − deg c, so (say deg a ≥ deg b) b, c, d are constants and a(4bd − 1/c) = n + b/c with deg a > 2 forces
  4bcd = 1 and n = −b/c ✗. So deg(abd) = 2, deg m ≤ 2. ✓
* Key identity (not stated by the author, but it is what makes "witness ≡ constant" meaningful and handles the a ↔ b
  mirror shapes): (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1 ≡ 1 (mod n). Hence f is a unit mod n, and f is
  ≡ a constant iff 4bcd − 1 is — so the reduction "up to a ↔ b" is legitimate (D4).
* deg m = 2 ⇒ max(deg a, deg b) ≥ 2 + deg c, so shape (2,0,0), c constant; a(4bcd − 1) = cn + b gives
  f ≡ 4bcd/(4bcd − 1) − 1 = 1/(4bcd − 1) (mod n). ✓
* deg m ≤ 1: (0,0,2) c, m constant, f ≡ cm/b − 1 ✓; (2,0,0) m constant ⇒ f ≡ const ✓, m linear ⇒ −4b²d = n(Y₀) > 0 ✗ ✓;
  (1,1,0) ✓; (1,0,1) ✓ (each uses n > 0 on ℝ, i.e. c₀, k > 0, at a rational real root). The list of (deg a, deg b, deg d)
  with sum 2 up to a ↔ b is complete. ✓
* Final step: f − f₀ = n·h in ℚ[Y]; clearing denominators, (f(Y)/n(Y)) = product of fixed Jacobi symbols (q/n(Y)), q ∈
  {−1, 2, odd primes}; near μ = 0, n ≡ 1 (8) and n ≡ 4^J mod every fixed odd q, so each symbol is +1 (reciprocity), against
  the Type II witness value −1 (NEAR_SQUARE Lemma 1.3; f₀ ≠ 0 by the key identity). ✓
* `scripts/review_r255_rung2.py` (from scratch; for each (a, b) it finds ALL (c, d) ∈ ℚ[Y]: m runs over positive multiples of
  monic divisors of a + b, the multiple forced by 4ab | n + m): (15,1) deg a, b ≤ 2, |coeff| ≤ 2, lc ∈ {1,2}, scalars
  {1, 2, 1/2, 3, 1/3, 1/4, 4}: 2156 families, shapes only (0,0,·,2,0), (2,0,·,0,2), (2,0,2,0,0) and mirrors; (3,1) deg a ≤ 3,
  deg b ≤ 1: 1372; (7,9) deg a, b ≤ 3, |coeff| ≤ 1: 588. **0 violations** (deg(abd) = 2 always, f mod n constant always).
  Negative control n = Y² − 3 (indefinite): 3710 of 8414 families have non-constant witness, shapes (1,1,·), (1,0,1), …
  appear — so the search can detect escapes and positivity is indeed the operative hypothesis.

## Defects

1. (MINOR) §1 "Heuristic" line: "J(ℚ₂)/2J(ℚ₂) has order ≈ 2^{g + #J[2](ℚ₂)}" is wrong. The correct formula is
   #J(ℚ₂)/2J(ℚ₂) = #J(ℚ₂)[2] · 2^g (since |2|₂^{−g} = 2^g). Also at D = 2 the curve is a conic (g = 0, trivial Jacobian),
   so the "J" reading does not apply literally there (even-degree model; the obstruction is the x − θ class of P₁ vs P₀
   in A^×/A^{×2}ℚ₂^×-type quotient). Repair: correct the formula and say "Heuristic (D odd)".

2. (MINOR) Lemma 2.3 consequence (i), odd D: the case t = t′ (common root, then the real root of n) is omitted. Repair: it
   would make −(k/c₀)^{1/D} rational, i.e. k = gu^D, c₀ = gv^D; then g(u^D + v^D) = 4^J with g, u, v odd and D odd gives
   u^D + v^D = (u + v)·(odd) = 2^{2J}/g ⇒ the odd cofactor is 1 ⇒ u = v = 1 ⇒ 2g = 4^J, impossible for odd g. (Or simply
   restrict (i) to the standing hypotheses and add this line.)
3. (MINOR) Lemma 2.3 consequence (ii) is labelled under "PROVED" but for odd D it is only the grid count (EVIDENCE); for
   even D it is a one-line corollary of the lemma (m linear has a real root), which makes the D = 4 sentence about
   b = Y² + pY + q redundant. Repair: "(ii) for even D PROVED (m linear has a real root); for odd D EVIDENCE (grid)".
4. (MINOR) Theorem 4.1 proof: "the four shapes up to a ↔ b" silently uses that the witness is not a ↔ b symmetric. Repair:
   add the identity (4acd − 1)(4bcd − 1) = 4c²dn + 1, so f ≡ const ⟺ 4bcd − 1 ≡ const (mod n); it also shows f₀ ≠ 0.
