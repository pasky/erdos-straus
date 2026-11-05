"""z58 LIT: transfer of Ventas arXiv:2610.41027 Thm 3.1 (modular inversion of Grid patterns) to (★).

Claim (elementary): for odd d ≡ 3 (mod 4) put H_d = {x mod d : x ≡ -r, 1 ≤ r < d, r | (d+1)/4}.
Then x ∈ H_d  <=>  (4x)^{-1} mod d ∈ H_d  (r <-> r' = (d+1)/(4r)).
Checks: (1) the per-d involution on H_d for all d ≤ 20000; (2) action of x -> (4x)^{-1} on the
Mordell classes mod 105 (the odd part of 840); (3) squares map to squares.
Run: timeout 600 uv run python scripts/z58_lit_inversion.py
"""
from math import gcd

def H(d):
    q = (d + 1) // 4
    return {(-r) % d for r in range(1, d) if q % r == 0}

bad = 0
for d in range(3, 20001, 4):
    h = H(d)
    for x in h:
        if gcd(x, d) != 1:
            bad += 1; continue
        y = pow(4 * x % d, -1, d)
        if y not in h:
            bad += 1
print("per-d involution violations for d<=20000:", bad)

M = [1, 121, 169, 289, 361, 529]
for a in M:
    a105 = a % 105
    b105 = pow(4 * a105 % 105, -1, 105)
    partner = [c for c in M if c % 105 == b105]
    print(f"class {a} (mod105={a105}) -> (4a)^-1 mod 105 = {b105}; Mordell partner(s) {partner}")
# squares to squares: (4 m^2)^{-1} = ((2m)^{-1})^2
print("square check: (4*m^2)^-1 is the square of (2m)^-1 -- identity")
