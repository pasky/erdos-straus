# z50 shifts: finite check behind Lemma 5.0(b) for small coordinates c.
# For each c in [3, CMAX] and each family F in {V, W, T}, find n ≡ 1 (mod 8), n <= NMAX, such that the relevant
# integer (n+c for V, W; c*n+1 for T) equals 2^a * p with p an odd prime, a <= 3, and the event F_c FAILS.
# Failure then depends only on (a, p mod 8c), so one witness gives a positive density of primes p (PNT in APs).
# Usage: floorcheck.py CMAX NMAX [CMIN]  (CMIN=1 also tests W_1, W_2, T_1, T_2; V needs c in C_n).
# Prints the c for which no witness was found (expected: none, except c not in C_n for family V).
import sys
from sympy import isprime, divisors

CMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 64
CMIN = int(sys.argv[3]) if len(sys.argv) > 3 else 3
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 200000

def inC(w, n):
    return w >= 3 and (w % 4 == 0 or (w % 2 == 1 and (n + w) % 8 == 0))

def V_holds(c, n):
    return any((d + 1) % c == 0 for d in divisors(n + c))

def W_holds(c, n):
    m = n + c
    return any((B + 1) % c == 0 and inC(m // B, n) for B in divisors(m))

def T_holds(c, n):
    m = c * n + 1
    for A in divisors(m):
        B = m // A
        if (A + 1) % c == 0 and (B + 1) % c == 0:
            u, w = (A + 1) // c, (B + 1) // c
            if inC(u, n) or inC(w, n):
                return True
    return False

def shape(m):
    a = 0
    while m % 2 == 0:
        m //= 2; a += 1
    return a, m

bad = []
for c in range(CMIN, CMAX + 1):
    for fam, holds, integ in (("V", V_holds, lambda n: n + c), ("W", W_holds, lambda n: n + c),
                              ("T", T_holds, lambda n: c * n + 1)):
        if fam == "V" and not (c % 4 == 0 or c % 8 == 7):
            continue
        found = None
        for n in range(1, NMAX, 8):
            a, p = shape(integ(n))
            if a <= 3 and p > max(2 * c, 8) and isprime(p) and not holds(c, n):
                found = (n, a, p % (8 * c)); break
        if found is None:
            bad.append((c, fam))
print("no witness found for:", bad)
