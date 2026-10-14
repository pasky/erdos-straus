# R219 — hostile review of O218 (SYNTHESIS_SPARKS4.md + BRAINSTORM/s4_*.md)

Reviewer branch `side-agent/review-synthesis-four` (merged `side-agent/synthesis-four`). From-scratch scripts:
`scripts/review_r219_*`. ES is not solved; nothing below changes that.

## Summary verdicts
(in progress)

## Defects

### D1 (MAJOR) — "signed" means two different things; the SQ_± record |t| ≤ 18 is false for the stated definition
*Location:* SYNTHESIS_SPARKS4 header ("'signed' = t u v ≠ 0, not positive"), §2.1 (R_n) (no "not positive"),
§2.5 bullets + CONJECTURE SQ_± ("some *signed* point"), s4_three_bits_meta P3(c), AGENT_REPORT SHARP 1;
`scripts/s4_sqpm.c` line 1 ("SIGNED word (t,u,v nonzero …)" — positive words included).
*Finding (from-scratch `scripts/review_r219_sqpm.c`, cross-checked by the factoring-free brute force
`scripts/review_r219_bruteword.py`):* every number in §2.5/§2.4 is reproduced **exactly** when the search admits
*all* words with t u v ≠ 0 (positive ones included): records 15 @ 97 185 (≤ 10⁶), 18 @ 4 884 441 (≤ 10⁷); |t| ≤ 6
failures 15 / 62 / 403 (≤ 10⁵/10⁶/10⁷); |t| ≤ 12 failures 8 (≤ 10⁷: 34 489, 97 185, 895 609, 3 567 369, 3 781 761,
4 884 441, 5 737 449, 8 351 385). Positive ES-five ≤ 10⁶: fails only at 105, record 231 @ 702 585 (reproduced).
But with the header's definition (signed = not positive) the least |t| is **not** ≤ 18:

| range | strictly-signed failures | record least \|t\| (strictly signed) | |t|>6 | |t|>12 |
|---|---|---|---|---|
| ≤ 10⁵ | 0 | 19 @ 60 369 | 34 | 7 |
| ≤ 10⁶ | 0 | 30 @ 297 465 | 203 | 34 |
| ≤ 10⁷ | 0 | 54 @ 9 817 305 | 1 277 | 156 |

Example (brute force, no factoring): n = 60 369 has positive χ = −1 words at t = 4, 5, 7, but the first strictly
signed χ = −1 word is (−19, 6, −525) (A = −115). So the *existence* half of SQ_± survives with either reading (0
failures ≤ 10⁷ for strictly signed words — the 105 statement is fine), but "least |t| ≤ 18", "403 vs 10 550" and
"8 vs 996" compare (signed ∪ positive) against positive, i.e. they measure ES-five *plus* signed tickets, not "signed
instead of positive". The quantitative "positivity is not the bottleneck" reading of §2.6 must be re-stated: dropping
positivity *and keeping* the positive words is easier (trivially ⊇ ES-five), while the strictly-signed problem alone
has a least-|t| record (54) far below ES-five's (231) but well above 18.
*Repair:* define (R_n) and SQ_± with "t u v ≠ 0" (positive allowed) — this is what was computed and is the natural
T1-keeping relaxation — and say so in the header; add the strictly-signed numbers above as a separate line
("even without positive words: 0 failures ≤ 10⁷, record 54 @ 9 817 305"); fix the comment in s4_sqpm.c.

