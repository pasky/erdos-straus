#!/usr/bin/env python3
"""Check exact Q tuple certificates and the stored nearest-valuation table."""
from pathlib import Path
import re

BASE = Path("data/z78/r2exact")
expected = {1: (0, 0), 3: (2, 1), 5: (2, 2), 7: (2, 2), 9: (2, 2)}

def v17(n):
    v = 0
    while n % 17 == 0:
        n //= 17
        v += 1
    return v

def vals_v(line, orientation):
    return int(re.search(rf"v17\(4{orientation}\^2d\+5\)=(\d+)", line).group(1))

for k, target in expected.items():
    text = (BASE / f"qnear_k{k}.txt").read_text()
    F = 17**k
    maxes = {}
    for line in text.splitlines():
        if line.startswith("MAX "):
            m = re.search(r"orientation=([ab]) valuation=(\d+)", line)
            assert m
            maxes[m[1]] = int(m[2])
        if line.startswith("HIT "):
            vals = {key: int(value) for key, value in
                    re.findall(r"\b(a|b|c|d|e)=(\d+)", line)}
            a, b, c, d, e = (vals[x] for x in ("a", "b", "c", "d", "e"))
            assert a <= b and a + b == c * e and e % 17
            assert 4*a*b*d == e*F + 1
            assert 4*a*b*c*d == F*(a+b) + c
            assert v17(4*a*a*d + 5) == vals_v(line, "a")
            assert v17(4*b*b*d + 5) == vals_v(line, "b")
    assert (maxes.get("a"), maxes.get("b")) == target, (k, maxes)

witnesses = (BASE / "qnear_k11_witnesses.tsv").read_text().splitlines()[1:]
F = 17**11
for row in witnesses:
    ori, a, b, c, d, e, va, vb = row.split("\t")
    a, b, c, d, e, va, vb = map(int, (a,b,c,d,e,va,vb))
    assert a <= b and a+b == c*e and e % 17
    assert 4*a*b*d == e*F+1 and 4*a*b*c*d == F*(a+b)+c
    assert v17(4*a*a*d+5) == va and v17(4*b*b*d+5) == vb
assert "maximum valuation <=3" in (BASE / "qnear_k11_bracket4.txt").read_text()
print("Q nearest tuple certificates and result table verified")
