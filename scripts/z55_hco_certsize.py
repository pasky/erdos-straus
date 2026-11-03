"""For HIGH records: the least congruence modulus mu among certificates at c = HC(p) (Z55_HCO.md P2.2):
for a divisor d of N (N = p+c [U] or cp+1 [T]) with d = -1 mod c and e = N/d:
  U-line: mu = min(d, c*e)   (d-fixed: p = -c mod d;  e-fixed: p = -c-e mod ce)
  T-line: mu = min(d, e)     (d-fixed: p = -c^{-1} mod d;  e-fixed: p = -(e+1)/c mod e)
Prints p, c, number of certificates, min mu, log mu/log p, and the minimising certificate (line, d, e, which side)."""
import sys, re, math
from sympy import divisors, isprime
for fn in sys.argv[1:]:
    for line in open(fn):
        m = re.match(r'HIGH p=(\d+) HC=(\d+)', line)
        if not m: continue
        p, c = int(m[1]), int(m[2]); best = None; nc = 0
        for ln, N in (('U', p + c), ('T', c * p + 1)):
            for d in divisors(N):
                if d % c == c - 1:
                    nc += 1; e = N // d
                    cands = [(d, 'd'), (c * e if ln == 'U' else e, 'e')]
                    for mu, side in cands:
                        if best is None or mu < best[0]: best = (mu, ln, d, e, side)
        mu, ln, d, e, side = best
        smallside = d if side == 'd' else e
        kind = 'prime' if isprime(smallside) else ('one' if smallside == 1 else 'composite')
        print(p, c, "ncert", nc, "mu", mu, "ratio %.3f" % (math.log(mu) / math.log(p)), "via", ln, side, "d", d, "e", e, "smallside", smallside, kind)
