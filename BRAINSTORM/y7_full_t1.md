# y7_full_t1 — 7 is T1-bearing only on the shot subfamily; full T1 is a 4 | M property (O215)

## Idea
O212 Prop 1.1 calls 7 "T1-bearing": its odd-g shot family (II-e of y7_mordell_levels: g = 7acd − 1 | n + 7a²d) is
sterile at odd squares. Check whether the WHOLE ET-shaped Type I/II family of 7/n is sterile at squares, as for 4.

## Computation (`scripts/y7_full_t1.py M 99 200`; exact divisor search)
Odd squares n = k², 3 ≤ k ≤ 99, gcd(k, 2M) = 1. Type II: M·abd = n + e, e | a + b (complete in e). Type I:
M·abd = ne + 1, e | a + b (e ≤ 200).
| M | squares | with Type II | with Type I |
|---|---|---|---|
| 4 | 49 | 0 | 0 |
| 8 | 49 | 0 | 0 |
| 12 | 32 | 0 | 0 |
| **7** | 42 | **41** (first 25) | **42** (first 9: 7/9 = 1/2 + 1/4 + 1/36, a, b, c, d, e = 1, 2, 1, 2, 3) |
| 11 | 44 | 36 | 42 |
| 5 | 39 | 39 | 39 |
| 6 | 32 | 30 | 32 |
For 4 | M the zero rows are theorems (ET Prop 1.6 for M = 4; POINTWISE_MN Lemma 1.1(d) for Type II, 4 | M); for 7, 11
the non-zero rows are explicit certificates (CERTIFIED).

## Reading
* **Full T1 ⟺ 4 | M** (PROVED for Type II and M = 4 Type I; EVIDENCE for Type I, M = 8, 12). The "−M is a
  discriminant" T1 of O212 lives only on the shot subfamily, and for M ≡ 3 (mod 4) the other four families
  (II-d, II-c, I-d, I-c) carry squares freely.
* So 7 is not "4's T1 sibling" in the strong sense: its identity families reach squares (y7_mordell_levels: only one
  square class mod 840 is uncovered, namely 1).
* Corrected sibling table: the failure-free numerators ≤ 10⁸ (3, 4, 5, 6, 7) include exactly one with full T1 (4).
  The numerators with full T1 are 4, 8, 12, 16, 20, 24, … and all except 4 fail.

## Barrier screen
B5/T1 is the steering point: a Type I/II proof route for 7/p has no step that must be false at squares. That
removes one barrier for 7 but not B1 (class of one, Lemma 3.1), B2 or B3.

## Assessment
PROVED/CERTIFIED as above. Important correction to the framing of O212 spark 1 ("7 is T1-bearing"): only partially.
A 7/n proof does NOT need a T1-breaking input; a 4/n proof does. So "7/n" is a strictly easier model problem
from the barrier point of view, and its failure-free record says nothing about 4's T1 problem.
