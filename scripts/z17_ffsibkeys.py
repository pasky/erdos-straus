"""z17_ffsibkeys.py (O242): for every q = 3 sibling pair (two balls of the same depth in one parent cylinder, any slice,
alive or not), list all generating data: Case B tuples (census line: s, pattern, m', g', w, C) and Case A data
(alpha, a1', b1, E).  Used to test whether siblings share a 'key' (m', g') (Lemma 1.2 of SIBLING.md).
usage: PYTHONPATH=scripts uv run python scripts/z17_ffsibkeys.py CENSUS DMAX"""
import sys, re
from collections import defaultdict
import bsE_caseA as CA
P = 3; cen, DMAX = sys.argv[1], int(sys.argv[2])
gen = defaultdict(list)
def ball(E, depth):
    E = list(E) + [0] * depth
    return tuple((-E[i]) % P for i in range(depth))
for line in open(cen):
    m = re.match(r"s=(\d+) a=(\d+) b=(\d+) mu=(\d+) y=(\d+) t=(\d+) c=(\d) w=\[([0-9,]*)\] C=\[([0-9,]*)\] m'=\[([0-9,]*)\] g'=\[([0-9,]*)\] E=\[([0-9,]*)\]", line)
    if not m: continue
    s = int(m.group(1)); E = [int(x) for x in m.group(12).split(",")]
    d = (s + 1) // 2 + 1
    if d <= DMAX: gen[ball(E, d)].append(("B", s, m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), "m'=" + m.group(10), "g'=" + m.group(11), "w=" + m.group(8), "C=" + m.group(9)))
for al in range(1, DMAX - 1):
    for (a1, b1, E) in CA.route_A4(P, al):
        gen[ball(E, al + 2)].append(("A", al, "a1'=" + str(list(a1)), "b1=" + str(list(b1)), "E=" + str(list(E))))
par = defaultdict(list)
for u in gen:
    if u[0] == 1 and u[1] != 0: par[u[:-1]].append(u)
for p in sorted(par, key=lambda x: (len(x), x)):
    if len(par[p]) < 2: continue
    print("parent depth", len(p), "".join(map(str, p)), "children", sorted(u[-1] for u in par[p]))
    for u in sorted(par[p]):
        for g in gen[u]: print("    child", u[-1], *g)
