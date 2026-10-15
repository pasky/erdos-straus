"""review_zl_conic.py -- R231 round 2: check STERILE_LOWER §7 (conic Gamma_{c,d,z}) on all P-data of N = r^{2L-1} (r ∤ abcd) and
(p, q) with qa - pb = zW, W = r^L: Gamma holds, N = X^2/(r z^2); r | X; whether r | N is forced also when r | z; Vieta partners."""
import random
from fractions import Fraction as Fr
random.seed(7)
def P_data(N):
    a = 1
    while 4 * a * a - 2 * a <= N:
        b = a
        while 4 * a * b - 2 * b <= N:
            m = 4 * a * b
            for d in range(-(-(N + 1) // m), (N + a + b) // m + 1):
                e = m * d - N
                if 1 <= e <= a + b and (a + b) % e == 0: yield (a, b, (a + b) // e, d, e)
            b += 1
        a += 1
n = 0; rz = 0
for r, L in [(3, 2), (5, 2), (7, 2), (17, 2), (3, 3)]:
    N, W = r ** (2 * L - 1), r ** L
    for (a, b, c, d, e) in P_data(N):
        if a % r == 0 or b % r == 0 or c % r == 0 or d % r == 0: continue
        binv = pow(b, -1, W)
        for _ in range(20):
            q = random.randint(1, 4 * W); p = (q * a * binv) % W + W * random.randint(-2, 2)
            X = q * a - p * b; z = X // W
            if z == 0: continue
            assert c * X * X - 4 * r * c * d * z * z * a * b + r * z * z * (a + b) == 0
            assert Fr(X * X, r * z * z) == N and X % r == 0
            rz += (z % r == 0); n += 1
print(f"Gamma and N = X^2/(r z^2) hold on {n} instances ({rz} with r | z)")
# example: Vieta partners
a, b, c, d, z, r, p, q = 1, 78, 1, 16, 3, 17, -11, 9
G = ((p + q) ** 2 + 4 * r * d * z * z) // (4 * a * b * d - 17 ** 3); U, V = G * a - c * p * p, G * b - c * q * q
print("a' =", Fr(b * V, c * q * q), " b' =", Fr(a * U, c * p * p), " (a a' = const/(c q^2):", Fr(c*p*p*b*b + r*z*z*b, c*q*q*a) == Fr(b*V, c*q*q), ")")
# conic points with r | z: does N stay divisible by r? search small (a,b) on Gamma for given (c,d,z) with r | z
r, c, d, z, p, q = 5, 1, 1, 5, -2, 3
bad = []
for a in range(1, 400):
    for b in range(a, 400):
        X = q * a - p * b
        if c * X * X - 4 * r * c * d * z * z * a * b + r * z * z * (a + b) == 0 and (a + b) % c == 0:
            Nn = Fr(X * X, r * z * z); bad.append((a, b, Nn))
print("r=5, z=5 conic points (a<=b<400):", bad[:5])
