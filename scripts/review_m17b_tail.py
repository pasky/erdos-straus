"""R93 from-scratch recomputation of the POINTWISE_MORDELL17B Theorem 4.1 table and §4 numbers.
T_P = 2 Σ_{K>=K0 odd} D_P(K) 17^{(1-K)/2},  T_Q = 2 Σ_{k>=9 odd} D_Q(k) 17^{1-k}.
Exponential hypothesis D_P <= C 17^{θK}: closed-form geometric sum.  Polynomial ones: summed to K=2001
(terms beyond are < 1e-300)."""
from fractions import Fraction
from mpmath import mp, mpf, power
mp.dps = 40
s17 = mpf(17)
rho1 = mpf(16344335) / 24137569; rho2 = mpf(961421) / 1419857
TQ = 2 * power(s17, 1 - mpf(18) / 5) / (1 - power(s17, mpf(-4) / 5))   # 2 Σ 17^{1-2k/5}, k=9,11,...
print("T_Q (3/5, C=1) =", mp.nstr(TQ, 6))
TQ34 = 2 * sum(power(s17, mpf(3) * k / 4 + 1 - k) for k in range(9, 2001, 2))
print("T_Q (3/4, C=1) =", mp.nstr(TQ34, 6))
for K0, rho in ((13, rho1), (15, rho2)):
    row = []
    for th in (0.25, 0.30, 0.35, 0.40, 0.42, 0.45):
        th = mpf(th)
        S = power(s17, th * K0 + (1 - mpf(K0)) / 2) / (1 - power(s17, 2 * th - 1))
        row.append(mp.nstr((rho - TQ) / (2 * S), 4))
    print(f"K0={K0}: Cmax", row)
def tp(fun, K0=13): return 2 * sum(fun(K) * power(s17, (1 - mpf(K)) / 2) for K in range(K0, 2001, 2))
def tq(fun): return 2 * sum(fun(k) * power(s17, 1 - mpf(k)) for k in range(9, 2001, 2))
for name, fp, fq in (("2K^3", lambda K: 2 * K**3, lambda k: 2 * k**3), ("K^4", lambda K: K**4, lambda k: k**4),
                     ("K^5", lambda K: K**5, lambda k: k**5), ("Conj4.2 (2K^3, 3k^3)", lambda K: 2 * K**3, lambda k: 3 * k**3)):
    a, b = tp(fp), tq(fq)
    print(f"{name}: T_P={mp.nstr(a,4)} T_Q={mp.nstr(b,4)} sum={mp.nstr(a+b,4)}")
DP = {1: 2, 3: 32, 5: 121, 7: 258, 9: 604, 11: 836, 13: 1463}
print("D_P/17^{0.4K}:", [mp.nstr(v / power(s17, 0.4 * K), 3) for K, v in DP.items()])
print("D_P vs 2K^3:", [(K, v, 2 * K**3) for K, v in DP.items()])
DQ = {1: 2, 3: 73, 5: 245, 7: 707}
print("D_Q vs 3k^3:", [(k, v, 3 * k**3) for k, v in DQ.items()], " 2k^3:", [2 * k**3 for k in DQ])
