"""R232: FROM-SCRATCH numerical check of STERILE_LOWER Lemma 4.3 (U-V factorisation) on all P-data of N = r^{2L-1}
for small r, L, with many (p, q) satisfying q a == p b (mod W = r^L)."""
import random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_r232_level1 import P_data
random.seed(232)
tested = hyp = 0
for r, L in [(3, 2), (3, 3), (5, 2), (7, 2), (11, 2), (13, 2), (17, 2), (19, 2), (3, 4), (5, 3)]:
    N = r ** (2 * L - 1); W = r ** L
    for (a, b, c, d) in P_data(N):
        if a % r == 0 or b % r == 0 or c % r == 0 or d % r == 0: continue
        e = (a + b) // c
        for _ in range(30):
            q = random.randint(1, 60)
            p = (q * a * pow(b, -1, W)) % W - W * random.randint(0, 2)
            if random.random() < 0.5 and p > -W: p -= W
            z, rem = divmod(q * a - p * b, W); assert rem == 0
            num = (p + q) ** 2 + 4 * r * d * z * z
            assert num % e == 0, (r, L, a, b, c, d, p, q)          # G integral
            G = num // e; U = G * a - c * p * p; V = G * b - c * q * q
            assert U * b == c * q * q * a + r * z * z and V * a == c * p * p * b + r * z * z
            assert U > 0 and V > 0 and U * V == c * c * p * p * q * q + G * r * z * z
            tested += 1
            if b <= N / (2 * (abs(p) + q) ** 2):
                hyp += 1; assert e <= 4 * q * q * a, (r, L, a, b, c, d, p, q)
# the worked example of the text
a, b, c, d, p, q, r = 1, 78, 1, 16, -11, 9, 17
z = (q * a - p * b) // 289; G = ((p + q) ** 2 + 4 * r * d * z * z) // ((a + b) // c)
print("example:", z, G, G * a - c * p * p, G * b - c * q * q)
print(f"tested {tested} (datum, p, q) instances; size hypothesis met in {hyp}; all identities hold")
