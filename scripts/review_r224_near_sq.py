# R224: is there an archimedean (distance-to-squares) effect on N-/N after controlling for (p mod 8, lnr) and p-size?
import sys, math, statistics as st
from collections import defaultdict
rows = [tuple(map(int, l.split())) for l in open(sys.argv[1])]
rows = [r for r in rows if r[0] > 10 ** 5]
def dsq(p):
    m = math.isqrt(p); return min(p - m * m, (m + 1) ** 2 - p)
import os
FULL = os.environ.get('FULL') == '1'
def lg(a, p): return 1 if pow(a, (p - 1) // 2, p) == 1 else -1
def cell(p, q):   # stratum: p mod 8, lnr bucket, p-size bin of width 1e5 (FULL=1: + signs (r/p), r = 3..13, and p mod 16)
    c = (p % 8, min(q, 17), p * 10 // 10 ** 6)
    return c + ((p % 16,) + tuple(lg(r, p) for r in (3, 5, 7, 11, 13)) if FULL else ())
g = defaultdict(list)
for p, N, Nm, q in rows: g[cell(p, q)].append(Nm / N)
mu = {k: st.mean(v) for k, v in g.items()}
res = [(p, Nm / N - mu[cell(p, q)], q) for p, N, Nm, q in rows]
sd = st.pstdev(r for _, r, _ in res)
def rep(name, f):
    s = [r for p, r, q in res if f(p)]
    print("%-28s n=%5d mean residual %+.4f  z=%+.2f" % (name, len(s), st.mean(s), st.mean(s) / (sd / math.sqrt(len(s)))))
rep("dsq <= 4", lambda p: dsq(p) <= 4)
rep("dsq <= 20", lambda p: dsq(p) <= 20)
rep("dsq <= 100", lambda p: dsq(p) <= 100)
rep("dsq/sqrt(p) < 0.01", lambda p: dsq(p) / math.sqrt(p) < 0.01)
rep("dsq/sqrt(p) < 0.05", lambda p: dsq(p) / math.sqrt(p) < 0.05)
rep("dsq/sqrt(p) > 0.5", lambda p: dsq(p) / math.sqrt(p) > 0.5)
for k in (1, 4, 9, 16, 25, 36, 49, 64, 81, 100):
    rep("p - m^2 = %d" % k, lambda p, k=k: p - math.isqrt(p) ** 2 == k)
for k in (3, 4, 7, 8, 11, 12, 15, 16):   # (m+1)^2 - p = k
    rep("(m+1)^2 - p = %d" % k, lambda p, k=k: (math.isqrt(p) + 1) ** 2 - p == k)
