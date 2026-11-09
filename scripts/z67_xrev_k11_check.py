"""Independent ET 1.9 checks and unbounded-modulus pi0 search.
Run under ulimit -v 6000000 and timeout; uv run --with cypari2 --with sympy.
check ROOT verifies archived slice certificates and a small exact shadow.
search X exhausts all seven families for parameter pair product <= X:
(a,d) for I1/II2/II3, (a,b) for I4/II1, (a,c) for I2, (c,d) for I3.
The remaining parameter is unrestricted, enumerated by necessary divisibility.
No dense arrays or persistent divisor caches are used.
"""
import ast
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, lcm
from pathlib import Path
import re
import sys


def split(n):
    s = 1
    for p in (11, 13):
        while n % p == 0:
            n //= p
            s *= p
    return s, n


def value(m):
    s, t = split(m)
    return (1 + t * pow(t, -1, s)) % m if s > 1 else 1 % m


def family_ok(fam, p, m, r):
    a, b, c, d, e, f = (p.get(k) for k in 'abcdef')
    if fam == 'I1':
        return m == 4*a*d and (r+f) % m == 0 and (4*a*a*d+1) % f == 0
    if fam == 'I2':
        return m == 4*a*c*f and gcd(4*a*c, f) == 1 and (r+f) % (4*a*c) == 0 and (r*a+c) % f == 0
    if fam == 'I3':
        return m == 4*c*d*f and gcd(4*c*d, f) == 1 and (r+f) % (4*c*d) == 0 and (r*r+4*c*c*d) % f == 0 and r % f == p['x'] % f
    if fam in ('I4', 'II1'):
        return m == 4*a*b and gcd(e, m) == 1 and (a+b) % e == 0 and ((r*e+1) if fam == 'I4' else (r+e)) % m == 0
    if fam == 'II2':
        return m == f and (f+1) % (4*a*d) == 0 and (r+4*a*a*d) % f == 0
    if fam == 'II3':
        return m == 4*a*d*e and gcd(4*a*d, e) == 1 and (r+4*a*a*d+e) % m == 0
    raise ValueError(fam)


