# R215 — from-scratch: genuine (Pomerance–Weingartner divisibility-sense) Type I / Type II solutions of M/n at odd squares.
# Type I : n | x, gcd(n, y) = gcd(n, z) = 1.  Type II: n | y, n | z, gcd(n, x) = 1.
# Search via PW Prop 2.1 / 2.3 parametrisation with a-priori bounds, every hit re-checked exactly and re-classified by
# divisibility (so the parametrisation is only a search device, not trusted).
import sys
from math import gcd, isqrt
from fractions import Fraction as F

def typeII(M, n):
    # x = abd = (n+e)/M, x <= n/(M-2) (since y, z >= n)
    out = []
    X = n // (M - 2) if M > 2 else 10**9
    a = 1
    while a * a <= X:
        b = a
        while a * b <= X:
            s = a + b
            for e in range(1, s + 1):
                if s % e or (n + e) % (M * a * b): continue
                d = (n + e) // (M * a * b); c = s // e
                x, y, z = a*b*d, a*c*d*n, b*c*d*n
                assert F(1, x) + F(1, y) + F(1, z) == F(M, n)
                if gcd(x, n) == 1: out.append((x, y, z))
            b += 1
        a += 1
    return out

def typeI(M, n):
    # y = acd <= z = bcd, 1/y + 1/z >= (M-1)/n  =>  acd <= 2n/(M-1)
    out = []
    Y = 2 * n // (M - 1)
    for a in range(1, Y + 1):
        for c in range(1, Y // a + 1):
            for d in range(1, Y // (a * c) + 1):
                f = M * a * c * d - n
                if f <= 0: continue
                t = M * a * a * d + 1
                if t % f: continue
                e = t // f; b = c * e - a
                if b <= 0: continue
                x, y, z = a*b*d*n, a*c*d, b*c*d
                if F(1, x) + F(1, y) + F(1, z) != F(M, n): continue
                if gcd(y, n) == 1 and gcd(z, n) == 1: out.append((x, y, z))
    return out

if __name__ == "__main__":
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 99
    for M in map(int, sys.argv[2:]):
        ks = [k for k in range(3, K + 1, 2) if gcd(k, M) == 1]
        h2 = h1 = 0; ex = None
        for k in ks:
            n = k * k
            t2 = typeII(M, n); t1 = typeI(M, n)
            h2 += bool(t2); h1 += bool(t1)
            if ex is None and (t1 or t2): ex = (n, (t1 or t2)[0])
        print(f"M={M}: odd squares k^2, 3<=k<={K}, gcd(k,M)=1: {len(ks)}; with Type II: {h2}; with Type I: {h1}; first {ex}")
