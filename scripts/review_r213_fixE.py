"""R213: independent fibre test for CAP_TWO §6 'fix E, vary c'. Fibre x = cE carries an integer point of
4n a^2 - x a B + B^2 = -E  iff  X^2 - Delta Y^2 = -4E (X = 2B - x a, Y = a, Delta = x^2 - 16n) has a solution
(X = Y mod 2 is automatic for odd Delta; Y != 0 automatic; sign of (a,B) can be flipped). Uses sympy diop_DN.
Admissible c: odd, 3 <= c <= C, gcd(c, nE) = 1 (reproduces the author's counts of admissible c)."""
import sys
from math import gcd, isqrt
from sympy.solvers.diophantine.diophantine import diop_DN
n, E, C = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
adm = yes = 0; ys = []
for c in range(3, C + 1, 2):
    if gcd(c, n*E) != 1: continue
    adm += 1
    x = c*E; D = x*x - 16*n
    if D <= 0 or isqrt(D)**2 == D: continue
    sols = diop_DN(D, -4*E)
    if sols:
        X, Y = sols[0]; assert X*X - D*Y*Y == -4*E
        yes += 1; ys.append(c)
print(f"n={n} E={E}: {yes} of {adm} admissible c <= {C} carry a point; c = {ys[:30]}; all 3|c: {all(c % 3 == 0 for c in ys)}")
