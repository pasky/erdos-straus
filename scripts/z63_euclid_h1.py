#!/usr/bin/env python3
"""z63 EUCLID — kill test KE1: Euclidean loops of n in H_1(Gamma_0(n)/±1; F_2).

For odd n: Schreier graph of Gamma_0(n) in PSL2(Z)=<S,T> on P^1(Z/n) (right action on rows (c:d)),
H := H_1(Gamma_0(n)/±1; F_2) via Reidemeister–Schreier (non-tree edges mod relators S^2, (ST)^3 at every coset).
Classes [gamma_A], gamma_A = S * S(b_1)...S(b_r), S(b) = T^b S, n/A = [[b_1..b_r]] (HJ).
Short set: A in L_3(n). Known set: L_1 ∪ L_2, all B <= BMAX coprime to n, cusp (T-cycle) classes, elliptic classes.
Reports rank data and every relation (mod H's relations) that involves a short loop.
Usage: python3 z63_euclid_h1.py n1 n2 ...   (or 'pop X' for primes p ≡ 1 (24) <= X, plus controls)
"""
import sys
from math import gcd

import os
BMAX = int(os.environ.get('BMAX', '30'))
HIGH = int(os.environ.get('HIGH', str(2 * BMAX)))  # short words of height > HIGH are 'high' (generic)


def hj(n, A):
    """HJ word of n/A, A in (0,n), gcd=1: b_i = ceil(x/y), remainder b*y - x."""
    w = []
    x, y = n, A
    while y > 0:
        b = -(-x // y)
        w.append(b)
        x, y = y, b * y - x
    return w


def jacobi(a, n):
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def matmul(X, Y):
    return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
            (X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))


