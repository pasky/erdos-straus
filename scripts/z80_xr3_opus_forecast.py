"""Opus R3 short no-fit check of the EXTREME.md §12 model (own reimplementation of the
stated rules from the note text; coefficients read from data/z80/model/coeff.csv,
which were independently re-derived in coef_indep.txt).
(1) model vs empirical survival P(g>=4j+3) on hard primes in (1e7,2e7];
(2) model expected number of *zeros* (no solution) on [1009, X] for several X;
(3) model expected count of g>=111 through 5e12 (observed: 9)."""
import csv, math
from math import sqrt, exp, log, pi, ceil
rows = list(csv.reader(open('data/z80/model/coeff.csv')))[1:]
S = {}; B = {}
for w in rows:
    v = [float(x) for x in w[1:7]]
    if ':' in w[0]: B[int(w[0].split(':')[1])] = v
    else: S[int(w[0])] = v
def surv(t, r, J):
    """P(first J windows all miss) and P(zero) at log-height t, residue index r."""
    j0 = ceil(t); E = [1.0]
    for j in range(1, j0 + 1):           # 1-based window index, k=4j-1
        k = 4 * j - 1; s = min(1, S[k][r] / sqrt(t))
        if j % 2 == 1: E.append(E[-1] * s)
        else:
            s0 = min(1, S[k - 4][r] / sqrt(t))
            E.append(E[-2] * min(s0, s, B[k][r] / t))
    z = exp(-3 * t * t / (4 * pi * pi)); n = int((2 * exp(t) + 1) // 4) - j0
    out = []
    for j in range(J + 1):
        out.append(E[j] if j <= j0 else E[j0] * (z + (1 - z) * max(0, 1 - (j - j0) / n)))
    return out, E[j0] * z
# (1)
emp = {3: 8311, 7: 4557, 11: 3896, 15: 844, 19: 694, 23: 378, 27: 56, 31: 100, 35: 16, 39: 14, 43: 2, 47: 5, 55: 2, 59: 3}
N = sum(emp.values())
num = [0.0] * 16; den = 0.0; zs = 0.0
for i in range(2000):
    x = 1e7 * (1 + (i + .5) / 2000); t = log(x); w = 1 / t; den += w
    for r in range(6):
        e, z = surv(t, r, 15)
        for j in range(16): num[j] += w * e[j] / 6
print('j  g>=  model  empirical(18878 hard primes in (1e7,2e7])')
for j in range(1, 16):
    g = 4 * j + 3; ec = sum(c for gg, c in emp.items() if gg >= g)
    print(j, g, f'{num[j]/den:.4g}', f'{ec/N:.4g}')
# (2),(3)
cum = 0.0; c111 = 0.0; t = log(1009); dt = 0.002; marks = [log(x) for x in (1e6, 1e9, 5e12, 1e17, 1e18)]
TEND = marks[-1]
while t < TEND:
    m = t + dt / 2; sc = exp(m) * dt / (192 * m)
    for r in range(6):
        e, z = surv(m, r, 27); cum += sc * z
        if m < log(5e12): c111 += sc * e[27]
    t += dt
    while marks and t >= marks[0]:
        print(f'model expected zeros on [1009,{exp(marks[0]):.3g}] = {cum:.4g}'); marks.pop(0)
print(f'model expected #hard primes <=5e12 with g>=111: {c111:.4g} (observed 9)')
