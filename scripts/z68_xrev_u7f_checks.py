#!/usr/bin/env python3
"""Independent arithmetic/screen audit; reads extracted lane files, never edits them.
Run: ulimit -v 6000000; timeout 1800 uv run --with sympy python \
 scripts/z68_xrev_u7f_checks.py /tmp/xrev_U7F
Census outputs independent_1e{7,8,9}.txt are produced by the companion C program.
Memory bounded: no Cartesian arrays; largest loop is a sieve of 1e6 integers.
"""
import gzip
import math
import re
import sys
from pathlib import Path
from fractions import Fraction
from sympy import divisors, factorint, isprime, primerange

root = Path(sys.argv[1])
Z7 = [105, 1465, 3865, 4545, 10305, 12145, 39361, 67425]

def witness(n, f):
    r = (-n) % f
    return r > 0 and (f + 1) % r == 0

def witnesses(n):
    return [f for f in range(7, 2*n+2, 8) if witness(n, f)]

def typ(n, f):
    r = (-n) % f
    z = (n+r)//f
    return (z if r & 1 else r) % 8

# Independently computed full lists, not merely aggregate counts.
for exponent in (7, 8, 9):
    own = (root / f'independent_1e{exponent}.txt').read_text()
    with gzip.open(root / f'data/z68/u7f/wit_1e{exponent}.txt.gz', 'rt') as stream:
        lane = stream.read()
    a = set(map(int, re.findall(r'^NOPRIME (\d+)', own, re.M)))
    b = set(map(int, re.findall(r'^NOPRIME p=(\d+)', lane, re.M)))
    assert a == b
    if exponent != 8:  # Archived 1e8 version predates types.
        a = set(re.findall(r'^ONETYPE (\d+) mask=(\d+)', own, re.M))
        b = set(re.findall(r'^ONETYPE p=(\d+) type=(\d+)', lane, re.M))
        assert a == b
    print(re.search(r'^N=.*$', own, re.M)[0], 'lists agree')

for n in (17, 2521, 21841, 66529, 225289):
    fs = witnesses(n)
    print('SPOT', n, 'all (f,r,omega,type)=',
          [(f, (-n)%f, len(factorint(f)), typ(n,f)) for f in fs],
          'prime witnesses=', [f for f in fs if isprime(f)],
          'y=1 witnesses=', [f for f in divisors(n+1) if f%8==7])
    assert fs and any(len(factorint(f)) <= 2 for f in fs)

