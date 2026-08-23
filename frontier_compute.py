#!/usr/bin/env python3
"""Large finite experiment for notes.md section 19.

Run with, e.g.:
    uv run --with sympy python frontier_compute.py --bound 100000000 --workers 12

The scan is restricted to the hard primes p == 1 (mod 24).  Every reported
criterion hit is computed from the prime factorization of n and the exact
residue set of divisors of n**2.
"""
from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import random
import time
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
from pathlib import Path

from sympy import Symbol, expand, factorint, jacobi_symbol, sieve

MODULI = tuple(range(3, 1000, 4))
DIVISOR_CAP = 1_000_000


def factor_tau_square(n: int):
    fac = factorint(n)
    tau2 = math.prod(2 * e + 1 for e in fac.values())
    return fac, tau2


def reachable_residues(fac: dict[int, int], w: int) -> set[int]:
    """Residues of all divisors of n^2, from n's factorization."""
    residues = {1}
    for prime, exponent in fac.items():
        powers = set()
        power = 1
        for _ in range(2 * exponent + 1):
            powers.add(power)
            power = power * prime % w
        residues = {a * b % w for a in residues for b in powers}
    return residues


def divisor_hit(n: int, w: int) -> tuple[bool, dict[int, int]]:
    """Test the literal divisor criterion; return the factorization for reuse.

    Below the cap this recursively visits residues of the individual divisors
    of n^2 (with early exit).  Above it, the bounded subset-product residue DP
    avoids enumerating more than w residues.
    """
    fac, tau2 = factor_tau_square(n)
    target = (-n) % w
    if tau2 > DIVISOR_CAP:
        return target in reachable_residues(fac, w), fac
    items = tuple(fac.items())

    def visit(i: int, residue: int) -> bool:
        if i == len(items):
            return residue == target
        prime, exponent = items[i]
        power = 1
        for _ in range(2 * exponent + 1):
            if visit(i + 1, residue * power % w):
                return True
            power = power * prime % w
        return False

    return visit(0, 1), fac


def minimal_row(p: int) -> tuple[int, int, int]:
    """Return (p, interleaved minimum, Case-B-only minimum)."""
    interleaved = None
    case_b = None
    # The observed maxima are tiny; 999 is a deliberate fail-loud guard, not
    # a mathematical search cap asserted in the report.
    for w in MODULI:
        b_hit = False
        if case_b is None:
            x = (p + w) // 4
            b_hit, _ = divisor_hit(x, w)
            if b_hit:
                case_b = w
        if interleaved is None:
            if b_hit:
                interleaved = w
            else:
                z0 = (p * w + 1) // 4
                a_hit, _ = divisor_hit(z0, w)
                if a_hit:
                    interleaved = w
        if interleaved is not None and case_b is not None:
            return p, interleaved, case_b
    raise RuntimeError(f"search guard exhausted at p={p}")


def hard_primes(bound: int) -> list[int]:
    """Generate with SymPy's sieve in bounded blocks, retaining exact order."""
    ans: list[int] = []
    block = 5_000_000
    lo = 2
    while lo < bound:
        hi = min(bound, lo + block)
        sieve.extend(hi)
        ans.extend(p for p in sieve.primerange(lo, hi) if p % 24 == 1)
        lo = hi
    return ans


def scan(bound: int, workers: int):
    t0 = time.perf_counter()
    primes = hard_primes(bound)
    t_sieve = time.perf_counter() - t0
    t1 = time.perf_counter()
    if workers == 1:
        rows = [minimal_row(p) for p in primes]
    else:
        ctx = mp.get_context("fork")
        with ctx.Pool(workers) as pool:
            rows = list(pool.imap(minimal_row, primes, chunksize=256))
    t_scan = time.perf_counter() - t1
    return rows, t_sieve, t_scan


def strict_records(rows, field: int, baseline=None):
    records = list(baseline or [])
    running = max((r[1] for r in records), default=-1)
    for row in rows:
        value = row[field]
        if value > running:
            records.append([row[0], value])
            running = value
    return records


