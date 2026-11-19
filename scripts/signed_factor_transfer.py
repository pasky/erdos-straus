"""Replay SIGNED_FACTOR_TRANSFER.md. Python integers; run from repo root."""
from collections import Counter
from math import gcd
from pathlib import Path

from signed_two_shifts import (case11, divisors_sq, eligibility, factors, hits,
                               prime, slots)


def certified(p, c, a, b, d):
    assert min(a, b, d, c) > 0 and gcd(a, b) == 1
    e, r = divmod(a+b, c)
    assert r == 0 and p+c == 4*a*b*d
    x, y, z = a*b*d, p*a*d*e, p*b*d*e
    assert x % p and 4*x*y*z == p*(x*y+x*z+y*z)
    return (a, b, d, e), (x, y, z)


def witness(p, c):
    assert c > 0 and c % 4 == 3 and p % 4 == 1
    if 3*c > p+4:
        return None
    k = (p+c)//4
    for t in divisors_sq(factors(k)):
        if t <= k and (k+t) % c == 0:
            g = gcd(k, t)
            a, b = t//g, k//g
            return certified(p, c, a, b, k//(a*b))
    return None


def factor_menu(f, h):
    # New shifts only; f=h impossible since gcd(f,h)=1 and f is prime.
    out = set()
    for n in (4*f-1, 4*f+1, abs(f-h), f+h):
        out.update(c for c in divisors_sq(factors(n)) if c % 4 == 3 and n % c == 0)
    return out - {11}


def obstruction23(q):
    """Only called for 23 eligible. Reserve 3 and one 2 in K=3(Q+1)."""
    nontrivial = [u % 23 for u, e in factors((q+1)//2) for _ in range(e) if u % 23 != 1]
    return nontrivial in ([5], [14])


def dual_obstruction23(q):
    m = 23*((q+1)//2)-22
    assert 6*m == (23*(12*q-11)+1)//4
    residues = sorted(u % 23 for u, e in factors(m) for _ in range(e) if u % 23 != 1)
    return all(pow(u,11,23) == 1 for u in residues) or residues == [5,14]


def split(p):
    q = (p+11)//12
    fs = [u for u, e in factors(q) for _ in range(e) if u % 11 != 1]
    assert len(fs) == 1 and fs[0] % 11 == p % 11
    return fs[0], q//fs[0]


def plus_one(p, f, h):
    c = 12*h+11
    if (f+1) % 12 or (f-98) % c:
        return False
    a, b = (f+1)//12, 9*h
    assert gcd(4*a, c) == 1 and ((4*a)**2+p) % c == 0
    g = gcd(a, b)
    certified(p, c, a//g, b//g, 4*g*g)
    return True


def survey():
    counts = Counter()
    for p in range(841, 10_000_001, 840):
        if not prime(p):
            continue
        counts['all'] += 1
        elig = eligibility(p,23)[1]
        if elig:
            q = (p+11)//12
            direct = not obstruction23(q)
            assert bool(witness(p,23)) == direct
            assert hits(p,23) == (direct, not dual_obstruction23(q))
        if p % 11 not in (2, 6) or case11(p)[0]:
            continue
        f, h = split(p)
        joint = not case11(p)[1]
        assert hits(p, 11) == (False, not joint)
        c = 12*h+11
        menu = [s for s in factor_menu(f,h) if witness(p,s)]
        w23 = bool(witness(p,23))
        keep_f = (4*f < 33*h+11 and any(witness(p,11+4*f*j) for j in range(1,h)))
        keep_h = (h>1 and any(witness(p,11+4*h*j) for j in range(1,f)))
        values = {'inputs': True, 'h>1': h>1, 'large f excluded': 4*f>=33*h+11,
                  'retain f in K': keep_f, 'retain nontrivial h in K': keep_h,
                  'retain either': keep_f or keep_h,
                  '23 eligible': elig, '23 eligible II': elig and w23,
                  'factor menu II': bool(menu),
                  'factor menu root II': any(eligibility(p,s)[1] for s in menu),
                  '12h+11 II, h>1': h>1 and bool(witness(p,c)),
                  '12h+11 root II, h>1': h>1 and eligibility(p,c)[1] and bool(witness(p,c)),
                  '12h+11 lemma, h>1': plus_one(p,f,h) and h>1}
        for name, value in values.items():
            if value:
                counts[name, 'direct'] += 1
                counts[name, 'joint'] += joint
    assert (counts['all'], counts['inputs','direct'], counts['inputs','joint']) == (3426,244,158)
    for name in values:
        print(name, counts[name,'direct'], counts[name,'joint'])


def examples():
    for p in (2521,12601):
        f,h = split(p)
        assert h == 1 and not any(hits(p,11))
        triples = slots(p)
        assert not any(x % f == 0 for row in triples for x in row)
        cert,row = witness(p,23)
        assert tuple(sorted(row)) in triples and eligibility(p,23)[1]
        print('23:', p, cert, row, 'all sorted triples:', len(triples))
    for p,c in [(76441,127),(206641,79),(2044561,815)]:
        f,h = split(p)
        assert case11(p) == (False,False) and eligibility(p,c)[1]
        if p == 76441:
            assert c == (f-h)//2 and c in factor_menu(f,h)
            assert all(not witness(p,11+4*w*j) for w,v in [(f,h),(h,f)] for j in range(v))
        elif p == 206641:
            assert c == 4*f+11
        else:
            assert plus_one(p,f,h)
        print('variable:', p, f,h,c,witness(p,c))
    assert case11(9565921) == (False,False) and eligibility(9565921,23)[1]
    assert hits(9565921,23) == (False,False)
    p = 1711921
    f,h = split(p)
    assert case11(p) == (False,False) and not witness(p,12*h+11)
    assert not any(any(hits(p,s)) for s in factor_menu(f,h))
    assert all(not witness(p,11+4*w*j) for w,v in [(f,h),(h,f)] for j in range(v))
    print('negative menu:', p, sorted(factor_menu(f,h)))
    qr = {i*i % 23 for i in range(1,23)}
    for v, missing in [(1,{9,18}), (2,set())]:
        box = {pow(2,i,23)*pow(3,j,23)%23 for i in range(-v,v+1) for j in (-1,0,1)}
        assert box == qr - missing


def screens():
    base = Path(__file__).resolve().parents[1]/'data/z58/screens'
    groups = {'odd squares': [(2*i+1)**2 for i in range(1,51)]}
    for path in sorted(base.glob('*.txt')):
        groups[path.stem] = [int(s.split()[0]) for s in path.read_text().splitlines()
                             if s.strip() and not s.startswith('#')]
    for label, ns in groups.items():
        domain = [p for p in ns if p % 840 == 1 and p % 11 in (2,6) and prime(p) and not case11(p)[0]]
        print(label, 'in transfer domain:', domain, 'out of', len(ns))


if __name__ == '__main__':
    examples()
    survey()
    screens()
