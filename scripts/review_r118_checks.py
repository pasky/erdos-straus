"""R118 from-scratch checks for §9 of paper/es-typei-heegner-note.tex (O118).

Independent of the author's scripts. Small, memory-bounded.
(a) Lemma 9.3 gamma bound; (b) Prop 9.4 weight bound; (c) Lemma 9.2 Abel identity;
(d) Prop 9.4 Phi-integrals for a concrete bump; (e) Cor 9.7 exponent algebra on the bad region,
and the size of q vs the hypothesis q <= N^{1/100} of Thm 9.6; (f) Thm 9.9 epsilon bookkeeping.
"""
import math
import random
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

random.seed(1)
np.random.seed(1)

# (a) |G(s_v)| = |Gamma((s-sig)/2) Gamma((s+sig)/2)| <= C L^2 exp(-pi|v|/2), s = sig + 1/L + iv
worst = 0.0
for L in [2, 3, 5, 10, 30, 100, 1000]:
    for sig in [1e-6, 0.01, 0.1, 0.2, 0.25]:
        for v in [0, 0.1, 0.5, 1, 2, 5, 10, 30, 80]:
            s = mp.mpf(sig) + mp.mpf(1) / L + 1j * v
            g = abs(mp.gamma((s - sig) / 2) * mp.gamma((s + sig) / 2))
            r = float(g / (L**2 * mp.e ** (-mp.pi * abs(v) / 2)))
            worst = max(worst, r)
print(f"(a) sup |G|/(L^2 e^(-pi|v|/2)) over grid = {worst:.3f}  (bounded => Lemma 9.3 gamma bound OK)")

# (b) |(pi t Y_d)^{-s}| <= e^2 w(t)^sigma, w = max(1, 1/(pi t Y0)), Y_d in [Y0/sqrt2, Y0], L >= log(2+1/(lam Y0))
worst = 0.0
for _ in range(20000):
    Y0 = 10 ** random.uniform(-12, 0)
    lam = 10 ** random.uniform(-6, 1)
    lm = min(lam, 1.0)
    L = math.log(2 + 1 / (lm * Y0)) * random.uniform(1, 3)
    Yd = Y0 * random.uniform(2**-0.5, 1)
    sig = random.uniform(0, 0.25)
    t = 10 ** random.uniform(0, 14)
    lhs = (math.pi * t * Yd) ** (-(sig + 1 / L))
    w = max(1.0, 1 / (math.pi * t * Y0))
    worst = max(worst, lhs / w**sig)
print(f"(b) sup |(pi t Y_d)^-s| / w^sigma = {worst:.4f}  vs e^2 = {math.e**2:.3f}")

# (c) Abel: sum_{n>=1} c(n) a_n = -int_1^inf S(t) c'(t) dt, c(t) = exp(-t/7) * cos(t/3)
a = np.random.randn(400)
c = lambda t: math.exp(-t / 7) * math.cos(t / 3)
cp = lambda t: -math.exp(-t / 7) * (math.cos(t / 3) / 7 + math.sin(t / 3) / 3)
lhs = sum(c(n) * a[n - 1] for n in range(1, 401))
S = np.cumsum(a)
rhs = 0.0
for n in range(1, 400):  # on [n, n+1) S(t) = S[n-1]
    rhs -= S[n - 1] * float(mp.quad(lambda x: cp(float(x)), [n, n + 1]))
rhs -= S[399] * (0 - c(400))  # tail int_400^inf c' = -c(400)
print(f"(c) Abel identity: lhs={lhs:.10f} rhs={rhs:.10f}")

# (d) Phi-integrals for phi = bump on [-2,-1]; hat phi computed numerically
def bump(x):
    if -2 < x < -1:
        y = (x + 1.5) * 4
        return math.exp(-1 / (1 - y * y)) if abs(y) < 1 else 0.0
    return 0.0

xs = np.linspace(-2, -1, 4001)
bx = np.array([bump(x) for x in xs])
dx = xs[1] - xs[0]

def phihat(xi):
    return np.sum(bx * np.exp(-2j * np.pi * xi * xs)) * dx

def phihatp(xi):
    return np.sum(bx * (-2j * np.pi * xs) * np.exp(-2j * np.pi * xi * xs)) * dx

us = np.concatenate([np.geomspace(1e-7, 1, 300), np.linspace(1, 40, 2000)[1:]])
H = np.array([abs(phihat(u)) for u in us])
Hp = np.array([abs(phihatp(u)) for u in us])
print("(d) lam, int Phi/(lam*log(2/lam)),  int Phi t^{1+a+eps} log^2(2t) / (log^2(2/lam) lam^{-a-eps}) for a=0,1,2")
for lam in [1e-6, 1e-4, 1e-2, 0.3, 1.0]:
    eps = 0.25
    m = us >= lam
    u, h, hp = us[m], H[m], Hp[m]
    t = u / lam
    Phi = lam**2 * hp + lam * h / t
    dt = np.gradient(t)
    I0 = np.sum(Phi * dt)
    Lg = math.log(2 / lam) + 1
    out = [I0 / (lam * Lg)]
    for aa in [0, 1, 2]:
        Ia = np.sum(Phi * t ** (1 + aa + eps) * np.log(2 * t) ** 2 * dt)
        out.append(Ia / (Lg**2 * lam ** (-aa - eps)))
    print(f"    {lam:8.1e}  " + "  ".join(f"{x:8.3f}" for x in out))

# (e) Cor 9.7 exponents (log_N units, q = 1, cell O(1/L) errors ignored)
eta = 0.01
eps1 = 0.01
worst = {"ii": -9, "iii": -9, "iv": -9}
fprime_bad = 0
maxdelta = 0
n = 0
while n < 200000:
    al, be, ga = random.uniform(0, 1), random.uniform(0, 1.05), random.uniform(0, eta)
    if not (ga <= eta and al + be >= 1 - eta and be <= 2 * al + ga + eta and be <= 1 + eta and be >= al and al + ga <= 1):
        continue
    dl = 2 * al - 1 + ga
    if dl <= 0:
        continue
    d_ = 1 - ga - al
    E, F = be - ga, 1 + al - be
    if be < al + ga:
        if ga > dl / 2:
            continue
        case, fp = "ii", E
    elif be < 1:
        case, fp = "iii", min(E, F)
    else:
        if be - 1 > dl / 2:
            continue
        case, fp = "iv", F
    n += 1
    maxdelta = max(maxdelta, dl)
    if fp > al + d_ / 2 + 1e-12:
        fprime_bad += 1
    T1 = -dl / 2 + max(0.0, al - fp) / 2
    T2 = eps1 / 2 + fp / 2 - al
    T3 = fp / 4 + d_ / 8 - al / 2
    worst[case] = max(worst[case], max(T1, T2, T3) + dl / 4)
print(f"(e) max over cells of [max(T1,T2,T3) + delta/4] by case: {worst}  (<= ~0 required)")
print(f"    F' > A sqrt(D) violations: {fprime_bad};  max delta on D<A side: {maxdelta:.3f}")
print(f"    => Q = N^(delta/64) up to N^{maxdelta/64:.4f}; Thm 9.6 hypothesis q <= N^(1/100) = N^0.0100")

# (f) bookkeeping
e = -Fr(1, 4) + Fr(3, 64) + Fr(2, 64)
print(f"(f) exponent -1/4 + 3/64 + 2*(1/64) = {e};  11/64 > 1/6: {Fr(11,64) > Fr(1,6)};  9/64 = {Fr(11,64)-Fr(2,64)}")
