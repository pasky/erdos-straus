"""Independent exact-arithmetic checks for Z53_PZ §§2,4,8.

Run: ulimit -v 2097152; ulimit -t 120; timeout 90s uv run --no-project python scripts/z53_xrev_pz_exact.py
Fixed small sizes: O(100) storage, streamed pair sums (no Cartesian array).
The supplied engines use floating point; this also checks the CRT model
against actual uniform units of a complete period, without a CRT assumption.
"""
from fractions import Fraction
from math import gcd, lcm, log, pi


def totients(limit):
    values = list(range(limit + 1))
    for p in range(2, limit + 1):
        if values[p] == p:
            for n in range(p, limit + 1, p):
                values[n] -= values[n] // p
    return values


def family(limit):
    return [
        (4 * u * c - 1, (-u) % (4 * u * c - 1))
        for u in range(1, (limit + 1) // 4 + 1)
        for c in range(1, (limit + 1) // (4 * u) + 1)
    ]


def check(limit):
    points, phi = family(limit), totients(limit)
    mean = sum((Fraction(1, m) for m, _ in points), Fraction())
    second = sum(
        (Fraction(phi[gcd(m, n)], m * n)
         for m, a in points for n, b in points
         if (a - b) % gcd(m, n) == 0), Fraction()
    )
    variance = second - mean * mean
    assert variance >= 0
    assert float(mean) >= log((limit + 1) / 4) ** 2 / 8
    if limit == 11:
        period = lcm(*(m for m, _ in points))
        count, total, squares = 0, Fraction(), Fraction()
        for x in range(period):
            if gcd(x, period) != 1:
                continue
            value = sum((Fraction(phi[m], m) for m, a in points
                         if x % m == a), Fraction())
            count += 1
            total += value
            squares += value * value
        assert total / count == mean
        assert squares / count == second
        print(f"Exact complete-period check: period={period}, units={count}, "
              f"M={mean}, V={variance}")
    print(f"Q={limit} P={len(points)} M={float(mean):.9f} "
          f"V={float(variance):.9f} V/M²={float(variance / mean**2):.9f}")


if __name__ == "__main__":
    for cutoff in (11, 100):
        check(cutoff)
    a = 32 / 9 + 8 * (pi * pi / 6) / 9
    print(f"a={a:.12f}; 256a={256*a:.12f}; 1024a={1024*a:.12f}; "
          f"kappa={2 * (1 / 8) * (1 / 4)**2}")
