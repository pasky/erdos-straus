"""R287 from-scratch checks: POWER_LADDER_ES §5 (one mute prime), Prop 3.1 (index formula), §2.3 numerator-8 examples.

usage: PYTHONPATH=scripts uv run python scripts/review_r287_mute.py QMAX NMAX
 1. For every prime q <= QMAX: hypothesis of Thm 5.1 holds (q = 3 (4), or q = 2 (3), or a prime g = 3 (4) with q a
    primitive root mod g); report max least witness g over q = 1 (12).
 2. q = 13, g = 11: for every prime p <= NMAX (p != 11, 13) and odd square <= NMAX prime to 143, build the witness
    solution (UNIT_ORBIT Prop 2.1 with Q^2 -> 13^c, 4*13^c = -n mod 11) or ES / scaling, verify exactly that den z is a
    power of 13; max c.
 3. Prop 3.1(a): brute-force [G : G^k] for G = (Z/4U)^x, U odd squarefree <= 200, k <= 12, vs gcd(k,2) prod gcd(k,l-1).
 4. Explicit identities quoted in §2.3, §5.
"""
import sys
from fractions import Fraction as F
from math import gcd, isqrt


def primes(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(N) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return s


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def is_primroot(q, g):
    if q % g == 0:
        return False
    return all(pow(q, (g - 1) // l, g) != 1 for l in factor(g - 1))


def den_is_power_of(z, q):
    d = F(z).denominator
    while d % q == 0:
        d //= q
    return d == 1


def solve13(n, q=13, g=11):
    """ES^<q>,*(n) for n prime to q via witness g (n prime to g), returns (x, y, z, c)."""
    t = (-n * pow(4, -1, g)) % g
    c = next(c for c in range(g - 1) if pow(q, c, g) == t)
    Q = q ** c
    a = n + 4 * Q
    e = a // g
    assert a % g == 0 and (n + e) % 4 == 0
    x = (n + e) // 4
    y = n * (g + 1) // 4
    z = F(n * x * (g + 1), 4 * Q)
    return x, y, z, c


def main():
    QMAX, NMAX = int(sys.argv[1]), int(sys.argv[2])
    S = primes(max(QMAX, NMAX, 10000))
    gs = [g for g in range(3, 10000) if S[g] and g % 4 == 3]
    worst, cnt = (0, 0), 0
    for q in range(3, QMAX + 1):
        if not S[q] or q % 4 == 3 or q % 3 == 2:
            continue
        assert q % 12 == 1
        cnt += 1
        g = next(g for g in gs if is_primroot(q, g))
        worst = max(worst, (g, q))
    print(f"1. {cnt} primes q = 1 (12) <= {QMAX}: all have a witness; max least witness g = {worst[0]} at q = {worst[1]}")
    # 2.
    maxc, nsol = 0, 0
    ns = [p for p in range(3, NMAX + 1) if S[p] and p not in (11, 13)]
    ns += [m * m for m in range(3, isqrt(NMAX) + 1, 2) if gcd(m, 143) == 1]
    for n in ns:
        if n % 11 == 0:
            raise AssertionError
        x, y, z, c = solve13(n)
        assert F(4, n) == F(1, x) + F(1, y) + 1 / z and x > 0 and y > 0 and z > 0
        assert den_is_power_of(z, 13)
        maxc = max(maxc, c); nsol += 1
    print(f"2. q=13, g=11: {nsol} n solved exactly (den z a power of 13), max c = {maxc}")
    # 3.
    bad = 0
    for U in range(1, 200, 2):
        f = factor(U)
        if any(e > 1 for e in f.values()):
            continue
        M = 4 * U
        G = [a for a in range(1, M) if gcd(a, M) == 1]
        for k in range(1, 13):
            Gk = {pow(a, k, M) for a in G}
            pred = gcd(k, 2)
            for l in f:
                pred *= gcd(k, l - 1)
            if len(G) // len(Gk) != pred:
                bad += 1
    print(f"3. Prop 3.1(a) index formula: {bad} mismatches over odd squarefree U < 200, k <= 12")
    # 4. explicit identities
    ex = [(8, 131, [64, 64], F(4192, 125)), (8, 241, [146, 146], F(17593, 343)),
          (8, 131, [20, 131], F(2620, 9)), (8, 131, [956, 131], F(125236, 9 ** 4)),
          (8, 241, [46, 241], F(11086, 81)), (4, 5, [58, 5], F(290, 169))]
    for num, n, (x, y), z in ex:
        ok = F(num, n) == F(1, x) + F(1, y) + 1 / z
        print(f"4. {num}/{n} = 1/{x} + 1/{y} + {z.denominator}/{z.numerator}: {ok}; den z = {z.denominator}")


if __name__ == "__main__":
    main()
