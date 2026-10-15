"""O221: coverage of m by escaping polynomial families (file from ns_polyfam.py) plus Mordell's 840 classes.
Usage: ns_coverage.py K FAMFILE MMAX"""
import sys, ast
from sympy import isprime
K = int(sys.argv[1]); fams = [ast.literal_eval(l) for l in open(sys.argv[2])]; MMAX = int(sys.argv[3])
MORD = {1, 121, 169, 289, 361, 529}
cls = [(L, set(g)) for _, _, L, g in fams if g]
hard = unc = 0; unl = []
for m in range(1, MMAX):
    n = m * m + K
    if n < 5 or n % 2 == 0 or not isprime(n) or n % 840 not in MORD: continue
    hard += 1
    if not any(m % L in g for L, g in cls):
        unc += 1; unl.append(m)
print("k", K, "families", len(cls), "Mordell-hard primes m^2+k (m <", MMAX, "):", hard, "uncovered by escaping families:", unc)
print("first uncovered m:", unl[:30])
