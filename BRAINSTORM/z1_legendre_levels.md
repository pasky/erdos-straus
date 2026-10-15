# z1_legendre_levels — Legendre's three-square obstruction as a character-free slice (O224)

## Idea
TWO_FIBRES Thm A ((J)48): a word w = (t, u, v) of odd n has χ(w) = +1 iff there are x, y ∈ ℤ³ with |x|² = A* = tv − 1,
|y|² = A = tu − 1, x·y = 1. Then |x × y|² = AA* − 1 = tn. So if **tn is not a sum of three squares**, i.e.
tn = 4^a(8b + 7) (Legendre–Gauss), every word at level t has χ = −1, with no character to check. Call such t a *Legendre
level* of n. The "archimedean/ℤ³ input" here is the one-class genus of I₃ in its crudest form (which integers it represents).
For p ≡ 1 (mod 8) the Legendre levels are t = 4^a t′ with t′ ≡ 7 (mod 8); for p ≡ 5 (mod 8), t′ ≡ 3 (mod 8).

## Literature
Legendre (1798) / Gauss DA §291 (three-square theorem); TWO_FIBRES Thm A, Thm B, and **§3.1** (R229 repair, D13: the three-squares
obstruction on A or A* is already there as a "PROVED sufficient condition; nothing new". New here is only the level-wise form,
all words at a level, and the 7-prime failure list); THREE_SQUARES Lemma 1.1 (clean levels:
the *other* deterministic extreme, levels where every word has χ = +1).

## Results
**Prop 1 (PROVED).** If t is a Legendre level of the odd integer n, every word of X_n at level t is an ES five-slice
certificate (χ = −1). *Proof.* Thm A plus the cross-product norm identity. ∎ (Direct check: t′ ≡ −n (mod 8) with
a = 0 gives tn + 1 ≡ 1 − n² ≡ 0 (mod 8), so 4 | A or 4 | A* — the word is in the A-slice; for a ≥ 1, 4 | t, the T-slice.
So Legendre levels lie inside the five slices: Prop 1 re-derives part of MODEL_SPECIFIC Thm 3.1 from Legendre.)
**Cor 2 (T1 in Legendre form; PROVED).** For an odd square n = m² and a Legendre level t (t ≡ 7 mod 8 after removing 4^a),
tm² + 1 has **no** divisor pair A·A* with A ≡ A* ≡ −1 (mod t). *Proof.* Such a pair is a word, which has χ = −1 by
Prop 1 and χ = +1 by T1 (CHI_FLIP Cor 1.3). ∎ (Equivalently ET's T1 argument restricted to these levels.)

## Barrier screen
"Some Legendre level of p carries a word" is a pure divisor-in-a-moving-class event (B2) with *no* character condition:
the cleanest possible sub-lottery of ES-five. It must fail at squares (Cor 2, T1-safe), and it does fail at primes:
**EVIDENCE (`scripts/z1_legendre.c`):** among the 39 175 primes p ≡ 1 (mod 4) below 10⁶, exactly 7 have no word at any
Legendre level: **73, 1201, 1489, 9649, 21169, 23041, 44641** (all ≡ 1 mod 8; checked over all levels t ≤ p + 2). The
least Legendre level carrying a word is < 8 for 89 % of these primes, but reaches 7119 at p = 704761. Odd squares
9 ≤ m² ≤ 10⁸, levels ≤ 3000: 0 words at Legendre levels (Cor 2 confirmed). For 8/p, the Legendre-level words with 8 | some
pentagon quantity are missing at 202 primes ≤ 10⁶ (levels ≤ 1000).
B1: a fixed finite set of Legendre levels is a congruence covering (fails i.o., POINTWISE_SIZE Thm M). B6: no averaging.

## Cheap numerics
`gcc -O2 scripts/z1_legendre.c`; `z1_legendre 1000000 1000 0` (primes), `z1_legendre 100000000 3000 1` (squares),
`z1_legendre p 2000000 2` (single n, full range; output in `data/z1/legendre_big.txt`).

## Assessment
PROVED dictionary (Prop 1, Cor 2), EVIDENCE that the character-free sub-lottery fails (7 primes ≤ 10⁶, from p = 73 on).
So stripping the character away does not remove the lottery: the B2 divisor event is the obstruction, not the sign.
The "4" of Legendre's 4^a(8b+7) is the T-slice, so this is one more appearance of the same 2-adic input, not a new one.
Promise 1/5.
