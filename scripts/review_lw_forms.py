"""R180: from-scratch check of LORENZINI_W §1 forms F1-F4 (as literally stated) vs brute force."""
import sys
from math import gcd
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
def W(n):
    for x in range(2, n + 3):
        for z in range(x, n + 3):
            if 2 * x * z - x - z > n: break   # y=2 minimal
            if (n + x + z) % (x * z) == 0 and (n + x + z) // (x * z) >= 2: return True
    return False
def F1(n):
    return any((n+x+z) % (x*z) == 0 and (n+x+z)//(x*z) >= 2 for x in range(2, n+3) for z in range(2, n+3) if x*z <= n+x+z)
def F2_literal(n):
    for z in range(2, n + 3):
        q = -(-n // z); r = q * z - n
        if r >= 2 and (q + 1) % r == 0 and (q + 1) // r >= 2: return True
    for x in range(2, n + 1):   # diagonal as literally stated: x|n, x|n/x+2  (no y>=2)
        if n % x == 0 and (n // x + 2) % x == 0: return True
    return False
def F2_fixed(n):
    for z in range(2, n + 3):
        q = -(-n // z); r = q * z - n
        if r >= 2 and (q + 1) % r == 0 and (q + 1) // r >= 2: return True
    for x in range(2, n + 1):
        if n % x == 0 and (n // x + 2) % x == 0 and (n // x + 2) // x >= 2: return True
    return False
def F3(n):
    for d in range(3, n + 3):
        rho = (-n) % d
        if rho >= 2 and (d + 1) % rho == 0 and 2 * rho <= d + 1 and n + rho >= 2 * d: return True
    return False
def F4(n):
    if n < 2: return False
    for a in range(1, n):
        if gcd(a, n) != 1: continue
        ab = pow(a, -1, n)
        if (a * ab - 1) % n: continue
        b = (a * ab - 1) // n
        if b >= 2 and (a + 1) % b == 0 and (ab + 1) % b == 0 and a >= 2 * b - 1 and ab >= 2 * b - 1: return True
    return False
mm = {k: [] for k in ["F1", "F2lit", "F2fix", "F3", "F4"]}
for n in range(2, N):
    w = W(n)
    for k, f in [("F1", F1), ("F2lit", F2_literal), ("F2fix", F2_fixed), ("F3", F3), ("F4", F4)]:
        if (k == "F1" and n > 400): continue
        if f(n) != w: mm[k].append(n)
print({k: v[:20] for k, v in mm.items()})
