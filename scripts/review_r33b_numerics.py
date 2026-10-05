"""R33b from-scratch numeric checks for es-subexp-note v2, Thm 4.1 proof constants."""
import math
# Case A: lambda = 1 - e^{-u}/beta, beta = 1 - u/log x, log x >= 16, u < L.
worst = 9
for lx in [16, 17, 20, 50, 1e3, 1e6]:
    for i in range(1, 20001):
        u = i * 1e-3
        b = 1 - u / lx
        if b <= 0.5: break
        lam = 1 - math.exp(-u) / b
        r = lam / min(u, 1)
        worst = min(worst, r)
print("min lambda/min(u,1) over grid (claim >= 1/2):", worst)
# lower bound chain used in paper
print("1-1/e-2/16 =", 1 - 1/math.e - 2/16)
# u e^{-u} <= min(u,1)
print("max u e^{-u}/min(u,1):", max(u*math.exp(-u)/min(u,1) for u in [i*1e-3 for i in range(1,50000)]))
# L e^{-3L} <= e^{-L} for L>=2  <=> L e^{-2L} <= 1
print("max L e^{-2L} (L>=2):", max(L*math.exp(-2*L) for L in [2+i*1e-3 for i in range(10000)]))
# 1-x >= e^{-1.1x} on [0,1/32]
print("min (1-x)-e^{-1.1x} on [0,1/32]:", min((1-x)-math.exp(-1.1*x) for x in [i/32/10000 for i in range(10001)]))
print("e^{1.1/32} =", math.exp(1.1/32))
# Lemma A: E|B| <= E B + 2 E[F-B]... A <= 1+2/99
print("1+2/99 =", 1+2/99)
