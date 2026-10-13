"""R174: from-scratch recount for HJ_DEEP Prop 2.1/2.2 evidence. For odd n < NMAX enumerate Type II tuples (a<=b, c, d)
with 4abd = n + e, e >= 1, a + b = c e (loop over a<=b, then the d-window (n+1)/(4ab) <= d <= (n+a+b)/(4ab)).
Check: exact ES identity, K(a,4cd,b) = c n, sign law (A/n) = -(-1/n) for A = 4cd*u - 1 in both orientations, for ALL odd
non-square n (not only primes); count at primes; count at odd squares (must be 0)."""
import sys
from fractions import Fraction as F
from math import isqrt
def jac(a, n):
    a %= n; s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: s = -s
        a %= n
    return s if n == 1 else 0
def isprime(n): return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))
N = int(sys.argv[1]); nprime = 0; table = {}; sq = 0; bad = 0; allodd_bad = 0; allodd = 0
for n in range(3, N, 2):
    pr = isprime(n); issq = isqrt(n) ** 2 == n
    a = 1
    while 4 * a * a <= n + 2 * a:
        b = a
        while 4 * a * b <= n + a + b:
            for d in range(max(1, -(-(n + 1) // (4 * a * b))), (n + a + b) // (4 * a * b) + 1):
                e = 4 * a * b * d - n
                if e < 1 or (a + b) % e: continue
                c = (a + b) // e
                if issq: sq += 1; continue
                ok = F(4, n) == F(1, a*b*d) + F(1, a*c*d*n) + F(1, b*c*d*n) and 4*c*d*a*b - a - b == c * n
                bad += not ok
                for u in (a, b):
                    A = 4 * c * d * u - 1; s = jac(A, n); allodd += 1
                    if s != -jac(n - 1, n): allodd_bad += 1
                    if pr: table[(n % 4, s)] = table.get((n % 4, s), 0) + 1
                if pr: nprime += 1
            b += 1
        a += 1
print(f"primes<{N}: Type II tuples (a<=b) {nprime}; identity failures {bad}; sign table {table}")
print(f"all odd non-square n<{N}: {allodd} oriented words, sign-law failures {allodd_bad}; tuples at odd squares: {sq}")
