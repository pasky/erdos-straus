"""z52d pass2 TO0b Z0060: Z analogue of Bradford-Ionascu Thm 3.1 (arXiv:1405.4025 eq. (9)): which n have 4/n = 1/a + 1/b over Z?
Criterion (derived here): 4/n = 1/a+1/b  <=>  (4a-n)(4b-n) = n^2, so a solution exists iff n^2 has a divisor d with
d = 4a - n, i.e. d = -n (mod 4) and n^2/d = -n (mod 4) (both positive). For prime p: p = 3 (mod 4) iff 2-term solvable.
Also checks the BI identity 4 = 1/u + 1/ubar with u = -4+3*sqrt2 (Tr u / N u = -8/-2 = 4)."""
import sys
sys.path.insert(0, 'scripts')
from fractions import Fraction as Fr
def two_term(n):
    m = n * n
    divs = [d for d in range(1, m + 1) if m % d == 0] if m < 10**6 else None
    for d in divs:
        if (d + n) % 4 == 0 and (m // d + n) % 4 == 0:
            a = (d + n) // 4; b = (m // d + n) // 4
            if Fr(1, a) + Fr(1, b) == Fr(4, n): return (a, b)
    return None
def isprime(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
P = [p for p in range(3, 400) if isprime(p)]
ok = all((two_term(p) is not None) == (p % 4 == 3) for p in P)
print('primes 3..399: 2-term 4/p = 1/a+1/b solvable iff p = 3 mod 4 :', ok, ' (count solvable', sum(1 for p in P if two_term(p)), 'of', len(P), ')')
print('non-prime examples: 4/9 =', two_term(9), '; 4/15 =', two_term(15), '; 4/21 =', two_term(21))
# BI identity in Z[sqrt2]: u = -4+3 sqrt2, ubar = -4-3 sqrt2: u + ubar = -8, u*ubar = 16-18 = -2 -> 1/u+1/ubar = -8/-2 = 4
print('BI identity check: (u+ubar)/(u*ubar) =', Fr(-8, -2), '= 4')
