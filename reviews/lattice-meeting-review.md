# R262 — hostile review of O251 (LATTICE_MEETING.md, BRAINSTORM/z23_*.md)

Reviewer: R262 side agent, branch side-agent/review-lattice-meeting, merged side-agent/lattice-meeting at start.
From-scratch scripts: `scripts/review_r262_*.py` (none reuse z23_* code).

## Verdict summary (filled in claim by claim)

## Claim-by-claim

### C1. p = 3361 (CERTIFIED) and "only such prime ≤ 10⁷"
Independent complete enumeration (`scripts/review_r262_3361.py`, sympy only for factoring/divisors).
Completeness proof used: Type II means p | y, p | z, p ∤ x. Then y, z ≥ p ⇒ 1/x = 4/p − 1/y − 1/z ≥ 2/p, so
x ≤ p/2, and x > p/4. With y = pY, z = pZ, m = 4x − p ≥ 1: (mY − x)(mZ − x) = x², mY − x > 0. So looping over all
x ∈ (p/4, p/2] and all δ | x² with δ ≡ −x, x²/δ ≡ −x (mod m) lists every ordered solution. Result for p = 3361:
exactly two unordered solutions, (x, Y, Z) = (841, 290, 8410) and (850, 25, 170) — matches the document. Slices
g = 4Y − 1, D = 4Z − 1: 1159 = 19·61, 33639 = 3·11213, 99 = 3²·11, 679 = 7·97; −3361 is a non-square modulo each
(checked by brute force over every prime-power factor); gcd(slice, p) = 1 in all four cases. ET parameter
d = gcd(x, Y, Z) is 29 resp. 5, matching (1, 29, 10, 29) and (5, 34, 1, 5).
