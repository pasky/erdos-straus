# y7_mordell_levels — the identity-hard core of 7/n is the class of one; for 4/n it is the square coset (O215)

## Idea
Run the classical Mordell covering (one-parameter ET-shaped identity families, all moduli dividing L) for each
numerator M and look at the *shape* of the uncovered set. For M = 4 at L = 840 it is Mordell's six square classes.
If 7 has a structurally different hard core, that is 7's own "input-shaped" feature.

## Families (identities PROVED by one line each; no coprimality needed)
Type II: M·abd = n + e, a + b = ce ⇒ M/n = 1/(abd) + 1/(acdn) + 1/(bcdn). Type I: M·abd = ne + 1, a + b = ce ⇒
M/n = 1/(abdn) + 1/(acd) + 1/(bcd). One free parameter gives an arithmetic progression of n:
| name | free | class of n | modulus |
|---|---|---|---|
| II-d | d | −e, e ∣ a+b | M·a·b |
| II-c | c (b = ce − a) | −M a²d − e | M·a·d·e |
| II-e | e (b = ce − a) | −M a²d | g = M·a·c·d − 1 (≡ −1 mod M; contains the square-shot family as d = □, R-O215 D1) |
| I-d | d | −e⁻¹, e ∣ a+b, gcd(e, Mab) = 1 | M·a·b |
| I-c | c (b = ce − a) | −(M a²d + 1)/e, e ∣ M a²d + 1 | M·a·d |
Positivity: for every n ≥ 1 in the class all denominators are positive (e.g. II-e: b = (cn + a)/g > 0; I-c:
b = (ne + 1)/(Mad) > 0). So a class covered at level L is solved for **every** n in it, small n included.

## Result (PROVED by exhaustive finite enumeration + exact certificates; `scripts/y7_mordell_cover.py`,
`scripts/y7_cover_verify.py`)
| M | L | unit classes | uncovered | shape of uncovered set |
|---|---|---|---|---|
| 4 | 840 | 192 | 6 | exactly the 6 unit squares (Mordell) |
| 4 | 1680, 2520 | 384, 576 | 12, 18 | exactly the unit squares |
| **7** | **840** | 192 | **4** | **exactly n ≡ 1 (mod 105)**: 1, 211, 421, 631 (one square) |
| 7 | 2520 | 576 | 10 | inside n ≡ 1 (mod 210) (12 lifts, 2 covered via 9) |
| 5 | 840 | 192 | 2 | n ≡ 1 (mod 420) |
| 6 | 840 | 192 | 11 | 1 square + 10 non-squares |
| 8 | 840 | 192 | 23 | all 6 squares + 17 non-squares (contains 11, 17, 131, 241 — the failures) |
| 11 | 9240 | 1920 | 28 | 1 square + 27 others, contains 37 (the failure) |
| 12 | 840 | 192 | 44 | all 6 squares + 38 others |
| 3 | 840 | 192 | 0 | — |
**Sharper (SEVEN_SIBLING Thm 3.1):** the core is exactly the class of one already at levels 14 (n ≢ 1 mod 7), 42 (+ n ≢ 1 mod 3) and 70 (+ n ≢ 1 mod 5); explicit families there. Near misses 7/43, 7/127 have exactly one solution each, the level-70 identity.
**Theorem Y7.1 (PROVED).** For every n ≥ 1 with gcd(n, 210) = 1 (so n odd) and n ≢ 1 (mod 105), 7/n = 1/x + 1/y + 1/z has a
solution, given explicitly by one of the five families with modulus dividing 840.
Verification (CERTIFIED): every prime 11 ≤ p ≤ 10⁶ with p ≢ 1 (mod 105) gets an exact certificate (Fraction check),
76 871 primes; the 1 623 uncertified primes are exactly those ≡ 1 (mod 105). Same harness for M = 4, p ≤ 10⁵:
uncertified residues = Mordell's six. (Novelty not claimed: PW sift with "the seven congruences of ET Prop 1.9 with 4
replaced by m"; covering results of this kind for m/n are classical — Sierpiński/Stewart-type.)

## Reading: two different hard cores
* For 4 (and 8, 12) the hard core **contains the whole square coset**, and must (Schinzel / ET Prop 1.6 / T1): a
  quadratic, "Hilbert-symbol" obstruction. Its size at level L is 2^{−ω(L)}-ish.
* For 7 the hard core at 840 is **exactly the fibre n ≡ 1 (mod 105)** (4 classes). Lemma 3.1 of ident_numerators
  (n ≡ 1 is in no ET-shaped family for m ≥ 4) forces only the residue 1 mod 840; the other three survivors are a verified
  feature of this menu (R-O215 D4). At levels 14, 42, 70, 210 the survivor set is exactly {1}. Density 4/192 = 1/48.
* So: P(M) := "at level lcm(840, M) the uncovered unit set is empty, or the full unit-square set, or a single fibre
  {n ≡ 1 mod L′}" (7: L′ = 105; 5: L′ = 420). P(3), P(4), P(5), P(7); ¬P(6), ¬P(8), ¬P(11), ¬P(12) (tested M only).
  This is the cleanest property found with P(4) ∧ P(7) ∧ ¬P(8) ∧ ¬P(11) ∧ ¬P(12). It is a **description** (a finite
  computation at a fixed level), not an input: covering a residue class is B1, and the hard cores are infinite.
* The near-miss primes of 7 live there: S₇(p) = ∅ at 43, 127, 211, 421, 463, 631, 967, 4201, 9661, 12601 — all
  ≡ 1 (mod 42); 211, 421, 631, 4201, 9661, 12601 ≡ 1 (mod 105). See y7_near_misses.

## Barrier screen
B1 exactly: finite congruence covering; the class of one is never covered (Lemma 3.1), so a finite menu leaves
infinitely many primes (Dirichlet). Observed per-prime coverage at level 840ℓ is 2–9 classes for 11 ≤ ℓ ≤ 31 (SEVEN_SIBLING §3.3);
that it stays bounded is a heuristic (Thm M-type count), not proved here. The sharpness of P looks like a small-level
accident, like Mordell's 840 (cf. y4_mordell_witness). T1: 7's core contains one square class only, consistent with 7 lacking
full T1 (y7_full_t1). B6: n/a. Nothing escapes B2.

## Assessment
PROVED (Thm Y7.1) + CERTIFIED (10⁶). **SHARP as a dictionary**: the identity-hard core is quadratic (squares) for 4 and
multiplicative-trivial (class of one) for 7, for this menu. Not an existence mechanism.
All-integer check (R-O215 D10): `cd scripts; python3 y7_cover_verify.py 7 L 300000 all` for L ∈ {14, 210}: every n ≤ 3·10⁵
coprime to 7L is certified except exactly the residue class 1 mod L (107 142 resp. 67 142 certified).
