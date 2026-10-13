"""bsA_profile: QNR fraction by HJ length r for primes p = 1 (8); exact identity r(p/A)+r(p/(p-A)) = sum of all
regular partial quotients. Usage: PYTHONPATH=scripts uv run python scripts/bsA_profile.py PMIN PMAX"""
import sys
from collections import defaultdict
from sympy import primerange, jacobi_symbol
from bsA_hjlen import hj_len
P0, P1 = int(sys.argv[1]), int(sys.argv[2])
tot = defaultdict(int); neg = defaultdict(int); np_ = 0
for p in primerange(P0, P1):
    if p % 8 != 1: continue
    np_ += 1
    for A in range(1, p):
        r = hj_len(p, A)
        if r <= 9:
            tot[r] += 1; neg[r] += jacobi_symbol(A, p) == -1
print("primes", np_)
for r in sorted(tot):
    print("r=%d  mean#words %.1f  QNR fraction %.3f" % (r, tot[r] / np_, neg[r] / tot[r]))
