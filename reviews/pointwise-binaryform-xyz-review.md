# R163 — hostile review of O163 (POINTWISE_BINARYFORM.md §8, (x,y,z)-families)

Reviewer: R163 (side-agent/review-binaryform-xyz). Reviewed: author branch `side-agent/binaryform-xyz`
(merged into this worktree), §8 and the "(O163 update)" lines in §0, §4.4(iv), §7; author report
`reviews/agent-reports/AGENT_REPORT_O163.md`. ES is not solved; nothing reviewed here proves any case.

Status: IN PROGRESS (written claim by claim).

## Summary verdicts

(filled in below as claims are checked)

## Claim-by-claim

### Lemma 8.1 (shapes) — SOUND

* Q prime in Q[u,v]: a primitive definite form has no rational (indeed no real) linear factor, so it
  is irreducible over Q; Q[u,v] is a UFD. ✓
* `4xyz = Q(xy+yz+zx)` (multiply the identity by Qxyz) ⇒ Q | xyz ⇒ Q divides ≥ 1 coordinate; the
  number of coordinates divisible by Q is 3, 1 or 2, giving (0), (I), (II) up to permutation;
  exhaustive and exclusive. ✓
* Case (0): at a valid P with gcd(n,δ) = 1 (n = Q(P) > 0 since P ≠ 0 at a valid point, x(0,0) = 0),
  `n·x₁(P) = x(P) ∈ Z` and `δx₁(P) ∈ Z` give `x₁(P) ∈ Z`, positive; 1/x₁+1/y₁+1/z₁ ≤ 3 < 4. ✓
* Side remark (used under "modulus hypothesis" below): by Gauss's lemma (Q primitive),
  content(Q·g) = content(g), so the denominators of x/Q are exactly those of x. The extra clause
  "and of x/Q, y/Q, z/Q" in the definition of δ is automatic.

### Lemma 8.2 (origin identities) — SOUND

Re-derived. (I) Multiplying `4/Q = 1/(Qx̃)+1/y+1/z` by Qx̃yz: `4x̃yz = yz + Qx̃(y+z)`, i.e.
`yz(4x̃−1) = Qx̃(y+z)`. 4x̃ = 1 ⇔ y+z = 0 (x̃ ≠ 0), never valid. Otherwise Q prime, Q ∤ y, Q ∤ z ⇒
Q | 4x̃−1 = Qh, and `yzh = x̃(y+z)`, `4yzh = (Qh+1)(y+z)` ✓. x̃(0) = 1/4 ✓. Orders: if k < l the
degree-k part of the RHS is y_k ≠ 0 while ord(LHS) ≥ k+l > k (uses l > k ≥ 0) ✓; for k ≥ 1,
ord(LHS) ≥ 2k > k forces y_k + z_k = 0 ✓.
(II) `4xỹz̃ = Qỹz̃ + x(ỹ+z̃)`, so `x(4ỹz̃−ỹ−z̃) = Qỹz̃`; Q ∤ x ⇒ Q | 4ỹz̃−ỹ−z̃ = Qh, `xh = ỹz̃` ✓.
At 0: `4ỹ₀z̃₀ = ỹ₀+z̃₀` ⇔ `(4ỹ₀−1)(4z̃₀−1) = 1` ✓; x₀ = 0 ⇒ ỹ₀z̃₀ = 0 ⇒ ỹ₀+z̃₀ = 0 ⇒ both 0 ✓.
Remark after 8.2 (composed one-variable families have k = 0) ✓: Y ∈ Q[n] with Y(0) = 0 gives n | Y,
i.e. Q | y, contradicting shape (I).
Minor: Theorem 3.2′ (k = 1) uses z₁ = −y₁, which needs the non-degenerate branch y+z ≠ 0; this is
automatic there (F is assumed valid on C ∩ S beyond R), but is not said (D-list, MINOR m1).

### Lemma 8.3 (pointwise descent) — SOUND

