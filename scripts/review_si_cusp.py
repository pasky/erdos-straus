"""R204: numeric sanity check of the cusp-0 expansions used in SIGN_IDENTITY Thm 2.2 (short proof):
for holomorphic weight-2 Eisenstein E2(z) - N E2(Nz) the y^{-1} anomaly of quasi-modular E2 cancels, so
f(iy) = b y^{-2} + exp. small; for E2 alone (quasi-modular, NOT in the theorem's scope) a 6/(pi y) term survives.
Also theta^3 (weight 3/2): theta(iy)^3 ~ (2y)^{-3/2}.  Uses mpmath."""
from mpmath import mp, mpf, exp, pi, sqrt

mp.dps = 30


def sigma1(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


S1 = [0] + [sigma1(n) for n in range(1, 4001)]


def E2(y):
    return 1 - 24 * sum(S1[n] * exp(-2 * pi * n * y) for n in range(1, 4001))


def theta(y):
    return 1 + 2 * sum(exp(-pi * k * k * y) for k in range(1, 200))


for y in (mpf('0.05'), mpf('0.03'), mpf('0.02')):
    e2 = E2(y)
    N = 2
    comb = E2(y) - N * E2(N * y)
    print(f"y={y}: E2(iy)+y^-2 = {float(e2 + y**-2):.6f} vs 6/(pi y) = {float(6/(pi*y)):.6f};"
          f"  y^2*(E2(iy)-2E2(2iy)) = {float(y**2 * comb):.8f} (pred -(1-1/N) = -0.5);"
          f"  theta(iy)^3*(2y)^1.5 = {float(theta(2*y)**3 * (2*y)**1.5 / 1):.8f}")
