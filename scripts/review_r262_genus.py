"""R262: §2.3(a) check — for k | 6 all values coprime to 4k of a primitive form of disc -16k^2 p are congruent mod 4k;
for k ∤ 6 (k = 4, 5, 7) they generally are not.  Reduced primitive forms enumerated from scratch."""
import math
from sympy import primerange
res = {}
for k in (1, 2, 3, 6, 4, 5, 7):
    Dn = 16 * k * k  # disc = -Dn*p
    bad = tot = 0
    for p in primerange(5, 400):
        if p % 4 != 1:
            continue
        D = Dn * p
        for A in range(1, math.isqrt(D // 3) + 1):
            for B in range(-A + 1, A + 1):
                if (B * B + D) % (4 * A):
                    continue
                C = (B * B + D) // (4 * A)
                if C < A or (B < 0 and A == C) or math.gcd(math.gcd(A, B), C) != 1:
                    continue
                vals = {(A * x * x + B * x * y + C * y * y) % (4 * k) for x in range(-12, 13) for y in range(-12, 13)
                        if math.gcd(A * x * x + B * x * y + C * y * y, 4 * k) == 1}
                tot += 1
                bad += len(vals) > 1
    res[k] = (tot, bad)
print("k: (#reduced primitive forms, #forms whose coprime values are NOT all congruent mod 4k)", res)
