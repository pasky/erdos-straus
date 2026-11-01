"""z52d avenue Q03 (Z0900): re-run of the Pass-1 practical(p-1) test with the 'hardest' ranking fixed.
Pass 1 (z52b_p1_U01_practical.py) sorted by -U4, i.e. took the 30 LARGEST counts, not the hardest.
Here: hardest = lowest residual of log(U4+1) after a quadratic fit in log p (p <= 3e4)."""
import sys, math, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import *
from z52b_p1_U01_practical import practical  # noqa (re-runs its prints too)
import numpy as np
f4 = load_counts(os.path.join(RAW, "f4_all_30000.txt"))
pr = [p for p in primes_upto(30000) if p > 5 and p in f4]
U4 = {p: f4[p][0] for p in pr}
X = np.array([math.log(p) for p in pr]); A = np.array([math.log(U4[p]+1) for p in pr])
res = dict(zip(pr, A - np.polyval(np.polyfit(X, A, 2), X)))
base = np.mean([practical(p-1) for p in pr])
for k in (30, 100):
    hard = sorted(pr, key=lambda p: res[p])[:k]
    print(f"hardest {k} by residual: practical(p-1) = {sum(practical(p-1) for p in hard)}/{k} (base rate {base:.3f}); first: {hard[:12]}")
easy = sorted(pr, key=lambda p: -res[p])[:30]
print("easiest 30 by residual: practical", sum(practical(p-1) for p in easy))
