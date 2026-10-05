"""EXCEPTIONAL_LARGESIEVE2.md numerics (EVIDENCE / sanity checks only).

Toy family: all R(M)-, (a,D)-, Case-A classes with modulus | L and the
selector classes 0 mod p (p | L), L = 24*5*7*11 = 9240, W = 3 (rough
primes 5, 7, 11).  "Arity" k = max number of rough primes per modulus of
V_D (a stand-in for the level).

(1) Lemma 1.1: LP min E_U nu over V_D (nu >= 0, >= 1 on A); extract the
    dual multipliers mu, check stationarity A^T mu = c and mu(A) = m*,
    put pi = mu|_A / mu(A), and check by a second LP that
    max{E_pi f : f in V_D, f >= 0, E_U f = 1} <= 1/m*.
(2) Lemma 2.2 + Theorem 2.4 (type (i), Q0 = 1): rows sqrt(w) e(n theta),
    theta Farey with denominators of arity <= k/2; Delta = top eigenvalue
    of the Gram matrix on an interval of length N (shift-invariant for
    additive rows); check N E_U|sum c phi|^2 <= Delta |c|^2 for random c,
    and Rtilde(pi)/E_pi|psi|^2 <= Delta/(N m*) for random twists |psi| >= 1.
(3) Lemma 4.1 + Theorem 4.2: random kernels (moduli of arity <= k/2),
    w~_theta <= h + (W-h)/N exactly; D* by QP; B >= (N/2) m*/(1+Nh/(W-h)).
(4) Theorem 4.3 proof steps on the exact plain sequential law sigma:
    chi^2_l(sigma) <= E[p/(1-p) 1_light], conditioning inequality,
    base marginals chi^2 = 7 (mod 8), 2 (mod 3).

Run (2 cores): OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 PYTHONPATH=scripts uv run --with cvxpy --with scipy --with numpy --with sympy \
        python scripts/largesieve2_checks.py
"""
import cmath
import itertools
import math
import random

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from sympy import divisors, factorint

BIG = [5, 7, 11]
SMALL = 24
L = SMALL * math.prod(BIG)
random.seed(20261005)
np.random.seed(20261005)


