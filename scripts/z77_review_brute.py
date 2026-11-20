"""Opus review (z77): brute-force checks of the K=3 ingredients of R17_F3 at small r.
All P-data (a<=b, in-cell r-free) of N=r^3 by e-enumeration; compares with p3.txt and the lemmas."""
from math import isqrt, gcd
from pathlib import Path
import sys

def spf_sieve(n):
    s = list(range(n+1))
    for p in range(2, isqrt(n)+1):
        if s[p] == p:
            for q in range(p*p, n+1, p):
                if s[q] == q: s[q] = p
    return s

def factor(m, spf):
    f = {}
    while m > 1:
        p = spf[m]; f[p] = f.get(p, 0) + 1; m //= p
    return f

def divisors(f):
    ds = [1]
    for p, k in f.items():
        ds = [d * p**i for d in ds for i in range(k+1)]
    return ds

def tau(f):
    t = 1
    for k in f.values(): t *= k+1
    return t

def p3cost(M, e, r, f):
    # replicate z77_p3.c semantics: primes <= r greedily into g; residual x.
    g = 1; cost = 1; x = 1
    for p in sorted(f):
        k = f[p]
        if p > r:
            x *= p**k; continue
        j = 0
        for _ in range(k):
            if g <= e // p: g *= p
            else: j += 1
        cost *= 2*j+1
    if x <= e // g: g *= x; x = 1
    mult = 1 if x == 1 else (3 if x < (r+1)**2 else 9)
    return cost * mult * (1 if g <= e // g else 2)

def run(r, p3row):
    N = r**3; W = r*r
    emax = N  # e <= a+b <= 2b, and 4abd = N+e => e < N for N>1
    Mmax = (N + emax)//4
    spf = spf_sieve(Mmax+1)
    sq = {(h*h) % r for h in range(1, r)}
    cum = 0; per_j = [0]*6; allcent = set(); viol = []
    for e in range(1, emax+1):
        if (N + e) % 4: continue
        M = (N+e)//4
        f = factor(M, spf)
        cents = set(); data = 0
        ds = divisors(f)
        for a in ds:
            if a % r == 0: continue
            Ma = M // a
            for b in divisors(factor(Ma, spf)) if Ma > 1 else [1]:
                if b < a or b % r == 0: continue
                d = Ma // b
                if d % r == 0: continue
                if (a + b) % e: continue
                c = (a+b)//e
                if c % r == 0: continue
                data += 1
                # oriented centres -a/b and -b/a mod W
                x = (-a * pow(b, -1, W)) % W; y = (-b * pow(a, -1, W)) % W
                cents.add(x); cents.add(y)
                # integer-centre cap check: acd <= (N/e+1)/2 and centre == 1-4acd
                assert 2*a*c*d*e <= N + e
                assert x == (1 - 4*a*c*d) % W
                # small-side lemma: check per-e afterwards
        # PL compression / p3 cost per e
        if e < 32*r:
            cst = p3cost(M, e, r, f)
            if len(cents) > cst: viol.append(('p3', e, len(cents), cst))
            cum += len(cents)
            for j in range(6):
                if e < r << j: per_j[j] = cum
        # small-side lemma for any t <= e (take t = largest power of two <= e)
        t = 1 << (e.bit_length()-1)
        if data and 2*data > 2*tau(f)*(1 + 2*(-(-isqrt(M//t)//t))): viol.append(('small', e, data))
        if t**3 >= M and 2*data > 4*tau(f): viol.append(('cube', e, data))
        allcent |= {x for x in cents if x % r not in sq}
    ok3 = all(per_j[j] <= p3row[j] for j in range(6))
    # total nonsquare-cell boxes vs combine's K=3 p3 bound (min over j)
    caps = []
    for j, s in enumerate(p3row):
        E = r << j; T = (N//E + 1)//2; full, rem = divmod(T, r)
        caps.append(s + 2*(full*((r-1)//2) + min(rem, (r-1)//2)))
    return dict(r=r, viol=viol[:5], nviol=len(viol), cum=per_j, p3=p3row, ok3=ok3,
                nonsq_boxes=len(allcent), cap=min(caps))

if __name__ == '__main__':
    p3 = {int(l.split()[0]): list(map(int, l.split()[1:])) for l in Path('data/z77/p3.txt').read_text().splitlines()}
    for r in map(int, sys.argv[1:]):
        print(run(r, p3[r]), flush=True)
