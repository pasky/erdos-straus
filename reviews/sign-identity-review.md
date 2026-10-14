# R204 — hostile review of SIGN_IDENTITY.md (O205, checkpoint 1)

Reviewer branch side-agent/review-sign-identity (merged side-agent/sign-identity at review start).
From-scratch scripts: `scripts/review_si_lemmas.py`, `scripts/review_si_avg.py` (+ further `review_si_*` below).
None reuse `scripts/si_*`.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 ((u,v)-form, χ = (−uv/n₀), size bound) | SOUND |
| Lemma 1.2 (trivial certificates; Dirichlet/Chebotarev form) | SOUND (classical; novelty nil — see D1) |
| Lemma 2.1 (averages, 240/512, 80/512) | SOUND |
| Thm 2.2 (no holomorphic modular generating function) | SOUND-AFTER-REPAIRS (minor: D2, D3) |

## Claim-by-claim

### Lemma 1.1 — SOUND
Re-derived. t·uv = n + u + v; Av = (tu−1)v = n + u, A*u = n + v; t ≥ 1 is automatic from positivity, so the bijection
holds. AA* = tn + 1 ⇒ gcd(A, n) = 1. If ℓ | n, ℓ | u: ℓ | Av, ℓ ∤ A ⇒ ℓ | v, and A ≡ −1 (ℓ) ⇒ (−A/ℓ) = 1; for ℓ | n,
ℓ ∤ uv: A ≡ u v⁻¹ ⇒ (−A/ℓ) = (−uv/ℓ). Size: t ≥ 1 ⇔ uv ≤ n + u + v ⇔ (u−1)(v−1) ≤ n + 1; for u ≤ v, v | n + u.
From-scratch brute force (`review_si_lemmas.py`, words found by scanning (u, v) directly, not via the divisor trick):
odd n ≤ 2000, 50 008 words (35 184 for n ≤ 1500 — matches the author's census total); χ = (−uv/n₀), the prime-sharing
claim, and the bound |X_n| ≤ 2Σ d(n+u) (n ≤ 600): 0 mismatches.
(The author's "50 003 words of odd n ≤ 2000" in Prop 4.1 excludes the 5 words of n = 1; cosmetic, D-minor below.)

### Lemma 1.2 — SOUND
All three word families re-verified by hand and by script (n < 20 000, all p ≡ 1 (4), q ≡ 3 (4), q | p + 1: 0 failures).
The Dirichlet/CRT and Chebotarev statements are correct: K′ ⊇ ℚ(i) Galois, q unramified in K′ ⇒ K′ ∩ ℚ(ζ_q) = ℚ, so
Frobenius (id, −1) in Gal(K′)×Gal(ℚ(ζ_q)) has positive density; p split in K′ ⇒ p ≡ 1 (4).
Overlap: the n ≡ 3 (4), 5 (8) words are Mordell's classical identities (already CHI_FLIP §3.1, (J)9/(J)32 mod-8 sign
law: they are χ = −1 cells), and "certificates exist for infinitely many p in every admissible class" is folklore (any
single Mordell–type family p ≡ −1 (q) does it). The document says this ("No certificates beyond the Mordell mechanism"),
so no overclaim; it should not be listed as a result in the report's PROVED list without "(classical)". D1.

### Lemma 2.1 — SOUND
Cells recomputed from scratch, and the *cell-function* property re-tested on 216 lifts per cell: 320 odd-K cells,
240 with χ = −1, 80 with χ = +1 (same as MODEL_SPECIFIC Thm 3.1(a)/CHI_FLIP Cor 1.2 — not new). Leading-term
uniformity over residue classes of #{tuv ≤ X} is standard (hyperbola method). The error analysis (t ≤ 2 words
O(X log X); t ≥ 3 ⇒ K ≥ tuv/3; boundary layer X < tuv ≤ X + u + v contributes Σ_{uv≤X}((u+v)/uv + 1) = O(X log X))
is correct. Numerical fit (`review_si_avg.py 200000`, exact counts, fit aX log²X + bX log X + cX on X/16…X):
a(N₋) = 0.23433 vs 15/64 = 0.234375; a(N₊) = 0.07820 vs 5/64 = 0.078125. Ratio ΣN₋/ΣN₊ = 2.43 at 2·10⁵,
consistent with the author's 2.40 (10⁵) / 2.50 (10⁶).

