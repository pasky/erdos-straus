"""R247: brute-force census coverings vs review_r247_search (lop mode) at all 54 polynomial points (deg 1..4,
u(0)=1, u'(0)!=0), k = 2 levels 3..8 and k = 3 levels 4..8 (census complete for s <= 16).
Census tuples that are exact (w1 = -u C1) are reported separately (lop mode is allowed to miss them)."""
import itertools, re, subprocess, sys
cov = {}
for l in open(sys.argv[1]):
    k, u, N, s, m, g, w, C = l.split()
    cov.setdefault((int(k), u), set()).add((int(N), int(s), m, g, w, C))
def pts():
    for h in range(1, 5):
        for mid in itertools.product(range(3), repeat=h - 1):
            for lc in (1, 2):
                co = (1,) + mid + (lc,)
                if co[1] != 0: yield ''.join(map(str, co))
tot = bad = 0; nexact = 0
for k, N1 in ((2, 3), (3, 4)):
    for u in pts():
        out = subprocess.run(['timeout', '600', '/tmp/r247s', str(k), ','.join(u), str(N1), '8', 'lop'],
                             capture_output=True, text=True, check=True).stdout
        S = set()
        for l in out.splitlines():
            if l.startswith('HIT'):
                m = re.search(r"N=(\d+) s=(\d+) m'=(\d+) g'=(\d+) w1=(\d+) C1=(\d+)", l)
                S.add((int(m[1]), int(m[2]), m[3], m[4], m[5], m[6]))
        Cn = {x for x in cov.get((k, u), set()) if x[0] >= N1}
        # exact census tuples: w1 = -u*C1  -> recompute
        def isexact(x):
            w = [int(c) for c in x[4]]; C = [int(c) for c in x[5]]; uu = [int(c) for c in u]
            r = [0] * (len(C) + len(uu) + len(w))
            for i, a in enumerate(C):
                for j, b in enumerate(uu): r[i + j] += a * b
            for i, a in enumerate(w): r[i] += a
            return all(v % 3 == 0 for v in r)
        ex = {x for x in Cn if isexact(x)}
        nexact += len(ex)
        tot += len(Cn)
        if (Cn - ex) - S or S - Cn:
            bad += 1; print('MISMATCH k', k, 'u', u, 'census-only', (Cn - ex) - S, 'search-only', S - Cn)
print('census covering records', tot, 'of which exact', nexact, 'mismatching (k,u)', bad)
