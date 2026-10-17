"""O259: heuristic model of N1(p) (b = 1 line) and Nc1(p) (c = 1 line), B1_LINE.md §3.
Input: files of lines "p N1 Nc1 [N1_{s>64}]" from `z29_census countlist` (complete counts).
Model: within the nontrivial class (b = 1: p = 1 mod 24; c = 1: p = 1 mod 8), N ~ negative binomial with mean mu(p) and
dispersion D = var/mean; P(N = 0) = D^(-mu/(D-1)) (Poisson: e^-mu). Back-test against observed zero counts; extrapolate.
usage: PYTHONPATH=scripts uv run python scripts/z29_model.py cl_1e6.txt cw_1e8.txt cw_1e10.txt
"""
import sys, math
from statistics import mean, pvariance

rows = []
for f in sys.argv[1:]:
    for l in open(f):
        a = l.split()
        if a: rows.append((int(a[0]), int(a[1]), int(a[2])))

def nb0(mu, D):
    return math.exp(-mu) if D <= 1.0001 else D ** (-mu / (D - 1))

def analyse(name, idx, cls):
    sel = [r for r in rows if r[0] % cls[0] == cls[1]]
    print(f"== {name} (nontrivial class p = {cls[1]} mod {cls[0]}: {len(sel)} primes)")
    print(" bin(log10 p)   n     mean   mean/log^2p  disp   obs#0  NB-pred#0  Poi-pred#0  obs#<=2  NB-pred#<=2")
    bins = {}
    for r in sel:
        b = math.floor(2 * math.log10(r[0])) / 2
        bins.setdefault(b, []).append(r)
    fit = []
    for b in sorted(bins):
        rs = bins[b]; v = [r[idx] for r in rs]
        if len(rs) < 30: continue
        mu = mean(v); D = max(pvariance(v) / mu, 1.0)
        L2 = mean(math.log(r[0]) ** 2 for r in rs)
        # NB with per-prime mu scaled by log^2 p within the bin
        pred0 = sum(nb0(mu * math.log(r[0]) ** 2 / L2, D) for r in rs)
        poi0 = sum(math.exp(-mu * math.log(r[0]) ** 2 / L2) for r in rs)
        r_ = mu / (D - 1) if D > 1.0001 else None
        def nbcdf2(m):
            if r_ is None: return sum(math.exp(-m) * m ** k / math.factorial(k) for k in range(3))
            q = m / (m + r_ * 1.0) ; rr = r_
            p0 = (1 - q) ** rr; p1 = p0 * rr * q; p2 = p1 * (rr + 1) * q / 2
            return p0 + p1 + p2
        pred2 = sum(nbcdf2(mu * math.log(r[0]) ** 2 / L2) for r in rs)
        obs0 = sum(1 for x in v if x == 0); obs2 = sum(1 for x in v if x <= 2)
        fit.append((L2, mu, D))
        print(f"  {b:4.1f}       {len(rs):5d}  {mu:7.2f}   {mu / L2:6.3f}     {D:4.2f}   {obs0:4d}   {pred0:8.3f}   {poi0:8.4f}   {obs2:5d}   {pred2:8.2f}")
    return fit

fb = analyse("b = 1 line", 1, (24, 1))
fc = analyse("c = 1 line (*)", 2, (8, 1))

def tail(fit, name, X0, dens):
    # alpha = mean/log^2 p from the two largest bins; D = max observed dispersion (conservative)
    al = min(f[1] / f[0] for f in fit[-2:]); D = max(f[2] for f in fit)
    tot = 0.0; x = X0
    while x < 1e40:
        x2 = x * 1.1
        nprimes = dens * (x2 - x) / math.log(x)
        tot += nprimes * nb0(al * math.log(x) ** 2, D)
        x = x2
    return al, D, tot

for fit, name, dens in ((fb, "b=1", 1 / 8), (fc, "c=1", 1 / 4)):
    for X0 in (1e6, 1e8, 1e11):
        al, D, tot = tail(fit, name, X0, dens)
        print(f"{name}: expected failures beyond {X0:.0e} (mu = {al:.3f} log^2 p, D = {D:.2f}, NB): {tot:.3g}")
        al2, D2 = 0.8 * al, D
        tot2 = 0.0; x = X0
        while x < 1e40:
            x2 = x * 1.1; tot2 += dens * (x2 - x) / math.log(x) * nb0(al2 * math.log(x) ** 2, D2); x = x2
        print(f"      same with mu depressed by 20% everywhere (hard-class depression, §3): {tot2:.3g}")
