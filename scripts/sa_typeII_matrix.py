"""O167: Type II <-> gamma=[[f,M],[c n,f']] in SL2(Z), M=4cd, f = f' = -1 (mod M).
Enumerate such gamma for odd n <= NMAX; check det, rebuild ES solution 4/n=1/x+1/y+1/z
exactly, and report: primes all have one; odd squares none (T1 control, ET Prop 1.6)."""
import sys
from fractions import Fraction
from sympy import isprime
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 600

def gammas(n):
    out = []
    for d in range(1, n // 4 + 2):
        for c in range(1, n + 2):
            M = 4 * c * d
            T = 4 * c * c * d * n + 1
            a = 1
            while True:
                f = M * a - 1
                if f * f > T:
                    break
                if T % f == 0:
                    fp = T // f
                    if (fp + 1) % M == 0:
                        assert f * fp - M * (c * n) == 1   # det gamma = 1
                        b = (fp + 1) // M
                        e = 4 * a * b * d - n               # ET: 4abd = n+e, a+b = ce
                        assert e > 0 and a + b == c * e
                        # ET Type II solution: x = abd·? -- rebuild via 4/n = 1/x+1/y+1/z
                        out.append((c, d, f, fp, a, b, e))
                a += 1
    return out

def es_check(n, sol):
    c, d, f, fp, a, b, e = sol
    # From 4abd = n+e and a+b = ce:  4/n = 1/(abd) + 1/(acdn) + 1/(bcdn)
    return Fraction(4, n) == Fraction(1, a*b*d) + Fraction(1, a*c*d*n) + Fraction(1, b*c*d*n)

bad = []
for n in range(5, NMAX + 1, 2):
    sq = int(n ** 0.5) ** 2 == n
    if not (isprime(n) or sq):
        continue
    G = gammas(n)
    assert all(es_check(n, s) for s in G)
    if isprime(n) and not G:
        bad.append(('prime-without', n))
    if sq and G:
        bad.append(('square-with', n))
print("NMAX", NMAX, "violations:", bad)
