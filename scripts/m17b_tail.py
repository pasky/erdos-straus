"""O93: explicit-hypothesis tail table.  T_P = sum_{K>=K0 odd} 17^((1-K)/2) * 2 D_P(K),
T_Q = sum_{k>=k0 odd} 17^(1-k) * 2 D_Q(k); sterile point if T_P + T_Q < rho.
Usage: m17b_tail.py K0 k0 rho_num rho_den
"""
import sys, math

def floor_sig(x, sig=4):  # round DOWN to sig significant digits (R93 repair M1/m2)
    from decimal import Decimal, ROUND_FLOOR
    d = Decimal(repr(x)); q = Decimal(1).scaleb(d.adjusted() - sig + 1)
    return str(d.quantize(q, rounding=ROUND_FLOOR))
from fractions import Fraction
K0, k0 = int(sys.argv[1]), int(sys.argv[2]); rho = Fraction(int(sys.argv[3]), int(sys.argv[4]))
S = 17.0
# sums to K, k <= 999 plus, for the power forms, the exact geometric remainder (R93 repair: no truncation)
def TP(th, C=1.0, f=None):
    if f is None:
        return sum(2 * C * S ** (th * K + (1 - K) / 2) for K in range(K0, 1001, 2)) \
            + 2 * C * S ** (th * 1001 + (1 - 1001) / 2) / (1 - S ** (2 * th - 1))
    return sum(2 * f(K) * S ** ((1 - K) / 2) for K in range(K0, 1001, 2))
def TQ(th, C=1.0, f=None):
    if f is None:
        return sum(2 * C * S ** (th * k + 1 - k) for k in range(k0, 1001, 2)) \
            + 2 * C * S ** (th * 1001 + 1 - 1001) / (1 - S ** (2 * th - 2))
    return sum(2 * f(k) * S ** (1 - k) for k in range(k0, 1001, 2))
r = float(rho)
print(f"rho = {rho} = {r:.9f}; P tail from K={K0}, Q tail from k={k0}")
for thQ in (0.6, 0.75):
    tq = TQ(thQ)
    print(f"  Q hyp D_Q(k) <= 17^({thQ} k): T_Q = {tq:.3e}")
tq = TQ(0.6)
for th in (0.25, 0.3, 0.35, 0.4, 0.42, 0.45):
    print(f"  theta_P={th}: T_P/C = {TP(th):.4e}; max C with D_P(K) <= C*17^(theta K) (and Q at 0.6, C_Q=1): {floor_sig((r - tq) / TP(th))} (exact {(r - tq) / TP(th):.7f}, rounded down)")
for name, f in (("2K^3", lambda K: 2 * K ** 3), ("K^4", lambda K: K ** 4), ("K^5", lambda K: K ** 5)):
    print(f"  D_P(K), D_Q(k) <= {name}: T_P = {TP(0, f=f):.3e}, T_Q = {TQ(0, f=f):.3e}")
