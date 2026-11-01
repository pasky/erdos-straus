# z53_thin15_iid3.py — search of the one-constant Type II pattern II-d at root degree D = 3 for n = 15Y^3 + 1
# (Z53_THIN15.md §3.4): a = Y - alpha (scaled), d constant, f = kappa (Y - zeta) (the gap), g = 4acd - 1 quadratic,
#   f g = n + C, C = 4 a^2 d,  d = -n(zeta)/(4 (zeta-alpha)^2),  kappa = -n(alpha)/(alpha - zeta),
#   x = (n + f)/4,  y = n (1 + g)/4,  z = n x (1 + g)/C      (b = (f+n)/(4ad), c = (g+1)/(4ad) are polynomials).
# Signs (Lemma 5): zeta < alpha < -15^(-1/3).  Validity near mu = 0 <=> x(1), y(1), z(1) in Z[1/2] and x(0), y(0), z(0)
# in Z_(2) (paper Lemma special).  Enumerates alpha, zeta = num/den, den <= QMAX, value in [-RMAX, -15^(-1/3)).
# EVIDENCE only (bounded heights).  Usage: z53_thin15_iid3.py QMAX RMAX
import sys
from fractions import Fraction as Fr
from math import gcd
QMAX, RMAX = int(sys.argv[1]), int(sys.argv[2])
rho = -(1 / 15) ** (1 / 3)
def n(Y): return 15 * Y ** 3 + 1
def odd(m):
    while m % 2 == 0: m //= 2
    return m
def half(q): return odd(q.denominator) == 1
def loc2(q): return q.denominator % 2 == 1
vals = sorted({Fr(p, q) for q in range(1, QMAX + 1) for p in range(-RMAX * q, 0) if gcd(p, q) == 1 and p / q < rho})
print('values per parameter:', len(vals), flush=True)
tested = 0; hits = []; part1 = 0
for i, al in enumerate(vals):
    nal = n(al); A1 = (1 - al) ** 2; A0 = al * al
    for ze in vals[:i]:                      # zeta < alpha
        tested += 1
        kap = -nal / (al - ze)
        f1 = kap * (1 - ze)
        x1 = (16 + f1) / 4
        if not half(x1): continue
        d4 = -n(ze) / (ze - al) ** 2         # = 4d
        C1 = d4 * A1
        g1 = (16 + C1) / f1
        y1 = 4 * (1 + g1)
        if not half(y1): continue
        z1 = 16 * x1 * (1 + g1) / C1
        if not half(z1): continue
        part1 += 1
        f0 = -kap * ze; C0 = d4 * A0
        x0 = (1 + f0) / 4; g0 = (1 + C0) / f0
        y0 = (1 + g0) / 4; z0 = x0 * (1 + g0) / C0
        if loc2(x0) and loc2(y0) and loc2(z0):
            hits.append((al, ze)); print('HIT alpha=%s zeta=%s' % (al, ze), flush=True)
print('II-d D=3: QMAX=%d RMAX=%d: %d (alpha, zeta) pairs, %d pass Y=1, %d pass Y=1 and Y=0' % (QMAX, RMAX, tested, part1, len(hits)))
