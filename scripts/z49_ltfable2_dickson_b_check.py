#!/usr/bin/env python3
"""Verify the conclusion of Proposition 3.3(b) (X = 4, k = 1) at the instances found by z49_ltfable2_dickson_b.c:
every word with a coordinate <= 4 is free and monochromatic, and there are >= 2^{k+2} = 8 words (t, 1, v).
Words with a coordinate <= 4 are enumerated exactly: endpoint u <= 4 (divisors of p + u) or level t <= 4 (divisors of
t p + 1 in the class -1 mod t); the symmetric copies are included.  Exit 1 on failure."""
import sys
from sympy import divisors, isprime, factorint

def inC(x, p): return x % 4 == 0 or (x + p) % 8 == 0

def main(ps):
    for p in ps:
        assert isprime(p) and p % 24 == 1
        words = set()
        for u in (1, 2, 3, 4):
            for v in divisors(p + u):
                if (v + p) % u == 0 and (p + u + v) % (u * v) == 0:
                    t = (p + u + v) // (u * v); words.add((t, u, v)); words.add((t, v, u))
        for t in (1, 2, 3, 4):
            N = t * p + 1
            for d in divisors(N):
                if (d + 1) % t == 0 and (N // d + 1) % t == 0:
                    u, v = (d + 1) // t, (N // d + 1) // t
                    if u >= 1 and v >= 1 and t * u * v - u - v == p: words.add((t, u, v))
        win = sorted(words)
        free = all(t <= 2 or min(u, v) <= 2 for t, u, v in win)
        mono = all(not (inC(t, p) or inC(u, p) or inC(v, p)) for t, u, v in win)
        nu1 = sum(1 for t, u, v in win if u == 1)
        print(f"p={p}: p+1 = {factorint(p+1)}; words with a coordinate <= 4: {len(win)}, all free: {free}, "
              f"all monochromatic: {mono}, words (t,1,v): {nu1} (>= 8: {nu1 >= 8})")
        if not (free and mono and nu1 >= 8): print("FAILED"); sys.exit(1)
    print("Prop 3.3(b) instances verified")

if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or [36683351787601, 181305326084401, 345153635946001])
