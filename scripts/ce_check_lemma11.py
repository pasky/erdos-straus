"""Lemma 1.1 check: odd unimodular <a1,a2,a3> over Z_2 (a_i in {1,3,5,7}) is isotropic iff not all a_i equal mod 4;
and then exactly two classes x mod 2 with Q(x) = 0 mod 4."""
from itertools import product
from cf_lib import ternary_aniso
bad = 0
for a in product((1, 3, 5, 7), repeat=3):
    iso = not ternary_aniso(list(a), 2)
    crit = len({x % 4 for x in a}) > 1
    cnt = sum(1 for x in product((0, 1), repeat=3) if any(x) and sum(ai * xi for ai, xi in zip(a, x)) % 4 == 0)
    if iso != crit or (crit and cnt != 2) or (not crit and cnt != 0):
        bad += 1; print('BAD', a, iso, crit, cnt)
print('triples', 4 ** 3, 'bad', bad)
