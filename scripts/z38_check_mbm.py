"""z38_check_mbm.py: brute-force M_BM(n) = sum_{pairs, gcd(n,q)=1} (1 - kron(-4uB,n))/phi(4uB) and R*(n), to cross-check z38_mbm.c."""
import sys
from math import gcd
from sympy import totient
from z38_bm_dictionary import kron
for n in map(int, sys.argv[1:]):
    R = 0; M = 0.0; M8 = 0.0
    for u in range(1, n):
        if 3*u-1 > n: break
        for B in range(1, (n+u)//(4*u-1)+1):
            if (u+B) % 2 == 0 or gcd(u, B) != 1: continue
            q = 4*u*B
            if (n+u+B) % q == 0: R += 1
            if gcd(n, q) == 1:
                M += (1 - kron(-4*u*B, n))/int(totient(q))
                # projection onto <chars mod 8, chi_{-4uB}>: average of chi(n)chi(a) over that group
                a = -(u+B); grp = set()
                for e1 in (0, 1):
                    for e2 in (0, 1):
                        for e3 in (0, 1):
                            grp.add((e1, e2, e3))
                vals = []
                for (e1, e2, e3) in grp:
                    f = lambda x: kron(-4, x)**e1 * kron(8, x)**e2 * kron(-4*u*B, x)**e3
                    vals.append(((e1, e2, e3), f(n)*f(a)))
                # distinct characters: chi_{-4uB} may coincide with a mod-8 character (odd part of uB = 1)
                o = u*B
                while o % 2 == 0: o //= 2
                # deduplicate characters by their value vector on (Z/q)^x (review fix: coincidence iff odd part of uB is a square)
                units = [x for x in range(1, q) if gcd(x, q) == 1]
                seen = {}
                for (e1, e2, e3) in grp:
                    f = lambda x, e1=e1, e2=e2, e3=e3: kron(-4, x)**e1 * kron(8, x)**e2 * kron(-4*u*B, x)**e3
                    vec = tuple(f(x) for x in units)
                    if vec not in seen: seen[vec] = f(n)*f(a)
                M8 += sum(seen.values())/int(totient(q))
    print(n, R, round(M, 4), round(M8, 4))
