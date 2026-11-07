"""Master set: ordered ES solutions (x,y,z) of 4/n, mapped to (g,a,b,c,eps) with
x~ = p-free parts, g = squarefree part of x~y~/z~ etc., 4gabc = sum eps_v v, eps_v in {1,n}.
Only valid as a bijection for prime n; for composite we just print what we get."""
import sys
from math import isqrt, gcd
from sympy import factorint, isprime
sys.path.insert(0, 'scripts')
from z62_parityf_enum import es_solutions
from itertools import permutations

def sqfree_split(m):
    """m = g * s^2 with g squarefree; return (g, s)."""
    f = factorint(m); g = 1; s = 1
    for q, e in f.items():
        if e % 2: g *= q
        s *= q ** (e // 2)
    return g, s

def master(n):
    out = []
    for sol in es_solutions(n):
        for (x, y, z) in set(permutations(sol)):
            tl = []
            eps = []
            for v in (x, y, z):
                if v % n == 0:
                    tl.append(v // n); eps.append(1)
                else:
                    tl.append(v); eps.append(n)
            xt, yt, zt = tl
            if (xt*yt) % zt or (xt*zt) % yt or (yt*zt) % xt:
                out.append(((x,y,z), None)); continue
            Pc = xt*yt//zt; Pb = xt*zt//yt; Pa = yt*zt//xt
            g, a = sqfree_split(Pa); gb, b = sqfree_split(Pb); gc, c = sqfree_split(Pc)
            if not (g == gb == gc):
                out.append(((x,y,z), None)); continue
            assert 4*g*a*b*c == eps[0]*a + eps[1]*b + eps[2]*c, ((x,y,z), g,a,b,c,eps)
            out.append(((x,y,z), (g,a,b,c,tuple(eps))))
    return out

if __name__ == "__main__":
    for n in map(int, sys.argv[1:]):
        print("n =", n, "prime" if isprime(n) else "composite")
        rows = master(n)
        for (xyz, m) in sorted(rows, key=lambda r: (r[1] is None, r[1] or (), r[0])):
            if m is None: print("  ", xyz, "NO MASTER FORM"); continue
            g,a,b,c,eps = m
            if a <= b <= c or True:
                print("  ", xyz, " g=%d (a,b,c)=(%d,%d,%d) eps=%s" % (g,a,b,c, ''.join('p' if e==n else '1' for e in eps)))
