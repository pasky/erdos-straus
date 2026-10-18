# R271 — hostile review of O264 (HARD_PAIR.md, side-agent/hard-pair)

Reviewer branch side-agent/review-hard-pair. Merged side-agent/hard-pair at review start. From-scratch scripts:
`scripts/review_r271_*.{c,py}` (no z34_* code reused). Astra text read only at d7300f8 via `git show`.

## Summary verdicts
| claim | verdict |
|---|---|
| Thm 1.2 (a)–(e) (one equation qs = pc + 1; c_q; N₁ = #{q : c_q ∣ h}; integral-on-arrival ⟺ Type A with square c) | SOUND |
| Cor 1.3 (i)–(iv), converse false | SOUND (minor wording) |
| §1 Check numbers (75 658 / 53 716 / 21 942 (29 %) / 22 627 / 314 / failures 193, 2521, 66529) | SOUND — reproduced exactly |
| "Astra source" matches Astra's definition at d7300f8 | SOUND (attribution MINOR, see D1) |
| (filled in below) | |

## Goal 1 — Theorem 1.2 / Corollary 1.3

**Re-derivation.** (a) c/(sh) + 1/(psh) + 1/(ph) = (pc + 1 + s)/(psh) = s(q + 1)/(psh) = 4/p. ✓ gcd(c, s) | qs − pc = 1. ✓
(c) Type A cp + a + 1 = 4acd ⟺ (4cd − 1)a = cp + 1, i.e. a generalized source (q, c, s) = (4cd − 1, c, a) with c | cd = h. ✓
Converse via gcd(c, s) = 1. ✓ (d) c ≡ −p⁻¹ (mod q), 1 ≤ c ≤ h < q ⟹ c = c_q. ✓ gcd(q, p) = 1 is automatic from qs − pc = 1.
(e) q | pm² + 1 ⟺ m² ≡ c_q; for composite q the "square unit" condition is (−p/ℓ) = 1 for every prime ℓ | q (c_q and −p
are in the same square class since c_q ≡ −p·p⁻²). Genuine lifts by CRT since gcd(q, h) = 1 (4h ≡ 1 mod q). ✓ The repaired
integrality statement (m² | h, not merely c_q = m²) is correct; 193, q = 79, m = 3, s = 22: c_q = 9, h = 20, ✓ non-integral.
Split slices exist for every p: for prime q ≡ 3 (4), (−p/q) = −(p/q) = −(q/p) (QR, p ≡ 1 (4)). ✓
Cor 1.3(ii): m = 1 ⟹ c_q = 1 | h ⟺ q | p + 1, and any odd prime ℓ ≡ 3 (4) dividing p + 1 is such a q. ✓ (iv): ET Type II
4abcd = a + b + pc with b = 1 is exactly Type A; ET's Type I/II dichotomy for prime p is standard. ✓

**Scan bound (author's "4cd − 1 ≤ p + 4d ≤ (3p+3)/2").** Correct but terse. My own derivation: c(4ad − p) = a + 1 and
4ad − p ≡ 3 (mod 4), so 4ad − p ≥ 3; a = 1 is impossible (c(4d − p) = 2 has no solution with p ≡ 1 (4)); hence
q = (cp + 1)/a ≤ p + (p + 1)/a ≤ (3p + 1)/2, and also c ≤ (p + 7)/12 (the author's m² bound for the source scan). ✓

**From-scratch check** (`scripts/review_r271_dict.c`, `review_r271_dict 100000 2`, ~1 min): Type A enumerated by a
(d is unique per a), independently a slice scan over *all* q ≡ 3 (4) ≤ 2p (composites included) with c_q by extended
Euclid, independently an integral-Astra-source scan q = 4m²H − 1 | pm² + 1, and split/non-split by Euler's criterion on
every prime factor of q. Result: 4783 primes, 75 658 Type A, 53 716 split, 21 942 non-split (0.2900), 22 627 square c,
failures 193, 2521, 66529, **314** primes with Type A but no integral source (first 73, 313, 337, 409, 577, …), 0 mismatches
between the three scans, c = c_q always, c ≤ (p+7)/12 always, Cor 1.3(ii) holds at all three failures. Extending the slice
scan to q ≤ 4p for p ≤ 5000 finds nothing new. All of §1's numbers reproduced exactly.

**Astra definition check.** Astra d7300f8 SQUARE_REMOVAL_STRUCTURAL §1: "q ≡ 3 mod 4, qs = pm²+1, h = (q+1)/4, N = pm²,
A = sh", integral source (A, NA, Nh) at N, composite q allowed, genuineness gcd(A, m) = 1 ⟸ gcd(h, m) = 1 (and ⟺, since
gcd(s, m) = 1). Same as HARD_PAIR's definition (dividing the N-solution by m² gives the stated rational point). ✓
