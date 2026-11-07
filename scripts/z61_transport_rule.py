#!/usr/bin/env python3
"""Frozen z61 CRT/reservoir transport; exact, bounded-memory diagnostics.

STUCK is a failed proposed rule, not a U7 counterexample. A sampled table is
never reported as a complete valuation transport. ES remains OPEN.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import lru_cache
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Z7 = (105, 1465, 3865, 4545, 10305, 12145, 39361, 67425)


@lru_cache(maxsize=8192)
def factors(n: int) -> tuple[tuple[int, int], ...]:
    assert n >= 1
    result = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            result.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.append((n, 1))
    return tuple(result)


@lru_cache(maxsize=1024)
def divisors(n: int) -> tuple[int, ...]:
    ds = [1]
    for p, e in factors(n):
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return tuple(sorted(ds))


def column(n: int, f: int) -> dict | None:
    if f < 7 or f > 2 * n + 1 or f % 8 != 7:
        return None
    r = (-n) % f
    if not r:
        return None
    k = (n + f - 1) // f
    g = gcd(r, f + 1)
    assert r == k * f - n and g == gcd(n + k, f + 1)
    return dict(f=f, r=r, k=k, g=g, a=r // g)


def proper_factor(n: int, *values: int) -> int | None:
    for value in values:
        d = gcd(n, value)
        if 1 < d < n:
            assert n % d == 0
            return d
    return None


def route(n: int, src: dict, ell: int, e: int, used: set,
          probe_limit: int = 100000) -> dict:
    """One actual token route. No lookup of hits outside prescribed destinations."""
    f, k, g, a = (src[x] for x in ("f", "k", "g", "a"))
    q = ell**e
    assert a % q == 0
    d = proper_factor(n, f, k, ell)
    if d:
        return dict(status="factor", factor=d, via="source")
    h, c = (f + 1) // g, (n + k) // g
    M = 8 // gcd(g, 8)
    assert a == k * h - c and gcd(h, c) == 1 and h % M == 0
    # This also covers ell=2: ell|a forces ell coprime to M.
    assert gcd(ell, k * M * c) == 1
    R = 1
    for p, _ in factors(c):
        R *= p
    u = pow(k * M * R, -1, q)
    probes = 0
    rejected = []

    def accept(dst: dict, via: str) -> dict | None:
        nonlocal probes
        probes += 1
        d = proper_factor(n, dst["f"], dst["k"])
        if d:
            return dict(status="factor", factor=d, destination=dst, via=via)
        if dst["a"] == 1:
            return dict(status="hit", destination=dst, via=via)
        assert (dst["a"] - 1) % q == 0
        slot = (dst["f"], ell, e)
        if slot not in used:
            used.add(slot)
            return dict(status="matched", destination=dst, via=via)
        return None

    for v in sorted((u, u - q), key=lambda x: (abs(x), x < 0)):
        fp = g * (h + M * R * v) - 1
        dst = column(n, fp)
        if dst is None or dst["k"] != k or dst["g"] != g:
            rejected.append(fp)
            continue
        assert gcd(c, (fp + 1) // g) == 1
        ans = accept(dst, "interior")
        if ans:
            return ans

    # Solve the mod-8 congruence first; no huge arrays or Cartesian products.
    for gp in divisors(n + 1):
        C = (n + 1) // gp
        max_t = (C - 1) // q
        period = 8 // gcd(gp * q, 8)
        starts = [t for t in range(period) if (n + gp * (1 + q * t)) % 8 == 7]
        assert len(starts) <= 1
        if not starts:
            continue
        # Every A in this progression shares this gcd. Skip an impossible
        # progression exactly, rather than spending the resource cap on it.
        if gcd(gcd(1 + q * starts[0], q * period), C) > 1:
            continue
        for t in range(starts[0], max_t + 1, period):
            probes += 1
            if probes > probe_limit:
                return dict(status="budget", probes=probes)
            A = 1 + q * t
            if gcd(A, C) != 1:
                continue
            dst = column(n, n + gp * A)
            assert dst and dst["k"] == 1 and dst["g"] == gp and dst["a"] == A
            ans = accept(dst, "reservoir")
            if ans:
                return ans
    return dict(status="stuck", q=q, c=c, M=M, R=R, u=u,
                interior_rejected=rejected, probes=probes)


def source_columns(n: int, complete_limit: int):
    if n <= complete_limit or n in Z7:
        return range(7, 2 * n + 2, 8), "complete"
    fs = set(range(7, min(512, 2 * n + 2), 8))
    for boundary in (n // 3, n // 2, n, 2 * n + 1):
        last = boundary - (boundary - 7) % 8
        fs.update(last + delta for delta in (-16, -8, 0, 8, 16))
    return sorted(f for f in fs if 7 <= f <= 2 * n + 1), "sampled"


def transport(n: int, complete_limit: int) -> dict:
    s = isqrt(n)
    if s * s == n:
        assert 1 < s < n and n % s == 0
        return dict(scope="square-preflight", status="factor", factor=s)
    fs, scope = source_columns(n, complete_limit)
    used = set()
    counts = Counter()
    ledgers = defaultdict(Counter)
    examples = defaultdict(list)
    source_hits = []
    columns = 0
    for f in fs:
        src = column(n, f)
        if src is None:
            continue
        columns += 1
        if src["a"] == 1:
            source_hits.append(f)  # diagnostic only; never an arbitrary sink
        for ell, exponent in factors(src["a"]):
            for e in range(1, exponent + 1):
                ans = route(n, src, ell, e, used)
                status = ans["status"]
                counts[status] += 1
                ledgers[ell]["initial"] += 1
                ledgers[ell][status] += 1
                if len(examples[status]) < 3:
                    examples[status].append(dict(source=src, ell=ell, e=e, **ans))
    for row in ledgers.values():
        assert row["initial"] == sum(v for key, v in row.items() if key != "initial")
    assert len(used) == counts["matched"]
    return dict(scope=scope, columns=columns, tokens=sum(counts.values()),
                counts=dict(counts), source_hits=source_hits,
                ledger={str(p): dict(v) for p, v in sorted(ledgers.items())},
                examples=dict(examples),
                status="failed" if counts["stuck"] else
                "incomplete" if counts["budget"] else "routed-tested-tokens")


def witness(n: int, restricted8: bool = False, cap: int = 200000) -> dict:
    bound = min(2 * n + 1, cap)
    for f in range(7, bound + 1, 8):
        r = (-n) % f
        if not r or (f + 1) % r:
            continue
        if restricted8 and ((f + 1) // 8) % r and r % 8:
            continue
        return dict(status="hit", f=f, r=r, g=gcd(r, f + 1),
                    word=[r, (f + 1) // r, (n + r) // f])
    return dict(status="zero" if cap >= 2 * n + 1 else "no-hit-in-prefix", bound=bound)


def square_ledger(n: int) -> dict:
    den, num, exit_primes = Counter(), Counter(), set()
    exits = []
    for f in range(7, 2 * n + 2, 8):
        col = column(n, f)
        if col is None:
            continue
        assert col["a"] > 1
        den.update(dict(factors(col["a"])))
        num.update(dict(factors(col["a"] - 1)))
        d = proper_factor(n, f, col["k"])
        if d:
            exits.append(dict(**col, factor=d))
            exit_primes.update(p for p, _ in factors(col["a"]))
    surplus = {p: den[p] - num[p] for p in den if den[p] > num[p]}
    s = isqrt(n)
    assert s * s == n and 1 < s < n
    return dict(n=n, denominator=dict(sorted(den.items())), numerator=dict(sorted(num.items())),
                square_preflight_factor=s, factor_bound_flux=dict(sorted(den.items())),
                surplus=dict(sorted(surplus.items())), nonunit_columns=exits,
                exit_primes=sorted(exit_primes), overlap=sorted(exit_primes & surplus.keys()))


def read_screen(name: str) -> list[int]:
    return [int(line.split()[0]) for line in (ROOT / "data/z58/screens" / name).read_text().splitlines()
            if line.strip() and not line.startswith("#")]


def run(out: Path, complete_limit: int):
    out.mkdir(parents=True, exist_ok=True)
    cases = defaultdict(set)
    for n in range(3, 1001, 2):
        if factors(n) == ((n, 1),):
            cases[n].add("small-prime")
    for n in (169, 289, 361, 529):
        cases[n].add("odd-square")
    for n in Z7:
        cases[n].add("U7-composite-zero")
    for name, tag in (("star_prime_zeros.txt", "star-prime-zero"),
                      ("gstar_zeros.txt", "gstar-prime-zero"),
                      ("r8_zeros_1e10.txt", "R8-prime-zero"),
                      ("composite_zeros_le8e6.txt", "star-composite-zero")):
        for n in read_screen(name):
            cases[n].add(tag)
    # Genuine two-branch numerator-8 zero, distinct from the C-even screen.
    cases[131].add("U8-prime-zero-control")
    totals = Counter()
    groups = defaultdict(Counter)
    with (out / "fixtures.jsonl").open("w") as dest:
        for n, tags in sorted(cases.items()):
            u7 = witness(n, cap=2 * n + 1 if n <= 8000000 else 200000)
            result = transport(n, complete_limit)
            if "U7-composite-zero" in tags or "odd-square" in tags:
                assert u7["status"] == "zero"
            elif any("prime" in t for t in tags):
                assert u7["status"] == "hit"
            row = dict(n=n, tags=sorted(tags), factorization=factors(n), u7=u7, transport=result)
            if n <= 1000:
                row["u8"] = witness(n, restricted8=True)
            if n == 131:
                assert row["u8"]["status"] == "zero"
            dest.write(json.dumps(row, sort_keys=True) + "\n")
            totals[result["status"]] += 1
            for tag in tags:
                groups[tag]["inputs"] += 1
                groups[tag][result["status"]] += 1
                groups[tag]["U7-" + u7["status"]] += 1
                groups[tag].update(result.get("counts", {}))
    squares = [square_ledger(n) for n in (169, 289, 361, 529)]
    (out / "squares.json").write_text(json.dumps(squares, indent=2, sort_keys=True) + "\n")
    # Capacity-free adversarial seed: no prior token can be blamed for this failure.
    src = column(193, 183)
    kill = dict(n=193, source=src, ell=173, e=1, route=route(193, src, 173, 1, set()),
                independent_u7=witness(193),
                finite_173_slots=[f for f in range(7, 388, 8)
                                 if (col := column(193, f)) and col["a"] > 1
                                 and (col["a"] - 1) % 173 == 0],
                block_k3=[column(193, f) for f in (71, 79, 87, 95)])
    assert kill["route"]["status"] == "stuck"
    composite_src = column(105, 103)
    kill["no_hit_composite"] = dict(n=105, source=composite_src, ell=101, e=1,
                                   route=route(105, composite_src, 101, 1, set()),
                                   independent_u7=witness(105))
    assert kill["no_hit_composite"]["route"]["status"] == "stuck"
    (out / "kill.json").write_text(json.dumps(kill, indent=2, sort_keys=True) + "\n")
    summary = dict(inputs=len(cases), complete_limit=complete_limit,
                   totals=dict(totals), groups={k: dict(v) for k, v in sorted(groups.items())})
    (out / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "data/z61/transport")
    parser.add_argument("--complete-limit", type=int, default=2000)
    args = parser.parse_args()
    run(args.out, args.complete_limit)
