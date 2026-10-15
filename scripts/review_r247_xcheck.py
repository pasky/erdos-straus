"""R247: cross-check (i) full search (no Liouville input) vs lop search (Lemma 1.2 + Prop 2.1-type degree bounds,
own enumeration) and (ii) both vs the author's zt_lop, at all polynomial points u (u(0)=1, u'(0)!=0, deg 1..4).
usage: review_r247_xcheck.py k Nmin Nmax_full Nmax_lop  (binaries /tmp/r247s, /tmp/zt_lop)"""
import itertools, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

k, Nmin, Nfull, Nlop = map(int, sys.argv[1:5])

def pts():
    for h in range(1, 5):
        for mid in itertools.product(range(3), repeat=h - 1):
            for lc in (1, 2):
                co = (1,) + mid + (lc,) if h >= 1 else (1,)
                if h >= 2 and co[1] == 0: continue
                yield co

def mine(u, N1, N2, mode):
    out = subprocess.run(['timeout', '3000', '/tmp/r247s', str(k), ','.join(map(str, u)), str(N1), str(N2), mode],
                         capture_output=True, text=True, check=True).stdout
    S = set()
    for l in out.splitlines():
        if l.startswith('HIT'):
            m = re.search(r"N=(\d+) s=(\d+) m'=(\d+) g'=(\d+) w1=(\d+) C1=(\d+)", l)
            S.add((int(m[1]), int(m[2]), m[3], m[4], m[5], m[6], 'EXACT' in l))
    return S

def author(u, N1, N2):
    out = subprocess.run(['timeout', '3000', '/tmp/zt_lop', '3', str(k), str(N1), str(N2), ','.join(map(str, u))],
                         capture_output=True, text=True, check=True).stdout
    S = set()
    for l in out.splitlines():
        if l.startswith('HIT'):
            m = re.search(r"s=(\d+) N=(\d+) .*m'=\[([\d,]*)\] g'=\[([\d,]*)\] w1=\[([\d,]*)\] C1=\[([\d,]*)\]", l)
            f = lambda x: x.replace(',', '')
            S.add((int(m[2]), int(m[1]), f(m[3]), f(m[4]), f(m[5]), f(m[6])))
    return S

def job(u):
    F = mine(u, Nmin, Nfull, 'full')
    L = mine(u, Nmin, Nlop, 'lop')
    A = author(u, Nmin, Nlop)
    Fne = {x for x in F if not x[6]}
    Lr = {x[:6] for x in L if x[0] <= Nfull}
    bad = []
    if {x[:6] for x in Fne} - Lr: bad.append(('full-nonexact not in lop', {x[:6] for x in Fne} - Lr))
    if Lr - {x[:6] for x in F}: bad.append(('lop not in full', Lr - {x[:6] for x in F}))
    La = {x[:6] for x in L}
    if La != A: bad.append(('mine-lop != zt_lop', La ^ A))
    return u, len(F), len([x for x in F if x[6]]), len(L), len(A), bad

with ThreadPoolExecutor(2) as ex:
    tot = [0, 0, 0, 0]; nbad = 0
    for u, nf, ne, nl, na, bad in ex.map(job, list(pts())):
        tot[0] += nf; tot[1] += ne; tot[2] += nl; tot[3] += na
        if bad: nbad += 1; print('MISMATCH', u, bad, flush=True)
        elif nf or nl: print('ok', u, 'full', nf, 'exact', ne, 'lop', nl, 'zt_lop', na, flush=True)
    print('points', len(list(pts())), 'totals full/exact/lop/zt_lop', tot, 'mismatching points', nbad)
