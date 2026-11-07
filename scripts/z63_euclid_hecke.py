#!/usr/bin/env python3
"""z63 EUCLID — KE2 (secondary, not pre-registered): Hecke-equivariant fake classes.

For odd prime n = p: H = H_1(Gamma_0(p)/±1; F_2) as in z63_euclid_h1.py. Hecke operators T_l (l in LS, l != p) act on
group elements by T_l[g] = sum_i [alpha_i g alpha_{sigma(i)}^{-1}], alpha_i in {[[1,k],[0,l]]} ∪ {[[l,0],[0,1]]}.
E := {psi in H^* : psi(T_l x) = (l+1) psi(x) for all x, l in LS}  (Eisenstein-type eigenspace containing chi_p, Lemma E2).
Reports dim E, checks chi_p in E, and whether a Hecke-equivariant fake exists:
  psi in E with psi = chi on the known part K and psi = 0 on all length-3 loops (or on all *high* length-3 loops).
Usage: python3 z63_euclid_hecke.py p1 p2 ...   (env BMAX, HIGH as in z63_euclid_h1.py; LS = comma list, default 2,3,5,7)
"""
import os
import sys
from math import gcd

sys.path.insert(0, os.path.dirname(__file__))
import z63_euclid_h1 as H1  # noqa: E402

LS = [int(x) for x in os.environ.get('LS', '2,3,5,7').split(',')]


def mm(X, Y):
    return H1.matmul(X, Y)


class LevelX(H1.Level):
    def __init__(self, n):
        super().__init__(n)
        # exact coset representatives
        G = [((0, -1), (1, 0)), ((1, 1), (0, 1))]
        Rx = [None] * self.N
        Rx[self.base] = ((1, 0), (0, 1))
        order = sorted(range(self.N), key=lambda y: self.depth(y))
        for y in order:
            if self.parent.get(y) is not None:
                x, g = self.parent[y]
                Rx[y] = mm(Rx[x], G[g])
        self.Rx = Rx
        # T-cycles with prefix xor
        self.cyc_of = [None] * self.N
        self.pos = [0] * self.N
        self.cycles = []
        for x in range(self.N):
            if self.cyc_of[x] is not None:
                continue
            cyc = []
            y = x
            while True:
                self.cyc_of[y] = len(self.cycles); self.pos[y] = len(cyc); cyc.append(y)
                y = self.act[y][1]
                if y == x:
                    break
            pre = [0]
            for z in cyc:
                e = self.eidx.get((z, 1))
                pre.append(pre[-1] ^ ((1 << e) if e is not None else 0))
            self.cycles.append((cyc, pre))

    def depth(self, y, _cache={}):
        d = 0
        while self.parent.get(y) is not None:
            y = self.parent[y][0]; d += 1
        return d

    def tpow(self, x, q):
        """class of T^q walked from coset x, and end coset."""
        cyc, pre = self.cycles[self.cyc_of[x]]
        L = len(cyc)
        i = self.pos[x]
        if q < 0:
            j = (i + q) % L
            v, _ = self.tpow(cyc[j], -q)
            return v, cyc[j]
        full, rem = divmod(q, L)
        v = pre[L] if full % 2 else 0
        j = i + rem
        if j <= L:
            v ^= pre[j] ^ pre[i]
        else:
            v ^= (pre[L] ^ pre[i]) ^ pre[j - L]
        return v, cyc[(i + q) % L]

    def elem_class(self, M):
        """class in H (F_2-vector over non-tree edges) of M in Gamma_0(n)."""
        (a, b), (c, d) = M
        assert a * d - b * c == 1 and c % self.n == 0
        # decompose M = T^{q1} S T^{q2} S ... T^{k} (up to sign)
        letters = []
        while c != 0:
            q = a // c
            # M <- S^{-1} T^{-q} M ; S^{-1} = [[0,1],[-1,0]]
            a, b = a - q * c, b - q * d
            a, b, c, d = c, d, -a, -b
            letters.append(('T', q)); letters.append(('S', 1))
        # now M = ±[[1,k],[0,1]]
        k = b // a  # a = ±1
        letters.append(('T', k))
        x = self.base
        v = 0
        for typ, q in letters:
            if typ == 'S':
                e = self.eidx.get((x, 0))
                if e is not None:
                    v ^= 1 << e
                x = self.act[x][0]
            else:
                w, x = self.tpow(x, q)
                v ^= w
        assert x == self.base
        return v


