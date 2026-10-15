# R224: aggregate /tmp/r224_census.txt (from review_r224_census.c): N-/N by lnr bucket and by archimedean distance to squares.
import sys, math, statistics as st
from collections import defaultdict
rows = []
for l in open(sys.argv[1]):
    p, N, Nm, q = map(int, l.split())
    if p > 5: rows.append((p, N, Nm, q))
print("primes", len(rows), "sign-dominance violations (N- < N+):", sum(2 * Nm < N for p, N, Nm, q in rows))
def dsq(p):
    m = math.isqrt(p); return min(p - m * m, (m + 1) ** 2 - p)
g = defaultdict(list)
for p, N, Nm, q in rows: g[(p % 8, min(q, 23))].append(Nm / N)
for k in sorted(g): print("p%8,lnr", k, len(g[k]), "%.3f" % st.mean(g[k]))
# value bins of dsq/sqrt(p) (author's convention) and true quantile deciles
x = [(dsq(p) / math.sqrt(p), Nm / N, p, q) for p, N, Nm, q in rows]
h = defaultdict(list)
for d, r, p, q in x: h[min(int(10 * d), 10)].append(r)
print("value bins:", [(k, len(h[k]), round(st.mean(h[k]), 4)) for k in sorted(h)])
xs = sorted(x); n = len(xs)
print("quantile deciles:", [round(st.mean(r for _, r, _, _ in xs[i * n // 10:(i + 1) * n // 10]), 4) for i in range(10)])
# within p = 1 (8), q = 3 (largest homogeneous bucket): quantile deciles; and p-size deciles (confounder check)
sub = sorted((d, r) for d, r, p, q in x if p % 8 == 1 and q == 3); m = len(sub)
print("p=1(8),q=3 quantile deciles:", [round(st.mean(r for _, r in sub[i * m // 10:(i + 1) * m // 10]), 4) for i in range(10)])
for lo, hi in [(0, 0.01), (0, 0.05), (0.05, 2)]:
    s = [r for d, r, p, q in x if lo <= d < hi and p > 10 ** 5]
    print("p>1e5, dsq/sqrt in [%g,%g):" % (lo, hi), len(s), round(st.mean(s), 4))
bys = sorted((p, r) for d, r, p, q in x)
print("by p-size deciles:", [round(st.mean(r for _, r in bys[i * n // 10:(i + 1) * n // 10]), 4) for i in range(10)])
