"""z78 cross-review (Opus): independent three-index search for P boxes at depth L
containing the point u=q/p (oriented a<=b with p a + q b = 0 mod W, W=r^L,
N=W^2/r).  Own code; J-mode uses a different reconstruction from the author's
(divisors e|B, then M | gcd(A, N+e)), Hd mode own candidate windows.

  python z78_xr_point.py search r L p q MODE Hlo Hhi   (theorem cutoff X)
  python z78_xr_point.py test                          (small-depth comparisons)
"""
import sys
from math import isqrt, gcd

def iroot4_up(n):
    x = isqrt(isqrt(n))
    while x**4 < n: x += 1
    return x

def Xcut(W):  # one of J, Hd, Ha <= X with J (Hd)^2 (Ha) < 0.28 W^2
    return iroot4_up(-(-28*W*W//100))

def mkcheck(r, W, N, p, q, hits, emax):
    def check(a, b, d):
        if a < 1 or b < a or d < 1: return
        e = 4*a*b*d - N
        if e < 1 or e > emax or (a+b) % e: return
        if (p*a+q*b) % W: return
        c = (a+b)//e
        if a % r and b % r and c % r and d % r:
            hits.add((a, b, c, d))
    return check

def mode_Ha(r, L, p, q, X, Hlo, Hhi, emax):
    W = r**L; N = W*W//r; hits = set(); chk = mkcheck(r, W, N, p, q, hits, emax)
    ip = pow(p, -1, q) if q > 1 else 0
    for H in range(Hlo, Hhi+1):
        V = W*H; a = (V*ip) % q if q > 1 else 0
        if a == 0: a = q
        amax = X//H
        while a <= amax:
            b = (V-p*a)//q
            if b < a: break
            s = 4*a*b; chk(a, b, N//s+1)
            a += q
    return hits

def mode_Hd(r, L, p, q, X, Hlo, Hhi, emax):
    # 4 d a (V - p a) = q (N+e), 1<=e<=emax.  Roots a = (dV +- sqrt(D(Y)))/(2dp), D(Y)=(dV)^2 - d p Y.
    W = r**L; N = W*W//r; hits = set(); chk = mkcheck(r, W, N, p, q, hits, emax)
    Ylo, Yhi = q*(N+1), q*(N+emax)
    for H in range(Hlo, Hhi+1):
        V = W*H
        for d in range(1, X//H+1):
            dV = d*V; D1 = dV*dV - d*p*Ylo
            if D1 < 0: continue
            D2 = dV*dV - d*p*Yhi
            s1 = isqrt(D1)+1            # >= sqrt(D1)
            s2 = isqrt(D2) if D2 > 0 else 0   # <= sqrt(D2)
            den = 2*d*p
            for lo, hi in ((dV-s1, dV-s2), (dV+s2, dV+s1)):
                for a in range(max(1, lo//den), hi//den+2):
                    t = V-p*a
                    if t <= 0 or t % q: continue
                    chk(a, t//q, d)
    return hits

def factor_block(vals, primes):
    rem = list(vals); fac = [[] for _ in vals]; n = len(vals)
    step = vals[1]-vals[0] if n > 1 else 1
    for t in primes:
        if t*t > vals[-1]: break
        # indices i with vals[0]+step*i = 0 mod t
        if step % t == 0:
            if vals[0] % t: continue
            idx = range(n)
        else:
            i0 = (-vals[0]*pow(step, -1, t)) % t; idx = range(i0, n, t)
        for i in idx:
            k = 0
            while rem[i] % t == 0: rem[i] //= t; k += 1
            if k: fac[i].append((t, k))
    for i in range(n):
        if rem[i] > 1: fac[i].append((rem[i], 1))
    return fac

def divisors(fl):
    ds = [1]
    for t, k in fl:
        ds = [x*t**j for x in ds for j in range(k+1)]
    return ds

def mode_J(r, L, p, q, X, Jlo, Jhi, emax):
    W = r**L; N = W*W//r; hits = set(); chk = mkcheck(r, W, N, p, q, hits, emax)
    w = W//r; j0 = Jlo + ((-q*w - Jlo) % 4)
    top = max(p, q)*w + Jhi + 8
    P = isqrt(top)+1; sv = bytearray([1])*(P+1); sv[0] = sv[1] = 0
    for i in range(2, isqrt(P)+1):
        if sv[i]: sv[i*i::i] = bytes(len(range(i*i, P+1, i)))
    primes = [i for i in range(2, P+1) if sv[i]]
    BL = 1 << 15
    for st in range(j0, Jhi+1, 4*BL):
        Js = list(range(st, min(Jhi, st+4*BL-1)+1, 4))
        if not Js: continue
        As = [q*w+J for J in Js]; Bs = [p*w+J for J in Js]
        fa = factor_block(As, primes) if len(As) > 1 else [factor_single(As[0], primes)]
        fb = factor_block(Bs, primes) if len(Bs) > 1 else [factor_single(Bs[0], primes)]
        for J, A, FA, FB in zip(Js, As, fa, fb):
            for e in divisors(FB):
                if e > emax or (N+e) % 4: continue
                g = gcd(A, N+e)
                if g % 4: continue
                # factor g from A's factor list
                fg = []
                for t, k in FA:
                    j = 0; gg = g
                    while j < k and gg % t == 0: gg //= t; j += 1
                    if j: fg.append((t, j))
                for M in divisors(fg):
                    if M % 4: continue
                    num = W*J - q*e
                    if num <= 0 or num % (p*M): continue
                    a = num//(p*M)
                    if M % (4*a): continue
                    chk(a, (N+e)//M, M//(4*a))
    return hits

def factor_single(v, primes):
    fl = []
    for t in primes:
        if t*t > v: break
        k = 0
        while v % t == 0: v //= t; k += 1
        if k: fl.append((t, k))
    if v > 1: fl.append((v, 1))
    return fl

MODES = {'Ha': mode_Ha, 'Hd': mode_Hd, 'J': mode_J}

def test():
    """Compare against complete own data dumps at r=17, K=5,7,9 (files from z78_xr_pdump)."""
    from pathlib import Path
    ntest = 0; nh = [0, 0, 0]; thm = 0
    for K in (5, 7, 9):
        L = (K+1)//2; W = 17**L; N = W*W//17; X0 = Xcut(W)
        D = [tuple(map(int, s.split()[:4])) for s in Path(f'data/z78/xreview/p17_K{K}.txt').read_text().splitlines()]
        pq = {(p, q) for p in range(1, 13) for q in range(1, 40)}
        for a, b, c, d in D:   # synthesize endpoints hit by actual data (both orientations)
            for x, y in ((a, b), (b, a)):
                for p in range(1, 31):
                    qq = (-p*x*pow(y, -1, W)) % W
                    if 0 < qq <= 3000: pq.add((p, qq))
        for p, q in sorted(pq):
                if gcd(p, q) > 1 or p == q: continue
                hit = [v for v in D if (p*v[0]+q*v[1]) % W == 0]
                for v in hit:   # size theorem where its hypotheses hold
                    a, b, c, d = v; e = (a+b)//c; H = (p*a+q*b)//W; M = 4*a*d; J = (p*M*a+q*e)//W
                    assert W*J == p*M*a+q*e and M*H == q*W//17+J
                    if p*q <= 5 and p+q <= 6:
                        assert J*(H*d)**2*(H*a)*100 < 28*W*W, (K, p, q, v)
                        assert min(J, H*d, H*a) <= X0 and e < W; thm += 1
                for i, m in enumerate(('Ha', 'Hd', 'J')):
                    Xt = 3000 if K < 9 else 1500
                    def key(v):
                        a, b, c, d = v; e = (a+b)//c; H = (p*a+q*b)//W; M = 4*a*d; J = (p*M*a+q*e)//W
                        return {'Ha': H*a, 'Hd': H*d, 'J': J}[m]
                    emax = W if m != 'Ha' else 10**60
                    want = {v for v in hit if key(v) <= Xt and (v[0]+v[1])//v[2] <= emax}
                    got = MODES[m](17, L, p, q, Xt, 1, Xt, emax)
                    assert got == want, (K, p, q, m, got ^ want)
                    ntest += 1; nh[i] += len(want)
    print('xr point tests', ntest, 'positive hits Ha/Hd/J', *nh, 'size-theorem hits checked', thm)

if __name__ == '__main__':
    if sys.argv[1] == 'test':
        test()
    else:
        r, L, p, q = map(int, sys.argv[2:6]); m = sys.argv[6]; lo, hi = int(sys.argv[7]), int(sys.argv[8])
        W = r**L; X = Xcut(W); hi = min(hi, X)
        assert W >= 1000 and p*q <= 5 and p+q <= 6 and p != q
        h = MODES[m](r, L, p, q, X, lo, hi, W)
        print('xr', r, L, p, q, m, 'X', X, 'range', lo, hi, 'hits', len(h), *sorted(h), flush=True)
