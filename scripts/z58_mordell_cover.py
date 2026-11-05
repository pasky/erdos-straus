# z58 MORDELL: Mordell-type covering of unit residue classes mod L by one-parameter ES identity families
# (the ET-shaped menu of BRAINSTORM/y7_mordell_levels.md, reimplemented with numpy; plus the (★)-only sub-menu).
# Families for 4/n (each a polynomial identity; one-line proofs in BRAINSTORM/y7_mordell_levels.md):
#  II-d: n = 4abd - e, e | a+b                      class -e            mod 4ab        (d free)
#  II-c: b = ce - a                                  class -4a^2 d - e   mod 4ade       (c free)
#  II-e: b = ce - a                                  class -4a^2 d       mod 4acd - 1   (e free)   [(★) = II-e with c=1]
#  I-d : ne + 1 = 4abd, e | a+b, gcd(e,4ab)=1        class -e^{-1}       mod 4ab        (d free)
#  I-c : b = ce - a, e | 4a^2 d + 1                  class -(4a^2d+1)/e  mod 4ad        (c free)
#  (★) menu ("star") = the one-parameter (★) families: fixed (u,C) [class H_d, d = 4uC-1 = II-e with c=1] and
#  fixed (u,B) [class -(u+B) mod 4uB = II-d with e = a+b]; menu "starH" = fixed (u,C) only (the H_d classes).
# Every n >= 1 in a covered class has an explicit solution (positivity: see BRAINSTORM/y7_mordell_levels.md).
# Usage: python z58_mordell_cover.py L [menu]   menu in {es, star, starH}; prints uncovered unit classes.
import sys
from math import gcd
import numpy as np

def divisors(x):
    out = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            out.append(i)
            if i * i != x:
                out.append(x // i)
        i += 1
    return sorted(out)

def cover(L, menu="es", M=4):
    cov = np.zeros(L, dtype=bool)
    D = divisors(L)
    def add(cls, q):
        if q <= 0 or L % q:
            return
        cov[cls % q::q] = True
    if menu == "es":
        for q in D:
            if q % M:
                continue
            ab = q // M
            for a in divisors(ab):
                b = ab // a
                for e in divisors(a + b):
                    add(-e, q)                                  # II-d
                    if gcd(e, q) == 1:
                        add(-pow(e, -1, q), q)                  # I-d
            r = q // M
            for a in divisors(r):
                for d in divisors(r // a):
                    e = r // (a * d)
                    add(-M * a * a * d - e, q)                  # II-c
            for a in divisors(r):
                d = r // a
                t = M * a * a * d + 1
                for e in divisors(t):
                    add(-(t // e), q)                           # I-c
    if menu == "star":                                          # fixed (u,B): n = 4uBC - u - B
        for q in D:
            if q % M: continue
            ab = q // M
            for a in divisors(ab):
                add(-(a + ab // a), q)
    for g in D:                                                 # II-e (all c) / (★) (c = 1)
        if (g + 1) % M:
            continue
        acd = (g + 1) // M
        for a in divisors(acd):
            for d in divisors(acd // a):
                c = acd // (a * d)
                if menu in ("star", "starH") and c != 1:
                    continue
                add(-M * a * a * d, g)
    return cov

def units(L):
    u = np.ones(L, dtype=bool)
    for q in prime_factors(L):
        u[::q] = False
    return u

def prime_factors(n):
    ps, q = [], 2
    while q * q <= n:
        if n % q == 0:
            ps.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        ps.append(n)
    return ps

def unit_squares(L):
    sq = np.zeros(L, dtype=bool)
    x = np.arange(L, dtype=np.int64)
    sq[(x * x) % L] = True
    return sq & units(L)

def uncovered(L, menu="es", restrict_mod4=True):
    u = units(L)
    cov = cover(L, menu)
    unc = u & ~cov
    if restrict_mod4 and L % 4 == 0:
        m = np.zeros(L, dtype=bool); m[1::4] = True
        unc &= m
    return unc

if __name__ == "__main__":
    L = int(sys.argv[1]); menu = sys.argv[2] if len(sys.argv) > 2 else "es"
    unc = uncovered(L, menu)
    sq = unit_squares(L)
    U = np.nonzero(unc)[0]
    ns = [int(r) for r in U if not sq[r]]
    print(f"L={L} menu={menu} uncovered(≡1 mod 4 units)={len(U)} squares={int((unc & sq).sum())}/{int(sq.sum())} "
          f"nonsquares={len(ns)}")
    print("nonsquare uncovered:", ns[:200])
