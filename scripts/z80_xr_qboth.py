"""Opus cross-review of z80_qboth.c (both-large Q_K region, e>=E, f>=T).
usage: z80_xr_qboth.py r K [wfactor]
(1) Re-implements the author's per-(c,d) charge in exact integers (Python, independent code)
    and reproduces the qboth.txt line (wmax scan tested total).
(2) EXACT count: factor V=F^2+4w with GNU factor, enumerate every divisor f of V with
    f = -F mod u, T<=f<=F+2, and test the full Q equations. Asserts, per (c,d):
      2*exact <= charge,   every exact f <= the author's clipped ceiling h.
(3) With wfactor>1, scans c^2 d in (wmax, wfactor*wmax] and asserts no both-large solution
    exists there (empirical check of the w ceiling lemma)."""
import sys, subprocess, tempfile, os
from math import isqrt
r, K = int(sys.argv[1]), int(sys.argv[2]); wf = int(sys.argv[3]) if len(sys.argv) > 3 else 1
F = r**K
z = 1
while z**3 < F: z += 1
E = T = z*z
assert 2*T <= F
wmax = (F+T)**2 // (4*(E*T-1))
sq = {(x*x) % r for x in range(r)}
live_d = lambda d: ((-d) % r) not in sq          # -d nonzero nonsquare
pairs = [(c, d) for c in range(1, isqrt(wf*wmax)+1) if c % r for d in range(1, wf*wmax//(c*c)+1) if live_d(d)]
with tempfile.TemporaryDirectory(dir='data/z80') as td:
    fin = os.path.join(td, 'v'); fout = os.path.join(td, 'f')
    with open(fin, 'w') as fh:
        for c, d in pairs: fh.write(f'{F*F+4*c*c*d}\n')
    subprocess.run(['factor'], stdin=open(fin), stdout=open(fout, 'w'), check=True, timeout=1700)
    facs = open(fout).read().splitlines()
assert len(facs) == len(pairs)
def divisors(fl):
    ds = [1]
    pe = {}
    for p in fl: pe[p] = pe.get(p, 0)+1
    for p, a in pe.items(): ds = [x*p**i for x in ds for i in range(a+1)]
    return ds
def genuine(c, d, f):
    u = 4*c*d
    if (F+f) % u: return False
    a = (F+f)//u; Mq = 4*a*a*d+1
    if Mq % f: return False
    e = Mq//f
    if e < E or e % r == 0 or c*e < 2*a: return False
    b = c*e-a; assert 4*a*b*d == F*e+1 and a % r and b % r
    return True
scan = tested = total = exact = 0; beyond = 0; worst = 0
for (c, d), line in zip(pairs, facs):
    n, rest = line.split(':'); w = c*c*d; u = 4*c*d; V = F*F+4*w; assert int(n) == V
    fl = list(map(int, rest.split()))
    p = 1
    for q in fl: p *= q
    assert p == V
    ex = [f for f in divisors(fl) if T <= f <= F+2 and genuine(c, d, f)]
    if w > wmax:
        beyond += len(ex); continue
    exact += len(ex)
    # author's ceiling clipping (5 rounds, outward)
    h = F+2
    for _ in range(5):
        cut = ((F+h)**2//(4*w)+1)//E
        if cut >= h: break
        h = cut
    assert all(f <= h for f in ex), (c, d, ex, h)
    x = T+(u-(F+T) % u) % u
    if x > h:
        assert not ex; continue
    cnt = 1+(h-x)//u
    if cnt <= 256:
        scan += cnt; ch = 0
        for f in range(x, h+1, u):
            if V % f == 0:
                tested += 1
                if genuine(c, d, f): ch += 2
    else:
        cap = 1; g = 1; y = V
        for q in [2]+list(range(3, 252, 2)):
            if y % q: continue
            j = 1
            while True:
                if g <= u//q: g *= q
                else: j += 1
                y //= q
                if y % q: break
            cap *= j
        if y <= u//g: y = 1
        while y >= 252: y //= 252; cap *= 2
        ch = 2*min(cap, cnt)
    assert 2*len(ex) <= ch, (c, d, ex, ch)
    total += ch
print(r, K, E, T, wmax, scan, tested, total, flush=True)
print(f'# exact both-large solutions (one orientation)={exact} x2={2*exact} charge={total} pairs={len(pairs)} beyond_wmax_solutions={beyond} (scanned to {wf}*wmax)', flush=True)
