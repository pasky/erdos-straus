"""O139 (POINTWISE_MORDELL17D §1): how far exact data must reach for explicit tail bounds.
(a) C*(K0): largest C with 2*(16/17)*C*sum_{K>=K0 odd} 17^(theta K+(1-K)/2) <= rho - T_Q (M17C Lemma 1.1),
    base rho = rho_2 = 961421/1419857 (generous: rho can only shrink when levels are added), T_Q = 1.4106e-3.
(b) For a hypothetical explicit bound D_P(K) <= A*17^(theta K)*(K ln 17)^B valid for K >= K0 (and exact data
    below), the least odd K0 >= 15 with T_P = 2*sum_{K>=K0} 17^((1-K)/2) D_P(K) < rho - T_Q.
Usage: python3 m17d_nogo.py
"""
import math
S, rho, TQ = 17.0, 961421 / 1419857, 1.4106e-3
def tail(f, K0, Kmax=2001):
    return sum(f(K) for K in range(K0, Kmax, 2))
print("(a) cumulative C*(K0) (floor, 4 sig.)")
ths = (0.30, 0.35, 0.40, 0.45)
print("K0   " + "  ".join(f"theta={t}" for t in ths))
for K0 in range(15, 33, 2):
    row = []
    for th in ths:
        s = tail(lambda K: S ** (th * K + (1 - K) / 2), K0)
        row.append(f"{(rho - TQ) / (2 * 16 / 17 * s) * (1 - 1e-9):.4g}")
    print(K0, "  ".join(row))
print("(b) least K0 for D_P <= A 17^(th K) (K ln17)^B")
for th, B in ((0.40, 0), (0.40, 1), (0.40, 2), (0.45, 1), (0.45, 2)):
    for A in (1, 11, 44, 1000):
        f = lambda K: 2 * A * S ** ((1 - K) / 2 + th * K) * (K * math.log(S)) ** B
        K0 = next((K for K in range(15, 1201, 2) if tail(f, K) < rho - TQ), None)
        print(f"theta={th} B={B} A={A}: K0={K0}  (N0 = 17^{K0} ~ 10^{K0 * math.log10(17):.0f} if K0 else '')")
