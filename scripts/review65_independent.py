#!/usr/bin/env python3
"""Independent hostile-review replay of the finite census in notes.md §65.

This deliberately does not import verify.py or SymPy.  It uses a private
segmented Eratosthenes sieve, trial-division factorization with Python ints,
and an M-ascending shrinking-survivor scan.  The endpoint is exclusive.
"""
from __future__ import annotations

import argparse
from collections import Counter
from math import isqrt
from time import perf_counter

import numpy as np


CLAIMED_RECORDS = (
    (73, 7, 11, 1),
    (193, 15, 15, 8),
    (1_201, 31, 39, 2),
    (2_521, 47, 55, 16),
    (3_361, 99, 39, 125),
    (33_289, 155, 215, 9),
    (90_841, 167, 551, 294),
    (144_169, 191, 755, 9),
    (167_521, 259, 647, 13),
    (225_289, 279, 811, 245),
    (361_321, 287, 1_259, 3),
    (915_961, 303, 3_023, 2),
    (954_409, 335, 2_855, 504),
    (1_853_329, 383, 4_839, 2),
    (2_031_121, 2_495, 815, 576),
)

# (low, high, count, argmax p, argmax W, W/log p, W/(log p log log p))
CLAIMED_DYADIC = (
    (64, 128, 2, 73, 7, 1.631527, 1.120251),
    (128, 256, 2, 193, 15, 2.850253, 1.716356),
    (256, 512, 5, 457, 15, 2.449106, 1.351360),
    (512, 1_024, 6, 673, 15, 2.303530, 1.229462),
    (1_024, 2_048, 16, 1_201, 31, 4.371794, 2.231858),
    (2_048, 4_096, 31, 3_361, 99, 12.192127, 5.821495),
    (4_096, 8_192, 58, 5_569, 39, 4.521754, 2.098591),
    (8_192, 16_384, 99, 12_721, 47, 4.973014, 2.214045),
    (16_384, 32_768, 200, 29_569, 87, 8.451130, 3.624593),
    (32_768, 65_536, 375, 33_289, 155, 14.885265, 6.352935),
    (65_536, 131_072, 704, 90_841, 167, 14.627482, 6.006953),
    (131_072, 262_144, 1_331, 225_289, 279, 22.636661, 9.012698),
    (262_144, 524_288, 2_548, 361_321, 287, 22.426217, 8.797177),
    (524_288, 1_048_576, 4_815, 954_409, 335, 24.330286, 9.277839),
    (1_048_576, 2_097_152, 9_147, 2_031_121, 2_495, 171.783468, 64.198698),
    (2_097_152, 4_194_304, 17_541, 3_587_809, 391, 25.905959, 9.544481),
    (4_194_304, 8_388_608, 33_433, 5_214_049, 747, 48.296787, 17.634931),
    (8_388_608, 16_777_216, 64_072, 13_383_241, 643, 39.184586, 14.005192),
    (16_777_216, 33_554_432, 123_271, 21_475_609, 911, 53.961431, 19.092786),
    (33_554_432, 67_108_864, 236_663, 39_203_761, 923, 52.790268, 18.449734),
    (67_108_864, 100_000_000, 225_462, 88_808_281, 1_007, 55.021338, 18.927125),
)


