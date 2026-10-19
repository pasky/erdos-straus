"""Degree-two ES_q classification and rarity/rank-code experiment.

Reuses the campaign's complete divisor engine for an independent comparison
at q <= 19; larger q use the proved five-curve classification in the memo.
No Cartesian-product arrays; O(q^2) streamed inputs and bounded small caches.
Run: ulimit -v 2000000; timeout 180 uv run python scripts/z45_transfer_logic_toy.py
"""
import json
from math import ceil, log2
from pathlib import Path

import bs_ff_es as ff


def classified(q, b, c):
    v = (c + b + 1) % q
    return (c in (q - 1, q - 2) or v == q - 1
            or c * v % q == q - 1 or c * v * v % q == q - 1)


def main():
    rows = []
    for q in (3, 5, 7, 11, 13, 17, 19, 31, 61, 101, 251, 503):
        ff.Q = q
        ff.factor.cache_clear()
        ff.irreducibles.cache_clear()
        total = solved = mismatches = checked = 0
        first_failure = None
        for b in range(q):
            for c in range(1, q):
                if pow((b * b - 4 * c) % q, (q - 1) // 2, q) != q - 1:
                    continue
                total += 1
                hit = classified(q, b, c)
                solved += hit
                if not hit and first_failure is None:
                    first_failure = [c, b, 1]
                if q <= 19:
                    engine_hit = next(ff.es_solutions((0, 1), (c, b, 1)), None) is not None
                    checked += 1
                    mismatches += engine_hit != hit
        assert total == q * (q - 1) // 2
        assert mismatches == 0
        row = dict(q=q, irreducibles=total, solved=solved, failures=total - solved,
                   solved_over_q=solved / q, solved_fraction=solved / total,
                   generic_index_bits=ceil(log2(total)),
                   failure_index_bits=ceil(log2(total - solved)) if total > solved else None,
                   first_failure_low_to_high=first_failure,
                   compared_with_divisor_engine=checked, mismatches=mismatches)
        rows.append(row)
        print(json.dumps(row), flush=True)
    out = Path('data/z45_transfer_logic')
    out.mkdir(parents=True, exist_ok=True)
    (out / 'toy.json').write_text(json.dumps(rows, indent=2) + '\n')


if __name__ == '__main__':
    main()
