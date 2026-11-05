# z58 LOGIC: independent decision of R(n) >= 1 by divisor enumeration (not the sieve).
# Any solution of 4uBC - u - B = n has m := min(u, B, C) with 4m^3 - 2m <= n. For each m:
#   C = m : (4Cu-1)(4CB-1) = 4Cn+1, need a divisor d = -1 (mod 4C), d >= 4C-1, cofactor >= 4C-1;
#   u = m : d := 4uC-1 divides n+u, d = -1 (mod 4u), d >= 4u-1, B = (n+u)/d >= 1;
#   B = m : d := 4BC-1 divides n+B, d = -1 (mod 4B), d >= 4B-1, u = (n+B)/d >= 1.
# usage: uv run --with sympy python scripts/z58_logic_check.py file_of_n   (prints "n R>=1?" per line)
import sys
from sympy import divisors
def hit(n):
    m = 1
    while 4 * m ** 3 - 2 * m <= n:
        q = 4 * m
        N = q * n + 1
        for d in divisors(N):
            if d % q == q - 1 and (N // d) % q == q - 1: return True
        for x in (n + m,):
            for d in divisors(x):
                if d >= q - 1 and d % q == q - 1: return True
        m += 1
    return False
for l in open(sys.argv[1]):
    n = int(l); print(n, int(hit(n)))
