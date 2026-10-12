"""O144 (a): check the Farey / Ford-circle dictionary for Type I.

Lemma A.1 (memo BRAINSTORM/farey_ford_cf.md): Type I solutions of a prime p (ET coordinates,
4abd - pe = 1, a + b = ce, a <= b, gcd(a,b,c) = 1) <-> triples (N, a, e) with N = 4ad, a | N/4,
e | aN + 1 and N | pe + 1 (then b = (pe+1)/N, c = (a+b)/e).  The Farey form: e/N < b/p are Farey
neighbours (Nb - pe = 1); when N < p and b < p they are the left parent of b/p in F_p, the right
parent being (b-e)/(p-N).
Checks the count against spec_typecount's FI array and reports how many primes have a solution in
the "F_{p-1}" range N < p, b < p, and with a = 1.
Usage: PYTHONPATH=scripts uv run python scripts/bs_farey_dict.py PREFIX PMAX
"""
import sys, math
import numpy as np
from sympy import divisors, primerange

pref, PMAX = sys.argv[1], int(sys.argv[2])
FI = np.fromfile(pref + ".FI.bin", dtype=np.uint32)

def type_i(p):
    sols = []
    for N in range(4, 2 * p + 3, 4):
        if N % p == 0:
            continue
        M = N // 4
        for a in divisors(M):
            for e in divisors(a * N + 1):
                if (p * e + 1) % N:
                    continue
                b = (p * e + 1) // N
                if a > b or (a + b) % e:
                    continue
                c = (a + b) // e
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                sols.append((N, a, b, c, e))
    return sols

bad = 0; nprimes = 0; no_farey = []; no_a1 = []; frac = []
for p in primerange(5, PMAX + 1):
    s = type_i(p); nprimes += 1
    if len(s) != FI[p]:
        bad += 1; print("MISMATCH", p, len(s), FI[p])
    far = [t for t in s if t[0] < p and t[2] < p]
    frac.append(len(far) / max(1, len(s)))
    if not far:
        no_farey.append(p)
    if not [t for t in s if t[1] == 1]:
        no_a1.append(p)
print(f"primes 5..{PMAX}: {nprimes}, count mismatches vs spec_typecount: {bad}")
print(f"primes with no Type I solution in the F_(p-1) range (N<p, b<p): {no_farey[:20]} (total {len(no_farey)})")
print(f"mean fraction of Type I solutions in F_(p-1) range: {np.mean(frac):.3f}")
print(f"primes with no a=1 Type I solution: {len(no_a1)} (first {no_a1[:10]})")
