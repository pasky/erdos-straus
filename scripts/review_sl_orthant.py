"""R175: orthant counts for X_n: cfg - c - f = n, fg = 1 mod 4, n = 1 mod 4 <= NMAX; check sign formula
((cg-1)/n) = -sgn(c) and that orthant points <-> D*(n) classes (t = g, m'' = cg - 1 resp. |c|g + 1)."""
import sys
from review_sl_rayclass import jac
NMAX = int(sys.argv[1]); pos = neg = bad = 0; dstar = {1: 0, -1: 0}
for n in range(1, NMAX + 1, 4):
    for g in range(1, 4 * n + 8):
        for f in range(1, 4 * n + 8):
            # positive orthant: c (fg-1) = n + f
            if (f * g) % 4 == 1 and f * g > 1 and (n + f) % (f * g - 1) == 0:
                c = (n + f) // (f * g - 1); pos += 1
                if jac(c * g - 1, n) != -1 and n > 1: bad += 1
            # negative orthant c, f <= -1 (f' = -f, so f'g = 3 mod 4): c'(f'g + 1) = n - f'
            if (f * g) % 4 == 3 and n - f > 0 and (n - f) % (f * g + 1) == 0:
                neg += 1
                cp = (n - f) // (f * g + 1)
                if jac(-cp * g - 1, n) != 1 and n > 1: bad += 1
    # D*(n) from the divisor side
    for t in range(3, n + 3, 4):
        M = t * n + 1
        for d in range(2, M + 1):
            if M % d == 0 and (M // d) % 4 == 0 and d % t in (1, t - 1):
                dstar[1 if d % t == 1 else -1] += 1
print("n<=", NMAX, "positive orthant", pos, "negative orthant", neg, "D* class -1", dstar[-1], "class +1", dstar[1], "sign violations", bad)
