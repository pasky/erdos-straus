"""O98: admissible constants for the CUMULATIVE hypothesis (M17C Lemma 1.1).
H_P^cum: S_P(K) = sum_{13<=K'<=K odd} D_P(K') <= C*17^(theta*K) for all odd K >= K0.
Abel summation gives T_P <= 2*(16/17)*C*sum_{K>=K0 odd} 17^(theta*K+(1-K)/2).
Usage: m17c_tail_cum.py K0 k0 rho_num rho_den   (T_Q from H_Q: D_Q(k) <= 17^(3k/5), un-weakened)
Series summed to 999 plus exact geometric remainder; thresholds floor-rounded.
"""
import sys
from decimal import Decimal, ROUND_FLOOR
from fractions import Fraction

def floor_sig(x, sig=4):
    d = Decimal(repr(x)); q = Decimal(1).scaleb(d.adjusted() - sig + 1)
    return str(d.quantize(q, rounding=ROUND_FLOOR))

K0, k0 = int(sys.argv[1]), int(sys.argv[2]); rho = float(Fraction(int(sys.argv[3]), int(sys.argv[4])))
S = 17.0
def ser(th, start, lin):  # sum_{K>=start odd} 17^(th*K + lin(K)) with geometric remainder
    s = sum(S ** (th * K + lin(K)) for K in range(start, 1001, 2))
    return s + S ** (th * 1001 + lin(1001)) / (1 - S ** (2 * th + (lin(1003) - lin(1001))))
TQ = 2 * ser(0.6, k0, lambda k: 1 - k)
print(f"rho={rho:.9f} K0={K0} k0={k0} T_Q={TQ:.6e}")
for th in (0.25, 0.30, 0.35, 0.40, 0.42, 0.45):
    sP = ser(th, K0, lambda K: (1 - K) / 2)
    pointwise = (rho - TQ) / (2 * sP)
    cum = (rho - TQ) / (2 * (16 / 17) * sP)
    # safety margin: shave 1e-9 relative before floor (float summation error)
    print(f"theta={th}: pointwise C* <= {floor_sig(pointwise*(1-1e-9))}   cumulative C* <= {floor_sig(cum*(1-1e-9))}")
