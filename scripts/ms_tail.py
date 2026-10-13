"""O197: failure rate as a function of the local mean count, pooled over numerators (Assessment-level model).
For each m: mu_m(p) = a_m log^3 p + b_m log^2 p, least squares on the complete counts f_m(p), 100 <= p < 2e4
(data/ms/counts_m{m}.txt).  Failures: data/ms/prime_fail_1e8.txt (m <= 20, 24; complete to 1e8) or _1e7 (21-23).
Primes are binned by mu_m(p); per bin: #primes, #failures, empirical rate F(mu).  Pools: 4|m (8,12,16,20,24) and
4!|m (5,6,7,9,10,11,13,14,15,17,18,19,21,22,23).  Then the pooled F is applied to m = 4 (and 5): expected number of
failures sum_p F(mu_m(p)) over primes p in [PMIN, PMAX].
usage: ms_tail.py PMAX_count   (primes counted up to PMAX_count, <= 1e8; default 1e7)"""
import sys, math, re
import numpy as np
from sympy import primepi
from ms_stats import load

PMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7


def fit(m):
    D = load(m)
    ps = [p for p in D if 100 <= p < 20000 and m % p]
    L = np.array([math.log(p) for p in ps]); f = np.array([D[p][0] for p in ps], float)
    coef, *_ = np.linalg.lstsq(np.vstack([L ** 3, L ** 2]).T, f, rcond=None)
    return coef


def failures():
    F = {}
    for fn, lim in (('data/ms/prime_fail_1e8.txt', 10**8), ('data/ms/prime_fail_1e7.txt', 10**7)):
        txt = open(fn).read()
        for blk in re.findall(r'm=(\d+) mode=p N=\d+ failures:([\d\s]*)', txt):
            m = int(blk[0])
            if m not in F:
                F[m] = ([int(x) for x in blk[1].split()], lim)
    return F


EDGES = [0, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 70, 100, 1e9]


def binned(m, coef, fails, lim, pmin):
    """counts of primes / failures per mu-bin for primes in [pmin, min(lim, PMAX)].  mu is monotone in p for
    p >= 100 (checked), so bins are p-intervals: count primes via primepi on the interval boundaries."""
    a, b = coef
    mu = lambda p: a * math.log(p) ** 3 + b * math.log(p) ** 2
    hi = min(lim, PMAX)
    # invert mu on [pmin, hi] by bisection in log p
    def p_of(mu_t):
        lo_, hi_ = math.log(pmin), math.log(hi)
        if mu(pmin) >= mu_t: return pmin
        if mu(hi) < mu_t: return hi
        for _ in range(80):
            mid = (lo_ + hi_) / 2
            if mu(math.exp(mid)) < mu_t: lo_ = mid
            else: hi_ = mid
        return int(math.exp(hi_))
    out = []
    for e0, e1 in zip(EDGES, EDGES[1:]):
        p0, p1 = p_of(e0), p_of(e1)
        if p1 <= p0: out.append((0, 0)); continue
        n = int(primepi(p1) - primepi(p0))
        k = sum(1 for q in fails if p0 < q <= p1)
        out.append((n, k))
    return out


if __name__ == '__main__':
    F = failures()
    pools = {'4|m': [8, 12, 16, 20, 24], '4!|m': [5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23]}
    rates = {}
    for name, ms in pools.items():
        tot = np.zeros((len(EDGES) - 1, 2))
        for m in ms:
            coef = fit(m)
            fl, lim = F[m]
            tot += np.array(binned(m, coef, fl, lim, 100))
        rates[name] = tot
        print(f"pool {name} {ms}: bins of mu (primes p >= 100, up to {PMAX:.0e}):")
        for (e0, e1), (n, k) in zip(zip(EDGES, EDGES[1:]), tot):
            if n: print(f"   mu in [{e0},{e1}): primes {int(n)}, failures {int(k)}, rate {k/n:.2e}")
    # leave-one-out validation: predict each sibling's failures (p >= 100) from the rest of its pool
    for name, ms in pools.items():
        per = {m: np.array(binned(m, fit(m), F[m][0], F[m][1], 100)) for m in ms}
        for m in ms:
            rest = sum(per[k] for k in ms if k != m)
            pred = sum(n * K / N for (n, _), (N, K) in zip(per[m], rest) if n and N)
            print(f"   LOO {name}: m={m:2d} predicted failures (p>=100) {pred:6.2f}, observed {int(per[m][:,1].sum())}")
    for m in (4, 5, 6, 7):
        coef = fit(m)
        print(f"m={m}: mu_m(p) = {coef[0]:.4f} log^3 + {coef[1]:.4f} log^2; mu(100) = "
              f"{coef[0]*math.log(100)**3+coef[1]*math.log(100)**2:.1f}")
        b = binned(m, coef, [], 10**8, 5)
        for name in rates:
            exp_ = 0.0; ub = 0.0
            for (n, _), (N, K) in zip(b, rates[name]):
                if n and N:
                    exp_ += n * K / N; ub += n * (K + 1) / N
            print(f"   pooled rate of {name} applied to m={m}, primes 5..{PMAX:.0e}: expected failures {exp_:.2f}"
                  f" (rule-of-three-ish upper, (K+1)/N per bin: {ub:.2f})")
