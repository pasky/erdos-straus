#!/usr/bin/env python3
"""Independent exact audit of archived transport certificates (no engine import)."""
import json
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/z61/transport"


def fac(x):
    result = Counter()
    for p in range(2, isqrt(x) + 1):
        while x % p == 0:
            result[p] += 1
            x //= p
        if x == 1:
            break
    if x > 1:
        result[x] += 1
    return result


def col(n, f):
    assert 7 <= f <= 2 * n + 1 and f % 8 == 7
    r = f - n % f
    if r == f:
        return None
    g = gcd(r, f + 1)
    return {"f": f, "r": r, "k": (n + r) // f, "g": g, "a": r // g}


def check_hit(n, hit):
    f, r = hit["f"], hit["r"]
    c = col(n, f)
    assert c and c["r"] == r and c["a"] == 1
    x, y, z = hit["word"]
    assert x * y * z - x - z == n and (x * y) % 8 == 0


def main():
    totals = Counter()
    failures_small = []
    by_n = {}
    for line in (DATA / "fixtures.jsonl").open():
        row = json.loads(line)
        n, result = row["n"], row["transport"]
        by_n[n] = row
        totals["inputs"] += 1
        if row["u7"]["status"] == "hit":
            check_hit(n, row["u7"])
            totals["fresh_U7_certificates"] += 1
        else:
            assert row["u7"]["status"] == "zero"
            assert all((c := col(n, f)) is None or c["a"] != 1
                       for f in range(7, 2 * n + 2, 8))
            totals["complete_U7_zeros"] += 1
        if result["scope"] == "square-preflight":
            d = result["factor"]
            assert 1 < d < n and n == d * d
            continue
        for ell, ledger in result["ledger"].items():
            assert ledger["initial"] == sum(v for k, v in ledger.items() if k != "initial")
            assert ledger.get("budget", 0) == 0
        if result["scope"] == "complete":
            den, num = Counter(), Counter()
            for f in range(7, 2 * n + 2, 8):
                c = col(n, f)
                if c:
                    den.update(fac(c["a"]))
                    if c["a"] > 1:
                        num.update(fac(c["a"] - 1))
            assert den == Counter({int(p): v["initial"] for p, v in result["ledger"].items()})
            for p, v in result["ledger"].items():
                assert v.get("matched", 0) <= num[int(p)]
            totals["complete_token_tables"] += 1
        for status, examples in result["examples"].items():
            for example in examples:
                source = example["source"]
                assert source == col(n, source["f"])
                q = example["ell"] ** example["e"]
                assert source["a"] % q == 0
                if "destination" in example:
                    dst = example["destination"]
                    assert dst == col(n, dst["f"])
                if status == "factor":
                    d = example["factor"]
                    assert 1 < d < n and n % d == 0
                elif status == "hit":
                    assert dst["a"] == 1
                elif status == "matched":
                    assert dst["a"] > 1 and (dst["a"] - 1) % q == 0
                else:
                    assert status == "stuck"
                totals["example_certificates"] += 1
        if "small-prime" in row["tags"] and result["status"] == "failed":
            failures_small.append(n)

    for row in json.loads((DATA / "squares.json").read_text()):
        n = row["n"]
        value, den = Fraction(1), Counter()
        for f in range(7, 2 * n + 2, 8):
            c = col(n, f)
            if c:
                a = c["a"]
                value *= Fraction(a - 1, a)
                den.update(fac(a))
        assert 0 < value < 1
        assert fac(value.denominator) == Counter({int(p): e for p, e in row["surplus"].items()})
        assert den == Counter({int(p): e for p, e in row["factor_bound_flux"].items()})
        assert row["square_preflight_factor"] ** 2 == n
        totals["exact_square_products"] += 1

    # An empty-capacity seed: failure cannot be blamed on matching order.
    kill = json.loads((DATA / "kill.json").read_text())
    n, q, f = 193, 173, 183
    assert all(n % d for d in range(2, isqrt(n) + 1))
    assert all(q % d for d in range(2, isqrt(q) + 1))
    c = col(n, f)
    assert c == kill["source"] and c["a"] == q
    allcols = [c for fp in range(7, 388, 8) if (c := col(n, fp))]
    assert not [c for c in allcols if c["a"] > 1 and (c["a"] - 1) % q == 0]
    # This excludes ALL same-(k,g) destinations and ALL k=1 destinations,
    # not just the production code's selected signed representatives.
    permitted = [c for c in allcols if c["k"] == 1 or (c["k"], c["g"]) == (2, 1)]
    assert all(c["a"] != 1 for c in permitted)
    assert [c["f"] for c in allcols if c["a"] == 1] == [15, 39, 103]
    totals["capacity_free_kill_certificates"] += 1

    # No-hit composite: guarded failure where Q really is positive.
    # It is NOT a failure if raw out-of-range proposals get factor-tested.
    n, q, f = 105, 101, 103
    assert col(n, f)["a"] == q
    allcols = [c for fp in range(7, 212, 8) if (c := col(n, fp))]
    assert all(c["a"] > 1 for c in allcols)
    assert not [c for c in allcols if (c["a"] - 1) % q == 0]
    assert gcd(n, f) == gcd(n, 2) == gcd(n, q) == 1
    assert not [c for c in allcols if c["k"] == 1 and (c["a"] - 1) % q == 0]
    u = pow(2 * 8 * 107, -1, q)
    raw_proposal = f + 8 * 107 * u
    assert raw_proposal > 2 * n + 1 and gcd(n, raw_proposal) == 3
    totals["guarded_composite_obstructions_with_raw_factor_exit"] += 1

    # Independent check of the normalization trap (not the frozen rule).
    assert col(53, 31) == dict(f=31, r=9, k=2, g=1, a=9)
    assert col(53, 39) == dict(f=39, r=25, k=2, g=5, a=5)
    print(json.dumps(dict(checks=dict(totals), failed_primes_le1000=failures_small,
                          status="PASS: certificates checked; proposed transport remains DEAD"),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
