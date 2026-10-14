# R224: §4.1 representation numbers r(T_w, I3) and §4.2 conic heights, from scratch.
import sys
from math import isqrt, gcd
from sympy import isprime
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def vecs(N):
    out = []
    for a in range(-isqrt(N), isqrt(N) + 1):
        m = N - a * a
        for b in range(-isqrt(m), isqrt(m) + 1):
            c2 = m - b * b; c = isqrt(c2)
            if c * c == c2:
                out.append((a, b, c))
                if c: out.append((a, b, -c))
    return out
def cross(x, y): return (x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0])
def dot(x, y): return sum(a * b for a, b in zip(x, y))
def words(p):
    for t in range(1, p + 3):
        M = t * p + 1
        for A in range(t - 1, isqrt(M) + 1, t):   # A = -1 mod t, A <= A*
            if A > 0 and M % A == 0 and ((M // A) + 1) % t == 0:
                yield t, (A + 1) // t, (M // A + 1) // t
def pairs(A, As):
    VY = vecs(A); VX = vecs(As)
    for x in VX:
        for y in VY:
            if dot(x, y) == 1: yield x, y
def height(z, p):
    best = p
    for lam in range(1, p):
        s = 0
        for c in z:
            r = lam * c % p; r = min(r, p - r); s += r * r
        best = min(best, s // p)   # s is divisible by p (z isotropic mod p)
    return best
mode = sys.argv[1]
if mode == "r":
    P = int(sys.argv[2]); ratios = set(); bad = 0; nw = 0
    for p in range(5, P + 1, 4):
        if not isprime(p): continue
        S = Np = 0
        for t, u, v in words(p):
            A, As = t * u - 1, t * v - 1
            r = sum(1 for _ in pairs(A, As)); mult = 1 if u == v else 2; nw += mult
            if (r > 0) != (leg(A, p) == 1): bad += 1; print("ThmA(iii) MISMATCH", p, t, u, v)
            if r: ratios.add(r / 48); assert r % 48 == 0 or print("r not /48", p, t, u, v, r)
            S += mult * r; Np += mult * (leg(A, p) == 1)
        if p in (5, 13, 17, 29, 53, 61): print(p, "sum r/48 =", S / 48, "N+ =", Np)
    print("primes <=", P, "ordered words", nw, "Thm A (iii) mismatches", bad, "r/48 values", sorted(ratios))
    r = rs = 0
    for x, y in pairs(62, 62):
        r += 1; z = cross(x, y); rs += gcd(gcd(z[0], z[1]), z[2]) == 1
    print("p=61 (63,1,1): r =", r, "r* (x×y primitive) =", rs)
elif mode == "h":
    p = int(sys.argv[2]); LIM = int(sys.argv[3])
    for t, u, v in words(p):
        A, As = t * u - 1, t * v - 1
        if leg(A, p) != 1 or max(A, As) > LIM: continue
        hs = set(); hall = set()
        for x, y in pairs(A, As):
            z = cross(x, y); h = height(z, p) if any(c % p for c in z) else None
            hall.add(h)
            if all((z[i] - x[i] - y[i]) % t == 0 for i in range(3)): hs.add(h)
        print("p=%d word (%d,%d,%d) min letter %d: heights over compatible pairs %s, over all pairs %s" % (p, t, u, v, min(t, u, v), sorted(hs), sorted(hall, key=str)))
elif mode == "g":   # z^perp for |z|^2 = p primitive lies in the principal genus of disc -4p ((a/p) = +1 for the form's values)
    bad = 0
    for p in range(5, int(sys.argv[2]) + 1, 4):
        if not isprime(p): continue
        for z in vecs(p):
            if gcd(gcd(*z[:2]), z[2]) != 1: continue
            vals = [dot(w, w) for w in vecs(p * p)[:0]]
            # values of the binary form z^perp: norms of integer vectors orthogonal to z, small box
            vs = [dot(w, w) for w in ((a, b, c) for a in range(-6, 7) for b in range(-6, 7) for c in range(-6, 7)) if dot(w, z) == 0 and dot(w, w) % p]
            if any(leg(n, p) != 1 for n in vs): bad += 1; print("genus FAIL", p, z)
    print("z^perp genus check failures:", bad)
