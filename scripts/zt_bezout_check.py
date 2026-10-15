"""zt_bezout_check.py (O227): numerical check of FF_THIRDS_CORNER Prop 5.1 (q = 3): for random monic M (T∤M) and N > deg M,
with Z = T^{-N} mod M: c(T^N Z - 1)/M == trunc_N(-c M^{-1}) and T*M*g' - 1 == c T^{N+1} Z - (1 + cT)."""
import random
from zt_poly import add, mul, sub, divmod_, mono, sinv, trunc, norm, neg

def egcd_inv(a, m):
    r0, r1, s0, s1 = m, divmod_(a, m)[1], [], [1]
    while r1:
        q, r = divmod_(r0, r1)
        r0, r1, s0, s1 = r1, r, s1, sub(s0, mul(q, s1))
    assert len(r0) == 1
    inv0 = pow(r0[0], 1, 3)  # r0 constant; 1/r0 = r0 in F_3
    return divmod_(mul(s0, [inv0]), m)[1]

rng = random.Random(7); n = 0
for _ in range(3000):
    d = rng.randrange(1, 9); N = rng.randrange(d + 1, 20); c = rng.choice([1, 2])
    M = [rng.choice([1, 2])] + [rng.randrange(3) for _ in range(d - 1)] + [1]
    Z = egcd_inv(mono(N), M)
    q, r = divmod_(sub(mul(mono(N), Z), [1]), M); assert not r
    g = mul([c], q)
    assert g == trunc(mul([(-c) % 3], sinv(M, N)), N)
    E = sub(mul(mul([0, 1], M), g), [1])
    assert E == sub(mul([c], mul(mono(N + 1), Z)), [1, c])
    n += 1
print("Prop 5.1 identities verified on", n, "random (M, N, c)")
