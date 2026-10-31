"""z52b pass-1 batch U08, item Z0143 follow-up: which n <= 1000 admit 4/n = 1/x + 1/y + 1/z^2 with z <= 600 (brute force,
independent of the divisor method), and is the failure set a congruence/Legendre pattern?
Output: data/z52b/pass1/U08/z0143_scan.json"""
import json, math, os
from fractions import Fraction as F
from sympy import primerange, legendre_symbol, isprime
OUT = "data/z52b/pass1/U08"
def bf(n, zmax):
    for z in range(1, zmax + 1):
        r = F(4, n) - F(1, z * z)
        if r <= 0:
            continue
        lo = math.floor(1 / r) + 1; hi = math.floor(2 / r)
        for x in range(lo, hi + 1):
            s = r - F(1, x)
            if s > 0 and s.numerator == 1:
                return (x, s.denominator, z)
    return None
fails, sols = [], {}
for n in range(2, 1001):
    w = bf(n, 600)
    if w is None:
        fails.append(n)
    else:
        sols[n] = w[2]
fp = [n for n in fails if isprime(n)]
pr1 = [n for n in primerange(3, 1001) if n % 4 == 1]
res = dict(n_range="2..1000", zmax=600, n_fail=len(fails), fails_first=fails[:60],
           prime_fails=fp, prime1mod4_fail=[n for n in pr1 if n in set(fails)],
           prime1mod4_n=len(pr1), prime3mod4_fail=[n for n in fp if n % 4 == 3])
# Legendre-symbol profile among primes ≡ 1 (4): failure rate by (q/n) for small q
prof = {}
for q in [2, 3, 5, 7, 11, 13]:
    for s in (1, -1):
        sel = [n for n in pr1 if legendre_symbol(q % n, n) == s]
        if sel:
            prof[f"({q}/n)={s:+d}"] = (len(sel), round(sum(1 for n in sel if n in set(fails)) / len(sel), 3))
res["fail_rate_by_legendre_pr1mod4"] = prof
os.makedirs(OUT, exist_ok=True)
json.dump(res, open(os.path.join(OUT, "z0143_scan.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
