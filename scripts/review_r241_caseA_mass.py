"""review_r241_caseA_mass.py (R241): Case A part of the Thm 2.2 certificate, independent of the author's fz1_caseA.py /
zc_caseA9.py. q = 9, only alpha == 0 (mod 4) (Thm 1.4 + E(0) in P8, re-derived in the review). alpha = 4: R241's own exact
count (review_r241_caseA.py; argv[1] = count used, 174 = P8 only, 268 = all off-F3 slices). 8 <= alpha <= 40: R226's own routes
(i), (ii), (v), (vi) (scripts/review_fz1_caseA.py own_routes; reviewer code, SOUND in ff-sterile-small-review-3).
alpha > 40: Lemma 7.2(b) tail over ALL alpha (no filter), as in R226's mass().
usage: review_r241_caseA_mass.py count_alpha4"""
import sys, math
from fractions import Fraction as Fr
sys.path.insert(0, 'scripts')
from review_fz1_caseA import own_routes
q = 9; c4 = int(sys.argv[1])
tot = Fr(c4, q**4); parts = {4: float(Fr(c4, q**4))}
for al in range(8, 41, 4):
    acc = 0
    for be in range(0, al + 1):
        for ka in range(0, al - be + 1):
            f = al - be - ka
            for la in range(0, max(f, be) + 1):
                acc += min(own_routes(q, al, la, be, ka))
    parts[al] = float(Fr(acc, q**al)); tot += Fr(acc, q**al)
a0 = 41
rho = ((a0 + 2) / (a0 + 1))**3 * math.sqrt(3 / q)
tail = (a0 + 1)**3 * math.sqrt(8) * q**((1 - a0) / 2) * 3**(a0 / 2) / (1 - rho) * 1.000001
print({k: f'{v:.3e}' for k, v in parts.items()})
print(f'caseA(alpha<=40, 4|alpha)={float(tot):.8f} tail(alpha>40)={tail:.3e} total={float(tot)+tail:.8f}')
