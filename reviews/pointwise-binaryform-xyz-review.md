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
