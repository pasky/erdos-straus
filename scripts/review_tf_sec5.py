"""R206: Prop 5.1 of TORSION_FIRING by brute force: for odd n, d >= 1, prime h = -1 mod 4d, h !| nd,
y^2 = x^3 + n d x has full F_h-rational 2-torsion iff (n/h) = -1 (counting roots of x^2 + nd directly)."""
from sympy import primerange
bad = tot = 0
for h in primerange(3, 3000):
    if h % 4 != 3:
        continue
    roots_sq = {x * x % h for x in range(1, h)}
    for d in range(1, (h + 1) // 4 + 1):
        if (h + 1) % (4 * d):
            continue
        for n in list(range(1, 60, 2)) + [m * m for m in range(3, 30, 2)]:
            if (n * d) % h == 0:
                continue
            full = ((-n * d) % h) in roots_sq
            leg = pow(n % h, (h - 1) // 2, h) == h - 1
            tot += 1
            bad += (full != leg)
print("Prop 5.1 cases", tot, "failures", bad)
