"""Review O8 (reviewer 1): from-scratch checks of Lemma 3.1 (BRW sandwich),
the Efron-Stein truncation formula of Lemma 3.2 (c_W coefficients, M_1(u)),
the product-of-cells l1 inflation, and E[A_j e_j^2] = P(E_j) energy(F^(j);t).

Independent of scripts/omega8_*.py. Truncations are computed two ways:
(i) least-squares projection onto the span of all cell indicators on <=t
coordinates (no formula), (ii) the c_W formula of Lemma 3.2.
"""
import itertools, sys
import numpy as np

rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
TRIALS = int(sys.argv[1]) if len(sys.argv) > 1 else 30


def space(qs):
    return np.array(list(itertools.product(*[range(q) for q in qs])), dtype=int)


def proj_lstsq(phi, X, coords, qs, t):
    """Orthogonal (uniform measure) projection of phi onto functions that are
    sums of functions of <=t of the given coords."""
    cols = [np.ones(len(X))]
    for s in range(1, t + 1):
        for W in itertools.combinations(coords, s):
            for vals in itertools.product(*[range(qs[c]) for c in W]):
                cols.append(np.all(X[:, list(W)] == np.array(vals), axis=1).astype(float))
    A = np.array(cols).T
    coef, *_ = np.linalg.lstsq(A, phi, rcond=None)
    return A @ coef


def cond_exp(phi, X, W):
    if len(W) == 0:
        return np.full(len(X), phi.mean())
    keys = [tuple(r) for r in X[:, list(W)]]
    d = {}
    for k_, v in zip(keys, phi):
        d.setdefault(k_, []).append(v)
    m = {k_: np.mean(v) for k_, v in d.items()}
    return np.array([m[k_] for k_ in keys])


def trunc_formula(phi, X, coords, t):
    n = len(coords)
    u = np.zeros(len(X)); m1 = 0.0; maxc = 0
    for s in range(0, t + 1):
        c = sum((-1) ** i * comb(n - s, i) for i in range(0, t - s + 1))
        maxc = max(maxc, abs(c))
        for W in itertools.combinations(coords, s):
            u += c * cond_exp(phi, X, W)
            m1 += abs(c) * phi.mean()   # M_1(E[phi|X_W]) = E phi for phi>=0
    return u, m1, maxc


from math import comb


def trial():
    N = int(rng.integers(3, 6))
    qs = [int(rng.integers(2, 5)) for _ in range(N)]
    X = space(qs)
    k = int(rng.integers(1, 4))
    m = int(rng.integers(2, 9))
    events = []
    for _ in range(m):
        s = int(rng.integers(1, min(k, N) + 1))
        supp = tuple(sorted(rng.choice(N, s, replace=False).tolist()))
        vals = tuple(int(rng.integers(qs[c])) for c in supp)
        events.append((supp, vals))
    A = [np.all(X[:, list(s)] == np.array(v), axis=1).astype(float) for s, v in events]
    t = int(rng.integers(0, N))
    us, energies, out = [], [], {}
    Fprev = np.ones(len(X))
    Flist = []
    for j, (s, v) in enumerate(events):
        Flist.append(Fprev.copy())
        # F^(j): F_{<j} with X_s pinned to v; as a function of other coords,
        # extended constantly in the pinned coords.
        others = [c for c in range(N) if c not in s]
        mask = A[j] > 0
        sub = X[mask][:, others]
        lut = {tuple(r): f for r, f in zip(sub, Fprev[mask])}
        Fj = np.array([lut[tuple(r)] for r in X[:, others]])
        u1 = proj_lstsq(Fj, X, others, qs, min(t, len(others)))
        u2, m1, maxc = trunc_formula(Fj, X, others, min(t, len(others)))
        out['formula_err'] = max(out.get('formula_err', 0), np.abs(u1 - u2).max())
        out['m1_ratio'] = max(out.get('m1_ratio', 0), m1 / (N + 1) ** (2 * t) if t else m1)
        out['maxc_ratio'] = max(out.get('maxc_ratio', 0), maxc / (N + 1) ** t)
        us.append(u1)
        energies.append(np.mean((Fj - u1) ** 2))
        Fprev = Fprev * (1 - A[j])
    F = Fprev
    B = np.ones(len(X)); err = np.zeros(len(X))
    for i in range(m):
        v = sum((A[j] * us[j] for j in range(i)), np.zeros(len(X)))
        B -= A[i] * (1 - v) ** 2
        e = sum((A[j] * (Flist[j] - us[j]) for j in range(i)), np.zeros(len(X)))
        err += A[i] * e ** 2
    PE = [a.mean() for a in A]
    lhs = [np.mean(A[j] * (Flist[j] - us[j]) ** 2) for j in range(m)]
    out['maxBminusF'] = (B - F).max()
    out['identity'] = np.abs(F - B - err).max()
    out['AjEj_vs_Penergy'] = max(abs(lhs[j] - PE[j] * energies[j]) for j in range(m))
    out['bound_ok'] = np.mean(F - B) <= m ** 2 * sum(PE[j] * energies[j] for j in range(m)) + 1e-12
    return out


if __name__ == '__main__':
    worst = {}
    allok = True
    for _ in range(TRIALS):
        o = trial()
        for kk, vv in o.items():
            if kk == 'bound_ok':
                allok &= vv
            else:
                worst[kk] = max(worst.get(kk, -1e9), vv)
    print('trials', TRIALS, 'worst', worst, 'bound_ok_all', allok)
    bad = worst['maxBminusF'] > 1e-12 or worst['identity'] > 1e-9 or worst['formula_err'] > 1e-8 \
        or worst['AjEj_vs_Penergy'] > 1e-12 or worst['m1_ratio'] > 1 or worst['maxc_ratio'] > 1 or not allok
    sys.exit(1 if bad else 0)