def hecke_image(lev, M, l):
    n = lev.n
    alphas = [((1, k), (0, l)) for k in range(l)] + [((l, 0), (0, 1))]
    v = 0
    used = set()
    for ai in alphas:
        P = mm(ai, M)
        for j, aj in enumerate(alphas):
            adj = ((aj[1][1], -aj[0][1]), (-aj[1][0], aj[0][0]))
            Q = mm(P, adj)
            if all(e % l == 0 for row in Q for e in row):
                Qd = tuple(tuple(e // l for e in row) for row in Q)
                if Qd[1][0] % n == 0:
                    assert j not in used
                    used.add(j)
                    v ^= lev.elem_class(Qd)
                    break
        else:
            raise AssertionError("no sigma(i)")
    return v


def solve_space(rows, E):
    """basis of {psi in F_2^E : psi . r = 0 for r in rows} (rows: python ints over E bits)."""
    piv = {}
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h in piv:
                r ^= piv[h]
            else:
                piv[h] = r
                break
    # reduced echelon
    keys = sorted(piv)
    for h in keys:
        for h2 in keys:
            if h2 != h and piv[h2] >> h & 1:
                piv[h2] ^= piv[h]
    free = [i for i in range(E) if i not in piv]
    basis = []
    for f in free:
        psi = 1 << f
        for h, r in piv.items():
            if r >> f & 1:
                psi |= 1 << h
        basis.append(psi)
    return basis


def dot(a, b):
    return bin(a & b).count('1') & 1


def analyse(p):
    lev = LevelX(p)
    E = lev.E
    rows = list(lev.basis.values())
    # Schreier generator elements
    gens = []
    for (x, g), e in lev.eidx.items():
        y = lev.act[x][g]
        Gm = ((0, -1), (1, 0)) if g == 0 else ((1, 1), (0, 1))
        (a, b), (c, d) = lev.Rx[y]
        Y = mm(mm(lev.Rx[x], Gm), ((d, -b), (-c, a)))
        gens.append((e, Y))
    # sanity: elem_class of every generator = its basis vector modulo relations (review fix m3)
    for e, Y in gens:
        v = lev.elem_class(Y) ^ (1 << e)
        w, h = lev.reduce_full(v, lev.basis)
        assert h is None, "elem_class mismatch"
    for l in LS:
        if l == p:
            continue
        lam = (l + 1) % 2
        for e, Y in gens:
            img = hecke_image(lev, Y, l)
            rows.append(img ^ ((1 << e) if lam else 0))
    Ebasis = solve_space(rows, E)
    chi = lev.chimask
    # chi in E?
    chi_in = all(dot(chi, r) == 0 for r in rows)
    # known/short sets
    out, srels, items, nk = H1.analyse(p)
    known = [v for (it, v) in items[:nk]]
    shortv = [v for (it, v) in items[nk:]]
    nlow = out['nlow']
    highv = shortv[nlow:]

    def fake_exists(zero_set, extra_known=()):
        # psi = sum c_i Ebasis_i ; constraints psi.k = chi.k (k in known), psi.s = 0 (s in zero_set)
        m = len(Ebasis)
        eqs = []
        for k in list(known) + list(extra_known):
            eqs.append((sum((dot(b, k) << i) for i, b in enumerate(Ebasis)), dot(chi, k)))
        for s_ in zero_set:
            eqs.append((sum((dot(b, s_) << i) for i, b in enumerate(Ebasis)), 0))
        piv = {}
        for row, rhs in eqs:
            r = row | (rhs << m)
            while r & ((1 << m) - 1):
                h = (r & ((1 << m) - 1)).bit_length() - 1
                if h in piv:
                    r ^= piv[h]
                else:
                    piv[h] = r
                    break
            else:
                if r >> m & 1:
                    return False
        return True
    # affine dimension of {psi in E : psi = chi on K}  (review fix M4)
    def rank(vs):
        piv = {}
        for c in vs:
            while c:
                hh = c.bit_length() - 1
                if hh in piv:
                    c ^= piv[hh]
                else:
                    piv[hh] = c
                    break
        return len(piv)
    affdim = len(Ebasis) - rank([sum((dot(b, k) << i) for i, b in enumerate(Ebasis)) for k in known])
    return dict(p=p, dimH=lev.dimH, dimE=len(Ebasis), chi_in_E=chi_in, nshort=len(shortv), nhigh=len(highv), affdim=affdim,
                nminus=out['nminus'], fake_all_short=fake_exists(shortv), fake_high_only=fake_exists(highv, shortv[:nlow]))


if __name__ == '__main__' and not os.environ.get('FIT'):
    cols = ['p', 'dimH', 'dimE', 'affdim', 'chi_in_E', 'nshort', 'nminus', 'nhigh', 'fake_all_short', 'fake_high_only']
    print("\t".join(cols))
    for a in sys.argv[1:]:
        r = analyse(int(a))
        print("\t".join(str(r[c]) for c in cols), flush=True)


def feature_fit(p):
    """Are the values of E's basis on ALL Euclidean loops [gamma_A] (A = 1..p-1) F_2-linear combinations of
    word-local features?  Features: 1, r, sum b_i, chi, #even letters, b_1, b_r (all mod 2)."""
    lev = LevelX(p)
    rows = list(lev.basis.values())
    gens = []
    for (x, g), e in lev.eidx.items():
        y = lev.act[x][g]
        Gm = ((0, -1), (1, 0)) if g == 0 else ((1, 1), (0, 1))
        (a, b), (c, d) = lev.Rx[y]
        gens.append((e, mm(mm(lev.Rx[x], Gm), ((d, -b), (-c, a)))))
    for l in LS:
        if l == p:
            continue
        lam = (l + 1) % 2
        for e, Y in gens:
            rows.append(hecke_image(lev, Y, l) ^ ((1 << e) if lam else 0))
    Eb = solve_space(rows, lev.E)
    names = ['1', 'r', 'sumb', 'chi', 'neven', 'b1', 'br', 'ell2']
    sfix = [lev.act[x][0] == x for x in range(lev.N)]

    def ell2(w):
        x = lev.base; cnt = 0
        for g in lev.word_letters(w):
            if g == 0 and sfix[x]:
                cnt += 1
            x = lev.act[x][g]
        return cnt & 1
    F = []   # per loop feature bits
    V = []   # per loop values of E basis
    for A in range(1, p):
        w = H1.hj(p, A)
        v = lev.loop_class(w)
        feats = [1, len(w) & 1, sum(w) & 1, 1 if H1.jacobi(A, p) == -1 else 0, sum(1 for b in w if b % 2 == 0) & 1,
                 w[0] & 1, w[-1] & 1, ell2(w)]
        F.append(feats)
        V.append([dot(b, v) for b in Eb])
    # ranks: dim span(E|loops), dim span(features), dim of sum -> intersection
    def rank(cols):
        piv = {}
        for c in cols:
            while c:
                h = c.bit_length() - 1
                if h in piv:
                    c ^= piv[h]
                else:
                    piv[h] = c
                    break
        return len(piv)
    Vc = [sum(V[i][j] << i for i in range(len(V))) for j in range(len(Eb))]
    Fc = [sum(F[i][k] << i for i in range(len(F))) for k in range(len(names))]
    rV, rF, rVF = rank(Vc), rank(Fc), rank(Vc + Fc)
    print('p', p, 'LS', LS, 'dimE', len(Eb), 'rank E|loops', rV, 'rank features', rF, 'intersection', rV + rF - rVF,
          flush=True)
    # for each basis psi (and the span), solve F c = psi over F_2
    nf = len(names)
    res = []
    for j in range(len(Eb)):
        piv = {}
        ok = True
        for i in range(len(F)):
            r = sum(F[i][k] << k for k in range(nf)) | (V[i][j] << nf)
            while r & ((1 << nf) - 1):
                h = (r & ((1 << nf) - 1)).bit_length() - 1
                if h in piv:
                    r ^= piv[h]
                else:
                    piv[h] = r
                    break
            else:
                if r >> nf & 1:
                    ok = False
                    break
        res.append(ok)
    return len(Eb), res


if __name__ == '__main__' and os.environ.get('FIT'):
    for a in sys.argv[1:]:
        print(a, *feature_fit(int(a)), flush=True)
