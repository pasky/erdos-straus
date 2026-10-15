# R228 — hostile review of O225 (NEAR_SQUARE_EXIST.md, checkpoint 1)

Reviewer: R228 side agent (branch side-agent/review-near-square, merged side-agent/near-square-exist at 305cf029).
From-scratch scripts: `scripts/review_r228_*.py` (none reuses the author's `z2_*`). ES is not solved; nothing below changes that.

(Verdict table and defect list at the end; written claim by claim.)

## Claim-by-claim

### Prop 1.1 (u-side T1, all u) — SOUND
Re-derived. p + u = x² + y², gcd(x, y) = 1 ⇒ 4 ∤ N and every odd prime of N is ≡ 1 (4).
* u even: N odd ⇒ every divisor ≡ 1 (4), so N ≡ 1 (4) ⇒ u ≡ 0 (4) and A = tu − 1 ≡ 3 (4) cannot divide N. No word. ✓
  (The v = u mirror is the same with A* = tv − 1.) The "too easy" worry is unfounded: the statement is genuinely
  vacuous for even u, and the author says so ("clean only vacuously"). The remark "4 | u is exactly the level where
  every word has χ = −1" is the sign table (u ≡ 0 mod 4), correct.
* u odd: N ≡ 2 (8) ⇒ u ≡ 1 (4); A odd ⇒ A ≡ 1 (4), v ≡ 2 (4), t ≡ 2 (4), A* odd; A even ⇒ A ≡ 2 (4), v ≡ 1 (4)
  (N/2 ≡ A/2 ≡ 1 mod 4), t ≡ 3 (4), A* ≡ 2 (4). None of t, u, v, A, A* is ≡ 0 (4) ⇒ χ = +1 by the DK table. ✓
* From scratch (`scripts/review_r228_prop11.py 200000`, Euler-criterion χ, own SPF sieve, coprime-two-squares test
  validated against brute force for n < 3000): 8 977 primes p ≡ 1 (4) < 2·10⁵, 1 103 693 ordered words (both
  orientations): **0 sign-table mismatches; 28 886 words with p + u a coprime two-square sum, 0 with χ = −1, 0 with
  that u even.** Agrees with the author's 10⁷ run in kind.
* Relation to R225: R225 had proved odd u only and left even u open; Prop 1.1 closes it correctly.
