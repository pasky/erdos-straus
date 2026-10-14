#!/usr/bin/env python3
"""R217 from scratch: char-2 Frobenius family of FF_STERILE_PUSH §4 over F_2 (c = 1), polynomials as bit-ints.
k = 2m, A = T^{2m}; for each class u mod T^{2m} with u = 1 mod T^m, u != 1 mod T^{m+1}, take g' monic with
g' = (u-1)/T^m mod T^m (here: g' = that residue + T^m, so deg g' = m, T not| g'), E = 1 + T^m g'. For random P with
P = u (mod T^{2m}) and P = 1 (mod E g'), check: A g' | P + E, E | s = g' + X/g' (X = (P+E)/A), lc ok (char 2: lc = 1),
and the resulting A/P = 1/X + 1/Y + 1/Z with polynomial X, Y, Z (cross-multiplied identity)."""
import random
def mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r
def dm(a, b):
    q = 0; db = b.bit_length() - 1
    while a and a.bit_length() - 1 >= db:
        sh = a.bit_length() - 1 - db; q ^= 1 << sh; a ^= b << sh
    return q, a
def crt_lift(mod1, r1, mod2, r2, deg):
    # brute: random P of degree deg with P = r1 mod mod1 and P = r2 mod mod2 (search by adjusting low part via linear algebra would
    # be faster; we just construct P = r1 + mod1 * t and test random t)
    for _ in range(200000):
        t = random.getrandbits(deg - mod1.bit_length() + 1) | (1 << (deg - mod1.bit_length() + 1))
        P = r1 ^ mul(mod1, t)
        if dm(P, mod2)[1] == dm(r2, mod2)[1]: return P
    return None
random.seed(1); ok = 0; bad = 0
for m in (1, 2, 3):
    A = 1 << (2 * m)
    for ures in range(1 << (2 * m)):
        u = ures
        if dm(u ^ 1, 1 << m)[1] != 0 or dm(u ^ 1, 1 << (m + 1))[1] == 0: continue    # u = 1 mod T^m, != 1 mod T^{m+1}
        h = (u ^ 1) >> m                                  # (u-1)/T^m mod T^m (deg < m), h(0) = 1
        g = h ^ (1 << m)                                  # monic, deg m, g(0) = 1
        E = 1 ^ mul(1 << m, g)
        for trial in range(20):
            P = crt_lift(A, u, mul(E, g), 1, 40)
            if P is None: continue
            X, r = dm(P ^ E, A)
            c1 = (r == 0) and dm(X, g)[1] == 0
            b = dm(X, g)[0]; s = g ^ b
            kap, r2 = dm(s, E)
            c2 = (r2 == 0)
            if c1 and c2:
                Y = dm(mul(mul(kap, P), X), g)[0]; Z = mul(mul(kap, P), g)
                # A X Y Z == P (Y Z + X Z + X Y)
                c3 = mul(A, mul(X, mul(Y, Z))) == mul(P, mul(Y, Z) ^ mul(X, Z) ^ mul(X, Y))
            else: c3 = False
            ok += c1 and c2 and c3; bad += not (c1 and c2 and c3)
print(f'char-2 Frobenius families (F_2, k = 2, 4, 6): valid {ok}, invalid {bad}')
