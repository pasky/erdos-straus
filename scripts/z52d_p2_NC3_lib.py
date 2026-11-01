"""Shared helpers for batch NC3 (z52d pass 2). Words of level 3: tuv - u - v = p, t,u,v >= 2.
A = tu-1, A* = tv-1, A*A = tp+1 (DEDEKIND_ES.md Lemma 1.1). L3(p) = {A : r(p/A) = 3}."""
import math
from functools import lru_cache

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def words(p):
    """All (t,u,v), t,u,v>=2 with t*u*v - u - v = p. For each u>=2: A=t*u-1 must divide p+u, t=(A+1)/u."""
    out = []
    for u in range(2, p + 1):
        M = p + u
        # need A = t*u-1 | M with t>=2  (A>=2u-1); A <= M
        for A in range(2 * u - 1, M + 1):
            if (A + 1) % u: continue
            if M % A: continue
            t = (A + 1) // u
            v = M // A
            if v >= 2 and t >= 2:
                out.append((t, u, v))
    return out

def L3(p):
    """Set of A=tu-1 over words (A in (0,p))."""
    return sorted({t*u-1 for (t, u, v) in words(p)})

def hj_len(n, a):
    """Length r of Hirzebruch-Jung expansion n/a = [[b1..br]], b_i>=2 (0<a<n, gcd=1)."""
    r = 0
    x, y = n, a
    while y:
        b = -(-x // y)  # ceil
        r += 1
        x, y = y, b*y - x
    return r

def hj_expansion(n, a):
    bs = []
    x, y = n, a
    while y:
        b = -(-x // y); bs.append(b); x, y = y, b*y - x
    return bs
