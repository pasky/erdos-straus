"""R121A from-scratch numeric checks for ttl3_thm2_effective.md (effective DI Thm 2)."""
import math
import mpmath as mp
mp.mp.dps = 30

# Step 4: derivative separation ratio |b/(2 sqrt t)|/|a-u| with |a-u|>=1/c, theta<2, m in [N,2N]
def sep(lo):  # support of eta(t/N) starts at lo*N
    return 2 * 2 * (math.sqrt(2) - 1) / (2 * math.sqrt(lo))  # theta*|sqrt m1-sqrt m2|/(c sqrt t) * c, theta=2
print("Step4 ratio, supp [3/4,..]:", sep(0.75), "< 31/32 =", 31 / 32, "; DI supp (1/2,..):", sep(0.5))

# Step 4: Cauchy disc: g(z) = 1/(1 + beta z^{-1/2}), |beta|/sqrt(3/4) <= 31/32 (worst), radius 2^-12
beta = 31 / 32 * math.sqrt(0.75)
mn = min(abs(1 - beta / mp.sqrt(mp.mpf(x) + mp.mpf(2) ** -12 * mp.expjpi(k / 50)))
         for x in [0.75, 1, 1.5, 2.25] for k in range(100))
print("Step4 min |1 - beta z^-1/2| on discs:", mn, ">= 1/64:", mn >= 1 / 64)

# Step 2: row sums e sqrt(pi) c T [1 + 2 sum_h exp(-(Tch/4N)^2)] <= 100 (cT + N)
worst = 0
for cT in [0.01, 0.1, 1, 10, 100, 1e4]:
    for N in [1, 10, 1e3, 1e6]:
        s = 1 + 2 * mp.nsum(lambda h: mp.e ** (-(cT * h / (4 * N)) ** 2), [1, mp.inf])
        worst = max(worst, math.e * math.sqrt(math.pi) * cT * s / (cT + N))
print("Step2 max row-sum/(cT+N) (<=100):", worst)

# Step 7: integrated H-kernel lower bound >= 2^-20 (1+|r|) for real |r|<=K, and exceptional r=i sigma
def Hint(r, K, a, b):
    return mp.quad(lambda t: t * mp.sinh(mp.pi * t) * mp.cosh(mp.pi * r) /
                   (mp.cosh(mp.pi * (r - t)) * mp.cosh(mp.pi * (r + t))) * mp.e ** (-(t / K) ** 2), [a, b])
worst = mp.inf
for K in [1, 2, 10, 100]:
    for r in [0, 0.3, 0.99, 1, 1.5, 5, 20, 99]:
        if r > K: continue
        a, b = (r, r + 1) if r >= 1 else (1, 2)
        worst = min(worst, Hint(mp.mpf(r), K, a, b) / (1 + r))
print("Step7 min restricted H-integral/(1+|r|) (>= 2^-20 = %.2e):" % 2 ** -20, mp.nstr(worst, 5))
# exceptional: weight (1/cos(pi s)) * int t sinh(pi t) cos(pi s)/(sinh^2+cos^2) e^-(t/K)^2 over [1,2]
worst = mp.inf
for K in [1, 2, 10]:
    for s in [0, 0.1, 0.25]:
        v = mp.quad(lambda t: t * mp.sinh(mp.pi * t) * mp.cos(mp.pi * s) /
                    (mp.sinh(mp.pi * t) ** 2 + mp.cos(mp.pi * s) ** 2) * mp.e ** (-(t / K) ** 2), [1, 2])
        # identity check of H(i s, t) vs DI formula
        t0 = mp.mpf('1.3')
        Hdi = mp.cosh(mp.pi * 1j * s) / (mp.cosh(mp.pi * (1j * s - t0)) * mp.cosh(mp.pi * (1j * s + t0)))
        Hme = mp.cos(mp.pi * s) / (mp.sinh(mp.pi * t0) ** 2 + mp.cos(mp.pi * s) ** 2)
        assert abs(Hdi - Hme) < 1e-20
        worst = min(worst, v / (1 + s))
