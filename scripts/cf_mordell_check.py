# check CHI_FLIP 3.1: q in {3,5,7} non-residue mod p (p = 1 mod 4 prime) => word with A = q, chi = -1
from sympy import primerange
from cf_lib import jacobi, chi
bad = 0; n = 0
for p in primerange(5, 10**6):
    if p % 4 != 1: continue
    for q in (3, 5, 7, 11):
        if jacobi(q, p) != -1: continue
        t = (-pow(p, -1, q)) % q or q
        ok = (q + 1) % t == 0
        if ok:
            u = (q + 1) // t; As = (t * p + 1) // q; v = (As + 1) // t
            assert (t * p + 1) % q == 0 and (As + 1) % t == 0 and t*u*v-u-v == p and chi((t,u,v), p) == -1
        if q < 11 and not ok: bad += 1
        if q == 11 and not ok: assert p % 11 in (2, 6)
        n += 1
print("cases", n, "failures for q<=7:", bad)
