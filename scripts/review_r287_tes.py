"""R287 from-scratch check of POWER_LADDER_ES §6 (TES_(k) over Z[w], fixed shot g = -8 + w, N(g) = 73).

Own Eisenstein arithmetic (a + b w, w^2 = -1 - w). For every split rational prime 7 <= p <= X, p = 1 (3), p != 73,
both primes pi | p, normalised pi = 1 (mod 2O) (one of +-pi; the criterion is sign-blind since -1 is a square and a
cube in F_73), and n in {pi, pi^3}, k in {1,2,3}:
 (a) criterion: -n/18 is a k-th power in O/g = F_73 (w -> 8);
 (b) exact: search odd rational Q prime to 6p with g | n + 18 Q^k, build SPARKS2 Prop 3.1 solution
     E=(n+18D)/g, a=(g+w^2)/9, x=(wn+E)/9, y=na, Z=nxa and verify 9/n = w/x + w^2/y + 2D/Z exactly
     (as 9xyZ = w n y Z + w^2 n x Z + 2 D n x y), gcd(Q, Z) = 1 in O (via norms), x,y,Z = 1 mod 2, Type II at pi.
 (a) and (b) must agree. Also tabulates index gcd(k, 72) and that every prime g = 10+w (18), N(g) <= 3000 has N = 1 (18).
"""
import sys
from math import gcd, isqrt


def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def conj(x):
    return (x[0] - x[1], -x[1])


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def divexact(x, y):
    n = norm(y)
    t = mul(x, conj(y))
    if t[0] % n or t[1] % n:
        return None
    return (t[0] // n, t[1] // n)


def power(x, k):
    r = (1, 0)
    for _ in range(k):
        r = mul(r, x)
    return r


W, W2 = (0, 1), (-1, -1)
UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]


def odd1(x):  # = 1 mod 2O
    return (x[0] - 1) % 2 == 0 and x[1] % 2 == 0


def val(x, pi):
    c = 0
    while True:
        q = divexact(x, pi)
        if q is None:
            return c
        x, c = q, c + 1


def primes(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(N) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def split(p):
    out = set()
    for a in range(-isqrt(4 * p) - 2, isqrt(4 * p) + 3):
        for b in range(-isqrt(4 * p) - 2, isqrt(4 * p) + 3):
            if norm((a, b)) == p:
                out.add((a, b))
    # group into the two associate classes
    classes = []
    for z in sorted(out):
        if not any(divexact(z, c) in UNITS for c in classes):
            classes.append(z)
    assert len(classes) == 2, (p, classes)
    return [next(mul(u, c) for u in UNITS if odd1(mul(u, c))) for c in classes]


def main():
    X = int(sys.argv[1])
    g, ell, wg = (-8, 1), 73, 8
    assert norm(g) == 73 and (g[0] - 10) % 18 == 0 and (g[1] - 1) % 18 == 0
    assert (wg * wg + wg + 1) % ell == 0 and (g[0] + g[1] * wg) % ell == 0
    a = divexact(add(g, W2), (9, 0))
    print("a = (g + w^2)/9 =", a)
    # every prime element = 10 + w (18) of prime norm <= 3000: norm = 1 mod 18
    bad = 0
    for l in primes(3000):
        if l % 3 == 1:
            for c in split(l):
                for u in UNITS:
                    h = mul(u, c)
                    if (h[0] - 10) % 18 == 0 and (h[1] - 1) % 18 == 0 and l % 18 != 1:
                        bad += 1
    print("class primes with N != 1 (18):", bad)
    inv18 = pow(18, -1, ell)
    tab = {}
    for p in primes(X):
        if p % 3 != 1 or p < 7 or p == ell:
            continue
        for pi in split(p):
            for tag, e in (("prime", 1), ("cube", 3)):
                n = power(pi, e)
                t = (-(n[0] + n[1] * wg) * inv18) % ell
                for k in (1, 2, 3):
                    crit = pow(t, (ell - 1) // gcd(k, ell - 1), ell) == 1
                    hit = None
                    for Q in range(1, 12 * ell, 2):
                        if gcd(Q, 6 * p) != 1:
                            continue
                        D = (Q ** k, 0)
                        Ee = divexact(add(n, mul((18, 0), D)), g)
                        if Ee is None:
                            continue
                        x = divexact(add(mul(W, n), Ee), (9, 0))
                        assert x is not None
                        y = mul(n, a); Z = mul(mul(n, x), a)
                        lhs = add(add(mul(mul(W, n), mul(y, Z)), mul(mul(W2, n), mul(x, Z))),
                                  mul(mul((2, 0), D), mul(n, mul(x, y))))
                        assert lhs == mul((9, 0), mul(x, mul(y, Z)))
                        assert gcd(Q, norm(Z)) == 1  # gcd(Q, Z) = 1 in O
                        assert odd1(x) and odd1(y) and odd1(Z), (x, y, Z)
                        typeII = val(x, pi) == 0 and val(y, pi) >= e and val(Z, pi) >= e
                        hit = typeII
                        break
                    assert crit == (hit is not None), (p, pi, tag, k)
                    r = tab.setdefault((tag, k), [0, 0, 0])
                    r[0] += 1; r[1] += hit is not None; r[2] += bool(hit)
    for key in sorted(tab):
        print(key, "fires %d/%d, Type II %d" % (tab[key][1], tab[key][0], tab[key][2]))
    print("index gcd(k,72):", {k: gcd(k, 72) for k in (1, 2, 3, 4, 5, 7, 8, 9)})


if __name__ == "__main__":
    main()
