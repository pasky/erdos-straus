"""Review diagnostics for EXCEPTIONAL_NONCRT §8.3 (scripts/noncrt_interval.py).
(1) tail mass beyond HCAP=80 dropped from the empirical and CRT laws; max H on [1,N];
(2) LP rerun with positivity on 0..HCAP2 (=200) and untruncated laws;
(3) cross-evaluation: E_int and E_CRT of the CRT-optimal P and of the interval-optimal P
    (the sign of Delta_N(nu) for a *fixed* nu = P(H)).
Run: uv run --with scipy python scripts/review_noncrt_interval.py N Y mode"""
import math, sys
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, "scripts")
from noncrt_interval import spf_sieve, divisors_of_square

def lp(w, k, hcap):
    hs = np.arange(hcap + 1); t = 2 * hs / hcap - 1
    B = np.polynomial.chebyshev.chebvander(t, k)
    c = w[:hcap + 1] @ B
    res = linprog(c, A_ub=np.vstack([-B, -B[0:1]]), b_ub=np.concatenate([np.zeros(hcap + 1), [-1.0]]),
                  bounds=[(None, None)] * (k + 1), method="highs")
    assert res.status == 0, res.message
    return res.fun, B @ res.x          # value, P on 0..hcap

def main(N, Y, mode, HC=200):
    M0 = 8 * ((N + 1) // 3) ** 2; Y = min(Y, M0)
    spf = spf_sieve((Y + 1) // 4 + 1)
    isp = np.ones(Y + 1, dtype=bool); isp[:2] = False
    for i in range(2, int(Y ** .5) + 1):
        if isp[i]: isp[i * i::i] = False
    H = np.zeros(N + 1, dtype=np.int64); pmf = np.zeros(HC + 1); pmf[0] = 1; lost = 0.0
    for l in np.nonzero(isp)[0]:
        l = int(l)
        if l % 4 != 3: continue
        F = {(-4 * d) % l for d in divisors_of_square((l + 1) // 4, spf)}
        p = len(F) / l
        lost += pmf[-1] * p
        pmf[1:] = pmf[1:] * (1 - p) + pmf[:-1] * p; pmf[0] *= 1 - p
        for r in F:
            if l <= N: H[r::l] += 1
            elif 1 <= r <= N: H[r] += 1
    nn = np.arange(N + 1)
    if mode == "all": sel = nn >= 1
    elif mode == "nonsquare": sel = (nn >= 1) & (np.round(np.sqrt(nn)) ** 2 != nn)
    else:
        sel = np.ones(N + 1, dtype=bool); sel[:2] = False
        for i in range(2, int(N ** .5) + 1):
            if sel[i]: sel[i * i::i] = False
    h = H[sel]
    print(f"N={N} Y={Y} {mode}: max H={h.max()}, frac H>80={np.mean(h > 80):.2e}, CRT mass beyond {HC}: {lost:.1e}, beyond 80: {pmf[81:].sum():.2e}")
    emp = np.bincount(h, minlength=HC + 1)[:HC + 1] / len(h)
    print("  k  int(HC=200)  CRT(HC=200) | E_int[P_crt]  E_crt[P_int]  (as -log)")
    for k in (2, 4, 6, 8, 10):
        vi, Pi = lp(emp, k, HC); vc, Pc = lp(pmf, k, HC)
        print(f"  {k:<2d} {-math.log(vi):9.4f}  {-math.log(vc):9.4f}   | {-math.log(emp @ Pc):9.4f}    {-math.log(pmf @ Pi):9.4f}")

main(int(sys.argv[1]), int(float(sys.argv[2])), sys.argv[3])
