"""R64 from-scratch check of Lemma 10.1 (planting) and Lemma 12.1 (pseudorandomness).
Bits b_i ~ Bern(p_i) independent; planted law nu = nu0 + P0 sum_{|J|=k+1} w_J sigma_J.
Big coordinates X_i uniform on Z_m, Omega_i a subset of size s_i (p_i = s_i/m).
We compute E_nu h for random reduced products h = prod h_i(X_i) (|h_i|<=1, |E h_i|<=1/4)
by summing over all bit patterns (independent of the telescoping identity in the paper)
and compare with E h = prod E h_i.  Checks: nu>=0, nu(b=0)=0, k-wise marginals exact,
|E_rho h| <= (4 r*)^{k+1}, E_rho h = 0 if |I|<=k."""
import itertools, random, math
import numpy as np
rng = np.random.default_rng(1)

def planted(p, k):
    N = len(p); r = [q / (1 - q) for q in p]
    P0 = math.prod(1 - q for q in p)
    pats = list(itertools.product([0, 1], repeat=N))
    nu0 = {y: math.prod(p[i] if y[i] else 1 - p[i] for i in range(N)) for y in pats}
    e = sum(math.prod(r[i] for i in J) for J in itertools.combinations(range(N), k + 1))
    nu = dict(nu0)
    for J in itertools.combinations(range(N), k + 1):
        wJ = math.prod(r[i] for i in J) / e
        for sz in range(len(J) + 1):
            for y in itertools.combinations(J, sz):
                pat = tuple(1 if i in y else 0 for i in range(N))
                nu[pat] += P0 * wJ * (-1) ** (sz + 1)
    return nu, nu0, r

def run(m, sizes, k, trials=200):
    N = len(sizes); p = [s / m for s in sizes]
    nu, nu0, r = planted(p, k); rstar = max(r); R = sum(r)
    assert R >= (k + 1) + (2 * k + 1) * rstar, (R, k, rstar)
    assert min(nu.values()) > -1e-12, min(nu.values())
    assert abs(nu[tuple([0] * N)]) < 1e-12
    assert abs(sum(nu.values()) - 1) < 1e-12
    # k-wise marginals of bits
    Yp = np.array(list(nu.keys())); dv = np.array([nu[y] - nu0[y] for y in nu.keys()])
    for K in itertools.combinations(range(N), min(k, N)):
        for z in itertools.product([0, 1], repeat=len(K)):
            mask = np.all(Yp[:, list(K)] == np.array(z)[None, :], axis=1)
            assert abs(dv[mask].sum()) < 1e-12
    worst = 0.0
    pats = list(nu.keys()); w = np.array([nu[y] - nu0[y] for y in pats])
    Y = np.array(pats)
    for t in range(trials):
        size = rng.integers(1, N + 1)
        I = sorted(rng.choice(N, size=size, replace=False))
        beta = np.ones(N, complex); gam = np.ones(N, complex)
        for i in I:
            while True:
                h = rng.uniform(0, 1, m) * np.exp(2j * np.pi * rng.uniform(0, 1, m))
                if t % 3 == 0:  # additive-character-like
                    a = rng.integers(1, m); h = np.exp(2j * np.pi * a * np.arange(m) / m)
                if abs(h.mean()) <= 0.25: break
            perm = rng.permutation(m); Om = perm[:sizes[i]]; Co = perm[sizes[i]:]
            beta[i] = h[Om].mean(); gam[i] = h[Co].mean()
        # E_rho h = sum_patterns rho(y) prod_i (beta_i if y_i else gam_i)
        fac = np.where(Y == 1, beta[None, :], gam[None, :]).prod(axis=1)
        Erho = abs((w * fac).sum())
        if len(I) <= k: assert Erho < 1e-12, Erho
        bound = (4 * rstar) ** (k + 1)
        assert Erho <= bound + 1e-12, (Erho, bound)
        worst = max(worst, Erho / bound)
    print(f"m={m} sizes={sizes} k={k} R={R:.3f} r*={rstar:.3f} ok; max |E_rho h|/(4r*)^(k+1) = {worst:.3e}")

run(12, [2] * 14, 1)
run(12, [2] * 16, 1)
run(14, [2] * 14 + [1] * 4, 1)
run(10, [2] * 17, 2, trials=60)  # 4r*=1: only the vanishing for |I|<=k is informative
