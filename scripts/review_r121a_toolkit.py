"""R121A from-scratch checks of LOGLOG3 §1 (Lemmas 1.1-1.3) and of the transform facts used in
ttl3_lemma81_effective.md §2.2 (c), (e); support computation §3.2; k-range §4."""
import math
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp

# ---- Lemma 1.3 (a): |h^{(p)}(x)| <= 9^p (p!)^2 for h = exp(-1/x)
x = sp.symbols('x', positive=True)
h = sp.exp(-1 / x)
worst = 0
d = h
for p in range(0, 16):
    if p > 0:
        d = sp.diff(d, x)
    f = sp.lambdify(x, d, 'mpmath')
    mp.mp.dps = 40
    m = max(abs(f(mp.mpf(t) / 400)) for t in range(1, 4000))  # x in (0,10]
    ratio = m / (mp.mpf(9) ** p * mp.factorial(p) ** 2)
    worst = max(worst, ratio)
print("Lemma1.3(a) max |h^(p)|/(9^p p!^2), p<=15:", mp.nstr(worst, 5))

# ---- Lemma 1.3 (b): I >= e^{-16}/4, and the eta derivative bound sanity (numerical, p<=6)
I = mp.quad(lambda t: mp.e ** (-1 / (0.25 + t)) * mp.e ** (-1 / (0.25 - t)), [-0.25, 0, 0.25])
print("I =", I, " e^-16/4 =", mp.e ** -16 / 4, " ok:", I >= mp.e ** -16 / 4)
# rho^(p) bound: |rho^(p)| <= 4 e^16 18^p p!^2 ; check numerically by symbolic diff for p<=6
t = sp.symbols('t', real=True)
rho = sp.exp(-1 / (sp.Rational(1, 4) + t)) * sp.exp(-1 / (sp.Rational(1, 4) - t))
worst = 0
d = rho
for p in range(0, 9):
    if p > 0:
        d = sp.diff(d, t)
    f = sp.lambdify(t, d, 'mpmath')
    m = max(abs(f(mp.mpf(k) / 4000 - mp.mpf(1) / 4)) for k in range(1, 2000)) / I
    worst = max(worst, m / (4 * mp.e ** 16 * mp.mpf(18) ** p * mp.factorial(p) ** 2))
print("Lemma1.3(b) max |rho^(p)| / bound, p<=8:", mp.nstr(worst, 5))


# ---- Lemma 1.1: f(n) <= (2B/delta)^{B 2^{B/delta}} n^delta for f = tau^B ; brute force small n
def tau(n):
    c, k = 1, 2
    while k * k <= n:
        e = 0
        while n % k == 0:
            n //= k; e += 1
        c *= e + 1; k += 1
    if n > 1: c *= 2
    return c
worst = 0
for B in [1, 2]:
    for dl in [1.0, 0.7, 0.5, 0.34, 0.25]:
        lK = (B * 2 ** (B / dl)) * math.log(2 * B / dl)
        for n in range(1, 200001):
            r = math.exp(B * math.log(tau(n)) - dl * math.log(n) - lK)
            worst = max(worst, r)
print("Lemma1.1 max ratio (should be <=1):", worst)

# ---- §3.2 support of switched modulus c, and §4 k-range
# x = 4 pi sqrt(mn)/(qc) in supp phi = [11/(12Y),17/(12Y)], q in [3Q/4, 9Q/4], sqrt(mn) in [N,2N]; C = pi N Y/Q
lo = Fr(4) * Fr(1) / (Fr(9, 4) * Fr(17, 12))  # c/(pi N Y/Q) lower = 4*1/(q/Q * xY)
hi = Fr(4) * Fr(2) / (Fr(3, 4) * Fr(11, 12))
print("c/C range:", lo, hi, float(lo), float(hi), "inside (1,16]:", lo > 1 and hi <= 16)
# DI printed supports [1/2,5/2] for both
print("DI pictured:", Fr(4) / (Fr(5, 2) * Fr(5, 2)), Fr(8) / (Fr(1, 2) * Fr(1, 2)))
# k = qc range in (P1): k = 4 pi sqrt(mn)/x, x in [11/(12Y), 17/(12Y)]
print("k/(NY) range:", float(4 * math.pi * 12 / 17), float(8 * math.pi * 12 / 11))

# ---- transform (c): phi^(-i sigma)/cos(pi sigma) >= Y^{2 sigma}/64, compute directly with mpmath
mp.mp.dps = 30
def eta_(u):  # any bump with eta=1 on [1,2], supp in [3/4,9/4]; positivity lower bound only uses plateau,
    # so test the worst case: plateau indicator of [1,4/3] for Psi (phi >= 1 on [1/Y,4/(3Y)], phi >= 0)
    return 1 if 1 <= u <= mp.mpf(4) / 3 else 0
def kernel(xx, s):  # normalised exceptional kernel pi/(2 sin(pi s)) [J_{-2s}(x) - J_{2s}(x)]
    return mp.pi / (2 * mp.sin(mp.pi * s)) * (mp.besselj(-2 * s, xx) - mp.besselj(2 * s, xx))
worst = mp.inf
for Y in [2 ** 32, 2 ** 40]:
    for s in [mp.mpf('1e-6'), mp.mpf('0.001'), mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.25')]:
        # positivity of kernel over whole support [11/12Y, 17/12Y] so plateau lower bound is legit
        kmin = min(kernel(mp.mpf(a) / (12 * Y), s) for a in [11, 12, 14, 16, 17])
        assert kmin > 0
        val = mp.quad(lambda xx: kernel(xx, s) / xx, [mp.mpf(1) / Y, mp.mpf(4) / (3 * Y)])
        worst = min(worst, val / mp.cos(mp.pi * s) / mp.mpf(Y) ** (2 * s))
print("(c) min phi^(-i s)/cos(pi s)/Y^{2s} over grid (needs >= 1/64):", mp.nstr(worst, 6))
