"""R216: naive brute force of Type II certificates for small n, to validate review_r216_census.c.
Certificate (c,d,h): h = 4cdj - 1, h | n + 4c^2 d.  For each c,d: divisors h of M = n + 4c^2 d with h ≡ -1 mod 4cd.
Bound: h >= 4cd - 1 and h <= M so 4cd - 1 <= n + 4c^2 d always possible -> need explicit bound:
from n = 4cdt - (c+t)/j >= 4cdt - c - t >= (4cd-1) - c  =>  c(4d-1) <= n + 1.
"""
import sys
from sympy import isprime, divisors

def certs(n):
    out = []
    d = 1
    while 3 * d <= n + 1:
        c = 1
        while c * (4 * d - 1) <= n + 1:
            M = n + 4 * c * c * d
            m = 4 * c * d
            for h in divisors(M):
                if h % m == m - 1:
                    out.append((c, d, h))
            c += 1
        d += 1
    return out

if __name__ == "__main__":
    N = int(sys.argv[1])
    for n in range(5, N + 1):
        if isprime(n) or (n % 2 == 1 and int(n ** 0.5) ** 2 == n):
            cs = certs(n)
            print(n, len(cs), sum(1 for (_, _, h) in cs if isprime(h)))
