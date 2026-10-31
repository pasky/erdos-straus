"""Z2562 control: P(-1 divisor | max-order prime factor) stratified by tau(N), C<=20, p=1 mod 4 < 1500."""
import sys, math, json
from collections import defaultdict
from sympy import primerange, divisors, factorint
from math import lcm
def carm(m):
    e = 1
    for a in range(1, m):
        if math.gcd(a, m) == 1:
            o = 1; x = a % m
            while x != 1 % m:
                x = x * a % m; o += 1
            e = lcm(e, o)
    return e
st = defaultdict(lambda: [0, 0, 0, 0])  # tau -> [n_with, hits_with, n_without, hits_without]
for C in range(1, 21):
    m = 4 * C; lam = carm(m); fl = factorint(lam)
    for p in [q for q in primerange(5, 1500) if q % 4 == 1]:
        N = 4 * C * p + 1; f = factorint(N); tau = 1
        for e in f.values(): tau *= e + 1
        has = any(pow(q % m, lam, m) == 1 and all(pow(q % m, lam // r, m) != 1 for r in fl) for q in f) if lam > 1 else True
        mi = any(1 < d < N and (d - (m - 1)) % m == 0 for d in divisors(N))
        s = st[tau]
        if has: s[0] += 1; s[1] += mi
        else: s[2] += 1; s[3] += mi
out = {}
for tau in sorted(st):
    a, b, c, d = st[tau]
    if a + c >= 30:
        out[tau] = {'with': a, 'P_minus1_with': round(b / a, 3) if a else None, 'without': c, 'P_minus1_without': round(d / c, 3) if c else None}
print(json.dumps(out))
json.dump(out, open('data/z52b/pass1/U02/Z2562_control.json', 'w'), indent=1)
