"""Prop 4.1 check: n non-square, l = 3 (mod 4) with (n/l) = -1; forced q (4q = -1/n mod l), q = 1 (mod m):
fraction with -l an m-th power mod q (Chebotarev predicts 2/m; the quadratic part is forced to be trivial)."""
from sympy import primerange, legendre_symbol
for n, l in [(13, 7), (7, 11), (101, 7), (131, 11), (241, 7)]:
    assert l % 4 == 3 and legendre_symbol(n % l, l) == -1
    tc = (-pow(n, -1, l)) % l
    out = []
    for m in (2, 4, 8, 16):
        Q = [q for q in primerange(3, 400000) if q % m == 1 and q != l and (4 * q) % l == tc]
        good = sum(1 for q in Q if pow(q - l, (q - 1) // m, q) == 1)
        out.append(f"m={m}: {good}/{len(Q)} (pred {2/m:.3f})")
    print(n, l, "; ".join(out))
