"""R175 from-scratch enumeration of Case B families on the slice x = 1 off T (q = 3, A = T^2).

Independent of scripts/bsB_*.  Own F_3[T] arithmetic (coefficient lists, low degree first).

Two modes:
  enum KMAX   : enumerate all (h1, h1') with deg h1 + deg h1' <= K, h1(0) = -h1'(0) != 0, both monic;
                L'' = quo(T^K, h1 h1'), r = L'' h1 h1' - T^K, g' = (h1 + h1')/(T r) (must be monic poly),
                require r(0) != 0, deg r < deg(h1 h1').  Print per-K counts, x* coverage, union measure.
  brute NMAX DLMAX : independent check of Lemma 1.1 itself straight from FF2's reduction:
                for all N <= NMAX, gamma <= N-1, monic L' (T not | L') of degree <= DLMAX, monic g' | L',
                factor D = 1 + T^(N+1+gamma) L' g' into all monic divisors E, keep E = -1 mod L' and
                E(0) = -1 (slice u(0) = 1) with v := -(E+1)/T mod T^N having v(0) != 0;
                record (K, cylinder of v mod T^N).  Compare against enum.
"""
import sys, itertools
from collections import defaultdict

P = 3

def trim(a):
    while a and a[-1] % P == 0:
        a.pop()
    return a

def add(a, b):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P for i in range(n)])

def neg(a):
    return [(-x) % P for x in a]

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] += x * y
    return trim([x % P for x in c])

def divmod_(a, b):
    """a = q b + r, deg r < deg b; b monic-or-not (lc invertible mod 3)."""
    a = list(a)
    db = len(b) - 1
    inv = 1 if b[-1] == 1 else 2
    q = [0] * max(0, len(a) - db)
    while len(a) - 1 >= db and a:
        coef = (a[-1] * inv) % P
        sh = len(a) - 1 - db
        q[sh] = coef
        for j, y in enumerate(b):
            a[sh + j] = (a[sh + j] - coef * y) % P
        trim(a)
    return trim(q), a

def Tpow(k):
    return [0] * k + [1]

def monic_polys(deg, c0=None):
    """monic polys of degree deg; if c0 given, constant term fixed to c0 (deg>=1) or poly must equal 1."""
    if deg == 0:
        if c0 is None or c0 == 1:
            yield [1]
        return
    consts = [c0] if c0 is not None else [1, 2]
    for c in consts:
        for mid in itertools.product(range(P), repeat=deg - 1):
            yield [c] + list(mid) + [1]

