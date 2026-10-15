# R257 — hostile review #1 of EXP_OPEN (O246), round 1

Reviewer: R257 (side-agent/review-exp-open). Author branch merged: side-agent/exp-open. From-scratch scripts:
`scripts/review_r257_*.py` (no z19_/z15_/z14_ imports).

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem 3.1 (ES for every 63·2^s + 1) | (in progress) |
| Theorem 2.3 (moving-gap class) | (in progress) |
| Theorem W / Lemmas 1.1–1.5 / Cor 1.7 | (pending) |
| Prop 2.1, Reduction 2.5, Prop 4.1, Comp 4.2 | (pending) |

## 1. Theorem 3.1 / Theorem 2.3 — from-scratch replay

`scripts/review_r257_cert63.py data/z19/cert63_et.json 1500` (pure Fractions; reads only the polynomial DATA of the
certificate). Output:
* Theorem 2.3: Type II identity cn + a + b = 4abcd verified as a polynomial identity in Y; the three factorisation claims
  (n + 4a²d = 63(Y + 3)(Y² − 3Y + 9), 4abd − n = 3(Y² − 3Y + 9), 4acd − 1 = 21(Y + 3)) verified.
  Integrality re-derived by hand: 340 = 4·85; for j = s/3 ≥ 2, Y = 2^j ≡ 0 (mod 4) and the numerators are ≡ 28, 64 ≡ 0
  (mod 4); ord₈₅(2) = lcm(ord₅ 2, ord₁₇ 2) = lcm(4, 8) = 8, so s ≡ 0 (24) ⇔ 8 | j ⇒ Y ≡ 1 (mod 85) ⇒ numerators ≡ 85,
  85 ≡ 0 (mod 85). So b, c ∈ ℤ for EVERY s ≡ 0 (mod 24), s ≥ 24 (for s = 0, Y = 1 fails mod 4: c = 85/340 — correctly
  excluded; s = 0 is handled by brute force). Positivity trivial (all of a, b, c, d > 0 for Y ≥ 1). Among j mod 8 only
  j ≡ 0 works (script: j ∈ [2, 10) → {8}), so the class is exactly s ≡ 0 (mod 24). **SOUND.**
* 18 classes: identity 4xyz = n(xy + yz + zx) verified for each; integer-valuedness on n ≡ r (mod M) verified by
  forward differences of p(r + Mt); positivity for n ≥ 63·2^10 + 1 verified by Taylor shift (all shifted coefficients
  ≥ 0, constant > 0 — stronger than the author's Cauchy bound); odd part of every M has ord(2) | 2520 (periods
  4, 7, 9, 10, 12, 14, 18, 24, 28, 140, 210), 2-part ≤ 2³ and r ≡ 1 mod the 2-part (consistent with n_s ≡ 1 mod 2^s).
  Hence n_s mod M depends only on s mod 2520 for s ≥ 10.
* Coverage: every s ∈ [2520, 5040) with s ≢ 0 (24) lies in some class → no uncovered residue. (The 18 classes even cover
  102 of the 105 residues s ≡ 0 (24); the three left are s ≡ 0, 840, 1680 (mod 2520), i.e. s ≡ 0 (mod 840) — consistent
  with the profinite unit-square point μ = 0.)
* Exact solutions with verified 4xyz = n(xy + yz + zx), all entries > 0, for every 0 ≤ s ≤ 1500 (62 moving, 1429 ET,
  10 brute force for s ≤ 9 with my own brute-force search).
* T1: 63·2^s + 1 = t² for s < 4000 only at s = 0 (n = 64, even) and s = 8 (127²). By hand: t ± 1 = 2A, 2(A + 1) with
  A(A + 1) = 63·2^{s−2}; consecutive integers with odd part 63 split as {63, 64} or {7·9 split…} — only 63·64 (s = 8)
  works. s = 8 is handled by brute force and lies in the divisor class D₁₂₇ (n ≡ 0 mod 127). No T1 tension.
