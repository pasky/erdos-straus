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
