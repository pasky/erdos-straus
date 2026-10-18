# z36 — Drop the character instead of the length: the numerator-free L = 3 rung is Lorenzini's (W) (O266 memo 5)

## Idea
Relax ES-five along the other axis: keep HJ length 3, drop the Jacobi condition. Then L₃(n) ≠ ∅ ⟺ n = tuv − u − v
(t, u, v ≥ 2) ⟺ t/n = 1/(uv) + 1/(un) + 1/(vn) for some t ≥ 2 ⟺ ∃ t: tn + 1 = (tu − 1)(tv − 1).

## Literature
Already in the campaign: (J)15 / DISCOVERIES l. 634 — this is **Lorenzini's question** (arXiv:2311.06367, Example 6.2(a)),
conjectured exceptional set {0, 1, 2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510}; even n proved (bsG_even_half Thm 9.1:
every even n ≥ 16 except 510). R174 checked to 10⁹.

## Content
At each t the event is a B2 divisor event (tn + 1 has a divisor ≡ −1 (mod t) with cofactor ≥ 2t − 1); the t ≡ 0 (4)
sub-union is the (★) line. With all t allowed the union is far more robust (12 exceptions ≤ 2·10⁶ vs 14 for (★) ≤ 10¹⁰),
but no pointwise mechanism is known for odd n. T1: odd squares are *not* exceptions here (L₃(997²) has 97 words): the
character is what makes ES T1-bearing; the length is what makes it a lottery.

## Cheap numerics (`scripts/z36_numfree.py 2000000`)
Exceptions ≤ 2·10⁶: exactly {1, 2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510} (agrees with Lorenzini/R174).

## Assessment
No new claim (re-derivation of a known item; recorded so that the two ES relaxation axes are on one page:
character-free = Lorenzini (B2 lottery, open), length-free = Theorem A (theorem)).
