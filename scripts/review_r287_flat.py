"""R287 from-scratch check of POWER_LADDER_ES §2 (flat ladder) and §7 (fixed shot r = 3, 11).

Independent of scripts/z44_*.py. For each n and k builds an ES_(k) solution and verifies EXACTLY:
  4/n = 1/x + 1/y + 1/z, x, y in Z_{>0}, z = Z/Q^k in lowest terms, Q odd, gcd(Q, n) = 1,
and records the shape at each prime l | n (Type I: exactly one of x,y,z has v_l >= v_l(n), others l-units;
Type II: one l-unit, two with v_l >= v_l(n)).
Usage: PYTHONPATH=scripts uv run python scripts/review_r287_flat.py N
"""
import sys
from fractions import Fraction
from math import gcd


def sieve(N):
    s = bytearray([1]) * (N + 1)
    s[0] = s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return s


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def v(l, a):
    """valuation of a positive Fraction or int."""
    a = Fraction(a)
    c, num, den = 0, a.numerator, a.denominator
    while num % l == 0:
        num //= l; c += 1
    while den % l == 0:
        den //= l; c -= 1
    return c


def check(n, k, x, y, z):
    """Return shape string; raise on failure."""
    z = Fraction(z)
    assert isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0 and z > 0
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / z, (n, k, x, y, z)
    D = z.denominator
    # D must be Q^k with Q odd, gcd(Q, n) = 1
    Q = round(D ** (1.0 / k)) if D > 1 else 1
    for cand in (Q - 1, Q, Q + 1):
        if cand >= 1 and cand ** k == D:
            Q = cand; break
    else:
        raise AssertionError(("den not k-th power", n, k, D))
    assert Q % 2 == 1 and gcd(Q, n) == 1, (n, k, Q)
    shapes = set()
    for l, e in factor(n).items():
        vals = [v(l, x), v(l, y), v(l, z)]
        big = sum(1 for t in vals if t >= e)
        unit = sum(1 for t in vals if t == 0)
        if big == 1 and unit == 2:
            shapes.add("I")
        elif big == 2 and unit == 1:
            shapes.add("II")
        else:
            shapes.add("other")
    return Q, "".join(sorted(shapes))


def odd_k_identity(n, k):
    """Thm 2.1: 4x = n + Q^k, Q = least Q = -n mod 4, gcd(Q, n) = 1."""
    Q = (-n) % 4
    while gcd(Q, n) != 1:
        Q += 4
    x = (n + Q ** k) // 4
    assert 4 * x == n + Q ** k
    return Q, (2 * x, 2 * x, Fraction(n * x, Q ** k))


def is_kth_power_mod(t, k, r):
    return pow(t % r, (r - 1) // gcd(k, r - 1), r) == 1


def shot(n, k, r):
    """UNIT_ORBIT_ES Prop 2.1 with Q^2 -> Q^k at a prime r = 3 (4); my own root search."""
    target = (-n * pow(4, -1, r)) % r
    roots = [t for t in range(1, r) if pow(t, k, r) == target]
    if not roots:
        return None
    Q0 = roots[0]
    Q = Q0
    while Q % 2 == 0 or gcd(Q, n * (r + 1)) != 1:
        Q += r
    a = n + 4 * Q ** k
    assert a % r == 0
    e = a // r
    assert (n + e) % 4 == 0
    x = (n + e) // 4
    y = n * (r + 1) // 4
    z = Fraction(n * x * (r + 1), 4 * Q ** k)
    return Q, (x, y, z)


def main():
    N = int(sys.argv[1])
    sv = sieve(N)
    primes = [p for p in range(3, N + 1) if sv[p]]
    r3mod4 = [r for r in range(3, 5000) if sv[r] and r % 4 == 3]
    sq = [m * m for m in range(3, int(N ** 0.5) + 1, 2)]
    cu = [m ** 3 for m in range(3, int(round(N ** (1 / 3))) + 2, 2) if m ** 3 <= N]
    # odd k: Thm 2.1
    for k in (1, 3, 5, 7):
        maxQ, shp = 0, {}
        for n in primes + sq + cu:
            Q, sol = odd_k_identity(n, k)
            Qc, s = check(n, k, *sol)
            assert Qc == Q
            maxQ = max(maxQ, Q) if n in (2,) or sv[n] else maxQ
            shp[s] = shp.get(s, 0) + 1
        print(f"odd k={k}: {len(primes)} primes, {len(sq)} odd squares, {len(cu)} odd cubes OK;"
              f" max Q over primes {maxQ}; shapes {shp}")
    # even k: Thm 2.3 at primes p = 1 (4) (search any r = 3 (4) where the shot fires), record whether
    # the first firing r satisfies the theorem's conditions; also least r satisfying the theorem's conditions.
    for k in (2, 4, 6, 8, 12):
        kodd = k
        while kodd % 2 == 0:
            kodd //= 2
        oddl = [l for l in factor(kodd)] if kodd > 1 else []
        maxr, maxr_thm, viol = 0, 0, 0
        for p in primes:
            if p % 4 == 3:
                continue
            fired = None
            for r in r3mod4:
                if r == p:
                    continue
                res = shot(p, k, r)
                if res:
                    fired = (r, res)
                    break
            assert fired, (p, k)
            r, (Q, sol) = fired
            Qc, s = check(p, k, *sol)
            assert s == "II", (p, k, s)
            maxr = max(maxr, r)
            # theorem's r: (p/r) = -1 and r != 1 mod l for l | kodd
            rt = next(r for r in r3mod4 if r != p and pow(p, (r - 1) // 2, r) == r - 1
                      and all(r % l != 1 for l in oddl))
            res = shot(p, k, rt)
            assert res, ("theorem r does not fire", p, k, rt)
            check(p, k, *res[1])
            maxr_thm = max(maxr_thm, rt)
        print(f"even k={k}: all primes p=1(4) <= {N} solved Type II; max first-firing r {maxr}; "
              f"max theorem-r {maxr_thm}")
    # Lemma 2.4 control: no modulus-4 shot at odd squares for even k (any r = 3 (4) up to 5000)
    for k in (2, 4, 6):
        bad = 0
        for n in sq[:200]:
            for r in r3mod4[:200]:
                if n % r and shot(n, k, r):
                    bad += 1
        print(f"even k={k}: shots firing at first 200 odd squares, 200 r's: {bad}")
    # §7 fixed shots: (k, r) = (3, 3), (3, 11), (5, 3), (5, 23)
    for k, r in ((3, 3), (3, 11), (5, 3), (5, 23), (7, 3), (9, 11)):
        cnt, maxQ, shp = 0, 0, {}
        for n in primes + sq + cu:
            if n % r == 0 or (n % 3 == 0 and r == 11 and False):
                continue
            res = shot(n, k, r)
            assert res, (n, k, r)
            Q, sol = res
            Qc, s = check(n, k, *sol)
            cnt += 1; maxQ = max(maxQ, Q)
            shp[s] = shp.get(s, 0) + 1
        print(f"fixed shot k={k} r={r}: {cnt} n solved, max Q {maxQ}, shapes {shp}")


if __name__ == "__main__":
    main()
