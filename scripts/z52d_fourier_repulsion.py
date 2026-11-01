"""Deuring–Heilbronn / Linnik-(c) analogue test (Z2940, Z2941): does exceptionality of the shared real character χ_p on the
window integers (x = fraction of unforced windows killed by χ_{-e}, i.e. N_e composed only of p-QR primes) make the
forced windows (where χ_p is silent, Cor 4) EASIER?  y = fraction of forced windows that succeed.  Controls: mean log M of
forced windows (box size), and qr = fraction of primes 11..97 that are p-QR.  Prints Pearson r and the partial
correlation of (x, y) given the controls, with a Fisher-z 95 % interval."""
import sys, json, gzip, math
import numpy as np
from collections import defaultdict
from z52d_fourier_lib import jacobi, small_primes
op = gzip.open if sys.argv[1].endswith('.gz') else open
D = defaultdict(lambda: defaultdict(float))
for l in op(sys.argv[1], 'rt'):
    r = json.loads(l); d = D[r['p']]
    if r['forced']:
        d['F'] += 1; d['Fok'] += r['type'] == 'ok'; d['FlogM'] += math.log(r['M'])
    else:
        d['U'] += 1; d['Ujac'] += r['type'] == 'sub' and r['kill_jac']; d['Uok'] += r['type'] == 'ok'
ls = [l for l in small_primes(100) if 11 <= l <= 97]
rows = []
for p, d in D.items():
    qr = sum(1 for l in ls if jacobi(p, l) == 1) / len(ls)
    rows.append([d['Ujac'] / d['U'], d['Fok'] / d['F'], d['FlogM'] / d['F'], qr, d['Uok'] / d['U']])
A = np.array(rows); n = len(A)
x, y = A[:, 0], A[:, 1]
def pc(x, y, Z):
    Z = np.column_stack([np.ones(len(x)), Z])
    rx = x - Z @ np.linalg.lstsq(Z, x, rcond=None)[0]; ry = y - Z @ np.linalg.lstsq(Z, y, rcond=None)[0]
    return np.corrcoef(rx, ry)[0, 1]
def ci(r, n, k):
    z = math.atanh(r); s = 1 / math.sqrt(n - 3 - k)
    return math.tanh(z - 1.96 * s), math.tanh(z + 1.96 * s)
r0 = np.corrcoef(x, y)[0, 1]; r1 = pc(x, y, A[:, 2:4])
print(f'n={n} primes; mean x={x.mean():.3f} mean y={y.mean():.3f}')
print(f'corr(x,y) = {r0:+.3f}  95% CI {ci(r0, n, 0)[0]:+.3f}..{ci(r0, n, 0)[1]:+.3f}')
print(f'partial corr(x,y | logM_forced, qr) = {r1:+.3f}  95% CI {ci(r1, n, 2)[0]:+.3f}..{ci(r1, n, 2)[1]:+.3f}')
r2 = pc(x, A[:, 4], A[:, 2:4]); print(f'(sanity) partial corr(x, unforced success rate | same) = {r2:+.3f}')
q = np.quantile(x, [0.1, 0.9])
print(f'forced success rate: top-decile x {y[x >= q[1]].mean():.4f}  bottom-decile x {y[x <= q[0]].mean():.4f}')