def toy_family():
    cls = set()
    for M in divisors(L):
        if M % 4 == 3:
            A = (M + 1) // 4
            for D in divisors(A * A):
                cls.add(((-4 * D) % M, M))
    for G in divisors(L):
        if G % 4:
            continue
        for g in divisors(G // 4):
            a = G // (4 * g)
            f = factorint(g)
            choices = [[p ** (2 * v - 1), p ** (2 * v)] for p, v in f.items()]
            for combo in itertools.product(*choices):
                D = math.prod(combo)
                cls.add(((-(4 * D + a)) % G, G))
        for h in divisors(G // 4):
            r = G // (4 * h)
            if any(e > 1 for e in factorint(r).values()):
                continue
            d = r * h * h
            for m in divisors(4 * d + 1):
                cls.add(((-pow(m, -1, G)) % G, G))
    for p in [2, 3] + BIG:
        cls.add((0, p))
    return cls


def avoider(cls):
    hit = np.zeros(L, dtype=bool)
    for b, G in cls:
        hit[b::G] = True
    return ~hit


def moduli(k):
    """divisors d of L with W-smooth part 24 and <= k rough primes."""
    out = []
    for j in range(k + 1):
        for S in itertools.combinations(BIG, j):
            out.append(SMALL * math.prod(S))
    return out


def basis(mods):
    rows, cols, c = [], [], []
    for d in mods:
        for b in range(d):
            j = len(c)
            mem = list(range(b, L, d))
            rows += mem
            cols += [j] * len(mem)
            c.append(len(mem) / L)
    A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(L, len(c))).tocsr()
    return A, np.array(c)


def check1(avoid, k):
    A, c = basis(moduli(k))
    lo = avoid.astype(float)
    res = linprog(c, A_ub=-A, b_ub=-lo, bounds=(None, None), method="highs")
    assert res.status == 0, res.message
    m = res.fun
    mu = -res.ineqlin.marginals
    assert mu.min() > -1e-9
    stat = np.abs(A.T @ mu - c).max()
    assert stat < 1e-8, stat
    assert abs(mu[avoid].sum() - m) < 1e-8
    pi = np.where(avoid, np.maximum(mu, 0), 0.0)
    pi /= pi.sum()
    # second LP: max E_pi f, f = A x >= 0, E_U f = c.x = 1
    res2 = linprog(-(A.T @ pi), A_ub=-A, b_ub=np.zeros(L), A_eq=c[None, :], b_eq=[1.0],
                   bounds=(None, None), method="highs")
    assert res2.status == 0, res2.message
    val = -res2.fun
    assert val <= 1 / m * (1 + 1e-7) + 1e-9, (val, 1 / m)
    print(f"(1) k={k}: |A mod L|={int(avoid.sum())}, m*={m:.6g} (log 1/m* = {math.log(1/m):.3f}), "
          f"stationarity {stat:.1e}, max E_pi f / E_U f = {val:.6g} <= 1/m* = {1/m:.6g}")
    return m, pi


def farey(mods):
    th = set()
    for d in mods:
        for a in range(d):
            g = math.gcd(a, d)
            th.add((a // g, d // g))
    return sorted(th)


def check2(pi, m, k, N):
    mods = moduli(k // 2)
    TH = farey(mods)
    J = len(TH)
    w = np.array([random.uniform(0.2, 1.0) for _ in TH])
    ns = np.arange(N)
    E = np.array([[cmath.exp(2j * math.pi * n * a / d) for n in ns] for a, d in TH])  # J x N
    Phi = np.sqrt(w)[:, None] * E
    G = Phi @ Phi.conj().T
    Delta = np.linalg.eigvalsh(G).max()
    nn = np.arange(L)
    Efull = np.array([np.exp(2j * np.pi * nn * a / d) for a, d in TH])  # J x L
    PhiL = np.sqrt(w)[:, None] * Efull
    worst2 = 0.0
    for _ in range(20):
        cc = np.random.randn(J) + 1j * np.random.randn(J)
        H = cc @ PhiL
        r = N * np.mean(np.abs(H) ** 2) / (Delta * np.vdot(cc, cc).real)
        worst2 = max(worst2, r)
    assert worst2 <= 1 + 1e-9
    worst = 0.0
    for _ in range(20):
        psi = np.exp(2j * np.pi * np.random.rand(L)) * (1 + 2 * np.random.rand(L))
        num = np.sum(np.abs(PhiL.conj() @ (pi * psi)) ** 2)
        den = np.sum(pi * np.abs(psi) ** 2)
        r = (num / den) / (Delta / (N * m))
        worst = max(worst, r)
    assert worst <= 1 + 1e-9
    print(f"(2) k={k}, N={N}, J={J} rows: Delta={Delta:.4g}; max N E|H|^2/(Delta|c|^2) = {worst2:.4f} <= 1; "
          f"max [Rt(pi)/E|psi|^2]/[Delta/(N m*)] = {worst:.4f} <= 1")


def check3(avoid, m, k, N, trials=6):
    import cvxpy as cp
    mods = [d for d in divisors(L) if sum(1 for p in BIG if d % p == 0) <= k // 2 and d > 1]
    pts = np.flatnonzero(avoid)
    out = []
    for t in range(trials):
        S = random.sample(mods, 8)
        w = {q: random.uniform(0.1, 2.0) for q in S}
        K = lambda mm: sum(wq for q, wq in w.items() if mm % q == 0)
        W = K(0)
        h = max(K(mm) for mm in range(1, N))
        # w~ on all theta with den | some q
        wt = {}
        for q, wq in w.items():
            for a in range(q):
                g = math.gcd(a, q)
                key = (a // g, q // g)
                wt[key] = wt.get(key, 0.0) + wq / q
        assert max(wt.values()) <= h + (W - h) / N + 1e-12
        x = cp.Variable(len(pts), nonneg=True)
        obj = 0
        for q, wq in w.items():
            P = coo_matrix((np.ones(len(pts)), (pts % q, np.arange(len(pts)))), shape=(q, len(pts)))
            obj = obj + wq * cp.sum_squares(P @ x)
        prob = cp.Problem(cp.Minimize(obj), [cp.sum(x) == 1])
        prob.solve()
        Dstar = prob.value
        if Dstar <= h + 1e-9:
            out.append(f"no bound (D*={Dstar:.3g} <= h={h:.3g})")
            continue
        B = (W - h) / (Dstar - h)
        lower = (N / 2) * m / (1 + N * h / (W - h))
        assert B >= lower * (1 - 1e-6), (B, lower)
        out.append(f"B={B:.3g} >= {lower:.3g}")
    print(f"(3) kernels (N={N}): w~ <= h+(W-h)/N in all {trials}; " + "; ".join(out))


def check4(cls):
    """exact plain sequential law: base unit squares mod 24 (= 1 mod 24), then 5, 7, 11."""
    sigma = np.zeros(L)
    # state: distribution over n mod 24*prod(lower primes); build iteratively
    mod = SMALL
    dist = {1: 1.0}  # unit squares mod 8 = {1}, mod 3 = {1}
    for b, G in cls:  # base avoids every W-smooth class (K2 Lemma 2.3)
        if SMALL % G == 0:
            assert (1 - b) % G != 0
    stats = []
    for ell in BIG:
        # classes with top prime ell
        top = [(b, G) for b, G in cls if G % ell == 0 and all(G % p for p in BIG if p > ell)]
        new = {}
        Ep = Elight = 0.0
        marg = np.zeros(ell)
        for x, pr in dist.items():
            F = set()
            for b, G in top:
                q = G // ell  # cofactor; its primes are < ell or W-smooth, so q | mod
                assert mod % q == 0
                if (x - b) % q == 0:
                    F.add(b % ell)
            p = len(F) / ell
            Ep += pr * p
            light = p <= ell ** -0.5
            if light:
                Elight += pr * p / (1 - p)
                allowed = [r for r in range(ell) if r not in F]
            else:
                allowed = list(range(ell))
            for r in allowed:
                y = next(z for z in range(x, mod * ell, mod) if z % ell == r)
                new[y] = new.get(y, 0.0) + pr / len(allowed)
                marg[r] += pr / len(allowed)
        chi2 = ell * np.sum(marg ** 2) - 1
        assert chi2 <= Elight + 1e-12, (ell, chi2, Elight)
        stats.append((ell, chi2, Elight, Ep))
        dist, mod = new, mod * ell
    assert mod == L
    for x, pr in dist.items():
        sigma[x] = pr
    avoid = avoider(cls)
    leak = sigma[~avoid].sum()
    pi = np.where(avoid, sigma, 0.0)
    pi /= pi.sum()
    rows = []
    for q in [8, 3] + BIG:
        ms = np.bincount(np.arange(L) % q, weights=sigma, minlength=q)
        mp = np.bincount(np.arange(L) % q, weights=pi, minlength=q)
        c_s = q * np.sum(ms ** 2) - 1
        c_p = q * np.sum(mp ** 2) - 1
        assert 1 + c_p <= (1 + c_s) / (1 - leak) ** 2 + 1e-12
        rows.append(f"q={q}: chi2(sigma)={c_s:.4f}, chi2(pi)={c_p:.4f}")
    print(f"(4) |family|={len(cls)}, sigma exact: leak={leak:.4f}; per prime (l, chi2_l(sigma), E[p/(1-p);light], E p): "
          + ", ".join(f"({a},{b:.4f},{c:.4f},{d:.4f})" for a, b, c, d in stats))
    print("    " + "; ".join(rows) + "  [base: 7 at q=8, 2 at q=3]")


def check5():
    """Section 8: band family. (a) LP: level-lambda majorants (each term sees at most one
    prime of each pair) have mean >= 1; (b) Lemma 8.3's polynomial: P >= 1 on J, int P^2 <= 1 - eta/3."""
    pairs = [(5, 7), (11, 13)]
    Mp = math.prod(a * b for a, b in pairs)
    for eta in (1 / 8, 1 / 9):
        avoid = np.ones(Mp, dtype=bool)
        n = np.arange(Mp)
        for (l1, l2), a in zip(pairs, (2, 3)):
            D = l1 * l2
            ph = (n * a % D) / D
            dist = np.abs(ph - np.round(ph))
            avoid &= dist <= 0.5 - eta
        # moduli: products of at most one prime from each pair
        mods = []
        for c1 in (1, 5, 7):
            for c2 in (1, 11, 13):
                mods.append(c1 * c2)
        rows, cols, c = [], [], []
        for d in mods:
            for b in range(d):
                j = len(c)
                mem = list(range(b, Mp, d))
                rows += mem
                cols += [j] * len(mem)
                c.append(len(mem) / Mp)
        A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(Mp, len(c))).tocsr()
        res = linprog(np.array(c), A_ub=-A, b_ub=-avoid.astype(float), bounds=(None, None), method="highs")
        assert res.status == 0 and res.fun >= 1 - 1e-9, res.fun
        R = math.ceil(4 / eta ** 2)
        t = np.linspace(0, 1, 200001)
        # G = I * F_R in Fourier: I^(m) = e(-m/2) sin(pi m eta)/(pi m), F_R^(m) = 1 - |m|/(R+1)
        m = np.arange(-R, R + 1)
        Ihat = np.where(m == 0, eta, np.sin(np.pi * m * eta) / (np.pi * np.where(m == 0, 1, m))) * np.cos(np.pi * m)
        Ghat = Ihat * (1 - np.abs(m) / (R + 1))
        chat = -Ghat
        chat[R] += 1 + eta / 4
        # evaluate P on a grid in chunks (memory-bounded)
        Pmin = np.inf
        for k0 in range(0, len(t), 20000):
            tt = t[k0:k0 + 20000]
            vals = np.cos(2 * np.pi * np.outer(tt, m)) @ chat  # chat real and even
            Jmask = np.abs(tt - 0.5) >= eta
            if Jmask.any():
                Pmin = min(Pmin, vals[Jmask].min())
        l2 = float(np.sum(chat ** 2))
        assert Pmin >= 1 - 1e-9 and l2 <= 1 - eta / 3
        print(f"(5) band family eta={eta:.4f}: |A mod {Mp}|={int(avoid.sum())} "
              f"(density {avoid.mean():.3f}); level-lambda majorant LP min = {res.fun:.6f} >= 1; "
              f"Lemma 8.3: R={R}, min_J P = {Pmin:.4f} >= 1, int P^2 = {l2:.4f} <= 1-eta/3 = {1-eta/3:.4f}")


def main():
    cls = toy_family()
    avoid = avoider(cls)
    res = {}
    for k in (0, 2):
        res[k] = check1(avoid, k)
    m2, pi2 = res[2]
    check2(pi2, m2, 2, N=60)
    check3(avoid, m2, 2, N=40)
    check4(cls)  # full toy family: every rough prime heavy (degenerate)
    for keep in (0.05, 0.1, 0.2):
        thin = {C for C in cls if SMALL % C[1] == 0 or random.random() < keep}
        check4(thin)
    check5()


if __name__ == "__main__":
    main()
