# R163 — hostile review of O163 (POINTWISE_BINARYFORM.md §8, (x,y,z)-families)

Reviewer: R163 (side-agent/review-binaryform-xyz). Reviewed: author branch `side-agent/binaryform-xyz`
(merged into this worktree), §8 and the "(O163 update)" lines in §0, §4.4(iv), §7; author report
`reviews/agent-reports/AGENT_REPORT_O163.md`. ES is not solved; nothing reviewed here proves any case.

Status: COMPLETE (round 1). Author branch was quiet for 25 min at the end of the review, so the
reviewer applied m1, m3, m4 and m5 directly to POINTWISE_BINARYFORM.md, each marked "(R163 repair)". m2 and m6
were not applied: m2 is presentation only, and m6 is not a defect.

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

**Numerical companion (from scratch, runs the proof's construction rather than a direct search):**
`scripts/review_bf2_lemma84_construct.py` → `data/review_bf2/lemma84_construct.txt`. For
Q ∈ {u²+v², u²+uv+v², u²+2v², u²+uv+2v², 2u²+uv+3v² (D = −23, h = 3, a non-principal form), u²+5v²},
M ∈ {8, 24, 40, 16, 48, 56, 184}, every (square class mod M, octant) pair (24 832 pairs), it performs
Step 1 (primitive X₁ ∈ unit·C, arg in a closed sub-arc), Step 2 (gcd(w₀,Mw₁) = 1), Step 3 (Y°, ψ(Y°) =
k₀X₁; checks primes of k₀ | 2Dw₀ and w₀ | k₀), Step 4 symbolically in sympy (X_Z, F₁ integral,
≡ X₁, w₁ mod M, non-constant coefficients of F₁ ≡ 0 mod w₀M, Q(X_Z) = F₁²), takes the first
Dirichlet prime λ ≡ μ⁻¹ (M), λ > 50, λ ∤ N, and counts Z in a box around T·Y°/|Y°| (T = 60) with
λX_Z in the open octant and (2)–(4) for G = (u−v)(2u+v−1)(u²−3v+2)·v·(u+2v) (G(0,0) = 0, Q ∤ G),
H = (u−3v)(u+v)(2u−v). Result: 0 failures of every Step-3/4 claim, 0 pairs without a good Z;
the fraction of good Z per box is ≥ 0.16 everywhere. (A first run with too small a point search
missed 2 of 23 unit-orbits of square classes for 2u²+uv+3v² mod 184; the smallest primitive square
points there are (−218,−367; 761) and (−746,769; 1521) — a search-box effect, confirming the
author's similar remark, not a counterexample to Lemma 2.1.)
Independent confirmation of the motivating claim (§8.5, check after 8.4):
`scripts/review_bf2_primitive_classes.py` → `data/review_bf2/primitive_classes.txt`: the share of
square classes mod M containing no primitive square point is 1/2 (u²+v² mod 8, 24; u²+uv+v² mod 24;
u²+2v² mod 16; u²+5v² mod 40) or 3/4 (u²+v² mod 40; 2u²+uv+3v² mod 184). Hand check: for u²+v²
mod 8, primitive Pythagorean points with 8 | v have u ≡ ±1 (8), so the square class (3,0) mod 8
has only imprimitive square points. So R159's suggested route really does fail when G(0,0) = 0, and
the λ-descent is genuinely needed. ✓

### Theorem 3.2′ — SOUND (one MINOR hypothesis remark)

All cases covered: shapes (0)/(I)/(II) are exhaustive (Lemma 8.1), and within (I), (II) the
cases k = 0, 1, ≥ 2 are exhaustive. Re-derived each:
* Setup ✓: δ | M and Q(C) a unit mod M ⇒ gcd(n,δ) = 1 ⇒ x̃(P) ∈ Z (resp. ỹ, z̃); integrality of
  F is δ-periodic; Lemma 3.1 (it is stated for six coordinates but is a statement about any finite
  list of nonzero polynomials) gives validity on C ∩ S beyond R; Lemma 8.4 then supplies P = λX.
* Hypotheses of Lemma 8.4 ✓: G = δ²yz (resp. δx) ∈ Z[u,v], Q ∤ G because Q is prime and divides
  none of the factors; H₁ = δy₁ (resp. δx₁) is a nonzero integral form when k = 1.
* (I) k = 0 ✓ (λ > |G(0,0)| ≠ 0; gcd(w,yz) = 1 from (3); Type I for the odd square n; 8.3(e)).
  k = 1 ✓: δy(λX) = Σ_{j≥1} λ^j δy_j(X) gives y(P)/λ ≡ y₁(X), z(P)/λ ≡ z₁(X) = −y₁(X) (mod λ, in
  Z_(λ)), x̃(P) ≡ 1/4; −x̃(y/λ)(z/λ) ≡ (y₁(X)/2)² ≢ 0 by (4), so the Legendre symbol is +1 against
  −1 from 8.3(a). k ≥ 2 ✓ (8.3(c)).
* (II) k = 0 ✓; k = 1 ✓ (x(0,0) = 0 ⇒ ỹ(0,0) = 0 ⇒ 1 − 4ỹ(P) ≡ 1, symbol +1 against 8.3(b));
  k ≥ 2 ✓ (8.3(d)).
* (c′) quantifiers ✓: A_F = ∅ is a property of F alone; for each δ′ the exceptional bounded set
  depends on (F, δ′) only (Lemma 3.1 on the compact arc-complement), not on C or P. No sign
  dilation needed (validity is x, y, z > 0). ✓
* Hidden-hypothesis check: Lemma 8.4 needs **2D | M** (Step 2: ℓ | w₁ ⇒ ℓ ∤ 2D; Step 3(ii) and
  Step 6: ℓ | k₀, ℓ ∤ M ⇒ ℓ | w₀; ℓ ∤ N ⇒ Q nondegenerate mod ℓ). Thm 3.2 allowed "2D | M **or** Q in
  the principal genus" (Lemma 2.1), and §4.2 uses the principal-genus clause to get a modulus
  independent of s₀. Thm 3.2′ as stated requires 2D | M, so §0's "with the same hypotheses" is
  slightly inaccurate. Easy repair (MINOR m3): since the conclusion A_F = ∅ does not depend on C,
  for Q in the principal genus and a square class C mod M with 2D ∤ M, pass to a sub-class
  C′ ⊂ C mod lcm(M,2D) on which Q is a unit square (exists: a principal-genus form represents
  ℓ-adic unit squares at every ℓ | 2D, CRT), apply (b′) to C′, and conclude (c′) on C.

### Modulus hypothesis "δ includes denominators of x/Q, y/Q, z/Q" — natural, harmless; even removable

(i) Redundant: by Gauss's lemma (Q primitive), content(x) = content(x/Q)·content(Q) =
content(x/Q), so the denominators of x/Q equal those of x. (ii) It does not weaken Cor 3.4′ relative
to Cor 3.4: Thm 3.2 already used K_F := common denominator of the coordinates, so the joint modulus
is of exactly the same kind. (iii) It can be weakened further (optional strengthening, not a
defect): in the proof δ is used only through gcd(n,δ) = 1, i.e. Q(C) a *unit* at primes of δ.
If F is integral on a square class C mod M₀ (8, 2D | M₀), C contains a square sub-class C′ mod
lcm(M₀,δ) (Q ≡ 1 at the new primes ℓ ∤ M₀, ℓ ∤ 2D, by CRT); (b′) on C′ gives A_F = ∅ and then (c′)
holds on all of Z². So the true hypothesis is "8, 2D | M and F integral on C" (integrality period
instead of denominator), e.g. for integer-valued polynomials such as u(u+1)/2.

### Corollary 3.4′ — SOUND relative to Hecke (same status as Cor 3.4); one wording point

Polynomial families: Thm 3.2′(c′) on each square class mod M (δ | M), then Cor 3.4's Hecke
counting verbatim ✓. Rational families: a coordinate g = A/B in lowest terms with B nonconstant
must be an integer at a valid point, so Lemma 3.3 gives ≪ X^{1+ε} valid points of norm ≤ X versus
≍ X²/log X prime points ✓. The modulus is "8, 2D and the δ's" — of the same kind as Cor 3.4 (see
above). Wording: "no 'Fermat + identity' certificate whatsoever" should keep the word *finite* and
the standing scope (positive definite Q with a square class, no floor/factorisation steps, bounded
families of forms) right in the sentence, since §8.5 lists exactly those exclusions (MINOR m5).

### Is R159 D6 genuinely closed? — YES

D6 was: the headline claimed all "ES solution = polynomial in (u,v)" certificates, but only
families with polynomial/rational ET coordinates were covered; (x,y,z)-families were open because
gcd(Q(P), y(P)z(P)) can be > 1 at every square point. §8 handles this. Lemma 8.1 removes shape (0).
Lemma 8.4 controls all primes of w by a sieve. The only common factor left is the prime λ, which is
harmless: Lemma 8.3 descends by λ or λ². The origin identities of Lemma 8.2 then turn the forced
symbol −1 into +1 when k = 1. Every step re-derived; Lemma 8.3 brute-forced to n ≤ 60 000; Lemma
8.4's construction run on 24 832 (class, octant) pairs, including a non-principal form of class
number 3. No residual case: rational families via Lemma 3.3; shapes and k exhaustive. The
stale sentence at §3 end (lines 175–176: "(x,y,z)-only families are §4.4(iv), open") must be
updated (m4), and §0's "with the same hypotheses" needs the 2D | M nuance (m3).

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 8.1 (shapes; Q prime; shape (0) never valid when gcd(Q(P),δ) = 1) | SOUND |
| Lemma 8.2 (origin identities, Types I/II) | SOUND (m1: y+z ≠ 0 branch implicit in Thm 3.2′) |
| Lemma 8.3 (descent by λ / λ², Legendre symbols, reciprocity sign) | SOUND; brute force CERTIFIED to n ≤ 60 000 |
| Lemma 8.4 (sieve: Steps 1–7, k₀, ℓ > T tail) | SOUND (m2 presentation) |
| Theorem 3.2′ (cases k = 0, 1, ≥ 2; quantifiers in (c′)) | SOUND (m3: needs 2D \| M, not "same hypotheses") |
| Cor 3.4′ (relative to Hecke) | SOUND relative to Hecke (m5 wording) |
| Modulus hypothesis (δ incl. denominators of x/Q…) | natural; redundant by Gauss's lemma; removable (integrality on C suffices) |
| D6 closed? | YES (after m4: stale "open" sentence at §3 end) |

No FATAL, no MAJOR defects.

## Defects

1. **m1 (MINOR).** Thm 3.2′ proof, Shape (I), k = 1 bullet: uses z₁ = −y₁ from Lemma 8.2, which is
   proved only in the branch y + z ≠ 0. Repair: add "(y + z ≠ 0, as F is valid somewhere)".
2. **m2 (MINOR).** Lemma 8.4 Step 6: the "finite set" of exceptional ℓ should also list the primes
   at which the isotropic vectors V, V̄ reduce to 0 (finitely many); Step 5: say B₀ avoids 0.
3. **m3 (MINOR).** §0 "(O163 update … with the same hypotheses)" and §8 Thm 3.2′: Thm 3.2 allowed
   "2D | M or Q in the principal genus"; Lemma 8.4 needs 2D | M. Repair: either say "M divisible by
   8, 2D, δ" in §0, or add the one-line reduction: for principal-genus Q and 2D ∤ M, apply (b′) on a
   sub-class C′ ⊂ C mod lcm(M,2D) with Q(C′) a unit square; A_F = ∅ is independent of C. (This also
   restores §4.2's s₀-independent modulus for (x,y,z)-families.)
4. **m4 (MINOR, stale text).** §3, paragraph after Cor 3.4 (lines 175–176): "(x,y,z)-only families
   are §4.4(iv), open" contradicts §8. Repair: append "(O163 update: closed by §8, Cor 3.4′.)".
5. **m5 (MINOR, wording).** Cor 3.4′ tail "no 'Fermat + identity' certificate whatsoever": insert
   "finite" and "within the scope of §4.4/§8.5". Optional strengthening (not a defect): the
   δ | M hypothesis may be replaced by "F integral on C" (see the modulus section).
6. **m6 (cosmetic).** Lemma 8.3 check counts: my from-scratch counts at n ≤ 12 000 are (a) 1 962,
   (b) 818 vs the author's 1 612 / 688; the difference comes from conventions (I count all λ ≤ √n,
   every decomposition n = λ²w², y↔z orderings separately; the author caps λ ≤ 47). Not a defect.
