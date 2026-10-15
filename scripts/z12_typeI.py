"""O236 goal 4: Type I-shape windows have no forced firing (CAP_POINTWISE Prop 4.1).

Type I shape: x = p*a, k' := (4a-1)/p prime, y = a*w, z = a*w/(k'w - 1).  A mute solution needs
D = k'w - 1 = G*q^2, G = gcd(D, a), q odd, rad q | a.  Prop 4.1: if every odd prime s | a has (s/p) = +1 and
(a odd or k' = 7 mod 8), there is none.  Checks: (1) (s/k') == (s/p) for all odd s | a; (2) brute force over
w <= W finds no solution in the predicted-empty windows, and finds solutions in many others;
(3) statistics of forced-empty windows.
usage: z12_typeI.py P K W
"""
import sys
from math import gcd, isqrt
from sympy import factorint, jacobi_symbol, primerange

P, KM, W = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
chk = empty_pred = empty_viol = found = 0
for p in primerange(5, P + 1):
    if p % 4 != 1:
        continue
    for k in primerange(3, KM + 1):
        if (p * k + 1) % 4 or k == p:
            continue
        a = (p * k + 1) // 4
        f = factorint(a)
        for s in f:
            if s > 2:
                assert jacobi_symbol(s, k) == jacobi_symbol(s, p)
                chk += 1
        pred_empty = all(jacobi_symbol(s, p) == 1 for s in f if s > 2) and (a % 2 == 1 or k % 8 == 7)
        sol = False
        for w in range(1, W + 1):
            D = k * w - 1
            G = gcd(D, a)
            r = D // G
            q = isqrt(r)
            if q * q == r and q % 2 == 1 and all(a % l == 0 for l in factorint(q)):
                sol = True
                break
        if pred_empty:
            empty_pred += 1
            empty_viol += sol
        else:
            found += sol
print(f"(s/k')==(s/p) checks: {chk}; predicted-empty windows: {empty_pred}, violations: {empty_viol}; "
      f"other windows with a solution (w <= {W}): {found}")
