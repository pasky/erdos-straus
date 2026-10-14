# R224: direct check (no Thm A) that n*G_w is a Gram matrix of three vectors of Z^3, vs the Thm A criterion (i),
# for all words of all odd n <= NMAX. G_w = [[v,-1,0],[-1,t,-1],[0,-1,u]] (Q_w = v x^2 + t y^2 + u z^2 - 2xy - 2yz).
import sys
from math import isqrt
from sympy import factorint
NMAX = int(sys.argv[1])
def reps(N):
    out = []
    for x in range(-isqrt(N), isqrt(N) + 1):
        r = N - x * x
        for y in range(-isqrt(r), isqrt(r) + 1):
            z2 = r - y * y; z = isqrt(z2)
            if z * z == z2:
                out.append((x, y, z))
                if z: out.append((x, y, -z))
    return out
def dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def embeds(n, t, u, v):
    R = {}
    def rp(N):
        if N not in R: R[N] = reps(N)
        return R[N]
    Bs = [b for b in rp(n * t) if b[0] >= b[1] >= b[2] >= 0]   # b up to signed permutations
    for b in Bs:
        As = [a for a in rp(n * v) if dot(a, b) == -n]
        Cs = [c for c in rp(n * u) if dot(c, b) == -n]
        for a in As:
            for c in Cs:
                if dot(a, c) == 0: return True
    return False
mism = 0; exc = []; nw = 0
for n in range(1, NMAX + 1, 2):
    L = [l for l, e in factorint(n).items() if e % 2]
    allemb = True
    for u in range(1, n + 3):
        for v in range(u, n + 3):
            if u * v > n + u + v: break
            if (n + u + v) % (u * v): continue
            t = (n + u + v) // (u * v); A = t * u - 1
            crit = all(leg(-A, l) == 1 for l in L)
            d = embeds(n, t, u, v); nw += 1
            if d != crit: mism += 1; print("MISMATCH", n, (t, u, v), d, crit)
            allemb &= d
    if allemb != (isqrt(n) ** 2 == n): exc.append(n)
print("odd n <=", NMAX, "unordered words", nw, "direct-vs-criterion mismatches", mism, "3SQ exceptions (direct)", exc)
