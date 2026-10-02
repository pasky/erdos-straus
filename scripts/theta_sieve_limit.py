"""Numerical companion for EXCEPTIONAL_THETA.md, Section 2 (sieve-limit theorem).

One-dimensional exchangeable problem.  K ~ Bin(z, q) (or Poisson(mu)).
    W(m) = min { E Q(K) : deg Q <= m, Q(k) >= 0 for k = 0..z, Q(0) >= 1 }.

We print, for several (mu, m):
  * logU  : -log of the Christoffel/Selberg value 1/sum_{j<=m/2} mu^j/j!
            (an UPPER bound for W: the square majorant q(K)^2);
  * logV  : -log of the LP value with the dual restricted to the support
            {0..kmax} (a LOWER bound for W: every dual-feasible pi gives
            W >= pi(0));
  * logL  : -log of the Lagrange-node bound of Lemma 2.2 with the explicit
            node recipe of the lemma (a rigorous LOWER bound for W);
  * logLopt: the same bound with the best nodes found by a small search;
  * claim : the explicit right-hand side (k/2)log(C1 mu/k)+(1/2)log(16 mu)
            of Lemma 2.2 (must be >= logL).
All logs are natural; "saving" = -log W.  Larger saving = stronger sieve.

Also checks Lemma 2.2's inequality on a grid of (z, q, k) with exact
binomial pmf (lgamma), and the Rankin step
    (k/2) log(C1 mu/k) <= a k s + (C1 mu/(2e)) exp(-2 a s).

Run:  uv run --with scipy python scripts/theta_sieve_limit.py
"""
import math
import sys

import numpy as np

C1 = 16 * math.e ** 6


def log_binom_pmf(z, q, y):
    return (math.lgamma(z + 1) - math.lgamma(y + 1) - math.lgamma(z - y + 1)
            + y * math.log(q) + (z - y) * math.log1p(-q))


def log_pois_pmf(mu, y):
    return -mu + y * math.log(mu) - math.lgamma(y + 1)


def lagrange_bound(nodes, logpmf):
    """log of max_i |ell_i(0)| / psi(y_i) for integer nodes (exact in logs)."""
    best = -math.inf
    for i, yi in enumerate(nodes):
        s = 0.0
        for j, yj in enumerate(nodes):
            if j == i:
                continue
            s += math.log(abs(yj)) - math.log(abs(yj - yi))
        best = max(best, s - logpmf(yi))
    return best


def recipe_nodes(mu, k):
    """Node recipe of Lemma 2.2: W=ceil(sqrt(k mu)/2), h=ceil(2W/k), a=ceil(mu)-W."""
    W = math.ceil(math.sqrt(k * mu) / 2)
    h = math.ceil(2 * W / k)
    a = math.ceil(mu) - W
    return [a + i * h for i in range(k + 1)]


def claim_rhs(mu, k):
    return (k / 2) * math.log(C1 * mu / k) + 0.5 * math.log(16 * mu)