def sample_rows(rows, count=2000):
    """Deterministic scale-stratified sample, deliberately overweighting low p."""
    rng = random.Random(0xE5)
    bands = [
        (0, 100_000, 273),
        (100_000, 1_000_000, 400),
        (1_000_000, 10_000_000, 500),
        (10_000_000, 10**30, 827),
    ]
    selected = []
    used = set()
    for lo, hi, want in bands:
        candidates = [row for row in rows if lo <= row[0] < hi]
        take = min(want, len(candidates))
        chosen = candidates if take == len(candidates) else rng.sample(candidates, take)
        selected.extend(chosen)
        used.update(row[0] for row in chosen)
    if len(selected) < count:
        remaining = [row for row in rows if row[0] not in used]
        take = min(count - len(selected), len(remaining))
        selected.extend(rng.sample(remaining, take))
    return sorted(selected[:count])


def subgroup_generated(fac: dict[int, int], w: int) -> set[int]:
    subgroup = {1}
    for prime in fac:
        generator = prime % w
        # Closing under one generator terminates after at most ord_w(generator)
        # rounds; all sets have size at most phi(w) in the coprime branch.
        while True:
            enlarged = subgroup | {a * generator % w for a in subgroup}
            if enlarged == subgroup:
                break
            subgroup = enlarged
    return subgroup


def classify_failure(p: int, w: int, half: str) -> str:
    n = (p + w) // 4 if half == "B" else (p * w + 1) // 4
    literal, fac = divisor_hit(n, w)
    residues = reachable_residues(fac, w)
    target = (-n) % w
    assert literal == (target in residues), (p, w, half)
    assert not literal, ("pair below w* unexpectedly succeeds", p, w, half)
    if gcd(n, w) != 1 or any(gcd(prime, w) != 1 for prime in fac):
        return "F0"
    if (jacobi_symbol(target, w) == -1
            and all(jacobi_symbol(prime, w) == 1 for prime in fac)):
        return "F1"
    subgroup = subgroup_generated(fac, w)
    if target not in subgroup:
        return "F2"
    if target not in residues:
        return "F3"
    return "F4"


def scale_label(p: int) -> str:
    if p < 100_000:
        return "[73,1e5)"
    decade = 10 ** int(math.log10(p))
    return f"[1e{int(math.log10(decade))},1e{int(math.log10(decade))+1})"


def add_count(tree, keys, category):
    node = tree
    for key in keys:
        node = node.setdefault(str(key), {})
    node[category] = node.get(category, 0) + 1


def taxonomy(rows, records):
    samples = sample_rows(rows)
    record_ps = {p for p, _ in records}
    record_rows = [row for row in rows if row[0] in record_ps]
    combined = {}
    record_detail = []
    for population, chosen in (("sample", samples), ("records", record_rows)):
        local = {}
        details = []
        for p, wstar, _ in chosen:
            per_prime = Counter()
            for w in range(3, wstar, 4):
                for half in ("B", "A"):
                    category = classify_failure(p, w, half)
                    per_prime[category] += 1
                    add_count(local, ("overall",), category)
                    add_count(local, ("by_w", w), category)
                    add_count(local, ("by_half", half), category)
                    add_count(local, ("by_scale", scale_label(p)), category)
                    add_count(local, ("by_w_half", w, half), category)
            if population == "records":
                details.append({"p": p, "w_star": wstar,
                                "failures": dict(sorted(per_prime.items()))})
        local["prime_count"] = len(chosen)
        local["failing_pair_count"] = sum(local.get("overall", {}).values())
        combined[population] = local
        if population == "records":
            record_detail = details
    combined["record_details"] = record_detail
    return combined


def divisors_from_factorization(fac: dict[int, int]):
    divs = [1]
    for prime, exponent in fac.items():
        divs = [d * prime**j for d in divs for j in range(2 * exponent + 1)]
    return divs


def decompose_witness(p, q, d, x):
    g0 = gcd(d, x)
    d1 = d // g0
    assert g0 % d1 == 0
    f = g0 // d1
    assert x % (d1 * f) == 0
    x1 = x // (d1 * f)
    assert gcd(d1, x1) == 1
    assert d == d1 * d1 * f and x == d1 * f * x1
    assert (d1 + x1) % q == 0
    k = (d1 + x1) // q
    assert k >= 1
    assert k * p == 4 * d1 * x1 * f * k - d1 - x1
    assert (4 * d1 * f * k - 1) * (4 * x1 * f * k - 1) == 4 * p * f * k * k + 1
    return d1, x1, f, k


