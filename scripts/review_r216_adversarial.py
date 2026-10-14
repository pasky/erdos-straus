"""R216: stacked-QR adversaries for PM-II. p ≡ 1 (mod 4·prod_{q<=Q} q), p prime; count slices (c,d), cd <= 200,
on which some PRIME h ≡ -1 (mod 4cd) divides M = p + 4c^2 d (prime-modulus Type II slice)."""
import sys
from sympy import isprime, factorint, primerange
from math import prod

def slices_firing(p, CD=200):
    k = 0
    for cd in range(1, CD + 1):
        for c in range(1, cd + 1):
            if cd % c: continue
            d = cd // c; m = 4 * cd
            M = p + 4 * c * c * d
            if any(q % m == m - 1 for q in factorint(M)):
                k += 1
    return k

if __name__ == "__main__":
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    for Q in (13, 17, 19, 23, 29):
        L = 4 * prod(primerange(2, Q + 1))
        out = []; t = 1
        while len(out) < first and t * L < 2 * 10 ** 11:
            p = t * L + 1
            if isprime(p):
                out.append((p, slices_firing(p)))
            t += 1
        print(Q, L, out)
