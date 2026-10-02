"""Independent exact-LP tests of Theorem 2.5 / Proposition 2.4 of EXCEPTIONAL_THETA.md.

Written by the hostile reviewer; shares no code with scripts/theta_*.py.

Part A (CRT level).  For small prime-slice CRT systems on Z/Q_tot (Q_tot may
contain prime powers of slice primes and free non-slice primes) solve
    W_CRT = min { E nu : nu in span of class indicators of slice-level <= lam,
                         nu >= 0 on Z/Q_tot, nu >= 1 on the avoider set }
and compare with
    (1/Q0) * sum_{c in R} W_bool(p(c), log l, lam)
(the Boolean fibre LPs).  The proof of Thm 2.5 gives ">=", and lifting a
Boolean fibre optimum gives "<=", so equality is expected.  Also report the
theorem's bound (2.4), optimised over alpha.

Part B (Boolean, multi-band).  For random weighted instances check the whole
chain of Proposition 2.4:
    W_bool >= E_w W_multi(z(w))                      (Steps 2-3)
           >= E_w 1/(sum_j |c_j| prod_g B_g(j_g))    (Step 4, recipe nodes)
           >= exp(-RHS(2.3))                         (Step 5 + Jensen)
where W_multi is the LP over polynomials in P_{Lambda'} nonnegative on the
count grid, and B_g(k) is the exact value B(Y) of the Lemma 2.2 node recipe
(min over the recipes (a),(b),(c) that apply).

Part C. Lemma 2.3 identity on random lower sets / random node sets, and
Lemma 2.2 inequality (2.2) on a dense grid including edge cases.

Run:  PYTHONPATH=scripts uv run --with scipy python scripts/review_theta_lp.py
"""
import itertools
import math
import random
import sys

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

C1 = 16 * math.e ** 6
C4 = 8 * math.e ** 5


# ---------------------------------------------------------------- Boolean LP
def bool_lp(p, s, lam):
    """min E f over f = sum_{S: sum s_i <= lam} c_S x^S, f>=0 on cube, f(0)>=1."""
    n = len(p)
    pts = list(itertools.product([0, 1], repeat=n))
    probs = np.array([math.prod(pi if xi else 1 - pi for pi, xi in zip(p, x)) for x in pts])
    subsets = [S for k in range(n + 1) for S in itertools.combinations(range(n), k)
               if sum(s[i] for i in S) <= lam + 1e-12]
    A = np.array([[1.0 if all(x[i] for i in S) else 0.0 for S in subsets] for x in pts])
    c = probs @ A
    b = np.zeros(len(pts)); b[0] = -1.0
    res = linprog(c, A_ub=-A, b_ub=b, bounds=[(None, None)] * len(subsets), method="highs")
    assert res.status == 0, res.message
    return res.fun


# ---------------------------------------------------------------- CRT LP
def crt_lp(Q0, R, slice_primes, E, F, lam, free=1):
    """Exact LP on Z/Q_tot, Q_tot = Q0*free*prod l^E_l.  F[(c,l)] = forbidden set mod l.
    Level counts only slice primes (sum log l over l | modulus)."""
    Ps = list(slice_primes)
    Qtot = Q0 * free * math.prod(l ** E[l] for l in Ps)
    n = np.arange(Qtot)
    c = n % Q0
    inR = np.isin(c, list(R))
    avoid = inR.copy()
    for l in Ps:
        r = n % l
        hit = np.zeros(Qtot, bool)
        for cc in R:
            fs = F[(cc, l)]
            if fs:
                hit |= (c == cc) & np.isin(r, list(fs))
        avoid &= ~hit
    # maximal allowed slice sets
    allowed = [T for k in range(len(Ps) + 1) for T in itertools.combinations(Ps, k)
               if sum(math.log(l) for l in T) <= lam + 1e-12]
    maximal = [T for T in allowed if not any(set(T) < set(U) for U in allowed)]
    cols, obj = [], []
    off = 0
    for T in maximal:
        m = Q0 * free * math.prod(l ** E[l] for l in T)
        cols.append((off, m))
        obj.extend([1.0 / m] * m)
        off += m
    rows = np.concatenate([n for _ in cols])
    colidx = np.concatenate([o + n % m for (o, m) in cols])
    A = sp.csr_matrix((np.ones(len(rows)), (rows, colidx)), shape=(Qtot, off))
    b = np.where(avoid, -1.0, 0.0)
    for meth in ("highs-ds", "highs-ipm", "highs"):
        res = linprog(np.array(obj), A_ub=-A, b_ub=b, bounds=[(None, None)] * off, method=meth)
        if res.status == 0:
            break
    if res.status != 0:
        return None, avoid.mean()
    return res.fun, avoid.mean()