ET statements checked against `sources/elsholtz-tao-1107.1010.pdf` (pdftotext): Type I = "n | x,
n coprime to y, z"; Type II = "n | y, z, n coprime to x" (p. 3); Prop 2.2 / 2.6 hold for **every**
n ∈ N (no primality), giving (a,…,f) ∈ N⁶ ∩ Σ with x = abdn, y = acd, z = bcd resp.
x = abd, y = acdn, z = bcdn and f = 4acd − n resp. 4acd − 1 (pp. 12–14; Prop 2.6 has a harmless
typo π^I for π^II); Prop 1.6: f_I(n) = f_II(n) = 0 for every odd perfect square n (incl. n = 1). ✓
(a) Descent: λ | x (n | x), `4/(λw²) = Σ 1/(x/λ)`; x′ = n′(x/n); λ ∤ y′z′ and gcd(w,y′z′) | gcd(w,yz) = 1
⇒ Type I for the odd n′ = λw² ✓. Lemma 1.1(I): (−D/n′) = −1; gcd(D,n′) = 1 by (2.1), so
(−D/n′) = (−D/λ)(−D/w)² = (−D/λ) ✓. `(x′/n′)y′z′ = DAB·DAC·DBC = D(DABC)²`, and λ ∤ y′z′ = D²ABC²·…
covers λ ∤ DABC, so the symbol of −(x/n)(y/λ)(z/λ) equals (−D/λ) = −1 ✓.
(b) Type II for n′ (n′ | y′ = n′(y/n), n′ | z′, gcd(n′,x′) = 1) ✓; F = 4ACD − 1 = 4y′/n′ − 1 =
4y/n − 1 ≥ 3, F ≡ 3 (4) ✓; Lemma 1.1(II): (n′/F) = −1, gcd(F,n′) = 1 by (2.21) ✓;
(n′/F) = (λ/F)(w/F)² = (λ/F). **Reciprocity sign re-derived:** for odd coprime positive λ, F,
(λ/F)(F/λ) = (−1)^{((λ−1)/2)((F−1)/2)}; (F−1)/2 is odd, so the sign is (−1)^{(λ−1)/2} = (−1/λ), hence
(λ/F) = (F/λ)(−1/λ) = (−F/λ) = ((1 − 4y/n)/λ) ✓. (Note y and z are interchangeable here, so the
same holds for z; my script tests both.)
(c), (d): dividing by λ² gives a Type I (resp. II) solution for the odd square w²: x/λ² = w²(x/n),
gcd(w², yz/λ⁴) = 1 (resp. y/λ² = w²(y/n), gcd(w², x/λ²) = 1) ✓; ET Prop 1.6 ✓ (w = 1 included).
(e) ET Prop 1.6 ✓. The implicit λ ∤ w is not needed (and is forced in (a),(c) by gcd(w,yz) = 1).

**From-scratch brute force** (`scripts/review_bf2_lemma83_brute.py`, output
`data/review_bf2/lemma83_brute.txt`): complete enumeration of all solutions (x ≤ y ≤ z via
x ∈ (n/4, 3n/4] and the divisor identity (ay−b)(az−b) = b²; cross-checked against a naive Fraction
enumeration for 10 values of n ≤ 441, identical solution sets), then every ordering and every
decomposition n = λ²w², for all n = λ²w² ≤ **60 000** (185 pairs (λ,w), 489 865 unordered
solutions). Hypotheses of (a): 7 969 times; of (b): 3 037 times (symbol checked for both y and z);
Legendre symbol −1 every time; (c), (d), (e): 0 occurrences. 0 violations. This extends the
author's n ≤ 12 000 check by 5×. CERTIFIED for n = λ²w² ≤ 60 000.

### Lemma 8.4 (coprime square points on a prime dilate) — SOUND (minor presentation points)

Re-derived step by step (numerical companion: `scripts/review_bf2_lemma84_construct.py`, below).
* Step 1 ✓ (Lemma 2.1's proof: λ(u₁,v₁) ≡ (u₀,v₀) mod M whenever λμ ≡ 1; w₁ ≡ unit; the sign of w₁
  is free since only w₁² enters).
* Step 2 ✓: a class mod Mw₁ that is C mod M and has Q ≡ 1 mod ℓ^e ∥ w₁ exists by CRT (w₁ prime to
  M ⊇ 2D, Q mod ℓ nondegenerate represents 1, Hensel); its Q-value is a unit square mod Mw₁, so Lemma
  2.1 applies (8, 2D | Mw₁); the primitive triple's w₀ is prime to Mw₁ since λw₀ is.
