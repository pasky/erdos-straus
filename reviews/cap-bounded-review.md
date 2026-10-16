# R261 — hostile review of CAP_BOUNDED.md (O250, checkpoint 1)

Reviewer: R261 side agent (branch side-agent/review-cap-bounded, merged side-agent/cap-bounded at 6c42e1dc).
From-scratch scripts: `scripts/review_r261_*.py` (no reuse of `scripts/z22_*`).
Self-test of the checker: `review_r261_selftest.py 400 23 2` — least Lemma-3.1 cap via residue DP vs. direct
enumeration of all D₁ = ∏ s^{c_s} (c_s ∈ [0, 2b_s + 2E + 2]) checked against Def 1.1 with exact rationals:
221 (p, m) pairs, 0 mismatches.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Lemma 1.1 / Cor 1.2 | SOUND |
| Thm 1.3 (+ explicit examples) | SOUND (CONDITIONAL on Dickson, as labelled) |

## 1. Lemma 1.1, Cor 1.2, Thm 1.3

**Lemma 1.1 — SOUND.** Re-derived: s | K, s | m ⇒ s | 4K − m = p; reciprocity with (m−1)/2 odd gives
(s/m) = (−m/s) = (p/s) = (s/p). (b): 8 | p + m ⇒ m ≡ −p (8), and (2/·) depends on ±(mod 8) only. (c), (d) fine.
Negative exponents are harmless (Jacobi symbol of an inverse = symbol). **Cor 1.2 — SOUND**, including δ_p via
(p/m) = (m/p); for K odd δ₂ = 0 is forced by CAP_DOWN Lemma 3.1 (c₂ ≤ 2v₂(N) = 0), so (b)'s hypothesis is never needed.

**Thm 1.3 — SOUND (CONDITIONAL on Dickson).** Re-derived every step:
* v_ℓ(L) = v_ℓ(Λ) + 1 (+4 at ℓ = 2) and v_ℓ(m+1) ≤ v_ℓ(Λ), so ℓ | L_m for every ℓ ≤ M+1 and v₂(L_m) ≥ 5; m | Λ and
  gcd(m, m+1) = 1 ⇒ m | L_m ⇒ R_m ≡ 1 (mod 4m). 8ℓ | L ⇒ (ℓ/p) = 1 for all ℓ ≤ M+1 (incl. ℓ = 2).
* Admissibility: forms ≡ 1 (mod ℓ) for ℓ ≤ M+1; for ℓ > M+1 the leading coefficients are units, at most
  1 + ⌊(M+1)/4⌋ < ℓ roots. Forms distinct. OK.
* (R_m/p) = (p/R_m) = (−m/R_m) = (m/R_m) = (R_m/m) = (1/m) = 1, using p = (m+1)(R_m−1)+1 ≡ −m (mod R_m). OK.
* (m/p) = 1 since all prime factors of m are ≤ M. So every generator in Cor 1.2 has symbol +1 ⇒ no certificate.
* Reduction "every ES^{(y)} solution with p ∤ x has x > (p+M)/4": 4/p > 1/x forces 4x > p, m = 4x − p ≡ 3 (4),
  gcd(m, p) = gcd(x, p) = 1, and CAP_DOWN Lemma 3.1 is the complete list. OK. (Solutions with p | x but p ∤ y are
  covered by swapping x ↔ y, since both are integers in ES^{(y,e)}; only "p divides both integer coordinates"
  (Type I in both) escapes — the stated scope p ∤ x is if anything slightly conservative.)

*Explicit examples — independently CONFIRMED* (`review_r261_windows.py p M 20`; cap ≤ 20 saturates the residue sets
since λ(m)/2 ≤ 9 for m ≤ 19, so "None" = no certificate at any cap):
* M = 11: p = 807 330 585 601, 1 482 496 646 401, 2 412 770 976 001 — all prime (SymPy), ≡ 1 (8); windows 3, 7, 11:
  K_m = ((m+1)/4)·R_m with R_m prime, every generator symbol (s/p) = +1, (m/p) = +1, no certificate.
* M = 19: p = 4 714 845 095 999 745 907 201, 11 787 094 675 874 034 316 801 (BPSW probable primes; R_m likewise —
  SymPy isprime/factorint, i.e. probable-prime status only, as the author says); windows 3, 7, 11, 15, 19 all dead.
  Note: these are probable primes, so the M = 19 check is EVIDENCE-grade; Thm 1.3 does not depend on them.
