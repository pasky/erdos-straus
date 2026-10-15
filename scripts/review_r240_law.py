"""R240 from-scratch check of FF_ODD_ABSENCE Lemma 1.1 / Thm 1.2 / Thm 1.4 / Prop 1.6 / Cor 1.7 on small q.

Own GF(q) arithmetic (q = p or p^r via a chosen irreducible), own polynomial code, own enumerators:
  Case B (k = 1): enumerate monic T-free (m', w, g') and solve C = (w + g'T^s)/(g'm'w - 1) (exact division),
     which finds EVERY tuple m'wC = T^s + v, w + C = g'v with z + a + y <= DMAX (DMAX = s + 1 > s, so the degree
     identity z + a + b = s and y <= b are *tested*, not assumed). Only orientation a <= b is recorded (for a > b,
     z + a + y can exceed DMAX; the law is invariant under w <-> C).
  k >= 2 tuples (B) of FF_STERILE_PUSH: m'w1C1 = T^{s-2} + v1, w1 + C1 = T g' v1, T not dividing m'g'w1C1v1:
     C1 = (w1 + g'T^{s-1})/(T g'm'w1 - 1).
  Case A (k = 1): (a1', b1, K), lc K in {1, 2}, E = a1'b1K - 1, E | T^al a1' + b1.
Checks: unsimplified Lemma 1.1 identity, simplified law E(0)^s = eps, E(0) != -1, Thm 1.4 E(0)^al in F3^* (q = 3^r),
Cor 1.7 parity z = t = s mod 2, Prop 1.6 construction.  Exit code 1 on any failure.
usage: review_r240_law.py [q ...]   (default: all of 5 7 9 27 25 3)
"""
import itertools, sys
from collections import Counter, defaultdict

IRRED = {9: (3, [1, 0, 1]), 27: (3, [1, 2, 0, 1]), 5: (5, [0, 1]), 7: (7, [0, 1]), 3: (3, [0, 1]), 25: (5, [2, 0, 1])}


