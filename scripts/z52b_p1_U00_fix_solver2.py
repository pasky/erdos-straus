# z52b pass1 U00 fix (2): Z0713 arrays, Z0976 QNR stats, Z1344 with a proper null (scale-matched random partner).
import sys, json, random
sys.path.insert(0, 'scripts')
from z52b_p1_U00_solver import solutions
from sympy import primerange, legendre_symbol
import numpy as np
out = {}
k1, k2 = [], []
for n in range(2, 15):
    s = solutions(n)
    c = [sum(1 for v in t if v % n == 0) for t in s]
    k1.append(sum(1 for x in c if x == 1)); k2.append(sum(1 for x in c if x == 2))
out['Z0713'] = {'n': list(range(2, 15)), 'k1': k1, 'k2': k2}
# Z0976: for p < 500 (p ≡ 1 mod 4), over all denominators d of all solutions with p ∤ d: fraction with (d/p) = -1; and for the first denominator x
dd = []; xx = []
for p in [q for q in primerange(5, 500) if q % 4 == 1]:
    for t in solutions(p):
        for v in t:
            if v % p: dd.append(legendre_symbol(v % p, p))
        if t[0] % p: xx.append(legendre_symbol(t[0] % p, p))
out['Z0976'] = {'denominators_prime_to_p': len(dd), 'frac_QNR': round(sum(1 for s_ in dd if s_ == -1) / len(dd), 4),
                'first_denominators_prime_to_p': len(xx), 'frac_first_QNR': round(sum(1 for s_ in xx if s_ == -1) / len(xx), 4)}
# Z1344 with null: for q-solution first denominator t0, the p-prediction t0·p/q; null = a random OTHER q-solution's scaled value
pr = [q for q in primerange(5, 1000) if q % 4 == 1]
random.seed(0); real = []; null = []
for p, q in zip(pr, pr[1:]):
    sp = sorted(set(t[0] for t in solutions(p))); sq = [t[0] for t in solutions(q)]
    if not sq: continue
    for i, x in enumerate(sq):
        real.append(any(abs(y - x * p / q) <= 1 for y in sp))
        xr = sq[random.randrange(len(sq))]
        null.append(any(abs(y - xr * p / q) <= 1 for y in sp))
out['Z1344'] = {'pairs': len(pr) - 1, 'n_tests': len(real), 'hit_real': round(float(np.mean(real)), 4), 'hit_null_scale_matched_random_partner': round(float(np.mean(null)), 4)}
json.dump(out, open('data/z52b/pass1/U00/fix_solver2.json', 'w'), indent=1)
print(json.dumps(out))
