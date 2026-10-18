"""R283: O272 §2 positive control from scratch: [l is a 4th power mod q] as a function of the primary Gaussian lift
pi = a + bi of q (q = 1 mod 4) -- keys (a mod l, b mod l, a mod 8, b mod 8) and the coarser (a mod l, b mod l) (sign test)."""
from collections import defaultdict
from math import isqrt
from sympy import primerange
def primary(q):
    for a in range(1, isqrt(q) + 1, 2):
        b2 = q - a * a; b = isqrt(b2)
        if b * b == b2:
            for A in (a, -a):
                for B in (b, -b):
                    if (A % 4 == 1 and B % 4 == 0) or (A % 4 == 3 and B % 4 == 2):
                        return A, B
for l in (3, 5, 7, 11, 13):
    fine = defaultdict(set); coarse = defaultdict(set)
    for q in primerange(5, 300000):
        if q % 4 != 1 or q == l:
            continue
        a, b = primary(q)
        ev = pow(l, (q - 1) // 4, q) == 1
        fine[(a % l, b % l, a % 8, b % 8)].add(ev); coarse[(a % l, b % l)].add(ev)
    cf = sum(len(s) > 1 for s in fine.values()); cc = sum(len(s) > 1 for s in coarse.values())
    print(f"l={l}: fine keys {len(fine)} clashes {cf}; coarse keys (a,b mod l) {len(coarse)} clashes {cc}")
