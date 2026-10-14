# y8_lnr_level — the least-non-residue level: Mordell's theorem as "the lnr level carries a χ = −1 word" (O217)

## Idea
At a non-square p some level is always unclean (y8_adelic_continuity): with q = lnr(p) and
t₀ := (−p⁻¹ mod q) ∈ [1, q − 1], q | t₀p + 1, so level t₀ (and every t₀ + kq) is unclean. ES-five(p) needs more:
an *admissible* divisor A ≡ −1 (mod t) of tp + 1 with (A/p) = −1. Construction: A = q·d with d | (tp + 1)/q,
qd ≡ −1 (mod t), (d/p) = +1.
**Lemma 1 (PROVED, elementary).** If q = lnr(p) ≤ 7 then level t₀ carries the χ = −1 word with A = q (d = 1):
q = 2 (p ≡ 5 mod 8): t₀ = 1, A = 2 | p + 1; q = 3: t₀ = 1, 3 | p + 1; q = 5: t₀ ∈ {2, 3}, A = 5 (5 ≡ −1 mod 2, mod 3);
q = 7: t₀ ∈ {1, 2, 4}, A = 7 ≡ −1 (mod 4). In each case A = q ≡ −1 (mod t₀) because t₀ | q + 1. ∎
Since {p ≡ 1 (4) prime : lnr(p) ≥ 11} = {p ≡ 1, 121, 169, 289, 361, 529 (mod 840)} (squares mod 840), Lemma 1 is
exactly Mordell's theorem restricted to ES-five, and the 840 obstruction is "lnr ≥ 11" (cf. y4_mordell_witness).
**Lemma 2 (PROVED).** For q ≥ 11 the d = 1 construction works iff t₀ | q + 1 (a congruence condition on p mod q);
otherwise the level t₀ needs a divisor d of (t₀p + 1)/q in the class −q⁻¹ (mod t₀) with (d/p) = +1 — B2.

## Literature
Mordell, *Diophantine Equations* (1969) p. 287–290; Elsholtz–Tao (2013) §2 (Type I/II and the least non-residue
heuristics); Burgess/Bach for lnr bounds; campaign y4_mordell_witness ((J)) and POINTWISE_MORDELL*.

## Barrier screen
B1: Lemma 1 is a congruence covering (Mordell's); Lemma 2 for q ≥ 11 is the divisor-in-class lottery with modulus
t₀ < q (B2), success probability bounded away from 1 at fixed p-size; the union over k is the polylog lottery (B3/B4).
T1: at p = m² there is no q, no unclean level — consistent. B6: rates are averages.

## Cheap numerics (`scripts/y8_lnr_level.py`)
Success of the lnr level t₀ (word with q | A), 3 000 random p ≡ 1 (4):
| range | q = 2,3,5,7 | q = 11 | q ≥ 13 |
|---|---|---|---|
| (10⁵, 10⁶) | 1.000 (2 802) | 0.845 (103) | 0.811 (95) |
| (10¹⁰, 10¹¹) | 1.000 (2 792) | 0.872 (109) | 0.909 (99) |
Not decaying with p. First k ≥ 0 with t₀ + kq successful, 500 primes with q ≥ 11 near 10¹⁰–10¹¹:
k = 0: 427, 1: 47, 2: 9, 3: 6, 4: 3, then sporadic up to k = 26; never > 40. Failures at k = 0 have t₀ ∤ q + 1
(t₀ ∈ {5, 9} for q = 11; {10, 11, 14} for q = 17), as Lemma 2 says. Example 2521 (q = 11, t₀ = 5):
5·2521 + 1 = 2·3·11·191 and the divisors of 1146 are ≡ 1, 2, 3 (mod 5), never 4.

## Assessment
PROVED (Lemmas 1–2) + EVIDENCE. A clean dictionary (Mordell = lnr ≤ 7 = "the lnr level is admissible for free"),
no new mechanism: for lnr ≥ 11 the lnr level is a finite-modulus lottery with success ≈ 0.85 per translate.
