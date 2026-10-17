"""O258 checks for SYNTHESIS_SPARKS8 §1: mutual shift pairs MP(n) (brute force) versus
(a) Prop 1.4's (x, s) parametrisation, (b) Prop 1.2/1.3 line criteria against s8_check_b1 brute force.
Usage: PYTHONPATH=scripts uv run python scripts/s8_mp_check.py [N]
"""
import sys
from math import gcd
from s8_check_b1 import b1_solutions, c1_solutions

def mp(n):
    out = set()
    for x in range(1, n + 2):
        # y | n + x, y >= 1
        t = n + x
        for y in range(1, int(t ** 0.5) + 1):
            if t % y == 0:
                for yy in {y, t // y}:
                    if (n + yy) % x == 0 and (n + x + yy) % (x * yy) == 0:
                        out.add((x, yy))
    return out

def mp_param(p):
    out = set()
    for s in range(1, p + 2):
        # x | s + 1 and s | p + x, x < y = (p + x)/s
        t = s + 1
        for x in range(1, t + 1):
            if t % x == 0 and (p + x) % s == 0:
                y = (p + x) // s
                if x < y:
                    out.add((x, y))
    return out

def isp(n):
    return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    bad = 0; cnt = 0
    tests = [p for p in range(5, N) if isp(p) and p % 4 == 1] + [9, 25, 49, 81, 121, 105]
    for n in tests:
        M = mp(n)
        if isp(n):
            if {(x, y) for (x, y) in M if x < y} != mp_param(n):
                bad += 1; print("param mismatch", n)
        b1 = any(x % 4 == 0 or y % 4 == 0 for (x, y) in M)
        c1 = any(((n + x + y) // (x * y)) % 4 == 0 for (x, y) in M)
        if b1 != bool(b1_solutions(n)) or c1 != bool(c1_solutions(n)):
            bad += 1; print("line mismatch", n, b1, c1)
        cnt += 1
    print(f"tested {cnt} n (primes p=1(4) < {N} + squares + 105); mismatches: {bad}")
