#!/usr/bin/env python3
"""Cellwise comparison of primary and independent native depth-3 lists."""
from pathlib import Path

ROOT = Path("data/z78/r2exact")

def values(path):
    return {int(word) for line in path.read_text().splitlines()
            if line and not line.startswith("#") for word in line.split()}

rows = ["r\tfamily\tprimary\tindependent\tequal"]
for r in (223, 929):
    def primary(family):
        return values(ROOT / f"sample{r}.{family}.tsv")

    cf_lines = (ROOT / f"independent{r}.cf.tsv").read_text().splitlines()
    for family in ("L1", "P3"):
        other = {int(line.split()[1]) for line in cf_lines
                 if line.startswith(f"{family} ")}
        got = primary(family)
        assert got == other, (r, family, len(got), len(other), len(got ^ other))
        rows.append(f"{r}\t{family}\t{len(got)}\t{len(other)}\tYES")

    other_q = values(ROOT / f"independent{r}.qalt.Q3.tsv")
    got_q = primary("Q3")
    assert got_q == other_q, (r, "Q3", len(got_q), len(other_q), len(got_q ^ other_q))
    rows.append(f"{r}\tQ3\t{len(got_q)}\t{len(other_q)}\tYES")

    raw = values(ROOT / f"independent{r}.P5raw.tsv")
    l1, p3 = primary("L1"), primary("P3")
    nonsquare = lambda x: x % r != 0 and pow(x % r, (r - 1) // 2, r) == r - 1
    other_p = {x for x in raw if nonsquare(x) and x % r not in l1
               and x % (r*r) not in p3 and x not in other_q}
    got_p = primary("P5")
    assert got_p == other_p, (r, "P5", len(got_p), len(other_p), len(got_p ^ other_p))
    rows.append(f"{r}\tP5\t{len(got_p)}\t{len(other_p)}\tYES")

report = "\n".join(rows) + "\n"
(ROOT / "validation.tsv").write_text(report)
print(report, end="")
