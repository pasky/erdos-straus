#!/usr/bin/env python3
"""Aggregate the delta*(T) estimates (data/pointwise_size/wtail/split*.json): batch-weighted
means, the independence exponent I(T), the census comparison, and the predicted maxima."""
import json, glob
from math import log, exp
D = 'data/pointwise_size/wtail/'
est = {}
for f in sorted(glob.glob(D + 'split*.json')):
    d = json.load(open(f))
    w = d['batches']
    for t, v in d['delta'].items():
        est.setdefault(int(t), []).append((v, w))
delta = {t: sum(v * w for v, w in L) / sum(w for _, w in L) for t, L in est.items()}
I = {int(t): v for t, v in json.load(open(D + 'indep_1M.json')).items()}
cen = json.load(open(D + 'census_1e9.json'))
print('T | delta*(T) | -log delta* | I(T) | ratio | census p<1e9 (count W>T) | predicted delta*.pi_h')
for t in sorted(delta):
    if delta[t] <= 0:
        continue
    c = cen['counts_W_gt_T'].get(str(t))
    print(t, '%.3g' % delta[t], round(-log(delta[t]), 2), I[t], round(-log(delta[t]) / I[t], 3),
          c, round(delta[t] * cen['hard_primes'], 1))
# predicted max W over hard p <= N:  delta*(T) pi_h(N) = 1, interpolating -log delta* linearly in log T;
# beyond the measured range use -log delta* = r * I(T) with r = mean ratio over 4095..16383.
r = sum(-log(delta[t]) / I[t] for t in (4095, 8191, 16383)) / 3
def target(t):
    return -log(delta[t]) if t <= 16383 else r * I[t]
ts = sorted(I)
print('ratio r =', round(r, 3))
for e in (8, 9, 12, 18, 30, 50):
    N = 10 ** e
    goal = log(N / (8 * log(N)))
    pts = [(t, target(t)) for t in ts]
    T = None
    for (t1, y1), (t2, y2) in zip(pts, pts[1:]):
        if y1 <= goal <= y2:
            T = exp(log(t1) + (goal - y1) / (y2 - y1) * (log(t2) - log(t1)))
    if T is None:   # extrapolate I by its last increment growth
        t, y, inc = ts[-1], target(ts[-1]), r * (I[ts[-1]] - I[ts[-2]])
        g = r * ((I[ts[-1]] - I[ts[-2]]) - (I[ts[-2]] - I[ts[-3]]))
        while y < goal:
            inc += g; t = 2 * t + 1; y += inc
        T = t
    print(f'N=1e{e}: ln pi_h = {goal:.2f}, predicted max W ~ {T:.3g}, = (log N)^{log(T)/log(log(N)):.2f}')
