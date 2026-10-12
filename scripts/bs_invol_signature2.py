"""O152(a) v2: windmill-signature test, numpy version with pairwise feature ANDs.

Rows: n <= X, n = 1 (mod 4), gcd(n,6)=1 (composites included).  Columns: F2 parities of weighted ES counts
W_j(n) (core features and pairwise ANDs of a core subset) and divisor-type vectors mod M.
Reports dim(span W ∩ span D) and whether intersection elements are odd on hard primes.
Also a prime-only test: is some F2-combination of core W_j a function of p mod L on primes p=1 (4)?
Usage: PYTHONPATH=scripts uv run python scripts/bs_invol_signature2.py /tmp/bsinv/sol20k_1mod4.txt 20000 24 [forms] [additive]
(optional 4th arg: also allow parities of representation counts by binary forms a x^2+bxy+cy^2, a<=8, c<=40)
"""
import sys
from math import gcd, isqrt
from collections import defaultdict
import numpy as np
from sympy import isprime

fn, X, M = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
A = np.array(open(fn).read().split(), dtype=np.int64).reshape(-1, 4)
A = A[A[:, 0] <= X]
n, x, y, z = A.T
F = {}
k = (x % n == 0).astype(int) + (y % n == 0) + (z % n == 0)
F['TI'], F['TII'], F['T0'] = k == 1, k == 2, k == 0
for nm, c in (('x', x), ('y', y), ('z', z)):
    for m in (2, 3, 4, 5, 8):
        for r in range(m - 1):
            F[f'{nm}%{m}={r}'] = c % m == r
    F[f'n|{nm}'] = c % n == 0
F['x=y'], F['y=z'] = x == y, y == z
F['x|y'], F['y|z'], F['x|z'] = y % x == 0, z % y == 0, z % x == 0
F['gxy1'], F['gyz1'], F['gxz1'] = np.gcd(x, y) == 1, np.gcd(y, z) == 1, np.gcd(x, z) == 1
q = 4 * x - n
for m in (3, 8, 5):
    for r in range(m):
        F[f'q%{m}={r}'] = q % m == r
F['q|n'] = n % q == 0
F['gq1'] = np.gcd(q, n) == 1
# role coordinates: Type II n-free coordinate a; Type I n-divisible coordinate / n
afree = np.where(x % n != 0, x, np.where(y % n != 0, y, z))
for m in (3, 4, 8):
    for r in range(m):
        F[f'afree%{m}={r}'] = (k == 2) & (afree % m == r)
ndiv = np.where(x % n == 0, x, np.where(y % n == 0, y, z)) // n
for m in (3, 4, 8):
    for r in range(m):
        F[f'Idiv%{m}={r}'] = (k == 1) & (ndiv % m == r)
names = list(F)
Fm = np.stack([F[c] for c in names], axis=1).astype(np.int64)
core_sub = names[:3] + [c for c in names if c.startswith(('x%', 'y%', 'z%')) and ('%2' in c or '%4' in c)] + \
    ['x=y', 'y=z', 'x|y', 'y|z', 'gxy1', 'gyz1', 'q%3=0', 'q%8=3', 'q%8=7', 'gq1']
core_sub = list(dict.fromkeys(core_sub))
starts = np.flatnonzero(np.r_[True, n[1:] != n[:-1]])
NS = n[starts]
row = {int(v): i for i, v in enumerate(NS)}
R = len(NS)


def tobits(colcounts):
    b = 0
    for i in np.flatnonzero(colcounts & 1):
        b |= 1 << int(i)
    return b


cols = [('ONE', tobits(np.diff(np.r_[starts, len(n)])))]
red = np.add.reduceat(Fm, starts, axis=0)
for j, c in enumerate(names):
    cols.append((c, tobits(red[:, j])))
idx = [names.index(c) for c in core_sub]
for a in range(len(idx)):
    prod = Fm[:, idx[a]:idx[a] + 1] * Fm[:, idx[a + 1:]]
    if prod.shape[1] == 0:
        continue
    rr = np.add.reduceat(prod, starts, axis=0)
    for b in range(prod.shape[1]):
        cols.append((f'{core_sub[a]}&{core_sub[a + 1 + b]}', tobits(rr[:, b])))
ncore = 1 + len(names)
cols = [(c, v) for c, v in cols if v]

Dv = defaultdict(int)
for m_ in NS.tolist():
    for u in range(1, isqrt(m_) + 1):
        if m_ % u == 0:
            v = m_ // u
            key = ('D', u % M, v % M) if u < v else ('Q', u % M)
            Dv[key] ^= 1 << row[m_]
