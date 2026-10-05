"""R27 from-scratch checks of LARGESIEVE2 Lemma 1.1, Lemma 2.2/Thm 2.4 type (i)
(additive Farey rows AND multiplicative character rows, with twists),
Lemma 4.1 and the Thm 4.2 inequality chain, on random toy avoider sets.

Independent of scripts/largesieve2_checks.py.  Toy: M' = 2*3*5*7*11 = 2310,
A = complement of random union of classes mod divisors of M'.
"Level" stand-in: number of primes in {5,7,11} dividing d (W = 3).
"""
import itertools, math, sys
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
PR = [2, 3, 5, 7, 11]
M = 2 * 3 * 5 * 7 * 11
divs = sorted({math.prod(c) for r in range(len(PR) + 1) for c in itertools.combinations(PR, r)})
divs = sorted(d for d in set(divs) if M % d == 0)
rough = [5, 7, 11]
def arity(d): return sum(d % p == 0 for p in rough)

n = np.arange(M)

def make_A():
    bad = np.zeros(M, bool)
    for _ in range(rng.integers(6, 14)):
        d = int(rng.choice([d for d in divs if d > 1]))
        bad |= (n % d) == rng.integers(d)
    # also forbid all non-squares-ish at 3 to mimic a base: keep it random
    return ~bad

def basis(Dset):
    cols = []
    for d in Dset:
        for b in range(d):
            cols.append(((n % d) == b).astype(float))
    return np.array(cols).T  # M x k

def lemma11(A, Dset):
    B = basis(Dset)                      # nu = B @ a, a free
    c = B.mean(axis=0)                   # E_U nu
    # constraints: nu(x) >= 1_A(x)  ->  -B a <= -1_A
    res = linprog(c, A_ub=-B, b_ub=-A.astype(float), bounds=[(None, None)] * B.shape[1],
                  method="highs")
    assert res.status == 0, res.message
    mstar = res.fun
    mu = -res.ineqlin.marginals          # >= 0
    stat = np.abs(B.T @ mu - c).max()    # sum_x mu(x) nu(x) = E_U nu
    assert mu.min() > -1e-9
    pi = np.where(A, mu, 0.0); pi /= pi.sum()
    # second LP: max E_pi f, f in V, f>=0, E_U f = 1   (should be <= 1/m*)
    res2 = linprog(-(B.T @ pi), A_ub=-B, b_ub=np.zeros(M), A_eq=c[None, :], b_eq=[1.0],
                   bounds=[(None, None)] * B.shape[1], method="highs")
    assert res2.status == 0
    return mstar, mu, pi, stat, abs(mu.sum() - 1), abs(mu[A].sum() - mstar), -res2.fun

