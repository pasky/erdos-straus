# z70 LOOSE item 1 (I6): numerical check of the fibre transformation law (Z70_LOOSE.md §2, Theorem F).
# L(z) = sum_{A = al (M), B = be (M), A,B >= 1} e(ABz);  a = al/M, b = be/M in (0,1);  w = -1/(M^2 z).
# Claimed:  L(z) = (1/(M^2 z)) L*_{a,b}(w) + E(z) + Psi(z),
#   L*_{u,v}(w) = sum_{m,n>=1} e(mu + nv + mnw),
#   E(z) = (i/(2 pi M^2 z)) (-gamma - log(-2 pi i M^2 z) - psi(a) - psi(b)) + (1/2 - a)(1/2 - b),
#   Psi(z) = (i/(2 pi M^2 z)) * int_{C-} [ S1(tw) t/(t-1) - S2(tw) t/(1+t) ] dt,
#   S1 = L*_{a,b} + L*_{-a,-b},  S2 = L*_{a,-b} + L*_{-a,b},  C- = ray from 0 to infinity passing BELOW t = 1.
# Double precision (numpy); quadrature on the ray t = s e^{-i theta}, theta = arg(w)/2, Gauss-Legendre panels in log s.
import sys, numpy as np
from scipy.special import digamma
EG = 0.5772156649015329
SMALL = 2e-4  # below this |w| the asymptotic series is used (error ~ k!(2 pi |w| / |1-e(u)|^2)^k)
def e(x): return np.exp(2j * np.pi * x)
def Ldirect(z, M, al, be):
    tot = 0j; A = al
    while True:
        t = e(A * be * z) / (1 - e(A * M * z)); tot += t
        if abs(e(A * be * z)) < 1e-20 and A > 10 * M: break
        A += M
    return tot
def Li_neg(k, x):
    return [x / (1 - x), x / (1 - x)**2, x * (1 + x) / (1 - x)**3, x * (1 + 4*x + x*x) / (1 - x)**4,
            x * (1 + 11*x + 11*x*x + x**3) / (1 - x)**5][k]
def Lstar_series(w, u, v, K=5):
    # asymptotic expansion at w -> 0 (Mellin residues at s = -k; F(u,s) entire for u not in Z):
    # L*_{u,v}(w) ~ sum_k (2 pi i w)^k / k! Li_{-k}(e(u)) Li_{-k}(e(v))
    from math import factorial
    return sum((2j * np.pi * w)**k / factorial(k) * Li_neg(k, e(u)) * Li_neg(k, e(v)) for k in range(K))
def Lstar(w, u, v):
    # vectorised over an array w; small |w| handled by the asymptotic series
    w = np.atleast_1d(w).astype(complex); tot = np.zeros(w.shape, complex)
    small = np.abs(w) < SMALL
    if small.any():
        tot[small] = Lstar_series(w[small], u, v)
        if small.all(): return tot
        big = Lstar(w[~small], u, v); tot[~small] = big; return tot
    mmax = int(np.ceil(48 / (2 * np.pi * w.imag.min()))) + 5
    for m in range(1, mmax + 1):
        q = e(v + m * w); tot += e(m * u) * q / (1 - q)
    return tot
def E(z, M, a, b):
    return (1j / (2 * np.pi * M * M * z)) * (-EG - np.log(-2j * np.pi * M * M * z) - digamma(a) - digamma(b)) + (0.5 - a) * (0.5 - b)
def Psi(z, M, a, b, npts=40):
    w = -1 / (M * M * z); th = np.angle(w) / 2; rot = np.exp(-1j * th)
    # panels in s: [0, s0] (integrand -> 0 like t), then log-spaced to s_max where |tw| Im large
    smax = 60 / (2 * np.pi * abs(w) * np.sin(np.angle(w) - th)) + 2
    edges = np.concatenate([[0.0], np.geomspace(1e-6, smax, 120)])
    xg, wg = np.polynomial.legendre.leggauss(npts)
    tot = 0j
    for lo, hi in zip(edges[:-1], edges[1:]):
        s = 0.5 * (hi - lo) * xg + 0.5 * (hi + lo); t = s * rot; tw = t * w
        S1 = Lstar(tw, a, b) + Lstar(tw, -a, -b); S2 = Lstar(tw, a, -b) + Lstar(tw, -a, b)
        f = S1 * t / (t - 1) - S2 * t / (1 + t)
        tot += np.sum(wg * f) * 0.5 * (hi - lo) * rot
    return (1j / (2 * np.pi * M * M * z)) * tot
def check(z, M, al, be):
    a, b = al / M, be / M; w = -1 / (M * M * z)
    lhs = Ldirect(z, M, al, be)
    q = Lstar(np.array([w]), a, b)[0] / (M * M * z); el = E(z, M, a, b); ps = Psi(z, M, a, b)
    rhs = q + el + ps
    return lhs, rhs, abs(lhs - rhs) / abs(lhs), q, el, ps
if __name__ == '__main__':
    base = [0.5j, 0.25j, 0.3 + 0.4j, -0.2 + 0.5j, 0.05 + 0.15j, 1.0 + 0.3j, 0.13 + 0.08j]
    for (M, al, be) in [(4, 3, 3), (12, 11, 11), (4, 1, 1), (12, 7, 5)]:
        print(f"M={M} alpha={al} beta={be}  (test points z = z0 * 1.6/(al*be) so that L(z) is not exponentially small)")
        for z0 in base:
            z = z0 * 1.6 / (al * be)
            lhs, rhs, rel, q, el, ps = check(z, M, al, be)
            print(f"  z={z:.5g}: L={lhs:.12g} law={rhs:.12g} rel.err={rel:.2e} abs.err={abs(lhs-rhs):.1e}  [q-part {q:.4g}, elem {el:.4g}, period {ps:.4g}]")
        sys.stdout.flush()