class GF:
    def __init__(self, q):
        p, f = IRRED[q]
        self.q, self.p = q, p
        r = len(f) - 1
        self.r = r
        # element i <-> base-p digits = coefficients of x^0..x^{r-1}
        def tovec(i): return [(i // p ** k) % p for k in range(r)]
        def toint(v): return sum(c * p ** k for k, c in enumerate(v))
        self.add = [[toint([(x + y) % p for x, y in zip(tovec(i), tovec(j))]) for j in range(q)] for i in range(q)]
        def mulv(u, v):
            prod = [0] * (2 * r)
            for i, x in enumerate(u):
                for j, y in enumerate(v):
                    prod[i + j] = (prod[i + j] + x * y) % p
            for d in range(2 * r - 1, r - 1, -1):  # reduce with monic f
                c = prod[d]
                if c:
                    for k in range(r + 1):
                        prod[d - r + k] = (prod[d - r + k] - c * f[k]) % p
            return prod[:r]
        self.mul = [[toint(mulv(tovec(i), tovec(j))) for j in range(q)] for i in range(q)]
        self.neg = [toint([(-x) % p for x in tovec(i)]) for i in range(q)]
        self.inv = [None] + [next(j for j in range(1, q) if self.mul[i][j] == 1) for i in range(1, q)]
        # field axioms (spot: associativity/distributivity exhaustively for q <= 27)
        for i in range(q):
            for j in range(q):
                assert self.add[i][j] == self.add[j][i] and self.mul[i][j] == self.mul[j][i]
                for k in range(q):
                    assert self.mul[i][self.add[j][k]] == self.add[self.mul[i][j]][self.mul[i][k]]
                    assert self.mul[self.mul[i][j]][k] == self.mul[i][self.mul[j][k]]
        self.F3 = {1, self.neg[1]}  # F_p^* subgroup {1,-1}; equals F_3^* when p = 3

    def pw(self, x, e):
        if e < 0:
            x, e = self.inv[x], -e
        r = 1
        for _ in range(e):
            r = self.mul[r][x]
        return r

    # polynomials: lists low -> high, no trailing zeros; [] = 0
    def trim(self, a):
        while a and a[-1] == 0:
            a.pop()
        return a

    def padd(self, a, b):
        n = max(len(a), len(b))
        A = self.add
        return self.trim([A[a[i] if i < len(a) else 0][b[i] if i < len(b) else 0] for i in range(n)])

    def psub(self, a, b):
        return self.padd(a, [self.neg[c] for c in b])

    def pmul(self, a, b):
        if not a or not b:
            return []
        out = [0] * (len(a) + len(b) - 1)
        M, A = self.mul, self.add
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    out[i + j] = A[out[i + j]][M[x][y]]
        return self.trim(out)

    def pdivmod(self, a, b):
        a = list(a)
        db = len(b) - 1
        ib = self.inv[b[-1]]
        if len(a) - 1 < db:
            return [], a
        qt = [0] * (len(a) - db)
        M, A, N = self.mul, self.add, self.neg
        for d in range(len(a) - 1, db - 1, -1):
            c = a[d]
            if c:
                f = M[c][ib]
                qt[d - db] = f
                for k in range(db + 1):
                    a[d - db + k] = A[a[d - db + k]][N[M[f][b[k]]]]
        return self.trim(qt), self.trim(a)

    def monic_tfree(self, d):
        """all monic polys of degree d with nonzero constant term"""
        if d == 0:
            yield [1]
            return
        for c0 in range(1, self.q):
            for mid in itertools.product(range(self.q), repeat=d - 1):
                yield [c0, *mid, 1]

    def Tpow(self, s):
        return [0] * s + [1]


def lemma11_rhs(F, s, t, z, a, lam, muM, muW):
    sign = 1 if (t + t * z + z * (1 + s) + t * s) % 2 == 0 else F.neg[1]
    r = sign
    r = F.mul[r][F.pw(lam, z + 2 * a - s)]
    r = F.mul[r][F.pw(muM, s - t)]
    r = F.mul[r][F.pw(muW, 2 * (s - t))]
    return r


def eps(F, s, z, t):
    return 1 if (t + t * z + z * (1 + s) + t * s) % 2 == 0 else F.neg[1]


FAIL = []


def caseB(F, smax):
    dist = defaultdict(Counter)
    ntup = 0
    for s in range(1, smax + 1):
        Ts = F.Tpow(s)
        DMAX = s + 1
        for z in range(DMAX + 1):
            for a in range(DMAX + 1 - z):
                for y in range(DMAX + 1 - z - a):
                    for m in F.monic_tfree(z):
                        for w in F.monic_tfree(a):
                            mw = F.pmul(m, w)
                            for g in F.monic_tfree(y):
                                den = F.psub(F.pmul(g, mw), [1])
                                if not den:
                                    continue
                                C, rem = F.pdivmod(F.padd(w, F.pmul(g, Ts)), den)
                                if rem or not C or C[-1] != 1 or C[0] == 0:
                                    continue
                                v = F.psub(F.pmul(mw, C), Ts)
                                if not v or v[0] == 0:
                                    continue
                                assert F.padd(w, C) == F.pmul(g, v)
                                b, t = len(C) - 1, len(v) - 1
                                if a > b:
                                    continue  # orientation a <= b only: for a > b, z + a + y may exceed DMAX (w <-> C symmetry)
                                ntup += 1
                                if z + a + b != s or y + t != max(a, b):
                                    FAIL.append(("deg", F.q, s, m, w, C, g))
                                if z + a + y > s:
                                    FAIL.append(("zay>s", F.q, s))
                                E0 = F.mul[w[0]][F.inv[C[0]]]
                                lhs = F.pw(E0, s)
                                if lhs != lemma11_rhs(F, s, t, z, a, v[-1], 1, 1):
                                    FAIL.append(("L1.1", F.q, s, m, w, C, g))
                                if lhs != eps(F, s, z, t):
                                    FAIL.append(("T1.2", F.q, s, m, w, C, g))
                                if E0 == F.neg[1]:
                                    FAIL.append(("E0=-1", F.q, s))
                                lam_expected = 1 if a != b else F.add[1][1]
                                if v[-1] != lam_expected:
                                    FAIL.append(("lam", F.q, s))
                                dist[s][E0] += 1
    return ntup, dist


def caseB_k2(F, smax):
    ntup = 0
    npat = Counter()
    for s in range(3, smax + 1):
        T1 = F.Tpow(s - 1)
        Ts2 = F.Tpow(s - 2)
        DMAX = s
        for z in range(DMAX + 1):
            for a1 in range(DMAX + 1 - z):
                for y in range(DMAX + 1 - z - a1):
                    for m in F.monic_tfree(z):
                        for w1 in F.monic_tfree(a1):
                            mw = F.pmul(m, w1)
                            for g in F.monic_tfree(y):
                                den = F.psub(F.pmul([0, 1], F.pmul(g, mw)), [1])
                                C1, rem = F.pdivmod(F.padd(w1, F.pmul(g, T1)), den)
                                if rem or not C1 or C1[-1] != 1 or C1[0] == 0:
                                    continue
                                v1 = F.psub(F.pmul(mw, C1), Ts2)
                                if not v1 or v1[0] == 0:
                                    continue
                                a, b, t = a1 + 1, len(C1), len(v1) + 1
                                ntup += 1
                                if z + a + b != s or y + t != max(a, b):
                                    FAIL.append(("k2deg", F.q, s))
                                # Lemma 1.1 with W/C = w1/C1, s' = s-2, t' = t-2, a' = a-1, lam = lc v1
                                lhs = F.pw(F.mul[w1[0]][F.inv[C1[0]]], s - 2)
                                if lhs != lemma11_rhs(F, s - 2, t - 2, z, a - 1, v1[-1], 1, 1):
                                    FAIL.append(("k2L1.1", F.q, s))
                                if not (z % 2 == t % 2 == s % 2):
                                    FAIL.append(("k2parity", F.q, s, z, t))
                                npat[(s, a, z, y, t)] += 1
    return ntup, npat


def caseA(F, almax, degmax):
    """Thm 1.4: for all (a1', b1, K) with a1', b1 monic, lc K in {1,2}, T not dividing a1'b1K, E = a1'b1K - 1,
    E | T^al a1' + b1, E(0) != 0: E(0)^al equals the Lemma 1.1 RHS and lies in {1,-1}."""
    n = 0
    hist = Counter()
    lcs = [1, F.add[1][1]]
    for al in range(1, almax + 1):
        Ta = F.Tpow(al)
        for d1 in range(degmax + 1):
            for be in range(degmax + 1 - d1):
                for ka in range(degmax + 1 - d1 - be):
                    for a1p in F.monic_tfree(d1):
                        for b1 in F.monic_tfree(be):
                            ab = F.pmul(a1p, b1)
                            for Km in F.monic_tfree(ka):
                                for lk in lcs:
                                    K = [F.mul[lk][c] for c in Km]
                                    E = F.psub(F.pmul(ab, K), [1])
                                    if not E or E[0] == 0:
                                        continue
                                    Fq, rem = F.pdivmod(F.padd(F.pmul(Ta, a1p), b1), E)
                                    if rem or not Fq:
                                        continue
                                    zz, rem2 = F.pdivmod(F.padd(Fq, b1), a1p)
                                    if rem2:
                                        FAIL.append(("A:z", F.q, al))
                                        continue
                                    if not zz or zz[0] == 0:
                                        FAIL.append(("A:z0", F.q, al))
                                        continue
                                    if F.pmul(F.pmul(b1, K), Fq) != F.padd(Ta, zz):
                                        FAIL.append(("A:id", F.q, al))
                                    E0 = E[0]
                                    if E0 != F.mul[b1[0]][F.inv[Fq[0]]]:
                                        FAIL.append(("A:E0", F.q, al))
                                    t = len(zz) - 1
                                    lhs = F.pw(E0, al)
                                    if lhs != lemma11_rhs(F, al, t, ka, be, zz[-1], lk, 1):
                                        FAIL.append(("A:L1.1", F.q, al))
                                    if F.p == 3 and lhs not in F.F3:
                                        FAIL.append(("A:F3", F.q, al, a1p, b1, K))
                                    n += 1
                                    hist[(al, E0 not in F.F3)] += 1
    return n, hist


def prop16(F, smax):
    """Prop 1.6 for D = T - rho, rho^s = -1, and for all monic D | T^s+1 of degree 1..s-1 found by trial division."""
    n = 0
    for s in range(2, smax + 1):
        P = F.padd(F.Tpow(s), [1])
        for d in range(1, s):
            for D in F.monic_tfree(d):
                C, rem = F.pdivmod(P, D)
                if rem or D[0] == F.neg[1]:
                    continue
                m = F.padd(D, [1])
                w, g = [1], [1]
                v = F.padd(C, [1])
                ok = (F.pmul(F.pmul(m, w), C) == F.padd(F.Tpow(s), v) and F.padd(w, C) == F.pmul(g, v)
                      and m[-1] == 1 and m[0] != 0 and C[-1] == 1 and C[0] != 0 and v and v[0] != 0)
                E0 = F.mul[w[0]][F.inv[C[0]]]
                if not ok or E0 != D[0]:
                    FAIL.append(("P1.6", F.q, s, D))
                n += 1
    return n


if __name__ == "__main__":
    plan = {5: (6, 7, 4, 3), 7: (5, 6, 4, 3), 9: (5, 5, 4, 3), 27: (3, 3, 2, 2), 25: (3, 4, 2, 2), 3: (9, 9, 6, 5)}
    sel = [int(x) for x in sys.argv[1:]] or list(plan)
    for q in sel:
        sB, sk2, alA, degA = plan[q]
        F = GF(q)
        nB, dist = caseB(F, sB)
        nk, npat = caseB_k2(F, sk2)
        nA, hA = caseA(F, alA, degA)
        nP = prop16(F, 8 if q < 27 else 5)
        print(f"q={q}: caseB s<={sB}: {nB} tuples; k>=2 s<={sk2}: {nk} tuples in {len(npat)} patterns; "
              f"caseA al<={alA},deg<={degA}: {nA} data (off-F3: {sum(v for k, v in hA.items() if k[1])}); prop1.6: {nP}")
        for s in sorted(dist):
            print(f"   s={s}: E(0) distribution {dict(sorted(dist[s].items()))}")
        print(f"   cumulative failures after q={q}: {len(FAIL)}")
        sys.stdout.flush()
    print("FAILURES:", len(FAIL), FAIL[:10])
    sys.exit(1 if FAIL else 0)
