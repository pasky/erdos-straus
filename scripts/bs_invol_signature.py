"""O152(a): windmill-signature test over ALL n (composites included).

Question: is some F2-combination of weighted ES counts W_j(n) = sum_{sol} w_j(sol) (mod 2) equal, for all
n <= X coprime to 6, to a divisor-type function D_phi(n) = sum_{n=uv,u<v} phi(u mod M, v mod M) + square term?
Every Zagier-type windmill identity has this shape (memo invol_windmill_signature.md).

Input: file of lines "n x y z" (x<=y<=z) from scripts/bs_invol_enum.cpp.
Usage: PYTHONPATH=scripts uv run python scripts/bs_invol_signature.py /tmp/bsinv/sol8000.txt 8000 24
"""
import sys
from math import gcd, isqrt
from collections import defaultdict
from sympy import isprime

fn, X, M = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
NS = [n for n in range(5, X + 1) if gcd(n, M) == 1 and gcd(n, 6) == 1]
row = {n: i for i, n in enumerate(NS)}
R = len(NS)
units = [r for r in range(M) if gcd(r, M) == 1]


def core_feats(n, x, y, z):
    f = {}
    k = (x % n == 0) + (y % n == 0) + (z % n == 0)
    f['T0'], f['TI'], f['TII'] = k == 0, k == 1, k == 2
    for nm, c in (('x', x), ('y', y), ('z', z)):
        for m in (2, 3, 4, 5, 8):
            for r in range(m - 1):
                f[f'{nm}%{m}={r}'] = c % m == r
        f[f'n|{nm}'] = c % n == 0
        s = isqrt(c)
        f[f'{nm}sq'] = s * s == c
    f['x=y'], f['y=z'] = x == y, y == z
    f['x|y'], f['y|z'], f['x|z'] = y % x == 0, z % y == 0, z % x == 0
    f['gxy1'], f['gyz1'], f['gxz1'] = gcd(x, y) == 1, gcd(y, z) == 1, gcd(x, z) == 1
    f['z=lcm'] = z == x * y // gcd(x, y)
    f['4x-n=1'] = 4 * x - n == 1
    for m in (3, 8):
        for r in range(m):
            f[f'(4x-n)%{m}={r}'] = (4 * x - n) % m == r
    return f


rows_feat = defaultdict(lambda: defaultdict(int))
names = None
with open(fn) as fh:
    for line in fh:
        n, x, y, z = map(int, line.split())
        if n > X or n not in row:
            continue
        cf = core_feats(n, x, y, z)
        if names is None:
            core = list(cf)
            types = ['TI', 'TII', 'T0']
            pairs = [(t, c) for t in types for c in core if c not in types]
            names = ['ONE'] + core + [f'{t}&{c}' for t, c in pairs]
        d = rows_feat[n]
        d['ONE'] += 1
        for c in core:
            if cf[c]:
                d[c] += 1
        for t, c in pairs:
            if cf[t] and cf[c]:
                d[f'{t}&{c}'] += 1

# column bit-vectors over rows
def colvec(func):
    v = 0
    for n in NS:
        if func(n) & 1:
            v |= 1 << row[n]
    return v

Wcols = [(nm, colvec(lambda n, nm=nm: rows_feat[n][nm])) for nm in names]
Wcols = [(nm, v) for nm, v in Wcols if v]

# divisor-type basis
Dv = defaultdict(int)
for n in NS:
    for u in range(1, isqrt(n) + 1):
        if n % u == 0:
            v = n // u
            key = ('D', u % M, v % M) if u < v else ('Q', u % M)
            Dv[key] ^= 1 << row[n]
Dcols = [v for v in Dv.values() if v]


class Echelon:
    def __init__(self):
        self.piv = {}  # lead bit -> (vec, mask)

    def reduce(self, v, mask):
        while v:
            b = v.bit_length() - 1
            if b not in self.piv:
                return v, mask
            pv, pm = self.piv[b]
            v ^= pv
            mask ^= pm
        return 0, mask

    def add(self, v, mask):
        v, mask = self.reduce(v, mask)
        if v:
            self.piv[v.bit_length() - 1] = (v, mask)
            return None
        return mask  # relation


E = Echelon()
for v in Dcols:
    E.add(v, 0)
rankD = len(E.piv)
rels = []
for j, (nm, v) in enumerate(Wcols):
    r = E.add(v, 1 << j)
    if r is not None:
        rels.append(r)

# Separate span(W) rank
E2 = Echelon()
for nm, v in Wcols:
    E2.add(v, 0)
rankW = len(E2.piv)
print(f'X={X} M={M} rows={R} rankD={rankD} #W={len(Wcols)} rankW={rankW} '
      f'dim(span W ∩ span D)={len(rels) - (len(Wcols) - rankW)}')

# For each relation c, compute combined W on hard primes p = 1 (24)
hard = [n for n in NS if n % 24 == 1 and isprime(n)]
primes = [n for n in NS if isprime(n)]
allW = {nm: v for nm, v in Wcols}


def comb(mask):
    v = 0
    for j in range(len(Wcols)):
        if mask >> j & 1:
            v ^= Wcols[j][1]
    return v


nontriv = []
for r in rels:
    v = comb(r)
    if v == 0:
        continue  # identically even combination (trivial)
    oddp = sum(v >> row[p] & 1 for p in hard)
    nontriv.append((oddp, r, v))
print(f'relations with nonzero W: {len(nontriv)}; hard primes: {len(hard)}')
for oddp, r, v in sorted(nontriv, key=lambda t: -t[0])[:15]:
    terms = [Wcols[j][0] for j in range(len(Wcols)) if r >> j & 1]
    oddall = sum(v >> row[p] & 1 for p in primes)
    print(f'  odd on {oddp}/{len(hard)} hard primes, {oddall}/{len(primes)} primes; {len(terms)} terms: {terms[:8]}')

# controls
def zagier(n):
    c = 0
    for x in range(1, isqrt(n) + 1, 1):
        t = n - x * x
        if t > 0 and t % 4 == 0:
            t //= 4
            c += sum(1 for yy in range(1, isqrt(t) + 1) if t % yy == 0) * 2 - (isqrt(t) ** 2 == t)
    return c


for nm, f in (('Zagier |S(n)|', zagier), ('#{x^2+4y^2=n}', lambda n: sum(1 for x in range(1, isqrt(n) + 1) if (n - x * x) > 0 and (n - x * x) % 4 == 0 and isqrt((n - x * x) // 4) ** 2 == (n - x * x) // 4))):
    v = colvec(f)
    rv, _ = E.reduce(v, 0)
    # reduce only by D part: rebuild a D-only echelon
    ED = Echelon()
    for d in Dcols:
        ED.add(d, 0)
    rd, _ = ED.reduce(v, 0)
    print(f'control {nm}: in span D? {rd == 0}')
import random
random.seed(1)
v = random.getrandbits(R)
ED = Echelon()
for d in Dcols:
    ED.add(d, 0)
print('control random vector in span D?', ED.reduce(v, 0)[0] == 0)
