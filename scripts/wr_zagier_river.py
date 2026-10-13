"""Zagier windmill <-> Conway river / reduction dictionary checks (O164 §1).

Y(D) = {[a,b,c]: a>0>c, b^2-4ac = D}  (simple forms = oriented river edges).
X(p) = {(x,y,z)>0: x^2+4yz=p}  <->  [y, x, -z] in Y(p) with b = x > 0.
R = river step [a,b,c] -> [a+b+c, b+2c, c] if a+b+c>0 else [a, b+2a, a+b+c].
Usage: python wr_zagier_river.py PMAX
"""
import sys
from math import isqrt


def Y(D):
    out = []
    for b in range(-isqrt(D) - 1, isqrt(D) + 2):
        r = D - b * b
        if r <= 0 or r % 4:
            continue
        m = r // 4  # = -a c
        for a in range(1, m + 1):
            if m % a == 0:
                out.append((a, b, -(m // a)))
    return out


def R(f):
    a, b, c = f
    v = a + b + c
    return (v, b + 2 * c, c) if v > 0 else (a, b + 2 * a, v)


def zagier(t):
    x, y, z = t
    if x < y - z:
        return (x + 2 * z, z, y - x - z)
    if x < 2 * y:
        return (2 * y - x, y, x - y + z)
    return (x - 2 * y, x - y + z, y)


def cycles(perm, S):
    seen, cyc = set(), []
    for s in S:
        if s in seen:
            continue
        c = []
        while s not in seen:
            seen.add(s)
            c.append(s)
            s = perm(s)
        cyc.append(c)
    return cyc


def isprime(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))


def main(pmax):
    bad = 0
    for p in range(5, pmax + 1, 4):
        if not isprime(p):
            continue
        S = Y(p)
        Sset = set(S)
        assert all(R(f) in Sset for f in S)
        riv = cycles(R, S)  # rivers = proper classes (each cycle one period)
        X = [(b, a, -c) for (a, b, c) in S if b > 0]
        # (1) Zagier map as form map: zeta(phi) = -phi o g ; check class relation:
        cls = {}
        for i, c in enumerate(riv):
            for f in c:
                cls[f] = i
        neg = lambda f: (-f[2], f[1], -f[0])  # [a,b,c] -> [-c,b,-a] is (-phi) in basis (e2,-e1)?
        rel = set()
        for t in X:
            u = zagier(t)
            f, g = (t[1], t[0], -t[2]), (u[1], u[0], -u[2])
            rel.add((cls[f], cls[g]))
        # (2) composition zeta o swap on X
        sw = lambda t: (t[0], t[2], t[1])
        comp = cycles(lambda t: zagier(sw(t)), X)
        print(p, "classes(h+)", len(riv), "riverlens", sorted(len(c) for c in riv),
              "|X|", len(X), "zeta.sw cyclens", sorted(len(c) for c in comp),
              "zeta class-pairs", sorted(rel)[:6])
        bad += 0
    return bad


if __name__ == "__main__":
    main(int(sys.argv[1]))
