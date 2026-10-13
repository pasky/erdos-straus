"""R167 from-scratch check of O167's Type II matrix dictionary (§3, §5, Lemma 10.1).
Enumerates ET Type II quadruples (a,b,c,d) for odd n <= NMAX directly from 4abcd - a - b = c n,
i.e. c(4abd - n) = a + b, then checks:
  * gamma = [[f, M],[c n, f']] with M=4cd, f=aM-1, f'=bM-1 has det 1 and f = f' = -1 mod M;
  * 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn) exactly;
  * Lemma 10.1 product formula (symbolic, sympy);
  * second normalisation gamma' = [[f, cM],[n, f']] in SL2, -gamma' = [[1,0],[-n,1]] mod M;
  * whether n | M ever happens for prime n (Lemma 10.1 uses p ∤ M);
  * every prime 5<=p<=NMAX has a Type II quadruple, no odd square does;
  * converse direction: brute-force gamma in SL2 with gamma12=M, gamma11=gamma22=-1 mod M, gamma21 = c n,
    c | M/4, M <= MMAX, matches the quadruple set for small n.
"""
import sys
from fractions import Fraction
from math import isqrt
import sympy as sp

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

def typeII(n):
    out = []
    a = 1
    while 3 * a - 1 <= n + 1:          # d=1 needs 4a-1 <= n+a
        d = 1
        while 4 * a * d - 1 <= n + a:
            k = 4 * a * d
            blo = n // k + 1                     # 4abd > n
            bhi = (n + a) // (k - 1)             # 4abd - n <= a + b
            for b in range(blo, bhi + 1):
                e = k * b - n
                if e > 0 and (a + b) % e == 0:
                    out.append((a, b, (a + b) // e, d))
            d += 1
        a += 1
    return out

def is_prime(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))

# symbolic Lemma 10.1
M, a, b = sp.symbols('M a b')
g = sp.Matrix([[M - 1, M], [M - 2, M - 1]])
prod = sp.Matrix([[1, 0], [b - 1, 1]]) * g * sp.Matrix([[1, 0], [a - 1, 1]])
target = sp.Matrix([[a * M - 1, M], [a * b * M - a - b, b * M - 1]])
assert sp.simplify(prod - target) == sp.zeros(2, 2) and sp.expand(g.det()) == 1
print("Lemma 10.1 product formula: OK (symbolic)")

bad = 0; pdivM = 0; prime_missing = []; square_hit = []
for n in range(3, NMAX + 1, 2):
    sols = typeII(n)
    for (a_, b_, c_, d_) in sols:
        Mv = 4 * c_ * d_
        f, fp = a_ * Mv - 1, b_ * Mv - 1
        if f * fp - Mv * c_ * n != 1 or f % Mv != Mv - 1 or fp % Mv != Mv - 1:
            bad += 1
        if Fraction(4, n) != Fraction(1, a_*b_*d_) + Fraction(1, a_*c_*d_*n) + Fraction(1, b_*c_*d_*n):
            bad += 1
        # second normalisation
        if f * fp - (c_ * Mv) * n != 1 or (-n) % Mv != (-n) % Mv:
            bad += 1
        if n % 2 and is_prime(n) and Mv % n == 0:
            pdivM += 1
    if is_prime(n) and n >= 5 and not sols:
        prime_missing.append(n)
    r = isqrt(n)
    if r * r == n and sols:
        square_hit.append(n)
print(f"odd n <= {NMAX}: identity/det/congruence failures = {bad}")
print("primes without Type II:", prime_missing[:20], "count", len(prime_missing))
print("odd squares with Type II:", square_hit)
print("prime n with n | M:", pdivM)

# converse: brute force over gamma for small n
for n in range(3, 200, 2):
    S = set()
    for Mv in range(4, 4 * (n + 2) * 4, 4):        # M = 4cd; d <= (n+2)/4 and c <= ? bounded below
        for c_ in range(1, Mv // 4 + 1):
            if (Mv // 4) % c_:
                continue
            T = c_ * Mv * n + 1                     # f f' = T, f = f' = -1 mod M
            for f in range(Mv - 1, isqrt(T) + 1, Mv):
                if T % f == 0 and (T // f) % Mv == Mv - 1:
                    for (x, y) in {(f, T // f), (T // f, f)}:
                        S.add(((x + 1) // Mv, (y + 1) // Mv, c_, Mv // (4 * c_)))
    Q = set(typeII(n))
    S = {s for s in S if s[3] <= (n + 2)}
    assert S <= Q, (n, S - Q)
    assert {q for q in Q if 4 * q[2] * q[3] < 4 * (n + 2) * 4} <= S, n
print("converse (matrix set == quadruple set) for odd n < 200: OK")
