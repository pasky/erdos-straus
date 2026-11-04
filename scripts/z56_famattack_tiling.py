# Areas of the Burgess-admissible tiling regions (tau = 1/4 limit) and the resulting constants.
# Thm U tiles: Omega_U = {1/15 < a < 3/5, (1+a)/4 < b < 1-a}; Thm X tiles: Omega_X = {1/15 < a < 1/5, 2a+1/4 < b < 1-a}.
# Also |Omega_U ∪ Omega_U^T| (ordered-pair plane) for the Assessment upper bound if all parity/squarefree classes were admissible.
from fractions import Fraction as F
import math
import numpy as np
def area_U():  # exact
    a0, a1 = F(1, 15), F(3, 5)
    G = lambda a: F(3, 4) * a - F(5, 8) * a * a
    return G(a1) - G(a0)
def area_X():
    a0, a1 = F(1, 15), F(1, 5)
    G = lambda a: F(3, 4) * a - F(3, 2) * a * a
    return G(a1) - G(a0)
AU, AX = area_U(), area_X()
pi4 = math.pi ** 4
print("Area Omega_U =", AU, float(AU), " c_tile(U) = 8/pi^4 * A =", 8 * float(AU) / pi4, " vs Thm U 2/(3pi^4) =", 2 / (3 * pi4))
print("Area Omega_X =", AX, float(AX), " c_tile(X) =", 8 * float(AX) / pi4, " vs c_X =", 8 * 121 / 5120 / pi4)
print("HB-large-sieve variant (alpha0 -> 0, Assessment): area", F(9, 40), " c =", 8 * 9 / 40 / pi4)
M0 = 3 / (2 * math.pi ** 2)
print("full M0 coefficient 3/(2pi^2) =", M0, "; tile share =", 8 * float(AU) / pi4 / M0)
# union with transpose, Monte Carlo on grid
n = 4000; xs = (np.arange(n) + 0.5) / n
A, B = np.meshgrid(xs, xs, indexing='ij')
inU = lambda a, b: (a > 1/15) & (a < 3/5) & (b > (1 + a) / 4) & (b < 1 - a)
U1 = inU(A, B); U2 = inU(B, A)
print("|Omega_U| grid =", U1.mean(), " |Omega_U ∪ Omega_U^T| =", (U1 | U2).mean(), " |∩| =", (U1 & U2).mean())
print("Assessment upper bound (3/pi^2)*|Ω∪Ω^T| =", 3 / math.pi ** 2 * (U1 | U2).mean(), " share of M0:", 3 / math.pi ** 2 * (U1 | U2).mean() / M0)
