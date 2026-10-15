"""O234: exact check of the overflow cube WITHOUT the exactness condition (Remark 1.3), at prime AND composite
moduli M = 3 mod 4 (Section 5).  For random M, random triples (c0,d0,R): c0,d0 odd squarefree coprime, c0*d0 | K=(M+1)/4,
rad R | c0, v_s(R) <= e; random prime p = -4 c0^2 d0 R^2 mod M with p not dividing R*M; verify
4/p = 1/x+1/y+1/z, x,y positive integers, den z = q^2, q odd, rad q | y, gcd(q,p)=1, v_s(q) <= e (Def 1.1).
usage: z10_cube_check.py Mmax trials e seed"""
import sys, random
from fractions import Fraction as Fr
from sympy import isprime, factorint, divisors
Mmax, trials, e, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
rng = random.Random(seed)
ok = bad = composite = nonexact = 0
def sqfree(n): return all(v == 1 for v in factorint(n).values())
while ok + bad < trials:
    M = rng.randrange(7, Mmax) | 3
    if rng.random() < 0.5: M = 4*9*25*rng.randrange(1, Mmax//900 + 2) - 1
    if M % 4 != 3: continue
    K = (M + 1) // 4
    ds = [d for d in divisors(K) if d % 2 and sqfree(d)]
    m = rng.choice(ds); fm = list(factorint(m))
    c0 = 1; d0 = 1
    for s in fm:
        if rng.random() < 0.6: c0 *= s
        else: d0 *= s
    R = 1
    for s in factorint(c0):
        R *= s ** rng.randrange(0, e + 1)
    V = c0 * c0 * d0 * R * R
    cls = (-4 * V) % M
    # find prime p in class
    p = None
    for _ in range(2000):
        t = cls + M * rng.randrange(1, 10**6)
        if isprime(t) and R % t and M % t: p = t; break
    if p is None: continue
    E, rem = divmod(p + 4 * V, M)
    assert rem == 0
    j = K // (c0 * d0)
    x = Fr(p + E, 4); y = Fr(p * c0 * d0 * j); z = Fr(p * x * j, c0 * R * R)
    good = x.denominator == 1 and x > 0 and y > 0 and z > 0 and Fr(4, p) == 1/x + 1/y + 1/z
    den = z.denominator
    if good:
        for s, v in factorint(den).items():
            if v % 2 or s == 2 or s == p or int(y) % s or v // 2 > e: good = False
    if good: ok += 1
    else: bad += 1; print("BAD", M, c0, d0, R, p)
    if not isprime(M): composite += 1
    if any(K % (q*q) == 0 for q in factorint(R)): nonexact += 1
print(f"Mmax={Mmax} e={e}: {ok} ok, {bad} bad, {composite} at composite moduli, {nonexact} non-exact (s^2 | K for some s | R)")
