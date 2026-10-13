"""bsE_caseA.py (O178): Case A families valid somewhere on a c-slice (A = T^2), by two independent enumerations.
Route A4 (DEPTH_ASPECT Lemma 2.3 (A4)): enumerate (a1', K, F), put b1 = (T^a a1' + F)/(a1' K F - 1).
Route A1 (independent): enumerate (a1', b1), list all monic divisors E of T^a a1' + b1 (sympy factorisation),
keep E == -1 mod a1' b1, T || E + 1.  Both report, per depth alpha, the set of tuples (a1', b1, E); they must agree.
Checks Lemma 2.3 identities on every tuple, compares counts with q^floor((alpha-1)/2), prints the covered relative
mass sum q^{-alpha} (union bound, k = 2; E is monic here because deg a1 > deg b1 forces lc(s) = 1).
usage: uv run python scripts/bsE_caseA.py p AMAX"""
import sys, itertools
from sympy import Poly, symbols
X = symbols('X')

def norm(a, P):
    a = [x % P for x in a]
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b, P):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return norm(r, P)
def add(a, b, P):
    n = max(len(a), len(b)); return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], P)
def divmod_(a, b, P):
    a = norm(a, P); b = norm(b, P); q = [0] * max(0, len(a) - len(b) + 1); inv = pow(b[-1], P - 2, P)
    while len(a) >= len(b):
        f = a[-1] * inv % P; s = len(a) - len(b); q[s] = f
        a = norm([a[i] - (f * b[i - s] if 0 <= i - s < len(b) else 0) for i in range(len(a))], P)
    return norm(q, P), a
def T(n): return [0] * n + [1]
def polys(deg, P, monic=True, t_free=False):
    for coeffs in itertools.product(range(P), repeat=deg):
        lcs = [1] if monic else range(1, P)
        for lc in lcs:
            p = list(coeffs) + [lc]
            if t_free and p[0] == 0: continue
            yield p

def route_A4(P, al):
    out = set()
    for lam in range(0, al):
        for ka in range(1, al + 1):
            for f in range(0, al - ka + 1):
                be = al - ka - f
                for a1 in polys(lam, P, True, True):
                    for K1 in polys(ka - 1, P, False, True):      # K = T*K1, T || K
                        K = [0] + K1
                        for F in polys(f, P, False):
                            den = add(mul(mul(a1, K, P), F, P), [P - 1], P)
                            b1, r = divmod_(add(mul(T(al), a1, P), F, P), den, P)
                            if r or not b1 or len(b1) - 1 != be or b1[-1] != 1 or b1[0] == 0: continue
                            E = add(mul(mul(a1, b1, P), K, P), [P - 1], P)
                            if E[-1] != 1: continue
                            # gcd(a1', b1) = 1
                            g = a1[:]; h = b1[:]
                            while h: g, h = h, divmod_(g, h, P)[1]
                            if len(g) != 1: continue
                            # identities (A1)-(A3)
                            z, r0 = divmod_(add(F, b1, P), a1, P); assert not r0 and z
                            assert mul(E, F, P) == add(mul(T(al), a1, P), b1, P)
                            assert not divmod_(add(T(al), mul(mul(b1, b1, P), K, P), P), E, P)[1]
                            assert mul(mul(b1, K, P), F, P) == add(T(al), z, P)
                            out.add((tuple(a1), tuple(b1), tuple(E)))
    return out

def divisors_monic(f, P):
    fp = Poly(list(reversed(f)), X, modulus=P)
    _, facs = fp.factor_list()
    fl = [(norm(list(reversed([int(c) % P for c in g.all_coeffs()])), P), e) for g, e in facs]
    divs = [[1]]
    for g, e in fl:
        g = mul(g, [pow(g[-1], P - 2, P)], P)
        new = []
        for d in divs:
            x = d
            for _ in range(e + 1):
                new.append(x); x = mul(x, g, P)
        divs = new
    return divs

def route_A1(P, al):
    out = set()
    for lam in range(0, al):
        for a1 in polys(lam, P, True, True):
            for be in range(0, al):
                for b1 in polys(be, P, True, True):
                    g = a1[:]; h = b1[:]
                    while h: g, h = h, divmod_(g, h, P)[1]
                    if len(g) != 1: continue
                    Nn = add(mul(T(al), a1, P), b1, P)
                    ab = mul(a1, b1, P)
                    for E in divisors_monic(Nn, P):
                        E1 = add(E, [1], P)
                        if divmod_(E1, ab, P)[1]: continue
                        if len(E1) < 2 or E1[0] != 0 or E1[1] == 0: continue   # T || E + 1
                        out.add((tuple(a1), tuple(b1), tuple(E)))
    return out

if __name__ == "__main__":
    P, AMAX = int(sys.argv[1]), int(sys.argv[2]); tot = 0.0
    for al in range(1, AMAX + 1):
        s4 = route_A4(P, al); s1 = route_A1(P, al)
        cyl = {E[:al + 2] for (_, _, E) in s4}
        mass = len(s4) * P ** (-al) / (P - 1)   # mean over the P-1 values of c
        tot += mass
        print("q=%d alpha=%d: A4 tuples %d, A1 tuples %d, agree %s, distinct cylinders %d, bound q^floor((a-1)/2)=%d, mean rel. mass %.5f (cum %.5f)"
              % (P, al, len(s4), len(s1), s4 == s1, len(cyl), P ** ((al - 1) // 2), mass, tot), flush=True)
