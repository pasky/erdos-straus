"""z66 UCOVER, Theorem S(b): rigorous bound sum_{k>=1} T_k(ell) < 1/2 for ell >= ELL0 (interval arithmetic).

T_k(ell) = ell/(ell-1) (k+2)(2.44 k ln ell + 10.15) ell^{-k/2} majorises B(ell^k, k)/phi(ell^k) for ell^k >= 1e5
(Z66_UCOVER.md Lemma S2').  Each T_k is decreasing in ell for k ln ell >= 2 and ell >= 2, so the sum at ELL0 bounds it
for every ell >= ELL0.  Usage: uv run --with mpmath python scripts/z66_ucover_sbound.py ELL0
"""
import sys
from mpmath import iv

iv.dps = 40
ell0 = int(sys.argv[1])
assert ell0 >= 10 ** 5
L = iv.mpf(ell0)
lnl = iv.log(L)


def T(k):
    return L / (L - 1) * (k + 2) * (iv.mpf("2.44") * k * lnl + iv.mpf("10.15")) * L ** (-iv.mpf(k) / 2)


tot = iv.mpf(0)
K3 = 60
for k in range(1, K3 + 1):
    tot += T(k)
rho = (1 + iv.mpf(1) / (K3 + 3)) * (1 + iv.mpf("2.44") * lnl / (iv.mpf("2.44") * (K3 + 1) * lnl + iv.mpf("10.15"))) \
    * L ** iv.mpf("-0.5")
tot += T(K3 + 1) / (1 - rho)
print(f"ell0={ell0}: sum_k T_k in {tot}  ->  upper bound {float(tot.b):.6f} {'< 1/2' if tot.b < 0.5 else '>= 1/2'}")