def rhs_23(p, s, lam, alpha):
    """Right side of (2.3) (log 1/Ef bound), coordinates with s_i<=lam only."""
    vis = [(pi, si) for pi, si in zip(p, s) if si <= lam and pi > 0]
    if not vis:
        return 0.0
    s_star = min(s)
    if lam < s_star:
        return 0.0
    G = math.floor(math.log2(lam / s_star)) + 1
    mu = sum(pi for pi, _ in vis)
    return (19 * alpha * lam + C4 * sum(pi * math.exp(-alpha * si) for pi, si in vis)
            + G * (75 + math.log(2 + lam / s_star)) + G / 2 * math.log(16 * mu + 16))


def best_rhs(p, s, lam):
    return min(rhs_23(p, s, lam, a) for a in np.geomspace(1e-3, 50, 400))


# ---------------------------------------------------------------- node lemma
def binom_pmf(z, q):
    return np.array([math.exp(math.lgamma(z + 1) - math.lgamma(k + 1) - math.lgamma(z - k + 1)
                              + k * math.log(q) + (z - k) * math.log1p(-q)) for k in range(z + 1)])


def B_of(Y, psi):
    Y = list(Y)
    worst = 0.0
    for i, yi in enumerate(Y):
        num = 1.0
        for j, yj in enumerate(Y):
            if j != i:
                num *= (0 - yj) / (yi - yj)
        worst = max(worst, abs(num) / psi[yi])
    return worst


def recipe_nodes(k, z, q):
    """All node sets offered by Lemma 2.2 (a),(b),(c) that apply; returns list."""
    mu = z * q
    out = []
    if k == 0:
        out.append([math.ceil(mu)] if mu >= 1 else [0])
        out.append([0])
    if k <= z:
        out.append(list(range(k + 1)))
    if mu >= 64 and 1 <= k <= mu / 16:
        W = math.ceil(math.sqrt(k * mu) / 2)
        h = math.ceil(2 * W / k)
        a = math.ceil(mu) - W
        out.append([a + i * h for i in range(k + 1)])
    return out


def B_recipe(k, z, q, psi=None):
    if psi is None:
        psi = binom_pmf(z, q)
    return min(B_of(Y, psi) for Y in recipe_nodes(k, z, q))


def rhs22(k, s, alpha, mu):
    return 19 * alpha * k * s + C4 * mu * math.exp(-2 * alpha * s) + 0.5 * math.log(16 * mu + 16) + 74