def small_primes_through(n: int) -> list[int]:
    """Plain bytearray Eratosthenes sieve, inclusive."""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for q in range(2, isqrt(n) + 1):
        if flags[q]:
            flags[q * q : n + 1 : q] = b"\x00" * (((n - q * q) // q) + 1)
    return [q for q, flag in enumerate(flags) if flag]


def hard_primes_below(limit: int, segment: int = 2_000_000) -> np.ndarray:
    """Segmented sieve of exactly the primes p < limit with p = 1 (mod 24)."""
    if limit <= 2:
        return np.empty(0, dtype=np.int64)
    base = small_primes_through(isqrt(limit - 1))
    chunks: list[np.ndarray] = []
    for low in range(0, limit, segment):
        high = min(limit, low + segment)
        prime = np.ones(high - low, dtype=np.bool_)
        if low == 0:
            prime[: min(2, high)] = False
        for q in base:
            start = max(q * q, ((low + q - 1) // q) * q)
            if start < high:
                prime[start - low :: q] = False
        offsets = np.flatnonzero(prime).astype(np.int64, copy=False)
        values = offsets + np.int64(low)
        chunks.append(values[values % np.int64(24) == 1])
    return np.concatenate(chunks) if chunks else np.empty(0, dtype=np.int64)


def factor_trial(n: int, trial_primes: list[int]) -> tuple[tuple[int, int], ...]:
    """Factor n by trial division; all arithmetic is ordinary Python int."""
    n = int(n)
    factors: list[tuple[int, int]] = []
    for q in trial_primes:
        if q * q > n:
            break
        if n % q:
            continue
        exponent = 0
        while n % q == 0:
            n //= q
            exponent += 1
        factors.append((int(q), exponent))
    if n > 1:
        factors.append((int(n), 1))
    return tuple(factors)


def square_divisors_expansion_order(
    A: int, trial_primes: list[int]
) -> tuple[int, ...]:
    """Divisors of A^2 in the campaign's nested factor-expansion order."""
    values = [1]
    for q, exponent in factor_trial(A, trial_primes):
        values = [int(D * q**e) for D in values for e in range(2 * exponent + 1)]
    return tuple(values)


def build_rows(cap: int) -> tuple[list[tuple[int, tuple[int, ...], dict[int, tuple[int, ...]]]], int]:
    """Build complete residue rows using only Python-int divisor arithmetic."""
    trial_primes = small_primes_through(isqrt((cap + 1) // 4))
    rows = []
    stored_classes = 0
    for M in range(3, cap + 1, 4):
        A = (M + 1) // 4
        by_residue: dict[int, list[int]] = {}
        for D in square_divisors_expansion_order(A, trial_primes):
            residue = int((-4 * D) % M)
            by_residue.setdefault(residue, []).append(D)
        frozen = {residue: tuple(values) for residue, values in by_residue.items()}
        classes = tuple(sorted(frozen))
        stored_classes += len(classes)
        rows.append((M, classes, frozen))
    assert len(rows) == (cap + 1) // 4
    return rows, stored_classes


def scan_minima(
    primes: np.ndarray,
    rows: list[tuple[int, tuple[int, ...], dict[int, tuple[int, ...]]]],
    cap: int,
) -> tuple[np.ndarray, int]:
    """Resolve each prime exactly once, at the first ascending M that hits."""
    assert primes.dtype == np.int64
    W = np.full(primes.size, -1, dtype=np.int32)
    unresolved = np.arange(primes.size, dtype=np.int64)
    last_M = -1
    for M, classes, _ in rows:
        assert M > last_M
        last_M = M
        class_bitmap = np.zeros(M, dtype=np.bool_)
        class_bitmap[np.asarray(classes, dtype=np.int64)] = True
        hit = class_bitmap[primes[unresolved] % np.int64(M)]
        hit_indices = unresolved[hit]
        assert np.all(W[hit_indices] == -1)
        W[hit_indices] = M
        unresolved = unresolved[~hit]
        if not unresolved.size:
            break
    assert not unresolved.size, (
        "modulus cap exhausted",
        cap,
        int(unresolved.size),
        tuple(int(x) for x in primes[unresolved[:10]]),
    )
    assert np.all(W > 0)
    return W, last_M


def strict_records(primes: np.ndarray, W: np.ndarray) -> tuple[tuple[int, int], ...]:
    records: list[tuple[int, int]] = []
    running = -1
    for p0, w0 in zip(primes, W):
        p, w = int(p0), int(w0)
        if w > running:
            records.append((p, w))
            running = w
    return tuple(records)


def selected_divisor_data(
    p: int,
    M: int,
    row_by_M: dict[int, tuple[int, tuple[int, ...], dict[int, tuple[int, ...]]]],
) -> tuple[int, int, int, frozenset[int]]:
    """Return least firing D/a, first-expansion D, and firing parities."""
    firing = row_by_M[M][2][p % M]
    selected_D = min(firing)
    first_D = firing[0]
    parities = frozenset(D % 2 for D in firing)
    assert all((p + 4 * D) % M == 0 for D in firing)
    return selected_D, (p + 4 * selected_D) // M, first_D, parities


def normalized_top(primes: np.ndarray, W: np.ndarray, mode: int, count: int = 10):
    logs = np.log(primes.astype(np.float64))
    denominator = logs if mode == 1 else logs * np.log(logs)
    ratios = W.astype(np.float64) / denominator
    order = np.argsort(ratios, kind="stable")[-count:][::-1]
    return tuple((float(ratios[i]), int(primes[i]), int(W[i])) for i in order)


def dyadic_rows(primes: np.ndarray, W: np.ndarray, limit: int):
    output = []
    low = 64
    while low < limit:
        high = min(2 * low, limit)
        selected = np.flatnonzero((primes >= low) & (primes < high))
        if selected.size:
            local_p, local_w = primes[selected], W[selected]
            first = normalized_top(local_p, local_w, 1, 1)[0]
            second = normalized_top(local_p, local_w, 2, 1)[0]
            output.append((low, high, int(selected.size), first, second))
        low *= 2
    return tuple(output)


def factor_plain(n: int) -> tuple[tuple[int, int], ...]:
    return factor_trial(n, small_primes_through(isqrt(n)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000_000)
    parser.add_argument("--cap", type=int, default=30_000)
    args = parser.parse_args()
    assert args.limit > 73 and args.cap >= 2_495

    started = perf_counter()
    rows, stored_classes = build_rows(args.cap)
    built_at = perf_counter()
    primes = hard_primes_below(args.limit)
    sieved_at = perf_counter()
    W, last_M = scan_minima(primes, rows, args.cap)
    scanned_at = perf_counter()
    row_by_M = {row[0]: row for row in rows}

    records = strict_records(primes, W)
    record_anatomy = []
    for p, M in records:
        D, a, first_D, parities = selected_divisor_data(p, M, row_by_M)
        record_anatomy.append((p, M, a, D, first_D, tuple(sorted(parities))))

    under_10m = np.flatnonzero(primes < 10_000_000)
    selected_parity = Counter()
    expansion_parity = Counter()
    intrinsic = Counter()
    firing_multiplicity = Counter()
    convention_mismatches = []
    for i0 in under_10m:
        i = int(i0)
        p, M = int(primes[i]), int(W[i])
        D, _, first_D, parities = selected_divisor_data(p, M, row_by_M)
        selected_parity["even" if D % 2 == 0 else "odd"] += 1
        expansion_parity["even" if first_D % 2 == 0 else "odd"] += 1
        intrinsic[
            "both" if len(parities) == 2 else "even_only" if 0 in parities else "odd_only"
        ] += 1
        firing_multiplicity[len(row_by_M[M][2][p % M])] += 1
        if D != first_D:
            convention_mismatches.append((p, M, D, first_D))

    histogram = Counter()
    histogram_bounds = (
        (1, 7, "[1,7]"),
        (8, 15, "[8,15]"),
        (16, 31, "[16,31]"),
        (32, 63, "[32,63]"),
        (64, 127, "[64,127]"),
        (128, 255, "[128,255]"),
        (256, 511, "[256,511]"),
        (512, 1_023, "[512,1023]"),
        (1_024, args.cap, "[1024,inf)"),
    )
    for w0 in W[under_10m]:
        w = int(w0)
        histogram[next(label for low, high, label in histogram_bounds if low <= w <= high)] += 1
    sorted_prefix = np.sort(W[under_10m])
    quantile_numerators = (5000, 7500, 9000, 9500, 9900, 9990, 9999, 10000)
    percentiles = tuple(
        int(sorted_prefix[(numerator * sorted_prefix.size + 9_999) // 10_000 - 1])
        for numerator in quantile_numerators
    )

    top_log = normalized_top(primes, W, 1)
    top_loglog = normalized_top(primes, W, 2)
    blocks = dyadic_rows(primes, W, args.limit)

    applicable = []
    violations = []
    for p, M in records:
        if M * M > p + 4:
            factors = factor_plain(p + 4)
            applicable.append((p, M, factors))
            if any(q % 4 == 3 for q, _ in factors):
                violations.append((p, M, factors))

    print("coverage", {"p_min": int(primes[0]), "p_max": int(primes[-1]), "exclusive_limit": args.limit})
    print("dtypes", {"primes": str(primes.dtype), "W": str(W.dtype), "divisors": "Python int"})
    print("class_rows", {"cap": args.cap, "rows": len(rows), "stored_classes": stored_classes})
    print("hard_prime_count", int(primes.size))
    print("last_M_needed", last_M)
    print("records", records)
    print("record_anatomy (p,M,a,selected-D,first-expansion-D,parities)", tuple(record_anatomy))
    print("parity_selected_least_D_below_1e7", dict(selected_parity))
    print("parity_first_expansion_below_1e7", dict(expansion_parity))
    print("selection_convention_mismatches_below_1e7", tuple(convention_mismatches))
    print("intrinsic_parity_below_1e7", dict(intrinsic))
    print("firing_multiplicity_below_1e7", dict(sorted(firing_multiplicity.items())))
    print("histogram_below_1e7", dict(histogram))
    print("nearest_rank_percentiles_below_1e7", percentiles)
    print("top10_W_over_log", top_log)
    print("top10_W_over_loglog", top_loglog)
    print("dyadic")
    for row in blocks:
        print(row)
    print("p_plus_4_applicable", tuple(applicable))
    print("p_plus_4_violations", tuple(violations))
    print("four_late", tuple((p, int(W[np.searchsorted(primes, p)])) for p in (225_289, 954_409, 1_853_329, 2_031_121)))
    print(
        "timings_seconds",
        {
            "classes": built_at - started,
            "prime_sieve": sieved_at - built_at,
            "minimum_scan": scanned_at - sieved_at,
            "total": perf_counter() - started,
        },
    )

    if args.limit == 100_000_000 and args.cap == 30_000:
        assert stored_classes == 244_216
        assert primes.size == 719_781 and primes[-1] == 99_999_721
        assert under_10m.size == 82_887
        assert last_M == 2_495
        assert records == tuple((p, M) for p, M, _, _ in CLAIMED_RECORDS)
        assert tuple((p, M, a, D) for p, M, a, D, _, _ in record_anatomy) == CLAIMED_RECORDS
        assert all(a * M == p + 4 * D for p, M, a, D, _, _ in record_anatomy)
        assert not convention_mismatches
        assert selected_parity == Counter({"even": 49_975, "odd": 32_912})
        assert expansion_parity == selected_parity
        assert intrinsic == Counter({"even_only": 49_975, "odd_only": 32_454, "both": 458})
        assert max(firing_multiplicity) == 2
        assert histogram == Counter({
            "[1,7]": 41_577,
            "[8,15]": 26_959,
            "[16,31]": 8_632,
            "[32,63]": 3_989,
            "[64,127]": 1_463,
            "[128,255]": 223,
            "[256,511]": 40,
            "[512,1023]": 3,
            "[1024,inf)": 1,
        })
        assert len(set(int(w) for w in W[under_10m])) == 67
        assert percentiles == (7, 15, 23, 39, 87, 203, 351, 2_495)
        assert np.isfinite(top_log[0][0]) and np.isfinite(top_loglog[0][0])
        assert (top_log[0][1], top_log[0][2], round(top_log[0][0], 6)) == (2_031_121, 2_495, 171.783468)
        assert (top_loglog[0][1], top_loglog[0][2], round(top_loglog[0][0], 6)) == (2_031_121, 2_495, 64.198698)
        observed_dyadic = tuple(
            (
                low,
                high,
                count,
                first[1],
                first[2],
                round(first[0], 6),
                round(second[0], 6),
            )
            for low, high, count, first, second in blocks
        )
        assert observed_dyadic == CLAIMED_DYADIC
        assert tuple((p, M) for p, M, _ in applicable) == (
            (193, 15),
            (3_361, 99),
            (2_031_121, 2_495),
        )
        assert not violations
        print("CLAIM_COMPARISON_OK")


if __name__ == "__main__":
    main()
