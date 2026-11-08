#!/usr/bin/env python3
"""z66 HSTARF: enumerate all ES solutions 4/p = 1/x+1/y+1/z (x<=y<=z) for a prime p,
classify by the number of denominators divisible by p, and cross-check against
 * Type II  : 4abcd = a + b + pc           (x,y,z) = (bcdp, acdp, abd)
 * (star)   : c = 1 sub-case 4abd = a + b + p
 * Type I   : 4X-1 = pt, X^2 = e*f with 4e = -1 (mod t) [p | exactly one denominator]
Usage: uv run scripts/z66_hstarf_types.py p1 p2 ...   (or 'range N')
"""
import sys
from math import gcd, isqrt
from sympy import isprime, divisors, primerange

def es_solutions(p):
    sols = []
    # x <= y <= z, 4/p = 1/x+1/y+1/z  => p/4 < x <= 3p/4
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        # 1/y + 1/z = r = (4x - p)/(px)
        num, den = 4 * x - p, p * x
        g = gcd(num, den); num //= g; den //= g
        # y <= z, y >= x; y <= 2*den/num
        for y in range(max(x, den // num + 1), 2 * den // num + 1):
            # 1/z = num/den - 1/y = (num*y - den)/(den*y)
            zn, zd = num * y - den, den * y
            if zn <= 0: continue
            if zd % zn == 0:
                z = zd // zn
                if z >= y: sols.append((x, y, z))
    return sols

def type2_solutions(p, bound=None):
    """all (a,b,c,d) with 4abcd = a+b+pc, returned with (x,y,z)."""
    out = set()
    # c*(4abd - p) = a + b  => 4abd > p; and a+b = c(4abd-p) >= 4abd - p
    # enumerate d, a, b with 4abd - p | a + b  ... brute force bounded: a,b <= p
    # use: for each (a,d): b(4ad c - 1) = a + pc  -> enumerate c as well; c <= a+b
    # simpler: enumerate x<=... from ES then test. Instead brute: a*b*d <= (a+b+pc)/(4c) ; small search
    for d in range(1, p):
        for a in range(1, p):
            if 4 * a * d > 3 * p + 3: break  # heuristic bound: 4abcd = a+b+pc <= ... (b>=1,c>=1 -> 4ad <= a+b+pc, loose)
            for c in range(1, p):
                q = 4 * a * c * d - 1
                if q > a + p * c: break
                if (a + p * c) % q == 0:
                    b = (a + p * c) // q
                    out.add((a, b, c, d, tuple(sorted((b * c * d * p, a * c * d * p, a * b * d)))))
    return out

def classify(p):
    sols = es_solutions(p)
    by = {1: [], 2: [], 3: []}
    for s in sols:
        k = sum(1 for v in s if v % p == 0)
        by[k].append(s)
    return sols, by

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "range":
        ps = list(primerange(5, int(args[1])))
    else:
        ps = [int(a) for a in args]
    for p in ps:
        sols, by = classify(p)
        t2 = type2_solutions(p)
        t2_xyz = {t[4] for t in t2}
        star_xyz = {t[4] for t in t2 if t[2] == 1}
        type2_set = set(by[2])
        ok = (t2_xyz == type2_set)
        print(f"p={p} #sol={len(sols)} typeI={len(by[1])} typeII={len(by[2])} (star:{len(star_xyz)}, c>1:{len(type2_set - star_xyz)}) three={len(by[3])} param_match={ok}")
        if not ok:
            print("   MISMATCH", sorted(t2_xyz ^ type2_set)[:5])
        if len(args) <= 3 and args[0] != "range":
            print("   typeI  :", by[1][:6])
            print("   typeII :", by[2][:6])
            print("   t2 params (a,b,c,d):", sorted(t[:4] for t in t2)[:8])