# ---------------------------------------------------------------- multi LP
def lower_set(svals, lam, zs):
    G = len(svals)
    ranges = [range(0, min(zs[g], int(lam // svals[g])) + 1) for g in range(G)]
    return [j for j in itertools.product(*ranges) if sum(jg * sg for jg, sg in zip(j, svals)) <= lam + 1e-12]


def multi_lp(zs, qs, svals, lam):
    Lam = lower_set(svals, lam, zs)
    grid = list(itertools.product(*[range(z + 1) for z in zs]))
    pm = [binom_pmf(z, q) for z, q in zip(zs, qs)]
    w = np.array([math.prod(pm[g][y[g]] for g in range(len(zs))) for y in grid])
    A = np.array([[math.prod(float(y[g]) ** a[g] for g in range(len(zs))) for a in Lam] for y in grid])
    b = np.zeros(len(grid)); b[grid.index(tuple([0] * len(zs)))] = -1.0
    res = linprog(w @ A, A_ub=-A, b_ub=b, bounds=[(None, None)] * len(Lam), method="highs")
    assert res.status == 0, res.message
    return res.fun


def comb_coeffs(Lam):
    S = set(Lam)
    G = len(Lam[0])
    out = {}
    for j in Lam:
        cj = 0
        for e in itertools.product([0, 1], repeat=G):
            if tuple(a + b for a, b in zip(j, e)) in S:
                cj += (-1) ** sum(e)
        out[j] = cj
    return out


def chain(p, s, lam):
    n = len(p)
    s_star = min(s)
    Gn = math.floor(math.log2(lam / s_star)) + 1
    bands = [[i for i in range(n) if 2 ** g * s_star <= s[i] < 2 ** (g + 1) * s_star and s[i] <= lam and p[i] > 0]
             for g in range(Gn)]
    bands = [b for b in bands if b]
    gidx = [min(g for g in range(Gn) if 2 ** g * s_star <= s[b[0]] < 2 ** (g + 1) * s_star) for b in bands]
    svals = [2 ** g * s_star for g in gidx]
    qs = [max(p[i] for i in b) for b in bands]
    Wf = bool_lp(p, s, lam)
    EWm, EB = 0.0, 0.0
    EPhi = 0.0
    for wv in itertools.product(*[list(itertools.product([0, 1], repeat=len(b))) for b in bands]):
        pw = 1.0
        zs = []
        for b, q, wb in zip(bands, qs, wv):
            for i, wi in zip(b, wb):
                pw *= (p[i] / q) if wi else (1 - p[i] / q)
            zs.append(sum(wb))
        if pw == 0:
            continue
        Wm = multi_lp(zs, qs, svals, lam)
        Lam = lower_set(svals, lam, zs)
        cc = comb_coeffs(Lam)
        Bg = [{k: B_recipe(k, z, q) for k in range(z + 1)} for z, q in zip(zs, qs)]
        denom = sum(abs(cc[j]) * math.prod(Bg[g][j[g]] for g in range(len(zs))) for j in Lam if cc[j])
        EWm += pw * Wm
        EB += pw / denom
        EPhi += pw * math.log(denom)
    return Wf, EWm, EB, math.exp(-EPhi), math.exp(-best_rhs(p, s, lam))


# ---------------------------------------------------------------- Part C
def lemma23_test(trials=200, seed=3):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        G = rng.choice([1, 2, 3])
        svals = [rng.uniform(1, 3) * 2 ** g for g in range(G)]
        lam = rng.uniform(2, 12)
        zs = [rng.randint(0, 6) for _ in range(G)]
        Lam = lower_set(svals, lam, zs)
        cc = comb_coeffs(Lam)
        coef = {a: rng.gauss(0, 1) for a in Lam}
        Qf = lambda y: sum(cf * math.prod(float(y[g]) ** a[g] for g in range(G)) for a, cf in coef.items())
        x0 = [rng.uniform(-3, 3) for _ in range(G)]
        # random distinct nodes per (g,k), non-nested
        nodes = [{k: rng.sample(range(-5, 12), k + 1) for k in range(zs[g] + 1)} for g in range(G)]
        tot = 0.0
        for j in Lam:
            if not cc[j]:
                continue
            Ys = [nodes[g][j[g]] for g in range(G)]
            val = 0.0
            for y in itertools.product(*Ys):
                wgt = 1.0
                for g in range(G):
                    for yy in Ys[g]:
                        if yy != y[g]:
                            wgt *= (x0[g] - yy) / (y[g] - yy)
                val += wgt * Qf(y)
            tot += cc[j] * val
        worst = max(worst, abs(tot - Qf(x0)) / (1 + abs(Qf(x0))))
        assert all(abs(c) <= 2 ** G for c in cc.values())
    return worst


def lemma22_grid():
    viol = 0
    worst_margin = math.inf
    cases = 0
    for z in [1, 2, 3, 5, 8, 13, 30, 64, 100, 257, 300, 600, 1200, 2000]:
        for q in [0.01, 0.05, 0.1, 0.2, 0.25]:
            mu = z * q
            psi = binom_pmf(z, q)
            for k in sorted(set([0, 1, 2, 3, 5, 8, int(mu / 16), int(mu / 16) + 1, int(mu / 4), z]) ):
                if k < 0 or k > z or k > 60:
                    continue
                B = B_recipe(k, z, q, psi)
                lB = math.log(B)
                for s in [0.5, 1, 2, 5, 10]:
                    for alpha in [1e-3, 1e-2, 0.05, 0.2, 1, 3]:
                        cases += 1
                        m = rhs22(k, s, alpha, mu) - lB
                        worst_margin = min(worst_margin, m)
                        if m < -1e-9:
                            viol += 1
                # (c) itself
                if mu >= 64 and 1 <= k <= mu / 16:
                    W = math.ceil(math.sqrt(k * mu) / 2); h = math.ceil(2 * W / k); a = math.ceil(mu) - W
                    Bc = B_of([a + i * h for i in range(k + 1)], psi)
                    if math.log(Bc) > (k / 2) * math.log(C1 * mu / k) + 0.5 * math.log(16 * mu) + 1e-9:
                        viol += 1
    return cases, viol, worst_margin


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "ABC"
    if "C" in part:
        print("Part C: Lemma 2.3 max rel. error over 200 random lower sets:", lemma23_test())
        print("Part C: Lemma 2.2 (2.2)/(c) grid: cases, violations, worst margin =", lemma22_grid())
    if "A" in part:
        rng = random.Random(7)
        print("Part A: CRT LP vs fibre Boolean LPs")
        configs = [
            dict(Q0=4, R=[1, 3], P=[5, 7, 11, 13], E={5: 1, 7: 1, 11: 1, 13: 1}, free=1),
            dict(Q0=6, R=[1, 5], P=[5, 7, 11, 13], E={5: 2, 7: 1, 11: 1, 13: 1}, free=1),
            dict(Q0=4, R=[1, 2, 3], P=[5, 7, 11], E={5: 1, 7: 1, 11: 1}, free=3),
            dict(Q0=2, R=[1], P=[5, 7, 11, 13, 17], E={5: 1, 7: 1, 11: 1, 13: 1, 17: 1}, free=1),
        ]
        for cf in configs:
            for trial in range(2):
                F = {}
                for c in cf["R"]:
                    for l in cf["P"]:
                        kmax = l // 4
                        F[(c, l)] = set(rng.sample(range(l), rng.randint(0, kmax)))
                lams = sorted(set([math.log(l) for l in cf["P"]] + [math.log(35), math.log(143), math.log(1001)]))
                if len(cf["P"]) > 4:
                    lams = [x for x in lams if x <= math.log(143) + 1e-9]
                for lam in lams:
                    W, dens = crt_lp(cf["Q0"], cf["R"], cf["P"], cf["E"], F, lam, cf["free"])
                    if W is None:
                        print(f"  (solver failure at lam=e^{math.exp(lam):.0f}, Q0={cf['Q0']}; skipped, not a math failure)")
                        continue
                    fib, bnd = 0.0, 0.0
                    for c in cf["R"]:
                        p = [len(F[(c, l)]) / l for l in cf["P"]]
                        s = [math.log(l) for l in cf["P"]]
                        fib += bool_lp(p, s, lam)
                    fib /= cf["Q0"]
                    # theorem bound with averaged profile
                    pbar = [np.mean([len(F[(c, l)]) / l for c in cf["R"]]) for l in cf["P"]]
                    s = [math.log(l) for l in cf["P"]]
                    bnd = len(cf["R"]) / cf["Q0"] * math.exp(-best_rhs(pbar, s, lam))
                    ok = abs(W - fib) < 1e-7 and W >= bnd * (1 - 1e-9) and W >= dens - 1e-9
                    print(f"  Q0={cf['Q0']} P={cf['P']} E={list(cf['E'].values())} free={cf['free']} lam=e^{math.exp(lam):.0f}: "
                          f"W_CRT={W:.6f} fibreLP={fib:.6f} void={dens:.6f} -log(W)={-math.log(W):.3f} "
                          f"thm_bound(-log)={-math.log(bnd):.1f} {'ok' if ok else 'FAIL'}")
                    assert ok
    if "B" in part:
        rng = random.Random(11)
        print("Part B: Proposition 2.4 chain on random multi-band instances")
        worst = [math.inf] * 4
        for trial in range(60):
            n = rng.choice([4, 5, 6, 7])
            s = [rng.choice([1.0, 1.3, 1.9, 2.2, 3.5, 4.1, 7.5]) for _ in range(n)]
            p = [rng.uniform(0.01, 0.25) for _ in range(n)]
            lam = rng.choice([1.0, 2.0, 3.0, 4.4, 6.0, 9.0])
            if lam < min(s):
                continue
            Wf, EWm, EB, EJ, Eth = chain(p, s, lam)
            gaps = [Wf - EWm, EWm - EB, EB - EJ, EJ - Eth]
            worst = [min(a, b) for a, b in zip(worst, gaps)]
            ok = all(g > -1e-8 for g in gaps)
            print(f"  n={n} lam={lam} -log: W={-math.log(Wf):.4f} multi={-math.log(EWm):.4f} "
                  f"lagr={-math.log(EB):.3f} jensen={-math.log(EJ):.3f} thm={-math.log(Eth):.1f} {'ok' if ok else 'FAIL'}")
            assert ok
        print("  min gaps (W-multi, multi-lagr, lagr-jensen, jensen-thm):", worst)
