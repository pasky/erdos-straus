"""Independent bounded audits for Z53_LATTICE (standard library only).
Run: ulimit -v 6000000; timeout 60s uv run python this_file.py /tmp/xrev_LATTICE/regimes
Checks new local-index proof arithmetic, a direct q=16 certificate, and the
existing enumerator against direct positive (u,B) enumeration (not factoring).
"""
import math
import subprocess
import sys
from itertools import product


def valuation(n, p):
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def subgroups2(q):
    # HNF lattices containing q Z^2: columns (a,0), (b,d).
    divisors = [a for a in range(1, q + 1) if q % a == 0]
    for a in divisors:
        for d in divisors:
            for b in range(a):
                if (b * (q // d)) % a:
                    continue
                points = [((a * i + b * j) % q, d * j)
                          for i in range(q // a) for j in range(q // d)]
                assert len(set(points)) == q * q // (a * d)
                yield a * d, points


def fixed_c():
    checked = 0
    for q, p in [(3, 3), (5, 5), (8, 2), (9, 3)]:
        groups = list(subgroups2(q))
        for c in range(1, 7):
            for u, b in product(range(q), repeat=2):
                n = (4 * c * u * b - u - b) % q
                if q % 2 == 0 and n % 2 == 0:
                    continue
                for index, points in groups:
                    if not all((4 * c * (u + x) * (b + y)
                                - u - x - b - y - n) % q == 0
                               for x, y in points):
                        continue
                    if (4 * c) % p:
                        denominator = math.gcd(q, 4 * c * n + 1)
                    else:
                        denominator = p ** (valuation(4 * c, p)
                                            + 3 * (p == 2))
                    assert index * index * denominator >= q ** 3
                    checked += 1
    print(f"Fixed-C local bound: {checked} exact subgroup/coset cases pass")


def modulus16():
    q, n = 16, 1
    def zero(v):
        u, b, c = v
        return (4 * c * u * b - u - b - n) % q == 0
    variety = {v for v in product(range(q), repeat=3) if zero(v)}
    assert len(variety) == 256
    t, a, b = (0, 15, 0), (1, 14, 0), (0, 15, 1)
    assert {t, a, b} <= variety
    assert tuple((a[i] + b[i] - t[i]) % q for i in range(3)) not in variety
    # A coset of size >128 would have size 256 and equal the entire variety,
    # contradicting failure of affine closure. This coset attains 128.
    certificate = {(u, (-u - 1) % q, c)
                   for u in range(q) for c in range(0, q, 2)}
    assert len(certificate) == 128 and certificate <= variety
    print("q=16: max |H|=128, min index=32; upper and lower bounds verified")


def direct_regimes(n):
    counts = [0] * 7
    for u in range(1, (n + 1) // 3 + 1):
        for b in range(1, (n + u) // (4 * u - 1) + 1):
            c, remainder = divmod(n + u + b, 4 * u * b)
            if remainder or c < 1:
                continue
            cl, cc = (4 * c) ** 3 > 4 * c * n + 1, (4 * c) ** 4 > 4 * c * n + 1
            ul, uc = (4 * u) ** 3 > n + u, (4 * u) ** 4 > n + u
            bl, bc = (4 * b) ** 3 > n + b, (4 * b) ** 4 > n + b
            row = [1, cl, cc, ul, uc, cl or ul or bl, cc or uc or bc]
            counts = [x + y for x, y in zip(counts, row)]
    return counts


def compare_enumerator(executable):
    ns = list(range(3, 502, 2))
    output = subprocess.run([executable, *map(str, ns)], check=True,
                            capture_output=True, text=True, timeout=20).stdout
    rows = output.splitlines()
    assert len(rows) == len(ns)
    for n, line in zip(ns, rows):
        fields = line.split()
        assert int(fields[0]) == n
        assert list(map(int, fields[1:8])) == direct_regimes(n), n
    print(f"Direct positive enumeration: all 7 regime counts agree for {len(ns)} odd n")


if __name__ == "__main__":
    fixed_c()
    modulus16()
    compare_enumerator(sys.argv[1])
