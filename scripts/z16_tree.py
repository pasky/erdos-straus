"""z16_tree.py (O241): the survivor tree of the c-slices of O(3, T^2) at low depth (EVIDENCE tool).
Forbidden balls ("tuple balls") on the slice u = 1 + cT + ... (k = 2):
  Case B tuple of parameter s: u == -E (mod T^{N(s)+1}), N(s) = ceil(s/2)   [census: bsE_famcount 3 2 SMAX print]
  Case A datum of depth alpha: u == -E (mod T^{alpha+2})                    [bsE_caseA.route_A4]
Complete for ball depth <= DMAX when SMAX >= 2(DMAX-1) and alpha <= DMAX-2.
For each c and depth n: survivors S_n (cylinders mod T^n not inside any ball of depth <= n), forbidden balls of
depth n, and the number of surviving parents at depth n-1 with exactly j = 0..3 forbidden children ("sibling
profile"; j = 3 kills the parent).  Also the branching ratio S_n / S_{n-1}.
usage: PYTHONPATH=scripts uv run python scripts/z16_tree.py CENSUS DMAX"""
import sys, re
from collections import defaultdict
import bsE_caseA as CA

P = 3
cen, DMAX = sys.argv[1], int(sys.argv[2])
balls = defaultdict(set)          # depth -> set of tuples (u mod T^depth) as digit tuples
def addball(E, depth):
    E = list(E) + [0] * depth
    u = tuple((-E[i]) % P for i in range(depth))
    if u[0] == 1 and u[1] != 0: balls[depth].add(u)
for line in open(cen):
    m = re.match(r"s=(\d+) a=.* E=\[([0-9,]*)\]", line)
    if not m: continue
    s = int(m.group(1)); E = [int(x) for x in m.group(2).split(",")]
    d = (s + 1) // 2 + 1
    if d <= DMAX: addball(E, d)
for al in range(1, DMAX - 1):
    for (a1, b1, E) in CA.route_A4(P, al):
        addball(E, al + 2)
for c in (1, 2):
    surv = {(1, c)}
    print(f"c={c}")
    for n in range(3, DMAX + 1):
        forb = {u for u in balls[n] if u[1] == c}
        prof = [0, 0, 0, 0]; new = set()
        for v in surv:
            ch = [v + (x,) for x in range(P)]
            j = sum(1 for w in ch if w in forb); prof[j] += 1
            new.update(w for w in ch if w not in forb)
        print(f"  depth {n}: balls {len(forb):5d} (rel.mass {len(forb)/P**(n-2):.4f})  survivors {len(new):6d} "
              f"(frac {len(new)/P**(n-2):.4f}, ratio {len(new)/max(1,len(surv)):.3f})  parents by #forbidden children {prof}")
        surv = new
