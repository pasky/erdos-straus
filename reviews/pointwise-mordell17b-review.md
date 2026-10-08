# Hostile review R93 of POINTWISE_MORDELL17B.md (task O93)

Reviewer: R93 (branch `side-agent/review-m17b`). Document reviewed at the merge of
`side-agent/r17-explicit-tail` into this branch. From-scratch scripts: `scripts/review_m17b_*`.

## Summary verdicts

(filled in claim by claim below; final table at the end)

## Claim (1): Lemma 2.1 and the P-enumerator

**Re-derivation of `acde ≤ n`.** For an N-point of `Σ^II_n` (`4abcd = a+b+nc`, `e = (a+b)/c`), dividing
by c gives `4abd = n+e`. As `c ≥ 1`, `e ≤ a+b ≤ 2b ≤ 2abd` (using `a ≤ b`, `a, d ≥ 1`), so
`4abd ≤ n + 2abd`, `abd ≤ n/2`, and `acde = ad(a+b) ≤ 2abd ≤ n`. Only the equation and positivity are
used. Then `e²·(ad)(ac)(cd) = (acde)² ≤ n²`. If all four quantities exceeded their thresholds the product
would be `> X_e² X_ad X_ac X_cd ≥ n²`. So the cover is correct. VERIFIED.

**Recovery formulas.** `e`: `4abd = n+e` (above). `ad`: `ef = n+4a²d` with `f = 4acd−1` (ET (2.19)/(2.20)
area; re-derived: `e(4acd−1) = 4acde − e = 4ad(a+b) − e = 4a²d + (4abd − e) = 4a²d + n`). `ac`: from
`b(4acd−1) = a + nc`. `cd`: `(4acd−1)(4bcd−1) = 16abc²d² − 4cd(a+b) + 1 = 4cd(4abcd − a − b) + 1 = 4c²dn + 1`.
All four are correct, and each regime recovers the whole point from the pair plus a divisor. VERIFIED.

**Code reading (`m17b_penum.py`).** The thresholds are exact integers with `Xo⁴·Xcd ≥ n²` asserted. In each regime the
loops cover all pairs with product ≤ X, and all divisors of the factored number. Skipping `17 | d` (ad), `17 | c` (ac)
and `17 | cd` (cd) is legitimate, since such points are discarded anyway. The `e`-regime restriction `a² ≤ abd` is
implied by `a ≤ b`. Every output is re-checked against the equation. No defect found.

**Independent test.** `scripts/review_m17b_brute.c` is a naive scan that does *not* use the cover. For every `a ≤ b`
with `4ab ≤ n+a+b`, `e` is forced to be the least positive residue of `−n mod 4ab`, since `0 < e ≤ a+b < 4ab`.
Then `d = (n+e)/(4ab)`, `c = (a+b)/e`, and the equation is checked in 128-bit.
Results, compared with `m17b_penum.py` **as sets of (a,b,c,d)**:
* K = 1, 3, 5, 7: 2, 32, 121, 258 data; set-equal.
* K = 2, 4, 6: 0 data (consistent with M17 Lemma 1.3).
