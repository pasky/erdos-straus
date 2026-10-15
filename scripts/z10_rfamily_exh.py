"""O234: exhaustive version of z10_rfamily_check: all M ≡ 3 (4) < Mmax, all D < M/4, the least prime p ≡ −4D (M)
with p ∤ DM and p > 4D: predicate D ∈ 𝒟_e(M) vs Def 1.1 of the Prop 5.1 solution.  usage: Mmax e"""
import sys
from fractions import Fraction as Fr
from sympy import isprime, factorint
Mmax, e = int(sys.argv[1]), int(sys.argv[2]); agree = dis = 0
for M in range(3, Mmax, 4):
    A = (M + 1) // 4; fA = factorint(A)
    for D in range(1, (M - 1) // 4 + 1):
        pred = all(fA.get(s, 0) and (t <= 2 * fA[s] or (s != 2 and t % 2 == 0 and t <= 2 * fA[s] + 2 * e))
                   for s, t in factorint(D).items())
        if __import__("math").gcd(D, M) > 1: continue
        p = (-4 * D) % M
        while not (isprime(p) and D % p and M % p and p > 4 * D): p += M
        E = (p + 4 * D) // M; x = Fr(p + E, 4); y = Fr(p * A); z = p * x * A / D
        assert x.denominator == 1 and Fr(4, p) == 1 / x + 1 / y + 1 / z
        got = all(v % 2 == 0 and s != 2 and p % s and int(y) % s == 0 and v // 2 <= e for s, v in factorint(z.denominator).items())
        if got == pred: agree += 1
        else: dis += 1; print("DIS", M, D, p)
print(f"exhaustive M<{Mmax}, e={e}: {agree} agree, {dis} disagree")
