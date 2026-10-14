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
