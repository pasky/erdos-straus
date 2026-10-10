"""R131: (a) spot-check the author's columns_2e4.npz against own computations (brute-force tuples n<=3000,
own Hurwitz class numbers, own tau); (b) EXACT rank over Q (fraction-free Bareiss, Python ints) of C, E, C∪E on
500 own-random rows per row set; (c) injectivity of the row restriction on span E (rational kernel of E on the
subset re-checked exactly on all rows of the set)."""
import sys, numpy as np
from fractions import Fraction
from math import gcd, isqrt
from collections import defaultdict
from sympy import isprime, divisor_count
Z = np.load('data/exf/columns_2e4.npz'); keys = list(Z.keys())
E = [k for k in keys if k.startswith('ES:')]; C = [k for k in keys if k.startswith('C:')]; N = 20000
# ---- (a) spot checks
def H12(D):  # 12*H(D) by counting reduced forms of disc -D (weights 1/2, 1/3 -> 6, 4)
    if D == 0: return -1
    if D % 4 in (1, 2): return 0
    s = 0
    for b in range(D % 2, isqrt(D // 3) + 1, 2):
        m = (b*b + D) // 4
        for a in range(max(b, 1), isqrt(m) + 1):
            if m % a: continue
            cc = m // a
            if a == b or a == cc or b == 0: w = 1 if not (a == b == cc) else 0
            else: w = 2
            if a == b == cc: s += 4; continue
            if b == 0 and a == cc: s += 6; continue
            s += 12 * w
    return s
Htab = np.fromfile('data/exf/H12_1p4e6.bin', dtype='<i4')
rng = np.random.default_rng(131)
badH = sum(H12(int(D)) != Htab[D] for D in list(range(0, 3001)) + list(rng.integers(3001, 1400000, 300)))
print('12H table mismatches (D<=3000 + 300 random up to 1.4e6):', badH)
T = [defaultdict(list) for _ in range(4)]
for line in open(sys.argv[1]):
    f, n, a, b, c, d = map(int, line.split()); T[f][n].append((a, b, c, d))
sq = {k*k for k in range(1, 200)}
def esvals(L):
    v = {'': len(L), '.diag': sum(a == b for a, b, c, d in L), '.a1': sum(a == 1 for a, b, c, d in L),
         '.prim': sum(gcd(gcd(a, b), c) == 1 for a, b, c, d in L),
         '.sgn_ab': sum((-1)**(a+b) for a, b, c, d in L), '.sgn_c': sum((-1)**c for a, b, c, d in L),
         '.sgn_d': sum((-1)**d for a, b, c, d in L), '.d_odd_sq': sum(d in sq for a, b, c, d in L)}
    for k in (1, 2, 3): v[f'.d{k}'] = sum(d == k for *_, d in L); v[f'.c{k}'] = sum(c == k for a, b, c, d in L)
    return v
bad = 0
for f, nm in enumerate(['T1p', 'T1m', 'T2p', 'T2m']):
    for n in range(1, 3001):
        for suf, val in esvals(T[f][n]).items():
            if Z['ES:' + nm + suf][n] != val: bad += 1
for n in range(1, 3001):
    for nm, val in (('H(1n)', H12(n)), ('H(4n)', H12(4*n)), ('tau(4n+1)', divisor_count(4*n+1)), ('tau(n^2+4)', divisor_count(n*n+4)),
                    ('SH(4n-x2)', sum(H12(4*n - x*x) for x in range(-isqrt(4*n), isqrt(4*n)+1))) if n <= 600 else ('tau', divisor_count(n))):
        if Z['C:' + nm][n] != val: bad += 1
print('ES (56 cols, n<=3000) + sample classical column mismatches:', bad)
# ---- (b) exact rank
def rank_exact(M):
    A = [list(map(int, r)) for r in M]; rows, cols = len(A), len(A[0]); r = 0; prev = 1
    for j in range(cols):
        piv = next((i for i in range(r, rows) if A[i][j]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r + 1, rows):
            A[i] = [(A[r][j]*A[i][k] - A[i][j]*A[r][k]) // prev for k in range(cols)]
        prev = A[r][j]; r += 1
        if r == rows: break
    return r
def kernel(M):  # rational nullspace basis of M (list of rows)
    A = [[Fraction(int(x)) for x in r] for r in M]; cols = len(A[0]); pivs = []; r = 0
    for j in range(cols):
        piv = next((i for i in range(r, len(A)) if A[i][j]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]; pv = A[r][j]; A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][j]: fac = A[i][j]; A[i] = [x - fac*y for x, y in zip(A[i], A[r])]
        pivs.append(j); r += 1
    out = []
    for j in (j for j in range(cols) if j not in pivs):
        v = [Fraction(0)]*cols; v[j] = Fraction(1)
        for i, pj in enumerate(pivs): v[pj] = -A[i][j]
        L = 1
        for x in v: L = L * x.denominator // gcd(L, x.denominator)
        out.append([int(x * L) for x in v])
    return out
allr = np.arange(2, N + 1); primes = np.array([p for p in range(5, N + 1) if isprime(p)])
sets = {'all n>=2': allr, 'odd n': allr[allr % 2 == 1], 'primes>=5': primes, 'p=1(4)': primes[primes % 4 == 1],
        'p=3(4)': primes[primes % 4 == 3], 'p=1(24)': primes[primes % 24 == 1]}
for name, R in sets.items():
    sub = np.sort(rng.choice(R, min(500, len(R)), replace=False))
    MC = np.stack([Z[k][sub] for k in C], 1); ME = np.stack([Z[k][sub] for k in E], 1)
    rC, rE, rCE = rank_exact(MC), rank_exact(ME), rank_exact(np.concatenate([MC, ME], 1))
    K = kernel(ME); MEfull = np.stack([Z[k][R] for k in E], 1).astype(object)
    inj = all(not any(MEfull.dot(np.array(v, dtype=object))) for v in K)
    print(f'[{name}] rows={len(sub)} exact rkC={rC} rkE={rE} rk(C∪E)={rCE} dim∩={rC + rE - rCE}  '
          f'kerE(sub) dim={len(K)} kills all {len(R)} rows: {inj}', flush=True)
