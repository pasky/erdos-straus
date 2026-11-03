"""For HIGH records: the smallest 'congruence modulus' among certificates at c = HC(p):
for a divisor d of N (N = p+c or cp+1) with d = -1 mod c, the certificate is the congruence condition
p = -c (mod d) [U] / cp = -1 (mod d) [T]  or, via the cofactor e = N/d, a condition mod c*e. Report min over certs of min(d, c*e)."""
import sys, re
from sympy import divisors
for fn in sys.argv[1:]:
    for line in open(fn):
        m = re.match(r'HIGH p=(\d+) HC=(\d+)', line)
        if not m: continue
        p, c = int(m[1]), int(m[2]); best = None; nc = 0
        for N in (p + c, c * p + 1):
            for d in divisors(N):
                if d % c == c - 1:
                    nc += 1; mod = min(d, c * (N // d))
                    best = mod if best is None else min(best, mod)
        print(p, c, "ncert", nc, "min modulus", best, "ratio log(mod)/log(p) = %.3f" % (__import__('math').log(best) / __import__('math').log(p)))
