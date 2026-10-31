"""Z0067 pass-1: Bradford–Ionascu Conj. 1.1 (arXiv:1405.4025): for n ∈ Z[i]∖{0,1,i,1+i} with Re n, Im n ≥ 0,
4/n = 1/a + 1/b + 1/c with each of a, b, c in the closed cone K = {Re, Im both ≥ 0} ∪ {Re, Im both ≤ 0}.
Search: a over K with |a| ≤ A·|n| (by increasing |a|), then 2-term m/N = 1/b + 1/c via Gaussian divisors d of N²:
(mb − N)(mc − N) = N², b = (N + d)/m, c = (N + N²/d)/m.
Usage: python z52b_p1_H00_gauss.py NORMMAX AFACTOR [q1]   (q1: closed first-quadrant cone only; real slice = ES)"""
import sys, json
from sympy import factorint
from math import isqrt
def mul(x, y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def nrm(x): return x[0]*x[0]+x[1]*x[1]
def divexact(x, y):  # x/y if exact Gaussian integer else None
    n = nrm(y); r = mul(x, (y[0], -y[1]))
    if r[0] % n or r[1] % n: return None
    return (r[0]//n, r[1]//n)
def incone(x): return (x[0] >= 0 and x[1] >= 0) or (x[0] <= 0 and x[1] <= 0)
_pi = {}
def gprime(p):  # π with norm p, p ≡ 1 (4)
    if p not in _pi:
        for a in range(1, isqrt(p)+1):
            b2 = p - a*a; b = isqrt(b2)
            if b*b == b2: _pi[p] = (a, b); break
    return _pi[p]
def gfactor(x):
    f = []; 
    for p, e in factorint(nrm(x)).items():
        if p == 2: f.append(((1, 1), e))
        elif p % 4 == 3: f.append(((p, 0), e//2))
        else:
            pi = gprime(p); pb = (pi[0], -pi[1]); y = x; k = 0
            while True:
                z = divexact(y, pi)
                if z is None: break
                y = z; k += 1
            f.append((pi, k)); f.append((pb, e-k))
    return [(q, e) for q, e in f if e]
def divisors(fac):
    ds = [(1, 0)]
    for q, e in fac:
        new = []
        for d in ds:
            t = d
            for _ in range(e+1): new.append(t); t = mul(t, q)
        ds = new
    out = []
    for d in ds:
        for u in ((1, 0), (0, 1), (-1, 0), (0, -1)): out.append(mul(d, u))
    return out
def solve(n, A):
    R = A*isqrt(nrm(n)) + 2
    cands = [(x, y) for x in range(-R, R+1) for y in range(-R, R+1) if (x, y) != (0, 0) and incone((x, y)) and x*x+y*y <= R*R]
    cands.sort(key=nrm)
    for a in cands:
        m = ((4*a[0]-n[0]), (4*a[1]-n[1])); N = mul(n, a)   # 4/n − 1/a = m/N
        if m == (0, 0): continue
        fac = gfactor(N); fac = [(q, 2*e) for q, e in fac]
        for d in divisors(fac):
            b = divexact((N[0]+d[0], N[1]+d[1]), m)
            if b is None or b == (0, 0) or not incone(b): continue
            e = divexact(mul(N, N), d); c = divexact((N[0]+e[0], N[1]+e[1]), m)
            if c is None or c == (0, 0) or not incone(c): continue
            return a, b, c
    return None
if __name__ == '__main__':
    NM, A = int(sys.argv[1]), int(sys.argv[2]); tag = ''
    if len(sys.argv) > 3 and sys.argv[3] == 'q1':
        incone = lambda x: x[0] >= 0 and x[1] >= 0; tag = 'Q1_'
    fails = []; cnt = 0
    for x in range(0, isqrt(NM)+1):
        for y in range(0, isqrt(NM)+1):
            if x*x+y*y > NM or (x, y) in ((0, 0), (1, 0), (0, 1), (1, 1)): continue
            cnt += 1; s = solve((x, y), A)
            if s is None: fails.append((x, y)); print('FAIL', (x, y), flush=True)
    print('checked', cnt, 'fails', len(fails))
    json.dump(dict(cone='Q1 closed' if tag else 'Q1 u Q3 closed', normmax=NM, A=A, checked=cnt, fails=fails), open(f'data/z52b/pass1/H00/gauss_{tag}{NM}_{A}.json', 'w'))
