"""R27b from-scratch checks of LARGESIEVE2 Lemma 8.3 and Prop 8.4 / Thm 8.5 constants.

1. Lemma 8.3: build P = 1 + eta/4 - I*F_R via its Fourier coefficients,
   check P >= 1 on J = {||t|| <= 1/2 - eta} (fine grid + margin), P > 0,
   sum c_m^2 <= 1 - eta/3, and the Fejer pointwise bound used.
2. Prop 8.4 steps for a K=2 instance with eta=1/9, R=324: choice of a_i,
   spacing of Theta >= 1/(2 Xi), weights, g >= 1 on A (sampled), and
   |A cap [1,N]| <= (5N/3)(sum c^2)^K.
3. Thm 8.5 constants: c = 1/(27 log 649), N_0 for a positive saving,
   density exponent log(9/7)/log 649.
"""
import math, random
import numpy as np


def coeffs(eta, R):
    m = np.arange(-R, R + 1)
    # I = indicator of ||t - 1/2|| <= eta/2 ; hat I(m) = int I(t) e(-mt) dt
    with np.errstate(invalid="ignore", divide="ignore"):
        Ihat = np.where(m == 0, eta, np.sin(np.pi * m * eta) / (np.pi * np.where(m == 0, 1, m)))
    Ihat = Ihat * np.cos(np.pi * m)  # e(-m/2) = (-1)^m
    Fhat = 1 - np.abs(m) / (R + 1)
    c = -Ihat * Fhat
    c[R] += 1 + eta / 4
    return m, c


def P_eval(m, c, t):
    t = np.atleast_1d(t)
    out = np.empty(len(t))
    B = max(1, 2_000_000 // len(m))  # memory-bounded batches
    for s in range(0, len(t), B):
        out[s:s + B] = np.real(np.exp(2j * np.pi * np.outer(t[s:s + B], m)) @ c)
    return out


def lemma83():
    for eta in (1 / 8, 1 / 9, 1 / 20):
        R = math.ceil(4 / eta**2)
        m, c = coeffs(eta, R)
        assert np.allclose(c, c[::-1])  # real & even
        t = np.linspace(0, 1, 200001)
        P = P_eval(m, c, t)
        dist = np.minimum(t, 1 - t)
        onJ = dist <= 0.5 - eta
        s2 = float(np.sum(c**2))
        print(f"eta={eta:.4f} R={R}: min P on J={P[onJ].min():.6f}  min P={P.min():.5f}  "
              f"sum c^2={s2:.6f}  1-eta/3={1-eta/3:.6f}  ok={P[onJ].min()>=1-1e-9 and s2<=1-eta/3}")
    # Fejer bound F_R(z) <= 1/(4(R+1)z^2)
    R = 50
    z = np.linspace(1e-4, 0.5, 100000)
    F = (np.sin(np.pi * (R + 1) * z) / np.sin(np.pi * z))**2 / (R + 1)
    print("Fejer bound holds:", bool(np.all(F <= 1 / (4 * (R + 1) * z**2) + 1e-9)))


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prop84(K=2, seed=3):
    eta = 1 / 9
    R = 324
    Xi = (2 * R + 1)**K
    N = 3 * Xi
    eps = 1 / (4 * K * R * Xi)
    lo = math.isqrt(16 * K * R * N) + 1
    pr = []
    p = lo
    while len(pr) < 2 * K:
        if is_prime(p):
            pr.append(p)
        p += 1
    thetas, Ds, As = [], [], []
    for i in range(1, K + 1):
        l, lp = pr[2 * i - 2], pr[2 * i - 1]
        D = l * lp
        beta = (2 * R + 1)**(-i)
        a0 = round(D * beta)
        cands = [a for a in range(a0 - 3, a0 + 4) if math.gcd(a, D) == 1 and abs(a / D - beta) <= eps]
        assert cands, "no coprime a_i in the window"
        a = cands[0]
        thetas.append(a / D)
        Ds.append(D)
        As.append(a)
    # spacing
    import itertools
    rng = np.arange(-R, R + 1)
    pts = np.zeros(1)
    for th in thetas:
        pts = (pts[:, None] + rng[None, :] * th).ravel()
    pts = np.sort(np.mod(pts, 1.0))
    gaps = np.diff(np.concatenate([pts, [pts[0] + 1]]))
    print(f"K={K}: Xi={Xi}, N={N}, D_i={Ds}, min gap*Xi={gaps.min()*Xi:.4f} (claim >= 0.5)")
    # A cap [1,N]
    n = np.arange(1, N + 1)
    inA = np.ones(N, bool)
    for a, D in zip(As, Ds):
        r = (n * a) % D
        x = r / D
        inA &= np.minimum(x, 1 - x) <= 0.5 - eta
    m, c = coeffs(eta, R)
    s2 = float(np.sum(c**2))
    bound = (5 * N / 3) * s2**K
    print(f"  |A|={inA.sum()}  bound (5N/3)(sum c^2)^K={bound:.1f}  N={N}  ok={inA.sum() <= bound}")
    # g >= 1 on A, sampled
    random.seed(seed)
    idx = np.flatnonzero(inA)
    samp = np.array(random.sample(list(idx), min(2000, len(idx)))) + 1
    g = np.ones(len(samp))
    for a, D in zip(As, Ds):
        t = ((samp * a) % D) / D
        g *= P_eval(m, c, t)
    print(f"  min g on sampled A = {g.min():.5f}")


def thm85():
    c = 1 / (27 * math.log(649))
    print(f"c = 1/(27 log 649) = {c:.6f}; density exponent log(9/7)/log 649 = {math.log(9/7)/math.log(649):.5f}")
    # saving K/27 - log(5/3) > 0 needs K >= 14
    Kmin = next(K for K in range(1, 100) if K / 27 > math.log(5 / 3))
    print(f"positive saving needs K >= {Kmin}, i.e. N >= 3*649^{Kmin} = 10^{math.log10(3)+Kmin*math.log10(649):.1f}")
    # exact (1-eta/3)^K vs e^{-K/27}
    print("1 - 1/27 <= e^{-1/27}:", 1 - 1 / 27 <= math.exp(-1 / 27))


if __name__ == "__main__":
    lemma83()
    prop84(K=1)
    prop84(K=2)
    thm85()
