# ec_xstar.py — the k=9 near-square point x*: x*_2 = 1, x*_q = 289 if v2(ord_q 2) <= 2, x*_q = -287 if v2(ord_q 2) = 3.
# Search ET classes (mordell_lib) of modulus M <= Mmax whose odd primes all have level <= 3 and which contain x*.
import sys
import mordell_lib as ML
from ec_screen import primes_upto
Mmax = int(sys.argv[1])
P = primes_upto(Mmax)
def lev(q):
    o = q - 1
    for p in ML.factor_small(q - 1):
        while o % p == 0 and pow(2, o // p, q) == 1:
            o //= p
    v = 0
    while o % 2 == 0:
        o //= 2; v += 1
    return v
LV = {q: lev(q) for q in P if q > 2}
def leg(a, q):
    a %= q
    return 0 if a == 0 else (1 if pow(a, (q - 1) // 2, q) == 1 else -1)
good3 = [q for q in LV if LV[q] == 3 and leg(-287, q) == -1]
print('level-3 primes with (-287/q) = -1:', good3[:12])
def xstar_mod(M):
    r, mod = 0, 1
    for q, e in ML.factor_small(M).items():
        Q = q ** e
        if q == 2:
            v = 1
        elif LV[q] <= 2:
            v = 289
        elif LV[q] == 3:
            v = -287
        else:
            return None
        v %= Q
        r = r + mod * (((v - r) * pow(mod, -1, Q)) % Q)
        mod *= Q
    return r % M
cnt = 0
for q in good3:
    for t in range(1, Mmax // q + 1):
        M = q * t
        if M % 4 not in (0, 3):
            continue
        x = xstar_mod(M)
        if x is None:
            continue
        cnt += 1
        for fam, Pp in ML.iter_classes(M):
            if x in ML.cls_modulus_residues(fam, Pp)[1]:
                print('FOUND', M, fam, Pp, ML.factor_small(M)); sys.exit()
print('none; moduli tried', cnt)