def run():
    out = []
    for trial in range(4):
        A = make_A()
        if A.sum() == 0: continue
        for k in (0, 1, 2):
            Dset = [d for d in divs if arity(d) <= k]
            mstar, mu, pi, stat, musum, mua, sup = lemma11(A, Dset)
            out.append(f"L1.1 trial{trial} k={k} dens={A.mean():.3f} m*={mstar:.4f} "
                       f"stat={stat:.1e} |mu|-1={musum:.1e} mu(A)-m*={mua:.1e} "
                       f"supp_offA={pi[~A].sum():.1e} maxE_pi f={sup:.4f} 1/m*={1/mstar:.4f}")
            assert stat < 1e-8 and sup <= 1 / mstar * (1 + 1e-7)
            if k == 1:
                # ---- Thm 2.4 type (i): rows of arity <= ... need lcm of rows in D (arity<=1 rows -> lcm arity<=2)
                # use pi from k=2 LP for rows of arity<=1
                pass
        # rows: additive Farey e(a n/q), q | M with arity(q)<=1 ; multiplicative chars mod q
        Dset2 = [d for d in divs if arity(d) <= 2]
        mstar2, _, pi2, *_ = lemma11(A, Dset2)
        qs = [q for q in divs if arity(q) <= 1 and q > 1]
        N = 60
        for kind in ("additive", "multiplicative"):
            rows = []
            for q in qs:
                if kind == "additive":
                    for a in range(q):
                        if math.gcd(a, q) == 1:
                            rows.append(np.exp(2j * np.pi * a * n / q))
                else:
                    # all characters mod q via discrete log on (Z/q)^* (brute force)
                    units = [u for u in range(q) if math.gcd(u, q) == 1]
                    G = len(units)
                    # build character table by finding generators of the group via Smith-free approach:
                    # characters = homomorphisms; enumerate via eigenvectors of regular rep (small q)
                    idx = {u: i for i, u in enumerate(units)}
                    mats = []
                    for g in units:
                        P = np.zeros((G, G))
                        for u in units: P[idx[(g * u) % q], idx[u]] = 1
                        mats.append(P)
                    # characters: simultaneous eigvecs; random combo of commuting perms
                    Z = sum(rng.normal() * P for P in mats)
                    w, V = np.linalg.eig(Z)
                    for col in range(G):
                        v = V[:, col] / V[idx[1], col]
                        chi = np.zeros(q, complex)
                        for u in units: chi[u] = v[idx[u]]
                        rows.append(chi[n % q] * math.sqrt(q / max(1, sum(1 for u in units))))
            R = np.array(rows)            # J x M
            # Delta: largest eigenvalue of Gram over an interval of length N (exact for these rows,
            # translate-invariant in law; check a few translates and take max)
            Delta = 0
            for t in range(M):
                idxs = (t + np.arange(N)) % M
                S = R[:, idxs]
                Delta = max(Delta, np.linalg.norm(S, 2) ** 2)
            # Lemma 2.2: N E_U |sum c_j phi_j|^2 <= Delta ||c||^2 ; random c
            worst22 = 0
            for _ in range(20):
                cvec = rng.normal(size=len(rows)) + 1j * rng.normal(size=len(rows))
                worst22 = max(worst22, N * np.mean(np.abs(cvec @ R) ** 2) / (Delta * np.vdot(cvec, cvec).real))
            # Thm 2.4 type (i): Rtilde(pi)/E_pi|psi|^2 <= Delta/(N m*) ; random twists |psi|>=1
            worst24 = 0
            for _ in range(20):
                per = int(rng.choice(divs))
                psi_base = (1 + 2 * rng.random(per)) * np.exp(2j * np.pi * rng.random(per))
                psi = psi_base[n % per]
                Rt = np.sum(np.abs(R.conj() @ (pi2 * psi)) ** 2)
                Epsi = np.sum(pi2 * np.abs(psi) ** 2)
                worst24 = max(worst24, (Rt / Epsi) / (Delta / (N * mstar2)))
            out.append(f"T2.4 trial{trial} {kind} rows={len(rows)} Delta={Delta:.2f} "
                       f"L2.2 ratio={worst22:.4f} T2.4 ratio={worst24:.4f}")
            assert worst22 <= 1 + 1e-9 and worst24 <= 1 + 1e-9
        # ---- Lemma 4.1 and Thm 4.2 chain: kernel on S = divisors of arity<=1
        for _ in range(3):
            S = [q for q in divs if arity(q) <= 1]
            w = {q: rng.random() * (rng.random() < 0.6) for q in S}
            N = 40
            K = lambda m: sum(wq for q, wq in w.items() if m % q == 0)
            WK = K(0); h = max(K(m) for m in range(1, N))
            # wtilde_theta for theta = a/M
            wt = np.zeros(M)
            for q, wq in w.items():
                step = M // q
                wt[::step] += wq / q
            assert np.all(wt <= h + (WK - h) / N + 1e-12), "Lemma 4.1 fails"
            # D(pi)-D_u = sum_{theta != 0} wt |pihat|^2 <= (1/m*) max_{theta!=0} wt
            pihat = np.fft.fft(pi2)       # pihat[k] = sum pi(x) e(-kx/M)
            lhs = np.sum(wt[1:] * np.abs(pihat[1:]) ** 2)
            # direct D(pi) from collisions
            D = sum(wq * sum(pi2[(n % q) == b].sum() ** 2 for b in range(q)) for q, wq in w.items())
            Du = sum(wq / q for q, wq in w.items())
            rhs = wt[1:].max() / mstar2
            out.append(f"L4.1/T4.2 trial{trial} max wt={wt.max():.4f} bound={h+(WK-h)/N:.4f} "
                       f"D-Du={D-Du:.5f} fourier={lhs:.5f} <= {rhs:.5f}")
            assert abs((D - Du) - lhs) < 1e-9 and lhs <= rhs + 1e-12
    print("\n".join(out))
    print("ALL ASSERTIONS PASSED")

run()
