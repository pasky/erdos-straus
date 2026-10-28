#!/usr/bin/env python3
"""Instances of the Dickson family of Proposition 3.3 (shadow primes with HC(p) > X).

For X >= 4 and p = 1 (mod 8) put C_X = {x in [4, X] : x = 0 (4) or x = 7 (8)}, Q = lcm(24, x(x+1) : x in C_X),
and the linear forms in s:
    p(s) = 1 + Q s,   F_x(s) = 1 + Q s/(x+1)  (p + x = (x+1) F_x),   G_x(s) = 1 + x Q s/(x+1)  (x p + 1 = (x+1) G_x).
If all are prime then (Prop 3.3) no word of p has a coordinate in C_X, i.e. HC(p) > X.
This script searches s and prints the first instances; the claim HC(p) > X is then re-checked by brute force.
"""
import sys
from math import lcm, isqrt
from sympy import isprime, divisors

def forms(X):
    CX = [x for x in range(4, X + 1) if x % 4 == 0 or x % 8 == 7]
    Q = lcm(24, *[x * (x + 1) for x in CX])
    fs = [("p", Q, 1)]
    for x in CX:
        fs.append((f"F_{x}", Q // (x + 1), 1)); fs.append((f"G_{x}", x * Q // (x + 1), 1))
    return CX, Q, fs

def HC(p):
    """least coordinate in C_p over all words of p (brute force)."""
    best = None
    u = 1
    while (u - 1) ** 2 <= p + 1:
        for v in divisors(p + u):
            if (v + p) % u == 0 and (p + u + v) % (u * v) == 0:
                t = (p + u + v) // (u * v)
                for x in (t, u, v):
                    if (x % 4 == 0 or (x + p) % 8 == 0) and (best is None or x < best): best = x
        u += 1
    return best

def main(X, smax):
    CX, Q, fs = forms(X)
    print(f"X={X}: C_X={CX}, Q={Q}, forms: " + ", ".join(f"{nm}=1+{c}s" for nm, c, _ in fs))
    found = 0
    for s in range(1, smax + 1):
        if all(isprime(1 + c * s) for _, c, _ in fs):
            p = 1 + Q * s
            h = HC(p)
            print(f"  s={s}: p={p} (p mod 8 = {p % 8}), HC(p) = {h}  {'OK (> X)' if h > X else 'FAIL'}")
            found += 1
            if found >= 3: break
    if not found: print("  no instance found below smax")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8, int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000)