def enum(KMAX):
    sols = []  # (K, a, b, cylinder tuple of v mod T^N0, data)
    for K in range(0, KMAX + 1):
        TK = Tpow(K)
        cnt = 0
        for d in range(1, K + 1):
            for a in range(0, d + 1):
                b = d - a
                for h1 in monic_polys(a):
                    c0 = (-h1[0]) % P
                    for h2 in monic_polys(b, c0):
                        prod = mul(h1, h2)
                        L2, rem = divmod_(TK, prod)
                        r = neg(rem)  # r = L2*prod - T^K = -rem
                        if not r or r[0] == 0:
                            continue
                        if not L2 or L2[0] == 0:
                            continue
                        s = add(h1, h2)
                        if not s or s[0] != 0:
                            continue
                        s1 = s[1:]  # s / T
                        g, rr = divmod_(s1, r)
                        if rr or not g or g[-1] != 1 or g[0] == 0:
                            continue
                        Lp = mul(g, L2)
                        w = mul(h1, Lp)
                        N0 = max(2, -(-K // 2) + 1)
                        vcyl = tuple(((-(w[i] if i < len(w) else 0)) % P) for i in range(N0))
                        sols.append((K, a, b, vcyl, (h1, h2, g, L2, r)))
                        cnt += 1
        print(f"K {K} count {cnt}", flush=True)
    return sols

def union_measure(cyls):
    cyls = sorted(set(cyls), key=len)
    mins = []
    pref = set()
    for c in cyls:
        if any(c[:l] in pref for l in range(1, len(c) + 1)):
            continue
        mins.append(c)
        pref.add(c)
    from fractions import Fraction
    m = sum(Fraction(1, 2 * 3 ** (len(c) - 1)) for c in mins)
    return m, mins

def covered(v, mins):
    return any(tuple(v[:len(c)]) == c for c in mins)

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "enum":
        KMAX = int(sys.argv[2])
        sols = enum(KMAX)
        out = sys.argv[3] if len(sys.argv) > 3 else None
        if out:
            with open(out, "w") as f:
                for K, a, b, vc, (h1, h2, g, L2, r) in sols:
                    f.write(f"{K} {a} {b} {''.join(map(str, vc))} h1={h1} h1p={h2} g={g} L2={L2} r={r}\n")
        for Kc in range(2, KMAX + 1):
            m, mins = union_measure([s[3] for s in sols if s[0] <= Kc])
            xs = [covered([c] + [0] * 40, mins) for c in (1, 2)]
            ys = [covered([c ** k % P for k in range(1, 42)], mins) for c in (1, 2)]  # v of 1/(1-cT)
            print(f"K<= {Kc}: union measure {float(m):.6f} = {m}  x*_1,x*_2 covered {xs}  iota(x*) covered {ys}")


# ---------------- brute mode: check Lemma 1.1 against direct factorisation of D -------------
def irreducibles(maxdeg):
    irr = []
    for d in range(1, maxdeg + 1):
        for f in monic_polys(d):
            if all(divmod_(f, p)[1] for p in irr if 2 * (len(p) - 1) <= d):
                irr.append(f)
    return irr

def factor(f, irr):
    fac = []
    for p in irr:
        if 2 * (len(p) - 1) > len(f) - 1:
            break
        e = 0
        while True:
            q, r = divmod_(f, p)
            if r:
                break
            f = q; e += 1
        if e:
            fac.append((p, e))
    if len(f) > 1:
        fac.append((f, 1))
    return fac

def divisors(fac):
    divs = [[1]]
    for p, e in fac:
        new = []
        for d in divs:
            x = d
            for _ in range(e + 1):
                new.append(x)
                x = mul(x, p)
        divs = new
    return divs

def brute(NMAX, DLMAX):
    irr = irreducibles((NMAX + 1 + NMAX - 1 + 2 * DLMAX) // 2)
    found = set()
    Lps = [L for d in range(0, DLMAX + 1) for L in monic_polys(d)]
    for N in range(1, NMAX + 1):
        for gam in range(0, N):
            for Lp in Lps:
                for gp in divisors(factor(Lp, irr)):
                    D = add([1], mul(Tpow(N + 1 + gam), mul(Lp, gp)))
                    for E in divisors(factor(D, irr)):
                        if E[0] != P - 1:          # E(0) = -1  <=>  u(0) = 1
                            continue
                        if divmod_(add(E, [1]), Lp)[1]:
                            continue
                        Ep1 = add(E, [1])          # = -T v  mod T^(N+1)
                        v = [(-(Ep1[i] if i < len(Ep1) else 0)) % P for i in range(1, N + 1)]
                        if v[0] == 0:
                            continue
                        found.add((N, gam, tuple(Lp), tuple(gp), tuple(E)))
    return found

def from_enum(sols, NMAX, DLMAX):
    exp = set()
    for K, a, b, vc, (h1, h2, g, L2, r) in sols:
        Lp = mul(g, L2)
        if len(Lp) - 1 > DLMAX:
            continue
        E = add([P - 1], mul(Tpow(1), mul(h1, Lp)))
        for N in range(1, NMAX + 1):
            gam = K + 1 - N
            if 0 <= gam <= N - 1:
                exp.add((N, gam, tuple(Lp), tuple(g), tuple(E)))
    return exp

if __name__ == "__main__" and sys.argv[1] == "brute":
    NMAX, DLMAX = int(sys.argv[2]), int(sys.argv[3])
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        sols = enum(2 * NMAX - 2)
    exp = from_enum(sols, NMAX, DLMAX)
    got = brute(NMAX, DLMAX)
    print("brute families", len(got), "enum-predicted", len(exp), "equal", got == exp)
    print("brute-only", sorted(got - exp)[:5]); print("enum-only", sorted(exp - got)[:5])
    # which (N, gamma) occur
    print("N=1 families:", [f for f in got if f[0] == 1])