def first_case_b_witness(p: int, qmax=63):
    for q in range(3, qmax + 1, 4):
        x = (p + q) // 4
        fac = factorint(x)
        for d in sorted(divisors_from_factorization(fac)):
            if (d + x) % q == 0:
                return q, d, x
    return None


def c_min_k1(p: int, cap=10_000):
    """Least c via p=4abc-a-b; check the smaller of the two factors."""
    for c in range(1, cap + 1):
        number = 4 * p * c + 1
        a = 1
        while (4 * a * c - 1) ** 2 <= number:
            divisor = 4 * a * c - 1
            if (p + a) % divisor == 0:
                b = (p + a) // divisor
                if b >= a and p == 4 * a * b * c - a - b:
                    return c, a, b
            a += 1
    return None


def percentile(values, proportion):
    values = sorted(values)
    return values[round(proportion * (len(values) - 1))]


def dictionary_checks(rows):
    rng = random.Random(0x19)
    f1_checks = 0
    for _ in range(10_000):
        g = rng.randint(1, 10_000)
        u = rng.randint(1, 1_000)
        v = rng.randint(1, 1_000)
        p = 4 * g * u * v - u - v
        q, x, d = u + v, g * u * v, u * u * g
        assert p + q == 4 * x and x * x % d == 0 and (d + x) % q == 0
        reconstructed = (x, p * (x + d) // q, p * (x + x * x // d) // q)
        assert reconstructed == (g * u * v, p * g * u, p * g * v)
        assert sum((Fraction(1, den) for den in reconstructed), Fraction()) == Fraction(4, p)
        f1_checks += 1

    hard_small = [row for row in rows if row[0] < 100_000]
    witness_count = 0
    decomposition_failures = 0
    identity_checks = 0
    replay_witnesses = []
    replay_ps = set(row[0] for row in hard_small[::max(1, len(hard_small) // 20)][:20])
    for p, _, _ in hard_small:
        first = None
        for q in range(3, 64, 4):
            x = (p + q) // 4
            fac = factorint(x)
            for d in divisors_from_factorization(fac):
                if (d + x) % q:
                    continue
                witness_count += 1
                try:
                    a, b, c, k = decompose_witness(p, q, d, x)
                except AssertionError:
                    decomposition_failures += 1
                    raise
                identity_checks += 1
                if first is None:
                    first = [p, q, d, x, a, b, c, k]
        assert first is not None
        if p in replay_ps:
            replay_witnesses.append(first)
    assert len(replay_witnesses) == 20

    c_rows = []
    c_values = []
    missing = []
    missing_below_10k = []
    cross = defaultdict(list)
    for p, _, bq in hard_small:
        # Any positive solution has c=(p+a+b)/(4ab) <= (p+2)/4, so this
        # per-prime cap is exhaustive, not an experimental truncation.
        exhaustive_cap = (p + 2) // 4
        result = c_min_k1(p, exhaustive_cap)
        if result is None:
            missing.append(p)
            missing_below_10k.append(p)
            c_rows.append({"p": p, "case_b_min_q": bq, "c_min_k1": None})
        else:
            c, a, b = result
            assert (4 * a * c - 1) * (4 * b * c - 1) == 4 * p * c + 1
            c_values.append(c)
            if c > 10_000:
                missing_below_10k.append(p)
            cross[bq].append(c)
            c_rows.append({"p": p, "case_b_min_q": bq, "c_min_k1": c,
                           "a": a, "b": b})
    cross_summary = {}
    for q, values in sorted(cross.items()):
        cross_summary[str(q)] = {
            "count": len(values), "min": min(values),
            "median": percentile(values, 0.5), "max": max(values),
        }
    c_distribution = Counter(c_values)
    c_summary = {
        "tested_prime_count": len(hard_small),
        "search_was_exhaustive": True,
        "exhaustive_bound": "c <= floor((p+2)/4)",
        "comparison_cap": 10_000,
        "found_count": len(c_values),
        "no_k1_witness_count": len(missing),
        "no_k1_witness_primes": missing,
        "no_witness_at_c_le_10000_count": len(missing_below_10k),
        "no_witness_at_c_le_10000_primes": missing_below_10k,
        "min": min(c_values) if c_values else None,
        "median": percentile(c_values, 0.5) if c_values else None,
        "p90": percentile(c_values, 0.9) if c_values else None,
        "p99": percentile(c_values, 0.99) if c_values else None,
        "max": max(c_values) if c_values else None,
        "distribution": {str(k): v for k, v in sorted(c_distribution.items())},
        "by_case_b_min_q": cross_summary,
        "rows": c_rows,
    }
    return {
        "random_F1_dictionary_checks": f1_checks,
        "all_case_b_witnesses_q_le_63_hard_p_lt_1e5": witness_count,
        "decomposition_failures": decomposition_failures,
        "factor_identity_checks": identity_checks,
        "replay_witnesses": replay_witnesses,
        "c_min_k1": c_summary,
    }


def growth_fit(records, bound, maximum):
    # Descriptive least-squares fit log(w)=alpha*log(log(p))+beta.  With only
    # a handful of record jumps this is calibration, not a statistical law.
    points = [(p, w) for p, w in records if p > 2 and w > 1]
    xs = [math.log(math.log(p)) for p, _ in points]
    ys = [math.log(w) for _, w in points]
    xm, ym = sum(xs) / len(xs), sum(ys) / len(ys)
    alpha = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sum((x - xm) ** 2 for x in xs)
    beta = ym - alpha * xm
    logs = [math.log(p) for p, _ in points]
    c_log_origin = sum(w * lp for (_, w), lp in zip(points, logs)) / sum(lp * lp for lp in logs)
    return {
        "descriptive_log_power_fit": {"alpha": alpha, "coefficient": math.exp(beta),
                                      "point_count": len(points)},
        "through_origin_c_times_log_p_fit": {"c": c_log_origin},
        "frontier_max_over_log_bound": maximum / math.log(bound),
        "warning": "Record-envelope fits use very few dependent jumps and are descriptive only.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, required=True, help="exclusive prime bound")
    parser.add_argument("--workers", type=int, default=max(1, min(12, mp.cpu_count() // 2)))
    parser.add_argument("--output", default="recorddata.json")
    parser.add_argument("--scan-only", action="store_true")
    args = parser.parse_args()

    rows, sieve_seconds, scan_seconds = scan(args.bound, args.workers)
    records = strict_records(rows, 1)
    # p=3,5 are the exact pre-hard baseline.  Beyond q=3, the separately
    # reported record sequence is measured on every hard prime in this scan.
    b_records = strict_records(rows, 2, baseline=[[3, 1], [5, 3]])
    histogram = Counter(row[1] for row in rows)
    b_histogram = Counter(row[2] for row in rows)
    result = {
        "schema_version": 1,
        "prime_bound_exclusive": args.bound,
        "max_prime_reached": rows[-1][0] if rows else None,
        "hard_prime_count": len(rows),
        "hard_prime_condition": "p prime and p % 24 == 1",
        "modulus_search_guard": max(MODULI),
        "interleaved_records": [{"p": p, "w_star": w} for p, w in records],
        "interleaved_histogram": {str(k): v for k, v in sorted(histogram.items())},
        "case_b_records": [{"p": p, "q_min": q} for p, q in b_records],
        "case_b_histogram_on_hard_primes": {str(k): v for k, v in sorted(b_histogram.items())},
        "timing": {"workers": args.workers, "sieve_seconds": sieve_seconds,
                   "scan_seconds": scan_seconds,
                   "hard_primes_per_scan_second": len(rows) / scan_seconds},
        "growth_fit": growth_fit(records, args.bound, max(histogram)),
    }
    if not args.scan_only:
        t = time.perf_counter()
        result["failure_taxonomy"] = taxonomy(rows, records)
        result["timing"]["taxonomy_seconds"] = time.perf_counter() - t
        t = time.perf_counter()
        result["type_II_dictionary"] = dictionary_checks(rows)
        result["timing"]["dictionary_seconds"] = time.perf_counter() - t
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "bound": args.bound, "hard_primes": len(rows),
        "max_prime": rows[-1][0], "records": records,
        "case_b_records": b_records, "histogram": dict(sorted(histogram.items())),
        "timing": result["timing"],
    }, indent=2))


if __name__ == "__main__":
    main()
