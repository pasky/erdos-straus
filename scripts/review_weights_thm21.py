"""R81 from-scratch check of EXCEPTIONAL_WEIGHTS Thm 2.1, Lemma 2.0, Lemma 1.2.

For a periodic set A subset Z/Q we compute
  * M(L) = max_t #(A cap (t,t+L])                       (sliding window)
  * the Selberg majorant Phi_K of 1_[0,1] (Beurling function), checks
    Phi>=0, Phi>=1 on [0,1], int Phi = 1+1/K, and W_N(j/Q) (folded sum + FFT)
  * DUAL value  D = max <g,1_A>, g>=0, |Q ghat(j)| <= |W_N(j/Q)|
    bracketed by inner/outer polygon LPs (Lemma 1.2's right side)
  * PRIMAL value P = min sum_j |W_N(j/Q)| |nuhat(j)| over nu >= 1_A
    bracketed by polygon LPs (Lemma 1.2's left side), on small Q
  * RELAX = max <g,1_A> with only: g>=0, spectrum in ||theta||<=K/N, sum g <= N(1+1/K)
    (what the proof of Thm 2.1 actually uses) and checks
        M(N) <= D <= RELAX <= 12(K+1) M(ceil(N/K)).
No code from the author's scripts is used.
"""
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.special import polygamma

rng = np.random.default_rng(81)


def beurling(z):
    z = np.asarray(z, float)
    out = np.empty_like(z)
    s2 = (np.sin(np.pi * z) / np.pi) ** 2
    pos = z > 0
    neg = z < 0
    zero = z == 0
    zp = z[pos]
    out[pos] = 1 + s2[pos] * (2 / zp - 2 * polygamma(1, 1 + zp))
    zn = z[neg]
    out[neg] = -1 + s2[neg] * (2 * polygamma(1, -zn) + 2 / zn)
    out[zero] = 1.0
    return out


def selberg_phi(x, K):
    return 0.5 * (beurling(K * x) + beurling(K * (1 - x)))


def check_phi(K):
    x = np.linspace(-200, 200, 4_000_001)
    ph = selberg_phi(x, K)
    dx = x[1] - x[0]
    integ = ph.sum() * dx
    # tail beyond |x|>200 ~ 2*int 1/(2 pi^2 K^2 x^2) = 1/(pi^2 K^2 200)
    integ += 1 / (np.pi ** 2 * K ** 2 * 200)
    inside = (x >= 0) & (x <= 1)
    return ph.min(), ph[inside].min(), integ


def W_folded(N, K, Q, T=400_000):
    """W_N(j/Q) for j mod Q, via sum over |n|<=T*... folded mod Q then FFT.
    W_N(theta) = sum_n Phi(n/N) e(n theta)."""
    n = np.arange(-T, T + 1)
    vals = selberg_phi(n / N, K)
    folded = np.bincount(n % Q, weights=vals, minlength=Q)
    # sum_r folded[r] e(j r/Q) = Q * ifft
    W = np.fft.ifft(folded) * Q
    return W


