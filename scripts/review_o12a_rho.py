"""R45a: brute-force root counts of the shifted polynomials in Lemma 4.1.

Quadratic: Q(a') = (4d (q a' + x0)^2 + 1)/q for odd prime powers q=l^i, l not | d,
x0 a root of 4d x^2+1 mod q.  Checks rho_Q(p^j) <= 2 for all p^j <= 400
(incl. p=2, p=l), coefficients nonnegative integers, and rho_Q(m)=rho_{4d}(m)
for l not | m.  Linear: P/q = 4a^2 d' + b_a, checks gcd(4a^2,b_a)=1, b_a<=4a^2.
"""
from math import gcd

def rho(poly, m):
    return sum(1 for x in range(m) if poly(x) % m == 0)

pp = []
for p in range(2, 400):
    if all(p % r for r in range(2, int(p ** 0.5) + 1)):
        x = p
        while x <= 400:
            pp.append((p, x))
            x *= p

qs = [(l, l ** i) for l in (3, 5, 7, 13, 17) for i in (1, 2, 3) if l ** i <= 400]
worst = 0
cnt = 0
for d in range(1, 40):
    for l, q in qs:
        if d % l == 0:
            continue
        roots = [x for x in range(q) if (4 * d * x * x + 1) % q == 0]
        assert len(roots) <= 2
        for x0 in roots:
            c2, c1, c0 = 4 * d * q, 8 * d * x0, (4 * d * x0 * x0 + 1)
            assert c0 % q == 0
            c0 //= q
            Q = lambda y: c2 * y * y + c1 * y + c0
            for y in range(5):
                assert Q(y) * q == 4 * d * (q * y + x0) ** 2 + 1
            for p, m in pp:
                r = rho(Q, m)
                worst = max(worst, r)
                assert r <= 2, (d, q, x0, m, r)
                if p == 2:
                    assert r == 0
                if p != l:
                    assert r == rho(lambda y: 4 * d * y * y + 1, m)
                cnt += 1
for a in range(1, 60):
    for l, q in qs:
        if a % l == 0:
            continue
        d0 = next(x for x in range(1, q) if (4 * a * a * x + 1) % q == 0)
        ba = (4 * a * a * d0 + 1) // q
        assert gcd(4 * a * a, ba) == 1 and ba <= 4 * a * a
print(f"quadratic root-count checks: {cnt}, max rho = {worst}; linear checks OK")
