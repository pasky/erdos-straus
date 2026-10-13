"""R199: independent recount of |G^-_p| (classes of positive classical ternary lattices of det p, anisotropic at p)
versus #(X_0(2)^ss / <Frob, w_2>), computed via the Hauptmodul of X_0(2):
    j(tau) = (s+256)^3/s^2,  j(2 tau) = (s+16)^3/s,  w_2: s -> 4096/s,  Frob: s -> s^p,
with the supersingular j's obtained from Deuring's Legendre polynomial H_p(lambda) = sum C(m,i)^2 lambda^i, m=(p-1)/2,
by brute force over F_{p^2}.  No Velu, no 2-torsion bookkeeping (independent of the author's ce_ss2.py).
Lattice side: candidates a<=b<=c, 2|f|<=a, 2|e|<=a, 2|d|<=b, abc<=2p (necessary Minkowski conditions), canonical form =
lexicographically least Gram over all bases realising the successive minima.  Also reports path classes.
"""
import sys
import math
from itertools import product
from math import comb

sys.path.insert(0, 'scripts')


def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


# ---------------- lattice side ----------------
def Qf(G, x):
    return sum(G[i][j] * x[i] * x[j] for i in range(3) for j in range(3))


def det3(G):
    (a, b, c), (d, e, f), (g, h, i) = G
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def adjd(G):
    (a, b, c), (d, e, f), (g, h, i) = G
    return [e * i - f * h, a * i - c * g, a * e - b * d]


def short_vectors(G, c):
    D = det3(G)
    ad = adjd(G)
    Bd = [math.isqrt(c * ad[i] // D) + 1 for i in range(3)]
    out = []
    for x in product(*[range(-b, b + 1) for b in Bd]):
        if any(x):
            q = Qf(G, x)
            if q <= c:
                out.append((q, x))
    return out


def rank(vs):
    import fractions
    M = [list(map(fractions.Fraction, v)) for v in vs]
    r = 0
    for col in range(3):
        piv = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                f = M[i][col] / M[r][col]
                M[i] = [M[i][k] - f * M[r][k] for k in range(3)]
        r += 1
    return r


def detv(a, b, c):
    return det3([a, b, c])


def canon(G):
    c = max(G[i][i] for i in range(3))
    sv = short_vectors(G, c)
    sv.sort()
    # successive minima
    mins, chosen = [], []
    for q, x in sv:
        if rank(chosen + [x]) > len(chosen):
            chosen.append(x)
            mins.append(q)
            if len(mins) == 3:
                break
    S = [[x for q, x in sv if q == m] for m in mins]
    # sign normalisation: first nonzero coord positive (Gram off-diagonals change sign; keep all to be safe on v2,v3)
    pos = lambda x: next(t for t in x if t) > 0
    S1 = [x for x in S[0] if pos(x)]
    best = None
    B = lambda x, y: sum(G[i][j] * x[i] * y[j] for i in range(3) for j in range(3))
    for v1 in S1:
        for v2 in S[1]:
            if v2 == v1 or v2 == tuple(-t for t in v1):
                continue
            f12 = B(v1, v2)
            for v3 in S[2]:
                d = detv(v1, v2, v3)
                if d not in (1, -1):
                    continue
                key = (f12, B(v1, v3), B(v2, v3))
                if best is None or key < best:
                    best = key
    return (tuple(mins), best)


def classes(p):
    seen = {}
    for a in range(1, int(round((2 * p) ** (1 / 3))) + 2):
        for b in range(a, int(math.isqrt(2 * p // a)) + 2):
            for f in range(-(a // 2), a // 2 + 1):
                for e in range(-(a // 2), a // 2 + 1):
                    for d in range(-(b // 2), b // 2 + 1):
                        # det linear in c: det = c*(ab-f^2) + const
                        G0 = [[a, f, e], [f, b, d], [e, d, 0]]
                        k = a * b - f * f
                        if k <= 0:
                            continue
                        const = det3(G0)
                        if (p - const) % k:
                            continue
                        c = (p - const) // k
                        if c < b or a * b * c > 2 * p:
                            continue
                        G = [[a, f, e], [f, b, d], [e, d, c]]
                        # positive definiteness: leading minors a>0, k>0, det=p>0
                        key = canon(G)
                        if key not in seen:
                            seen[key] = G
    return seen


def aniso_p(G, p):
    ad = adjd(G)
    for m in ad:
        if m % p:
            return leg(-m, p) == -1
    raise ValueError


# ---------------- X_0(2) side ----------------
class Fp2:
    def __init__(self, p):
        self.p = p
        d = 2
        while leg(d, p) != -1:
            d += 1
        self.d = d

    def mul(self, x, y):
        p, d = self.p, self.d
        return ((x[0] * y[0] + d * x[1] * y[1]) % p, (x[0] * y[1] + x[1] * y[0]) % p)

    def add(self, x, y):
        return ((x[0] + y[0]) % self.p, (x[1] + y[1]) % self.p)

    def pw(self, x, n):
        r = (1, 0)
        while n:
            if n & 1:
                r = self.mul(r, x)
            x = self.mul(x, x)
            n >>= 1
        return r

    def inv(self, x):
        return self.pw(x, self.p * self.p - 2)


def ss_js(p):
    K = Fp2(p)
    m = (p - 1) // 2
    co = [comb(m, i) ** 2 % p for i in range(m + 1)]
    js = set()
    for a in range(p):
        for b in range(p):
            lam = (a, b)
            if lam in ((0, 0), (1, 0)):
                continue
            h = (0, 0)
            for cf in reversed(co):
                h = K.add(K.mul(h, lam), (cf, 0))
            if h == (0, 0):
                l2 = K.mul(lam, lam)
                num = K.add(K.add(l2, ((-a) % p, (-b) % p)), (1, 0))
                num = K.mul(K.mul(num, num), num)
                num = K.mul((256 % p, 0), num)
                lm1 = K.add(lam, (p - 1, 0))
                den = K.mul(l2, K.mul(lm1, lm1))
                js.add(K.mul(num, K.inv(den)))
    return js


def x02_orbits(p):
    K = Fp2(p)
    js = ss_js(p)
    pts = []
    for a in range(p):
        for b in range(p):
            s = (a, b)
            if s == (0, 0):
                continue
            num = K.add(s, (256 % p, 0))
            num = K.mul(K.mul(num, num), num)
            j = K.mul(num, K.inv(K.mul(s, s)))
            if j in js:
                pts.append(s)
    P = set(pts)
    c4096 = (4096 % p, 0)
    seen, orb = set(), 0
    for s in pts:
        if s in seen:
            continue
        orb += 1
        st = [s]
        while st:
            x = st.pop()
            if x in seen:
                continue
            seen.add(x)
            for y in (K.pw(x, p), K.mul(c4096, K.inv(x))):
                assert y in P
                st.append(y)
    return len(js), len(pts), orb


if __name__ == '__main__':
    for p in [int(x) for x in sys.argv[1:]]:
        cl = classes(p)
        neg = [G for G in cl.values() if aniso_p(G, p)]
        nss, npts, orb = x02_orbits(p)
        print(f'p={p}: classes det p = {len(cl)}, G^- = {len(neg)}, G^+ = {len(cl) - len(neg)}; '
              f'#ss j = {nss}, #X0(2)^ss = {npts}, orbits <Frob,w2> = {orb}', flush=True)
