# s5_scale_law — the sign ratio's slow drift at primes is the forced fraction; on unforced words it is scale-stable (own idea, O230)

## Idea
(J)39 Lemma 2.1: averaged over all odd n, Σ N₋ : Σ N₊ = 15 : 5, so N₋/N → 3/4 (240 of the 320 odd cells mod 8). At
primes p ≡ 1 (mod 4) the observed N₋/N is far lower and creeps up slowly. Split the words into forced (on a clean side,
s5_three_sides) and unforced (U, s5_unforced_words).

## Data (EVIDENCE; s5_sides.c, all 1 029 thousand primes p ≡ 1 (mod 4), 5 < p < 3·10⁷, dyadic blocks)
| block 2^b | primes | forced fraction | N₋/N | N₋/U | forced·√(log p) |
|---|---|---|---|---|---|
| b = 10 | 66 | 0.209 | 0.591 | 0.747 | 0.56 |
| b = 14 | 805 | 0.167 | 0.623 | 0.747 | 0.53 |
| b = 17 | 5 378 | 0.149 | 0.639 | 0.750 | 0.52 |
| b = 20 | 36 827 | 0.131 | 0.654 | 0.753 | 0.49 |
| b = 22 | 133 975 | 0.121 | 0.662 | 0.753 | 0.48 |
| b = 24 | 390 016 | 0.114 | 0.668 | 0.754 | 0.47 |
* Split by p mod 8, cumulative over the ranges (≤ 10⁵ / ≤ 10⁶ / (10⁵, 5·10⁶) / (5·10⁶, 3·10⁷)):
  * N₋/U = 0.769 / 0.771 / 0.770 / 0.770 for p ≡ 1 (8);
  * N₋/U = 0.733 / 0.737 / 0.738 / 0.740 for p ≡ 5 (8).
* Words: 32.9 M in (10⁵, 5·10⁶) and about 160 M in total.

## Law (EVIDENCE + heuristic)
* **N₋/U is scale-stable (0.747 → 0.754 over 2¹⁰ to 2²⁴), while N₋/N drifts (0.59 → 0.67).** The whole drift is the
  forced fraction, which decays roughly like 0.5/√(log p) (Landau-type: a side number is clean with probability
  ≍ (log)^{−1/2}). The slow downward trend of forced·√log suggests an extra log log factor; this is not fitted.
* Prediction: N₋/N → ≈ 0.75 (the (J)39 cell average) as p → ∞, with a (log p)^{−1/2} deficit. Forced words are exactly
  the "missing certificates" at primes relative to the all-n average.
* The p mod 8 split 0.770 / 0.739 is stable and reflects the 2-adic cell proportions of unforced words. It is not
  derived here.

## Literature
(J)39 Lemma 2.1 (cell average). Landau–Ramanujan-type densities for integers composed of primes in a half set of
classes (Serre's "Divisibilité de certaines fonctions arithmétiques" for the (log)^{−1/2} order).

## Barrier screen
* B6: these are averages over p; nothing is forced at a single p.
* T1: forced fraction = 1 at squares.
* B3: no main-term certificate is proposed.

## Cheap numerics
The table above comes from the s5_sides outputs (tiny awk over /tmp files; the reproducing command is in
SYNTHESIS_SPARKS5 §3).

## Assessment
A clean descriptive law, EVIDENCE. It sharpens the lottery model: **at a prime, the certificate lottery runs only over
unforced words, with a stable success rate ≈ 3/4 per word**, and the hardness is concentrated in the forced fraction.
Steering: a heuristic for f(p) or for record-hard primes should model U(p), not N(p). This is not an existence
mechanism.
