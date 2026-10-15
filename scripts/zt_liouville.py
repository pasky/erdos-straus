"""zt_liouville.py (O227): check FF_THIRDS_CORNER Lemma 1.1/1.2 on the exact q = 3 census of Case B tuples.

Input: output of `bsE_famcount 3 2 SMAX print` (lines s=.. a=.. ... w=[..] C=[..] m'=[..] g'=[..] E=[..]).
For every tuple: recompute v, w1, C1, v1, E independently, verify (B) and E*C1 = g'T^{s-1} + w1, and for each
polynomial slice point u of degree h <= HMAX with u(0) = 1 compute the agreement depth
dep(u) = max{m : E = -u mod T^m}; check Lemma 1.2: min(dep, s-1) <= max(a-1, b-1+h) unless w1 = -u*C1.
Also tabulates, per s, the lopsided tuples (max(a-1, b) >= N(s)+1) and which tuples cover x*_c.
usage: python zt_liouville.py FILE [HMAX]
"""
import itertools
import re
import sys

from zt_poly import add, mul, divmod_, mono, deg, tval, sub, neg, norm

f = sys.argv[1]
HMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 3
pat = re.compile(r"s=(\d+) a=(\d+) b=(\d+) mu=(\d+) y=(\d+) t=(\d+) c=(\d+) w=\[(.*?)\] C=\[(.*?)\] m'=\[(.*?)\] g'=\[(.*?)\] E=\[(.*?)\]")


def L(x):
    return norm([int(v) for v in x.split(",")]) if x else []


def Nof(s, k=2):
    return -(-(s + k - 2) // 2)


us = []
for h in range(1, HMAX + 1):
    for tail in itertools.product(range(3), repeat=h):
        if tail[-1] == 0:
            continue
        us.append([1] + list(tail))

ntup = 0
viol = 0
exact = 0
per_s = {}
for line in open(f):
    m = pat.search(line)
    if not m:
        continue
    s, a, b = int(m[1]), int(m[2]), int(m[3])
    w, C, mp, gp, Ef = L(m[8]), L(m[9]), L(m[10]), L(m[11]), L(m[12])
    ntup += 1
    # independent recomputation
    wC = mul(w, C)
    v = sub(mul(mp, wC), mono(s))
    assert v and add(w, C) == mul(gp, v), "identity (B)"
    assert tval(w) == 1 and tval(C) == 1 and tval(v) >= 2
    w1, C1, v1 = w[1:], C[1:], v[2:]
    Lp = mul(gp, mp)
    E = sub(mul(Lp, w), [1])
    assert E == Ef
    assert mul(E, C1) == add(mul(gp, mono(s - 1)), w1), "Lemma 1.1"
    N = Nof(s)
    dS = per_s.setdefault(s, [0, 0, 0, 0])
    dS[0] += 1
    if max(a - 1, b) >= N + 1:
        dS[1] += 1
    for u in us:
        h = deg(u)
        r = add(E, u)
        dep = tval(r)
        if dep >= N + 1 and h == 1:
            dS[2] += 1
        if mul(neg(u), C1) == w1:
            exact += 1
            if h == 1:
                viol += 1  # Lemma 1.2 says impossible for h = 1
            continue
        if min(dep, s - 1) > max(a - 1, b - 1 + h):
            viol += 1
            print("VIOLATION", s, a, b, u, dep)
print(f"tuples {ntup}; polynomial points tested {len(us)} (deg 1..{HMAX}); Lemma 1.2 violations {viol}; exact w1=-uC1 cases (h>=2) {exact}")
print("s  tuples  lopsided(max(a-1,b)>=N+1)  covering x*_c (both c)")
for s in sorted(per_s):
    print(s, *per_s[s][:3])
