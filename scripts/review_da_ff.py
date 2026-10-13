"""review_da_ff.py (R178, from scratch): F_q[T] checks of DEPTH_ASPECT §2 (q prime).

Own polynomial arithmetic (coefficient lists, low -> high); sympy's galoistools.gf_factor is used ONLY as a
black-box factoriser of monic polynomials over F_p.

 caseB q s_max      : enumerate the Case B tuple set F(s) (DEPTH_ASPECT (B)) by a route different from the author's
                      (author: enumerate (w, C), v := -T^s mod wC; here: enumerate v, factor T^s + v, split into
                      ordered triples (m', w, C)); verify (R3), (R4) on every tuple; print counts per s and the
                      per-pattern Lemma 2.2 exponent vs the counted number.
 caseA q a_max      : enumerate Case A tuples (a1', b1, g', E), gamma = 0, from the definition (E a monic divisor of
                      a1 + b1, E = -1 mod g'a1'b1, T || E + 1), verify (A0)-(A4), print counts per alpha.
"""
import sys, itertools
from sympy.polys.galoistools import gf_factor
from sympy.polys.domains import ZZ

Q = 3


def norm(a):
    a = list(a)
    while a and a[-1] % Q == 0:
        a.pop()
    return tuple(x % Q for x in a)


def add(a, b):
    n = max(len(a), len(b))
    return norm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return norm([-x for x in a])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return norm(r)


def divmod_(a, b):
    a = list(a); db = len(b) - 1; inv = pow(b[-1], Q - 2, Q)
    qt = [0] * max(len(a) - db, 1)
    for i in range(len(a) - 1 - db, -1, -1):
        c = a[i + db] * inv % Q
        qt[i] = c
        if c:
            for j in range(db + 1):
                a[i + j] = (a[i + j] - c * b[j]) % Q
    return norm(qt), norm(a[:db] if db > 0 else [])


def deg(a):
    return len(a) - 1


def Tpow(n):
    return tuple([0] * n + [1])


def vT(a):
    i = 0
    while i < len(a) and a[i] == 0:
        i += 1
    return i


def factor(a):
    """monic a -> list of (monic irreducible, exponent)."""
    hl = [ZZ(x) for x in reversed(a)]
    lc, fs = gf_factor(hl, Q, ZZ)
    assert int(lc) % Q == 1
    return [(norm([int(x) for x in reversed(f)]), e) for f, e in fs]


def divisors_vec(fac):
    """all exponent vectors."""
    return itertools.product(*[range(e + 1) for _, e in fac])


def from_vec(fac, vec):
    r = (1,)
    for (f, _), k in zip(fac, vec):
        for _ in range(k):
            r = mul(r, f)
    return r


def polys(d, lcs, low_zero=0):
    """all polynomials of degree d with leading coeff in lcs and coefficients of T^0..T^{low_zero-1} zero."""
    if d < low_zero:
        return
    for mid in itertools.product(range(Q), repeat=max(d - low_zero, 0)):
        for lc in lcs:
            yield norm([0] * low_zero + list(mid) + [lc]) if d >= low_zero else None


# ---------------------------------------------------------------- Case B
def caseB(s):
    """F(s): tuples (m', g', w, C) monic, m'wC = T^s + v, w + C = g'v, T||w, T||C, T∤m'g', v != 0."""
    out = []
    Ts = Tpow(s)
    for t in range(2, s):
        # v_T(v) = 2 exactly (T^2 || m'wC); lc(v) = lc(w + C) / lc(g') in {1, 2}
        for v in polys(t, sorted({1, 2 % Q}), 2):
            if v[2] == 0:
                continue
            P = add(Ts, v)
            fac = factor(P)
            iT = [i for i, (f, e) in enumerate(fac) if f == (0, 1)]
            assert len(iT) == 1 and fac[iT[0]][1] == 2
            for vw in divisors_vec(fac):
                if vw[iT[0]] != 1:
                    continue
                rest = [e - k for (_, e), k in zip(fac, vw)]
                for vc in itertools.product(*[range(r + 1) for r in rest]):
                    if vc[iT[0]] != 1:
                        continue
                    w = from_vec(fac, vw); C = from_vec(fac, vc)
                    m = from_vec(fac, [r - k for r, k in zip(rest, vc)])
                    g, rem = divmod_(add(w, C), v)
                    if rem or not g or g[-1] != 1 or g[0] == 0:
                        continue
                    out.append((m, g, w, C, v))
    return out


def check_B(tup, s):
    m, g, w, C, v = tup
    Ts = Tpow(s)
    assert mul(mul(m, w), C) == add(Ts, v) and add(w, C) == mul(g, v)
    L = mul(g, m); E = sub(mul(L, w), (1,)); E2 = sub(mul(L, C), (1,))
    assert mul(E, E2) == add((1,), mul(Ts, mul(L, g)))              # EE' = 1 + T^s L'g'
    q3, r3 = divmod_(add(mul(g, Ts), w), E); assert not r3 and q3 == C  # (R3)
    q4, r4 = divmod_(add(Ts, mul(m, mul(w, w))), E); assert not r4      # (R4)
    assert divmod_(add((1,), E), w) == (L, ())
    a, b, z, y, t = deg(w), deg(C), deg(m), deg(g), deg(v)
    if a > b:
        a, b = b, a
    ex = min(t - 2, y + z, a - 1 + y, a - 1 + z)
    assert ex <= 2 * (s - 3) / 5
    return (a, b, z, y, t), ex