if len(sys.argv) > 4:  # add binary-form representation parities r_F(n), F = a x^2 + b xy + c y^2, x,y>0
    for a_ in range(1, 9):
        for c_ in range(a_, 41):
            for b_ in range(0, a_ + 1):
                if b_ * b_ - 4 * a_ * c_ >= 0:
                    continue
                cnt = defaultdict(int)
                for xx in range(1, isqrt(X // a_) + 2):
                    for yy in range(1, isqrt(X // c_) + 2):
                        val = a_ * xx * xx + b_ * xx * yy + c_ * yy * yy
                        if val <= X and val in row:
                            cnt[val] ^= 1
                for m_, par in cnt.items():
                    if par:
                        Dv[('F', a_, b_, c_)] ^= 1 << row[m_]
    print('added binary-form columns')
if len(sys.argv) > 5:  # add completely-additive mod-2 columns Omega_r(n), omega_r(n) (prime factors = r mod M)
    from sympy import factorint
    for m_ in NS.tolist():
        for pr_, e_ in factorint(m_).items():
            if e_ & 1:
                Dv[('Om', pr_ % M)] ^= 1 << row[m_]
            Dv[('om', pr_ % M)] ^= 1 << row[m_]
    print('added Omega_r / omega_r columns')
Dcols = [v for v in Dv.values() if v]


class Ech:
    def __init__(s):
        s.piv = {}

    def red(s, v, mk):
        while v:
            b = v.bit_length() - 1
            if b not in s.piv:
                return v, mk
            pv, pm = s.piv[b]
            v ^= pv
            mk ^= pm
        return 0, mk

    def add(s, v, mk):
        v, mk = s.red(v, mk)
        if v:
            s.piv[v.bit_length() - 1] = (v, mk)
            return None
        return mk


def intersect(Wc, Dc):
    E = Ech()
    for v in Dc:
        E.add(v, 0)
    rels = [r for j, (_, v) in enumerate(Wc) if (r := E.add(v, 1 << j)) is not None]
    E2 = Ech()
    for _, v in Wc:
        E2.add(v, 0)
    return len(E.piv) - len(Wc) + len(rels), len(E2.piv), rels


rd, rw, rels = intersect(cols, Dcols)
print(f'ALL-n test: X={X} M={M} rows={R} #cols={len(cols)} rankW={rw} rankD={len(Dcols)} '
      f'dim(W∩D)={len(rels) - (len(cols) - rw)}')
hard = [p for p in NS.tolist() if p % 24 == 1 and isprime(p)]


def comb(mk, C):
    v = 0
    j = 0
    while mk:
        if mk & 1:
            v ^= C[j][1]
        mk >>= 1
        j += 1
    return v


seen = set()
for r in rels:
    v = comb(r, cols)
    if v == 0 or v in seen:
        continue
    seen.add(v)
    odd = sum(v >> row[p] & 1 for p in hard)
    terms = [cols[j][0] for j in range(len(cols)) if r >> j & 1]
    print(f'  nonzero W in span D: odd on {odd}/{len(hard)} hard primes; terms {terms[:6]}')

# prime-only test: rows primes p=1 (4); class indicators mod L
for L in (24, 120, 840):
    P = [p for p in NS.tolist() if isprime(p)]
    prow = {p: i for i, p in enumerate(P)}
    Wc = []
    for c, v in cols[:ncore]:
        b = 0
        for p in P:
            if v >> row[p] & 1:
                b |= 1 << prow[p]
        if b:
            Wc.append((c, b))
    Cc = defaultdict(int)
    for p in P:
        Cc[p % L] |= 1 << prow[p]
    _, rwp, relp = intersect(Wc, list(Cc.values()))
    nonz = {comb(r, Wc) for r in relp} - {0}
    print(f'PRIME test L={L}: primes={len(P)} classes={len(Cc)} #Wcore={len(Wc)} rankW={rwp} '
          f'nonzero W periodic mod L: {len(nonz)} (dim(W∩C)={len(relp) - (len(Wc) - rwp)})')
    for r in relp:
        v = comb(r, Wc)
        if v:
            terms = [Wc[j][0] for j in range(len(Wc)) if r >> j & 1]
            oddcls = sorted({p % L for p in P if v >> prow[p] & 1})
            print(f'    terms {terms}; odd exactly on p mod {L} in {oddcls[:12]}')
