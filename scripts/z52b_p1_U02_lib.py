"""Shared helpers for z52b pass-1 batch U02 (cheap first steps).

esols(n): all (x,y,z) with 1 <= x <= y <= z and 4/n = 1/x + 1/y + 1/z (n >= 2),
via the divisor method: for x, with a = 4x - n, b = n*x, 1/y+1/z = a/b  <=>
(a*y - b)(a*z - b) = b^2, so enumerate divisors d | b^2 with d <= b, d = -b (mod a).
"""
import math
import numpy as np
from sympy import divisors


def esols(n):
    out = []
    for x in range(-(-n // 4), (3 * n) // 4 + 1):
        a = 4 * x - n
        if a <= 0:
            continue
        b = n * x
        if b < 1:
            continue
        # y >= x and y <= 2b/a (since 1/y <= a/(2b))
        ymax = (2 * b) // a
        for d in divisors(b * b):
            if d > b:
                continue
            if (d + b) % a:
                continue
            y = (d + b) // a
            if y < x or y > ymax:
                continue
            e = b * b // d
            if (e + b) % a:
                continue
            z = (e + b) // a
            if y <= z:
                out.append((x, y, z))
    return out

def U_count(n):
    return len(esols(n))

def load_f4():
    import numpy as np
    return np.loadtxt('data/z52b/raw/f4_all_30000.txt' if False else
                      '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
