"""review_zl_lemma43.py -- R231, FROM SCRATCH: brute-force check of STERILE_LOWER Lemma 4.3 (U-V factorisation)
over all P-data (a,b,c,d,e) of N = r^{2L-1} (4abd = N+e, a+b = ce, a<=b, r∤ab) and many (p,q) with qa - pb = zW, W = r^L."""
import random
from fractions import Fraction
random.seed(231)
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
tests = hyp = 0
for r, L in [(3, 2), (3, 3), (5, 2), (7, 2), (11, 2), (13, 2), (17, 2), (19, 2), (23, 2), (5, 3)]:
    N, W = r ** (2 * L - 1), r ** L
    for (a, b, c, d, e) in P_data(N):
        if a % r == 0 or b % r == 0: continue
        binv = pow(b, -1, W)
        for _ in range(30):
            q = random.randint(1, 3 * W)
            p = (q * a * binv) % W + W * random.randint(-3, 3)
            assert (q * a - p * b) % W == 0
            z = (q * a - p * b) // W
            Gn = (p + q) ** 2 + 4 * r * d * z * z
            assert Gn % e == 0, ("G not integral", r, L, a, b, c, d, e, p, q)
            G = Gn // e
            U, V = G * a - c * p * p, G * b - c * q * q
            assert U * b == c * q * q * a + r * z * z and V * a == c * p * p * b + r * z * z
            assert U > 0 and V > 0 and U * V == c * c * p * p * q * q + G * r * z * z
            tests += 1
            if 2 * (abs(p) + q) ** 2 * b <= N:
                hyp += 1; assert e <= 4 * q * q * a, ("e bound fails", r, L, a, b, e, p, q)
# the worked example
a, b, c, d, r, p, q = 1, 78, 1, 16, 17, 11, 9
N, W = 17 ** 3, 17 ** 2
e = 4 * a * b * d - N; z = (q * a + p * b) // W   # u = 11/9 written as -p'/q with p' = -11
print("example: e", e, "z", z, "u = 11/9 mod 17 =", 11 * pow(9, -1, 17) % 17, "; box -f mod 289 =", (-(4*a*c*d-1)) % 289,
      "; 11/9 mod 289 =", 11 * pow(9, -1, 289) % 289)
print(f"Lemma 4.3: {tests} (datum, p, q) instances OK; e<=4q^2a hypothesis met in {hyp}, never violated")
# targeted: all small (p,q) satisfying the congruence, to exercise the e <= 4 q^2 a implication
hyp2 = 0
for r, L in [(3, 2), (3, 3), (5, 2), (7, 2), (3, 4), (5, 3), (17, 2)]:
    N, W = r ** (2 * L - 1), r ** L
    for (a, b, c, d, e) in P_data(N):
        if a % r == 0 or b % r == 0: continue
        for q in range(1, 60):
            for p in range(-60, 61):
                if (q * a - p * b) % W or 2 * (abs(p) + q) ** 2 * b > N: continue
                z = (q * a - p * b) // W; G = ((p + q) ** 2 + 4 * r * d * z * z) // e
                assert ((p + q) ** 2 + 4 * r * d * z * z) % e == 0
                assert (G * a - c * p * p) * (G * b - c * q * q) == c * c * p * p * q * q + G * r * z * z
                assert e <= 4 * q * q * a; hyp2 += 1
print("targeted small (p,q) with the size hypothesis:", hyp2, "instances, e <= 4q^2a never violated")
