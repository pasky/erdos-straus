"""R206: exponent arithmetic of TORSION_FIRING Thm 3.1 and Cor 3.2 at the level of actual groups.

(1) gcd(h^s + 1, h^t - 1) == 2 for odd h (all odd h, not only primes), s <= 8, odd t <= 9; and the counterexample
    side: for even t, the gcd can be large (shows 't odd' is necessary).
(2) Cor 3.2 in F_{h^2}: for prime h = 3 mod 4, mu_{h+1} meets F_h^* in {+-1}; any coset sigma*mu_{h+1}
    (sigma in F_{h^2}^*) meets F_h^* in 0 or 2 elements -> amplification per seed element is <= 2 even for seeds
    outside F_h^*.
(3) Ordinary contrast: for y^2 = x^3 + x + 1 (non-CM) at primes h = 3 mod 4 below 400, gcd(#E(F_h), h - 1),
    i.e. the largest image of a homomorphism E(F_h) -> F_h^* when E(F_h) is cyclic, is often large.
"""
from math import gcd
from sympy import primerange

bad = 0
for h in range(3, 400, 2):
    for s in range(1, 9):
        for t in range(1, 10, 2):
            if gcd(h ** s + 1, h ** t - 1) != 2:
                bad += 1
print("(1) odd h<400, s<=8, odd t<=9: gcd != 2 count:", bad)
print("    even t example h=7,s=1,t=2:", gcd(7 + 1, 7 ** 2 - 1), "; h=7,s=1,t=4:", gcd(8, 7 ** 4 - 1))

# (2) F_{h^2} = F_h[i] (h = 3 mod 4), elements as pairs (a, b) = a + b i
bad2 = 0
for h in primerange(3, 200):
    if h % 4 != 3:
        continue
    def mul(u, v):
        return ((u[0] * v[0] - u[1] * v[1]) % h, (u[0] * v[1] + u[1] * v[0]) % h)
    def pw(u, n):
        r = (1, 0)
        while n:
            if n & 1:
                r = mul(r, u)
            u = mul(u, u)
            n >>= 1
        return r
    allel = [(a, b) for a in range(h) for b in range(h) if (a, b) != (0, 0)]
    mu = [u for u in allel if pw(u, h + 1) == (1, 0)]
    assert len(mu) == h + 1
    if sorted(u for u in mu if u[1] == 0) != [(1, 0), (h - 1, 0)]:
        bad2 += 1
    for sig in allel[:: max(1, len(allel) // 50)]:
        cnt = sum(1 for u in mu if mul(sig, u)[1] == 0)
        if cnt not in (0, 2):
            bad2 += 1
print("(2) primes h=3 mod 4 < 200: violations", bad2)

# (3) ordinary contrast
def count(a, b, h):
    sq = [0] * h
    for y in range(h):
        sq[y * y % h] += 1
    return 1 + sum(sq[(x ** 3 + a * x + b) % h] for x in range(h))
big = []
for h in primerange(5, 400):
    if h % 4 == 3:
        N = count(1, 1, h)
        g = gcd(N, h - 1)
        if N != h + 1 and g > 10:
            big.append((h, N, g))
print("(3) y^2=x^3+x+1, h=3 mod 4 < 400 with gcd(#E, h-1) > 10:", len(big), big[:6])
