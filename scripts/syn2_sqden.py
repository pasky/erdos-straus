"""O192 §2: ES with a square denominator in one slot (ES^□), elementary existence.

ES^□(n): 4/n = 1/x + 1/y + 1/z, x, y ∈ Z_{>0}, z ∈ Q_{>0} whose denominator is an odd square coprime to n.
(= ES^{(S)} of UNIT_ORBIT_ES §1 with S = all odd primes not dividing n.)
Mechanism: r = least prime ≡ 3 (mod 4) with Jacobi (n/r) = -1 (n ≡ 1 mod 4); Q odd, 0 < Q < 2r, 4Q² ≡ -n (mod r);
UNIT_ORBIT_ES Prop 2.1 with g = r.  For n ≡ 3 (mod 4): Q = 1, g = n + 4.
Checks every solution exactly (Fractions), Type II shape at every prime of n, and the T1 control on odd squares.
Usage: PYTHONPATH=scripts uv run python scripts/syn2_sqden.py N
"""
import sys
from fractions import Fraction
from math import gcd, isqrt


def primes_upto(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(N) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(N + 1) if s[i]]


def jacobi(a, n):
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def sqrt_mod_3mod4(a, r):  # r ≡ 3 (mod 4), a a QR
    return pow(a % r, (r + 1) // 4, r)


def is_square(n):
    return isqrt(n) ** 2 == n


def build(n, Q, g):
    D = Q * Q
    a = n + 4 * D
    assert a % g == 0 and g % 4 == 3
    e = a // g
    assert (n + e) % 4 == 0
    x = (n + e) // 4
    y = n * (g + 1) // 4
    z = Fraction(n * x * (g + 1), 4 * D)
    return x, y, z


def check(n, x, y, z):
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z, (n, x, y, z)
    assert x > 0 and y > 0 and z > 0
    den = z.denominator
    assert den % 2 == 1 and is_square(den) and gcd(den, n) == 1
    # Type II shape at every prime of n: n ∤ ... x coprime to n, n | y, n | numerator of z
    assert gcd(x, n) == 1 and y % n == 0 and z.numerator % n == 0


def solve(n, rprimes):
    if n % 4 == 3:
        a = n + 4
        g = a
        while g % 4 != 3:  # odd part of n+4 is n+4 itself (odd); n+4 ≡ 3 mod 4
            break
        return 1, n + 4, None
    for r in rprimes:
        if n % r == 0:
            continue
        if jacobi(n, r) == -1:
            # -n/4 is a QR mod r (since (-1/r) = -1)
            s = sqrt_mod_3mod4(-n * pow(4, -1, r), r)
            Q = s if s % 2 == 1 else r - s
            if Q == 0 or gcd(Q, n) != 1:
                Q += 2 * r  # still odd, same class
                if gcd(Q, n) != 1:
                    continue
            return Q, r, r
    return None


def main():
    N = int(sys.argv[1])
    P = primes_upto(N)
    rprimes = [r for r in P if r % 4 == 3]
    maxr, hist = 0, {}
    worst = None
    cnt = 0
    for p in P:
        if p < 5:
            continue
        res = solve(p, rprimes)
        assert res is not None, p
        Q, g, r = res
        x, y, z = build(p, Q, g)
        check(p, x, y, z)
        cnt += 1
        if r is not None:
            hist[r] = hist.get(r, 0) + 1
            if r > maxr:
                maxr, worst = r, p
    print(f"primes 5<=p<={N}: {cnt} solved, all checked exactly")
    print(f"p≡1(4): max r(p) = {maxr} at p = {worst}; r histogram (top): {sorted(hist.items())[:12]}")
    # T1 control: odd squares n = m^2: no prime r≡3(4) with (n/r)=-1 trivially; check stronger: no shot n+4Q^2,
    # Q odd ≤ 99 coprime to n, has a prime factor ≡ 3 mod 4.
    bad = 0
    for m in range(3, isqrt(N) + 1, 2):
        n = m * m
        for Q in range(1, 100, 2):
            if gcd(Q, n) != 1:
                continue
            a = n + 4 * Q * Q
            # factor a by trial division with primes
            t = a
            for q in P:
                if q * q > t:
                    break
                while t % q == 0:
                    if q % 4 == 3:
                        bad += 1
                    t //= q
            if t > 1 and t % 4 == 3:
                bad += 1
    print(f"T1 control: odd squares m^2 <= {N}, Q odd <= 99: prime factors ≡ 3 (4) of m^2+4Q^2 found: {bad}")


if __name__ == "__main__":
    main()
