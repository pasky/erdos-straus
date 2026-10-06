"""R68b from-scratch sanity checks of POINTWISE_OMEGA17 Lemmas 1.2, 1.3, 2.1, 4.1, 5.1.

1.2: every class mod q>x meets [1,x] in <=1 integer (brute force small x).
1.3: random SALC LPs: primal min sum mF  ==  dual max  alpha N + sum(beta l - gamma u) - sum theta.
2.1: LP on {0,1}^n: psi>=0 nondecreasing, psi(0)=0, E psi=1, E[psi z_b]=p_b  -> infeasible;
     without monotonicity -> feasible (planted law) when R large.
4.1: example f(j)=j(j-5)^2/12 has Poisson mean exactly 1 at R=2,3 (exact).
5.1: aggregated LP (cells with capacities) == full LP (random instances).
"""
import itertools, random
from fractions import Fraction as Fr
from math import factorial
import numpy as np
from scipy.optimize import linprog

rng = random.Random(1768)

# ---- 1.2
for x in range(1, 60):
    for q in range(x + 1, 2 * x + 3):
        for a in range(q):
            assert sum(1 for n in range(1, x + 1) if n % q == a) <= 1
print("1.2: classes mod q>x meet [1,x] in <=1 integer (x<60): OK")

# ---- 1.3 and 5.1 on random instances
def random_instance(nS=30, nC=10):
    F = [rng.random() < 0.6 for _ in range(nS)]
    Ns = sorted(rng.sample(range(nS), rng.randint(5, 12)))  # 'primes'
    mtrue = np.zeros(nS); mtrue[Ns] = 1
    classes = []
    for _ in range(nC):
        q = rng.randint(2, 7); a = rng.randrange(q)
        C = np.array([1.0 if i % q == a else 0.0 for i in range(nS)])
        v = C @ mtrue
        classes.append((C, v - rng.choice([0, 0.5, 1]), v + rng.choice([0, 0.5, 1])))
    return np.array(F, float), len(Ns), classes

def primal(F, N, classes, nS):
    A_ub = []; b_ub = []
    for C, l, u in classes:
        A_ub.append(C); b_ub.append(u); A_ub.append(-C); b_ub.append(-l)
    r = linprog(F, A_ub=np.array(A_ub), b_ub=b_ub, A_eq=np.ones((1, nS)), b_eq=[N],
                bounds=[(0, 1)] * nS, method="highs")
    assert r.status == 0
    return r.fun

def dual(F, N, classes, nS):
    nC = len(classes)
    # vars: alpha (free), beta_C>=0, gamma_C>=0, theta_n>=0 ; maximise
    nv = 1 + 2 * nC + nS
    c = np.zeros(nv); c[0] = -N
    for i, (C, l, u) in enumerate(classes):
        c[1 + i] = -l; c[1 + nC + i] = u
    c[1 + 2 * nC:] = 1.0
    A = np.zeros((nS, nv)); A[:, 0] = 1
    for i, (C, l, u) in enumerate(classes):
        A[:, 1 + i] = C; A[:, 1 + nC + i] = -C
    A[:, 1 + 2 * nC:] = -np.eye(nS)
    bounds = [(None, None)] + [(0, None)] * (2 * nC + nS)
    r = linprog(c, A_ub=A, b_ub=F, bounds=bounds, method="highs")
    assert r.status == 0
    return -r.fun

def aggregated(F, N, classes, nS):
    keys = {}
    for i in range(nS):
        k = (F[i],) + tuple(C[i] for C, _, _ in classes)
        keys.setdefault(k, []).append(i)
    cells = list(keys.items())
    cost = np.array([k[0] for k, _ in cells])
    A_ub = []; b_ub = []
    for j, (C, l, u) in enumerate(classes):
        row = np.array([k[1 + j] for k, _ in cells])
        A_ub.append(row); b_ub.append(u); A_ub.append(-row); b_ub.append(-l)
    r = linprog(cost, A_ub=np.array(A_ub), b_ub=b_ub, A_eq=np.ones((1, len(cells))), b_eq=[N],
                bounds=[(0, len(v)) for _, v in cells], method="highs")
    return r.fun

worst = 0
for t in range(200):
    nS = 30
    F, N, classes = random_instance(nS)
    p, d, a = primal(F, N, classes, nS), dual(F, N, classes, nS), aggregated(F, N, classes, nS)
    worst = max(worst, abs(p - d), abs(p - a))
print(f"1.3 duality and 5.1 aggregation: 200 random LPs, max |primal-dual|,|primal-agg| = {worst:.2e}")

# ---- 2.1
def lp21(n, p, monotone):
    cfg = list(itertools.product((0, 1), repeat=n))
    P = np.array([np.prod([p[b] if z[b] else 1 - p[b] for b in range(n)]) for z in cfg])
    nv = len(cfg)
    A_eq = [P.copy()]; b_eq = [1.0]
    for b in range(n):
        A_eq.append(np.array([P[i] * (z[b] - p[b]) for i, z in enumerate(cfg)])); b_eq.append(0)
    A_ub = []; b_ub = []
    if monotone:
        idx = {z: i for i, z in enumerate(cfg)}
        for z in cfg:
            for b in range(n):
                if z[b] == 0:
                    w = list(z); w[b] = 1
                    row = np.zeros(nv); row[idx[z]] = 1; row[idx[tuple(w)]] = -1
                    A_ub.append(row); b_ub.append(0)
    bounds = [(0, 0)] + [(0, None)] * (nv - 1)
    r = linprog(np.zeros(nv), A_ub=np.array(A_ub) if A_ub else None, b_ub=b_ub or None,
                A_eq=np.array(A_eq), b_eq=b_eq, bounds=bounds, method="highs")
    return r.status  # 0 feasible, 2 infeasible

res = {True: [], False: []}
for t in range(100):
    n = rng.randint(2, 6)
    p = [rng.uniform(0.05, 0.9) for _ in range(n)]
    for mono in (True, False):
        res[mono].append(lp21(n, p, mono))
print("2.1: monotone fake feasible in", sum(s == 0 for s in res[True]), "/100 (expect 0);",
      "non-monotone feasible in", sum(s == 0 for s in res[False]), "/100")

# ---- 4.1 example
def pois_mean(f, R, J=200):
    # exact: E f(N) for polynomial f via factorial moments; here brute-force with closed form
    pass
for R in (2, 3):
    # E[N(N-5)^2] = E N^3 - 10 E N^2 + 25 E N; Poisson moments
    EN, EN2, EN3 = R, R * R + R, R ** 3 + 3 * R * R + R
    assert Fr(EN3 - 10 * EN2 + 25 * EN, 12) == 1
print("4.1 example f(j)=j(j-5)^2/12: Poisson mean 1 at R=2 and R=3: OK")