def check(root):
    from sympy import divisors, sqrt_mod
    certs = sorted((root/'data/z67/k11/slice_certs').glob('*.txt'))
    entries = 0
    q7 = []
    for path in certs:
        lines = path.read_text().splitlines()
        h = re.fullmatch(r'# slice q1=(\S+) T=(\(.+\)) LEVEL=(\d+) box residues (\d+)', lines[0])
        q, T, level, count = Fraction(h[1]), ast.literal_eval(h[2]), int(h[3]), int(h[4])
        if 11 not in T:
            assert pow(q.numerator * pow(q.denominator, -1, 11) % 11, 5, 11) == 10
            q7.append(q)
        for v in (abs(q.numerator), q.denominator):
            for p in T:
                while v % p == 0:
                    v //= p
            assert v == 1
        cylinders = []
        for line in lines[1:]:
            left, right = line.split('|')
            fam = left.split()[0]
            pars = {k:int(v) for k,v in re.findall(r'(\w+)=(\d+)', left)}
            m, r = map(int, right.split())
            assert gcd(m, r) == 1 and family_ok(fam, pars, m, r), line
            mo = m
            for p in T:
                while mo % p == 0:
                    mo //= p
            mt = m//mo
            assert (r*q.denominator-q.numerator) % mo == 0
            assert level % mt == 0
            cylinders.append((mt, r % mt))
            entries += 1
        seen = 0
        for x in range(1, level, gcd(level, 840)):
            if gcd(x, level) != 1 or (11 in T and pow(x % 11, 5, 11) != 10):
                continue
            seen += 1
            assert any(x % m == r for m,r in cylinders), (path, x)
        assert seen == count
        print('certificate', path.name, 'OK', seen, flush=True)
    assert len(q7) == len(set(q7)) == 21
    print('CERTIFICATES', len(certs), 'entries', entries, 'nonempty T7 slices', len(q7), flush=True)

    # Independent full class list at a small modulus, using SymPy roots rather than PARI/Hensel.
    Q = 120120
    ds = list(map(int, divisors(Q)))
    actual = set()
    def add(m, r):
        r %= m
        if gcd(r,m) == 1 and r % gcd(m,840) == 1 % gcd(m,840) and (m % 11 or pow(r % 11,5,11) == 10):
            actual.add((m,r))
    for m in ds:
        if m % 4 == 0:
            for a0 in divisors(m//4):
                a = int(a0)
                d = m//(4*a)
                for f in divisors(4*a*a*d+1):
                    add(m,-int(f))
                for e0 in divisors(a+d):
                    e = int(e0)
                    if gcd(e,m) == 1:
                        add(m,-e)
                        add(m,-pow(e,-1,m))
                for f in ds:
                    if Q % (m*f) or gcd(m,f) != 1:
                        continue
                    targets = {(-d*pow(a,-1,f)) % f} if f > 1 else {0}
                    targets.update(map(int,sqrt_mod(-4*a*a*d,f,all_roots=True)))
                    for z in targets:
                        r = -f + m*((z+f)*pow(m,-1,f) % f) if f > 1 else -1
                        add(m*f,r)
            for e in ds:
                if m % (4*e) or gcd(m//e,e) != 1:
                    continue
                for a0 in divisors(m//(4*e)):
                    a = int(a0)
                    add(m,-4*a*a*(m//(4*e*a))-e)
        if (m+1) % 4 == 0:
            for a0 in divisors((m+1)//4):
                a = int(a0)
                for d0 in divisors((m+1)//(4*a)):
                    add(m,-4*a*a*int(d0))
    sys.path.insert(0,str(root/'scripts'))
    from z67_k11_classes import classes_dividing
    expected = {(m,r) for m,rs in classes_dividing({2:3,3:1,5:1,7:1,11:1,13:1}).items() for r in rs}
    assert actual == expected, (actual-expected,expected-actual)
    for level in (9240,120120):
        xs = [x for x in range(1,level,840) if gcd(x,level) == 1 and pow(x % 11,5,11) == 10]
        alive = [x for x in xs if not any(level % m == 0 and x % m == r for m,r in actual)]
        print('SHADOW',level,len(alive),'/',len(xs),'residues',alive,flush=True)
    assert family_ok('II3',{'a':11,'d':2,'e':247},21736,-1215)
    assert (-1215-1) % (21736//143) == 0 and -1215 % 11 == 6 and -1215 % 13 == 7
    S = classes_dividing({2:3,11:1,13:1,19:1})
    assert -1215 % 21736 in S[21736]
    assert family_ok('I3',{'c':2,'d':19,'f':55,'x':46},8360,6481)
    assert 6481 % 40 == 1 and 6481 % 209 == 2
    print('KNOWN CLASSES -1215 mod 21736 and 6481 mod 8360 OK',flush=True)
    # New counterexample, checked directly against ET rather than search equations.
    assert 11999 == 13**2 * 71 and gcd(4*8*33,11999) == 1
    assert family_ok('II3',{'a':8,'d':33,'e':11999},12670944,-20447)
    assert -20447 % 11 == 2 and -20447 % 169 == 2 and -20447 % 6816 == 1
    assert value(12670944) == -20447 % 12670944
    assert family_ok('I2',{'a':125,'c':88,'f':11999},527956000,426568001)
    assert value(527956000) == 426568001
    print('PI0 REFUTED: II3 -20447 mod 12670944; I2 426568001 mod 527956000',flush=True)


def search(X):
    import cypari2
    pari = cypari2.Pari()
    counts, hits = Counter(), Counter()
    pairs = 0
    def hit(fam, a, d, z, m, r):
        assert r % m == value(m)
        hits[fam] += 1
        print('HIT',fam,a,d,z,'class',r % m,m,flush=True)
    def divs(n):
        return [int(v) for v in pari.divisors(n)]
    for a in range(1,X+1):
        for d in range(1,X//a+1):
            pairs += 1
            base = 4*a*d
            A = a*base
            t = value(base)
            sb, _ = split(base)
            n2,_ = split(A+2)
            n4,_ = split(A+4)
            # I1 and the I3/II2/II3 off-S divisor constraints share A+1.
            full = divs(A+1) if sb > 1 or n2 > 1 or n4 > 1 else []
            free = [f for f in full if gcd(f,143) == 1]
            if sb > 1:
                for f in full:
                    counts['I1'] += 1
                    if (f+t) % base == 0:
                        hit('I1',a,d,f,base,-f)
            for n, fam in ((n2,'II3'),(n4,'I3')):
                for s in divs(n):
                    for fp in free:
                        f = s*fp
                        counts[fam] += 1
                        if (f+t) % base == 0 and gcd(base,f) == 1:
                            if fam == 'II3':
                                hit(fam,a,d,f,base*f,-A-f)
                            else:
                                r = value(base*f)
                                assert (r*r+A) % f == 0
                                hit(fam,a,d,f,base*f,r)
            for s in divs(n2):
                for fp in free:
                    f = s*fp
                    counts['II2'] += 1
                    if (f+1) % base == 0:
                        hit('II2',a,d,f,f,-A)
            sums = divs(a+d)
            if sb > 1:
                for e in sums:
                    if gcd(e,base) != 1:
                        continue
                    counts['I4'] += 1
                    counts['II1'] += 1
                    if (e*t+1) % base == 0:
                        hit('I4',a,d,e,base,-pow(e,-1,base))
                    if (e+t) % base == 0:
                        hit('II1',a,d,e,base,-e)
            ns,_ = split(2*a+d)
            for s in divs(ns):
                for fp in sums:
                    if gcd(fp,143) != 1:
                        continue
                    f = s*fp
                    counts['I2'] += 1
                    if (f+t) % base == 0 and gcd(base,f) == 1:
                        r = value(base*f)
                        assert (r*a+d) % f == 0
                        hit('I2',a,d,f,base*f,r)
        if a % 10000 == 0:
            print('progress',a,'pairs',pairs,'hits',dict(hits),flush=True)
    print('SEARCH COMPLETE X',X,'pairs',pairs,'candidate counts',dict(counts),'hits',dict(hits),flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'check':
        check(Path(sys.argv[2]))
    elif sys.argv[1] == 'search':
        search(int(sys.argv[2]))
    else:
        raise SystemExit('check ROOT | search X')
