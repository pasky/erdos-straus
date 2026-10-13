"""O169 Thm 4.5 brute-force check: every (t,u,v) >= 2 with n = tuv-u-v <= N, n = 1 (4), non-square or square:
Jacobi((tu-1)/n) = -1  <=>  [4|tu-1 or 4|tv-1 or 4|t or 4|u or 4|v]   (gcd(tu-1,n)=1 automatic).
Usage: uv run python scripts/dk_thm45_check.py N
"""
import sys
from math import isqrt
def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
N = int(sys.argv[1]); cnt = bad = sq = 0
t = 2
while 4 * t - 4 <= N:
    u = 2
    while 2 * (t * u - 1) - u <= N:
        A = t * u - 1; v = 2
        while (n := v * A - u) <= N:
            if n % 4 == 1:
                cnt += 1
                es = A % 4 == 0 or (t * v - 1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0
                j = jac(A, n)
                if (j == -1) != es: bad += 1
                if es and isqrt(n) ** 2 == n: sq += 1
            v += 1
        u += 1
    t += 1
print(f"N={N}: length-3 words with n=1(4): {cnt}, Thm 4.5 failures: {bad}, ES-slice words at squares: {sq}")