# Both factorisation refinements genuinely differ from U^(8), even at primes.
for n in (17,2521):
    assert not any(((-n)%f)%8==0 or ((f+1)//((-n)%f))%8==0
                   for f in witnesses(n))
assert any(isprime(f) for f in witnesses(17))
assert witnesses(2521)==[87]
assert {2*a%7 for a in (3,5,6)}=={3,5,6}  # Contradicts literal §3.4 exclusivity.

# Exact small-shift equivalences: substitute back into xyz-x-z=n,
# rather than just checking the memo's two congruences.
def check_small(n):
    Ds = {}
    for r, m, modulus, target, allowed in (
        (1,(n+1)//2,4,3,({1},)),
        (2,n+2,8,5,({1,3},)),
        (4,n+4,8,3,({1,5},)),
    ):
        ds = divisors(m)
        D = any(d % modulus == target for d in ds)
        F = any(all(q % modulus in H for q in factorint(m)) for H in allowed)
        W = any((n+x+r) % (x*r) == 0 and (n+x+r) % 8 == 0
                for x in divisors(n+r))
        assert W == D == (not F), (n, r, W, D, F)
        Ds[f'outer{r}'] = D
    if n % 3 == 1:
        m = (n+3)//4
        D = any(d%3==2 for d in divisors(m))
        F = all(q%3==1 for q in factorint(m))
        W = any((n+x+3)%(3*x)==0 and (n+x+3)%8==0 for x in divisors(n+3))
        assert W == D == (not F)
        Ds['outer3'] = D
    for y, Hs in ((2,({1,3},)),(4,({1,5},)),(8,({1,3},{1,5}))):
        m = y*n+1
        ds = divisors(m)
        D = any(d%8==7 for d in ds)
        F = any(all(q%8 in H for q in factorint(m)) for H in Hs)
        W = False
        for d in ds:
            h = m//d
            if (d+1)%y or (h+1)%y:
                continue
            x,z = (d+1)//y,(h+1)//y
            if x*y%8==0:
                assert x*y*z-x-z == n
                W = True
        assert W == D == (not F)
        Ds[f'y{y}'] = D
    m = n+8
    D = any(d%8==7 for d in divisors(m))
    F = any(all(q%8 in H for q in factorint(m)) for H in ({1,3},{1,5}))
    W = any((n+8+z)%(8*z)==0 for z in divisors(n+8))
    assert W == D == (not F)
    Ds['outer8'] = D
    return Ds

count = 0
fails = []
for p in primerange(17, 1000001):
    if p%8 != 1:
        continue
    count += 1
    if not any(check_small(p).values()):
        fails.append(p)
assert count == 19552 and len(fails) == 43
for n in Z7:
    assert not any(check_small(n).values()) and not witnesses(n)
for m in range(1,102,2):
    assert not witnesses(m*m) and not any(check_small(m*m).values())
print('SMALLSHIFT', count, 'primes, 0 mismatches, all-fail=', len(fails),
      '; 8 Z7 zeros and 51 odd squares checked')

# The whole-class obstruction and smooth-part reduction.
classes = set()
for A in range(8):
    u,v,m = A*A+A-1,2*A+1,A*A+A+1
    assert u*u+v*v-1 == m*m
    for a,b in ((u,v),(v,u)):
        for s in (-1,1):
            for t in (-1,1):
                classes.add((s*a%8,t*b%8))
assert len(classes)==16
R,Y=4,5
M=1
for q in primerange(2,Y+1):
    power=q
    while power<=8*R*(R+1):
        power*=q
    M*=power
assert M==38880000
nprimes=0
for p in range(M+1,2000000000,M):
    if not isprime(p):
        continue
    nprimes+=1
    for r in range(1,R+1):
        smooth=math.prod(q**e for q,e in factorint(p+r).items() if q<=Y)
        Q=(p+r)//smooth
        assert smooth==r+1 and Q%math.lcm(8,r)==1
        for x in divisors(p+r):
            if (p+x+r)%(x*r) or (p+x+r)%8:
                continue
            g=math.prod(q**e for q,e in factorint(x).items() if q>Y)
            assert not isprime(Q) and 1<g<Q and Q%g==0 and (r+1)%(x//g)==0
assert nprimes==7
print('PROPOSITIONS 3.2:16/16 classes; 3.6:7 primes, no violations')

# CF identities, including a=1 and s=2, evaluated exactly.
def cf(terms):
    value = Fraction(terms[-1])
    for a in reversed(terms[:-1]):
        value = a + 1/value
    return value
ncf=0
for f in range(7,3000,8):
    for a in divisors(f+1):
        if a>=f:
            continue
        s=(f+1)//a
        for t in (1,2,7):
            n=f*t-a
            terms=([t-1,1,f-1] if a==1 else
                   [t-1,2,a-1] if s==2 else [t-1,1,s-2,1,a-1])
            assert cf(terms)==Fraction(n,f)
            ncf+=1
print('CF identities:', ncf, 'exact rational checks')

# All mandatory screens, including all 285 composites, not just the eight zeros.
for file in ('r8_zeros_1e10.txt','star_prime_zeros.txt','gstar_zeros.txt',
             'composite_zeros_le8e6.txt'):
    nums=[int(line.split()[0]) for line in (root/'data/z58/screens'/file).read_text().splitlines()
          if line and not line.startswith('#')]
    zeros=[]; no2=[]; maxf=0
    for n in nums:
        if n in Z7:
            assert not witnesses(n)
            zeros.append(n)
            continue
        f2=next((f for f in range(7,min(2*n+2,1000000),8)
                 if witness(n,f) and len(factorint(f))<=2),None)
        if f2 is None:
            # Distinguish an exhausted search from mere failure below the cap.
            assert 2*n+2 <= 1000000, (file,'increase search bound',n)
            fs=witnesses(n)
            assert fs and all(len(factorint(f))>2 for f in fs)
            no2.append(n)
            print('U7-POSITIVE BUT NO OMEGA2',n,'factorisation=',factorint(n),
                  'ALL witnesses=',[(f,(-n)%f,factorint(f)) for f in fs])
        else:
            maxf=max(maxf,f2)
            if file=='r8_zeros_1e10.txt':
                print('R8 CERTIFICATE',n,f2,(-n)%f2)
    print('SCREEN',file,'size=',len(nums),'U7 zeros=',zeros,
          'U7-positive omega2 failures=',no2,'max positive omega2 certificate f=',maxf)
    if file=='composite_zeros_le8e6.txt':
        assert sorted(zeros)==Z7 and no2==[196065]
    else:
        assert not zeros and not no2
# Independent fixed-n pair enumeration confirms the new composite boundary.
n=196065
pairs=[]
x=1
while 2*x*x<=n+2*x:
    for y in range(2,(n+2*x)//(x*x)+1):
        d=x*y-1
        if (n+x)%d:
            continue
        z=(n+x)//d
        if z>=x and (x*y*z)%8==0:
            pairs.append((x,y,z))
    x+=1
for x in range(2,math.isqrt(n+1)+2):
    if (n+1)%(x-1)==0:
        z=(n+1)//(x-1)+1
        if z>=x and (x*z)%8==0:
            pairs.append((x,1,z))
assert pairs==[(15,109,120)], pairs
print('196065 independent unordered words:',pairs)
print('ALL CHECKS PASSED')
