#!/usr/bin/env python3
"""Exact sparse union for L1, P3, Q3, P5 on the r-generic line.

Run from repository root with `uv run --offline --no-project python -B scripts/z78_exact_union.py [r ...]`.
Output cells are at common depth 3; counts are marginal newly covered nonsquare
cells, in the required L1, P3, Q3, P5 order. Enumeration is sequential.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/z78/exact"
OUT.mkdir(parents=True, exist_ok=True)
ENUM = ROOT / "scripts/z78_exact_enum.c"
EXE = OUT / "enum.bin"


def family(r: int, typ: str, exponent: int) -> set[int]:
    p = subprocess.run([str(EXE), str(r), typ, str(exponent)], check=True,
                       capture_output=True, text=True, timeout=1700)
    residues = set()
    for line in p.stdout.splitlines():
        _, x = line.split()
        residues.add(int(x))
    (OUT / f"r{r}_{typ.lower()}{exponent}.txt").write_text("\n".join(map(str, sorted(residues))) + "\n")
    return residues


def is_square_mod(x: int, r: int) -> bool:
    return x % r == 0 or pow(x % r, (r - 1) // 2, r) == 1


def one(r: int) -> list[int]:
    # All families are lifted to r^3; each residue is a depth-3 cylinder.
    mod = r ** 3
    stages = [
        ("L1", (family(r, "P", 1) | family(r, "Q", 1)), r),
        ("P3", family(r, "P", 3), r ** 2),
        ("Q3", family(r, "Q", 3), r ** 3),
        ("P5", family(r, "P", 5), r ** 3),
    ]
    universe = [x for x in range(mod) if not is_square_mod(x, r)]
    live = set(universe)
    counts = []
    for name, boxes, depthmod in stages:
        covered = set()
        for b in boxes:
            # residues divisible by r lie in the square class; filter by first digit.
            if not is_square_mod(b, r):
                covered.update(range(b, mod, depthmod))
        new = live & covered
        counts.append(len(new))
        live.difference_update(new)
    return counts


def main() -> None:
    primes = [int(x) for x in sys.argv[1:]] or [17]
    subprocess.run(["gcc", "-O3", str(ENUM), "-o", str(EXE)], check=True, timeout=60)
    rows = []
    for r in primes:
        cs = one(r)
        rows.append((r, *cs))
        print(r, *cs, flush=True)
    table = "r\tl1\tp3\tq3\tp5\n" + "".join("\t".join(map(str, row)) + "\n" for row in rows)
    (OUT / "union.tsv").write_text(table)


if __name__ == "__main__":
    main()
