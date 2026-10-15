"""R247: reproduce the O227 §3 calibration hit counts with the R247 searcher: all 52 polynomial points of degree 2..4
(u(0)=1, u'(0)!=0), k = 2, levels 3..Nmax; hit is 'structured' iff v_T(E + u) >= s - 2.  usage: calib.py Nmax"""
import itertools, re, subprocess, sys
from collections import defaultdict
Nmax = int(sys.argv[1])
def mul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return [x % 3 for x in r]
def add(a, b):
    n = max(len(a), len(b)); return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % 3 for i in range(n)]
uns = defaultdict(list); st = defaultdict(list)
for h in (2, 3, 4):
    for mid in itertools.product(range(3), repeat=h - 1):
        if mid[0] == 0: continue
        for lc in (1, 2):
            u = [1] + list(mid) + [lc]
            out = subprocess.run(['timeout', '600', '/tmp/r247s', '2', ','.join(map(str, u)), '3', str(Nmax), 'lop'],
                                 capture_output=True, text=True, check=True).stdout
            for l in out.splitlines():
                if not l.startswith('HIT'): continue
                m = re.search(r"N=(\d+) s=(\d+) m'=(\d+) g'=(\d+) w1=(\d+)", l)
                N, s = int(m[1]), int(m[2]); f = lambda x: [int(c) for c in x]
                E = add(mul(mul(mul(f(m[4]), f(m[3])), [0, 1]), f(m[5])), [2])
                d = add(E, u); dep = next((i for i, x in enumerate(d) if x), 999)
                (st if dep >= s - 2 else uns)[N].append((''.join(map(str, u)), lc))
for lo in (3, 5, 6, 7):
    U = [x for N in range(lo, Nmax + 1) for x in uns[N]]
    S = [x for N in range(lo, Nmax + 1) for x in st[N]]
    print(f"levels {lo}..{Nmax}: unstructured hits {len(U)} at {len(set(U))} points; structured {len(S)} "
          f"(lc=-1: {sum(1 for x in S if x[1] == 2)}); unstructured at lc=+1: {sum(1 for x in U if x[1] == 1)}")
print('unstructured by level', {N: len(v) for N, v in sorted(uns.items())})
