"""R116-B from-scratch checks (independent of the author's scripts).

(1) Mellin formula K_nu(x) = (8 pi i)^{-1} int_{(c)} Gamma((s+nu)/2)Gamma((s-nu)/2) (x/2)^{-s} ds
    for REAL nu = sigma in (0,1/4] (exceptional case), on the line c = sigma + 1/LL (Lemma 2.1).
(2) Lemma 2.1 Gamma bound: sup_v |G(s_v)| e^{pi|v|/2} / LL^2 bounded uniformly in sigma, LL.
(3) Prop 2.2 pointwise bound |(pi t Y_d)^{-s}| <= e^2 w(t)^sigma, w(t)=max(1,1/(pi t Y0)), Y_d in [Y0/sqrt2, Y0],
    LL >= log(1/Y0).
(4) Lemma 1.2 Abel identity sum c(n) rho(n) = -int_1^inf S(t) c'(t) dt and the Cauchy-Schwarz inequality,
    random rho, Schwartz-type c.
"""
import mpmath as mp
import random

mp.mp.dps = 30


def K_mellin(nu, x, c):
    f = lambda v: mp.gamma((c + 1j * v + nu) / 2) * mp.gamma((c + 1j * v - nu) / 2) * (x / 2) ** (-(c + 1j * v))
    # ds = i dv ; (8 pi i)^{-1} * i = 1/(8 pi)
    return mp.quad(f, [-mp.inf, -20, 0, 20, mp.inf]) / (8 * mp.pi)


worst = 0
for sig in [0.01, 0.1, 0.25]:
    for LL in [3, 10, 30]:
        c = sig + 1.0 / LL
        for x in [0.05, 0.7, 3.0]:
            a = K_mellin(sig, x, c)
            b = mp.besselk(sig, x)
            worst = max(worst, abs(a - b) / abs(b))
print("(1) Mellin formula max rel err:", mp.nstr(worst, 5))

ratio = 0
for sig in [1e-4, 0.01, 0.1, 0.25]:
    for LL in [3, 10, 100, 1000]:
        c = sig + 1.0 / LL
        for v in [0, 0.001, 0.01, 0.1, 1, 3, 10, 30]:
            G = abs(mp.gamma((c + 1j * v + sig) / 2) * mp.gamma((c + 1j * v - sig) / 2))
            ratio = max(ratio, G * mp.e ** (mp.pi * v / 2) / LL ** 2)
print("(2) sup |G(s_v)| e^{pi|v|/2} / LL^2 =", mp.nstr(ratio, 5), "(should be O(1))")

random.seed(1)
bad = 0
for _ in range(20000):
    Y0 = 10 ** random.uniform(-12, -0.5)
    LL = mp.log(1 / Y0) * random.uniform(1, 3)
    Yd = Y0 * random.uniform(2 ** -0.5, 1)
    sig = random.uniform(0, 0.25)
    t = 10 ** random.uniform(0, 14)
    lhs = (mp.pi * t * Yd) ** (-(sig + 1 / LL))
    w = max(1, 1 / (mp.pi * t * Y0))
    if lhs > mp.e ** 2 * w ** sig * (1 + 1e-12):
        bad += 1
print("(3) violations of |(pi t Y_d)^{-s}| <= e^2 w^sigma:", bad)

# (4) Abel summation
random.seed(2)
NMAX = 400
rho = [0] + [complex(random.gauss(0, 1), random.gauss(0, 1)) * n ** 0.5 for n in range(1, NMAX + 1)]
lam = 0.05
c = lambda t: mp.e ** (-(lam * t) ** 2) * t ** (-0.3 + 0.7j)
cp = lambda t: mp.diff(c, t)
lhs = sum(c(n) * rho[n] for n in range(1, NMAX + 1))  # c is ~0 beyond NMAX
S = [0] * (NMAX + 1)
for n in range(1, NMAX + 1):
    S[n] = S[n - 1] + rho[n]
# -int_1^inf S(t) c'(t) dt, S piecewise constant on [n, n+1)
rhs = -sum(S[n] * (c(n + 1) - c(n)) for n in range(1, NMAX)) - S[NMAX] * (0 - c(NMAX))
print("(4) Abel identity |lhs-rhs|/|lhs| =", mp.nstr(abs(lhs - rhs) / abs(lhs), 5))
I1 = sum(mp.quad(lambda t: abs(cp(t)), [n, n + 1]) for n in range(1, 120))
I2 = sum(abs(S[n]) ** 2 * mp.quad(lambda t: abs(cp(t)), [n, n + 1]) for n in range(1, 120))
print("    Lemma 1.2: |sum|^2 =", mp.nstr(abs(lhs) ** 2, 6), "<= bound", mp.nstr(I1 * I2, 6), abs(lhs) ** 2 <= I1 * I2 * 1.001)
