# z54 EXACTSUM: summarise W(a,q) sizes (output of z54_exactsum_wsum.c). Usage: python ... wsum.tsv
# Groups rows by scale (1e12 primes, 1e14 primes, squares) and q-range; reports medians over (n,q) of
#   max_a|W|/Wtriv (cancellation vs trivial bound) and rms_a|W| / sqrt(sum u^-2) (vs random phases).
import sys, math
import numpy as np
rows = [l.split() for l in open(sys.argv[1])]
def grp(n):
    r = math.isqrt(n)
    if r * r == n: return 'SQUARE'
    return 'P1e%d' % int(math.log10(n))
data = {}
for r in rows:
    n, q, nu, nt = int(r[0]), int(r[1]), int(r[2]), int(r[3]); triv, rms2, mx, rms, P = map(float, r[4:9])
    if q == 1 or nt == 0: continue
    qb = '3-9' if q < 10 else '11-29' if q < 30 else '31-99'
    data.setdefault((grp(n), qb), []).append((mx / triv, rms / rms2, nt, abs(P) / triv))
print('group qrange #(n,q) median#terms median max|W|/triv median rms|W|/rms2 median |P_q|/triv')
for k in sorted(data):
    a = np.array(data[k])
    print(k[0], k[1], len(a), int(np.median(a[:, 2])), '%.3f' % np.median(a[:, 0]), '%.3f' % np.median(a[:, 1]), '%.3f' % np.median(a[:, 3]))
