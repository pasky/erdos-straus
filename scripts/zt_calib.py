"""zt_calib.py (O227): calibrate the random-remainder model of zt_lop against actual hits at polynomial points.

Input: output of `zt_ctl.sh BIN NMAX HMAX` (HIT lines and per-level 'N=.. done' lines with the model columns).
Groups points by lc(u) (+1 / -1) and by whether u = 1 + cT + 2T^2 (mod T^3) (already covered at level 2);
reports, per group and per level range, the number of points, actual hits (all / excluding 'structured' hits with
dep >= s-2, i.e. E = -u up to T^{s-2}) and the model expectation (case1 + case2).
usage: python zt_calib.py FILE [NMIN]
"""
import re
import sys
from collections import defaultdict

f = sys.argv[1]
NMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 3
lev = re.compile(r"u=(\S+) N=(\d+) done: hits this level (\d+) .*model: case1 (\S+) case2 (\S+) .*refined: case1 (\S+) case2 (\S+)")
hit = re.compile(r"u=(\S+) HIT \S+ s=(\d+) N=(\d+) .*?dep=(\d+)")
model = defaultdict(float)
modelr = defaultdict(float)
done = defaultdict(set)
hits = defaultdict(lambda: [0, 0])
for line in open(f):
    m = lev.search(line)
    if m:
        u, N = m[1], int(m[2])
        if N >= NMIN:
            model[u] += float(m[4]) + float(m[5])
            modelr[u] += float(m[6]) + float(m[7])
        done[u].add(N)
        continue
    m = hit.search(line)
    if m:
        u, s, N, dep = m[1], int(m[2]), int(m[3]), int(m[4])
        if N >= NMIN:
            hits[u][0] += 1
            if dep < s - 2:
                hits[u][1] += 1
nmax = max(max(v) for v in done.values())
groups = defaultdict(lambda: [0, 0, 0, 0.0, 0, 0.0])
for u, ns in done.items():
    if max(ns) < nmax:
        continue  # incomplete point
    co = list(map(int, u.split(",")))
    key = ("lc=+1" if co[-1] == 1 else "lc=-1", "u2=2" if len(co) > 2 and co[2] == 2 else "u2!=2", f"h={len(co)-1}")
    g = groups[key]
    g[0] += 1
    g[1] += hits[u][0]
    g[2] += hits[u][1]
    g[3] += model[u]
    g[4] += 1 if hits[u][1] > 0 else 0
    g[5] += modelr[u]
print(f"levels {NMIN}..{nmax}; complete points only")
print("group                      points  hits(all)  hits(unstructured)  points-with-unstructured-hit  model-expected  refined-model")
for key in sorted(groups):
    g = groups[key]
    print(f"{str(key):27s} {g[0]:6d} {g[1]:9d} {g[2]:12d} {g[4]:12d} {g[3]:16.3f} {g[5]:12.3f}")
tot = [round(sum(g[i] for g in groups.values()), 3) for i in range(6)]
print("TOTAL", tot)
