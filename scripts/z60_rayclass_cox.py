"""z60 RAYCLASS Prop 5.1 check: Cox Thm 7.24 h(O) = h(O_K) f/[O_K^*:O^*] prod_{l|f}(1-(d_K/l)/l) vs PARI qfbclassno,
for O of discriminant -16 C m^2, C in {1,2,3,5,6,7,10,11}, m in {3,5,7,9,15,21,105,1001} (64 pairs).
usage: uv run --with cypari2 python scripts/z60_rayclass_cox.py"""
import math, cypari2
from fractions import Fraction
pari = cypari2.Pari(); bad = 0; n = 0
for C in [1, 2, 3, 5, 6, 7, 10, 11]:
    for m in [3, 5, 7, 9, 15, 21, 105, 1001]:
        D = -16 * C * m * m; h = int(pari.qfbclassno(D))
        dK = int(pari.coredisc(D)); f = math.isqrt(D // dK); hK = int(pari.qfbclassno(dK))
        w = 6 if dK == -3 else 4 if dK == -4 else 2
        prod = Fraction(1)
        for l in [int(x) for x in pari.factor(f)[0]]: prod *= 1 - Fraction(int(pari.kronecker(dK, l)), l)
        n += 1; bad += (hK * f * prod / (w // 2) != h)
print(f"{n} pairs, mismatches {bad}")
