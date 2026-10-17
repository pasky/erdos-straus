"""O257 helpers: all solutions (via the C solver z28_lab) and their ET slice representations for prime n.
A representation of a Type II solution (x, y, z) = (abd, acdn, bcdn) [Type I: (abdn, acd, bcd)] is any d with
a^2 d = X Y/Z, b^2 d = X Z/Y, c^2 d = Y Z/X integral squares (X, Y, Z the n-free parts); modulus H = k a b."""
import subprocess, os
from math import isqrt, gcd
from functools import lru_cache
LAB = '/tmp/z28_lab'
if not os.path.exists(LAB):
    subprocess.run(['gcc', '-O2', '-o', LAB, os.path.join(os.path.dirname(__file__), 'z28_lab.c')], check=True)

@lru_cache(maxsize=None)
def sols(n, k=4):
    out = subprocess.run([LAB, 'sol', str(k), str(n)], capture_output=True, text=True, check=True).stdout
    return tuple(tuple(map(int, l.split())) for l in out.split('\n') if l)

def _sq(v):
    r = isqrt(v); return r if r * r == v else None

@lru_cache(maxsize=None)
def reps(n, k=4):
    """list of (theta, a, b, c, d, e, H) over all solutions and representations (prime n, n ∤ k)."""
    res = []
    for s in sols(n, k):
        dv = [t % n == 0 for t in s]
        if sum(dv) == 2:
            th = 'II'; X = [t for t, f in zip(s, dv) if not f][0]; Y, Z = [t // n for t, f in zip(s, dv) if f]
        elif sum(dv) == 1:
            th = 'I'; X = [t // n for t, f in zip(s, dv) if f][0]; Y, Z = [t for t, f in zip(s, dv) if not f]
        else:
            continue
        g = gcd(gcd(X, Y), Z)
        for d in range(1, g + 1):
            if g % d: continue
            if (X * Y) % (Z * d) or (X * Z) % (Y * d) or (Y * Z) % (X * d): continue
            a = _sq(X * Y // (Z * d)); b = _sq(X * Z // (Y * d)); c = _sq(Y * Z // (X * d))
            if None in (a, b, c) or a * b * d != X: continue
            if (a + b) % c: continue
            e = (a + b) // c; H = k * a * b
            N = n + e if th == 'II' else n * e + 1
            assert N == H * d, (n, s, th, a, b, c, d)
            res.append((th, a, b, c, d, e, H))
    return tuple(res)

def is_square_mod(r, L):
    """r (coprime to L) is a square mod L."""
    from sympy import factorint
    for l, v in factorint(L).items():
        if l == 2:
            if v == 2 and r % 4 != 1: return False
            if v >= 3 and r % 8 != 1: return False
        elif pow(r % l, (l - 1) // 2, l) != 1:
            return False
    return True
