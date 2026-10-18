# z40_pierpont_cover.py (O270): search a finite 2D covering of n(a,b) = 2^a 3^b + 1, a >= A0, b >= B0, by cells
# (a mod L, b mod L) using: cyclotomic descent (odd p | gcd(a,b)), the Theorem-B/C window-11 rules at (0,1)
# (a = 0 (4), b = 1 (4), X = 2^{(a-4)/4} 3^{(b-1)/4} not = 0, +-1 mod 11), divisor classes q | n, and ET classes mod M.
# Usage: z40_pierpont_cover.py L Mmax A0 B0 [OUT.json [RESIDUAL_IN.json]]
import sys, json, functools
from math import lcm
import mordell_lib as ML
from sympy import n_order, primerange, factorint
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
L, Mmax, A0, B0 = map(int, sys.argv[1:5]); OUT = sys.argv[5] if len(sys.argv) > 5 else None
def rep(i, base):            # representative exponent >= base in class i mod L
    return i + L * (base // L + 2)
cells = {(i, j) for i in range(L) for j in range(L)}
if len(sys.argv) > 6:          # restrict to lifts of a residual list from a previous run (JSON with L, left)
    R = json.load(open(sys.argv[6])); L0 = R['L']; assert L % L0 == 0
    cells = {(i + L0 * u, j + L0 * v) for i, j in R['left'] for u in range(L // L0) for v in range(L // L0)}
def nmod(i, j, M):
    return (pow(2, rep(i, 64), M) * pow(3, rep(j, 64), M) + 1) % M
covered = {}
# descent
for p in factorint(L):
    if p > 2:
        for (i, j) in cells:
            if i % p == 0 and j % p == 0: covered.setdefault((i, j), ('desc', p))
# windows (need 40 | L for a, 20 | L for b)
if L % 40 == 0:
    for (i, j) in cells:
        if i % 4 == 0 and j % 4 == 1:
            X = pow(2, ((rep(i, 64) - 4) // 4) % 10, 11) * pow(3, ((rep(j, 64) - 1) // 4) % 5, 11) % 11
            if X not in (0, 1, 10): covered.setdefault((i, j), ('win', X))
# admissible odd prime powers q^e (q != 3) with 2^L = 3^L = 1 mod q^e
pp = []
for q in primerange(5, Mmax + 1):
    if pow(2, L, q) == 1 and pow(3, L, q) == 1:
        Q = q
        while Q * q <= Mmax and pow(2, L, Q * q) == 1 and pow(3, L, Q * q) == 1: Q *= q
        pp.append((q, Q))
print('admissible primes', [q for q, _ in pp][:40], len(pp), flush=True)
sets = []
for q, Q in pp:
    st = {c for c in cells if nmod(*c, q) == 0}
    if st: sets.append((q, ('D', (q,)), st))
odd = [1]
for q, Q in pp:
    new = []
    for d in odd:
        x = d
        while x * q <= Mmax and Q % (x * q // d) == 0:
            x *= q; new.append(x)
    odd += new
Ms = sorted({2 ** u * 3 ** v * d for u in range(0, A0 + 1) for v in range(0, B0 + 1) for d in odd if 2 < 2 ** u * 3 ** v * d <= Mmax})
for M in Ms:
    if M % 4 not in (0, 3): continue
    W = ML.residue_table(M); cv = {}
    for c in cells:
        r = nmod(*c, M)
        if r in W: cv.setdefault(W[r], set()).add(c)
    for cls, st in cv.items(): sets.append((M, cls, st))
unc = cells - set(covered)
allc = set().union(*[s for _, _, s in sets]) if sets else set()
left = unc - allc
print('L=%d cells %d; descent/window %d; ET-uncoverable %d' % (L, len(cells), len(covered), len(left)), flush=True)
print('sample uncovered:', sorted(left)[:40])
chosen = []; u = unc & allc
while u:
    M, cls, st = max(sets, key=lambda t: (len(u & t[2]), -t[0])); chosen.append((M, cls, sorted(st & u))); u -= st
print('ET/divisor classes chosen %d, moduli %s' % (len(chosen), sorted({m for m, _, _ in chosen})))
if OUT:
    json.dump({'L': L, 'A0': A0, 'B0': B0, 'left': sorted(left), 'special': {'%d,%d' % k: v for k, v in covered.items()},
               'classes': [{'M': M, 'fam': cls[0], 'params': list(cls[1]), 'cells': [list(c) for c in st]} for M, cls, st in chosen]},
              open(OUT, 'w'))
