#!/usr/bin/env python3
# z55 CROSSF: summarise hits(p) = R_F(p)/2 scans (data/z55/crossf/scan_1e*.txt, sample_1e*.txt): per scale N, mean, variance,
# zero fraction vs Poisson e^{-mean}, hits/log^2 p, and the Poisson-model tail integral E(x) (expected number of primes
# p = 1 (4), p > x, with hits = 0, if hits ~ Poisson(c log^2 p)).  Usage: uv run --with mpmath python scripts/z55_crossf_stats.py
import glob, math, re, os
import mpmath as mp

D = os.path.join(os.path.dirname(__file__), '..', 'data', 'z55', 'crossf')
rows = []
for f in sorted(glob.glob(os.path.join(D, 'scan_1e*.txt')) + glob.glob(os.path.join(D, 'sample_1e*.txt'))):
    hs = []; pmin = pmax = None
    for line in open(f):
        t = line.split()
        if len(t) != 2: continue
        p, h = int(t[0]), int(t[1]); hs.append(h); pmin = p if pmin is None else min(pmin, p); pmax = p if pmax is None else max(pmax, p)
    if not hs: continue
    N = len(hs); mean = sum(hs) / N; var = sum((h - mean) ** 2 for h in hs) / N; z = hs.count(0)
    lp = math.log((pmin + pmax) / 2)
    rows.append((os.path.basename(f), pmin, pmax, N, mean, var, z / N, math.exp(-mean), mean / lp ** 2, max(hs)))
print('file\tpmin\tpmax\tN\tmean\tvar\tzero_frac\texp(-mean)\tmean/log^2p\tmaxhits')
for r in rows:
    print('%s\t%d\t%d\t%d\t%.4f\t%.4f\t%.4f\t%.4f\t%.5f\t%d' % r)

mp.mp.dps = 20
def E(c, logx):  # int_{log x}^inf e^{s - c s^2}/(2s) ds
    return mp.quad(lambda s: mp.e ** (s - c * s * s) / (2 * s), [logx, 1 / c, 2 / c, mp.inf])
print('\nPoisson model: hits ~ Poisson(c log^2 p).  E(x) = expected # primes p = 1 (4), p > x, with hits = 0.')
for c in [1 / (3 * mp.pi ** 4), mp.mpf('0.0030')]:
    tot = E(c, mp.log(10 ** 8)); xs = mp.findroot(lambda L: mp.log(E(c, L)), 1 / c - 8)
    print('c=%.6f: E(1e8)=%s  E(1e18)=%s  E(1e60)=%s  E(1e100)=%s  peak of integrand (s=(1+sqrt(1-8c))/(4c)) at log10 p=%.1f  E=1 at log10 p=%.1f' % (
        float(c), mp.nstr(tot, 4), mp.nstr(E(c, mp.log(10 ** 18)), 4), mp.nstr(E(c, mp.log(10 ** 60)), 4),
        mp.nstr(E(c, mp.log(10 ** 100)), 4), float((1 + mp.sqrt(1 - 8 * c)) / (4 * c) / mp.log(10)), float(xs / mp.log(10))))