def logU(mu, m):
    # -log(1/sum_{j<=m/2} mu^j/j!)
    terms = [j * math.log(mu) - math.lgamma(j + 1) for j in range(m // 2 + 1)]
    mx = max(terms)
    return mx + math.log(sum(math.exp(t - mx) for t in terms))


def charlier_orthonormal(mu, m, ks):
    """Orthonormal Charlier polynomials p_0..p_m (w.r.t. Poisson(mu)) at ks."""
    ks = np.asarray(ks, dtype=float)
    P = np.zeros((m + 1, len(ks)))
    P[0] = 1.0
    if m >= 1:
        P[1] = (ks - mu) / math.sqrt(mu)
    for n in range(1, m):
        # monic recurrence: C_{n+1} = (x - n - mu) C_n - n mu C_{n-1}
        # orthonormal: p_{n+1} = ((x-n-mu) p_n - sqrt(n mu) p_{n-1}) / sqrt((n+1) mu)
        P[n + 1] = ((ks - n - mu) * P[n] - math.sqrt(n * mu) * P[n - 1]) / math.sqrt((n + 1) * mu)
    return P


def logV(mu, m, kmax=None):
    from scipy.optimize import linprog
    if kmax is None:
        kmax = int(mu + 14 * math.sqrt(mu) + 3 * m + 20)
    ks = np.arange(kmax + 1)
    P = charlier_orthonormal(mu, m, ks)
    # variables pi_k >= 0 ; constraints: sum pi = 1, sum pi p_j(k) = 0 (j=1..m)
    # rescale the pi_0 column by exp(-s), s ~ Selberg saving, so that the
    # optimal variable is O(1) (otherwise pi_0 ~ 1e-15 is below LP tolerances)
    s = logU(mu, m)
    A_eq = P.copy()
    A_eq[:, 0] *= math.exp(-s)
    b_eq = np.zeros(m + 1)
    b_eq[0] = 1.0
    c = np.zeros(kmax + 1)
    c[0] = -1.0
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * (kmax + 1), method="highs",
                  options={"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10})
    if res.status != 0:
        return float("nan")
    v = -res.fun
    return s - math.log(v) if v > 0 else float("inf")


def best_nodes_search(mu, k):
    """Small search over arithmetic progressions of nodes (a, h)."""
    lp = lambda y: log_pois_pmf(mu, y)
    best = math.inf
    for W in np.linspace(0.2, 1.6, 15) * math.sqrt(k * mu):
        h = max(1, int(round(2 * W / k)))
        a = int(round(mu - k * h / 2))
        if a < 1:
            continue
        nodes = [a + i * h for i in range(k + 1)]
        best = min(best, lagrange_bound(nodes, lp))
    return best


def table():
    print("# saving = -log W ; logU <= saving(W) <= logV ; logL,logLopt rigorous lower bounds on W")
    print(f"{'mu':>6} {'m':>4} {'logU(Selberg)':>14} {'logV(LP)':>10} {'logLopt':>9} "
          f"{'logL(recipe)':>13} {'claim':>8} {'(m/2)log(mu/m)':>15}")
    for mu in [64, 128, 256, 512]:
        for m in [2, 4, 8, 16]:
            if m > mu / 16:
                continue
            k = m  # degree of the majorant = number of interpolation nodes - 1
            u = logU(mu, m)
            try:
                v = logV(mu, m)
            except Exception as e:  # pragma: no cover
                v = float("nan")
            lo = best_nodes_search(mu, k)
            lr = lagrange_bound(recipe_nodes(mu, k), lambda y: log_pois_pmf(mu, y))
            cl = claim_rhs(mu, k)
            print(f"{mu:6d} {m:4d} {u:14.3f} {v:10.3f} {lo:9.3f} {lr:13.3f} {cl:8.3f} "
                  f"{(m/2)*math.log(mu/m):15.3f}")
            # consistency: Selberg value is an upper bound on W, LP value a lower bound
            # on W (so logV >= saving >= logU), Lagrange bound a lower bound (logL >= logV)
            if math.isnan(v):  # LP may fail numerically for large instances
                print(f"   (LP solver failed for mu={mu}, m={m}; row has no LP value)")
            else:
                assert u <= v + 1e-3, (mu, m, u, v)
                assert v <= lo + 1e-6 and v <= lr + 1e-6, (mu, m, v, lo, lr)
            assert u <= lo + 1e-6 and u <= lr + 1e-6, (mu, m, u, lo, lr)
            assert lr <= cl + 1e-9, (mu, m, lr, cl)


def check_lemma_grid():
    """Lemma 2.2 for binomial laws: recipe nodes, all k in [1, mu/16], mu >= 64."""
    bad = 0
    n = 0
    for z in [10 ** 3, 10 ** 4, 10 ** 6]:
        for q in [0.5, 0.25, 0.1, 0.01, 1e-3]:
            mu = z * q
            if mu < 64:
                continue
            for k in sorted(set([1, 2, 3, 5, 8, 13, int(mu // 64), int(mu // 32), int(mu // 16)])):
                if k < 1 or k > mu / 16:
                    continue
                nodes = recipe_nodes(mu, k)
                assert len(set(nodes)) == k + 1 and min(nodes) >= mu / 2 and max(nodes) <= 2 * mu
                assert max(nodes) <= z - 1
                lb = lagrange_bound(nodes, lambda y: log_binom_pmf(z, q, y))
                n += 1
                if lb > claim_rhs(mu, k) + 1e-9:
                    bad += 1
                    print("VIOLATION", z, q, k, lb, claim_rhs(mu, k))
    print(f"Lemma 2.2 grid: {n} cases, {bad} violations")
    assert bad == 0


def check_rankin_step():
    bad = 0
    for mu in [64, 1e3, 1e5]:
        for k in range(1, int(mu // 16) + 1, max(1, int(mu // 160))):
            for s in [0.5, 1, 3, 10, 30]:
                for a in [1e-3, 1e-2, 0.1, 0.5, 1]:
                    lhs = (k / 2) * math.log(C1 * mu / k)
                    rhs = a * k * s + (C1 * mu / (2 * math.e)) * math.exp(-2 * a * s)
                    if lhs > rhs * (1 + 1e-12):
                        bad += 1
    print(f"Rankin step: violations {bad}")
    assert bad == 0


if __name__ == "__main__":
    check_lemma_grid()
    check_rankin_step()
    table()
    print("OK")
