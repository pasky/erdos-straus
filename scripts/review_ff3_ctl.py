"""review_ff3_ctl.py (R173): re-run of the O173 control (§3) with the R173 search code, on the SAME points as
scripts/ff3_ctl.sh (python random.seed(s + s0), digits [1,1] + [0]*(m-2) + 70 random digits).
Counts distinct families (l, j, gamma, L', g') with 1 <= deg L' <= LMAX and j <= 4l - 2, as ff3_ctl.sh does.
usage: review_ff3_ctl.py m npts LMAX s0"""
import random
import sys
import review_ff3_search as S

m, n, lm, s0 = map(int, sys.argv[1:5])
hits = []
for s in range(1, n + 1):
    random.seed(s + s0)
    d = [1, 1] + [0] * (m - 2) + [random.randrange(3) for _ in range(70)]
    fams = S.search(3, 2, 1, lm, -1, d, log=lambda x: None)
    h = len({(f[0], f[2], f[3], f[1], f[4]) for f in fams})
    hits.append(h)
    print(s, h, flush=True)
print(f"m={m} LMAX={lm}: points with >=1 family {sum(1 for h in hits if h)}/{n}, mean {sum(hits)/n:.3f}")
