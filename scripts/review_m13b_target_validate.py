"""R95: validate review_m13b_target.c: for random II3/I3/I1 data from the reviewer's enumeration pickle
(e <= X), run the search at the point u_11=u_13=r (box residue) and check the datum is reported."""
import sys, pickle, random, subprocess, re
res = pickle.load(open(sys.argv[1], 'rb')); X = int(sys.argv[2]); n = int(sys.argv[3]); random.seed(4)
pool = [(f, P, MT, r) for N, (ns, D) in res.items() for f, P, (M, MT, rs) in D for r in rs
        if f in ('II3', 'I3', 'I1') and P[2] <= X]
print('pool', len(pool))
def tp(m):
    t = 1
    for q in (11, 13):
        while m % q == 0: m //= q; t *= q
    return t
ok = bad = 0
for f, P, MT, r in random.sample(pool, min(n, len(pool))):
    out = subprocess.run(['/tmp/r95/tgt', str(r), str(r), str(P[2])], capture_output=True, text=True).stdout
    found = set()
    for l in out.splitlines():
        m = re.match(r'HIT (\w+) \w=(\d+)\*(\d+) d=(\d+)\*(\d+) \w=(\d+)', l)
        if m: found.add((m[1], (int(m[2])*int(m[3]), int(m[4])*int(m[5]), int(m[6]))))
    if (f, P) in found: ok += 1
    else: bad += 1; print('MISSED', f, P, MT, r)
print('recovered', ok, 'missed', bad)
