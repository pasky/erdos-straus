"""R128 from-scratch checks of O128 Lemma 1.1 (forms 1-5) against the independent brute force
scripts/review_t2s_brute.c (output file argv[1]).  Each form yields a SET of triples; we verify every
triple is a genuine Type II solution (exact rational check), the map is injective (no duplicates), and
the count equals brute f_II(n) => set equality.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_t2s_param.py brute.txt N1 N2"""
import sys, math
from fractions import Fraction as Fr
from sympy import isprime, divisors

def is_t2(n, t):
    x, y, z = t
    return Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z) and math.gcd(x, n) == 1 and y % n == 0 and z % n == 0

def form1(n):  # 4abcd = a+b+nc, gcd(a,b,c)=1, gcd(abd,n)=1.  4ab <= n+e <= n+a+b bounds a,b.
    L = []
    for a in range(1, n + 2):
        if 4 * a - a - 1 > n: break
        for b in range(1, n + 2):
            if 4 * a * b - a - b > n: break
            for c in divisors(a + b):  # c | a+b from 4abcd = a+b+nc
                num = a + b + n * c
                if num % (4 * a * b * c): continue
                d = num // (4 * a * b * c)
                if math.gcd(math.gcd(a, b), c) != 1 or math.gcd(a * b * d, n) != 1: continue
                L.append((a * b * d, a * c * d * n, b * c * d * n))
    return L

def form2(p):  # e f - 4a^2 d = p, f = 4acd-1, gcd(a,c)=1, b = ce-a.  Bound: 4ad*b = p+e <= 2p.
    L = []
    for a in range(1, p + 1):
        if 4 * a > 2 * p: break
        for d in range(1, 2 * p // (4 * a) + 1):
            for c in range(1, p + 1):
                f = 4 * a * c * d - 1
                if f > p + 4 * a * a * d: break
                if (p + 4 * a * a * d) % f or math.gcd(a, c) != 1: continue
                e = (p + 4 * a * a * d) // f
                b = c * e - a
                assert b >= 1
                L.append((a * b * d, a * c * d * p, b * c * d * p))
    return L

def form3(p):  # f f' - 4c^2 dp = 1, f == f' == -1 (4cd), gcd((f+1)/4cd, c) = 1
    L = []
    for c in range(1, p + 1):
        for d in range(1, p + 1):
            m = 4 * c * d
            N = 4 * c * c * d * p + 1
            if (m - 1) ** 2 > N: break  # f, f' >= m-1 (rigorous; increasing in d)
            for f in divisors(N):
                if (f + 1) % m or (N // f + 1) % m: continue
                a, b = (f + 1) // m, (N // f + 1) // m
                if math.gcd(a, c) != 1: continue
                L.append((a * b * d, a * c * d * p, b * c * d * p))
    return L

def form4(p):  # (4acd-1) | (a + pc), gcd(a,c)=1
    L = []
    for a in range(1, p + 1):
        for c in range(1, p + 1):
            if 4 * a * c - 1 > a + p * c: break
            for d in range(1, p + 1):
                f = 4 * a * c * d - 1
                if f > a + p * c: break
                if (a + p * c) % f or math.gcd(a, c) != 1: continue
                b = (a + p * c) // f
                L.append((a * b * d, a * c * d * p, b * c * d * p))
    return L

def form5(p):  # e = least positive residue of -p mod 4ab divides a+b, gcd(a,(a+b)/e)=1
    L = []
    for a in range(1, p + 1):
        for b in range(1, p + 1):
            if 4 * a * b - a - b > p: break
            e = (-p) % (4 * a * b) or 4 * a * b
            if (a + b) % e: continue
            c = (a + b) // e
            if math.gcd(a, c) != 1: continue
            d = (p + e) // (4 * a * b)
            L.append((a * b * d, a * c * d * p, b * c * d * p))
    return L

if __name__ == "__main__":
    brute = {int(l.split()[0]): int(l.split()[1]) for l in open(sys.argv[1])}
    N1, N2 = int(sys.argv[2]), int(sys.argv[3])
    bad = tot = 0
    for n in range(2, N1 + 1):
        forms = [("form1", form1)]
        if isprime(n) and 5 <= n <= N2:
            forms += [("form2", form2), ("form3", form3), ("form4", form4), ("form5", form5)]
        for name, F in forms:
            L = F(n)
            ok = len(set(L)) == len(L) and all(is_t2(n, t) for t in L) and len(L) == brute[n]
            if not ok:
                bad += 1; print(name, "MISMATCH n=", n, len(L), len(set(L)), brute[n])
        tot += brute[n]
    print(f"n<={N1}: form1 vs brute; primes 5..{N2}: forms 2-5; total f_II {tot}; mismatches {bad}")