class Level:
    def __init__(self, n):
        self.n = n
        self.key2id = {}
        self.reps = []
        self.base = self.add(self.key(0, 1), (0, 1))
        # BFS over cosets with generators S, T
        self.act = []  # act[x] = [xS, xT]
        q = [self.base]
        self.tree = set()  # (x, g) tree edges (g=0:S, 1:T)
        self.parent = {self.base: None}
        i = 0
        while i < len(q):
            x = q[i]; i += 1
            c, d = self.reps[x]
            nbrs = []
            for g, (c2, d2) in enumerate(((d, -c), (c, c + d))):
                k = self.key(c2, d2)
                if k not in self.key2id:
                    y = self.add(k, (c2 % n, d2 % n))
                    self.tree.add((x, g))
                    self.parent[y] = (x, g)
                    q.append(y)
                nbrs.append(self.key2id[k])
            self.act.append(nbrs)
        self.N = len(self.reps)
        # coset representatives as matrices mod n (product of generators along the BFS tree)
        n = self.n
        G = [((0, n - 1), (1, 0)), ((1, 1), (0, 1))]
        R = [None] * self.N
        R[self.base] = ((1, 0), (0, 1))
        for y in q:
            if self.parent.get(y) is not None:
                x, g = self.parent[y]
                M = matmul(R[x], G[g])
                R[y] = tuple(tuple(e % n for e in row) for row in M)
        self.R = R
        self.G = G
        # non-tree edges index
        self.eidx = {}
        for x in range(self.N):
            for g in (0, 1):
                if (x, g) not in self.tree:
                    self.eidx[(x, g)] = len(self.eidx)
        self.E = len(self.eidx)
        # chi on Schreier generators y = R_x g R_{xg}^{-1}; R^{-1} of [[a,b],[c,d]] = [[d,-b],[-c,a]]
        self.chimask = 0
        for (x, g), e in self.eidx.items():
            y = self.act[x][g]
            M = matmul(self.R[x], self.G[g])
            (a, b), (c, d) = self.R[y]
            Y = matmul(M, ((d, -b), (-c, a)))
            assert Y[1][0] % n == 0, "Schreier generator not in Gamma_0(n)"
            if n % 4 == 1 and jacobi(Y[1][1] % n, n) == -1:
                self.chimask |= 1 << e
        # relations
        self.basis = {}  # pivot bit -> vector (python int), pure relations (no tags)
        for x in range(self.N):
            self.reduce_add(self.walk(x, [0, 0])[0])
            self.reduce_add(self.walk(x, [0, 1] * 3)[0])
        self.relrank = len(self.basis)
        self.dimH = self.E - self.relrank
        # assertions (review fix m3): index of Gamma_0(n) and dim H_1(Gamma_0(n)/±1; F_2) = e2 + 2g + c - 1
        fac = {}
        m = n; q = 2
        while q * q <= m:
            while m % q == 0:
                fac[q] = fac.get(q, 0) + 1; m //= q
            q += 1
        if m > 1:
            fac[m] = fac.get(m, 0) + 1
        mu = n
        for q in fac:
            mu = mu * (q + 1) // q
        assert self.N == mu, ("coset count", n, self.N, mu)
        e2 = 1
        e3 = 1
        for q, k in fac.items():
            e2 *= (1 + jacobi(-1, q)) if q != 2 else (0 if k >= 2 else 1)
            e3 *= (1 + jacobi(-3, q)) if q != 3 else (0 if k >= 2 else 1)
        def phi(x):
            r = x; y = x; f = 2
            while f * f <= y:
                if y % f == 0:
                    while y % f == 0:
                        y //= f
                    r -= r // f
                f += 1
            if y > 1:
                r -= r // y
            return r
        c = sum(phi(gcd(d, n // d)) for d in range(1, n + 1) if n % d == 0)
        g12 = 12 + mu - 3 * e2 - 4 * e3 - 6 * c   # 12 g
        assert g12 % 12 == 0, ("genus", n)
        assert self.dimH == e2 + g12 // 6 + c - 1, ("dimH", n, self.dimH, e2, g12 // 12, c)

    def key(self, c, d):
        n = self.n
        c %= n; d %= n
        g = gcd(c, n)
        Np = n // g
        if Np == 1:
            return (n, 0)
        c1 = (c // g) % Np
        u = pow(c1, -1, Np)
        return (g, (u * d) % Np)

    def add(self, k, rep):
        self.key2id[k] = len(self.reps)
        self.reps.append(rep)
        return self.key2id[k]

    def walk(self, x, letters):
        v = 0
        for g in letters:
            e = self.eidx.get((x, g))
            if e is not None:
                v ^= 1 << e
            x = self.act[x][g]
        return v, x

    def reduce(self, v):
        while v:
            h = v.bit_length() - 1
            if h >= self.E:  # tag bits are above E; stop at real part
                break
            b = self.basis.get(h)
            if b is None:
                break
            v ^= b
        return v

    def reduce_full(self, v, basis):
        # reduce v by basis on bits < E (relations+added vectors), highest pivot first
        mask = (1 << self.E) - 1
        while v & mask:
            h = (v & mask).bit_length() - 1
            b = basis.get(h)
            if b is None:
                return v, h
            v ^= b
        return v, None

    def reduce_add(self, v):
        v, h = self.reduce_full(v, self.basis)
        if h is not None:
            self.basis[h] = v

    def word_letters(self, w):
        L = [0]
        for b in w:
            L += [1] * b + [0]
        return L

    def loop_class(self, w):
        v, xend = self.walk(self.base, self.word_letters(w))
        assert xend == self.base, "word not in Gamma_0(n)"
        return v


def check_E1(n, A, w):
    S = ((0, -1), (1, 0))
    M = ((1, 0), (0, 1))
    for b in w:
        M = matmul(M, ((b, -1), (1, 0)))
    G = matmul(S, M)
    assert G[1][0] % n == 0
    assert (G[1][1] * A) % n == (n - 1) % n, (n, A, G)
    if n % 4 == 1:
        assert jacobi(G[1][1], n) == jacobi(A, n)


def analyse(n, verbose=False):
    lev = Level(n)
    # short loops
    short, known = [], []
    for A in range(1, n):
        if gcd(A, n) != 1:
            continue
        w = hj(n, A)
        r = len(w)
        if r == 3:
            check_E1(n, A, w)
            short.append(('S', A, tuple(w), jacobi(A, n)))
        if r <= 2 or A <= BMAX:  # known part: independent of the short set (review fix F1)
            known.append(('K', A, tuple(w), jacobi(A, n)))
    # cusp classes: T-cycles
    seen = set()
    for x in range(lev.N):
        if x in seen:
            continue
        cyc = []
        y = x
        while True:
            seen.add(y); cyc.append(y)
            y = lev.act[y][1]
            if y == x:
                break
        v = 0
        for y in cyc:
            e = lev.eidx.get((y, 1))
            if e is not None:
                v ^= 1 << e
        known.append(('cusp', len(cyc), None, None, v))
    # elliptic: S-fixed and ST-fixed cosets
    for x in range(lev.N):
        if lev.act[x][0] == x:
            known.append(('ell2', x, None, None, lev.walk(x, [0])[0]))
        y = lev.act[lev.act[x][0]][1]
        if y == x:
            known.append(('ell3', x, None, None, lev.walk(x, [0, 1])[0]))
    # verification of Lemma E1 at the level of H_1: chi(loop) via cocycle == (A/n)
    if n % 4 == 1:
        for it in short + [k for k in known if len(k) == 4]:
            v = lev.loop_class(list(it[2]))
            assert (bin(v & lev.chimask).count('1') & 1) == (1 if it[3] == -1 else 0), ("chi mismatch", n, it)
        for b in lev.basis.values():
            assert bin(b & lev.chimask).count('1') % 2 == 0, "chi not a cocycle"
    items = []
    for it in known:
        v = it[4] if len(it) == 5 else lev.loop_class(list(it[2]))
        items.append((it, v))
    def height_le(A, H):
        # A ≡ ±a·b^{-1} (mod n) with 1 <= a, b <= H, b a unit mod n ?  (review fix M1)
        for b in range(1, H + 1):
            if gcd(b, n) != 1:
                continue
            a = (A * b) % n
            if a <= H or n - a <= H:
                return True
        return False
    low = [it for it in short if height_le(it[1], HIGH)]
    high = [it for it in short if not height_le(it[1], HIGH)]
    for it in low + high:
        items.append((it, lev.loop_class(list(it[2]))))
    nlow = len(low)
    # elimination: known first, then short; track tags
    E = lev.E
    basis = dict(lev.basis)
    rels = []
    rank_known = rank_short = 0
    nk = len(known)
    for i, (it, v) in enumerate(items):
        vt = v | (1 << (E + i))
        vt, h = lev.reduce_full(vt, basis)
        if h is not None:
            basis[h] = vt
            if i < nk:
                rank_known += 1
            else:
                rank_short += 1
        else:
            tags = vt >> E
            idx = [j for j in range(len(items)) if tags >> j & 1]
            rels.append(idx)
    # relations involving short loops
    srels = [r for r in rels if any(j >= nk for j in r)]
    hrels = [r for r in rels if any(j >= nk + nlow for j in r)]
    # 'index relations': short-involving relations whose known side has odd chi (=> odd # of chi=-1 short loops in it)
    def chi_bit(j):
        return bin(items[j][1] & lev.chimask).count('1') & 1
    idxrels = [r for r in srels if sum(chi_bit(j) for j in r if j < nk) % 2 == 1] if n % 4 == 1 else []
    # rank increment of high words over known+low
    hb = dict(lev.basis)
    for i, (it, v) in enumerate(items[:nk + nlow]):
        vv, h = lev.reduce_full(v, hb)
        if h is not None:
            hb[h] = vv
    r0 = len(hb)
    for it, v in items[nk + nlow:]:
        vv, h = lev.reduce_full(v, hb)
        if h is not None:
            hb[h] = vv
    high_inc = len(hb) - r0
    # chi-consistency check on all relations (chi of cusp/elliptic computed implicitly must vanish => use loops only)
    out = dict(n=n, cosets=lev.N, dimH=lev.dimH, nshort=len(short), nknown=nk,
               rank_known=rank_known, rank_short_over_known=rank_short, nrels=len(rels), nshortrels=len(srels),
               nminus=sum(1 for s in short if s[3] == -1), nlow=nlow, nhigh=len(high), high_rank_inc=high_inc,
               nhighrels=len(hrels), nidxrels=len(idxrels))
    if verbose:
        out['shortrels'] = [[items[j][0][:4] for j in r] for r in srels]
        out['highrels'] = [[items[j][0][:4] for j in r] for r in hrels]
    return out, srels, items, nk


def primes_upto(X):
    s = bytearray([1]) * (X + 1); s[0] = s[1] = 0
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(X + 1) if s[i]]


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == 'pop':
        X = int(args[1])
        ns = [p for p in primes_upto(X) if p % 24 == 1]
    else:
        ns = [int(a) for a in args]
    cols = ['n', 'cosets', 'dimH', 'nshort', 'nminus', 'nknown', 'rank_known', 'rank_short_over_known', 'nrels',
            'nshortrels', 'nlow', 'nhigh', 'high_rank_inc', 'nhighrels', 'nidxrels']
    print("\t".join(cols) + "\thighrels\tshortrels")
    for n in ns:
        out, srels, items, nk = analyse(n, verbose=True)
        print("\t".join(str(out[k]) for k in cols) + "\t" + repr(out['highrels'])[:3000] + "\t"
              + repr(out['shortrels'])[:3000], flush=True)
