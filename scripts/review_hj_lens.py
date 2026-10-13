"""R174: P1 scope numerics of bsA_lens_homotopy_surgery: at n = m^2, count length-3 words (ordered, A in L3(n)) and how
many have A a non-square mod m^2 (<=> L(n,A) not homotopy equivalent to L(n,1), Whitehead: qq' == +-k^2, -1 square here).
Also checks Jacobi (A/n) = +1 on all of them."""
from math import gcd
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
for m in (5, 13, 17, 29, 3, 7, 15, 21):
    n = m * m; sq = {k * k % n for k in range(n) if gcd(k, n) == 1}
    words = [(t, u, v) for t in range(2, n) for u in range(2, n) for v in range(2, n // 2 + 2) if t * u * v - u - v == n]
    As = [t * u - 1 for t, u, v in words]
    nonsq = [A for A in As if A % n not in sq and (-A) % n not in sq]
    print(n, "|L3|=", len(As), "not homotopy-equiv to L(n,1):", len(nonsq), sorted(nonsq)[:6], "Jacobi:", {jac(A, n) for A in As})
