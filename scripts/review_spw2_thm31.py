"""R53 from-scratch check of SPW2 Theorem 3.1 (K-free edge bound).
(1) Fejer kernel pointwise/tail bounds; (2) the Lipschitz constant
sum_{|k|<m0}|k| vs m0^2; (3) LP on Z/e with exactly the theorem's hypotheses
(profile mod d|e, d<=D; rho<=1-eta on W only), then every inequality of the
proof chain is verified on the optimiser and on random feasible points."""
import numpy as np, math, sys
from scipy.optimize import linprog

def fejer(e, M):
    x = np.arange(e)
    k = np.arange(-M, M+1)
    return ((1 - np.abs(k)/(M+1))[None, :]*np.cos(2*np.pi*np.outer(x, k)/e)).sum(1)/e

def cdist(x, e):
    x = np.mod(x, e); return np.minimum(x, e - x)

def check_kernel(e, M):
    K = fejer(e, M); t = cdist(np.arange(e), e)
    assert K.min() > -1e-12 and abs(K.sum() - 1) < 1e-9
    m = t >= 1
    assert np.all(K[m] <= e/(4*(M+1)*t[m]**2) + 1e-12)
    for a in range(2, e//2):
        assert K[t >= a].sum() <= e/(2*(M+1)*(a-1)) + 1e-12

def lp(N, C, e, M, obj=None, eta_fix=None):
    D = N//2; W = np.zeros(e, bool); W[[n % e for n in range(1, N+1)]] = True
    Aeq, beq = [], []
    for d in range(1, D+1):
        if e % d: continue
        for b in range(d):
            Aeq.append(np.r_[(np.arange(e) % d == b).astype(float), 0.0])
            beq.append(sum(1 for n in range(1, N+1) if n % d == b))
    Aub, bub = [], []
    for x in np.nonzero(W)[0]:
        row = np.zeros(e+1); row[x] = 1; row[e] = 1; Aub.append(row); bub.append(1.0)
    c = np.zeros(e+1); c[e] = -1
    bounds = [(0, None)]*e + [(eta_fix, eta_fix) if eta_fix is not None else (None, None)]
    if obj is not None: c = np.r_[obj, 0.0]
    r = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    assert r.status == 0, r.message
    return r.x[:e], r.x[e], W

def chain(N, C, e, M, rho, eta, W):
    D = N//2; m0 = e/D; K = fejer(e, M)
    f = rho - W
    T = np.real(np.fft.ifft(np.fft.fft(K)*np.fft.fft(f)))
    Th = np.fft.fft(T); kk = np.fft.fftfreq(e, 1/e)
    assert np.all(np.abs(Th[np.abs(kk) >= m0 - 1e-9]) < 1e-7), "Fourier support"
    assert np.all(np.abs(Th) <= 2*N + 1e-7)
    S = np.abs(kk[np.abs(kk) < m0]).sum()
    worst = 0.0
    phi = np.real(np.fft.ifft(np.fft.fft(K)*np.fft.fft(W.astype(float))))
    rmax = min(N - 1, (C - 1)*N - 1)/2
    r = 1
    while r < rmax:
        xin, xout = 1 + r, (-r) % e
        tau = e/(2*(M+1)*r); A = e*N/(4*(M+1)*r**2)
        assert phi[xin] >= 1 - tau - 1e-12 and phi[xout] <= tau + 1e-12
        assert T[xin] <= -eta + eta*tau + A + 1e-9 and T[xout] >= -tau - 1e-12
        lip_true = 4*math.pi*N*S/e**2
        assert abs(T[xout] - T[xin]) <= lip_true*(2*r+1) + 1e-9
        rhs = A + 2*tau + 4*math.pi*m0**2*N*(2*r+1)/e**2
        assert eta <= rhs + 1e-9
        worst = max(worst, abs(T[xout]-T[xin])/((2*r+1)*4*math.pi*N/e**2))
        r += 1
    return S, m0**2, worst

if __name__ == "__main__":
    for e, M in ((120, 6), (840, 8), (2520, 10), (420, 7)):
        check_kernel(e, M)
    print("Fejer pointwise and tail bounds OK")
    # Lipschitz constant: sum_{|k|<m0}|k| = m'(m'+1), m' = ceil(m0)-1, vs m0^2
    bad = [(m0, (math.ceil(m0)-1)*math.ceil(m0)) for m0 in np.arange(1.05, 8, 0.25) if (math.ceil(m0)-1)*math.ceil(m0) > m0**2]
    print("m0 with sum|k| > m0^2 (constant in (a)/(3.1) too small):", [(round(a,2), b) for a, b in bad][:6])
    rng = np.random.default_rng(1)
    for (N, C, e, M) in ((60, 1.5, 120, 6), (60, 2.0, 180, 6), (100, 1.5, 180, 6), (84, 2.0, 420, 7)):
        rho, eta, W = lp(N, C, e, M)
        S, m2, worst = chain(N, C, e, M, rho, eta, W)
        print(f"N={N} C={C} e={e} M={M} m0={e/(N//2):.2f}: LP eta*={eta:.4f}; sum|k|={S:.0f} vs m0^2={m2:.2f}; max |dT|/(unit Lip) = {worst:.2f}")
        for _ in range(5):
            rho2, _, _ = lp(N, C, e, M, obj=rng.normal(size=e), eta_fix=eta*rng.uniform(0, 1))
            chain(N, C, e, M, rho2, eta*0 + (1 - rho2[W].max()), W)
    print("proof chain verified on optimisers and random feasible points")
