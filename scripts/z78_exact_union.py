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
ET = ROOT / "scripts/z78_exact_et.cpp"
EXE = OUT / "enum.bin"
ET_EXE = OUT / "et.bin"


def family(r: int, typ: str, exponent: int) -> set[int]:
    target = OUT / f"r{r}_{typ.lower()}{exponent}.txt"
    if typ == "P" and exponent == 5:
        subprocess.run([str(ET_EXE), str(r), str(target)], check=True, timeout=1700)
        return {int(line) for line in target.read_text().splitlines()}
    p = subprocess.run([str(EXE), str(r), typ, str(exponent)], check=True,
                       capture_output=True, text=True, timeout=1700)
    residues = set()
    for line in p.stdout.splitlines():
        _, x = line.split()
        residues.add(int(x))
    target.write_text("\n".join(map(str, sorted(residues))) + "\n")
    return residues


def is_square_mod(x: int, r: int) -> bool:
    return x % r == 0 or pow(x % r, (r - 1) // 2, r) == 1


def one(r: int) -> list[int]:
    # Keep cylinders at native depth. Only reduce to ancestors for containment
    # tests, and scale the final sparse box counts to depth 3 at the very end.
    stages = [
        ("L1", (family(r, "P", 1) | family(r, "Q", 1)), 1),
        ("P3", family(r, "P", 3), 2),
        ("Q3", family(r, "Q", 3), 3),
        ("P5", family(r, "P", 5), 3),
    ]
    covered: dict[int, set[int]] = {1: set(), 2: set(), 3: set()}
    marginal = []
    for _, boxes, depth in stages:
        fresh = set()
        for box in boxes:
            if is_square_mod(box, r):
                continue
            if any(box % (r ** d) in covered[d] for d in range(1, depth + 1)):
                continue
            fresh.add(box)
        covered[depth].update(fresh)
        marginal.append(len(fresh) * r ** (3 - depth))
    return marginal


def main() -> None:
    primes = [int(x) for x in sys.argv[1:]] or [17]
    subprocess.run(["gcc", "-O3", str(ENUM), "-o", str(EXE)], check=True, timeout=60)
    subprocess.run(["g++", "-O3", "-std=c++17", str(ET), "-o", str(ET_EXE)], check=True, timeout=60)
    rows = []
    for r in primes:
        cs = one(r)
        rows.append((r, *cs))
        print(r, *cs, flush=True)
    table_rows = {}
    table_path = OUT / "union.tsv"
    if table_path.exists():
        for line in table_path.read_text().splitlines()[1:]:
            if line.strip():
                row = tuple(map(int, line.split("\t")))
                table_rows[row[0]] = row
    table_rows.update({row[0]: row for row in rows})
    table = "r\tl1\tp3\tq3\tp5\n" + "".join(
        "\t".join(map(str, table_rows[r])) + "\n" for r in sorted(table_rows))
    table_path.write_text(table)


if __name__ == "__main__":
    main()