# ---------------------------------------------------------------- Case A
def monics(d, Tfree=True):
    for mid in itertools.product(range(Q), repeat=d):
        p = norm(list(mid) + [1])
        if Tfree and d > 0 and p[0] == 0:
            continue
        yield p


def gcd(a, b):
    while b:
        a, b = b, divmod_(a, b)[1]
    return a


def caseA(alpha):
    out = []
    for lam in range(0, alpha + 1):
        for a1p in monics(lam):
            a1 = mul(Tpow(alpha), a1p)
            for beta in range(0, alpha):  # beta <= alpha-1: T a1'b1 | E+1, deg E <= alpha+lam
                for b1 in monics(beta):
                    if deg(gcd(a1, b1)) > 0:
                        continue
                    S = add(a1, b1)
                    fac = factor(S)  # S monic since deg a1 > deg b1
                    ab = mul(a1p, b1)
                    for vec in divisors_vec(fac):
                        E = from_vec(fac, vec)
                        if deg(E) < 1:
                            continue
                        E1 = add(E, (1,))
                        K, r = divmod_(E1, ab)
                        if r or vT(E1) != 1:
                            continue
                        KT = divmod_(K, Tpow(1))[0]
                        for gv in divisors_vec(factor(KT)) if deg(KT) > 0 else [()]:
                            gp = from_vec(factor(KT), gv) if deg(KT) > 0 else (1,)
                            out.append((a1p, b1, gp, E, K))
    return out


def check_A(tup, alpha):
    a1p, b1, gp, E, K = tup
    Ta = Tpow(alpha); a1 = mul(Ta, a1p)
    F, r = divmod_(add(a1, b1), E); assert not r
    z, r = divmod_(add(F, b1), a1p); assert not r and z                         # (A0), z != 0
    assert not divmod_(add(mul(Ta, a1p), b1), E)[1]                            # (A1)
    assert not divmod_(add(Ta, mul(mul(b1, b1), K)), E)[1]                     # (A2)
    assert mul(mul(b1, K), F) == add(Ta, z)                                    # (A3)
    assert mul(b1, sub(mul(mul(a1p, K), F), (1,))) == add(mul(Ta, a1p), F)     # (A4)
    assert E[-1] == 1 and F[-1] == 1 and K[-1] == 1
    lam, beta, kap, f = deg(a1p), deg(b1), deg(K), deg(F)
    assert f == alpha - beta - kap and f <= alpha - 1
    ex = min(f, alpha - f - 1) if f >= beta else min(beta - lam, lam + alpha - beta - 1)
    assert ex <= (alpha - 1) / 2
    return (lam, beta, kap), ex


def famcheck(lmax, jmax, k=2):
    """forward completeness: brute-force Case B families from Lemma 1.1 data (L', j, gamma, g', E | D) at k, map each
    to (m', g', w, C) and check membership in F(s) as enumerated by caseB()."""
    cache = {}; n = 0
    for l in range(0, lmax + 1):
        for Lp in monics(l):
            facL = factor(Lp) if l > 0 else []
            for gv in (divisors_vec(facL) if l > 0 else [()]):
                g = from_vec(facL, gv) if l > 0 else (1,)
                m = divmod_(Lp, g)[0]
                for j in range(0, jmax + 1):
                    for gam in range(0, j + 1):
                        s = k + j + gam
                        D = add((1,), mul(Tpow(s), mul(Lp, g)))
                        fD = factor(D)
                        for ev in divisors_vec(fD):
                            E = from_vec(fD, ev)
                            if deg(E) < 1: continue
                            E2 = divmod_(D, E)[0]
                            E1 = add(E, (1,))
                            if divmod_(E1, Lp)[1] or vT(E1) != 1: continue   # E = -1 mod L', E = -1-cT mod T^2, c != 0
                            if E2[-1] != 1: continue
                            w = divmod_(E1, Lp)[0]; C, r = divmod_(add(E2, (1,)), Lp)
                            assert not r
                            if s not in cache:
                                cache[s] = {(t[0], t[1], t[2], t[3]) for t in caseB(s)}
                            assert (m, g, w, C) in cache[s], (Lp, g, j, gam, E)
                            n += 1
    print("famcheck q=%d k=%d deg L'<=%d j<=%d: %d families, all in F(s)" % (Q, k, lmax, jmax, n))


if __name__ == "__main__":
    Q = int(sys.argv[2]); mx = int(sys.argv[3])
    if sys.argv[1] == "caseB":
        for s in range(3, mx + 1):
            tups = caseB(s)
            pats = {}
            for tp in tups:
                pat, ex = check_B(tp, s)
                pats.setdefault(pat, [0, ex])[0] += 1
            worst = max((c / Q**ex for c, ex in pats.values()), default=0)
            print("q=%d s=%d |F(s)|=%d patterns=%d max count/q^exponent=%.3f" % (Q, s, len(tups), len(pats), worst), flush=True)
    elif sys.argv[1] == "famcheck":
        famcheck(mx, int(sys.argv[4]), int(sys.argv[5]) if len(sys.argv) > 5 else 2)
    else:
        for al in range(1, mx + 1):
            tups = caseA(al)
            for tp in tups:
                check_A(tp, al)
            nE = len({(t[0], t[1], t[3]) for t in tups}); nc = len({t[3] for t in tups})
            print("q=%d alpha=%d CaseA tuples (a1',b1,g',E)=%d  (a1',b1,E)=%d  distinct E=%d  mass(distinct E)*q^-alpha=%.4f"
                  % (Q, al, len(tups), nE, nc, nc * Q**(-al)), flush=True)

