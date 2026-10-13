"""R164 from-scratch check of WINDMILL_REDUCTION §1 (Computation 1.2).
For primes p = 1 mod 4 up to N:
  * h+(p) computed independently by Gauss reduced indefinite forms and the standard rho-cycles
    (proper SL2(Z) equivalence = narrow classes);
  * cycles of zeta∘sigma on X(p) = {x^2+4yz=p}; each cycle -> class of [y,x,-z]; check bijection;
  * cycle length vs river period (number of R steps, R as in the doc; also count via rho-cycle:
    river period = sum of |partial quotients| of the reduced cycle);
  * zeta maps cycle(C) onto cycle(C^{-1}).
"""
import sys
from math import isqrt


def primes(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def is_reduced(a, b, c, D):
    r = isqrt(D)  # D nonsquare: sqrt(D) in (r, r+1)
    # 0 < b < sqrt D and sqrt D - b < 2|a| < sqrt D + b
    return 0 < b <= r and (r - b) < 2 * abs(a) <= (r + b)  # integer version: sqrtD-b<2|a| <=> r-b<2|a| (as 2|a| int, sqrtD nonint)


def rho(a, b, c, D):
    """Gauss/Buchmann rho: (a,b,c) -> (c, b', ...) with b' = -b mod 2c in the reduced window."""
    r = isqrt(D)
    cc = abs(c)
    # choose b' == -b mod 2c, with r - 2|c| < b' <= r  (if |c| <= r/... standard normalisation)
    if cc <= r:
        # b' in (r-2|c|, r]
        bp = -b + 2 * cc * ((r + b) // (2 * cc))
    else:
        # b' in (-|c|, |c|]
        bp = -b + 2 * cc * ((cc + b) // (2 * cc))
        if bp > cc:
            bp -= 2 * cc
    assert (bp * bp - D) % (4 * c) == 0
    return (c, bp, (bp * bp - D) // (4 * c))


def reduce_form(f, D):
    a, b, c = f
    for _ in range(10000):
        if is_reduced(a, b, c, D):
            return (a, b, c)
        a, b, c = rho(a, b, c, D)
    raise RuntimeError("no reduction")


def cycle_of(f, D):
    f = reduce_form(f, D)
    cyc = [f]
    g = rho(*f, D)
    while g != f:
        cyc.append(g)
        g = rho(*g, D)
        assert len(cyc) < 10 ** 6
    return cyc


def canon(f, D):
    return min(cycle_of(f, D))


def all_reduced(D):
    r = isqrt(D)
    out = []
    for b in range(1, r + 1):
        if (b * b - D) % 4:
            continue
        m = (D - b * b) // 4
        for a in range(1, m + 1):
            if m % a == 0 and is_reduced(a, b, 0, D):
                c = -m // a
                out += [(a, b, c), (-a, b, -c)]
    return out


def zeta(x, y, z):
    if x < y - z:
        return (x + 2 * z, z, y - x - z)
    if x < 2 * y:
        return (2 * y - x, y, x - y + z)
    return (x - 2 * y, x - y + z, y)


def Rstep(a, b, c):
    if a + b + c > 0:
        return (a + b + c, b + 2 * c, c)
    return (a, b + 2 * a, a + b + c)


def river_period(f):
    g = Rstep(*f); n = 1
    while g != f:
        g = Rstep(*g); n += 1
    return n


def check(p):
    D = p
    red = all_reduced(D)
    classes = {}
    for f in red:
        classes.setdefault(canon(f, D), None)
    hplus = len(classes)
    X = [(x, y, (p - x * x) // (4 * y)) for x in range(1, isqrt(p) + 1, 2)
         for y in range(1, (p - x * x) // 4 + 1) if ((p - x * x) // 4) % y == 0 and (p - x * x) % 4 == 0]
    Xs = set(X)
    # zeta involution check
    for P in X:
        Q = zeta(*P); assert Q in Xs and zeta(*Q) == P
    seen = {}
    cycles = []
    for P in X:
        if P in seen:
            continue
        cyc = [P]; seen[P] = len(cycles)
        Q = zeta(Q[0], Q[2], Q[1]) if False else zeta(P[0], P[2], P[1])
        while Q != P:
            seen[Q] = len(cycles); cyc.append(Q)
            Q = zeta(Q[0], Q[2], Q[1])
        cycles.append(cyc)
    ok = True
    cls_of_cycle = []
    for cyc in cycles:
        cs = {canon((y, x, -z), D) for (x, y, z) in cyc}
        if len(cs) != 1:
            ok = False
        c0 = cs.pop()
        cls_of_cycle.append(c0)
        x, y, z = cyc[0]
        L = river_period((y, x, -z))
        if 2 * len(cyc) != L:
            ok = False
    if len(set(cls_of_cycle)) != len(cycles) or len(cycles) != hplus:
        ok = False
    # zeta maps cycle C onto cycle C^{-1}
    for i, cyc in enumerate(cycles):
        imgs = {seen[zeta(*P)] for P in cyc}
        if len(imgs) != 1:
            ok = False
        j = imgs.pop()
        x, y, z = cyc[0]
        inv = canon((y, -x, -z), D)
        if cls_of_cycle[j] != inv:
            ok = False
        if (i == j) != (cls_of_cycle[i] == canon((1, 1, -(p - 1) // 4), D)):
            ok = False
    return ok, hplus, sorted(len(c) for c in cycles)


if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    bad = 0; n = 0
    for p in primes(hi):
        if p < lo or p % 4 != 1:
            continue
        ok, h, ls = check(p); n += 1
        if not ok:
            bad += 1; print("FAIL", p, h, ls)
        if p == 1297:
            print(p, h, ls)
    print(f"checked {n} primes in [{lo},{hi}], failures {bad}")
