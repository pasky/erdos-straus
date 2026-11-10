"""Independent numerical audit. Standard library only; run with uv run python.
Usage: checks.py /tmp/xrev_IDEAA (archive lane scripts/data there first).
Census output must be root/census.txt from z69_xrev_ideaa_census.cpp.
No arrays beyond a 3 MB sieve; no Cartesian-product allocations.
"""
import math
import random
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
data = root / 'data/z69/ideaa'

def load(name):
    text = (data / name).read_text()
    n = int(re.search(r'primes=(\d+)', text)[1])
    rows = {int(w[1]): list(map(int, w[2:])) for line in text.splitlines()
            if (w := line.split()) and w[0] == 'S'}
    return n, rows

nb, both = load('kcost_1e10_both.txt')
ni, one = load('kcost_1e10_typeI.txt')
nii, two = load('kcost_1e10_typeII.txt')
assert nb == ni == nii == 56876600
matches = 0
for line in (root / 'census.txt').read_text().splitlines():
    if not line.startswith('S '):
        continue
    _, q, b, i, ii = map(lambda x: int(x) if x != 'S' else x, line.split())
    for table, got in [(both, b), (one, i), (two, ii)]:
        if q in table:
            assert got == sum(table[q][1:6]), (q, got, table[q])
            matches += 1
print('Census agrees with all', matches, 'available cumulative <=1e8 survival cells')
for q in (5, 21, 68, 108, 421, 1031, 3152):
    pb, pi, pii = both[q][0]/nb, one[q][0]/nb, two[q][0]/nb
    print('DEP', q, 'ratio', pb/(pi*pii), 'theta', math.log(pb)/math.log(pii))

N = 3_000_000
sieve = bytearray(b'\1')*(N+1)
sieve[:2] = b'\0\0'
for q in range(2, math.isqrt(N)+1):
    if sieve[q]:
        sieve[q*q::q] = b'\0'*((N-q*q)//q+1)
small = [q for q in range(2, math.isqrt(N)+1) if sieve[q]]
ps = [p for p in range(1009, N+1, 24) if sieve[p]]
sample = random.Random(69).sample(ps, 20000)

def divisors_square(n, power=2):
    ds = [1]
    for q in small:
        if q*q > n:
            break
        k = 0
        while n % q == 0:
            n //= q
            k += 1
        if k:
            ds = [d*q**j for d in ds for j in range(power*k+1)]
    if n > 1:
        ds = [d*n**j for d in ds for j in range(power+1)]
    return ds

def hit(p, e):
    m = (p+e)//4
    assert (p+e)%4 == 0 and math.gcd(m, e) == 1
    for f in divisors_square(m):
        g = m*m//f
        if (f+m)%e == 0 and (g+m)%e == 0:
            x, y = (f+m)//e, (g+m)//e
            assert e*x*y == m*(x+y)
            return 1
    return 0

rows = []
for p in sample:
    # Independent of Cornacchia: enumerate the unique positive odd coordinate.
    for a in range(1, math.isqrt(p)+1, 2):
        b = math.isqrt(p-a*a)
        if a*a+b*b == p:
            break
    else:
        raise AssertionError(p)
    e = 2*a+1
    g = hit(p,e)
    controls = [e+4*k for k in (-3,-2,-1,1,2,3) if e+4*k>=3]
    c = sum(hit(p,t) for t in controls)
    rows.append((g,c,len(controls)))
ng = len(rows)
g = sum(r[0] for r in rows)
c = sum(r[1] for r in rows)
nc = sum(r[2] for r in rows)
assert (g,ng,c,nc) == (1015,20000,4176,119826)
rg, rc = g/ng, c/nc
ratio = rg/rc
# Cluster delta-method uncertainty for the ratio, retaining all six controls per prime.
mg, mc, mn = g/ng, c/ng, nc/ng
influences = [ratio*((x-mg)/mg+(z-mn)/mn-(y-mc)/mc) for x,y,z in rows]
se = math.sqrt(sum(v*v for v in influences)/(ng*(ng-1)))
print('T3', g, ng, c, nc, 'ratio', ratio, 'iid-cluster SE', se,
      'approx 95% CI', (ratio-1.96*se,ratio+1.96*se))
fpc_se = se*math.sqrt((len(ps)-ng)/len(ps))
print('T3 finite population',len(ps),'FPC SE',fpc_se,
      'approx 95% CI',(ratio-1.96*fpc_se,ratio+1.96*fpc_se))
assert 3**2-2*93**2 == -17289 and 17289 == 3**2*17*113
assert all(d%8 != 7 for d in range(1,17290) if 17289%d == 0)
assert sieve[2161] and 2161%24 == 1
print('Lemma T m=8 counterexample verified')

def three_terms(p, numerator):
    for x in range((p+numerator-1)//numerator, 3*p//numerator+1):
        r = numerator*x-p
        if r <= 0:
            continue
        for y in range(max(x,p*x//r+1),2*p*x//r+1):
            den = r*y-p*x
            num = p*x*y
            if num%den == 0 and num//den >= y:
                return x,y,num//den
    return None

assert three_terms(131,8) is None and three_terms(241,8) is None
assert 4*1*117*1 == 409+59 and 1+117 == 59*2
print('F2 full numerator-8 failures 131,241 and F4 Type II rescue of 409 verified')

# Check the withdrawn trace claim's concrete CRT counterexample.
p = 7183201
mod = 4*721
r = next(x for x in range(mod) if x%412 == p%412 and x%7 == pow(p,-1,7))
assert (r+pow(r,-1,mod)-p-pow(p,-1,mod))%mod == 0
assert (r+19)%mod == 0 or (r*19+1)%mod == 0
assert (p+19)%mod != 0 and (p*19+1)%mod != 0
print('TRACE counterexample at ab=721 verified; CRT residue', r)

# A nonsquare-d algebraic factorisation missed by TYPE-I-FIXED's blanket wording.
# d=4m^2 k^2-2k gives 4dm^2+1=(4m^2 k-1)^2, here m=1,k=6.
p,a,b,c,d,e = 1033,1,45,2,132,23
assert sieve[p] and p%24 == 1 and math.isqrt(d)**2 != d
assert 4*d*a*a+1 == 23**2 and 4*a*b*d == p*e+1 and a+b == e*c
print('TYPE-I-FIXED nonsquare d example:', (p,a,b,c,d,e))

# Bounded attempt to falsify the empirically-empty e=p+2 Type I slice.
# N=(pe+1)/4=((p+1)/2)^2; e/N splits iff f | N^2, f == -N mod e.
tried = 0
for p in range(17,1_000_001,8):
    if not sieve[p]:
        continue
    tried += 1
    e = p+2
    m = (p+1)//2
    n = m*m
    f = next((f for f in divisors_square(m,4) if (f+n)%e == 0), None)
    if f is not None:
        x,y = (f+n)//e,(n*n//f+n)//e
        g = math.gcd(x,y)
        a,b = x//g,y//g
        c,d = (a+b)//e,n//(a*b)
        assert a+b == e*c and 4*a*b*d == p*e+1 and c>0 and d>0
        print('ALG-SLICE e=p+2 first hit', (p,a,b,c,d,e))
        break
else:
    print('ALG-SLICE e=p+2: no hit at',tried,'primes p=1(8), p<=1e6; not a proof')
