"""U01 Z0973: m/p = 2/x + 1/z (two equal denominators). For x: z = p x/(m x - 2p) integer, z >= x  => x in (2p/m, 3p/m]."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto
def iso_solutions(m, p):
    sols = []
    lo = 2*p//m + 1
    for x in range(lo, 3*p//m + 1):
        d = m*x - 2*p
        if d <= 0: continue
        if (p*x) % d == 0:
            z = p*x//d
            if z >= x: sols.append((x, z))
    return sols
if __name__ == "__main__":
    P = [p for p in primes_upto(20000) if p > 3]
    for m in (4, 5, 7, 8):
        has = [p for p in P if iso_solutions(m, p)]
        print(f"m={m}: primes p<=2e4 with an isosceles (x=y) solution: {len(has)} of {len(P)}; first 15 fail-free ones:",
              [p for p in P if p not in set(has)][:0], "examples:", [(p, iso_solutions(m, p)[:2]) for p in has[:4]])
        print("   primes in window with NO isosceles solution, largest 8:", [p for p in P if p not in set(has)][-8:])