def window_max(A, L):
    Q = len(A)
    ext = np.concatenate([A, A[: L + Q]]) if L <= Q else np.tile(A, L // Q + 3)
    cs = np.concatenate([[0], np.cumsum(ext)])
    return int(max(cs[t + L] - cs[t] for t in range(Q)))


def dual_lp(A, wabs, m=16, inner=False, band=None):
    """max <g,1_A> s.t. g>=0, |Q ghat(j)| <= wabs[j] (polygon approx).
    Variables: c0, (a_j,b_j) j=1..J where support = j with wabs>0 (or band)."""
    Q = len(A)
    js = [j for j in range(1, Q // 2 + 1) if (wabs[j] > 1e-9 if band is None else band[j])]
    nvar = 1 + 2 * len(js)
    n = np.arange(Q)
    # g(n) = (1/Q)[c0 + sum_j mult_j (a_j cos - b_j sin)], mult=2 except j=Q/2
    G = np.zeros((Q, nvar))
    G[:, 0] = 1.0 / Q
    for k, j in enumerate(js):
        mult = 1.0 if (2 * j == Q) else 2.0
        G[:, 1 + 2 * k] = mult * np.cos(2 * np.pi * j * n / Q) / Q
        G[:, 2 + 2 * k] = -mult * np.sin(2 * np.pi * j * n / Q) / Q
    c = -(A @ G)
    A_ub = [-G]
    b_ub = [np.zeros(Q)]
    bounds = [(0, wabs[0])] + [(None, None)] * (2 * len(js))
    fac = np.cos(np.pi / m) if inner else 1.0
    phis = 2 * np.pi * np.arange(m) / m
    for k, j in enumerate(js):
        if 2 * j == Q:  # real coefficient
            bounds[2 + 2 * k] = (0, 0)
            bounds[1 + 2 * k] = (-wabs[j] * fac, wabs[j] * fac)
            continue
        rows = np.zeros((m, nvar))
        rows[:, 1 + 2 * k] = np.cos(phis)
        rows[:, 2 + 2 * k] = np.sin(phis)
        A_ub.append(rows)
        b_ub.append(np.full(m, wabs[j] * fac))
    res = linprog(c, A_ub=np.vstack(A_ub), b_ub=np.concatenate(b_ub), bounds=bounds, method="highs")
    assert res.status == 0, res.message
    return -res.fun


def primal_lp(A, wabs, m=16, inner=False):
    """min sum_j wabs[j]|nuhat(j)| over nu>=1_A (polygon approx of |.|).
    outer polygon constraints t>=Re(z e^{-i phi}) give t >= |z|cos(pi/m) (lower bound on P);
    rescaling by 1/cos(pi/m) gives an upper bound."""
    Q = len(A)
    n = np.arange(Q)
    js = [j for j in range(0, Q // 2 + 1) if wabs[j] > 1e-9]
    nvar = Q + len(js)
    c = np.zeros(nvar)
    phis = 2 * np.pi * np.arange(m) / m
    A_ub, b_ub = [], []
    for k, j in enumerate(js):
        mult = 1.0 if (j == 0 or 2 * j == Q) else 2.0
        c[Q + k] = mult * wabs[j]
        # nuhat(j) = (1/Q) sum nu(n) e(-jn/Q); Re(nuhat e^{-i phi}) = (1/Q) sum nu cos(2pi j n/Q + phi)
        for ph in phis:
            row = np.zeros(nvar)
            row[:Q] = np.cos(2 * np.pi * j * n / Q + ph) / Q
            row[Q + k] = -1
            A_ub.append(row)
            b_ub.append(0.0)
    bounds = [(1, None) if A[i] else (0, None) for i in range(Q)] + [(0, None)] * len(js)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds, method="highs")
    assert res.status == 0, res.message
    lo = res.fun
    return lo, lo / np.cos(np.pi / m)


def relax_lp(A, N, K):
    Q = len(A)
    band = np.zeros(Q // 2 + 1, bool)
    for j in range(1, Q // 2 + 1):
        band[j] = j / Q <= K / N + 1e-12
    wabs = np.full(Q // 2 + 1, 1e9)
    wabs[0] = N * (1 + 1 / K)
    # no modulus constraint on in-band coefficients except via g>=0 (huge cap)
    return dual_lp(A, wabs, band=band)


def families(Q, rng):
    fam = {}
    fam["random_p0.3"] = (rng.random(Q) < 0.3).astype(float)
    fam["random_p0.05"] = (rng.random(Q) < 0.05).astype(float)
    B = np.zeros(Q); B[: Q // 5] = 1; fam["one_block"] = B
    B = np.zeros(Q); B[::7] = 1; fam["AP_step7"] = B
    B = np.zeros(Q); B[0] = 1; fam["single_point"] = B
    return fam


def main():
    out = []
    for K in (1, 2, 3):
        mn, mn01, integ = check_phi(K)
        out.append(f"K={K}: min Phi={mn:.3e}  min_[0,1] Phi={mn01:.6f}  int Phi={integ:.5f} (1+1/K={1+1/K:.5f})")
    print("\n".join(out)); out = []
    worst_ratio = 0
    for (Q, N, K) in [(60, 12, 1), (90, 16, 2), (120, 24, 2), (150, 20, 3), (210, 30, 2), (240, 40, 4)]:
        W = W_folded(N, K, Q)
        wabs = np.abs(W[: Q // 2 + 1])
        # Lemma 2.0 checks
        offband = [wabs[j] for j in range(Q // 2 + 1) if j / Q > K / N + 1e-12]
        print(f"Q={Q} N={N} K={K}: W(0)={W[0].real:.4f} vs N(1+1/K)={N*(1+1/K):.4f}; max offband |W|={max(offband) if offband else 0:.2e}; max|W|/W(0)={wabs.max()/W[0].real:.4f}")
        wabs_c = wabs.copy()
        for j in range(Q // 2 + 1):
            if j / Q > K / N + 1e-12:
                wabs_c[j] = 0.0
        for name, A in families(Q, rng).items():
            if A.sum() == 0:
                continue
            MN = window_max(A, N)
            ML = window_max(A, -(-N // K))
            Dlo = dual_lp(A, wabs_c, inner=True)
            Dhi = dual_lp(A, wabs_c, inner=False)
            R = relax_lp(A, N, K)
            bound = 12 * (K + 1) * ML
            ok = (MN <= Dhi + 1e-6) and (Dlo <= R + 1e-6) and (R <= bound + 1e-6)
            worst_ratio = max(worst_ratio, R / bound)
            line = f"  {name:14s} M(N)={MN:3d} D in [{Dlo:8.3f},{Dhi:8.3f}] RELAX={R:8.3f} 12(K+1)M(L)={bound:5d} D/M(N)={Dlo/MN:6.3f} {'OK' if ok else 'FAIL'}"
            print(line)
            if Q <= 90:
                Plo, Phi_ = primal_lp(A, wabs_c)
                print(f"      Lemma1.2 primal P in [{Plo:8.3f},{Phi_:8.3f}]  dual D in [{Dlo:8.3f},{Dhi:8.3f}]  overlap={'yes' if Plo <= Dhi + 1e-6 and Dlo <= Phi_ + 1e-6 else 'NO'}")
    print(f"max RELAX/(12(K+1)M(L)) = {worst_ratio:.4f}")


if __name__ == "__main__":
    main()
