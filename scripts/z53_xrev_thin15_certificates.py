"""Independent streaming check of THIN15 certificates; no lane-script imports.

Run with uv run --with gmpy2 python SCRIPT /tmp/xrev_THIN15/data/z53/thin15.
Check divisibility via modular exponentiation (never construct n for all rows).
Check the literal identity at file boundaries and at every t <= 10000.
"""
import sys
from collections import Counter
from pathlib import Path

from gmpy2 import mpz

root = Path(sys.argv[1])
files = ("cert_t1_10000.txt", "cert_t10001_30000.txt", "cert_t30001_50000.txt")
expected = 1
counts = Counter()
small = Counter()
literal = 0
for name in files:
    with (root / name).open() as stream:
        for line in stream:
            if not line.strip() or line.startswith("#"):
                continue
            t, m, d1, d2 = map(int, line.split())
            assert t == expected, (name, t, expected)
            assert min(m, d1, d2) > 0 and m % 4 == 3, t
            assert (d1 + d2) % m == 0, t
            for divisor in (d1, d2):
                assert (15 * pow(2, 60 * t, 4 * divisor) + 1 + m) % (4 * divisor) == 0, t
            if t <= 10000 or t in (10001, 30000, 30001, 50000):
                n = 15 * (mpz(1) << (60 * t)) + 1
                x = (n + m) // 4
                k = (d1 + d2) // m
                y, z = n * x * k // d1, n * x * k // d2
                assert 4 * x * y * z == n * (x * y + y * z + z * x), t
                literal += 1
            counts[m] += 1
            if t <= 10000:
                small[m] += 1
            expected += 1
    print(name, "checked through", expected - 1, flush=True)
assert expected == 50001
print("PASS: 50000 ordered, positive certificates; no gaps or duplicates")
print("literal identities:", literal)
print("max m:", max(counts), "m=3:", counts[3], "m=7:", counts[7])
print("t<=10000: max m:", max(small), "m=3:", small[3], "m=7:", small[7])
