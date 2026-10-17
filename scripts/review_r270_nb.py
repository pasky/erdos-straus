"""R270: NB tail prediction of B1_LINE §3.4, recomputed from scratch, plus sensitivity to growing dispersion D(L).
Expected # of b = 1 failures among primes p = 1 (24), p > X:  ∫_{ln X}^∞ e^L/(8L) · D^{-μ/(D-1)} dL,  μ = cμ L²."""
import math
def expected(X, cmu=0.125, Dfun=lambda L: 3.24, Lmax=200, h=1e-3):
    tot = 0.0; L = math.log(X)
    while L < Lmax:
        D = Dfun(L); mu = cmu * L * L
        tot += math.exp(L - mu * math.log(D) / (D - 1)) / (8 * L) * h
        L += h
    return tot
lin = lambda L: 0.78 + 0.103 * L        # fit to R270 class-(1 mod 24) dispersions 2.20, 2.67, 3.26, 3.62 at L = 13.8 … 27.6
for X in (1e6, 1e8, 1e11, 1e15):
    print(f"X={X:.0e}: fixed D=3.24: {expected(X):.3g} | -20% mu: {expected(X, 0.1):.3g} | D linear in L: {expected(X, Dfun=lin):.3g}"
          f" | D linear, -20% mu: {expected(X, 0.1, lin):.3g} | D linear, mu=0.119L^2: {expected(X, 0.119, lin):.3g}")
