#!/usr/bin/env python3
"""Exact finite a-frame failure and first-a censuses for notes.md §72.

Prime generation uses chunked NumPy boolean bitmaps.  Every value passed to
factorization, every residue product, and every divisor-side operation is an
ordinary Python int.  Intervals are half open.  The JSON output contains exact
counts plus explicitly informational floating-point normalizations.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from collections.abc import Iterable
from hashlib import sha256
from math import isqrt, log, sqrt
from pathlib import Path
from time import perf_counter

import numpy as np
from sympy import factorint, isprime, jacobi_symbol

WINDOWS = (
    (100_000, 200_000),
    (1_000_000, 1_200_000),
    (10_000_000, 10_200_000),
    (100_000_000, 100_200_000),
)
PAIR_MODULI = (3, 7, 11, 19, 23, 31)
BUDGET_MODULI = (31, 43, 59, 79, 103, 127, 151, 199)
HISTOGRAM_1M = {
    3: 5_192, 7: 3_551, 11: 584, 15: 131, 19: 113, 23: 96,
    27: 8, 31: 33, 35: 4, 39: 9, 43: 1, 47: 3, 51: 2,
    55: 2, 59: 2, 63: 1,
}
HISTOGRAM_10M = {
    3: 47_137, 7: 28_606, 11: 4_419, 15: 961, 19: 766,
    23: 637, 27: 63, 31: 183, 35: 27, 39: 44, 43: 7, 47: 23,
    51: 2, 55: 4, 59: 4, 63: 1, 71: 2, 107: 1,
}
HISTOGRAM_100M = {
    3: 430_409, 7: 235_146, 11: 35_036, 15: 7_736, 19: 5_323,
    23: 4_040, 27: 437, 31: 1_059, 35: 143, 39: 227, 43: 33,
    47: 120, 51: 16, 55: 20, 59: 20, 63: 6, 71: 7, 79: 1,
    91: 1, 107: 1,
}
ANATOMY_DIGEST_100M = (
    "5d1f08c0054b6ff858259c8dd59c8a5c8d60c0cde83b37d1d19d77af9e2bf1e8"
)


def numpy_primes_through(n: int) -> list[int]:
    """Return primes <= n; the only array here is a prime-sieve bitmap."""
    if n < 2:
        return []
    prime = np.ones(n + 1, dtype=np.bool_)
    prime[:2] = False
    for q0 in np.flatnonzero(prime[: isqrt(n) + 1]):
        q = int(q0)
        if q >= 2:
            prime[q * q :: q] = False
    return [int(q) for q in np.flatnonzero(prime)]


def hard_prime_chunks(
    low: int, high: int, chunk_size: int = 1_000_000
) -> Iterable[tuple[int, int, list[int]]]:
    """Yield primes p=1 (mod 24) in [low,high), one bounded chunk at a time."""
    assert 0 <= low < high and chunk_size > 0
    base = numpy_primes_through(isqrt(high - 1))
    for chunk_low in range(low, high, chunk_size):
        chunk_high = min(high, chunk_low + chunk_size)
        prime = np.ones(chunk_high - chunk_low, dtype=np.bool_)
        if chunk_low == 0:
            prime[: min(2, chunk_high)] = False
        elif chunk_low == 1:
            prime[0] = False
        for q in base:
            start = max(q * q, ((chunk_low + q - 1) // q) * q)
            if start < chunk_high:
                prime[start - chunk_low :: q] = False
        offsets = np.flatnonzero(prime)
        # NumPy remains confined to prime enumeration.  Convert at ingress to
        # the factor/residue path and never retain a NumPy scalar there.
        values = [
            int(chunk_low + int(offset))
            for offset in offsets
            if (chunk_low + int(offset)) % 24 == 1
        ]
        yield chunk_low, chunk_high, values


def factors_python(n: int) -> tuple[tuple[int, int], ...]:
    """SymPy factorization normalized immediately to Python ints."""
    n = int(n)
    return tuple((int(q), int(e)) for q, e in factorint(n).items())


def ratio_success(a: int, factors: tuple[tuple[int, int], ...]) -> bool:
    """Test -1 in the exact bounded-exponent ratio spectrum modulo a."""
    a = int(a)
    target = a - 1
    reachable = {1}
    for q, budget in factors:
        c = int(q % a)
        assert c and pow(c, -1, a)
        powers = {int(pow(c, exponent, a))
                  for exponent in range(-budget, budget + 1)}
        reachable = {int(r * power % a)
                     for r in reachable for power in powers}
        assert len(reachable) <= a
        if target in reachable:
            return True
    return target in reachable


def subgroup_contains_minus_one(
    a: int, factors: tuple[tuple[int, int], ...]
) -> bool:
    """Exact unbudgeted subgroup test, used only as an F3 structure audit."""
    target = a - 1
    subgroup = {1}
    for q, _ in factors:
        c = int(q % a)
        powers = []
        value = 1
        while value not in powers:
            powers.append(value)
            value = int(value * c % a)
        assert value == 1 and len(powers) <= a - 1
        subgroup = {int(r * power % a)
                    for r in subgroup for power in powers}
        if target in subgroup:
            return True
    return target in subgroup


def prime_failure_kind(
    a: int, factors: tuple[tuple[int, int], ...]
) -> tuple[str, int]:
    """Classify an already-established failure at prime a as F1 or F3."""
    assert a % 4 == 3 and isprime(a)
    sigma = 0
    for q, _ in factors:
        symbol = int(jacobi_symbol(q, a))
        assert symbol in (-1, 1)
        sigma += symbol == -1
    if sigma == 0:
        return "F1", sigma
    # A violation here would contradict the structure theorem under review.
    assert subgroup_contains_minus_one(a, factors), (
        "F3 subgroup counterexample", a, factors
    )
    return "F3", sigma


def prime_moduli_through(cap: int) -> tuple[int, ...]:
    return tuple(a for a in range(3, cap + 1, 4) if isprime(a))


def omega_bin(omega: int) -> str:
    return str(omega) if omega <= 4 else "5+"


def scan_windows(
    windows: tuple[tuple[int, int], ...] = WINDOWS,
    chunk_size: int = 1_000_000,
) -> dict:
    """Tasks 1, 2, and 5: frequencies, dependence, and budget transition."""
    started = perf_counter()
    moduli = prime_moduli_through(199)
    result: dict[str, object] = {
        "interval_convention": "half-open [low,high)",
        "prime_moduli": list(moduli),
        "windows": {},
        "dependence": {},
        "budget_conditioning": {},
    }
    for low, high in windows:
        window_started = perf_counter()
        stats = {a: Counter() for a in moduli}
        joint = Counter()
        budget = {
            a: {label: Counter() for label in ("1", "2", "3", "4", "5+")}
            for a in BUDGET_MODULI
        }
        n = 0
        p_sum = 0
        for _, _, primes in hard_prime_chunks(low, high, chunk_size):
            for p in primes:
                n += 1
                p_sum += p
                failures: dict[int, bool] = {}
                for a in moduli:
                    h = int((p + a) // 4)
                    factors = factors_python(h)
                    failed = not ratio_success(a, factors)
                    failures[a] = failed
                    row = stats[a]
                    if not failed:
                        row["success"] += 1
                        continue
                    kind, sigma = prime_failure_kind(a, factors)
                    assert kind in ("F1", "F3")
                    row["fail"] += 1
                    row[kind] += 1
                    row["sigma_sum"] += sigma
                    if low == 10_000_000 and a in BUDGET_MODULI:
                        budget[a][omega_bin(len(factors))][kind] += 1
                if low in (1_000_000, 10_000_000):
                    for i, a in enumerate(PAIR_MODULI):
                        for b in PAIR_MODULI[i + 1:]:
                            if failures[a] and failures[b]:
                                joint[(a, b)] += 1
        assert n and all(stats[a]["fail"] + stats[a]["success"] == n
                         for a in moduli)
        p_bar = p_sum / n
        rows = {}
        for a in moduli:
            fail = int(stats[a]["fail"])
            f1 = int(stats[a]["F1"])
            f3 = int(stats[a]["F3"])
            assert fail == f1 + f3
            frequency = fail / n
            rows[str(a)] = {
                "fail": fail,
                "F1": f1,
                "F3": f3,
                "frequency_info": frequency,
                "frequency_sqrt_log_pbar_info": frequency * sqrt(log(p_bar)),
                "F3_share_info": (f3 / fail if fail else None),
            }
        key = f"{low}:{high}"
        result["windows"][key] = {
            "n": n,
            "p_sum": p_sum,
            "p_bar_info": p_bar,
            "per_a": rows,
            "seconds_info": perf_counter() - window_started,
        }
        if low in (1_000_000, 10_000_000):
            dependency_rows = []
            for i, a in enumerate(PAIR_MODULI):
                fa = int(stats[a]["fail"])
                for b in PAIR_MODULI[i + 1:]:
                    fb = int(stats[b]["fail"])
                    both = int(joint[(a, b)])
                    dependency_rows.append({
                        "a": a, "b": b, "n": n,
                        "fail_a": fa, "fail_b": fb, "joint": both,
                        "ratio_info": (both * n / (fa * fb)
                                       if fa and fb else None),
                    })
            result["dependence"][key] = dependency_rows
        if low == 10_000_000:
            budget_rows = {}
            for a in BUDGET_MODULI:
                by_omega = {}
                for label in ("1", "2", "3", "4", "5+"):
                    f1 = int(budget[a][label]["F1"])
                    f3 = int(budget[a][label]["F3"])
                    failures = f1 + f3
                    by_omega[label] = {
                        "fail": failures, "F1": f1, "F3": f3,
                        "F3_share_info": f3 / failures if failures else None,
                    }
                budget_rows[str(a)] = by_omega
            result["budget_conditioning"][key] = budget_rows
    result["seconds_info"] = perf_counter() - started
    return result


def first_a_with_trail(p: int) -> tuple[int, list[dict]]:
    """Return a_1 and every preceding failure; no artificial a cutoff."""
    B = (p + 1) // 3
    trail: list[dict] = []
    for a in range(3, 2 * B + 1, 4):
        h = int((p + a) // 4)
        factors = factors_python(h)
        if ratio_success(a, factors):
            return a, trail
        entry = {"a": a, "omega": len(factors), "prime": bool(isprime(a))}
        if entry["prime"]:
            kind, sigma = prime_failure_kind(a, factors)
            entry.update({"kind": kind, "sigma": sigma})
        else:
            entry.update({"kind": "C", "sigma": None})
        trail.append(entry)
    raise AssertionError(("finite admissible range exhausted", p, 2 * B))


def sorted_counter(counter: Counter) -> dict[str, int]:
    return {str(k): int(counter[k]) for k in sorted(counter)}


def atomic_json(path: Path, data: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def scan_a1(
    limit: int = 100_000_000,
    chunk_size: int = 1_000_000,
    checkpoint: Path | None = None,
) -> dict:
    """Tasks 3 and 4: complete a_1 histogram and deep-failure anatomy."""
    assert limit > 73
    started = perf_counter()
    thresholds = tuple(x for x in (1_000_000, 10_000_000, 100_000_000)
                       if x <= limit)
    histograms = {bound: Counter() for bound in thresholds}
    counts = Counter()
    total_histogram = Counter()
    deep_rows: list[dict] = []
    record_rows: list[dict] = []
    all_prime_failures = Counter()
    deep_prime_failures = Counter()
    record_prime_failures = Counter()
    chunks: list[dict] = []
    running_max = -1
    max_a1 = -1
    maximum_primes: list[int] = []

    for chunk_low, chunk_high, primes in hard_prime_chunks(2, limit, chunk_size):
        chunk_started = perf_counter()
        chunk_histogram = Counter()
        chunk_deep = 0
        for p in primes:
            a1, trail = first_a_with_trail(p)
            chunk_histogram[a1] += 1
            total_histogram[a1] += 1
            for bound in thresholds:
                if p < bound:
                    histograms[bound][a1] += 1
                    counts[bound] += 1
            prime_trail = [row for row in trail if row["prime"]]
            for row in prime_trail:
                all_prime_failures[row["kind"]] += 1
            is_record = a1 > running_max
            if is_record:
                running_max = a1
                record = {"p": p, "a1": a1, "failures": trail}
                record_rows.append(record)
                for row in prime_trail:
                    record_prime_failures[row["kind"]] += 1
            if a1 > running_max:
                raise AssertionError("record ordering failure")
            if not maximum_primes or a1 > max_a1:
                max_a1 = a1
                maximum_primes = [p]
            elif a1 == max_a1:
                maximum_primes.append(p)
            if a1 >= 43:
                chunk_deep += 1
                row = {"p": p, "a1": a1, "failures": trail}
                deep_rows.append(row)
                for failure in prime_trail:
                    deep_prime_failures[failure["kind"]] += 1
        chunk_row = {
            "low": chunk_low, "high": chunk_high,
            "hard_primes": len(primes),
            "histogram": sorted_counter(chunk_histogram),
            "deep_count": chunk_deep,
            "seconds_info": perf_counter() - chunk_started,
        }
        chunks.append(chunk_row)
        if checkpoint is not None:
            partial = {
                "exclusive_limit": limit,
                "completed_through": chunk_high,
                "hard_primes_completed": int(sum(counts.values())
                                              if len(thresholds) == 1
                                              else sum(total_histogram.values())),
                "cumulative_histogram": sorted_counter(total_histogram),
                "chunks": chunks,
            }
            atomic_json(checkpoint, partial)

    if 1_000_000 in histograms:
        assert dict(sorted(histograms[1_000_000].items())) == HISTOGRAM_1M
        assert counts[1_000_000] == 9_732
    if 10_000_000 in histograms:
        assert dict(sorted(histograms[10_000_000].items())) == HISTOGRAM_10M
        assert counts[10_000_000] == 82_887
    canonical_anatomy = [
        (row["p"], row["a1"],
         [(failure["a"], failure["kind"], failure["sigma"])
          for failure in row["failures"]])
        for row in deep_rows
    ]
    anatomy_digest = sha256(json.dumps(
        canonical_anatomy, separators=(",", ":")
    ).encode()).hexdigest()
    if limit == 100_000_000:
        assert counts[100_000_000] == 719_781
        assert dict(sorted(total_histogram.items())) == HISTOGRAM_100M
        assert (max_a1, maximum_primes) == (107, [8_803_369])
        assert anatomy_digest == ANATOMY_DIGEST_100M

    def share(counter: Counter) -> float | None:
        denominator = counter["F1"] + counter["F3"]
        return counter["F3"] / denominator if denominator else None

    result = {
        "interval_convention": "all hard primes 2 <= p < limit",
        "exclusive_limit": limit,
        "hard_prime_count": int(sum(total_histogram.values())),
        "histograms": {str(bound): sorted_counter(histograms[bound])
                       for bound in thresholds},
        "histogram": sorted_counter(total_histogram),
        "maximum_a1": max_a1,
        "maximum_primes": maximum_primes,
        "strict_records": record_rows,
        "deep_threshold": 43,
        "deep_rows": deep_rows,
        "deep_anatomy_sha256": anatomy_digest,
        "failure_enrichment": {
            "all_hard_primes": {
                "F1": int(all_prime_failures["F1"]),
                "F3": int(all_prime_failures["F3"]),
                "F3_share_info": share(all_prime_failures),
            },
            "a1_at_least_43": {
                "primes": len(deep_rows),
                "F1": int(deep_prime_failures["F1"]),
                "F3": int(deep_prime_failures["F3"]),
                "F3_share_info": share(deep_prime_failures),
            },
            "strict_record_primes": {
                "primes": len(record_rows),
                "F1": int(record_prime_failures["F1"]),
                "F3": int(record_prime_failures["F3"]),
                "F3_share_info": share(record_prime_failures),
            },
        },
        "chunks": chunks,
        "seconds_info": perf_counter() - started,
        "cross_checks": {
            "histogram_1m": 1_000_000 in histograms,
            "histogram_10m": 10_000_000 in histograms,
            "hard_prime_count_100m": limit == 100_000_000,
        },
    }
    return result


def parse_windows(text: str) -> tuple[tuple[int, int], ...]:
    if text == "campaign":
        return WINDOWS
    rows = []
    for item in text.split(","):
        low, high = item.split(":", 1)
        rows.append((int(low), int(high)))
    return tuple(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=("windows", "a1", "all"),
                        required=True)
    parser.add_argument("--limit", type=int, default=100_000_000,
                        help="exclusive endpoint for --task a1/all")
    parser.add_argument("--windows", default="campaign",
                        help="campaign or comma-separated low:high pairs")
    parser.add_argument("--chunk-size", type=int, default=1_000_000)
    parser.add_argument("--checkpoint", type=Path,
                        help="atomically updated per-chunk a1 checkpoint")
    parser.add_argument("--output", type=Path,
                        help="write JSON here instead of standard output")
    args = parser.parse_args()

    output: dict[str, object] = {}
    if args.task in ("windows", "all"):
        output["windows"] = scan_windows(
            parse_windows(args.windows), args.chunk_size
        )
    if args.task in ("a1", "all"):
        output["a1"] = scan_a1(args.limit, args.chunk_size, args.checkpoint)
    text = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
