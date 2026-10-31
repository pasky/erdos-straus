"""U04 pass-1 tests: Z1407 (union-find of witness templates), Z0992 (height comparison on all certificates),
Z0993 (normalised log-denominator coordinates). Complete enumeration via U_all from scriptA (imported by copy)."""
import json, math
from math import gcd
from fractions import Fraction as F
from sympy import primerange, factorint
import numpy as np
from scipy.stats import spearmanr
def divs_of(n):
    fac = factorint(n); ds = [1]
    for q, e in fac.items(): ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def egypt3(num, den):
    out = []
    g = gcd(num, den); a, b = num // g, den // g
    for d in divs_of(b * b):
        if (d + b) % a: continue
        y = (d + b) // a; dd = b * b // d
        if (dd + b) % a: continue
        z = (dd + b) // a
        if y <= z: out.append((y, z))
    return out
def U_all(n, m=4):
    res = []
    for x in range(-(-n // m), (3 * n) // m + 1):
        a, b = m * x - n, n * x
        if a <= 0: continue
        for y, z in egypt3(a, b):
            if x <= y: res.append((x, y, z))
    return res
out = {}
# Z1407: union-find over primes and witness templates (C,d): d | 4Cp+1, d ≡ -1 mod 4C, d>1
PMAX, CMAX = 3000, 12
parent = {}
def find(a):
    parent.setdefault(a, a)
    while parent[a] != a:
        parent[a] = parent[parent[a]]; a = parent[a]
    return a
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[ra] = rb
primes = [p for p in primerange(5, PMAX) if p % 4 == 1]
for p in primes:
    find(('p', p))
    for C in range(1, CMAX + 1):
        m = 4 * C; N = m * p + 1
        for d in divs_of(N):
            if d > 1 and d % m == m - 1:
                union(('p', p), ('t', C, d))
roots = {}
for p in primes:
    roots.setdefault(find(('p', p)), []).append(p)
sizes = sorted((len(v) for v in roots.values()), reverse=True)
out['Z1407'] = dict(n_primes=len(primes), n_components_among_primes=len(roots), largest_component=sizes[:5],
                    n_singletons=sum(1 for s in sizes if s == 1), note='nodes: primes p<3000 and templates (C,d), C<=12; edge p-(C,d) iff d|4Cp+1, d≡-1 (4C)')
# Z0992: heights on complete certificate sets for p<=500
rank_rows = []; agree = 0; tot = 0; mx_xyz = []
for p in primerange(5, 500):
    if p % 4 != 1: continue
    S = U_all(p)
    if not S: continue
    mx = np.array([max(s) for s in S], float); pr = np.array([s[0] * s[1] * s[2] for s in S], float)
    mx_xyz.append(float(spearmanr(mx, pr)[0]) if len(S) > 2 else 1.0)
    tot += 1
    agree += int(np.argmin(mx) == np.argmin(pr) or len(set(mx)) == 1)
out['Z0992'] = dict(n_primes=tot, mean_spearman_max_vs_xyz=round(float(np.mean(mx_xyz)), 3),
                    frac_primes_argmin_max_eq_argmin_xyz=round(agree / tot, 3))
# Z0993: normalised log coordinates over all certificates p<=1000
L = []
for p in primerange(5, 1000):
    if p % 4 != 1: continue
    for s in U_all(p):
        L.append([math.log(v) / math.log(p) for v in s])
L = np.array(L)
out['Z0993'] = dict(n=len(L), quantiles_log_x=[round(float(q), 3) for q in np.quantile(L[:, 0], [0.1, 0.5, 0.9])],
                    quantiles_log_y=[round(float(q), 3) for q in np.quantile(L[:, 1], [0.1, 0.5, 0.9])],
                    quantiles_log_z=[round(float(q), 3) for q in np.quantile(L[:, 2], [0.1, 0.5, 0.9])],
                    frac_z_le_2=round(float(np.mean(L[:, 2] <= 2.0)), 4),
                    frac_x_le_1=round(float(np.mean(L[:, 0] <= 1.0)), 4),
                    note='complete enumeration: no bounded box is missed; quantiles of log_p(x),log_p(y),log_p(z)')
json.dump(out, open('data/z52b/pass1/U04/scriptB.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str))
