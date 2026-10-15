"""O230 s5_cm_frobenius: (b) for M in {4, 8, 12}: h = -1 (mod M) and (h/p) = -1  <=>  h splits completely in
F_M = Q(zeta_M)^+(sqrt(p(theta^2-4))) but (p/h) = -1; F_4 = Q(sqrt(-p)), F_8 = Q(sqrt2, sqrt(-2p)), F_12 = Q(sqrt3, sqrt(-p)).
(c) every prime-modulus Type II certificate h | p + 4c^2 d, h = -1 (mod 4cd) of p = 1 (4) has (h/p) = -1."""
from sympy import primerange, legendre_symbol as L
PM, HM = 3000, 5000
bad = cnt = 0
for p in primerange(5, PM):
    if p % 4 != 1: continue
    for h in primerange(3, HM):
        if h == p: continue
        for M, gens in ((4, [-p]), (8, [2, -2 * p]), (12, [3, -p])):
            if M % h == 0: continue
            lhs = (h % M == M - 1) and L(h % p, p) == -1
            rhs = all(L(g % h, h) == 1 for g in gens) and L(p % h, h) == -1
            cnt += 1; bad += lhs != rhs
print("(b) checks", cnt, "mismatches", bad)
bad = cnt = 0
for p in primerange(5, PM):
    if p % 4 != 1: continue
    for c in range(1, 60):
        for d in range(1, 60):
            N = p + 4 * c * c * d
            for h in primerange(3, min(N, 4000) + 1):
                if N % h == 0 and h % (4 * c * d) == 4 * c * d - 1:
                    cnt += 1; bad += L(h % p, p) != -1
print("(c) PM-II certificates (c,d < 60, h < 4000)", cnt, "with (h/p) != -1:", bad)
