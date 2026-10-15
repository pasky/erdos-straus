"""O234 §5: the exact ES^{(y,e)} class family at a modulus M ≡ 3 (mod 4) (prime or composite), A = (M+1)/4.
For D ≥ 1 and a prime p ≡ −4D (mod M), p ∤ D·M: E = (p+4D)/M, x = (p+E)/4, y = pA, z = p·x·A/D satisfy
4/p = 1/x+1/y+1/z with x, y ∈ Z_{>0}.  Claim (Prop 5.1): this is an ES^{(y,e)}(p) solution iff D ∈ 𝒟_e(M):
rad D | A, and for each prime s | D with t = v_s(D), σ = v_s(A): t ≤ 2σ, or (s odd, t even, t ≤ 2σ + 2e).
Tests random D (both in and outside 𝒟_e) against Def 1.1 with exact rationals.  usage: Mmax trials e seed"""
import sys, random, math
from fractions import Fraction as Fr
from sympy import isprime, factorint
Mmax, trials, e, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
def inD(D, A):
    for s, t in factorint(D).items():
        sg = A % s == 0 and factorint(A).get(s, 0)
        if not sg: return False
        if t <= 2 * sg: continue
        if s != 2 and t % 2 == 0 and t <= 2 * sg + 2 * e: continue
        return False
    return True
def esye(p, x, y, z):
    if not (x.denominator == 1 and x > 0 and y > 0 and z > 0 and Fr(4, p) == 1/x + 1/y + 1/z): return None
    for s, v in factorint(z.denominator).items():
        if v % 2 or s == 2 or p % s == 0 or int(y) % s or v // 2 > e: return False
    return True
agree = dis = ins = 0
while agree + dis < trials:
    M = rng.randrange(7, Mmax) | 3
    if rng.random() < 0.5: M = 4 * rng.choice([9, 25, 27, 45, 75, 81, 225, 7 * 9]) * rng.randrange(1, 40) - 1
    A = (M + 1) // 4; fA = factorint(A)
    D = 1
    for s, sg in fA.items():
        r = rng.random()
        if r < 0.4: continue
        D *= s ** rng.randrange(0, 2 * sg + 2 * e + 3)
    if rng.random() < 0.2: D *= rng.choice([3, 5, 7, 11, 13])
    if 4 * D >= 10 ** 15: continue
    p = None
    for _ in range(3000):
        t = (-4 * D) % M + M * rng.randrange(1, 10 ** 7)
        if isprime(t) and D % t and M % t: p = t; break
    if p is None: continue
    E, rem = divmod(p + 4 * D, M); assert rem == 0
    x = Fr(p + E, 4); y = Fr(p * A); z = p * x * A / D
    got = esye(p, x, y, z); assert got is not None, (M, D, p)
    pred = inD(D, A); ins += pred
    if got == pred: agree += 1
    else: dis += 1; print("DISAGREE", M, D, p, got, pred)
print(f"Mmax={Mmax} e={e}: {agree} agree, {dis} disagree; {ins} with D in 𝒟_e, {agree+dis-ins} outside")