### Thm 2.2 — SOUND-AFTER-REPAIRS (mathematics correct; projection step and scope sentence need fixing)
*Short proof (cusp 0), re-derived.* For a holomorphic modular form f_k of weight k ∈ ½ℤ_{>0} on a finite-index
subgroup with any multiplier, f_k|S is holomorphic modular for S⁻¹ΓS, with expansion Σ_{m≥0} c_m q^{(m+κ)/h}; at
z = i/y every term but the κ = 0 constant decays like e^{−2π/(hy)}. Hence f(iy) = Σ_k b_k(iy)^{−k} + O(y^{−K}e^{−c/y}),
a finite sum of distinct powers: either ≍ y^{−k₀} or exponentially small. With Σ_{n≤X} a(n) ~ c·X log²X/2, c ≠ 0 for all
four a (c(S) = −5/16), Abel summation gives Σ a(n)e^{−2πny} ~ (c/2)(2πy)^{−1}log²(1/y). Contradiction. Correct.
The same computation along x = a/c (z = a/c + iy, γ(∞) = a/c, j(γ, γ⁻¹z) = i/(cy)) gives
f(a/c + iy) = Σ_k (i/(cy))^k (b_{k,γ} + exp. small), which is what step (i) of the long proof needs: cusp components of
*higher* weight are exponentially small on that ray (the sup-norm bound y^{−K/2} would NOT suffice if K > 2k — the
parenthetical "slash by γ" must be read this way; D3).
*Brief's specific worries.*
* E₂: quasi-modular, not a modular form, so outside the hypothesis; its cusp-0 expansion does carry an extra
  6/(πy) term (`review_si_cusp.py`: E₂(iy) + y⁻² = 6/(πy) to 8 digits). The holomorphic weight-2 Eisenstein series
  E₂(z) − NE₂(Nz) have the y⁻¹ terms cancel exactly (checked: y²(E₂(iy) − 2E₂(2iy)) = −1/2 to 8 digits, no y⁻¹ term).
  Even if a y⁻¹ term occurred it would be y⁻¹, not y⁻¹log²(1/y).
* Weight 1 Eisenstein: coefficients Σ_{d|n}χ₁(d)χ₂(n/d) with χ₁χ₂ odd, so not both trivial; Dirichlet series
  L(s,χ₁)L(s,χ₂) has at most a simple pole: average c·X, no log; expansions at every cusp are genuine q-expansions
  with constant terms (L-values), no log terms. Logs (d(n), X log X) arise only from the *non-holomorphic* weight-0
  Eisenstein series, outside the theorem.
* Weight ½: Serre–Stark (unary theta series), ≍ y^{−1/2} or exp. small at each cusp. Half-integral-weight Eisenstein
  series of weight ≥ 3/2: constant terms at cusps, covered by the same expansion.
* Oldforms, all cusps: the short proof needs only cusp 0 applied to each slash; level-raising f(dz) is again a modular
  form, nothing changes.
* Long proof (iii): Rankin–Selberg Σ_{n≤X}|a_g(n)|² ~ c_g X^K (c_g ∝ Petersson norm > 0) holds for cusp forms of
  half-integral weight with multiplier; the lower-weight mean squares (cusp X^{k′}, weight-1 Eisenstein X log³X,
  weight-½ X^{1/2}) are O(X^{K−1/2}); the triangle inequality in ℓ² finishes; the bound Σ|a(n)|² ≪ X^{3/2+ε} is correct
  (|a(n)| ≤ |X_n| ≪ n^{1/2+ε}). Correct, but redundant given the short proof.
*Defects:* D2 (projection to odd n), D3 (step (i) wording), D4 (scope sentence about Thm 9.1 and "log¹" is wrong).
