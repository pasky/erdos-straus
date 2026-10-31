"""U01 Z1735/Z3014/Z3046: greedy-chain statistics. For prime p<=PMAX and each first term x in [ceil(p/4), floor(3p/4)],
indicator s(x)=1 iff (4x-p)/(px) is a sum of two unit fractions (two-term completion succeeds)."""
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto
from z52b_p1_U01_four import two_term_all
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
rates = []; corr = []; byp = {}
for p in primes_upto(PMAX):
    if p < 5: continue
    xs = range(-(-p//4), (3*p)//4 + 1)
    s = []
    for x in xs:
        A = 4*x - p
        if A <= 0: s.append(0); continue
        B = p*x; g = math.gcd(A, B)
        s.append(1 if two_term_all(A//g, B//g) else 0)
    s = np.array(s, float)
    byp[p] = (len(s), s.mean())
    rates.append(s.mean())
    if s.std() > 0 and len(s) > 2: corr.append(np.corrcoef(s[:-1], s[1:])[0, 1])
rates = np.array(rates)
print(f"Z1735: primes ≤{PMAX} ({len(rates)}): fraction of first terms x∈[p/4,3p/4] giving a two-term completion: mean {rates.mean():.3f}, min {rates.min():.3f}, max {rates.max():.3f}")
print("  examples (p, #x, rate):", [(p, byp[p][0], round(byp[p][1], 3)) for p in list(byp)[-5:]])
print(f"Z3046: lag-1 autocorrelation of s(x) over x, median over primes: {np.nanmedian(corr):.3f}, mean {np.nanmean(corr):.3f} (nan slices dropped)")
hard = {2521, 1201, 2689, 4201, 401, 53}
print("  rate at small hard primes:", {p: round(byp[p][1], 3) for p in byp if p in hard})
