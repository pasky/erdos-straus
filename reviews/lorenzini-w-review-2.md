# R184 — independent hostile review (reviewer 2 of 2) of O180 `LORENZINI_W.md`

Reviewer: side-agent `review-lorenzini-2`. Did NOT read `reviews/lorenzini-w-review.md`.
From-scratch code: `scripts/review_lw2_cover.py`, `scripts/review_lw2_brute.c` (+ further `review_lw2_*` below).
Source checked: `sources/lorenzini/CriticalPolynomialOfAGraph.txt` (arXiv:2311.06367 text), Example 6.2(a), Prop 6.3, Remark 6.4.

## Summary verdicts
| claim | verdict |
|---|---|
| Thm 9.1 (even n ≥ 16, n ≠ 510, are values) | **SOUND** (proof re-derived end to end; minor presentational defects only) |
| Novelty of Thm 9.1 | see §2 |
| Prop 8.1 / Cor 8.2 | see §3 |
| Prop 6.1 | see §4 |

## 1. Theorem 9.1 — re-derivation (SOUND)

**Reduction (checked against Lorenzini's exact statement).** Lorenzini Prop 6.3(a) (p. 24): "V_{A₃}(2) contains all even positive
integers n, except possibly those of the form n = 2^m − 2 with m odd or m = 2, 4." His proof: z = 2 gives x(2y − 1) = n + 2, solvable
with x, y ≥ 2 when n + 2 is neither prime nor a 2-power; for even m > 4 the word (4, (2^{m−3}+1)/3, 6). I re-derived both:
for even n, n + 2 is even (never prime for n ≥ 2), so if n + 2 = 2^a·u with u ≥ 3 odd take 2y − 1 = u, x = 2^a ≥ 2; and
24·(2^{m−3}+1)/3 − 10 = 2^m − 2 with 3 | 2^{m−3}+1 ⟺ m − 3 odd, y ≥ 2 ⟺ m ≥ 6. m = 2, 4 give n = 2, 14 (excluded by n ≥ 16).
So the residue is exactly n = 2^m − 2, m odd, as the author states. No hidden hypothesis.

**The six families (symbolic).** With n = 2^m − 2:
* (x,z) = (3,3): 9y − 6 = n ⟺ 9 | 2^m + 4 ⟺ 2^m ≡ 5 (mod 9) ⟺ m ≡ 5 (mod 6) (2^k mod 9: 2,4,8,7,5,1).
* (x,z) = (6,12): 72y − 18 = n ⟺ 72 | 2^m + 16 ⟺ (m ≥ 3) ∧ 2^m ≡ 2 (mod 9) ⟺ m ≥ 3, m ≡ 1 (mod 6).
* (x,y) = (7,2): 13z − 7 = n ⟺ 13 | 2^m + 5 ⟺ 2^m ≡ 8 (mod 13) ⟺ m ≡ 3 (mod 12) (ord₁₃2 = 12).
* (x,z) = (3,9): 27y − 12 = n ⟺ 27 | 2^m + 10 ⟺ 2^m ≡ 17 (mod 27) ⟺ m ≡ 15 (mod 18) (ord₂₇2 = 18).
* (x,y) = (10,11): 109z − 10 = n ⟺ 109 | 2^m + 8 ⟺ m ≡ 21 (mod 36) (ord₁₀₉2 = 36).
* (x,z) = (8,74): 592y − 82 = n ⟺ 16 | 2^m + 80 ∧ 37 | 2^m + 80 ⟺ m ≥ 4 ∧ 2^m ≡ 31 (mod 37) ⟺ m ≥ 4, m ≡ 9 (mod 36).
`review_lw2_cover.py` recomputes each m-class set by direct evaluation of 2^m over 4 periods at two windows (m ∈ [11,155) and
[1001,1145)): the sets agree with the table, and their union is **all 18 odd classes mod 36** (residue classes: 6+6+3+2+1+1 = 19 with
one overlap, 15 covered twice). Orders ord₉ = 6, ord₁₃ = 12, ord₂₇ = 18, ord₃₇ = ord₁₀₉ = 36 confirmed.

**Size thresholds.** Third letter ≥ 2 ⟺ n ≥ 2d − x ((x,y) kind) or n ≥ 2xz − x − z ((x,z) kind); the worst is (8,74): n ≥ 1102.
m ≥ 11 gives n ≥ 2046. ✓. Fixed letters are all ≥ 2. ✓. Explicit (x,y,z) with exact integers verified for every odd m ≤ 4001:
the only failures are m = 1, 3, 9 (n = 0, 6, 510), exactly the stated exceptions; m = 5, 7 are in fact also caught by families
(3,3) and (6,12). Brute force for m ≤ 11: n = 30 → (3,4,3) only; 126 → (6,2,12),(12,2,6); 510 → none; 2046 → (3,228,3),(8,10,26),(26,10,8).

**Independent brute force (`review_lw2_brute.c`, x ≤ z symmetric enumeration, 16 s).** All n ≤ **10⁸**: the non-values are exactly
{0, 2, 6, 14, 510} (even) and {1, 3, 5, 9, 11, 15, 35, 105} (odd). This matches L_{A₃} of Lorenzini Ex. 6.2(a) and the even
statement of Thm 9.1 including "the even part of the complement is exactly {0, 2, 6, 14, 510}".

**Verdict: SOUND.** The proof is complete and elementary; I found no quantifier or threshold error.
Minor defects (presentation only) listed in §5 (D1–D2).
