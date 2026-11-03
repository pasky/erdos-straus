"""Audit whether the minimum-HC modulus evidence survives a larger c window.

Usage: uv run scripts/z55_xrev_hco_window.py /tmp/xrev_HCO
Input is an archived z55-hco tree. Enumerate all P2.2 certificate families
with c <= B and mu <= B, B = floor((log p)^2), for each HIGH record.
No factorization or primality oracle is needed: each reported witness is
validated directly. This does not establish an asymptotic bound.
"""
import math
import re
import sys
from pathlib import Path


def small_certificate(p, bound):
    for c in range(3, bound + 1):
        if c % 4 and (c + p) % 8:
            continue
        # d-fixed U and T; e-fixed T is identical by divisor symmetry.
        for d in range(c - 1, bound + 1, c):
            for line, n in (("U", p + c), ("T", c * p + 1)):
                if n % d == 0:
                    return c, line, d, n // d
        # The remaining possibility is e-fixed U, with c*e <= bound.
        for e in range(1, bound // c + 1):
            if (p + c + e) % (c * e) == 0:
                return c, "U", (p + c) // e, e
    return None


def main(root):
    records = []
    for path in sorted((root / "data/z55/hco").glob("census_*.txt")):
        records.extend((int(p), int(c)) for p, c in re.findall(
            r"HIGH p=(\d+) HC=(\d+)", path.read_text()))
    assert records and len({p for p, _ in records}) == len(records)
    at_minimum = beyond_minimum = missed = 0
    for p, hc in sorted(records):
        bound = math.floor(math.log(p) ** 2)
        witness = small_certificate(p, bound)
        if witness is None:
            missed += 1
            print(f"NO_SMALL p={p} HC={hc} B={bound}")
            continue
        c, line, d, e = witness
        n = p + c if line == "U" else c * p + 1
        mu = min(d, c * e if line == "U" else e)
        assert d * e == n and d % c == c - 1
        assert c % 4 == 0 or (c + p) % 8 == 0
        assert hc <= c <= bound and mu <= bound
        if c == hc:
            at_minimum += 1
        else:
            beyond_minimum += 1
        print(f"SMALL p={p} HC={hc} c={c} line={line} d={d} e={e} mu={mu} B={bound}")
    print(f"records={len(records)} at_HC={at_minimum} larger_c={beyond_minimum} "
          f"no_small_certificate={missed}")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
