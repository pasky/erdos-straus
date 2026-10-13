"""review_fms_affine.py A HMAX — R191 from-scratch check of FIXED_MODULUS_SHOTS Thm 2.1 / Cor 2.2 / Cor 2.3.

"h certifies through (alpha, beta)" (h odd, gcd(h, alpha*beta) = 1, h | alpha p + beta) iff exists c, j, t >= 1,
4cjt = h + 1, h | pj + c, i.e. (p ≡ -beta/alpha mod h)  alpha*c ≡ beta*j (mod h).
Computed directly from the definition (enumerate all (c, j) with cj | k), compared with the M-set prediction.
M-set (own implementation): c0/j0 = beta/alpha reduced -> c0*j0; if alpha | beta and 4 | beta/alpha: D = beta/(4 alpha),
D/c for c^2 | D; if beta | alpha and 4 | alpha/beta: E = alpha/(4 beta), E/j for j^2 | E.
"""
import sys
from math import gcd, isqrt

A = int(sys.argv[1]) if len(sys.argv) > 1 else 40
HMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 60000


def Mset(a, b):
    g = gcd(a, b)
    c0, j0 = b // g, a // g
    M = {c0 * j0}
    if b % (4 * a) == 0:
        D = b // (4 * a)
        M |= {D // c for c in range(1, isqrt(D) + 1) if D % (c * c) == 0}
    if a % (4 * b) == 0:
        E = a // (4 * b)
        M |= {E // j for j in range(1, isqrt(E) + 1) if E % (j * j) == 0}
    return M


pairs = [(a, b) for a in range(1, A + 1) for b in range(1, A + 1) if gcd(a, b) == 1]
Ms = {pr: Mset(*pr) for pr in pairs}
fail_a = 0
exc = 0
worst = (0, None)
exc_lines = 0
for h in range(3, HMAX + 1, 4):
    k = (h + 1) // 4
    dk = [d for d in range(1, k + 1) if k % d == 0] if k < 2000 else None
    if dk is None:
        dk = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                dk.append(i)
                if i * i != k:
                    dk.append(k // i)
            i += 1
    # residues c * j^{-1} mod h over cj | k
    R = set()
    for c in dk:
        for j in dk:
            if (k // c) % j == 0:
                R.add(c * pow(j, -1, h) % h)
    for (a, b) in pairs:
        if gcd(h, 2 * a * b) != 1:
            continue
        cert = (b * pow(a, -1, h)) % h in R
        pred = any((h + 1) % (4 * M) == 0 for M in Ms[(a, b)])
        if pred and not cert:
            fail_a += 1
            print("Thm 2.1(a) FAILS", a, b, h)
        if cert and not pred:
            exc += 1
            mu = max(a, b)
            assert h < 4 * mu ** 5, ("Thm 2.1(b) FAILS", a, b, h)
            if h / mu ** 2 > worst[0]:
                worst = (h / mu ** 2, (a, b, h))
            if (a, b) in [(1, 1), (1, 4), (4, 1)]:
                exc_lines += 1
print(f"{len(pairs)} coprime pairs, h <= {HMAX}: (a)-failures {fail_a}, (b)-exceptions {exc} (all < 4 mu^5), "
      f"max h/mu^2 = {worst[0]:.3f} at {worst[1]}, exceptions on the three lines: {exc_lines}")
# Cor 2.3: which pairs have 1 in M?
print("pairs with 1 in M:", [pr for pr in pairs if 1 in Ms[pr]])
# Cor 2.2: M >= sqrt(H)/2
for (a, b), M in Ms.items():
    H = max(a, b)
    assert all(4 * m * m >= H for m in M), (a, b, M)
print("Cor 2.2 (M >= sqrt(H)/2) holds for all pairs")
