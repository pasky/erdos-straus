"""O139 (17D §4): admissible constants, in box units, for the global and the localized criterion.
Global (M17B Thm 4.1, base rho_2, P from K=15, Q from k=9): NB_P(K) <= C 17^(theta K) for odd K >= 15,
  NB_Q(k) <= 2*17^(3k/5); need C*S(15) + T_Q(9) < rho_2.
Local (17D Thm 4.1, ball R of level Ls free through level Ls): NB_P^R(K) <= C 17^(theta K) 17^(1-Ls) for odd
  K >= 2Ls+1, NB_Q^R(k) <= 2*17^(3k/5) 17^(1-Ls) for odd k > Ls; need C*S(2Ls+1) + T_Q(Ls+1) < 1.
S(K0) = sum_{K>=K0 odd} 17^(theta K + (1-K)/2); T_Q(k0) = 2 sum_{k>=k0 odd} 17^(3k/5+1-k). Floor-rounded.
Usage: m17d_local_tail.py Ls [Ls ...]
"""
import sys
from decimal import Decimal, ROUND_FLOOR
S17, rho2 = 17.0, 961421 / 1419857
def fl(x, sig=4):
    d = Decimal(repr(x * (1 - 1e-9))); q = Decimal(1).scaleb(d.adjusted() - sig + 1)
    return str(d.quantize(q, rounding=ROUND_FLOOR))
def S(th, K0): return sum(S17 ** (th * K + (1 - K) / 2) for K in range(K0, 4001, 2))
def TQ(k0): return 2 * sum(S17 ** (0.6 * k + 1 - k) for k in range(k0 + (k0 % 2 == 0), 4001, 2))
ths = (0.30, 0.35, 0.40, 0.45)
print("theta:", ths)
print("global  (K>=15):", [fl((rho2 - TQ(9)) / S(t, 15)) for t in ths], f"T_Q={TQ(9):.4e}")
for Ls in map(int, sys.argv[1:]):
    print(f"local Ls={Ls} (K>={2*Ls+1}):", [fl((1 - TQ(Ls + 1)) / S(t, 2 * Ls + 1)) for t in ths], f"T_Q^R={TQ(Ls+1):.4e}")