print("Step9 exceptional min restricted integral/(1+s) (s<=1/4):", mp.nstr(worst, 5))
s = mp.mpf('0.4999')
v = mp.quad(lambda t: t * mp.sinh(mp.pi * t) * mp.cos(mp.pi * s) / (mp.sinh(mp.pi * t) ** 2 + mp.cos(mp.pi * s) ** 2), [0, 3])
print("  (non-uniform as s->1/2 without the 1/cos factor: H-integral at s=.4999 =", mp.nstr(v, 4), ")")

# Step 6: D_K <= 2K^2 ; w-integrals
worst = 0
for K in [1, 1.5, 2, 5, 50, 500]:
    DK = mp.nsum(lambda l: (2 * l - 1) * mp.e ** (-(2 * l - 1) / K), [1, mp.inf])
    worst = max(worst, DK / (2 * K * K))
    w = lambda x: mp.sinh(2 / mp.mpf(K)) * (mp.cosh(1 / mp.mpf(K)) ** 2 - x * x) ** -1.5
    i1 = mp.quad(lambda x: w(x) * x, [0, 0.5, 0.9, 0.99, 1])
    ih = mp.quad(lambda x: w(x) * mp.sqrt(x), [0, 0.5, 0.9, 0.99, 1])
    imh = mp.quad(lambda x: w(x) / mp.sqrt(x), [0, 0.5, 0.9, 0.99, 1])
    assert abs(i1 - 2 * mp.e ** (-1 / mp.mpf(K))) < 1e-8, (K, i1)
    assert ih <= 32 and imh <= 32, (K, ih, imh)
print("Step6 max D_K/(2K^2):", mp.nstr(worst, 5), "; w-integrals ok")
# angular integrals
for D in [0.01, 0.1, 0.5, 1]:
    a = mp.quad(lambda v: mp.cos(v) ** -0.5, [0, D]); b = mp.quad(lambda v: mp.sqrt(mp.cos(v)) / mp.sin(v) ** 2, [D, mp.pi / 2])
    assert a <= 4 * D and b <= 4 / D, (D, a, b)
print("Step6 angular integrals ok")

# Step 8: sup_X X exp(-X^{2s}/2) <= (1+1/s)^{1/s}
for s in [0.1, 0.01, 0.001]:
    lmax = (math.log(1 / s) - 1) / (2 * s)  # max of log X - X^{2s}/2
    assert lmax <= (1 / s) * math.log(1 + 1 / s)
print("Step8 G(s) ok")

# Step 10: log K_T2 bound and K_T2 <= exp(exp(96/delta))
def logKT2(s):
    p = math.floor(2 / s)
    lA = 10000 * math.log(2)
    lRp = 100 * (p + 1) * math.log(2) + 4 * math.lgamma(p + 1)
    lD = 4 * 2 ** (4 / s) * math.log(8 / s) if 4 / s < 1000 else None
    return lA, lRp, p
worst = -1e9
for delta in [0.1, 0.05, 0.02, 0.01]:
    s = delta / 16; p = math.floor(2 / s)
    lA = 10000 * math.log(2); lRp = 100 * (p + 1) * math.log(2) + 4 * math.lgamma(p + 1)
    l1s = math.log(1 + 1 / s)
    # log D = 4*2^{4/s} log(8/s): work with log(log D)
    llD = math.log(4 * math.log(8 / s)) + (4 / s) * math.log(2)
    lG = (1 / s) * l1s
    lP_noD = lA + lRp + 4 * l1s
    rest = 4 * lA + 2 * lP_noD + 2 * lG + 4 * l1s
    # log K_T2 = rest + 4 log D ; compare log(log K_T2) with 96/delta
    llK = llD + math.log(4) + math.log1p(rest * math.exp(-llD - math.log(4)))
    worst = max(worst, llK - 96 / delta)
print("Step10 max loglogK_T2 - 96/delta (<0):", worst)
