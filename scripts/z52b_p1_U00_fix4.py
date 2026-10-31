# z52b pass1 U00 fix (4): Z0133, Z0210, Z0097, Z0090, Z0156, Z1559, Z2067, Z2454, Z1372, Z0127 (see record lines).
import sys, json, math, random, itertools
sys.path.insert(0, 'scripts')
from z52b_p1_U00_solver import solutions
from sympy import primerange, factorint, legendre_symbol, isprime
import numpy as np
out = {}
def Omega(n): return sum(factorint(n).values())
# Z0133: 4/p with all three denominators semiprime (Ω=2), p ≡ 1 mod 4, p ≤ 1000
hit = []; tot = 0
for p in [q for q in primerange(5, 1000) if q % 4 == 1]:
    tot += 1
    s = solutions(p)
    ok = [t for t in s if all(Omega(v) == 2 for v in t)]
    hit.append((p, len(ok), len(s)))
out['Z0133'] = {'primes': tot, 'primes_with_all_semiprime_solution': sum(1 for h in hit if h[1] > 0),
                'examples': [h for h in hit if h[1] > 0][:10], 'primes_no_semiprime_solution_first': [h[0] for h in hit if h[1] == 0][:20]}
# Z0210: finite-field box: prime M ∈ [50, 2000], fixed p ∈ {5, 13, 17} (p ≢ 0 mod M): count (x,y,z) ∈ [1, √M]^3 with
# 1/x+1/y+1/z ≡ 4/p (mod M); report counts vs the heuristic M^{-1}·(√M)^3 = √M.
rows = []
for M in [q for q in primerange(50, 2001)][::12]:
    r = int(M ** 0.5)
    inv = lambda a: pow(a, -1, M)
    row = {'M': M}
    for pp in [5, 13, 17]:
        target = (4 * inv(pp)) % M
        cnt = 0
        for x in range(1, r + 1):
            ix = inv(x)
            for y in range(1, r + 1):
                zi = (target - ix - inv(y)) % M
                if zi == 0: continue
                z = inv(zi)
                if z <= r: cnt += 1
        row[str(pp)] = cnt
    row['heur_sqrtM'] = round(M ** 0.5, 1)
    rows.append(row)
out['Z0210'] = {'rows_sample': rows[:12], 'min_counts': {pp: min(r[str(pp)] for r in rows) for pp in [5, 13, 17]},
                'zero_count_cases': sum(1 for r in rows for pp in [5, 13, 17] if r[str(pp)] == 0), 'n_cases': 3 * len(rows)}
# Z0097: smoothness of F = 4xyz − n(xy+yz+zx) at integer solutions: gradient zero?  n = prime ≤ 500, all solutions
sing = 0; tot = 0
for p in [q for q in primerange(5, 500) if q % 4 == 1]:
    for t in solutions(p):
        x, y, z = t; tot += 1
        g = (4 * y * z - p * (y + z), 4 * x * z - p * (x + z), 4 * x * y - p * (x + y))
        if g == (0, 0, 0): sing += 1
out['Z0097'] = {'solutions_checked': tot, 'singular_points_at_solutions': sing}
# Z0090: Pell/norm units in F_3[T][√D], D = T²+1: look for a, b ∈ F_3[T], deg ≤ 3, a² − D b² = ±1 (brute force over coefficients)
import itertools as it
def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % 3
    return r
def padd(a, b):
    n = max(len(a), len(b)); return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % 3 for i in range(n)]
D = [1, 0, 1]
units = []
polys = [list(c) for d in range(4) for c in it.product(range(3), repeat=d + 1) if c[-1] != 0 or d == 0]
polys = [list(c) for d in range(4) for c in it.product(range(3), repeat=d + 1)]
for a in polys:
    a2 = pmul(a, a)
    for b in polys:
        val = padd(a2, [(-c) % 3 for c in pmul(D, pmul(b, b))])
        val = [c for c in val]
        while val and val[-1] == 0: val.pop()
        if val == [1] or val == [2]:
            units.append((a, b, val))
            if len(units) > 30: break
    if len(units) > 30: break
out['Z0090'] = {'D': 'T^2+1 over F_3', 'unit_examples(a,b,a^2-Db^2)': [(u[0], u[1], u[2]) for u in units[:6]],
                'note': 'T + sqrt(T^2+1) has norm -1 (a=T, b=1): T^2 - (T^2+1) = -1'}
# Z0156: lct of x^a y + y^b + z^c = (a+b-1)/(ab) + 1/c  (a,b,c ≥ 2): which values equal 4/n? count distinct n ≤ 1000
ns = {}
from fractions import Fraction as F
for a in range(2, 41):
    for b in range(2, 41):
        for c in range(2, 41):
            v = F(a + b - 1, a * b) + F(1, c)
            if v.numerator == 4 and v.denominator <= 1000 or (v.numerator == 4):
                n = F(4) / v
                if n.denominator == 1 and n <= 1000: ns.setdefault(int(n), []).append((a, b, c))
out['Z0156'] = {'triples_checked': 39 ** 3, 'n_with_4/n_eq_lct_le1000': len(ns), 'n_examples': {k: ns[k][:2] for k in sorted(ns)[:8]},
                'residues_mod4_of_n': sorted(set(k % 4 for k in ns))}
# Z2067: Gauss: r3(8n+3) > 0 (8n+3 = sum of three odd squares)?  n ≤ 3000 (brute force)
def r3odd(m):
    cnt = 0; r = int(m ** .5) + 1
    odd = [i for i in range(1, r + 1, 2)]
    sq = {i * i for i in range(1, r + 2)}
    for a in odd:
        for b in odd:
            c2 = m - a * a - b * b
            if c2 >= 1 and int(round(c2 ** .5)) ** 2 == c2 and int(round(c2 ** .5)) % 2 == 1: cnt += 1
    return cnt
bad = [n for n in range(0, 3001) if r3odd(8 * n + 3) == 0]
out['Z2067'] = {'n_range': '0..3000', 'n_with_no_representation': bad}
# (Z2454 is in scripts/z52b_p1_U00_fix5.py)
json.dump(out, open('data/z52b/pass1/U00/fix4.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str)[:5000])