### D2 (MINOR) — §2.3 "positivity costing nothing at these t" is false at t = 6
*Location:* SYNTHESIS_SPARKS4 §2.3, sentence after the table.
*Check:* re-derived the table (for n ≡ 1 (8): (−A/n) = (|A|/n); for an odd prime q | tn + 1, (q/n) = (n/q) = (−t/q);
since (ℤ/t)* = {±1} and gcd(d, t) = 1, a divisor d ∉ {1, |tn+1|} can be signed into A ≡ −1 (mod t), A, B ≠ −1; total
symbol of |tn+1| is +1, so a χ = −1 divisor exists iff some prime factor has (−t/q) = −1). All ten rows are correct:
`scripts/review_r219_slots.py 40000` — 4 900 non-squares n ≡ 1 (8), 0 mismatches between brute force and the table.
For **positive** words, A > 0 forces d ≡ −1 (mod t), and (d/n) = (−t/d) (Kronecker). For t = 1, 2, 3, 4 this is
automatic ((−3/d) = (d/3), (−4/d) = (−1/d)). For t = 6 it is not: (−6/d) = −(2/d) when d ≡ 5 (6), so the positive
t = 6 slot holds iff **6n + 1 has a divisor ≡ 17 or 23 (mod 24)** (0 mismatches on the same 4 900 n), and it differs
from the signed t = 6 slot at **694 of the 4 900 n** (first: n = 41, 6n + 1 = 13·19, both ≡ 1 (6); A = −13 gives a
signed word (6, −2, −41) with χ = −1, but no positive t = 6 word).
*Repair:* "positivity costs nothing at t = 1, 2, 3, 4; at t = 6 the positive slot needs a divisor ≡ 17, 23 (mod 24)".

### D3 (MAJOR → repairable) — §2.4 "no finite t-set" sketch: the argument is fixable, cleaner than stated, and needs only Dickson's conjecture
*Location:* SYNTHESIS_SPARKS4 §2.4; s4_three_bits_meta P3(d).
*Problems as written:* (i) "(bounded power of 2 and 3) × prime" — without fixing n ≡ 0 (mod p) for each odd prime
p ≤ 2T + 1 the tuple is never admissible (e.g. p = 5: the residues −1/t, t ∈ {±1, ±2}, cover (ℤ/5)*, so 5 divides one of
n ± 1, 2n ± 1 unless 5 | n); the "suitable modulus" is left unspecified. (ii) "signs fixed by congruences … +1 or
excluded (to be checked per T)" is an unproved per-T case analysis. (iii) Only *linear* polynomials occur, so the
right hypothesis is Dickson's conjecture, not full Schinzel H.
*Repaired argument (CONDITIONAL on Dickson's prime k-tuples conjecture; I regard it as a complete proof modulo
Dickson).* Fix T. Let P = ∏ odd primes p ≤ 2T + 1 and take n ≡ 0 (mod P), n ≡ r (mod 2^K) with r ≡ 1 (8) and K large
(so v₂(tn + 1) = a_t is fixed). For p | P, tn + 1 ≡ 1 (mod p); for p > 2T + 1 the 2T linear forms
f_t(k) = (t n(k) + 1)/2^{a_t} cannot cover ℤ/p; so the tuple {f_t : 1 ≤ |t| ≤ T} has no fixed prime divisor and Dickson
gives infinitely many n with every |tn + 1| = 2^{a_t}·q_t, q_t prime. For such n ≡ 1 (8): (2/n) = (−1/n) = 1 and
(q_t/n) = (|tn+1|/n) = 1, so **every** divisor A of tn + 1 has (−A/n) = +1 — no sign analysis needed. Finally n−1 =
2^{a}q with a fixed excludes all but finitely many squares. Hence for every T there are infinitely many odd non-square
n with no χ = −1 word (signed or positive) of |t| ≤ T. Numerical illustration `scripts/review_r219_dickson.py 3`:
n = 7 665, 29 505, 202 545 have all |tn + 1| (|t| ≤ 3) of the form 2^a·prime and indeed no χ = −1 word at |t| ≤ 3.
*Repair:* replace §2.4 by the above; label CONDITIONAL (Dickson).

### D4 (MINOR) — §2.2: the prime 2
"the sign is a genus character ψ_t(q) = (−t/q) of the prime factors" omits q = 2: for odd t, 2 | tn + 1 and
χ(2) = (2/n), which is −1 for n ≡ 5 (8). Harmless (n ≡ 5 (8) is settled by Prop 2.1(c)) but state "for n ≡ 1 (8)" or
add the factor (2/n)^{v₂(tn+1)}.
