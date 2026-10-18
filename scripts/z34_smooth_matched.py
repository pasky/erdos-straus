"""O264 (review repair): size-matched comparison of the smooth-(p-1) cell with its size neighbours.
Percentile u = mid-rank among the 1001 nearest primes (as z34_ranks). Only p >= P0 (window spans < factor ~1.5).
For each Y-smooth prime p (p-1 Y-smooth), controls = the non-smooth primes in the same 1001-window.
usage: z34_smooth_matched.py scores.txt P0"""
import sys
import numpy as np
A = np.loadtxt(sys.argv[1], dtype=np.int64); P0 = int(sys.argv[2])
p = A[:, 0]; n = len(p); W = 1001; h = W // 2
cols = {'N1': -A[:, 1], 'fII': -A[:, 2], 'm0': A[:, 3], 'S': -A[:, 5], 'e0': np.where(A[:, 6] == 0, 10**9, A[:, 6])}
def win(i):
    lo = max(0, min(i - h, n - W)); return lo, lo + W
U = {}
for k, x in cols.items():
    u = np.empty(n)
    for i in range(n):
        lo, hi = win(i); w = x[lo:hi]
        u[i] = ((w < x[i]).sum() + 0.5 * ((w == x[i]).sum() - 1)) / (W - 1)
    U[k] = u
def smooth(m, Y):
    for l in [q for q in (2, 3, 5, 7, 11, 13) if q <= Y]:
        while m % l == 0: m //= l
    return m == 1
T = 0.95
for Y in (11, 13):
    sm = np.array([smooth(int(q) - 1, Y) for q in p])
    idx = np.where(sm & (p >= P0))[0]
    print(f'\nY = {Y}: {len(idx)} smooth primes in [{P0}, {p[-1]}]')
    for k in cols:
        ctrl = np.mean([U[k][lo:hi][~sm[lo:hi]].mean() for lo, hi in map(win, idx)])
        print(f'  mean u {k}: smooth {U[k][idx].mean():.3f}  matched controls {ctrl:.3f}')
    for a, b in (('N1', 'S'), ('N1', 'm0'), ('fII', 'S'), ('fII', 'm0'), ('N1', 'e0'), ('m0', 'e0')):
        J = (U[a] >= T) & (U[b] >= T)
        js = J[idx].mean()
        jc = np.mean([J[lo:hi][~sm[lo:hi]].mean() for lo, hi in map(win, idx)])
        prod = (U[a][idx] >= T).mean() * (U[b][idx] >= T).mean()
        print(f'  joint top-5% {a}&{b}: smooth {js:.3f}  matched controls {jc:.4f}  ratio {js / jc if jc else float("inf"):.1f}'
              f'  (product of smooth marginals {prod:.3f})')
