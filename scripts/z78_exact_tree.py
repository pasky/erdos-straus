#!/usr/bin/env python3
"""Exact branch histograms for the L1/P3/Q3/P5/U tree through depth 3."""
from collections import Counter, defaultdict
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


def family(r: int, typ: str, k: int) -> set[int]:
    target = OUT / f"r{r}_{typ.lower()}{k}.txt"
    if typ == "P" and k == 5:
        subprocess.run([str(ET_EXE), str(r), str(target)], check=True, timeout=1700)
        return {int(x) for x in target.read_text().splitlines()}
    run = subprocess.run([str(EXE), str(r), typ, str(k)], check=True,
                         capture_output=True, text=True, timeout=1700)
    ans = {int(line.split()[1]) for line in run.stdout.splitlines()}
    target.write_text("\n".join(map(str, sorted(ans))) + "\n")
    return ans


def is_nonsquare(x: int, r: int) -> bool:
    return x % r != 0 and pow(x % r, (r - 1) // 2, r) == r - 1


def make_tree(r: int) -> str:
    boxes = defaultdict(set)
    # M17B Lemma 1.1: every U-box is contained in a P-box, so P/Q gives the same union.
    boxes[1] = family(r, "P", 1) | family(r, "Q", 1)
    boxes[2] = family(r, "P", 3)
    boxes[3] = family(r, "P", 5) | family(r, "Q", 3)
    nonres = [v for v in range(1, r) if is_nonsquare(v, r)]
    out = [f"r = {r}: non-residues {nonres}; level-1 boxes {sorted(boxes[1])}"]
    for v in nonres:
        if v in boxes[1]:
            out.append(f"  cell C_{v}: covered at level 1")
            continue
        alive = 1.0
        out.append(f"  cell C_{v}:")
        for d in (2, 3):
            fresh = [x for x in boxes[d] if x % r == v and
                     all(x % (r ** j) not in boxes[j] for j in range(1, d))]
            parents = Counter(x % (r ** (d - 1)) for x in fresh)
            hist = Counter(parents.values())
            alive -= len(fresh) / (r ** (d - 1))
            out.append(f"    d{d}: new {len(fresh)}, alive {alive:.8f}, max {max(parents.values(), default=0)}, hist {dict(sorted(hist.items()))}")
    return "\n".join(out) + "\n"


def main() -> None:
    subprocess.run(["gcc", "-O3", str(ENUM), "-o", str(EXE)], check=True, timeout=60)
    subprocess.run(["g++", "-O3", "-std=c++17", str(ET), "-o", str(ET_EXE)], check=True, timeout=60)
    for r in map(int, sys.argv[1:]):
        text = make_tree(r)
        path = OUT / f"rtree{r}_d3.txt"
        path.write_text(text)
        print(text, end="", flush=True)


if __name__ == "__main__":
    main()