* Step 3 ✓: with β₀ = 2B(P₀,·), `Q(aP₀+bY) = a²w₀² + abβ₀ + b²Q(Y)`; a = Q(Y), b = −β₀ gives
  Q(Y)²w₀². The line {sX₀ + t(Y,0)} meets the conic where t(sβ₀ + tQ(Y)) = 0, so the second point is
  ψ(Y) ✓; conversely Y ∝ w₀P − wP₀ (tangent case Y ⊥ P₀) ✓. (ii): ℓ ∤ 2Dw₀, ℓ | ψ(Y), Y primitive
  ⇒ ℓ | Q(Y), ℓ | β₀(Y) ⇒ Ȳ isotropic and Ȳ^⊥ = F_ℓȲ ∋ P̄₀ ⇒ ℓ | w₀² ✓. Hence primes of k₀ divide
  2Dw₀; w₀Q(Y°) = k₀w₁ with gcd(w₀,w₁) = 1 ⇒ w₀ | k₀ ✓ (also fine in the degenerate case X₁ = X₀,
  possible only if w₀ = w₁ = 1).
* Step 4 ✓: each coordinate of ψ is an integral quadratic form, so ψ(Y°+NZ) = ψ(Y°) + N·Bψ(Y°,Z) +
  N²ψ(Z) with Bψ integral bilinear; dividing by k₀ (N = k₀M) gives X_Z ≡ X₁, F₁ ≡ w₁ (mod M),
  F₁ = w₁ + w₀M·β(Y°,Z) + w₀k₀M²Q(Z) ✓. All data (ψ, Y°, k₀, N) are fixed **before** λ, so "λ larger
  than the constants" is legitimate (no circularity).
* Step 5 ✓ (ψ₁₂(Y) ≠ 0 for real Y ≠ 0 because Q(ψ₁₂) = ψ₃² = w₀²Q(Y)² > 0).
* Step 6 ✓: ℓ | M and ℓ | k₀, ℓ ∤ M (then ℓ | w₀ and F₁ ≡ w₁ mod w₀) give ρ_ℓ = 1; ℓ ∤ N:
  ℓ | F₁ ⇔ ℓ | Q(Y_Z), ≤ 2ℓ−1 zeros. The O(1/ℓ²) bound: inert ℓ — only Y ≡ 0 (1 class); split ℓ —
  on the line tȲ_ℓ, ψ₁₂ ≡ −t²β₀(Ȳ_ℓ)Ȳ_ℓ, β₀(Ȳ_ℓ) ≢ 0, and t ↦ G(−λt²β₀Ȳ_ℓ/k₀) has leading
  coefficient G_j(V)(−λβ₀/k₀)^j ≢ 0 mod 𝔩 outside a λ-independent finite set of ℓ (G does not
  vanish on the isotropic line KV: otherwise L₁ | G, then by conjugation L₂ | G, so Q | G) ✓.
  ℓ = λ: H_i∘ψ₁₂ is a fixed nonzero integral form (ψ₁₂ is dominant), nonzero mod λ for λ large ✓;
  ρ_λ ≥ 1 − (2+2Σdeg H_i)/λ > 0 for λ > 2+2Σdeg H_i ✓. ∑(1−ρ_ℓ) < ∞, every ρ_ℓ > 0 ⇒ ρ > 0 ✓.
* Step 7 ✓: F₁ irreducible (invertible affine image of Q, times a constant), b²-coefficient
  w₀N²Q(0,1)/k₀ constant ✓; F₁ ∤ G₁ because ψ₁₂(tV) = −t²β₀(V)V with β₀(V) ≠ 0 (P₀ anisotropic) and
  t² covers C, so G would vanish on CV ⇒ Q | G ✓; hence ℛ = Res_b(F₁,G₁) ≢ 0 (if G₁ has b-degree 0,
  ℛ = G₁² ≢ 0) ✓. Small primes by CRT (period ∏_{ℓ≤L}ℓ·λ; error O_L(T)); L < ℓ ≤ c₁T: ≤ 4degG+1
  bad residues each, Σ O((T/ℓ+1)²) = O(T²/L + T) ✓; ℓ > c₁T: ℓ | ℛ(a), ω_{>c₁T}(ℛ(a)) = O(1),
  ≤ 2 residues of b, interval length < ℓ ✓; roots of ℛ: O(T) ✓. Conclusion (3) also holds in the
  degenerate case G₁(Z) = 0 (then goodness forces w = F₁(Z) = 1) — irrelevant in the application,
  where y(P)z(P) > 0.
Presentation points (MINOR m2): (i) Step 6 says "ρ_ℓ ≥ 1 − (4 deg G + 1)/ℓ²" for ℓ outside a finite
set — correct, but the exceptional set also contains the primes 𝔩 at which V mod 𝔩 = 0 or V, V̄
collide (ℓ | D, already excluded by ℓ ∤ N); worth one clause. (ii) the box B₀ must avoid 0 (it does,
being inside the open cone Γ) — say so, since |Y_Z| ≫ T is used in Step 5.
